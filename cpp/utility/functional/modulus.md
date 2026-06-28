---
title: std::modulus
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/modulus
---


```cpp
**Header:** `<`functional`>`
dcl rev multi|until1=c++14|dcl1=
template< class T >
struct modulus;
|dcl2=
template< class T  void >
struct modulus;
```

Function object for computing remainders of divisions. Implements `operator%` for type `T`.

## Specializations

rev|since=c++14|
The standard library provides a specialization of `std::modulus` when `T` is not specified, which leaves the parameter types and return type to be deduced.


| cpp/utility/functional/dsc modulus_void | (see dedicated page) |


## Member functions

member|operator()|2=

```cpp
dcla|constexpr=c++14|1=
T operator()( const T& lhs, const T& rhs ) const;
```

Returns the remainder of the division of `lhs` by `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to divide one by another

## Return value

The result of `lhs % rhs`.

## Possible implementation

eq fun|1=
constexpr T operator()(const T& lhs, const T& rhs) const
{
return lhs % rhs;
}

## See also


| cpp/numeric/math/dsc fmod | (see dedicated page) |
| cpp/numeric/math/dsc remainder | (see dedicated page) |

