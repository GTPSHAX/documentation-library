---
title: deduction guides for std::optional
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/optional/deduction_guides
---


# deduction guides for tt|std::optional


```cpp
**Header:** `<`optional`>`
dcl|since=c++17|
template< class T >
optional(T) -> optional<T>;
```

One deduction guide is provided for `std::optional` to account for the edge cases missed by the implicit deduction guides, in particular, non-copyable arguments and array to pointer conversion.

## Example

