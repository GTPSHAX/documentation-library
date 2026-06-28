---
title: std::chrono::year_month_weekday_last::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_weekday_last/operator_arith
---


## Example


### Example

```cpp
#include <chrono>
#include <iostream>
using namespace std::chrono;

int main()
{
    auto ymwdl{August/Friday[last]/2022};
    std::cout << year_month_day{ymwdl} << '\n';
    ymwdl += months(2);
    std::cout << year_month_day{ymwdl} << '\n';
    ymwdl -= years(1); 
    std::cout << year_month_day{ymwdl} << '\n';
}
```


**Output:**
```
2022-08-26
2022-10-28
2021-10-29
```


## See also


| {{BASEPAGENAMEE | (see dedicated page) |

