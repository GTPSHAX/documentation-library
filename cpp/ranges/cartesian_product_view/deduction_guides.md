---
title: deduction guides for std::ranges::cartesian_product_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/cartesian_product_view/deduction_guides
---


# deduction guides for tt|std::ranges::cartesian_product_view

ddcl|header=ranges|since=c++23|
template< class... Rs >
cartesian_product_view( Rs&&... ) ->
cartesian_product_view<views::all_t<Rs>...>;
The deduction guide is provided for `std::ranges::cartesian_product_view` to allow deduction from s.

## Example

