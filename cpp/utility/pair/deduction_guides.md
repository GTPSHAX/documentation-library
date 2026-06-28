---
title: deduction guides for std::pair
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/pair/deduction_guides
---


# deduction guides for tt|std::pair


```cpp
**Header:** `<`utility`>`
dcl | since=c++17 |
template<class T1, class T2>
pair(T1, T2) -> pair<T1, T2>;
```

One deduction guide is provided for `std::pair` to account for the edge cases missed by the implicit deduction guides, in particular, non-copyable arguments and array to pointer conversion.

## Example

