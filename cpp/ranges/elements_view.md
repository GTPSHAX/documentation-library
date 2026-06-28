---
title: std::ranges::views::elements
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/elements_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< ranges::input_range V, std::size_t N >
requires ranges::view<V> &&
/*has-tuple-element*/<ranges::range_value_t<V>, N> &&
/*has-tuple-element*/<std::remove_reference_t<
ranges::range_reference_t<V>>, N> &&
/*returnable-element*/<ranges::range_reference_t<V>, N>
class elements_view
: public ranges::view_interface<elements_view<V, N>>;
dcl|num=2|since=c++20|1=
namespace views {
template< std::size_t N >
constexpr /* unspecified */ elements = /* unspecified */;
}
dcl|since=c++20|1=
template< ranges::viewable_range R >
requires /* see below */
constexpr ranges::view auto elements<N>( R&& r );
dcl rev multi|num=3
|notes1=|dcl1=
template< class T, std::size_t N >
concept /*has-tuple-element*/ =
requires(T t) {
typename std::tuple_size<T>::type;
requires N < std::tuple_size_v<T>;
typename std::tuple_element_t<N, T>;
{ std::get<N>(t) } -> std::convertible_to<
const std::tuple_element_t<N, T>&>;
};
|since2=c++23|notes2=|dcl2=
template< class T, std::size_t N >
concept /*has-tuple-element*/ =
/*tuple-like*/<T> && N < std::tuple_size_v<T>
|1=
template< class T, std::size_t N >
concept returnable-element =
std::is_reference_v<T>  std::move_constructible<
std::tuple_element_t<N, T>>;
```

1. Accepts a  of tuple-like values, and issues a view with a value type of the `N` element of the adapted view's value-type.
2. Every specialization of `views::elements` is a *RangeAdaptorObject*. The expression `views::elements<M>(e)` is expression-equivalent to } for any suitable subexpression `e` and constant expression `M`.
3. Ensures that the elements of the underlying view are tuple-like values<sup>(since C++23)</sup> , see .
4. Ensures that dangling references cannot be returned.
`elements_view` models the concepts , , , , , and  when the underlying view `V` models respective concepts.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|elements_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|elements_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|elements_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|elements_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc size|elements_view|notes | (see dedicated page) |
| cpp/ranges/adaptor/dsc reserve_hint|elements_view | (see dedicated page) |


## Nested classes


## Helper templates

ddcl|since=c++20|1=
template<class T, std::size_t N>
constexpr bool enable_borrowed_range<std::ranges::elements_view<T, N>> =
ranges::enable_borrowed_range<T>;
This specialization of `ranges::enable_borrowed_range` makes `elements_view` satisfy  when the underlying view satisfies it.

## Example


### Example

```cpp
#include <iostream>
#include <ranges>
#include <string>
#include <tuple>
#include <vector>

int main()
{
    const std::vector<std::tuple<int, char, std::string>> vt
    {
        {1, 'A', "α"},
        {2, 'B', "β"},
        {3, 'C', "γ"},
        {4, 'D', "δ"},
        {5, 'E', "ε"},
    };

    for (int const e : std::views::elements<0>(vt))
        std::cout << e << ' ';
    std::cout << '\n';

    for (char const e : vt {{!
```

std::cout << e << ' ';
std::cout << '\n';
for (std::string const& e : std::views::elements<2>(vt))
std::cout << e << ' ';
std::cout << '\n';
}
|output=
1 2 3 4 5
A B C D E
α β γ δ ε

## Defect reports


## See also


| cpp/ranges/dsc keys_view | (see dedicated page) |
| cpp/ranges/dsc values_view | (see dedicated page) |
| cpp/ranges/dsc zip_view | (see dedicated page) |
| cpp/ranges/dsc zip_transform_view | (see dedicated page) |
| cpp/numeric/valarray/dsc slice | (see dedicated page) |

