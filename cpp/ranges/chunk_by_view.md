---
title: std::ranges::views::chunk_by
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_by_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++23|1=
template< ranges::forward_range V, std::indirect_binary_predicate<iterator_t<V>,
ranges::iterator_t<V>> Pred >
requires ranges::view<V> && std::is_object_v<Pred>
class chunk_by_view
: public ranges::view_interface<chunk_by_view<V, Pred>>
dcl|num=2|since=c++23|1=
namespace views {
inline constexpr /* unspecified */ chunk_by = /* unspecified */ ;
}
dcl|since=c++23|1=
template< ranges::viewable_range R, class Pred >
requires /* see below */
constexpr ranges::view auto chunk_by( R&& r, Pred&& pred );
dcl|since=c++23|1=
template< class Pred >
constexpr /*range adaptor closure*/ chunk_by( Pred&& pred );
```

1. `chunk_by_view` is a range adaptor that takes a  and an invocable object `pred` (the binary predicate), and produces a  of subranges (chunks), by splitting the underlying view between each pair of adjacent elements for which `pred` returns `false`. The first element of each such pair belongs to the previous chunk, and the second element belongs to the next chunk.
2. The name `views::chunk_by` denotes a *RangeAdaptorObject*. Given a subexpression `e` and `f`, the expression `views::chunk_by(e, f)` is expression-equivalent to `chunk_by_view(e, f)`.
`chunk_by_view` always models , and models  and/or , if adapted  type models the corresponding concepts.
`chunk_by_view` never models  or .

## Data members


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Member functions


| cpp/ranges/adaptor/dsc constructor|chunk_by_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|chunk_by_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc pred|chunk_by_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|chunk_by_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|chunk_by_view | (see dedicated page) |


## 


## Nested classes


## Notes

In order to provide the amortized constant time complexity required by the  concept, the result of  is cached within the `chunk_by_view` object. If the underlying range is modified after the first call to , subsequent uses of the `chunk_by_view` object might have unintuitive behavior.

## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <ranges>
#include <string_view>

void print_chunks(auto view, std::string_view separator = ", ")
{
    for (auto const subrange : view)
    {
        std::cout << '[';
        for (std::string_view prefix; auto const& elem : subrange)
            std::cout << prefix << elem, prefix = separator;
        std::cout << "] ";
    }
    std::cout << '\n';
}

int main()
{
    std::initializer_list v1 = {1, 2, 3, 1, 2, 3, 3, 3, 1, 2, 3};
    auto fn1 = std::ranges::less{};
    auto view1 = v1 {{!
```

print_chunks(view1);
std::initializer_list v2 = {1, 2, 3, 4, 4, 0, 2, 3, 3, 3, 2, 1};
auto fn2 = std::ranges::not_equal_to{};
auto view2 = v2 | std::views::chunk_by(fn2);
print_chunks(view2);
std::string_view v3 = "__cpp_lib_ranges_chunk_by";
auto fn3 = [](auto x, auto y) { return not(x == '_' or y == '_'); };
auto view3 = v3 | std::views::chunk_by(fn3);
print_chunks(view3, "");
std::string_view v4 = "\u007a\u00df\u6c34\u{1f34c}"; // "zß水🍌"
auto fn4 = [](auto, auto ß) { return 128 == ((128 + 64) & ß); };
auto view4 = v4 | std::views::chunk_by(fn4);
print_chunks(view4, "");
}
|output=
[1, 2, 3] [1, 2, 3] [3] [3] [1, 2, 3]
[1, 2, 3, 4] [4, 0, 2, 3] [3] [3, 2, 1]
[_] [_] [cpp] [_] [lib] [_] [ranges] [_] [chunk] [_] [by]
[z] [ß] [水] [🍌]

## References


## See also


| cpp/ranges/dsc chunk_view | (see dedicated page) |
| cpp/ranges/dsc slide_view | (see dedicated page) |
| cpp/ranges/dsc stride_view | (see dedicated page) |

