---
title: std::locale::facet
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/locale/facet
---


```cpp
**Header:** `<`locale`>`
dcl|1=
class locale::facet;
```

`std::locale::facet` is the base class for facets. It provides a common base class so that locales could store pointers to the facets they implement in a single indexed container, and it abstracts support for facet reference counting.
Whenever a facet is added to a locale, the locale increments the reference count in the facet (through an implementation-specific mechanism). Whenever a locale is destructed or modified, it decrements the reference count in each facet it no longer implements. Whenever a facet's reference count becomes zero, the locale performs `delete static_cast<std::locale::facet*>(f);` where `f` is the pointer to the facet.

## Facet class

A class is a ''facet'' if
* it is publicly derived from another facet, or
* it is a class derived from `std::locale::facet` and contains a publicly accessible declaration as follows:

## Member functions


## Example


## See also


| cpp/locale/locale/dsc id | (see dedicated page) |

