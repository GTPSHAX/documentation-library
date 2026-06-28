---
title: std::locale::operators (operator!=)
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/locale/operator_cmp
---


```cpp
dcl|num=1|1=
bool operator==( const locale& other ) const;
dcl|num=2|until=c++20|1=
bool operator!=( const locale& other ) const;
```

Tests two locales for equality. Named locales are considered equal if their names are equal. Unnamed locales are considered equal if they are copies of each other.
rrev|since=c++20|

## Parameters


### Parameters

- `other` - a `std::locale` object to compare

## Return value

1. `true` if `other` is a copy of `*this` or has an identical name, `false` otherwise.
2. `false` if `other` is a copy of `*this` or has an identical name, `true` otherwise.

## Example


## See also


| cpp/locale/locale/dsc locale | (see dedicated page) |
| cpp/locale/locale/dsc name | (see dedicated page) |

