---
title: std::bit_xor
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/bit_xor
---


```cpp
**Header:** `<`functional`>`
dcl rev multi|until1=c++14|dcl1=
template< class T >
struct bit_xor;
|dcl2=
template< class T = void >
struct bit_xor;
```

Function object for performing bitwise XOR. Effectively calls `operator^` on type `T`.

## Specializations

rev|since=c++14|
The standard library provides a specialization of `std::bit_xor` when `T` is not specified, which leaves the parameter types and return type to be deduced.


| cpp/utility/functional/dsc bit_xor_void | (see dedicated page) |


## Member functions

member|operator()|2=

```cpp
dcla|constexpr=c++14|1=
T operator()( const T& lhs, const T& rhs ) const;
```

Returns the result of bitwise XOR of `lhs` and `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to compute bitwise XOR of

## Return value

The result of `lhs ^ rhs`.

## Possible implementation

eq fun|1=
constexpr T operator()(const T& lhs, const T& rhs) const
{
return lhs ^ rhs;
}

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-660 | C++98 | function objects for bitwise operations are missing | added |

