---
title: std::match_results::length
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/match_results/length
---

ddcl|since=c++11|1=
difference_type length( size_type n = 0 ) const;
Returns the length of the specified sub-match.
If `1=n == 0`, the length of the entire matched expression is returned.
If `n > 0 && n < size()`, the length of `n` sub-match is returned.
if `1=n >= size()`, a length of the unmatched match is returned.
The call is equivalent to `(*this)[n].length()`.

## Parameters


### Parameters

- `n` - integral number specifying which match to examine

## Return value

The length of the specified match or sub-match.

## Example

