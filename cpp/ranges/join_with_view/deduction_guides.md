---
title: deduction guides for std::ranges::join_with_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_with_view/deduction_guides
---


# deduction guides for tt|std::ranges::join_with_view


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++23|1=
template< class R, class P >
join_with_view( R&&, P&& ) -> join_with_view<views::all_t<R>, views::all_t<P>>;
dcl|num=2|since=c++23|1=
template< class R >
join_with_view( R&&, ranges::range_value_t<ranges::range_reference_t<R>> )
-> join_with_view<views::all_t<R>,
ranges::single_view<
ranges::range_value_t<ranges::range_reference_t<R>>>;
```

These deduction guides are provided for `join_with_view` to allow deduction from a range and a delimiter.
1. The delimiter is a range of elements.
2. The delimiter is a single element.

## Example

