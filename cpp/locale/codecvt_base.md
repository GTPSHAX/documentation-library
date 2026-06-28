---
title: std::codecvt_base
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/codecvt_base
---


```cpp
dcl | 1=
class codecvt_base;
```

The class `std::codecvt_base` provides the conversion status constants which are inherited and used by the `std::codecvt` facets.

## Member types


| dsc | } | Unscoped enumeration type | |


## Notes

The value `std::codecvt_base::partial` is used to indicate that either the destination range is too short to receive the results of the conversion or the input is truncated in the middle of an otherwise valid multibyte character.

## See also

de:cpp/locale/codecvt base
es:cpp/locale/codecvt base
fr:cpp/locale/codecvt base
it:cpp/locale/codecvt base
ja:cpp/locale/codecvt base
pt:cpp/locale/codecvt base
ru:cpp/locale/codecvt base
zh:cpp/locale/codecvt base
