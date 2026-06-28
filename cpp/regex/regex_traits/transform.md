---
title: std::regex_traits::transform
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_traits/transform
---


```cpp
dcl|1=
template< class ForwardIt >
string_type transform( ForwardIt first, ForwardIt last) const;
```

Obtains the sort key for the character sequence [first, last), such that if a sort key compares less than another sort key with `operator<`, then the character sequence that produced the first sort key comes before the character sequence that produced the second sort key, in the currently imbued locale's collation order.
For example, when the regex flag `std::regex_constants::collate` is set, then the sequence `[a-b]` would match some character `c1` if `1=traits.transform("a") <= traits.transform(c1) <= traits.transform("b")`. Note that this function takes a character sequence as the argument to accommodate to the ranges defined like `[``[.ae.]-d]`.
Standard library specializations of `std::regex_traits` return `std::use_facet<std::collate<CharT>>(getloc()).transform(str.data(), str.data() + str.length())` for some temporary string `str` constructed as `string_type str(first, last)`.

## Parameters


### Parameters

- `first, last` - a pair of *ForwardIterator*s which determines the sequence of characters to compare

**Type requirements:**

- `ForwardIt`

## Return value

The collation key for the character sequence [first, last) in the currently imbued locale.

## Example

