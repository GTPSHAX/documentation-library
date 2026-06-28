---
title: deduction guides for std::ranges::split_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/split_view/deduction_guides
---


# deduction guides for tt|std::ranges::split_view


```cpp
dcl | num=1 | since=c++20 |1=
template< class R, class P >
split_view( R&&, P&& )
-> split_view<views::all_t<R>, views::all_t<P>>;
dcl | num=2 | since=c++20 |1=
template< ranges::input_range R >
split_view( R&&, ranges::range_value_t<R> )
-> split_view<views::all_t<R>, ranges::single_view<ranges::range_value_t<R>>>;
```

These deduction guides are provided for `split_view` to allow deduction from a range and a delimiter.
1. The delimiter is a range of elements.
2. The delimiter is a single element.

## Example

