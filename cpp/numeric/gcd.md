---
title: std::gcd
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/gcd
---

ddcl|header=numeric|since=c++17|
template< class M, class N >
constexpr std::common_type_t<M, N> gcd( M m, N n );
Computes the [greatest common divisor](https://en.wikipedia.org/wiki/greatest common divisor) of the integers `m` and `n`.
If either `M` or `N` is not an integer type, or if either is (possibly cv-qualified) `bool`, the program is ill-formed.
If either ` or ` is not representable as a value of type `std::common_type_t<M, N>`, the behavior is undefined.

## Parameters


### Parameters

- `m, n` - integer values

## Return value

If both `m` and `n` are zero, returns zero. Otherwise, returns the greatest common divisor of ` and `.

## Exceptions

Throws no exceptions.

## Notes


## Example


## See also


| cpp/numeric/dsc lcm | (see dedicated page) |

