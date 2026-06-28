---
title: std::strict_weak_order
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/strict_weak_order
---


```cpp
**Header:** `<`concepts`>`
dcl|since=c++20|1=
template< class R, class T, class U >
concept strict_weak_order = std::relation<R, T, U>;
```

The concept `strict_weak_order<R, T, U>` specifies that the  `R` imposes a strict weak ordering on its arguments.

## Semantic requirements

A relation `r` is a strict weak ordering if
* it is irreflexive: for all `x`, `r(x, x)` is `false`;
* it is transitive: for all `a`, `b` and `c`, if `r(a, b)` and `r(b, c)` are both `true` then `r(a, c)` is `true`;
* let `e(a, b)` be `!r(a, b) && !r(b, a)`, then `e` is transitive: `e(a, b) && e(b, c)` implies `e(a, c)`.
Under these conditions, it can be shown that `e` is an equivalence relation, and `r` induces a strict total ordering on the equivalence classes determined by `e`.

## Notes

The distinction between  and `strict_weak_order` is purely semantic.

## References


## See also

* *LessThanComparable*
