---
title: deduction guides for std::ranges::stride_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/deduction_guides
---


# deduction guides for tt|std::ranges::stride_view

ddcl|header=ranges|since=c++23|
template< class R >
stride_view( R&&, ranges::range_difference_t<R> ) -> stride_view<views::all_t<R>>;
The deduction guide is provided for `std::ranges::stride_view` to allow deduction from  and number of elements.

## Example

