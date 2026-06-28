---
title: deduction guides for std::ranges::zip_transform_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_transform_view/deduction_guides
---


# deduction guides for tt|std::ranges::zip_transform_view


```cpp
dcl | since=c++23 |1=
template< class F, class... Rs >
zip_transform_view( F, Rs&&... ) -> zip_transform_view<F, views::all_t<Rs>...>;
```

The deduction guide is provided for `std::ranges::zip_transform_view` to allow deduction from transformation function and s.

## Example

