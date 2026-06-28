---
title: std::logical_not
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/logical_not
---


```cpp
**Header:** `<`functional`>`
dcl rev multi|until1=c++14|dcl1=
template< class T >
struct logical_not;
|dcl2=
template< class T  void >
struct logical_not;
```

Function object for performing logical NOT (logical negation). Effectively calls `operator!` for type `T`.

## Specializations

rev|since=c++14|
The standard library provides a specialization of `std::logical_not` when `T` is not specified, which leaves the parameter types and return type to be deduced.


| cpp/utility/functional/dsc logical_not_void | (see dedicated page) |


## Member functions

member|operator()|2=

```cpp
dcla|constexpr=c++14|1=
bool operator()( const T& arg ) const;
```

Returns the logical NOT of `arg`.

## Parameters


### Parameters

- `arg` - value to compute logical NOT of

## Return value

The result of `!arg`.

## Possible implementation

eq fun|1=
constexpr // since C++14
bool operator()(const T& arg) const
{
return !arg;
}
