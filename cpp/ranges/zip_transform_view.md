---
title: std::ranges::zip_transform_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_transform_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++23|1=
template< std::move_constructible F, ranges::input_range... Views >
requires (ranges::view<Views> && ...) && (sizeof...(Views) > 0) &&
std::is_object_v<F> && std::regular_invocable<
F&, ranges::range_reference_t<Views>...> &&
/*can-reference*/<std::invoke_result_t<
F&, ranges::range_reference_t<Views>...>>
class zip_transform_view
: public ranges::view_interface<zip_transform_view<F, Views...>>
dcl|num=2|since=c++23|1=
namespace views {
inline constexpr /*unspecified*/ zip_transform = /*unspecified*/;
}
dcl|since=c++23|1=
template< class F, ranges::viewable_range... Rs >
requires /* see below */
constexpr auto zip_transform( F&& f, Rs&&... rs );
```

1. `zip_transform_view` is a range adaptor that takes an invocable object and one or more s, and produces a  whose  element is the result of applying the invocable object to the  elements of all views.<br>
A type `T` models the exposition-only concept `/*can-reference*/` if and only if `T&` is a valid type.</div>
2. `views::zip_transform` is a customization point object.
When calling with one argument `f`, let `FD` be `std::decay_t<decltype(f)>`, if:
* `FD` models ,
* `FD&` models , and
* `std::invoke_result_t<FD&>` is an object type,
then `views::zip_transform(f)` is expression-equivalent to `((void)f, auto(views::empty<std::decay_t<std::invoke_result_t<FD&>>>))`. Otherwise, the call to `views::zip_transform` is ill-formed.
When calling with more than one arguments `f` and `rs...`, `views::zip_transform(f, rs...)` is expression-equivalent to `ranges::zip_transform_view(f, rs...)`.
`zip_transform_view` models the concepts , , , , , and  when the underlying `ranges::zip_view<Views...>` models respective concepts.

## Member functions


| cpp/ranges/adaptor/dsc constructor|zip_transform_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|zip_transform_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|zip_transform_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc size|zip_transform_view | (see dedicated page) |


## 


## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| dsc expos mem type|ziperator|private=yes| | |
| * `ranges::iterator_t<const InnerView>` if `Const` is `true`, otherwise | |
| * `ranges::iterator_t<InnerView>`. | |
| dsc expos mem type|zentinel|private=yes| | |
| * `ranges::sentinel_t<const InnerView>` if `Const` is `true`, otherwise | |
| * `ranges::sentinel_t<InnerView>`. | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Nested classes


## Notes


## Example


### Example

```cpp
#include <array>
#include <iostream>
#include <list>
#include <ranges>
#include <vector>

void print(auto const rem, auto const& r)
{
    std::cout << rem << '{'; 
    for (char o[]{0,' ',0}; auto const& e : r)
        std::cout << o << e, *o = ',';
    std::cout << "}\n";
}

int main()
{
    auto v1 = std::vector<float>{1, 2, 3};
    auto v2 = std::list<short>{1, 2, 3, 4};
    auto v3 = std::to_array({1, 2, 3, 4, 5});

    auto add = [](auto a, auto b, auto c) { return a + b + c; };

    auto sum = std::views::zip_transform(add, v1, v2, v3);

    print("v1:  ", v1);
    print("v2:  ", v2);
    print("v3:  ", v3);
    print("sum: ", sum);
}
```


**Output:**
```
v1:  {1, 2, 3}
v2:  {1, 2, 3, 4}
v3:  {1, 2, 3, 4, 5}
sum: {3, 6, 9}
```


## See also


| cpp/ranges/dsc zip_view | (see dedicated page) |
| cpp/ranges/dsc transform_view | (see dedicated page) |
| cpp/ranges/dsc elements_view | (see dedicated page) |

