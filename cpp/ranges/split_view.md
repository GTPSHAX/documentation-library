---
title: std::ranges::views::split
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/split_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< ranges::forward_range V, ranges::forward_range Pattern >
requires ranges::view<V> &&
ranges::view<Pattern> &&
std::indirectly_comparable<ranges::iterator_t<V>,
ranges::iterator_t<Pattern>,
ranges::equal_to>
class split_view
: public ranges::view_interface<split_view<V, Pattern>>
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr /* unspecified */ split = /* unspecified */;
}
dcl|since=c++20|1=
template< ranges::viewable_range R, class Pattern >
requires /* see below */
constexpr ranges::view auto split( R&& r, Pattern&& pattern );
dcl|since=c++20|1=
template< class Pattern >
constexpr /* range adaptor closure */ split( Pattern&& pattern );
```

1. `split_view` takes a  and a delimiter, and splits the  into subranges on the delimiter.
2. *RangeAdaptorObject*. The expression `views::split(e, p)` is expression-equivalent to `split_view(e, p)` for any suitable subexpressions `e` and `p`.
`split_view` models the concepts , and  when the underlying  `V` models respective concepts.
The inner range (`ranges::range_reference_t<split_view>`) is a `ranges::subrange<ranges::iterator_t<V>>`, which models , models  when `ranges::iterator_t<V>` models `std::sized_sentinel_for<ranges::iterator_t<V>>`, and models , , , and  when `V` models respective concepts.
Unlike `lazy_split_view`, `split_view` maintains the continuity of the subrange, making it suitable for string splitting.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|split_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|split_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|split_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|split_view | (see dedicated page) |


## Nested classes


## 


## Notes

Before `P2210R2`, `split_view` used a ''lazy'' mechanism for splitting, and thus could not keep the bidirectional, random access, or contiguous properties of the underlying view, or make the iterator type of the inner range same as that of the underlying view. Consequently, it is redesigned by `P2210R2`, and the lazy mechanism is moved to `lazy_split_view`.
The delimiter `pattern` generally should not be an ordinary string literal, as it will consider the null terminator to be necessary part of the delimiter; therefore, it is advisable to use a `std::string_view` literal instead.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <ranges>
#include <string_view>

int main()
{
    using std::operator""sv;
    constexpr auto words{"Hello^_^C++^_^20^_^!"sv};
    constexpr auto delim{"^_^"sv};

    for (const auto word : std::views::split(words, delim))
        // with string_view's C++23 range constructor:
        std::cout << std::quoted(std::string_view(word)) << ' ';
    std::cout << '\n';
}
```


**Output:**
```
"Hello" "C++" "20" "!"
```


## Defect reports


## See also


| cpp/ranges/dsc lazy_split_view | (see dedicated page) |
| cpp/ranges/dsc join_view | (see dedicated page) |

