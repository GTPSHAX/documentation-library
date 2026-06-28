---
title: std::chrono::year_month::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month/operator_arith
---


## Example


### Example

```cpp
#include <cassert>
#include <chrono>

int main()
{
    auto ym{std::chrono::day(1)/7/2023};

    ym -= std::chrono::years{2};
    assert(ym.month() == std::chrono::July);
    assert(ym.year() == std::chrono::year(2021));

    ym += std::chrono::months{7};
    assert(ym.month() == std::chrono::month(2));
    assert(ym.year() == std::chrono::year(2022));
}
```


## See also


| {{BASEPAGENAMEE | (see dedicated page) |

