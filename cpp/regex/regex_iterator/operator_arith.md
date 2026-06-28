---
title: std::regex_iterator::operators (int)
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_iterator/operator_arith
---


```cpp
dcl|since=c++11|1=
regex_iterator& operator++();
dcl|since=c++11|1=
regex_iterator operator++( int );
```

Advances the iterator on the next match.
At first, a local variable of type `BidirIt` is constructed with the value of `match[0].second`.
If the iterator holds a zero-length match and `start , `*this` is set to end-of-sequence iterator and the function returns.
Otherwise, if the iterator holds a zero-length match the operator invokes the following:
cc|regex_search(start, end, match, *pregex,
flags | regex_constants::match_not_null |
regex_constants::match_continuous);
If the call returns `true`, the function returns.
Otherwise the operator increments `start` and continues as if the most recent match was not a zero-length match.
If the most recent match was not a zero-length match, the operator sets `flags` to `flags  and invokes the following:
If the call returns `false`, the iterator sets `*this` to the end-of-sequence iterator, the function returns.
In all cases in which the call to `regex_search` returns `true`, `match.prefix().first` will be equal to the previous value of `match[0].second` and for each index i in the range [0, match.size()) for which `match[i].matched` is `true`, `match[i].position()` will return `distance(begin, match[i].first)`.
This means that `match[i].position()` gives the offset from the beginning of the target sequence, which is often not the same as the offset from the sequence passed in the call to `regex_search`.
It is unspecified how the implementation makes these adjustments. This means that a compiler may call an implementation-specific search function, in which case a user-defined specialization of `regex_search` will not be called.
The behavior is undefined if the iterator is end-of-sequence iterator.

## Parameters

(none)

## Return value

1. `*this`
2. The previous value of the iterator.
