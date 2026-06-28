---
title: std::char_traits::eq/lt
type: Strings
source: https://en.cppreference.com/w/cpp/string/char_traits/cmp
---


```cpp
<br>|
static bool eq( char_type a, char_type b );
<br>|
static bool lt( char_type a, char_type b );
```

Compares two characters.
1. Compares `a` and `b` for equality, behaves identically to
* `1=static_cast<unsigned char>(a) == static_cast<unsigned char>(b)`, if `char_type` is `char`,
* `1=a == b` otherwise.
2. Compares `a` and `b` in such a way that they are totally ordered, behaves identically to
* `static_cast<unsigned char>(a) < static_cast<unsigned char>(b)`, if `char_type` is `char`,
* `a < b` otherwise.
See *CharTraits* for the general requirements on character traits for `X::eq` and `X::lt`.

## Parameters


### Parameters

- `a, b` - character values to compare

## Return value

1. `true` if `a` and `b` are equal, `false` otherwise.
2. `true` if `a` is less than `b`, `false` otherwise.

## Complexity

Constant.

## Defect reports

