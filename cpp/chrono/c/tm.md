---
title: std::tm
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/c/tm
---

ddcl|header=ctime|
struct tm;
Structure holding a calendar date and time broken down into its components.

## Member objects

<references group="note"/>

## Notes

BSD, GNU and musl C library support two additional members, which are standardized in [https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/time.h.html POSIX.1-2024].

## Example


### Example

```cpp
#include <ctime>
#include <iostream>

int main()
{
    std::tm tm{};
    tm.tm_year = 2022 - 1900;
    tm.tm_mday = 1;
    std::mktime(&tm);

    std::cout << std::asctime(&tm); // note implicit trailing '\n'
}
```


**Output:**
```
Sat Jan  1 00:00:00 2022
```


## See also


| cpp/chrono/c/dsc localtime | (see dedicated page) |
| cpp/chrono/c/dsc gmtime | (see dedicated page) |

