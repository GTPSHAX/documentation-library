---
title: std::logical_and
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/logical_and
---


```cpp
**Header:** `<`functional`>`
dcl rev multi|until1=c++14|dcl1=
template< class T >
struct logical_and;
|dcl2=
template< class T = void >
struct logical_and;
```

Function object for performing logical AND (logical conjunction). Effectively calls `operator&&` on type `T`.

## Specializations

rev|since=c++14|
The standard library provides a specialization of `std::logical_and` when `T` is not specified, which leaves the parameter types and return type to be deduced.


| cpp/utility/functional/dsc logical_and_void | (see dedicated page) |


## Member functions

member|operator()|2=

```cpp
dcla|constexpr=c++14|1=
bool operator()( const T& lhs, const T& rhs ) const;
```

Returns the logical AND of `lhs` and `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to compute logical AND of

## Return value

The result of `lhs && rhs`.

## Possible implementation

eq fun|1=
constexpr bool operator()(const T& lhs, const T& rhs) const
{
return lhs && rhs;
}
