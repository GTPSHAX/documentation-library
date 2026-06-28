---
title: std::equality_comparable
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/equality_comparable
---


```cpp
**Header:** `<`concepts`>`
dcl|num=1|since=c++20|1=
template< class T >
concept equality_comparable = __WeaklyEqualityComparableWith<T, T>;
dcl|num=2|since=c++20|1=
template< class T, class U >
concept equality_comparable_with =
std::equality_comparable<T> &&
std::equality_comparable<U> &&
__ComparisonCommonTypeWith<T, U> &&
std::equality_comparable<
std::common_reference_t<
const std::remove_reference_t<T>&,
const std::remove_reference_t<U>&>> &&
__WeaklyEqualityComparableWith<T, U>;
|1=
template< class T, class U >
concept __WeaklyEqualityComparableWith =
requires(const std::remove_reference_t<T>& t,
const std::remove_reference_t<U>& u) {
{ t == u } -> boolean-testable;
{ t != u } -> boolean-testable;
{ u == t } -> boolean-testable;
{ u != t } -> boolean-testable;
};
dcl rev multi|num=4|until1=c++23|notes1=|dcl1=
template< class T, class U >
concept __ComparisonCommonTypeWith =
std::common_reference_with<
const std::remove_reference_t<T>&,
const std::remove_reference_t<U>&>;
|notes2=|dcl2=
template< class T, class U, class C = std::common_reference_t<const T&, const U&> >
concept _ComparisonCommonTypeWithImpl =
std::same_as<std::common_reference_t<const T&, const U&>,
std::common_reference_t<const U&, const T&>> &&
requires {
requires std::convertible_to<const T&, const C&>
std::convertible_to<T, const C&>;
requires std::convertible_to<const U&, const C&>
std::convertible_to<U, const C&>;
};
template< class T, class U >
concept __ComparisonCommonTypeWith =
_ComparisonCommonTypeWithImpl<std::remove_cvref_t<T>, std::remove_cvref_t<U>>;
```

1. The concept `std::equality_comparable` specifies that the comparison operators `1===` and `1=!=` on `T` reflects equality: `1===` yields `true` if and only if the operands are equal.
2. The concept `std::equality_comparable_with` specifies that the comparison operators `1===` and `1=!=` on (possibly mixed) `T` and `U` operands yield results consistent with equality. Comparing mixed operands yields results equivalent to comparing the operands converted to their common type.
3. The exposition-only concept `''__WeaklyEqualityComparableWith''` specifies that an object of type `T` and an object of type `U` can be compared for equality with each other (in either order) using both `1===` and `1=!=`, and the results of the comparisons are consistent.
4. The exposition-only concept `''__ComparisonCommonTypeWith''` specifies that two types share a common type, and a const lvalue<sup>(since C++23)</sup>  or a non-const rvalue of either type is convertible to that common type.

## Semantic requirements

These concepts are modeled only if they are satisfied and all concepts they subsume are modeled.
In the following paragraphs, given an expression `E` and a type `C`, `CONVERT_TO<C>(E)` is defined as:
rrev multi|rev1=
* `static_cast<C>(std::as_const(E))`.
|since2=c++23|rev2=
* `static_cast<const C&>(std::as_const(E))` if that is a valid expression,
* `static_cast<const C&>(std::move(E))` otherwise.
1.  is modeled only if, given objects `a` and `b` of type `T`, `1=bool(a == b)` is `true` if and only if `a` and `b` are equal. Together with the requirement that `1=a == b` is equality-preserving, this implies that `1===` is symmetric and transitive, and further that `1===` is reflexive for all objects `a` that are equal to at least one other object.
2.  is modeled only if, let
* `t` and `t2` be lvalues denoting distinct equal objects of types `const std::remove_reference_t<T>` and `std::remove_cvref_t<T>` respectively,
* `u` and `u2` be lvalues denoting distinct equal objects of types `const std::remove_reference_t<U>` and `std::remove_cvref_t<U>` respectively,
* `C` be `std::common_reference_t<const std::remove_reference_t<T>&, const std::remove_reference_t<U>&>`,
the following expression is true:
* `1=bool(t == u) == bool(CONVERT_TO<C>(t2) == CONVERT_TO<C>(u2))`.
3. `__WeaklyEqualityComparableWith<T, U>` is modeled only if given
* `t`, an lvalue of type `const std::remove_reference_t<T>` and
* `u`, an lvalue of type `const std::remove_reference_t<U>`,
the following are true:
* `1=t == u`, `1=u == t`, `1=t != u`, `1=u != t` have the same domain;
* `1=bool(u == t) == bool(t == u)`;
* `1=bool(t != u) == !bool(t == u)`; and
* `1=bool(u != t) == bool(t != u)`.
4. `__WeaklyEqualityComparableWith<T, U>` is modeled only if:
rrev multi|rev1=The corresponding  concept is modeled.
|since2=c++23|rev2=
Let
* `C` be `std::common_reference_t<const T&, const U&>`,
* `t1` and `t2` be equality-preserving expressions that are lvalues of type `std::remove_cvref_t<T>`,
* `u1` and `u2` be equality-preserving expressions that are lvalues of type `std::remove_cvref_t<U>`,
the following conditions hold:
* `CONVERT_TO<C>(t1)` equals `CONVERT_TO<C>(t2)` if and only if `t1` equals `t2`; and
* `CONVERT_TO<C>(u1)` equals `CONVERT_TO<C>(u2)` if and only if `u1` equals `u2`.

## References

