---
title: std::copy_constructible
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/copy_constructible
---

ddcl|header=concepts|since=c++20|1=
template< class T >
concept copy_constructible =
std::move_constructible<T> &&
std::constructible_from<T, T&> && std::convertible_to<T&, T> &&
std::constructible_from<T, const T&> && std::convertible_to<const T&, T> &&
std::constructible_from<T, const T> && std::convertible_to<const T, T>;
The concept `copy_constructible` is satisfied if `T` is an lvalue reference type, or if it is a  object type where an object of that type can constructed from a (possibly const) lvalue or const rvalue of that type in both direct- and copy-initialization contexts with the usual semantics (a copy is constructed with the source unchanged).

## Semantic requirements

If `T` is an object type, then `copy_constructible<T>` is modeled only if given
* `v`, an lvalue of type (possibly `const`) `T` or an rvalue of type `const T`,
the following are true:
* After the definition `1=T u = v;`, `u` is equal to `v` and `v` is not modified;
* `T(v)` is equal to `v` and does not modify `v`.

## References


## See also


| cpp/types/dsc is_copy_constructible | (see dedicated page) |

