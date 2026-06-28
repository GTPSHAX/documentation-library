---
title: std::assume_aligned
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/assume_aligned
---

ddcl|header=memory|since=c++20|1=
template< std::size_t N, class T >
constexpr T* assume_aligned( T* ptr );
Informs the implementation that the object `ptr` points to is aligned to at least `N`. The implementation may use this information to generate more efficient code, but it might only make this assumption if the object is accessed via the return value of `assume_aligned`.
`N` must be a power of 2. The behavior is undefined if `ptr` does not point to an object of type `T` (ignoring cv-qualification at every level), or if the object's alignment is not at least `N`.

## Return value

`ptr`.

## Exceptions

Throws nothing.

## Notes

To ensure that the program benefits from the optimizations enabled by `assume_aligned`, it is important to access the object via its return value:

```cpp
void f(int* p)
{
    int* p1 = std::assume_aligned<256>(p);
    // Use p1, not p, to ensure benefit from the alignment assumption.
    // However, the program has undefined behavior if p is not aligned
    // regardless of whether p1 is used.
}
```

It is up to the program to ensure that the alignment assumption actually holds. A call to `assume_aligned` does not cause the compiler to verify or enforce this.

## Example

