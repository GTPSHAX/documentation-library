---
title: std::formatter<std::chrono::hh_mm_ss>
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/hh_mm_ss/formatter
---


# formattersmall|<std::chrono::hh_mm_ss>

ddcl|header=chrono|since=c++20|
template< class CharT >
struct formatter<std::chrono::hh_mm_ss, CharT>;
Specialization of `std::formatter` that defines formatting rules for a `std::chrono::hh_mm_ss`.
The `std::formatter` specialization is usually not directly accessed, but is used through formatting functions.

## Format specification


## Example


### Example

```cpp
#include <chrono>
#include <format>
#include <iostream>
using namespace std::literals;

int main()
{
    std::chrono::hh_mm_ss c{16h + 32min + 10s};

    std::cout << "%R: " << std::format("{:%R}", c) << '\n'
              << "%T: " << std::format("{:%T}", c) << '\n';
}
```


**Output:**
```
%R: 16:32
%T: 16:32:10
```


## Defect reports


## See also


| cpp/utility/format/dsc format | (see dedicated page) |

