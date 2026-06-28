---
title: std::common_with
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/common_with
---

ddcl|header=concepts|since=c++20|1=
template< class T, class U >
concept common_with =
std::same_as<std::common_type_t<T, U>, std::common_type_t<U, T>> &&
requires {
static_cast<std::common_type_t<T, U>>(std::declval<T>());
static_cast<std::common_type_t<T, U>>(std::declval<U>());
} &&
std::common_reference_with<
std::add_lvalue_reference_t<const T>,
std::add_lvalue_reference_t<const U>> &&
std::common_reference_with<
std::add_lvalue_reference_t<std::common_type_t<T, U>>,
std::common_reference_t<
std::add_lvalue_reference_t<const T>,
std::add_lvalue_reference_t<const U>>>;
The concept `common_with<T, U>` specifies that two types `T` and `U` share a ''common type'' (as computed by `std::common_type_t`) to which both can be converted.

## Semantic requirements

T and U model  only if, given equality-preserving expressions `t1`, `t2`, `u1` and `u2` such that `decltype((t1))` and `decltype((t2))` are both `T` and `decltype((u1))` and `decltype((u2))` are both `U`,
* `std::common_type_t<T, U>(t1)` equals `std::common_type_t<T, U>(t2)` if and only if `t1` equals `t2`; and
* `std::common_type_t<T, U>(u1)` equals `std::common_type_t<T, U>(u2)` if and only if `u1` equals `u2`.
In other words, the conversion to the common type must preserve equality.

## References


## See also


| cpp/types/dsc common_type | (see dedicated page) |
| cpp/types/dsc common_reference | (see dedicated page) |
| cpp/concepts/dsc common_reference_with | (see dedicated page) |

