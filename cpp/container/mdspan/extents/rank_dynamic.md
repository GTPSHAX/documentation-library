---
title: std::extents::rank_dynamic
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/extents/rank_dynamic
---

ddcl|since=c++23|
static constexpr rank_type rank_dynamic() noexcept;
Returns the number of dynamic dimensions in `extents`.

## Return value

The number of dynamic dimensions.

## Example


### Example

```cpp
#include <iostream>
#include <mdspan>

int main()
{
    std::extents<int, 1, 2> e1;
    std::extents<int, 3, 4, std::dynamic_extent> e2(5);
    std::extents<int, std::dynamic_extent, 7, std::dynamic_extent> e3(6, 8);
    std::cout << e1.rank_dynamic() << ", "
              << e2.rank_dynamic() << ", "
              << e3.rank_dynamic() << '\n';
}
```


**Output:**
```
0, 1, 2
```


## See also


| cpp/container/mdspan/extents/dsc rank | (see dedicated page) |
| cpp/types/dsc rank | (see dedicated page) |

