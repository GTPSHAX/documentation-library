---
title: std::atomic_ref::required_alignment
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_ref/required_alignment
---


```cpp
dcl|since=c++20|
static constexpr std::size_t required_alignment  /*implementation-defined*/;
```

The value of `required_alignment` is the required alignment for an object to be referenced by an atomic reference, which is at least `alignof(T)`.

## Notes

Hardware could require that an object to be referenced by an `atomic_ref<T>` have stricter alignment than other `T` objects, and whether operations on an `atomic_ref` are lock-free can depend on the alignment of the referenced object.
