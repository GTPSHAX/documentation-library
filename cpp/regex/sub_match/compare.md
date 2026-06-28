---
title: std::sub_match::compare
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/sub_match/compare
---


```cpp
dcl|num=1|since=c++11|
int compare( const sub_match& m ) const;
dcl|num=2|since=c++11|
int compare( const string_type& s ) const;
dcl|num=3|since=c++11|
int compare( const value_type* c ) const;
```

1. Compares two `sub_match`es directly by comparing their underlying character sequences. Equivalent to `str().compare(m.str())`.
2. Compares a `sub_match` with a `std::basic_string`. Equivalent to `str().compare(s)`.
3. Compares a `sub_match` with a null-terminated sequence of the underlying character type pointed to by `s`. Equivalent to `str().compare(c)`.

## Parameters


### Parameters

- `m` - a reference to another sub_match
- `s` - a reference to a string to compare to
- `c` - a pointer to a null-terminated character sequence of the underlying `value_type` to compare to

## Return value

A value less than zero if this `sub_match` is ''less'' than the other character sequence, zero if the both underlying character sequences are equal, greater than zero if this `sub_match` is ''greater'' than the other character sequence.

## Notes

This function is infrequently used directly by application code. Instead, one of the non-member comparison operators is used.

## Example

