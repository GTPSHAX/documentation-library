---
title: operators (std::stacktrace_entry)
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/stacktrace_entry/operator_cmp
---


# 1=operator==, operator<=><small>(std::stacktrace_entry)</small>


```cpp
dcl|num=1|since=c++23|1=
friend constexpr bool operator==( const stacktrace_entry& lhs,
const stacktrace_entry& rhs ) noexcept;
dcl|num=2|since=c++23|1=
friend constexpr std::strong_ordering
operator<=>( const stacktrace_entry& lhs, const stacktrace_entry& rhs ) noexcept;
```

1. Compares `lhs` and `rhs` for equality. Two `stacktrace_entry` values are equal if and only if they represent the same stacktrace entry, or both of them are empty.
2. Gets the relative order between `lhs` and `rhs` in the unspecified strict total order over all `stacktrace_entry` values which is consistent with the equality relation established by `1=operator==`.

## Parameters


### Parameters

- `lhs, rhs` - `stacktrace_entry` values to compare

## Return value

1. `true` if two `lhs` and `rhs` compare equal, `false` otherwise.
2. `std::strong_ordering::equal` if `lhs` and `rhs` compare equal.
@@ Otherwise, `std::strong_ordering::less` if `lhs` is ordered before `rhs` in the strict total order.
@@ Otherwise, `std::strong_ordering::greater` (in which case `rhs` is ordered before `lhs` in the strict total order).

## Example

