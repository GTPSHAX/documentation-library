---
title: std::bit_xor<void>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/bit_xor_void
---

ddcl|header=functional|since=c++14|
template<>
class bit_xor<void>;
`std::bit_xor<void>` is a specialization of `std::bit_xor` with parameter and return type deduced.

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions

member|operator()|2=
ddcl|1=
template< class T, class U >
constexpr auto operator()( T&& lhs, U&& rhs ) const
-> decltype(std::forward<T>(lhs) ^ std::forward<U>(rhs));
Returns the result of `std::forward<T>(lhs) ^ std::forward<U>(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - values to bitwise XOR

## Return value

`std::forward<T>(lhs) ^ std::forward<U>(rhs)`.

## Example

