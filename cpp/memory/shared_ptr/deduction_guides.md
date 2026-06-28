---
title: deduction guides for std::shared_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/shared_ptr/deduction_guides
---


# deduction guides for tt|std::shared_ptr


```cpp
**Header:** `<`memory`>`
dcl|num=1|since=c++17|
template< class T >
shared_ptr( std::weak_ptr<T> ) -> shared_ptr<T>;
dcl|num=2|since=c++17|
template< class T, class D >
shared_ptr( std::unique_ptr<T, D> ) -> shared_ptr<T>;
```

These deduction guides are provided for `std::shared_ptr` to account for the edge cases missed by the implicit deduction guides.
Note that there is no class template argument deduction from pointer types because it is impossible to distinguish pointers obtained from array and non-array forms of `new`.

## Example

