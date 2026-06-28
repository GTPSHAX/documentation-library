---
title: std::formatter<std::chrono::duration>
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/formatter
---


# formattersmall|<std::chrono::duration>

ddcl|header=chrono|1=
template< class Rep, class Period, class CharT >
struct formatter<std::chrono::duration<Rep, Period>, CharT>;
Specialization of `std::formatter` that defines formatting rules for a `std::chrono::duration`. The `duration` is interpreted as the time of day since midnight.
The `std::formatter` specialization is usually not directly accessed, but is used through formatting functions.

## Format specification


## Example


### Example

```cpp
#include <chrono>
#include <print>
using namespace std::chrono_literals;

int main()
{
    auto du{3h + 2min + 1s};

    std::print(
        "Duration is:\n"
        "{}\n"
        "{:%T}\n"
        "{:%H:%M:%S}\n"
        "{:%H hours %M minutes %S seconds}\n",
        du, du, du, du);
}
```


**Output:**
```
Duration is:
10921s
03:02:01
03:02:01
03 hours 02 minutes 01 seconds
```


## See also


| cpp/utility/format/dsc format | (see dedicated page) |

