---
title: std::chrono::duration::zero
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/zero
---


```cpp
dcl rev multi|until1=c++20|dcl1=
static constexpr duration zero();
|dcl2=
static constexpr duration zero() noexcept;
```

Returns a zero-length duration.
If the representation `rep` of the duration requires some other implementation to return a zero-length duration, `std::chrono::duration_values` can be specialized to return the desired value.

## Parameters

(none)

## Return value

Returns `duration(std::chrono::duration_values<rep>::zero())`.

## Example


## See also


| cpp/chrono/duration/dsc min | (see dedicated page) |
| cpp/chrono/duration/dsc max | (see dedicated page) |

