---
title: std::localeconv
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/localeconv
---


```cpp
**Header:** `<`clocale`>`
dcl |
std::lconv* localeconv();
```

The `localeconv` function obtains a pointer to a static object of type `std::lconv`, which represents numeric and monetary formatting rules of the current C locale.

## Parameters

(none)

## Return value

Pointer to the current `std::lconv` object.

## Notes

Modifying the object references through the returned pointer is undefined behavior.
`std::localeconv` modifies a static object, calling it from different threads without synchronization is undefined behavior.

## Example


## See also

de:cpp/locale/localeconv
es:cpp/locale/localeconv
fr:cpp/locale/localeconv
it:cpp/locale/localeconv
ja:cpp/locale/localeconv
pt:cpp/locale/localeconv
ru:cpp/locale/localeconv
zh:cpp/locale/localeconv
