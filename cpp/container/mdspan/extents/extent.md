---
title: std::extents::extent
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/extents/extent
---

ddcl|since=c++23|
constexpr index_type extent( rank_type i ) const noexcept;
Returns dynamic extent size of an `extents` at a certain rank index.

## Parameters


### Parameters

- `i` - The rank index to get the extent size of

## Return value

The dynamic extent size of an `extents` at a certain rank index.

## Example


### Example

```cpp
#include <iostream>
#include <mdspan>

int main()
{
    std::extents<int, 1, 2> e1;
    std::extents<int, 3, std::dynamic_extent, std::dynamic_extent> e2(4, 5);
    std::cout << e1.extent(0) << ", " << e1.extent(1) << '\n';
    std::cout << e2.extent(0) << ", " << e2.extent(1) << ", " << e2.extent(2) << '\n';
}
```


**Output:**
```
1, 2
3, 4, 5
```


## See also


| cpp/container/mdspan/extents/dsc static_extent | (see dedicated page) |
| cpp/types/dsc extent | (see dedicated page) |

