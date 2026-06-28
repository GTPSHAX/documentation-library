---
title: std::lcm
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/lcm
---

ddcl|header=numeric|since=c++17|
template< class M, class N >
constexpr std::common_type_t<M, N> lcm( M m, N n );
Computes the [least common multiple](https://en.wikipedia.org/wiki/least common multiple) of the integers `m` and `n`.
If either `M` or `N` is not an integer type, or if either is (possibly cv-qualified) `bool`, the program is ill-formed.
The behavior is undefined if `, `, or the least common multiple of ` and ` is not representable as a value of type `std::common_type_t<M, N>`.

## Parameters


### Parameters

- `m, n` - integer values

## Return value

If either `m` or `n` is zero, returns zero. Otherwise, returns the least common multiple of ` and `.

## Exceptions

Throws no exceptions.

## Notes


## Example


### Example


**Output:**
```
lcm(2 * 3, 3 * 4, 4 * 5) = 60
lcm(2 * 3 * 4, 3 * 4 * 5, 4 * 5 * 6) = 120
lcm(2 * 3 * 4, 3 * 4 * 5, 4 * 5 * 6, 5 * 6 * 7) = 840
```


## See also


| cpp/numeric/dsc gcd | (see dedicated page) |

