---
title: std::weak_order
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/compare/weak_order
---


```cpp
**Header:** `<`compare`>`
dcl|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */ weak_order = /* unspecified */;
}
dcl|1=
template< class T, class U >
requires /* see below */
constexpr std::weak_ordering weak_order(T&& t, U&& u) noexcept(/* see below */);
```

Compares two values using 3-way comparison and produces a result of type `std::weak_ordering`.
Let `t` and `u` be expressions and `T` and `U` denote `decltype((t))` and `decltype((u))` respectively, `std::weak_order(t, u)` is expression-equivalent to:
* If `std::is_same_v<std::decay_t<T>, std::decay_t<U>>` is `true`:
** `std::weak_ordering(weak_order(t, u))`, if it is a well-formed expression with overload resolution performed in a context that does not include a declaration of `std::weak_order`,
** otherwise, if `T` is a floating-point type:
*** if `std::numeric_limits<T>::is_iec559` is `true`, performs the weak ordering comparison of floating-point values (see below) and returns that result as a value of type `std::weak_ordering`,
*** otherwise, yields a value of type `std::weak_ordering` that is consistent with the ordering observed by `T`'s comparison operators,
** otherwise, `std::weak_ordering(std::compare_three_way()(t, u))`, if it is well-formed,
** otherwise, `std::weak_ordering(std::strong_order(t, u))`, if it is well-formed.
* In all other cases, the expression is ill-formed, which can result in substitution failure when it appears in the immediate context of a template instantiation.

### Strict weak order of IEEE floating-point types

Let `x` and `y` be values of same IEEE floating-point type, and `weak_order_less(x, y)` be the boolean result indicating if `x` precedes `y` in the strict weak order defined by the C++ standard.
* If neither `x` nor `y` is NaN, then `1=weak_order_less(x, y) == true` if and only if `x < y`, i.e. all representations of equal floating-point value are equivalent;
* If `x` is negative NaN and `y` is not negative NaN, then `1=weak_order_less(x, y) == true`;
* If `x` is not positive NaN and `y` is positive NaN, then `1=weak_order_less(x, y) == true`;
* If both `x` and `y` are NaNs with the same sign, then `1=(weak_order_less(x, y) , i.e. all NaNs with the same sign are equivalent.

## Example

