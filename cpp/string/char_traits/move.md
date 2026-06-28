---
title: std::char_traits::move
type: Strings
source: https://en.cppreference.com/w/cpp/string/char_traits/move
---

ddcl|notes=<sup>(constexpr C++20)</sup>|
static char_type*
move( char_type* dest, const char_type* src, std::size_t count );
Copies `count` characters from the character string pointed to by `src` to the character string pointed to by `dest`.
Performs correctly even if the ranges [src, src + count) and [dest, dest + count) overlap.
See *CharTraits* for the general requirements on character traits for `X::move`.

## Parameters


### Parameters

- `dest` - pointer to a character string to copy to
- `src` - pointer to a character string to copy from
- `count` - the number of characters to copy

## Return value

`dest`

## Exceptions

Throws nothing.

## Complexity

Linear in `count`.

## Defect reports

