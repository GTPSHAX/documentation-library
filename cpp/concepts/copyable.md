---
title: std::copyable
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/copyable
---

ddcl|header=concepts|since=c++20|1=
template< class T >
concept copyable =
std::copy_constructible<T> &&
std::movable<T> &&
std::assignable_from<T&, T&> &&
std::assignable_from<T&, const T&> &&
std::assignable_from<T&, const T>;
The concept `copyable<T>` specifies that `T` is a  object type that can also be copied (that is, it supports copy construction and copy assignment).

## References


## See also


| cpp/concepts/dsc movable | (see dedicated page) |

