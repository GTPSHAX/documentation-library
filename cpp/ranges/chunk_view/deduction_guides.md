---
title: deduction guides for std::ranges::chunk_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/deduction_guides
---


# deduction guides for tt|std::ranges::chunk_view

ddcl|header=ranges|since=c++23|
template< class R >
chunk_view( R&&, ranges::range_difference_t<R> ) -> chunk_view<views::all_t<R>>;
The deduction guide is provided for `ranges::chunk_view` only if `V` models the . This guide allows deduction from  and number of elements.

## Example

