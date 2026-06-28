---
title: std::formatter<std::chrono::month_day>
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_day/formatter
---


# formattersmall|<std::chrono::month_day>

ddcl|header=chrono|since=c++20|
template< class CharT >
struct formatter<std::chrono::month_day, CharT>;
Specialization of `std::formatter` that defines formatting rules for `std::chrono::month_day`.
The `std::formatter` specialization is usually not directly accessed, but is used through formatting functions.

## Format specification


## Example


### Example

```cpp
#include <chrono>
#include <format>
#include <iostream>

int main()
{
    using namespace std::chrono_literals;
    constexpr std::chrono::month_day md{std::chrono::February / 29d};

    std::cout << "%B: " << std::format("{:%B}", md) << '\n'
              << "%d: " << std::format("{:%d}", md) << '\n';
}
```


**Output:**
```
%B: February
%d: 29
```


## Defect reports


## See also


| cpp/utility/format/dsc format | (see dedicated page) |

