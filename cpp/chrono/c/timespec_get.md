---
title: std::timespec_get
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/c/timespec_get
---


```cpp
**Header:** `<`ctime`>`
dcl|num=1|since=c++17|
int timespec_get( std::timespec* ts, int base );
dcl|num=2|since=c++17|
#define TIME_UTC /* implementation-defined */
```

1. Modifies the `std::timespec` object pointed to by `ts` to hold the current calendar time in the time base `base`.
2. Expands to a value suitable for use as the `base` argument of `std::timespec_get`.
Other macro constants beginning with `TIME_` may be provided by the implementation to indicate additional time bases.
If `base` is `TIME_UTC`, then
* `ts->tv_sec` is set to the number of seconds since an implementation defined epoch, truncated to a whole value,
* `ts->tv_nsec` member is set to the integral number of nanoseconds, rounded to the resolution of the system clock.

## Parameters


### Parameters

- `ts` - pointer to an object of type `std::timespec`
- `base` - `TIME_UTC` or another nonzero integer value indicating the time base

## Return value

The value of `base` if successful, zero otherwise.

## Notes

The POSIX function [https://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_getres.html `clock_gettime(CLOCK_REALTIME, ts)`] may also be used to populate a `std::timespec` with the time since the Epoch.

## Example


### Example

```cpp
#include <ctime>
#include <iostream>

int main()
{
    std::timespec ts;
    std::timespec_get(&ts, TIME_UTC);
    char buf[100];
    std::strftime(buf, sizeof buf, "%D %T", std::gmtime(&ts.tv_sec));
    std::cout << "Current time: " << buf << '.' << ts.tv_nsec << " UTC\n";
}
```


**Output:**
```
Current time: 06/24/16 20:07:42.949494132 UTC
```


## See also


| cpp/chrono/c/dsc timespec | (see dedicated page) |
| cpp/chrono/c/dsc time | (see dedicated page) |

