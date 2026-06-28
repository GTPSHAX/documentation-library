---
title: std::tuple_element
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple_element
---


```cpp
**Header:** `<`tuple`>`
**Header:** `<`array`>`
**Header:** `<`utility`>`
**Header:** `<`ranges|notes=
**Header:** `<`complex|notes=
dcl|num=1|since=c++11|1=
template< std::size_t I, class T >
struct tuple_element; // not defined
dcl|num=2|since=c++11|1=
template< std::size_t I, class T >
struct tuple_element< I, const T > {
using type = typename
std::add_const<typename std::tuple_element<I, T>::type>::type;
};
dcl|num=3|since=c++11|deprecated=c++20|1=
template< std::size_t I, class T >
struct tuple_element< I, volatile T > {
using type = typename
std::add_volatile<typename std::tuple_element<I, T>::type>::type;
};
dcl|num=4|since=c++11|deprecated=c++20|1=
template< std::size_t I, class T >
struct tuple_element< I, const volatile T > {
using type = typename
std::add_cv<typename std::tuple_element<I, T>::type>::type;
};
```

Provides compile-time indexed access to the types of the elements of a  type.
1. The primary template is not defined. An explicit (full) or partial specialization is required to make a type tuple-like.
@2-4@ Specializations for cv-qualified types simply add corresponding cv-qualifiers by default.
rrev|since=c++17|
`std::tuple_element` interacts with the core language: it can provide  support in the tuple-like case.

## Specializations

The standard library provides following specializations for standard library types:


| cpp/utility/tuple/dsc tuple_element | (see dedicated page) |
| cpp/utility/pair/dsc tuple_element | (see dedicated page) |
| cpp/container/array/dsc tuple_element | (see dedicated page) |
| cpp/ranges/subrange/dsc tuple_element | (see dedicated page) |
| cpp/numeric/complex/dsc tuple_element | (see dedicated page) |

Users may specialize `std::tuple_element` for program-defined types to make them tuple-like.
In normal cases where the `get` functions returns reference members or reference to subobjects, only specializations for cv-unqualified types are needed to be customized.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Helper types

ddcl|header=tuple|since=c++14|1=
template< std::size_t I, class T >
using tuple_element_t = typename tuple_element<I, T>::type;

## Notes


## Example


### Example

```cpp
#include <array>
#include <cstddef>
#include <iostream>
#include <ranges>
#include <tuple>
#include <type_traits>
#include <utility>

template<typename T1, typename T2, typename T3>
struct Triple
{
    T1 t1;
    T2 t2;
    T3 t3;
};

// A specialization of std::tuple_element for program-defined type Triple:
template<std::size_t I, typename T1, typename T2, typename T3>
    struct std::tuple_element<I, Triple<T1, T2, T3>>
    { static_assert(false, "Invalid index"); }; <!-- CWG2518 -->
template<typename T1, typename T2, typename T3>
    struct std::tuple_element<0, Triple<T1, T2, T3>> { using type = T1; };
template<typename T1, typename T2, typename T3>
    struct std::tuple_element<1, Triple<T1, T2, T3>> { using type = T2; };
template<typename T1, typename T2, typename T3>
    struct std::tuple_element<2, Triple<T1, T2, T3>> { using type = T3; };


template<typename... Args> struct TripleTypes
{
    static_assert(3 == sizeof...(Args), "Expected exactly 3 type names");
    template<std::size_t N>
    using type = typename std::tuple_element_t<N, Triple<Args...>>;
};

int main()
{
    TripleTypes<char, int, float>::type<1> i{42};
    std::cout << i << '\n';

    using Tri = Triple<int, char, short>; //< Program-defined type
    static_assert(std::is_same_v<std::tuple_element_t<0, Tri>, int> &&
                  std::is_same_v<std::tuple_element_t<1, Tri>, char> &&
                  std::is_same_v<std::tuple_element_t<2, Tri>, short>);

    using Tuple = std::tuple<int, char, short>;
    static_assert(std::is_same_v<std::tuple_element_t<0, Tuple>, int> &&
                  std::is_same_v<std::tuple_element_t<1, Tuple>, char> &&
                  std::is_same_v<std::tuple_element_t<2, Tuple>, short>);

    using Array3 = std::array<int, 3>;
    static_assert(std::is_same_v<std::tuple_element_t<0, Array3>, int> &&
                  std::is_same_v<std::tuple_element_t<1, Array3>, int> &&
                  std::is_same_v<std::tuple_element_t<2, Array3>, int>);

    using Pair = std::pair<Tuple, Tri>;
    static_assert(std::is_same_v<std::tuple_element_t<0, Pair>, Tuple> &&
                  std::is_same_v<std::tuple_element_t<1, Pair>, Tri>);

    using Sub = std::ranges::subrange<int*, int*>;
    static_assert(std::is_same_v<std::tuple_element_t<0, Sub>, int*> &&
                  std::is_same_v<std::tuple_element_t<1, Sub>, int*>);
}
```


**Output:**
```
42
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2212 | C++11 | specializations for cv types were not required in some headers, which led to ambiguity | required |


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/utility/dsc tuple_size | (see dedicated page) |
| cpp/utility/tuple/dsc tuple_cat | (see dedicated page) |

