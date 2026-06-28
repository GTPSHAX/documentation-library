---
title: std::ranges::take_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/take_view/end
---


```cpp
dcla|num=1|since=c++20|
constexpr auto end() requires (!/*simple-view*/<V>);
dcla|num=2|since=c++20|
constexpr auto end() const requires ranges::range<const V>;
```

Returns a sentinel or an iterator representing the end of the `take_view`. The end of the `take_view` is either one past the `count` element in the underlying range, or the end of the underlying range if the latter has less than `count` elements.
1. Returns a `take_view::/*sentinel*/<false>`, a `std::default_sentinel_t`, or a `ranges::iterator_t<V>`.
2. Returns a `take_view::/*sentinel*/<true>`, a `std::default_sentinel_t`, or a `ranges::iterator_t<const V>`.
Overload  does not participate in overload resolution if `V` is a simple view (that is, if `V` and `const V` are views with the same iterator and sentinel types).

## Parameters

(none)

## Return value

The result depends on the concepts satisfied by possibly const-qualified underlying view type , that is `V` for  or `const V` for .
Let  be the underlying view.


| - |
| rowspan=2 colspan=2 | The underlying view type<br>satisfies ... |
| colspan=2 | lconcept | random_access_range |
| - |
| yes |
| no |
| - |
| rowspan=2 | lconcept | sized_range |
| yes |
| c multi | ranges::begin(base_) + |
| ranges::range_difference_t<Base_>(this->size()) |
| c | std::default_sentinel |
| - |
| no |
| colspan=2 |  |


## Example


### Example

```cpp
#include <iostream>
#include <iterator>
#include <list>
#include <ranges>
#include <type_traits>
namespace ranges = std::ranges;
namespace views = std::views;

int main()
{
    const auto list1 = {3, 1, 4, 1, 5};
    const auto seq1{list1 {{!
```

static_assert(ranges::sized_range<decltype(seq1)> and
ranges::random_access_range<decltype(seq1)> and
std::is_same_v<decltype(seq1.end()), decltype(list1.end())>);
for (auto it = seq1.begin(); it != seq1.end(); ++it)
std::cout << *it << ' ';
std::cout << '\n';
std::list list2{2, 7, 1, 8, 2};
const auto seq2{list2 | views::take(4)};
static_assert(ranges::sized_range<decltype(seq2)> and
not ranges::random_access_range<decltype(seq2)> and
std::is_same_v<decltype(seq2.end()), std::default_sentinel_t>);
for (auto it = seq2.begin(); it != std::default_sentinel; ++it)
std::cout << *it << ' ';
std::cout << '\n';
}
|output=
3 1 4 1
2 7 1 8

## Defect reports


## See also


| cpp/ranges/adaptor/dsc begin|take_view | (see dedicated page) |
| cpp/iterator/dsc counted_iterator | (see dedicated page) |
| cpp/ranges/adaptor/sentinel/dsc operator cmp|take_view | (see dedicated page) |

