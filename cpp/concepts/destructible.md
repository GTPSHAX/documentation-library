---
title: std::destructible
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/destructible
---

ddcl|header=concepts|since=c++20|1=
template< class T >
concept destructible = std::is_nothrow_destructible_v<T>;
The concept `destructible` specifies the concept of all types whose instances can safely be destroyed at the end of their lifetime (including reference types).

## Notes

Unlike the *Destructible* named requirement, `std::destructible` requires the destructor to be `noexcept(true)`, not merely non-throwing when invoked, and allows reference types and array types.

## References


## See also


| cpp/types/dsc is_destructible | (see dedicated page) |

