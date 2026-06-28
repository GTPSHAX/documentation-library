---
title: operator==(ranges::chunk_view::outer-iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/outer_iterator/operator_cmp
---


# 1=operator==small|(ranges::chunk_view::''outer-iterator'')

ddcl|since=c++23|1=
friend constexpr bool
operator==( const /*outer-iterator*/& x, std::default_sentinel_t );
Compares the `iterator` and the sentinel.
Let  be the underlying pointer to enclosing `chunk_view`. Equivalent to:

```cpp
return *x.parent_->current_ == ranges::end(x.parent_->base_) and x.parent_->remainder_ != 0;
```


## Parameters


### Parameters

- `x` - `iterator` to compare

## Return value

The result of comparison.
