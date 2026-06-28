---
title: std::ranges::views::join
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|
template< ranges::input_range V >
requires ranges::view<V> and
ranges::input_range<ranges::range_reference_t<V>>
class join_view
: public ranges::view_interface<join_view<V>>
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr /* unspecified */ join = /* unspecified */;
}
dcl|since=c++20|1=
template< ranges::viewable_range R >
requires /* see below */
constexpr ranges::view auto join( R&& r );
```

1. A range adaptor that represents  consisting of the sequence obtained from flattening a view of ranges.
2. *RangeAdaptorObject* (and also *RangeAdaptorClosureObject*). The expression `views::join(e)` is expression-equivalent to } for any suitable subexpressions `e`.
`join_view` models .
`join_view` models  when:
* `ranges::range_reference_t<V>` is a reference type, and
* `V` and `ranges::range_reference_t<V>` each model .
`join_view` models  when:
* `ranges::range_reference_t<V>` is a reference type,
* `V` models , and
* `ranges::range_reference_t<V>` models both  and .
`join_view` models  when:
* `ranges::range_reference_t<V>` is a reference type, and
* `V` and `ranges::range_reference_t<V>` each model  and  .

## Member functions


| cpp/ranges/adaptor/dsc constructor|join_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|join_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|join_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|join_view | (see dedicated page) |


## 


## Nested classes


## Notes

Before `P2328R1` was adopted, the inner range type (`ranges::range_reference_t<V>`) cannot be a container type (but can be reference to container). For example, it was not allowed to join a `transform_view` of `std::string` prvalue.

```cpp
struct Person { int age; std::string name; };

auto f(std::vector<Person>& v) {
//  return v {{!
```

//           | std::views::join; // error before P2328R1
return v | std::views::transform([](auto& p) -> std::string& { return p.name; })
| std::views::join; // OK
}

## Example


### Example

```cpp
#include <iostream>
#include <ranges>
#include <string_view>
#include <vector>

int main()
{
    using namespace std::literals;

    const auto bits = {"https:"sv, "//"sv, "cppreference"sv, "."sv, "com"sv};
    for (char const c : bits {{!
```

std::cout << c;
std::cout << '\n';
const std::vector<std::vector<int>> v1, 2}, {3, 4, 5}, {6}, {7, 8, 9;
auto jv = std::ranges::join_view(v);
for (int const e : jv)
std::cout << e << ' ';
std::cout << '\n';
}
|output=
https://cppreference.com
1 2 3 4 5 6 7 8 9

## Defect reports


## See also


| cpp/ranges/dsc join_with_view | (see dedicated page) |
| cpp/ranges/dsc concat_view | (see dedicated page) |

