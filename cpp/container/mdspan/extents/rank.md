---
title: std::extents::rank
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/extents/rank
---

ddcl|since=c++23|
static constexpr rank_type rank() noexcept;
Returns the number of dimensions in `extents`.

## Return value

The number of dimensions.

## Example


### Example

```cpp
#include <iostream>
#include <mdspan>

int main()
{
    std::extents<int, 1, 2> e1;
    std::extents<int, 3, 4, std::dynamic_extent> e2(5);
    std::cout << e1.rank() << ", " << e2.rank() << '\n';
}
```


**Output:**
```
2, 3
```


## See also


| cpp/container/mdspan/extents/dsc rank_dynamic | (see dedicated page) |
| cpp/types/dsc rank | (see dedicated page) |

