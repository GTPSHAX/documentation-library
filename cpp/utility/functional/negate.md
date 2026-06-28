---
title: std::negate
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/negate
---


```cpp
**Header:** `<`functional`>`
dcl rev multi|until1=c++14|dcl1=
template< class T >
struct negate;
|dcl2=
template< class T  void >
struct negate;
```

Function object for performing negation. Effectively calls `operator-` on an instance of type `T`.

## Specializations

rev|since=c++14|
The standard library provides a specialization of `std::negate` when `T` is not specified, which leaves the parameter types and return type to be deduced.


| cpp/utility/functional/dsc negate_void | (see dedicated page) |


## Member functions

member|operator()|2=

```cpp
dcla|constexpr=c++14|1=
T operator()( const T& arg ) const;
```

Returns the negation of `arg`.

## Parameters


### Parameters

- `arg` - value to compute negation of

## Return value

The result of `-arg`.

## Possible implementation

eq fun|1=
constexpr T operator()(const T& arg) const
{
return -arg;
}
