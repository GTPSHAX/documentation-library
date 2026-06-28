---
title: std::span::subspan
type: Containers
source: https://en.cppreference.com/w/cpp/container/span/subspan
---


```cpp
dcl|since=c++20|num=1|1=
template< std::size_t Offset,
std::size_t Count = std::dynamic_extent >
constexpr std::span<element_type, /* see below */>
subspan() const;
dcl|since=c++20|num=2|1=
constexpr std::span<element_type, std::dynamic_extent>
subspan( size_type offset,
size_type count = std::dynamic_extent ) const;
```

Obtains a subview over some consecutive elements of this span, the elements to be included are determined by an element count and an offset.
1. The element count and offset are provided as template arguments, and the subview has a dynamic extent only if both `Count` and `Offset` are `std::dynamic_extent`.
* If `Count` is `std::dynamic_extent`, the subview contains all elements starting from the `Offset`.
* Otherwise, the subview contains `Count` elements starting from the `Offset`.
@@ Denote the second template argument of the return type as `FinalExtent`, it is defined as c multi
|Count ! std::dynamic_extent
|    ? Count
|    : (Extent ! std::dynamic_extent
|        ? Extent - Offset
|        : std::dynamic_extent)
.
@@ .
@@
2. The element count and offset are provided as function arguments, and the subview always has a dynamic extent.
* If `count` is `std::dynamic_extent`, the subview contains all elements starting from the `offset`.
* Otherwise, the subview contains `count` elements starting from the `offset`.
@@

## Return value

1.
2.

## Example


### Example

```cpp
#include <algorithm>
#include <cstdio>
#include <numeric>
#include <ranges>
#include <span>

void display(std::span<const char> abc)
{
    const auto columns{20U};
    const auto rows{abc.size() - columns + 1};

    for (auto offset{0U}; offset < rows; ++offset)
    {
        std::ranges::for_each(abc.subspan(offset, columns), std::putchar);
        std::puts("");
    }
}

int main()
{
    char abc[26];
    std::ranges::iota(abc, 'A');
    display(abc);
}
```


**Output:**
```
ABCDEFGHIJKLMNOPQRST
BCDEFGHIJKLMNOPQRSTU
CDEFGHIJKLMNOPQRSTUV
DEFGHIJKLMNOPQRSTUVW
EFGHIJKLMNOPQRSTUVWX
FGHIJKLMNOPQRSTUVWXY
GHIJKLMNOPQRSTUVWXYZ
```


## See also


| cpp/container/span/dsc first | (see dedicated page) |
| cpp/container/span/dsc last | (see dedicated page) |

