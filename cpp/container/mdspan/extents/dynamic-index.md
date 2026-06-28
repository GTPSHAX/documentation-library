---
title: std::extents::dynamic-index
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/extents/dynamic-index
---

ddcl|since=c++23|notes=|
private:
static constexpr auto /*dynamic-index*/( rank_type i ) noexcept;
Returns the number of dynamic extents below index `i`. If `1=i <= rank()` is `false`, the behavior is undefined.

## Parameters


### Parameters

- `i` - the index

## Return value

The number of  with `r < i` for which  is a dynamic extent.

## See also

