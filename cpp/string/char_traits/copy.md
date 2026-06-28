---
title: std::char_traits::copy
type: Strings
source: https://en.cppreference.com/w/cpp/string/char_traits/copy
---

ddcl|notes=<sup>(constexpr C++20)</sup>|
static char_type*
copy( char_type* dest, const char_type* src, std::size_t count );
Copies `count` characters from the character string pointed to by `src` to the character string pointed to by `dest`.
If [dest, dest + count) and [src, src + count) overlap, the behavior is undefined.
See *CharTraits* for the general requirements on character traits for `X::copy`.

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

## See also


| cpp/string/char_traits/dsc assign | (see dedicated page) |

