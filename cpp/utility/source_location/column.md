---
title: std::source_location::column
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/source_location/column
---

ddcl | since=c++20 |
constexpr std::uint_least32_t column() const noexcept;
Returns an implementation-defined value representing some offset from the start of the line represented by this object (i.e., the column number). Column numbers are presumed to be 1-indexed.

## Parameters

(none)

## Return value

An implementation-defined value representing some offset from the start of the line represented by this object (i.e., the column number).
An implementation is encouraged to use `0` when the column number is unknown.

## Example


## See also

