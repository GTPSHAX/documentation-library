---
title: std::logical_or
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/logical_or
---


```cpp
**Header:** `<`functional`>`
dcl rev multi|until1=c++14|dcl1=
template< class T >
struct logical_or;
|dcl2=
template< class T  void >
struct logical_or;
```

Function object for performing logical OR (logical disjunction). Effectively calls `operator on type `T`.

## Specializations

rev|since=c++14|
The standard library provides a specialization of `std::logical_or` when `T` is not specified, which leaves the parameter types and return type to be deduced.


| cpp/utility/functional/dsc logical_or_void | (see dedicated page) |


## Member functions

member|operator()|2=

```cpp
dcla|constexpr=c++14|1=
bool operator()( const T& lhs, const T& rhs ) const;
```

Returns the logical OR of `lhs` and `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to compute logical OR of

## Return value

The result of `lhs .

## Possible implementation

eq fun|1=
constexpr bool operator()(const T& lhs, const T& rhs) const
{
return lhs  rhs;
}
