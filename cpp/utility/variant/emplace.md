---
title: std::variant::emplace
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/emplace
---


```cpp
dcla|num=1|constexpr=c++20|since=c++17|1=
template< class T, class... Args >
T& emplace( Args&&... args );
dcla|num=2|anchor=no|constexpr=c++20|since=c++17|1=
template< class T, class U, class... Args >
T& emplace( std::initializer_list<U> il, Args&&... args );
dcla|num=3|anchor=no|constexpr=c++20|since=c++17|1=
template< std::size_t I, class... Args >
std::variant_alternative_t<I, variant>& emplace( Args&&... args );
dcla|num=4|anchor=no|constexpr=c++20|since=c++17|1=
template< std::size_t I, class U, class... Args >
std::variant_alternative_t<I, variant>&
emplace( std::initializer_list<U> il, Args&&... args );
```

Creates a new value in-place, in an existing `variant` object
1. Equivalent to `emplace<I>(std::forward<Args>(args)...)`, where `I` is the zero-based index of `T` in `Types...`.
* .
2. Equivalent to `emplace<I>(il, std::forward<Args>(args)...)`, where `I` is the zero-based index of `T` in `Types...`.
* .
3. First, destroys the currently contained value (if any). Then direct-initializes the contained value as if constructing a value of type `T_I` with the arguments `std::forward<Args>(args)...`. If an exception is thrown, `*this` may become `valueless_by_exception`.
* .
* It is a compile-time error if `I` is not less than `sizeof...(Types)`.
4. First, destroys the currently contained value (if any). Then direct-initializes the contained value as if constructing a value of type `T_I` with the arguments `il, std::forward<Args>(args)...`. If an exception is thrown, `*this` may become `valueless_by_exception`.
* .
* It is a compile-time error if `I` is not less than `sizeof...(Types)`.

## Parameters


### Parameters

- `args` - constructor arguments to use when constructing the new value
- `il` - initializer_list argument to use when constructing the new value

## Return value

A reference to the new contained value.

## Exceptions

@1-4@ Any exception thrown during the initialization of the contained value.

## Notes


## Example


## Defect reports


## See also


| cpp/utility/variant/dsc operator{{= | (see dedicated page) |

