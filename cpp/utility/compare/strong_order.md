---
title: std::strong_order
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/compare/strong_order
---


```cpp
**Header:** `<`compare`>`
dcl|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */ strong_order = /* unspecified */;
}
dcl|1=
template< class T, class U >
requires /* see below */
constexpr std::strong_ordering strong_order( T&& t, U&& u ) noexcept(/* see below */);
```

Compares two values using 3-way comparison and produces a result of type `std::strong_ordering`.
Let `t` and `u` be expressions and `T` and `U` denote `decltype((t))` and `decltype((u))` respectively, `std::strong_order(t, u)` is expression-equivalent to:
* If `std::is_same_v<std::decay_t<T>, std::decay_t<U>>` is `true`:
** `std::strong_ordering(strong_order(t, u))`, if it is a well-formed expression with overload resolution performed in a context that does not include a declaration of `std::strong_order`,
** otherwise, if `T` is a floating-point type:
*** if `std::numeric_limits<T>::is_iec559` is `true`, performs the ISO/IEC/IEEE 60559 ''totalOrder'' comparison of floating-point values and returns that result as a value of type `std::strong_ordering` (note: this comparison can distinguish between the positive and negative zero and between the NaNs with different representations),
*** otherwise, yields a value of type `std::strong_ordering` that is consistent with the ordering observed by `T`'s comparison operators,
** otherwise, `std::strong_ordering(std::compare_three_way()(t, u))` if it is well-formed.
* In all other cases, the expression is ill-formed, which can result in substitution failure when it appears in the immediate context of a template instantiation.

### Strict total order of IEEE floating-point types

Let `x` and `y` be values of same IEEE floating-point type, and `total_order_less(x, y)` be the boolean result indicating if `x` precedes `y` in the strict total order defined by ''totalOrder'' in ISO/IEC/IEEE 60559.
`1=(total_order_less(x, y)  if and only if `x` and `y` have the same bit pattern.
* if neither `x` nor `y` is NaN:
** if `x < y`, then `1=total_order_less(x, y) == true`;
** if `x > y`, then `1=total_order_less(x, y) == false`;
** if `1=x == y`,
*** if `x` is negative zero and `y` is positive zero, `1=total_order_less(x, y) == true`,
*** if `x` is not zero and `x`'s exponent field is less than `y`'s, then `1=total_order_less(x, y) == (x > 0)` (only meaningful for decimal floating-point number);
* if either `x` or `y` is NaN:
** if `x` is negative NaN and `y` is not negative NaN, then `1=total_order_less(x, y) == true`,
** if `x` is not positive NaN and `y` is positive NaN, then `1=total_order_less(x, y) == true`,
** if both `x` and `y` are NaNs with the same sign and `x`'s mantissa field is less than `y`'s, then `1=total_order_less(x, y) == !std::signbit(x)`.

## Example

