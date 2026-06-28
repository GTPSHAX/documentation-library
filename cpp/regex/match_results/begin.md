---
title: std::match_results::cbegin
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/match_results/begin
---


```cpp
dcl|since=c++11|
iterator begin() noexcept;
dcl|since=c++11|
const_iterator begin() const noexcept;
dcl|since=c++11|
const_iterator cbegin() const noexcept;
```

Returns an iterator to the beginning of the list of sub-matches. If match was successful, the iterator will point to the entire matched expression.

## Parameters

(none)

## Return value

Iterator to the first sub-match.

## Complexity

Constant.

## See also


| cpp/regex/match_results/dsc end | (see dedicated page) |

