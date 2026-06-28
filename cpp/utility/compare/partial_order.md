---
title: std::partial_order
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/compare/partial_order
---


```cpp
**Header:** `<`compare`>`
dcl|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */ partial_order = /* unspecified */;
}
dcl|1=
template< class T, class U >
requires /* see below */
constexpr std::partial_ordering
partial_order( T&& t, U&& u ) noexcept(/* see below */);
```

Compares two values using 3-way comparison and produces a result of type `std::partial_ordering`.
Let `t` and `u` be expressions and `T` and `U` denote `decltype((t))` and `decltype((u))` respectively, `std::partial_order(t, u)` is expression-equivalent to:
* If `std::is_same_v<std::decay_t<T>, std::decay_t<U>>` is `true`:
** `std::partial_ordering(partial_order(t, u))`, if it is a well-formed expression with overload resolution performed in a context that does not include a declaration of `std::partial_order`,
** otherwise, `std::partial_ordering(std::compare_three_way()(t, u))`, if it is well-formed,
** otherwise, `std::partial_ordering(std::weak_order(t, u))`, if it is well-formed.
* In all other cases, the expression is ill-formed, which can result in substitution failure when it appears in the immediate context of a template instantiation.

## Example

