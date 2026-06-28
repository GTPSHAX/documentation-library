---
title: deduction guides for std::ranges::transform_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/transform_view/deduction_guides
---


# deduction guides for tt|std::ranges::transform_view


```cpp
dcl | since=c++20 |1=
template< class R, class F >
transform_view( R&&, F ) -> transform_view<views::all_t<R>, F>;
```

The deduction guide is provided for `std::ranges::transform_view` to allow deduction from  and transformation function.

## Example

