---
title: std::ranges::views::lazy_split
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/lazy_split_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< ranges::input_range V, ranges::forward_range Pattern >
requires ranges::view<V> &&
ranges::view<Pattern> &&
std::indirectly_comparable<ranges::iterator_t<V>,
ranges::iterator_t<Pattern>,
ranges::equal_to> &&
(ranges::forward_range<V>  /*tiny-range*/<Pattern>)
class lazy_split_view
: public ranges::view_interface<lazy_split_view<V, Pattern>>
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr /* unspecified */ lazy_split = /* unspecified */;
}
dcl|since=c++20|1=
template< ranges::viewable_range R, class Pattern >
requires /* see below */
constexpr ranges::view auto lazy_split( R&& r, Pattern&& pattern );
dcl|since=c++20|1=
template< class Pattern >
constexpr /* range adaptor closure */ lazy_split( Pattern&& pattern );
|1=
template< class R >
concept /*tiny-range*/ =
ranges::sized_range<R> &&
requires { /* is-statically-constexpr-sized */<R>; } &&
(std::remove_reference_t<R>::size() <= 1);
```

1. `lazy_split_view` takes a  and a delimiter, and splits the  into subranges on the delimiter.
Two major scenarios are supported:
* The view is an , the delimiter is a single element (wrapped in a `single_view`).
* The view is a , the delimiter is a  of elements.
2. A *RangeAdaptorObject*. The expression `views::lazy_split(e, f)` is expression-equivalent to `lazy_split_view(e, f)`.
3. The exposition-only concept `/*tiny-range*/<Pattern>` is satisfied if `Pattern` satisfies , `Pattern::size()` is a constant expression and suitable as a template non-type argument, and the value of `Pattern::size()` is less than or equal to `1`. Notably, `empty_view` and `single_view` satisfy this concept.
`lazy_split_view` models the concepts  and  when the underlying  `V` models respective concepts, and models  when `V` models both  and .
The inner range (`ranges::range_reference_t<lazy_split_view>`) models the concepts  and  when the underlying  `V` models respective concepts. It does not model , and cannot be used with algorithms that expect a  or higher.
Unlike `split_view`, `lazy_split_view` does not maintain the continuity of the subrange.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |
| dsc expos mem obj|pattern_|id=pattern|private=yes | |
| |spec=`Pattern`|the pattern that is used as a delimiter to split the underlying | |
| dsc expos mem obj|current_|id=current|private=yes | |
| |maybe=(present only if `V` does not satisfy ) | |
| |spec=`<ranges::iterator_t<V>>` | |
| |an object that caches the result of calls to | |


## Member functions


| cpp/ranges/adaptor/dsc constructor|lazy_split_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|lazy_split_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|lazy_split_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|lazy_split_view | (see dedicated page) |


## Nested classes


## 


## Notes

The name `lazy_split_view` is introduced by the post-C++20 defect report `P2210R2`. It has the same lazy mechanism as that of the old `split_view` before change.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <ranges>
#include <string_view>

auto print = [](auto const& view)
{
    // `view` is of std::views::lazy_split_view::__outer_iterator::value_type

    for (std::cout << "{ "; const auto element : view)
        std::cout << element << ' ';
    std::cout << "} ";
};

int main()
{
    constexpr static auto source = {0, 1, 0, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9};
    constexpr int delimiter{0};
    constexpr std::ranges::lazy_split_view outer_view{source, delimiter};
    std::cout << "splits[" << std::ranges::distance(outer_view) << "]:  ";
    for (auto const& inner_view: outer_view)
        print(inner_view);

    constexpr std::string_view hello{"Hello C++ 20 !"};
    std::cout << "\n" "substrings: ";
    std::ranges::for_each(hello {{!
```

constexpr std::string_view text{"Hello-+-C++-+-20-+-!"};
constexpr std::string_view delim{"-+-"};
std::cout << "\n" "substrings: ";
std::ranges::for_each(text | std::views::lazy_split(delim), print);
}
|output=
splits[5]:  { } { 1 } { 2 3 } { 4 5 6 } { 7 8 9 }
substrings: { H e l l o } { C + + } { 2 0 } { ! }
substrings: { H e l l o } { C + + } { 2 0 } { ! }

## Defect reports


## See also


| cpp/ranges/dsc split_view | (see dedicated page) |
| cpp/ranges/dsc join_view | (see dedicated page) |

