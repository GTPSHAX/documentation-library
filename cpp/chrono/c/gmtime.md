---
title: std::gmtime
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/c/gmtime
---


```cpp
**Header:** `<`ctime`>`
dcl|num=1|
std::tm* gmtime  ( const std::time_t* time );
dcl|num=2|since=c++26|
std::tm* gmtime_r( const std::time_t* time, std::tm* buf );
```

Converts given time since epoch as `std::time_t` value into calendar time, expressed in Coordinated Universal Time (UTC).
1. Upon successfull conversion, the result is stored in an internal `std::tm` object shared between `std::gmtime`, `std::localtime`, and `std::ctime` and may be overwritten on each invocation.
rrev|since=c++11|
.
2. Upon successfull conversion, the result is stored in the `std::tm` object pointed to by `buf`.

## Parameters


### Parameters

- `time` - pointer to a `std::time_t` object to convert

## Return value

1. A pointer to the shared internal `std::tm` object on success, or a null pointer on error.
2. `buf` on success, or a null pointer on error.

## Notes

rrev|since=c++11|
`std::gmtime` may not be thread-safe.
POSIX requires that this function sets `errno` to `EOVERFLOW` if it fails because the argument is too large.

## Example


### Example

```cpp
#include <ctime>
#include <iomanip>
#include <iostream>
#include <sstream>

int main()
{
    setenv("TZ", "/usr/share/zoneinfo/Europe/London", 1); // POSIX-specific

    std::tm tm{}; // get_time does not set all fields hence {}
    tm.tm_year = 2020 - 1900; // 2020
    tm.tm_mon = 7 - 1; // July
    tm.tm_mday = 15; // 15th
    tm.tm_hour = 10;
    tm.tm_min = 15;
    tm.tm_isdst = 1; // Daylight saving in London
    std::time_t t = std::mktime(&tm); 

    std::cout << "UTC:   " << std::put_time(std::gmtime(&t), "%c %Z") << '\n';
    std::cout << "local: " << std::put_time(std::localtime(&t), "%c %Z") << '\n';
}
```


**Output:**
```
UTC:   Wed Jul 15 09:15:00 2020 GMT
local: Wed Jul 15 10:15:00 2020 BST
```


## See also


| cpp/chrono/c/dsc localtime | (see dedicated page) |

