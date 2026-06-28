---
title: std::relation
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/relation
---


```cpp
**Header:** `<`concepts`>`
dcl|since=c++20|num=1|1=
template< class R, class T, class U >
concept relation =
std::predicate<R, T, T> && std::predicate<R, U, U> &&
std::predicate<R, T, U> && std::predicate<R, U, T>;
```

The concept `relation<R, T, U>` specifies that `R` defines a binary relation over the set of expressions whose type and value category are those encoded by either `T` or `U`.

## References

