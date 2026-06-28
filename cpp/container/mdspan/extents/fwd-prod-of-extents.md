---
title: std::extents::fwd-prod-of-extents
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/extents/fwd-prod-of-extents
---

ddcl|since=c++23|notes=|
constexpr std::size_t /*fwd-prod-of-extents*/( rank_type i ) const noexcept;
Returns the product of the sizes of extents with index less than `i`. The behavior is undefined if `1=i <= rank()` is `false`.

## Parameters


### Parameters

- `i` - The end index of the range of extents to be multiplied together.

## Return value

If `i > 0` is `true`, return the product of  for all `k` in range , otherwise `1`.

## See also


| cpp/container/mdspan/extents/dsc rev-prod-of-extents | (see dedicated page) |

