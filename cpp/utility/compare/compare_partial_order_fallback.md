---
title: std::compare_partial_order_fallback
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/compare/compare_partial_order_fallback
---


```cpp
**Header:** `<`compare`>`
dcl|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */
compare_partial_order_fallback = /* unspecified */;
}
dcl|since=c++20|1=
template< class T, class U >
requires /* see below */
constexpr std::partial_ordering
compare_partial_order_fallback( T&& t, U&& u ) noexcept(/* see below */);
```

Performs three-way comparison on subexpressions `t` and `u` and produces a result of type , even if the operator `1=<=>` is unavailable.
If `std::decay_t<T>` and `std::decay_t<U>>` are the same type, `std::compare_partial_order_fallback(t, u)` is expression-equivalent to:
* `std::partial_order(t, u)`, if it is a well-formed expression;
* otherwise, c multi
|1=t == u ? std::partial_ordering::equivalent :
|2=t < u  ? std::partial_ordering::less :
|3=u < t  ? std::partial_ordering::greater :
|4=         std::partial_ordering::unordered
, if the expressions `1=t == u`, `t < u` and `u < t` are all well-formed and each of `1=decltype(t == u)`, `decltype(t < u)` and `decltype(u < t)` models , except that `t` and `u` are evaluated only once.
In all other cases, `std::compare_partial_order_fallback(t, u)` is ill-formed, which can result in substitution failure when it appears in the immediate context of a template instantiation.

## Example


## See also


| cpp/utility/compare/dsc partial_order | (see dedicated page) |

