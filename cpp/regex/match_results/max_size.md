---
title: std::match_results::max_size
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/match_results/max_size
---

ddcl|since=c++11|
size_type max_size() const noexcept;
Returns the maximum number of submatches the `match_results` type is able to hold due to system or library implementation limitations, i.e. `std::distance(begin(), end())` for the largest number of submatches.

## Parameters

(none)

## Return value

Maximum number of submatches.

## Complexity

Constant.
