---
title: std::ranges::adjacent_transform_view::iterator<Const>::operator[]
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_transform_view/iterator/operator_at
---

ddcl|since=c++23|
constexpr decltype(auto) operator[]( difference_type n ) const
requires ranges::random_access_range<Base>;
Returns an element at specified relative location.
Let  and  be the data members of the `iterator`. Equivalent to:

```cpp
return apply([&](const auto&... iters) -> decltype(auto)
             {
                return invoke(*parent_->fun_, iters[n]...);
             },
             inner_.current_);
```


## Parameters


### Parameters

- `n` - position relative to current location

## Return value

The element at displacement `n` relative to the current location.

## Example


## See also

