---
title: std::ranges::views::keys
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/keys_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< class R >
using keys_view = ranges::elements_view<R, 0>;
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr auto keys = ranges::elements<0>;
}
```

Takes a  of ''tuple-like'' values (e.g. `std::tuple` or `std::pair`), and produces a view with a ''value-type'' of the ''first'' element of the adapted view's value-type.
1. An alias for `ranges::elements_view<R, 0>`.
2. *RangeAdaptorObject* (and also *RangeAdaptorClosureObject*). The expression `views::keys(e)` is expression-equivalent to } for any suitable subexpression `e`.

## Notes

`keys_view` can be useful for extracting ''keys'' from associative containers, e.g.

```cpp
std::map<std::string, int> map{{"one", 1}, {"two", 2
```

for (auto const& key : std::views::keys(map))
std::cout << key << ' ';
// prints: one two

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <locale>
#include <ranges>
#include <string>
#include <tuple>
#include <vector>

int main()
{
    const std::vector<std::tuple<std::string, double, bool>> quark_mass_charge
    {
        // name, MeV/c², has positive electric-charge:
        {"up", 2.3, true}, {"down", 4.8, false},
        {"charm", 1275, true}, {"strange", 95, false},
        {"top", 173'210, true}, {"bottom", 4'180, false},
    };

    std::cout.imbue(std::locale("en_US.utf8"));
    std::cout << "Quark name:  │ ";
    for (std::string const& name : std::views::keys(quark_mass_charge))
        std::cout << std::setw(9) << name << " │ ";

    std::cout << "\n" "Mass MeV/c²: │ ";
    for (const double mass : std::views::values(quark_mass_charge))
        std::cout << std::setw(9) << mass << " │ ";

    std::cout << "\n" "E-charge:    │ ";
    for (const bool pos : std::views::elements<2>(quark_mass_charge))
        std::cout << std::setw(9) << (pos ? "+2/3" : "-1/3") << " │ ";
    std::cout << '\n';
}
```


**Output:**
```
Quark name:  │        up │      down │     charm │   strange │       top │    bottom │
Mass MeV/c²: │       2.3 │       4.8 │     1,275 │        95 │   173,210 │     4,180 │
E-charge:    │      +2/3 │      -1/3 │      +2/3 │      -1/3 │      +2/3 │      -1/3 │
```


## Defect reports


## See also


| cpp/ranges/dsc values_view | (see dedicated page) |
| cpp/ranges/dsc elements_view | (see dedicated page) |
| cpp/numeric/valarray/dsc slice | (see dedicated page) |

