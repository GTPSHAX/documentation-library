---
title: std::constructible_from
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/constructible_from
---

ddcl|header=concepts|since=c++20|1=
template< class T, class... Args >
concept constructible_from =
std::destructible<T> && std::is_constructible_v<T, Args...>;
The `constructible_from` concept specifies that a variable of type `T` can be initialized with the given set of argument types `Args...`.

## References


## See also


| cpp/types/dsc is_constructible | (see dedicated page) |

