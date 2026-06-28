---
title: std::bit_not<void>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/bit_not_void
---

ddcl|header=functional|since=c++14|
template<>
class bit_not<void>;
`std::bit_not<void>` is a specialization of `std::bit_not` with parameter and return type deduced.

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions

member|operator()|2=
ddcl|1=
template< class T >
constexpr auto operator()( T&& arg ) const
-> decltype(~std::forward<T>(arg));
Returns the result of `~std::forward<T>(arg)`.

## Parameters


### Parameters

- `arg` - value to bitwise NOT

## Return value

`~std::forward<T>(arg)`.

## Example

