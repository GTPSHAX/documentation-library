---
title: deduction guides for std::ranges::enumerate_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/enumerate_view/deduction_guides
---


# deduction guides for tt|std::ranges::enumerate_view

ddcl|since=c++23|header=ranges|
template< class R >
enumerate_view( R&& ) -> enumerate_view<views::all_t<R>>;
The deduction guide is provided for `std::ranges::enumerate_view` to allow deduction from .

## Example

