---
title: deduction guides for std::ranges::drop_while_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/drop_while_view/deduction_guides
---


# deduction guides for tt|std::ranges::drop_while_view

ddcl | since=c++20 | header=ranges |
template< class R, class Pred >
drop_while_view( R&&, Pred ) -> drop_while_view<views::all_t<R>, Pred>;
The deduction guide is provided for `std::ranges::drop_while_view` to allow deduction from  and predicate.

## Example

