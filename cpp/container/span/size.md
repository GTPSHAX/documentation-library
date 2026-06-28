---
title: std::span::size
type: Containers
source: https://en.cppreference.com/w/cpp/container/span/size
---

ddcl|since=c++20|
constexpr size_type size() const noexcept;
Returns the number of elements in the span.

## Return value

The number of elements in the span.

## Note


## Example


### Example

```cpp
#include <span>

int main()
{
    constexpr static int c_array[]{1, 2, 3, 4, 5, 6, 7, 8};

    constexpr std::span<const int> span{c_array};

    static_assert(8 == span.size());
    static_assert(7 == span.first(7).size());
    static_assert(6 == span.first<6>().size());
    static_assert(5 == span.last(5).size());
    static_assert(4 == span.last<4>().size());
    static_assert(3 == span.subspan(2, 3).size());
    static_assert(2 == span.subspan<3, 2>().size());
    static_assert(1 == span.subspan<7>().size());
}
```


## See also


| cpp/container/span/dsc constructor | (see dedicated page) |
| cpp/container/span/dsc size_bytes | (see dedicated page) |

