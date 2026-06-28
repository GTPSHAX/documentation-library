---
title: std::ranges::take_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/take_view/begin
---


```cpp
dcla|num=1|since=c++20|
constexpr auto begin() requires (!/*simple-view*/<V>);
dcla|num=2|since=c++20|
constexpr auto begin() const requires ranges::range<const V>;
```

Returns an iterator to the first element of the `take_view`.
1. Returns a `std::counted_iterator` or a `ranges::iterator_t<V>`.
2. Returns a `std::counted_iterator` or a `ranges::iterator_t<const V>`.
Overload  does not participate in overload resolution if `V` is a simple view (that is, if `V` and `const V` are views with the same iterator and sentinel types).

## Parameters

(none)

## Return value

The result depends on the concepts satisfied by possibly const-qualified underlying view type , which is `V` for  or `const V` for .
Let  be the underlying view,  be the underlying counter (equals to `0` if `take_view` was default initialized).


| - |
| rowspan=2 colspan=2 | The underlying view type<br>satisfies ... |
| colspan=2 | lconcept | random_access_range |
| - |
| yes |
| no |
| - |
| rowspan=2 | lconcept | sized_range |
| yes |
| c | ranges::begin(base_) |
| c multi | std::counted_iterator(ranges::begin(base_), |
| ranges::range_difference_t<Base_>(this->size())) |
| - |
| no |
| colspan=2 | c | std::counted_iterator(ranges::begin(base_), count_) |


## Example


### Example

```cpp
#include <concepts>
#include <forward_list>
#include <iostream>
#include <ranges>
#include <string_view>
#include <type_traits>
using namespace std::literals;

int main()
{
    {
        static constexpr auto v = {"∀x"sv, "∃y"sv, "ε"sv, "δ"sv};
        auto view = std::ranges::take_view(v, 8);
        auto iter = view.begin();
        std::cout << *iter << '\n';
        static_assert(
            std::ranges::sized_range<decltype(v)> and
            std::ranges::random_access_range<decltype(v)> and
            std::is_same_v<decltype(iter), decltype(std::ranges::begin(v))>
        );
    }

    {
        std::forward_list v = {"Ax"sv, "Ey"sv, "p"sv, "q"sv};
        auto view = std::ranges::take_view(v, 8);
        auto iter = view.begin();
        std::cout << *iter << '\n';
        static_assert(
            not std::ranges::sized_range<decltype(v)> and
            not std::ranges::random_access_range<decltype(v)> and
            std::is_same_v<decltype(iter),
                std::counted_iterator<
                    std::forward_list<std::string_view>::iterator>>
        );
    }
}
```


**Output:**
```
∀x
Ax
```


## Defect reports


## See also


| cpp/ranges/adaptor/dsc end|take_view | (see dedicated page) |
| cpp/iterator/dsc counted_iterator | (see dedicated page) |
| cpp/ranges/adaptor/sentinel/dsc operator cmp|take_view | (see dedicated page) |

