---
title: std::logical_and<void>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/logical_and_void
---

ddcl|header=functional|since=c++14|
template<>
class logical_and<void>;
`std::logical_and<void>` is a specialization of `std::logical_and` with parameter and return type deduced.

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions

member|operator()|2=
ddcl|1=
template< class T, class U >
constexpr auto operator()( T&& lhs, U&& rhs ) const
-> decltype(std::forward<T>(lhs) && std::forward<U>(rhs));
Returns the result of `lhs && rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to logical AND

## Return value

The result of `lhs && rhs`.

## Example

