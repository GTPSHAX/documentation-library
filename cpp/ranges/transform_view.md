---
title: std::ranges::views::transform
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/transform_view
---


```cpp
**Header:** `<`ranges`>`
dcl rev multi|num=1|since1=c++20|dcl1=
template< ranges::input_range V,
std::copy_constructible F >
requires ranges::view<V> &&
std::is_object_v<F> &&
std::regular_invocable<F&, ranges::range_reference_t<V>> &&
/* invoke_result_t<F&, range_reference_t<V>>& is a valid type */
class transform_view
: public ranges::view_interface<transform_view<V, F>>
|since2=c++23|dcl2=
template< ranges::input_range V,
std::move_constructible F >
requires ranges::view<V> &&
std::is_object_v<F> &&
std::regular_invocable<F&, ranges::range_reference_t<V>> &&
/* invoke_result_t<F&, range_reference_t<V>>& is a valid type */
class transform_view
: public ranges::view_interface<transform_view<V, F>>
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr /*unspecified*/ transform = /*unspecified*/;
}
dcl|since=c++20|
template< ranges::viewable_range R, class F >
requires /* see below */
constexpr ranges::view auto transform( R&& r, F&& fun );
dcl|since=c++20|
template< class F >
constexpr /*range adaptor closure*/ transform( F&& fun );
```

1. A range adaptor that represents  of an underlying sequence after applying a transformation function to each element.
2. *RangeAdaptorObject*. The expression `views::transform(e, f)` is expression-equivalent to `transform_view(e, f)` for any suitable subexpressions `e` and `f`.
`transform_view` models the concepts , , , , , and  when the underlying view `V` models respective concepts.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|transform_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|transform_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|transform_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|transform_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc size|transform_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc reserve_hint|transform_view | (see dedicated page) |


## 


## Nested classes


## Example


### Example

```cpp
#include <algorithm>
#include <cstdio>
#include <iterator>
#include <ranges>
#include <string>

char rot13a(const char x, const char a)
{
    return a + (x - a + 13) % 26;
}

char rot13(const char x)
{
    if ('Z' >= x and x >= 'A')
        return rot13a(x, 'A');

    if ('z' >= x and x >= 'a')
        return rot13a(x, 'a');

    return x;
}

int main()
{
    auto show = [](const unsigned char x) { std::putchar(x); };

    std::string in{"cppreference.com\n"};
    std::ranges::for_each(in, show);
    std::ranges::for_each(in {{!
```

std::string out;
std::ranges::copy(std::views::transform(in, rot13), std::back_inserter(out));
std::ranges::for_each(out, show);
std::ranges::for_each(out | std::views::transform(rot13), show);
}
|output=
cppreference.com
pccersrerapr.pbz
pccersrerapr.pbz
cppreference.com

## See also


| cpp/algorithm/ranges/dsc transform | (see dedicated page) |

