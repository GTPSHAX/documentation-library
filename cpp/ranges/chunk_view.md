---
title: std::ranges::views::chunk
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view
---


```cpp
**Header:** `<`ranges`>`
dcla|num=1|since=c++23|1=
template< ranges::view V >
requires ranges::input_range<V>
class chunk_view
: public ranges::view_interface<chunk_view<V>>
dcla|num=2|since=c++23|1=
template< ranges::view V >
requires ranges::forward_range<V>
class chunk_view<V>
: public ranges::view_interface<chunk_view<V>>
dcl|num=3|since=c++23|1=
namespace views {
inline constexpr /* unspecified */ chunk = /* unspecified */;
}
dcl|since=c++23|1=
template< ranges::viewable_range R >
constexpr ranges::view auto chunk( R&& r, ranges::range_difference_t<R> n );
dcl|since=c++23|1=
template< class DifferenceType >
constexpr /*range adaptor closure*/ chunk( DifferenceType&& n );
dcla|anchor=div-ceil|num=4|notes=|1=
template< class I >
constexpr I /*div-ceil*/( I num, I denom );
```

`chunk_view` takes a  and a number `n` and produces a range of views (the ) of the original view, such that each , except maybe the last one, has the size `n`. These ''chunks'' are non-overlapping, successive sub-ranges of the elements of the original view, in order.
Let  be the size of the original view. If  is not the multiple of `n`, the size of the ''last'' produced view is exactly `s % n` (the remainder). Otherwise, the size of each , including the last one, is `n`.
The size of produced view is `/*div-ceil*/(s)`.
If the `n` is not greater than `0` the behavior is undefined.
1. An implementation that supports the underlying view `V` that models only .
2. A partial specialization that supports the underlying view `V` that models  or stronger. Models  if the underlying view `V` is , , and either  or non .
3. The name `views::chunk` denotes a *RangeAdaptorObject*. Given subexpressions `e` and `n`, the expression `views::chunk(e, n)` is expression-equivalent to `chunk_view(e, n)`.
4. Computes the smallest integer value that is not less than the quotient of dividing `num` by `denom`. Equivalent to:

```cpp
I r = num / denom;
if (num % denom)
    ++r;
return r;
```


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |

#### If {{tt|V


## Member functions


| cpp/ranges/adaptor/dsc constructor|chunk_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|chunk_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|chunk_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|chunk_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc size|chunk_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc reserve_hint|chunk_view | (see dedicated page) |


## 


## Nested classes


## Helper templates

ddcl|since=c++23|1=
template< class V >
constexpr bool ranges::enable_borrowed_range<chunk_view<V>> =
ranges::forward_range<V> && ranges::enable_borrowed_range<V>;
This specialization of `ranges::enable_borrowed_range` makes `chunk_view` satisfy  when the underlying view `V` satisfies both, the  and the .

## Notes

If `V` models  , `chunk_view`'s iterator has a dedicated type:  that is itself an input view.
If `V` models  or stronger , `chunk_view` defers to `views::take` for its `value_type`.
If `V` models  or stronger ranges , the need to calculate size the last chunk correctly (from the end ) requires the underlying range type `V` to be .

## Example


### Example

```cpp
#include <algorithm>
#include <initializer_list>
#include <iostream>
#include <ranges>

auto print_subrange = [](std::ranges::viewable_range auto&& r)
{
    std::cout << '[';
    for (int pos{}; auto elem : r)
        std::cout << (pos++ ? " " : "") << elem;
    std::cout << "] ";
};

int main()
{
    const auto v = {1, 2, 3, 4, 5, 6};

    for (const unsigned width : std::views::iota(1U, 2U + v.size()))
    {
        auto const chunks = v {{!
```

std::cout << "chunk(" << width << "): ";
std::ranges::for_each(chunks, print_subrange);
std::cout << '\n';
}
}
|output=
chunk(1): [1] [2] [3] [4] [5] [6]
chunk(2): [1 2] [3 4] [5 6]
chunk(3): [1 2 3] [4 5 6]
chunk(4): [1 2 3 4] [5 6]
chunk(5): [1 2 3 4 5] [6]
chunk(6): [1 2 3 4 5 6]
chunk(7): [1 2 3 4 5 6]

## References


## See also


| cpp/ranges/dsc chunk_by_view | (see dedicated page) |
| cpp/ranges/dsc adjacent_view | (see dedicated page) |
| cpp/ranges/dsc slide_view | (see dedicated page) |

