---
title: std::localtime
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/c/localtime
---


```cpp
**Header:** `<`ctime`>`
dcl|num=1|
std::tm* localtime  ( const std::time_t* time );
dcl|num=2|since=c++26|
std::tm* localtime_r( const std::time_t* time, std::tm* buf );
```

Converts given time since epoch as `std::time_t` value into calendar time, expressed in local time.
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
`std::localtime` may not be thread-safe.
POSIX requires that this function sets `errno` to `EOVERFLOW` if it fails because the argument is too large.
[https://pubs.opengroup.org/onlinepubs/9699919799/functions/localtime.html POSIX specifies] that the timezone information is determined by this function as if by calling [https://pubs.opengroup.org/onlinepubs/9699919799/functions/tzset.html `tzset`], which reads the environment variable `TZ`.

## Example


### Example

```cpp
#include <ctime>
#include <iomanip>
#include <iostream>
#include <sstream>

int main()
{
    setenv("TZ", "/usr/share/zoneinfo/America/Los_Angeles", 1); // POSIX-specific

    std::tm tm{}; // Zero initialise
    tm.tm_year = 2020 - 1900; // 2020
    tm.tm_mon = 2 - 1; // February
    tm.tm_mday = 15; // 15th
    tm.tm_hour = 10;
    tm.tm_min = 15;
    tm.tm_isdst = 0; // Not daylight saving
    std::time_t t = std::mktime(&tm); 

    std::cout << "UTC:   " << std::put_time(std::gmtime(&t), "%c %Z") << '\n';
    std::cout << "local: " << std::put_time(std::localtime(&t), "%c %Z") << '\n';
}
```


**Output:**
```
UTC:   Sat Feb 15 18:15:00 2020 GMT
local: Sat Feb 15 10:15:00 2020 PST
```


## See also


| cpp/chrono/c/dsc gmtime | (see dedicated page) |
| c/chrono/dsc localtime | (see dedicated page) |

