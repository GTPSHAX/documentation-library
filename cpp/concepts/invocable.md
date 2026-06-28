---
title: std::invocable
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/invocable
---


```cpp
**Header:** `<`concepts`>`
dcl|since=c++20|1=
template< class F, class... Args >
concept invocable =
requires(F&& f, Args&&... args) {
std::invoke(std::forward<F>(f), std::forward<Args>(args)...);
/* not required to be equality-preserving */
};
dcl|since=c++20|1=
template< class F, class... Args >
concept regular_invocable = std::invocable<F, Args...>;
```

The `invocable` concept specifies that a callable type `F` can be called with a set of arguments `Args...` using the function template `std::invoke`.
The `regular_invocable` concept adds to the `invocable` concept by requiring the `invoke` expression to be equality-preserving and not modify either the function object or the arguments.

## Notes

The distinction between `invocable` and `regular_invocable` is purely semantic.
A random number generator may satisfy `invocable` but cannot satisfy `regular_invocable` (comical ones excluded).

## References


## See also


| cpp/types/dsc is_invocable | (see dedicated page) |


## External links

