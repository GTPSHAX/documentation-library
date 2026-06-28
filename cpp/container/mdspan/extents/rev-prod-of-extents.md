---
title: std::extents::rev-prod-of-extents
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/extents/rev-prod-of-extents
---

ddcl|since=c++23|notes=|
constexpr std::size_t /*rev-prod-of-extents*/( rank_type i ) const noexcept;
Returns the product of the sizes of extents with index greater than `i`. The behavior is undefined if `i < rank()` is `false`.

## Parameters


### Parameters

- `i` - an index above which the sizes of corresponding extents will be multiplied together

## Return value

If `i + 1 < rank()` is `true`, return the product of  for all `k` in range , otherwise `1`.

## See also


| cpp/container/mdspan/extents/dsc fwd-prod-of-extents | (see dedicated page) |

