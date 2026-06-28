---
title: std::regex_traits::imbue
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_traits/imbue
---


```cpp
dcl|since=c++11|1=
locale_type imbue( locale_type loc );
```

Replaces the current locale with a copy of `loc`. If `loc` is different than the current locale, then all cached data is invalidated.
After the call `1=getloc() == loc`.

## Parameters


### Parameters

- `loc` - the locale to imbue

## Return value

The current locale of the traits object.
If `imbue()` has been never called for this object, then the global locale at the time of the call is returned. Otherwise, the locale passed to the last call to `imbue()` is returned.

## Example

