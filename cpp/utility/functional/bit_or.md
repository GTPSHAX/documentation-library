---
title: std::bit_or
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/bit_or
---


```cpp
**Header:** `<`functional`>`
dcl rev multi|until1=c++14|dcl1=
template< class T >
struct bit_or;
|dcl2=
template< class T = void >
struct bit_or;
```

Function object for performing bitwise OR. Effectively calls `operator on type `T`.

## Specializations

rev|since=c++14|
The standard library provides a specialization of `std::bit_or` when `T` is not specified, which leaves the parameter types and return type to be deduced.


| cpp/utility/functional/dsc bit_or_void | (see dedicated page) |


## Member functions

member|operator()|2=

```cpp
dcla|constexpr=c++14|1=
T operator()( const T& lhs, const T& rhs ) const;
```

Returns the result of bitwise OR of `lhs` and `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to compute bitwise OR of

## Return value

The result of `lhs .

## Possible implementation

eq fun|1=
constexpr T operator()(const T& lhs, const T& rhs) const
{
return lhs | rhs;
}

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-660 | C++98 | function objects for bitwise operations are missing | added |

