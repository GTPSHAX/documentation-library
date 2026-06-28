---
title: std::minus
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/minus
---


```cpp
**Header:** `<`functional`>`
dcl rev multi|until1=c++14|dcl1=
template< class T >
struct minus;
|dcl2=
template< class T  void >
struct minus;
```

Function object for performing subtraction. Effectively calls `operator-` on two instances of type `T`.

## Specializations

rev|since=c++14|
The standard library provides a specialization of `std::minus` when `T` is not specified, which leaves the parameter types and return type to be deduced.


| cpp/utility/functional/dsc minus_void | (see dedicated page) |


## Member functions

member|operator()|2=

```cpp
dcla|constexpr=c++14|1=
T operator()( const T& lhs, const T& rhs ) const;
```

Returns the difference between `lhs` and `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to subtract from one another

## Return value

The result of `lhs - rhs`.

## Possible implementation

eq fun|1=
constexpr T operator()(const T& lhs, const T& rhs) const
{
return lhs - rhs;
}
