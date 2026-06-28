---
title: deduction guides for std::ranges::zip_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_view/deduction_guides
---


# deduction guides for tt|std::ranges::zip_view


```cpp
dcl | since=c++23 |1=
template< class... Rs >
zip_view( Rs&&... ) -> zip_view<views::all_t<Rs>...>;
```

The deduction guide is provided for `std::ranges::zip_view` to allow deduction from s.

## Example

