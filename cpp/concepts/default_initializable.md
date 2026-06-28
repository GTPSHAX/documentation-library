---
title: std::default_initializable
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/default_initializable
---

ddcl|header=concepts|since=c++20|1=
template< class T >
concept default_initializable = std::constructible_from<T> && requires { T{}; } &&
/* T t; is well-formed, see below */;
The `default_initializable` concept checks whether variables of type `T` can be
* value-initialized (i.e., whether `T()` is well-formed);
* direct-list-initialized from an empty initializer list (i.e., whether } is well-formed); and
* default-initialized (i.e., whether `T t;` is well-formed).
Access checking is performed as if in a context unrelated to T. Only the validity of the immediate context of the variable initialization is considered.

## Possible implementation

eq fun|1=
template<class T>
concept default_initializable =
std::constructible_from<T> &&
requires { T{}; ::new T; };

## References


## See also


| cpp/concepts/dsc constructible_from | (see dedicated page) |
| cpp/types/dsc is_default_constructible | (see dedicated page) |

