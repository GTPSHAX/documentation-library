---
title: std::ranges::views::values
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/values_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< class R >
using values_view = ranges::elements_view<R, 1>;
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr auto values = ranges::elements<1>;
}
```

Takes a  of ''tuple-like'' values (e.g. `std::tuple` or `std::pair`), and produces a view with a ''value-type'' of the ''second'' element of the adapted view's value-type.
1. An alias for `ranges::elements_view<R, 1>`.
2. *RangeAdaptorObject* (and also *RangeAdaptorClosureObject*). The expression `views::values(e)` is expression-equivalent to } for any suitable subexpression `e`.

## Notes

`values_view` can be useful for extracting ''values'' from associative containers, e.g.

```cpp
std::map<int, std::string> map{{1, "alpha"}, {2, "beta"
```

for (auto const& value : std::views::values(map))
std::cout << value << ' ';
// prints: alpha beta

## Example


### Example

```cpp
#include <iostream>
#include <map>
#include <ranges>

int main()
{
    const auto list = {std::pair{1, 11.1}, {2, 22.2}, {3, 33.3}<!---->};
    std::cout << "pair::second values in the list: ";
    for (double value : list {{!
```

std::cout << value << ' ';
std::map<char, int> map'A', 1}, {'B', 2}, {'C', 3}, {'D', 4}, {'E', 5;
auto odd = [](int x) { return 0 != (x & 1); };
std::cout << "\nodd values in the map: ";
for (int value : map | std::views::values | std::views::filter(odd))
std::cout << value << ' ';
std::cout << '\n';
}
|output=
pair::second values in the list: 11.1 22.2 33.3
odd values in the map: 1 3 5

## Defect reports


## See also


| cpp/ranges/dsc keys_view | (see dedicated page) |
| cpp/ranges/dsc elements_view | (see dedicated page) |
| cpp/numeric/valarray/dsc slice | (see dedicated page) |

