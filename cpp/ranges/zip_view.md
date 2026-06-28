---
title: std::ranges::zip_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++23|
template< ranges::input_range... Views >
requires (ranges::view<Views> && ...) && (sizeof...(Views) > 0)
class zip_view
: public ranges::view_interface<zip_view<Views...>>
dcl|num=2|since=c++23|1=
namespace views {
inline constexpr /*unspecified*/ zip = /*unspecified*/;
}
dcl|since=c++23|
template< ranges::viewable_range... Rs >
requires /* see below */
constexpr ranges::view auto zip( Rs&&... rs );
```

1. `zip_view` is a range adaptor that takes one or more s, and produces a  whose th element is a tuple-like value consisting of the  elements of all views. The size of produced view is the minimum of sizes of all adapted views.
2. `views::zip` is a customization point object.<br>
When calling with no argument, `views::zip()` is expression-equivalent to `auto(views::empty<std::tuple<>>)`.<br>
Otherwise, `views::zip(rs...)` is ''expression-equivalent'' to `ranges::zip_view<views::all_t<decltype((rs))>...>(rs...)`.
`zip_view` always models , and models , , , or  if all adapted  types model the corresponding concept.
`zip_view` models  if
* `sizeof...(Views)` is equal to `1`, and the only adapted view type models , or
* at least one adapted view type does not model , and every adapted view type models , or
* every adapted view type models both  and .

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|zip_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|zip_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|zip_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc size|zip_view | (see dedicated page) |


## 


## Nested classes


## Helper templates

ddcl|since=c++23|1=
template< class... Views >
constexpr bool enable_borrowed_range<ranges::zip_view<Views...>> =
(ranges::enable_borrowed_range<Views> && ...);
This specialization of `cpp/ranges/borrowed_range|ranges::enable_borrowed_range` makes  satisfy  when each underlying view satisfies it.

## Notes


## Example


### Example

```cpp
#include <array>
#include <iostream>
#include <list>
#include <ranges>
#include <string>
#include <tuple>
#include <vector>

void print(auto const rem, auto const& range)
{
    for (std::cout << rem; auto const& elem : range)
        std::cout << elem << ' ';
    std::cout << '\n';
}

int main()
{
    auto x = std::vector{1, 2, 3, 4};
    auto y = std::list<std::string>{"α", "β", "γ", "δ", "ε"};
    auto z = std::array{'A', 'B', 'C', 'D', 'E', 'F'};

    print("Source views:", "");
    print("x: ", x);
    print("y: ", y);
    print("z: ", z);

    print("\nzip(x,y,z):", "");

    for (std::tuple<int&, std::string&, char&> elem : std::views::zip(x, y, z))
    {
        std::cout << std::get<0>(elem) << ' '
                  << std::get<1>(elem) << ' '
                  << std::get<2>(elem) << '\n';

        std::get<char&>(elem) += ('a' - 'A'); // modifies the element of z
    }

    print("\nAfter modification, z: ", z);
}
```


**Output:**
```
Source views:
x: 1 2 3 4
y: α β γ δ ε
z: A B C D E F

zip(x,y,z):
1 α A
2 β B
3 γ C
4 δ D

After modification, z: a b c d E F
```


## See also


| cpp/ranges/dsc zip_transform_view | (see dedicated page) |
| cpp/ranges/dsc elements_view | (see dedicated page) |

