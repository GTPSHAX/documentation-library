---
title: std::ranges::ssize
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/ssize
---


```cpp
**Header:** `<`ranges`>`
**Header:** `<`iterator`>`
|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */ ssize = /* unspecified */;
}
dcl|since=c++20|
template< class T >
requires /* see below */
constexpr auto ssize( T&& t );
```

Calculates the number of elements in `t` in constant time, and converts the result to a signed type.
Given the subexpression of which `t` denotes the (possibly materialized) result object as `E`:
* If `ranges::size(t)` is ill-formed, `ranges::ssize(E)` is also ill-formed.
* Otherwise, let `Signed` be `<decltype(ranges::size(t))>`:
** If `std::ptrdiff_t` is wider than `Signed`, `ranges::ssize(E)` is expression-equivalent to `static_cast<std::ptrdiff_t>(ranges::size(t))`.
** Otherwise, `ranges::ssize(E)` is expression-equivalent to `static_cast<Signed>(ranges::size(t))`.

## Notes

If `ranges::ssize(e)` is valid for an expression `e`, the return type is a signed-integer-like type.

## Example


### Example


**Output:**
```
ranges::ssize(arr) = 5
ranges::ssize is signed
reversed arr: 5 4 3 2 1
s = -1
```


## Defect reports


## See also


| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc sized_range | (see dedicated page) |
| cpp/iterator/ranges/dsc distance | (see dedicated page) |
| cpp/iterator/dsc size | (see dedicated page) |

