---
title: deduction guides for std::ranges::chunk_by_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_by_view/deduction_guides
---


# deduction guides for tt|std::ranges::chunk_by_view


```cpp
dcl|since=c++23|1=
template< class R, class Pred >
chunk_by_view( R&&, Pred ) -> chunk_by_view<views::all_t<R>, Pred>;
```

The deduction guide is provided for `std::ranges::chunk_by_view` to allow deduction from  and predicate function.

## Example

