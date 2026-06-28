---
title: std::get(std::tuple)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple/get
---


# getpetty|(std::tuple)


```cpp
**Header:** `<`tuple`>`
dcla|num=1|anchor=no|since=c++11|constexpr=c++14|
template< std::size_t I, class... Types >
typename std::tuple_element<I, std::tuple<Types...>>::type&
get( std::tuple<Types...>& t ) noexcept;
dcla|num=2|anchor=no|since=c++11|constexpr=c++14|
template< std::size_t I, class... Types >
typename std::tuple_element<I, std::tuple<Types...>>::type&&
get( std::tuple<Types...>&& t ) noexcept;
dcla|num=3|anchor=no|since=c++11|constexpr=c++14|
template< std::size_t I, class... Types >
const typename std::tuple_element<I, std::tuple<Types...>>::type&
get( const std::tuple<Types...>& t ) noexcept;
dcla|num=4|since=c++11|constexpr=c++14|
template< std::size_t I, class... Types >
const typename std::tuple_element<I, std::tuple<Types...>>::type&&
get( const std::tuple<Types...>&& t ) noexcept;
dcla|num=5|since=c++14|
template< class T, class... Types >
constexpr T& get( std::tuple<Types...>& t ) noexcept;
dcl|num=6|since=c++14|
template< class T, class... Types >
constexpr T&& get( std::tuple<Types...>&& t ) noexcept;
dcl|num=7|since=c++14|
template< class T, class... Types >
constexpr const T& get( const std::tuple<Types...>& t ) noexcept;
dcla|num=8|since=c++14|
template< class T, class... Types >
constexpr const T&& get( const std::tuple<Types...>&& t ) noexcept;
```

@1-4@ Extracts the `I` element from the tuple. `I` must be an integer value in [0, sizeof...(Types)).
@5-8@ Extracts the element of the tuple `t` whose type is `T`. Fails to compile unless the tuple has exactly one element of that type.

## Parameters


### Parameters

- `t` - tuple whose contents to extract

## Return value

A reference to the selected element of `t`.

## Notes


## Example


### Example

```cpp
#include <cassert>
#include <iostream>
#include <string>
#include <tuple>

int main()
{
    auto x = std::make_tuple(1, "Foo", 3.14);

    // Index-based access
    std::cout << "( " << std::get<0>(x)
              << ", " << std::get<1>(x)
              << ", " << std::get<2>(x)
              << " )\n";

    // Type-based access (since C++14)
    std::cout << "( " << std::get<int>(x)
              << ", " << std::get<const char*>(x)
              << ", " << std::get<double>(x)
              << " )\n";

    const std::tuple<int, const int, double, double> y(1, 2, 6.9, 9.6);
    const int& i1 = std::get<int>(y); // OK: not ambiguous
    assert(i1 == 1);
    const int& i2 = std::get<const int>(y); // OK: not ambiguous
    assert(i2 == 2);
    // const double& d = std::get<double>(y); // Error: ill-formed (ambiguous)

    // Note: std::tie and structured binding can be
    // used to unpack a tuple into individual objects.
}
```


**Output:**
```
( 1, Foo, 3.14 )
( 1, Foo, 3.14 )
```


## Defect reports


## See also


| cpp/container/array/dsc get | (see dedicated page) |
| cpp/utility/pair/dsc get | (see dedicated page) |
| cpp/utility/variant/dsc get | (see dedicated page) |
| cpp/ranges/subrange/dsc get | (see dedicated page) |
| cpp/numeric/complex/dsc get | (see dedicated page) |
| cpp/utility/tuple/dsc tie | (see dedicated page) |
| cpp/language/dsc structured binding | (see dedicated page) |

