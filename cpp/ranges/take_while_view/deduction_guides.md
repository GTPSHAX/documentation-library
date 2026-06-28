---
title: deduction guides for std::ranges::take_while_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/take_while_view/deduction_guides
---


# deduction guides for tt|std::ranges::take_while_view

ddcl | since=c++20 | header=ranges |
template< class R, class Pred >
take_while_view( R&&, Pred ) -> take_while_view<views::all_t<R>, Pred>;
The deduction guide is provided for `std::ranges::take_while_view` to allow deduction from  and predicate.

## Example

