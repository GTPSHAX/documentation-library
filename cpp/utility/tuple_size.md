---
title: std::tuple_size
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple_size
---


```cpp
**Header:** `<`array`>`
**Header:** `<`tuple`>`
**Header:** `<`utility`>`
**Header:** `<`ranges|notes=
**Header:** `<`complex|notes=
dcl|num=1|since=c++11|1=
template< class T >
struct tuple_size; // not defined
dcl|num=2|since=c++11|1=
template< class T >
struct tuple_size< const T >
: std::integral_constant<std::size_t, std::tuple_size<T>::value> {};
dcl|num=3|since=c++11|deprecated=c++20|1=
template< class T >
struct tuple_size< volatile T >
: std::integral_constant<std::size_t, std::tuple_size<T>::value> {};
dcl|num=4|since=c++11|deprecated=c++20|1=
template< class T >
struct tuple_size< const volatile T >
: std::integral_constant<std::size_t, std::tuple_size<T>::value> {};
```

Provides access to the number of elements in a  type as a compile-time constant expression.
1. The primary template is not defined. An explicit (full) or partial specialization is required to make a type tuple-like.
@2-4@ Specializations for a cv-qualified types reuse the `value` from the corresponding cv-unqualified versions by default.
rrev|since=c++17|
`std::tuple_size` interacts with the core language: it can provide  support in the tuple-like case.
are SFINAE-friendly: if `std::tuple_size<T>::value` is
ill-formed when treated as an unevaluated operand, they do not provide the member `value`. Access checking is performed as if in a context unrelated to `tuple_size` and `T`. Only the validity of the immediate context of the expression is considered. This allows

```cpp
#include <utility>

struct X { int a, b; };
const auto [x, y] = X(); // structured binding declaration first attempts
                         // tuple_size<const X> which attempts to use tuple_size<X>::value,
                         // then soft error encountered, binds to public data members
```


## Specializations

The standard library provides following specializations for standard library types:


| cpp/utility/tuple/dsc tuple_size | (see dedicated page) |
| cpp/utility/pair/dsc tuple_size | (see dedicated page) |
| cpp/container/array/dsc tuple_size | (see dedicated page) |
| cpp/ranges/subrange/dsc tuple_size | (see dedicated page) |
| cpp/numeric/complex/dsc tuple_size | (see dedicated page) |

All specializations of `std::tuple_size` satisfy *UnaryTypeTrait* with ''base characteristic'' `std::integral_constant<std::size_t, N>` for some `N`.
Users may specialize `std::tuple_size` for program-defined types to make them tuple-like. Program-defined specializations must meet the requirements above.
Usually only specialization for cv-unqualified types are needed to be customized.

## Helper variable template

ddcl|header=tuple|since=c++17|1=
template< class T >
constexpr std::size_t tuple_size_v = tuple_size<T>::value;

## Example


### Example

```cpp
#include <array>
#include <cstddef>
#include <ranges>
#include <tuple>
#include <utility>

template<class T, std::size_t Size> struct Arr { T data[Size]; };

// Program-defined specialization of std::tuple_size:
template<class T, std::size_t Size> struct std::tuple_size<Arr<T, Size>>
    : public integral_constant<std::size_t, Size> {};

int main()
{
    using tuple1 = std::tuple<int, char, double>;
    static_assert(3 == std::tuple_size_v<tuple1>); // uses using template (C++17)

    using array3x4 = std::array<std::array<int, 3>, 4>;
    static_assert(4 == std::tuple_size<array3x4>{}); // uses operator std::size_t

    using pair = std::pair<tuple1, array3x4>;
    static_assert(2 == std::tuple_size<pair>()); // uses operator()

    using sub = std::ranges::subrange<char*, char*>;
    static_assert(2 == std::tuple_size<sub>::value);

    using Arr5 = Arr<int, 5>;
    static_assert(5 == std::tuple_size_v<Arr5>);
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2212 | C++11 | specializations for cv types were not required in some headers, which led to ambiguity | required |


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/utility/dsc tuple_element | (see dedicated page) |
| cpp/utility/tuple/dsc tuple_cat | (see dedicated page) |

