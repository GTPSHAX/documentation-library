---
title: deduction guides for std::ranges::slide_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/slide_view/deduction_guides
---


# deduction guides for tt|std::ranges::slide_view

ddcl|header=ranges|since=c++23|
template< class R >
slide_view( R&&, ranges::range_difference_t<R> ) -> slide_view<views::all_t<R>>;
The deduction guide is provided for `std::ranges::slide_view` to allow deduction from  and number of elements.

## Example

