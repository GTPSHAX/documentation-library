---
title: std::three_way_comparable_with
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/compare/three_way_comparable
---


```cpp
**Header:** `<`compare`>`
dcl|since=c++20|num=1|1=
template< class T, class Cat = std::partial_ordering >
concept three_way_comparable =
__WeaklyEqualityComparableWith<T, T> &&
__PartiallyOrderedWith<T, T> &&
requires(const std::remove_reference_t<T>& a,
const std::remove_reference_t<T>& b) {
{ a <=> b } -> __ComparesAs<Cat>;
};
dcl|since=c++20|num=2|1=
template< class T, class U, class Cat = std::partial_ordering >
concept three_way_comparable_with =
std::three_way_comparable<T, Cat> &&
std::three_way_comparable<U, Cat> &&
__ComparisonCommonTypeWith<T, U> &&
std::three_way_comparable<
std::common_reference_t<
const std::remove_reference_t<T>&,
const std::remove_reference_t<U>&>, Cat> &&
__WeaklyEqualityComparableWith<T, U> &&
__PartiallyOrderedWith<T, U> &&
requires(const std::remove_reference_t<T>& t,
const std::remove_reference_t<U>& u) {
{ t <=> u } -> __ComparesAs<Cat>;
{ u <=> t } -> __ComparesAs<Cat>;
};
|num=3|1=
template< class T, class Cat >
concept __ComparesAs =
std::same_as<std::common_comparison_category_t<T, Cat>, Cat>;
```

1. The concept `std::three_way_comparable` specifies that the three way comparison operator `1=<=>` on `T` yield results consistent with the comparison category implied by `Cat`.
2. The concept `std::three_way_comparable_with` specifies that the three way comparison operator `1=<=>` on (possibly mixed) `T` and `U` operands yield results consistent with the comparison category implied by `Cat`. Comparing mixed operands yields results equivalent to comparing the operands converted to their common type.
`cpp/concepts/equality_comparable|''__WeaklyEqualityComparableWith''`, `cpp/concepts/totally_ordered|''__PartiallyOrderedWith''`, and `cpp/concepts/equality_comparable|''__ComparisonCommonTypeWith''` are exposition-only concepts. See descriptions of  and .

## Semantic requirements

These concepts are modeled only if they are satisfied and all concepts they subsume are modeled.
1. `T` and `Cat` model `std::three_way_comparable<T, Cat>` only if, given lvalues `a` and `b` of type `const std::remove_reference_t<T>`, following are true:
* `1=(a <=> b == 0) == bool(a == b)`,
* `1=(a <=> b != 0) == bool(a != b)`,
* `1=((a <=> b) <=> 0)` and `1=(0 <=> (b <=> a))` are equal,
* `1=bool(a > b) == bool(b < a)`,
* `1=bool(a >= b) == !bool(a < b)`,
* `1=bool(a <= b) == !bool(b < a)`,
* `1=(a <=> b < 0) == bool(a < b)`,
* `1=(a <=> b > 0) == bool(a > b)`,
* `1=(a <=> b <= 0) == bool(a <= b)`, and
* `1=(a <=> b >= 0) == bool(a >= b)`, and
* if `Cat` is convertible to `std::strong_ordering`, `T` models .
2. `T`, `U`, and `Cat` model `std::three_way_comparable_with<T, U, Cat>` only if given
* `t` and `t2`, lvalues denoting distinct equal objects of types `const std::remove_reference_t<T>` and `std::remove_reference_t<T>` respectively, and
* `u` and `u2`, lvalues denoting distinct equal objects of types `const std::remove_reference_t<U>` and `std::remove_reference_t<U>` respectively.
Let `C` be `std::common_reference_t<const std::remove_reference_t<T>&, const std::remove_reference_t<U>&>` and given an expression `E` and a type `C`, let `CONVERT_TO<C>(E)` be:
rrev multi|rev1=
* `static_cast<C>(std::as_const(E))`.
|since2=c++23|rev2=
* `static_cast<const C&>(std::as_const(E))` if that is a valid expression,
* `static_cast<const C&>(std::move(E))` otherwise.
the following are true:
* `1=t <=> u` and `1=u <=> t` have the same domain,
* `1=((t <=> u) <=> 0)` and `1=(0 <=> (u <=> t))` are equal,
* `1=(t <=> u == 0) == bool(t == u)`,
* `1=(t <=> u != 0) == bool(t != u)`,
* `1=Cat(t <=> u) == Cat(CONVERT_TO<C>(t2) <=> CONVERT_TO<C>(u2))`,
* `1=(t <=> u < 0) == bool(t < u)`,
* `1=(t <=> u > 0) == bool(t > u)`,
* `1=(t <=> u <= 0) == bool(t <= u)`,
* `1=(t <=> u >= 0) == bool(t >= u)`, and
* if `Cat` is convertible to `std::strong_ordering`, `T` and `U` model `std::totally_ordered_with<T, U>`.

## See also


| cpp/concepts/dsc equality_comparable | (see dedicated page) |
| cpp/concepts/dsc totally_ordered | (see dedicated page) |

