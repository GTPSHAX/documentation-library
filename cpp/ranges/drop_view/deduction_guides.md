---
title: deduction guides for std::ranges::drop_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/drop_view/deduction_guides
---


# deduction guides for tt|std::ranges::drop_view

ddcl | header=ranges | since=c++20 |
template< class R >
drop_view( R&&, ranges::range_difference_t<R> ) -> drop_view<views::all_t<R>>;
The deduction guide is provided for `std::ranges::drop_view` to allow deduction from  and number of elements.

## Example

