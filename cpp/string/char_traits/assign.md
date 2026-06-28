---
title: std::char_traits::assign
type: Strings
source: https://en.cppreference.com/w/cpp/string/char_traits/assign
---


```cpp
<br><sup>(constexpr C++17)</sup>|
static void assign( char_type& c1, const char_type& c2 );
|
static char_type* assign( char_type* ptr, std::size_t count, char_type c2 );
```

1. Assigns `c2` to `c1`, behaves identically to `1=c1 = c2`.
2. Assigns `c2` to each character in `count` characters in the character sequence pointed to by `ptr`.
See *CharTraits* for the general requirements on character traits for `X::assign`.

## Parameters


### Parameters

- `c1` - character to assign to
- `c2` - character value to assign
- `ptr` - pointer to a character sequence to assign to
- `count` - the length of the character sequence

## Return value

1. (none)
2. `ptr`

## Complexity

1. Constant.
2. Linear in `count`.
