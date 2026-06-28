---
title: std::match_results::empty
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/match_results/empty
---


```cpp
dcl|since=c++11|
bool empty() const;
```

Checks whether the match was successful.

## Parameters

(none)

## Return value

`true` if `*this` represents the result of a failed match, `false` otherwise, i.e. `1= size() == 0`.

## Complexity

Constant.

## See also


| cpp/regex/match_results/dsc size | (see dedicated page) |

