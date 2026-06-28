---
title: std::equal_to
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/equal_to
---


```cpp
**Header:** `<`functional`>`
dcl rev multi|until1=c++14|dcl1=
template< class T >
struct equal_to;
|dcl2=
template< class T  void >
struct equal_to;
```

Function object for performing comparisons. Unless specialised, invokes `operator on type `T`.

## Specializations

rev|since=c++14|
The standard library provides a specialization of `std::equal_to` when `T` is not specified, which leaves the parameter types and return type to be deduced.


| cpp/utility/functional/dsc equal_to_void | (see dedicated page) |


## Member functions

member|operator()|2=

```cpp
dcla|constexpr=c++14|1=
bool operator()( const T& lhs, const T& rhs ) const;
```

Checks whether `lhs` is ''equal'' to `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to compare

## Return value

`true` if `1=lhs == rhs`, `false` otherwise.

## Possible implementation

eq fun|1=
constexpr bool operator()(const T& lhs, const T& rhs) const
{
return lhs == rhs;
}

## See also


| cpp/algorithm/dsc equal | (see dedicated page) |
| cpp/utility/functional/dsc not_equal_to | (see dedicated page) |
| cpp/utility/functional/dsc less | (see dedicated page) |
| cpp/utility/functional/ranges/dsc {{SUBPAGENAMEE | (see dedicated page) |

