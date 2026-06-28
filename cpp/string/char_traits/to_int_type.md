---
title: std::char_traits::to_int_type
type: Strings
source: https://en.cppreference.com/w/cpp/string/char_traits/to_int_type
---

ddcl|notes=<sup>(constexpr C++11)</sup><br>|
static int_type to_int_type( char_type c );
Converts `c` to `int_type`.
See *CharTraits* for the general requirements on character traits for `X::to_int_type`.

## Parameters


### Parameters

- `c` - value to convert

## Return value

A value equivalent to `c`.

## Complexity

Constant.

## Notes

For every valid value of `char_type`, there must be a unique value of `int_type` distinct from `eof()`.
