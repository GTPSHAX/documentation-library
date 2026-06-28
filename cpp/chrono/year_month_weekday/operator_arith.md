---
title: std::chrono::year_month_weekday::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_weekday/operator_arith
---


## Example


### Example

```cpp
#include <cassert>
#include <chrono>
#include <iostream>

int main()
{
    auto ymwi{1/std::chrono::Wednesday[2]/2021};
    std::cout << ymwi << '\n';

    ymwi += std::chrono::years(5);
    std::cout << ymwi << '\n';
    assert(static_cast<std::chrono::year_month_day>(ymwi) ==
                       std::chrono::year(2026)/1/14);

    ymwi -= std::chrono::months(1);
    std::cout << ymwi << '\n';
    assert(static_cast<std::chrono::year_month_day>(ymwi) == 
                       std::chrono::day(10)/12/2025);
}
```


**Output:**
```
2021/Jan/Wed[2]
2026/Jan/Wed[2]
2025/Dec/Wed[2]
```


## See also


| {{BASEPAGENAMEE | (see dedicated page) |

