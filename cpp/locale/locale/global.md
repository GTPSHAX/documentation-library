---
title: std::locale::global
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/locale/global
---

ddcl|
static locale global( const locale& loc );
Replaces the global C++ locale with `loc`, which means all future calls to the `std::locale` default constructor will now return a copy of `loc`. If `loc` has a name, also replaces the C locale as if by `1=std::setlocale(LC_ALL, loc.name().c_str());`. This function is the only way to modify the global C++ locale, which is otherwise equivalent to `std::locale::classic()` at program startup.

## Parameters


### Parameters

- `loc` - the new global C++ locale

## Return value

The previous value of the global C++ locale.

## Example


## Defect reports


## See also


| cpp/locale/locale/dsc locale | (see dedicated page) |
| cpp/locale/locale/dsc classic | (see dedicated page) |
| cpp/locale/dsc setlocale | (see dedicated page) |

