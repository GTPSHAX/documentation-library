---
title: std::signed_integral
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/signed_integral
---

ddcl|header=concepts|since=c++20|1=
template< class T >
concept signed_integral = std::integral<T> && std::is_signed_v<T>;
The concept `signed_integral<T>` is satisfied if and only if `T` is an integral type and `std::is_signed_v<T>` is `true`.

## Notes

`signed_integral<T>` may be satisfied by a type that is not a signed integer type, for example, `char` (on a system where `char` is signed).

## Example


## References


## See also


| cpp/types/dsc is_integral | (see dedicated page) |
| cpp/types/dsc is_signed | (see dedicated page) |

