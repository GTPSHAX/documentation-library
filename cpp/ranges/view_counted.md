---
title: std::ranges::views::counted
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/view_counted
---


```cpp
**Header:** `<`ranges`>`
dcl|since=c++20|1=
inline constexpr /* unspecified */ counted = /* unspecified */;
dcl|since=c++20|1=
template< class Iterator, class DifferenceType >
requires /* see below */
constexpr /*span-or-subrange*/ counted( Iterator&& it, DifferenceType&& count );
```

A counted view presents a  of the elements of the ''counted range''  for some iterator `i` and non-negative integer `n`.
A counted range  is the `n` elements starting with the element pointed to by `i` and up to but not including the element, if any, pointed to by the result of `n` applications of `++i`.
If `1=n == 0`, the counted range is valid and empty. Otherwise, the counted range is only valid if `n` is positive, `i` is dereferenceable, and [++i, --n) is a valid counted range.
Formally, if `it` and `count` are expressions, `T` is `std::decay_t<decltype((it))>`, and `D` is `std::iter_difference_t<T>`, then
: if `T` models  and `decltype((count))` models `std::convertible_to<D>`,
:* if `T` models , then `views::counted(it, count)` is expression-equivalent to `std::span(std::to_address(it), static_cast<std::size_t>(static_cast<D>(count)))`,
:* otherwise, if `T` models , then `views::counted(it, count)` is expression-equivalent to `ranges::subrange(it, it + static_cast<D>(count))`,
:* otherwise, `views::counted(it, count)` is expression-equivalent to `ranges::subrange(std::counted_iterator(it, count), std::default_sentinel)`.
: Otherwise, `views::counted(it, count)` is ill-formed.

## Notes

`views::counted` does not check if the range is long enough to provide all `count` elements: use `views::take` if that check is necessary.

## Example


### Example

```cpp
#include <iostream>
#include <ranges>

int main()
{
    const int a[]{1, 2, 3, 4, 5, 6, 7};
    for (int i : std::views::counted(a, 3))
        std::cout << i << ' ';
    std::cout << '\n';

    const auto il = {1, 2, 3, 4, 5};
    for (int i : std::views::counted(il.begin() + 1, 3))
        std::cout << i << ' ';
    std::cout << '\n';
}
```


**Output:**
```
1 2 3
2 3 4
```


## Defect reports


## See also


| cpp/ranges/dsc take_view | (see dedicated page) |
| cpp/ranges/dsc subrange | (see dedicated page) |
| cpp/iterator/dsc counted_iterator | (see dedicated page) |
| cpp/algorithm/ranges/dsc count | (see dedicated page) |

