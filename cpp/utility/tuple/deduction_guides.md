---
title: deduction guides for std::tuple
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple/deduction_guides
---


# deduction guides for tt|std::tuple


```cpp
**Header:** `<`tuple`>`
dcl | num=1 | since=c++17 |
template<class... UTypes>
tuple(UTypes...) -> tuple<UTypes...>;
dcl | num=2 | since=c++17 |
template<class T1, class T2>
tuple(std::pair<T1, T2>) -> tuple<T1, T2>;
dcl | num=3 | since=c++17 |
template<class Alloc, class... UTypes>
tuple(std::allocator_arg_t, Alloc, UTypes...) -> tuple<UTypes...>;
dcl | num=4 | since=c++17 |
template<class Alloc, class T1, class T2>
tuple(std::allocator_arg_t, Alloc, std::pair<T1, T2>) -> tuple<T1, T2>;
dcl | num=5 | since=c++17 |
template<class Alloc, class... UTypes>
tuple(std::allocator_arg_t, Alloc, tuple<UTypes...>) -> tuple<UTypes...>;
```

These deduction guides are provided for `std::tuple` to account for the edge cases missed by the implicit deduction guides, in particular, non-copyable arguments and array to pointer conversion.

## Example

