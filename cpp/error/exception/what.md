---
title: std::exception::what
type: Utilities
source: https://en.cppreference.com/w/cpp/error/exception/what
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
virtual const char* what() const throw();
|notes2=<sup>(constexpr C++26)</sup>
|dcl2=
virtual const char* what() const noexcept;
```

Returns the explanatory string.

## Parameters

(none)

## Return value

Pointer to a null-terminated string with explanatory information. The pointer is guaranteed to be valid at least until the exception object from which it is obtained is destroyed, or until a non-const member function on the exception object is called.
rrev|since=c++26|
The returned string is encoded with the ordinary literal encoding during constant evaluation.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-108 | C++98 | it was unspecified when the returned pointer becomes invalid | specified |

