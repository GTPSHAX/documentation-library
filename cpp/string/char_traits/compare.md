---
title: std::char_traits::compare
type: Strings
source: https://en.cppreference.com/w/cpp/string/char_traits/compare
---

ddcl|notes=<sup>(constexpr C++17)</sup>|
static int compare( const char_type* s1, const char_type* s2,
std::size_t count );
Compares the first `count` characters of the character strings `s1` and `s2`. The comparison is done lexicographically.
If `count` is zero, strings are considered equal.
See *CharTraits* for the general requirements on character traits for `X::compare`.

## Parameters


### Parameters

- `s1, s2` - pointers to character strings to compare
- `count` - the number of characters to compare from each character string

## Return value

Negative value if `s1` is ''less than'' `s2`.
`0` if `s1` is ''equal to'' `s2`.
Positive value if `s1` is ''greater than'' `s2`.

## Complexity

Linear in `count`.

## Note

The return value is determined by lexicographical order. Formally, the return value is determined as follows:
* If for each `i` in [0, count), `eq(s1[i], s2[i])` is `true`, then return `0`.
* Otherwise, if for some `i` in [0, count), `lt(s1[i], s2[i])` is `true` and for every `j` in [0, i), `eq(s1[j], s2[j])` is `true`, then return a negative value.
* Otherwise, return a positive value.

## See also


| cpp/string/char_traits/dsc cmp | (see dedicated page) |

