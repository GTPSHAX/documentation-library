---
title: std::ranges::slide_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/slide_view/end
---


```cpp
dcl|num=1|since=c++23|1=
constexpr auto end()
requires (!(/*simple-view*/<V> && /*slide-caches-nothing*/<const V>));
dcl|num=2|since=c++23|1=
constexpr auto end() const
requires /*slide-caches-nothing*/<const V>;
```

Returns a `sentinel` or an `iterator` representing the end of the `slide_view`.
1. Let  and  be the underlying data members. Equivalent to:
* If `V` models , `return iterator<false>(ranges::begin(base_) + ranges::range_difference_t<V>(size()), n_);`.
* Otherwise, if `V` models , `return iterator<false>(ranges::prev(ranges::end(base_), n_ - 1, ranges::begin(base_)), n_);`.
* Otherwise, if `V` models , `return iterator<false>(ranges::end(base_), ranges::end(base_), n_);`.
* Otherwise, `return sentinel(ranges::end(base_));`.
@@ If `V` models , this function caches the result within the  for use on subsequent calls. This is necessary to provide the amortized constant-time complexity required by the .
2. Equivalent to `begin() + ranges::range_difference_t<const V>(size())`.

## Parameters

(none)

## Return value

A `sentinel` or an `iterator` representing the end of the `slide_view`.

## Example


### Example

```cpp
#include <iostream>
#include <ranges>

int main()
{
    static constexpr auto source = {'A', 'B', 'C', 'D'};

    for (const auto subrange: source {{!
```

{
std::cout << "[ ";
for (auto it = subrange.begin(); it != subrange.end(); ++it)
std::cout << *it << ' ';
std::cout << "]\n";
}
}
|output=
[ A B C ]
[ B C D ]

## See also


| cpp/ranges/adaptor/dsc begin|slide_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |

