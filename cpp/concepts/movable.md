---
title: std::movable
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/movable
---

ddcl|header=concepts|since=c++20|1=
template< class T >
concept movable =
std::is_object_v<T> &&
std::move_constructible<T> &&
std::assignable_from<T&, T> &&
std::swappable<T>;
The concept `movable<T>` specifies that `T` is an object type that can be moved (that is, it can be move constructed, move assigned, and lvalues of type `T` can be swapped).

## References


## See also


| cpp/concepts/dsc copyable | (see dedicated page) |

