---
title: std::timespec
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/c/timespec
---

ddcl|header=ctime|since=c++17|
struct timespec;
Structure holding an interval broken down into seconds and nanoseconds.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |

The declaration order of `tv_sec` and `tv_nsec` is unspecified. Implementation may add other data members to `timespec`.

## Notes

The type of `tv_nsec` is `long long` on some platforms, which is currently non-conforming in C++, but is allowed in C since C23.

## Example


### Example

```cpp
#include <ctime>
#include <iostream>

int main()
{
    std::timespec ts;
    std::timespec_get(&ts, TIME_UTC);
    char buff[0x80];
    std::strftime(buff, sizeof buff, "%D %T", std::gmtime(&ts.tv_sec));

//  auto [sec, nsec] = ts; // UB: structured bindings should not be used because the
                           // declaration order and data member list are unspecified

    std::cout << "Current time: " << buff << " (UTC)\n"
              << "Raw timespec.tv_sec: " << ts.tv_sec << '\n'
              << "Raw timespec.tv_nsec: " << ts.tv_nsec << '\n';
}
```


**Output:**
```
Current time: 04/06/23 12:03:31 (UTC)
Raw timespec.tv_sec: 1680782611
Raw timespec.tv_nsec: 678437213
```


## See also


| cpp/chrono/c/dsc timespec_get | (see dedicated page) |
| cpp/chrono/c/dsc tm | (see dedicated page) |

