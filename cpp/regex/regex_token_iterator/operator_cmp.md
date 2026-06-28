---
title: std::regex_token_iterator::operators (operator!=)
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_token_iterator/operator_cmp
---


```cpp
dcl|num=1|since=c++11|1=
bool operator==( const regex_token_iterator& other ) const;
dcl|num=2|since=c++11|until=c++20|1=
bool operator!=( const regex_token_iterator& other ) const;
```

Checks whether `*this` and `other` are equivalent.
Two regex token iterators are equal if:
@a@ They are both end-of-sequence iterators.
@b@ They are both suffix iterators and the suffixes are equal.
@c@ Neither of them is end-of-sequence or suffix iterator and:
::* `1=position == other.position`
::* `1=N == other.N`
::* `1=subs == other.subs`
1. Checks whether `*this` is ''equal to'' `other`.
2. Checks whether `*this` is ''not equal to'' `other`.
rrev|since=c++20|
> **TODO:** Explain better. For example, `subs` is an exposition-only vector of matched sub-expressions.

## Parameters


### Parameters

- `other` - another regex token iterator to compare to

## Return value

1. `true` if `*this` is ''equal to'' `other`, `false` otherwise.
2. `true` if `*this` is ''not equal to'' `other`, `false` otherwise.
