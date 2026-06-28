---
title: std::ranges::subrange::size
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/subrange/size
---

ddcl|since=c++20|1=
constexpr /*make-unsigned-like-t*/<std::iter_difference_t<I>> size() const
requires (K == ranges::subrange_kind::sized);
Obtains the number of elements in the `subrange`:
* If  is `true`, returns .
* Otherwise, returns .
For the definition of `/*make-unsigned-like-t*/`, see .

## Return value

As described above.

## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <ranges>
#include <utility>

int main()
{
    const auto v = {2, 2, 2, 7, 1, 1, 1, 1, 8, 2, 2, 2, 2, 2};

    // the value type of views::chunk_by is the ranges::subrange

    auto to_pair = [](auto sub) { return std::make_pair(sub[0], sub.size()); };
                                                                 /* ^^^^ */
    auto pairs = v {{!
```

| std::views::transform(to_pair);
for (auto x : pairs bitor std::views::keys)
std::cout << x << ' ';
std::cout << '\n';
for (auto x : pairs bitor std::views::values)
std::cout << x << ' ';
std::cout << '\n';
}
|output=
2 7 1 8 2
3 1 4 1 5

## See also


| cpp/ranges/subrange/dsc empty | (see dedicated page) |
| cpp/iterator/dsc size | (see dedicated page) |
| cpp/ranges/dsc size | (see dedicated page) |

