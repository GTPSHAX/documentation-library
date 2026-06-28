---
title: std::ref
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/ref
---


```cpp
**Header:** `<`functional`>`
dcla|num=1|since=c++11|constexpr=c++20|1=
template< class T >
std::reference_wrapper<T> ref( T& t ) noexcept;
dcla|num=2|since=c++11|constexpr=c++20|1=
template< class T >
std::reference_wrapper<T>
ref( std::reference_wrapper<T> t ) noexcept;
dcla|num=3|since=c++11|1=
template< class T >
void ref( const T&& ) = delete;
dcla|num=4|since=c++11|constexpr=c++20|1=
template< class T >
std::reference_wrapper<const T> cref( const T& t ) noexcept;
dcla|num=5|since=c++11|constexpr=c++20|1=
template< class T >
std::reference_wrapper<const T>
cref( std::reference_wrapper<T> t ) noexcept;
dcla|num=6|since=c++11|1=
template< class T >
void cref( const T&& ) = delete;
```

Function templates `ref` and `cref` are helper functions that generate an object of type `std::reference_wrapper`, using template argument deduction to determine the template argument of the result.
<sup>(since C++20)</sup> `T` may be an incomplete type.

## Parameters


### Parameters


## Return value

1. `std::reference_wrapper<T>(t)`
2. `t`
4. `std::reference_wrapper<const T>(t)`
5. `t`
@3,6@ rvalue reference wrapper is deleted.

## Example


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3146 | C++11 | unwrapping overloads sometimes led to error | made always valid |


## See also

