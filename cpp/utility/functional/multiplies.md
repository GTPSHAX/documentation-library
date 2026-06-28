---
title: std::multiplies
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/multiplies
---


```cpp
**Header:** `<`functional`>`
dcl rev multi|until1=c++14|dcl1=
template< class T >
struct multiplies;
|dcl2=
template< class T  void >
struct multiplies;
```

Function object for performing multiplication. Effectively calls `operator*` on two instances of type `T`.

## Specializations

rev|since=c++14|
The standard library provides a specialization of `std::multiplies` when `T` is not specified, which leaves the parameter types and return type to be deduced.


| cpp/utility/functional/dsc multiplies_void | (see dedicated page) |


## Member functions

member|operator()|2=

```cpp
dcla|constexpr=c++14|1=
T operator()( const T& lhs, const T& rhs ) const;
```

Returns the product of `lhs` and `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to multiply

## Return value

The result of `lhs * rhs`.

## Possible implementation

eq fun|1=
constexpr T operator()(const T& lhs, const T& rhs) const
{
return lhs * rhs;
}
