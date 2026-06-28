---
title: std::regex_traits::getloc
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_traits/getloc
---


```cpp
dcl|since=c++11|1=
locale_type getloc() const;
```

Returns the current locale of the traits object.
If `imbue()` has been never called for this object, then the global locale at the time of the call is returned. Otherwise, the locale passed to the last call to `imbue()` is returned.

## Parameters

(none)

## Return value

The current locale of the traits object.

## Example

