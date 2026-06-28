---
title: std::equivalence_relation
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/equivalence_relation
---


```cpp
**Header:** `<`concepts`>`
dcl|since=c++20|1=
template< class R, class T, class U >
concept equivalence_relation = std::relation<R, T, U>;
```

The concept `equivalence_relation<R, T, U>` specifies that the  `R` imposes an [equivalence relation](https://en.wikipedia.org/wiki/equivalence relation) on its arguments.

## Semantic requirements

A relation `r` is an equivalence relation if
* it is reflexive: for all `x`, `r(x, x)` is `true`;
* it is symmetric: for all `a` and `b`, `r(a, b)` is `true` if and only if `r(b, a)` is `true`;
* it is transitive: `r(a, b) && r(b, c)` implies `r(a, c)`.

## Notes

The distinction between  and `equivalence_relation` is purely semantic.

## References

