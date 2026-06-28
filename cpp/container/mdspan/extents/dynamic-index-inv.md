---
title: std::extents::dynamic-index-inv
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/extents/dynamic-index-inv
---

ddcl|since=c++23|notes=|
private:
static constexpr auto /*dynamic-index-inv*/( rank_type i ) noexcept;
Returns the number `r` such that in range  there are exactly  dynamic extents. If `1=i <= rank_dynamic()` is `false`, the behavior is undefined.

## Parameters


### Parameters

- `i` - the index

## Return value

The minimum value of  such that  is `true`.

## See also

