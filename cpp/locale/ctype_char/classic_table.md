---
title: std::ctype::classic_table
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/ctype_char/classic_table
---


```cpp
**Header:** `<`locale`>`
dcl rev multi|until1=c++11
|dcl1=
static const mask* classic_table() throw();
|dcl2=
static const mask* classic_table() noexcept;
```

Returns the classification table that matches the classification used by the minimal "C" locale.

## Parameters

(none)

## Return value

A pointer to the first element in the classification table (which is an array of size `std::ctype<char>::table_size`).

## Notes

Default-constructed `std::ctype<char>` facets use this table for classification.

## Example

