---
title: std::ranges::stride_view::size
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/size
---


```cpp
dcl|since=c++23|
constexpr auto size() requires ranges::sized_range<V>;
dcl|since=c++23|
constexpr auto size() const requires ranges::sized_range<const V>;
```

Returns the number of elements.
Let  be the underlying view and  be the stored stride value. Equivalent to:

```cpp
return /*to-unsigned-like*/(/*div-ceil*/(ranges::distance(base_), stride_));
```


## Parameters

(none)

## Return value

The number of elements. The returned value is calculated as if by expression
`(ranges::size(base_) / stride_) + ((ranges::size(base_) % stride_ ? 1 : 0)`.

## Example


### Example

```cpp
#include <forward_list>
#include <ranges>

int main()
{
    namespace vs = std::views;
    constexpr static auto v = {1, 2, 3, 4, 5};
    static_assert
    (
        vs::stride(v, 1).size() == 5 and
        vs::stride(v, 2).size() == 3 and
        vs::stride(v, 3).size() == 2 and
        vs::stride(v, 4).size() == 2 and
        vs::stride(v, 5).size() == 1 and
        vs::stride(v, 6).size() == 1
    );

    std::forward_list list{v};
//  auto s = vs::stride(list, 2).size(); // Error: not a sized_range
}
```


## See also


| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc ssize | (see dedicated page) |

