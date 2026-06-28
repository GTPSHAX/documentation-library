---
title: std::move_constructible
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/move_constructible
---

ddcl|header=concepts|since=c++20|1=
template< class T >
concept move_constructible = std::constructible_from<T, T> && std::convertible_to<T, T>;
The concept `move_constructible` is satisfied if `T` is a reference type, or if it is an object type where an object of that type can be constructed from an rvalue of that type in both direct- and copy-initialization contexts, with the usual semantics.

## Semantic requirements

If `T` is an object type, then `move_constructible<T>` is modeled only if given
* `rv`, an rvalue of type `T`, and
* `u2`, a distinct object of type `T` equal to `rv`,
the following are true:
* After the definition `T u , `u` is equal to `u2`;
* `T(rv)` is equal to `u2`; and
* If `T` is not const-qualified, then `rv`'s resulting state (after the definition/expression is evaluated in either bullets above) is valid but unspecified; otherwise, it is unchanged.

## References


## See also


| cpp/types/dsc is_move_constructible | (see dedicated page) |

