---
title: std::unsigned_integral
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/unsigned_integral
---

ddcl|header=concepts|since=c++20|1=
template< class T >
concept unsigned_integral = std::integral<T> && !std::signed_integral<T>;
The concept `unsigned_integral<T>` is satisfied if and only if `T` is an integral type and `std::is_signed_v<T>` is `false`.

## Notes

`unsigned_integral<T>` may be satisfied by a type that is not an unsigned integer type, for example, `bool`.

## Example


## References


## See also


| cpp/types/dsc is_integral | (see dedicated page) |
| cpp/types/dsc is_signed | (see dedicated page) |

