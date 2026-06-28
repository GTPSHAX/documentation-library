---
title: std::char_traits::to_char_type
type: Strings
source: https://en.cppreference.com/w/cpp/string/char_traits/to_char_type
---

ddcl|notes=<sup>(constexpr C++11)</sup><br>|
static char_type to_char_type( int_type c );
Converts `c` to `char_type`. If there is no equivalent `char_type` value (such as when `c` is a copy of the  value), the result is unspecified.
See *CharTraits* for the general requirements on character traits for `X::to_char_type`.

## Parameters


### Parameters

- `c` - value to convert

## Return value

A value equivalent to `c`.

## Complexity

Constant.
