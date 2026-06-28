---
title: std::char_traits::eq_int_type
type: Strings
source: https://en.cppreference.com/w/cpp/string/char_traits/eq_int_type
---

ddcl|notes=<sup>(constexpr C++11)</sup><br>|
static bool eq_int_type( int_type c1, int_type c2 );
Checks whether two values of type `int_type` are equal.
See *CharTraits* for the general requirements on character traits for `X::eq_int_type`.

## Parameters


### Parameters

- `c1, c2` - values to compare

## Return value

`true` if `c1` is equal to `c2`, `false` otherwise.

## Complexity

Constant.
