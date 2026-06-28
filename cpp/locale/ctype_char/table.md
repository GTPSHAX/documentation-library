---
title: std::ctype::table
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/ctype_char/table
---


```cpp
dcl rev multi | until1=c++11
| dcl1=
const mask* table() const throw();
| dcl2=
const mask* table() const noexcept;
```

Returns the classification table that was provided in the constructor of this instance of `std::ctype<char>`, or returns a copy of `classic_table()` if none was provided.

## Parameters

(none)

## Return value

A pointer to the first element in the classification table (which an array of size `std::ctype<char>::table_size`).

## Example

