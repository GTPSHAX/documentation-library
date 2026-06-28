---
title: std::swap(std::tuple)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple/swap2
---


```cpp
**Header:** `<`tuple`>`
dcl rev multi|num=1|since1=c++11|dcl1=
template< class... Types >
void swap( std::tuple<Types...>& lhs,
std::tuple<Types...>& rhs ) noexcept(/* see below */);
|since2=c++20|dcl2=
template< class... Types >
constexpr void swap( std::tuple<Types...>& lhs,
std::tuple<Types...>& rhs ) noexcept(/* see below */);
dcl|num=2|since=c++23|
template< class... Types >
constexpr void swap( const std::tuple<Types...>& lhs,
const std::tuple<Types...>& rhs ) noexcept(/* see below */);
```

Swaps the contents of `lhs` and `rhs`. Equivalent to `lhs.swap(rhs)`.
rrev|since=c++17|
1. .
2. .

## Parameters


### Parameters

- `lhs, rhs` - tuples whose contents to swap

## Return value

(none)

## Exceptions


## Example

