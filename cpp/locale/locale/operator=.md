---
title: std::locale::operator=
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/locale/operator=
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
const locale& operator=( const locale& other ) throw();
|dcl2=
const locale& operator=( const locale& other ) noexcept;
```

Creates a copy of `other`, replacing the contents of `*this`. The reference counts of all facets held by `other` are incremented. The reference counts of all facets previously held by `*this` are decremented, and those facets whose reference count becomes zero are deleted.

## Return value

Returns `*this`, which is now a copy of `other`.

## Example


## See also


| cpp/locale/locale/dsc locale | (see dedicated page) |

