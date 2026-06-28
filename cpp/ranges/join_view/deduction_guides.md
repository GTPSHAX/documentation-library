---
title: deduction guides for std::ranges::join_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view/deduction_guides
---


# deduction guides for tt|std::ranges::join_view


```cpp
dcl | since=c++20 |1=
template<class R>
explicit join_view(R&&) -> join_view<views::all_t<R>>;
```

The deduction guide is provided for `std::ranges::join_view` to allow deduction from .

## Example

