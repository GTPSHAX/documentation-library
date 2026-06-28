---
title: std::chrono::year_month_day_last::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_day_last/operator_arith
---


## Example


### Example

```cpp
#include <cassert>
#include <chrono>

int main()
{
    auto ymdl{11/std::chrono::last/2020};

    ymdl += std::chrono::years(15);
    assert(ymdl.day() == std::chrono::day(30));
    assert(ymdl.month() == std::chrono::November);
    assert(ymdl.year() == std::chrono::year(2035));

    ymdl -= std::chrono::months(6);
    assert(ymdl.day() == std::chrono::day(31));
    assert(ymdl.month() == std::chrono::May);
    assert(ymdl.year() == std::chrono::year(2035));
}
```


## See also


| {{BASEPAGENAMEE | (see dedicated page) |

