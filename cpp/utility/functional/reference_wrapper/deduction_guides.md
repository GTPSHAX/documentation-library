---
title: deduction guides for std::reference_wrapper
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/reference_wrapper/deduction_guides
---


# deduction guides for tt|std::reference_wrapper


```cpp
**Header:** `<`functional`>`
dcl|since=c++17|
template< typename T >
reference_wrapper( T& ) -> reference_wrapper<T>;
```

One deduction guide is provided for `std::reference_wrapper` to support deduction of the sole class template parameter.

## Example

