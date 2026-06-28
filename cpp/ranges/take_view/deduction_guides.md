---
title: deduction guides for std::ranges::take_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/take_view/deduction_guides
---


# deduction guides for tt|std::ranges::take_view


```cpp
**Header:** `<`ranges`>`
dcl|since=c++20|1=
template< class R >
take_view( R&&, ranges::range_difference_t<R> ) -> take_view<views::all_t<R>>;
```

The deduction guide is provided for `std::ranges::take_view` to allow deduction from  and number of elements.

## Example


## Defect reports

