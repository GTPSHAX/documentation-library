---
title: operator==(ranges::chunk_view::inner-iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/inner_iterator/operator_cmp
---


# 1=operator==small|(ranges::chunk_view::''inner-iterator'')

ddcl|since=c++23|1=
friend constexpr bool operator==( const /*inner-iterator*/& x,
std::default_sentinel_t );
Compares the `iterator` and the sentinel.
Let  be the underlying pointer to enclosing `chunk_view`.
Equivalent to: `1=returns x.parent_->remainder_ == 0;`

## Parameters


### Parameters

- `x` - `iterator` to compare

## Return value

The result of comparison.
