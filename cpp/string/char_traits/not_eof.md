---
title: std::char_traits::not_eof
type: Strings
source: https://en.cppreference.com/w/cpp/string/char_traits/not_eof
---

ddcl|notes=<sup>(constexpr C++11)</sup><br>|
static int_type not_eof( int_type e );
Given `e`, produces a suitable value that is not equivalent to .
This function is typically used when a value other than  needs to be returned, such as in implementations of `std::basic_streambuf::overflow()`.
See *CharTraits* for the general requirements on character traits for `X::not_eof`.

## Parameters


### Parameters

- `e` - value to analyze

## Return value

`e` if `e` and  value are not equivalent, or some other non-eof value otherwise.

## Complexity

Constant.

## See also


| cpp/string/char_traits/dsc eof | (see dedicated page) |

