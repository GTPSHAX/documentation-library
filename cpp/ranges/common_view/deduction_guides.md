---
title: deduction guides for std::ranges::common_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/common_view/deduction_guides
---


# deduction guides for tt|std::ranges::common_view

ddcl|since=c++20|header=ranges|
template< class R >
common_view( R&& ) -> common_view<views::all_t<R>>;
The deduction guide is provided for `std::ranges::common_view` to allow deduction from .

## Example

