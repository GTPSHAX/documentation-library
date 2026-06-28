---
title: std::get
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/get
---


# getpetty|(std::variant)


```cpp
**Header:** `<`variant`>`
dcl|since=c++17|num=1|
template< std::size_t I, class... Types >
constexpr std::variant_alternative_t<I, std::variant<Types...>>&
get( std::variant<Types...>& v );
dcl|since=c++17|num=2|
template< std::size_t I, class... Types >
constexpr std::variant_alternative_t<I, std::variant<Types...>>&&
get( std::variant<Types...>&& v );
dcl|since=c++17|num=3|
template< std::size_t I, class... Types >
constexpr const std::variant_alternative_t<I, std::variant<Types...>>&
get( const std::variant<Types...>& v );
dcl|since=c++17|num=4|
template< std::size_t I, class... Types >
constexpr const std::variant_alternative_t<I, std::variant<Types...>>&&
get( const std::variant<Types...>&& v );
dcl|since=c++17|num=5|
template< class T, class... Types >
constexpr T& get( std::variant<Types...>& v );
dcl|since=c++17|num=6|
template< class T, class... Types >
constexpr T&& get( std::variant<Types...>&& v );
dcl|since=c++17|num=7|
template< class T, class... Types >
constexpr const T& get( const std::variant<Types...>& v );
dcl|since=c++17|num=8|
template< class T, class... Types >
constexpr const T&& get( const std::variant<Types...>&& v );
```

@1-4@ Index-based value accessor: If `1=v.index() == I`, returns a reference to the value stored in `v`. Otherwise, throws `std::bad_variant_access`. The call is ill-formed if `I` is not a valid index in the variant.
@5-8@ Type-based value accessor: If `v` holds the alternative `T`, returns a reference to the value stored in `v`. Otherwise, throws `std::bad_variant_access`. The call is ill-formed if `T` is not a unique element of `Types...`.

## Template parameters


### Parameters

- `I` - index to look up
- `T` - unique type to look up
- `Types...` - types forming the `variant`

## Parameters


### Parameters

- `v` - a `variant`

## Return value

Reference to the value stored in the variant.

## Exceptions

Throws `std::bad_variant_access` on errors.

## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <variant>

int main()
{
    std::variant<int, float> v{12}, w;
    std::cout << std::get<int>(v) << '\n';
    w = std::get<int>(v);
    w = std::get<0>(v); // same effect as the previous line

//  std::get<double>(v); // error: no double in [int, float]
//  std::get<3>(v);      // error: valid index values are 0 and 1

    try
    {
        w = 42.0f;
        std::cout << std::get<float>(w) << '\n'; // ok, prints 42
        w = 42;
        std::cout << std::get<float>(w) << '\n'; // throws
    }
    catch (std::bad_variant_access const& ex)
    {
        std::cout << ex.what() << ": w contained int, not float\n";
    }
}
```


**Output:**
```
12
42
Unexpected index: w contained int, not float
```


## See also


| cpp/utility/variant/dsc get_if | (see dedicated page) |
| cpp/utility/tuple/dsc get | (see dedicated page) |
| cpp/container/array/dsc get | (see dedicated page) |
| cpp/utility/pair/dsc get | (see dedicated page) |
| cpp/ranges/subrange/dsc get | (see dedicated page) |
| cpp/numeric/complex/dsc get | (see dedicated page) |

