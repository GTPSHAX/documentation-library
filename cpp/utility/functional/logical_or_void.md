---
title: std::logical_or<void>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/logical_or_void
---

ddcl|header=functional|since=c++14|
template<>
class logical_or<void>;
`std::logical_or<void>` is a specialization of `std::logical_or` with parameter and return type deduced.

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions

member|operator()|2=
ddcl|1=
template< class T, class U >
constexpr auto operator()( T&& lhs, U&& rhs ) const
-> decltype(std::forward<T>(lhs)  std::forward<U>(rhs));
Returns the result of `std::forward<T>(lhs) .

## Parameters


### Parameters

- `lhs, rhs` - values to logical OR

## Return value

`std::forward<T>(lhs) .

## Example

