---
title: std::logical_not<void>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/logical_not_void
---

ddcl|header=functional|since=c++14|
template<>
class logical_not<void>;
`std::logical_not<void>` is a specialization of `std::logical_not` with parameter and return type deduced.

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions

member|operator()|2=
ddcl|1=
template< class T >
constexpr auto operator()( T&& arg ) const
-> decltype(!std::forward<T>(arg));
Returns the result of `!std::forward<T>(arg)`.

## Parameters


### Parameters

- `arg` - value to apply logical NOT to

## Return value

`!std::forward<T>(arg)`.

## Example

