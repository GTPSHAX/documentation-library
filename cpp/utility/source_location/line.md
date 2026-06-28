---
title: std::source_location::line
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/source_location/line
---

ddcl | since=c++20 |
constexpr std::uint_least32_t line() const noexcept;
Returns the line number represented by this object.

## Parameters

(none)

## Return value

The line number represented by this object.
An implementation is encouraged to return `0` when the line number is unknown.

## Example


## See also

