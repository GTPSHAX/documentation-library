---
title: std::ranges::transform_view::iterator<Const>::operator[]
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/transform_view/iterator/operator_at
---


```cpp
dcl | since=c++20 |1=
constexpr decltype(auto) operator[]( difference_type n ) const
requires ranges::random_access_range<Base>;
```

Returns the element at specified relative location, after transformation.
Effectively returns `std::invoke(*parent_->fun_, current_[n])`, where `*parent_->fun_` is the transformation function stored in the parent `transform_view`, and `current_` is the underlying iterator into `V`.

## Parameters


### Parameters


## Return value

the transformed element

## Example

