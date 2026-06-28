---
title: std::basic_streambuf::pubimbue
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/pubimbue
---


```cpp
dcl | num=1 |1=
std::locale pubimbue( const std::locale& loc );
dcl | num=2 |1=
protected:
virtual void imbue( const std::locale& loc );
```

Changes the associated locale.
1. Sets `loc` as the associated locale. Calls `imbue(loc)` of the most derived class
2. The base class version of this function has no effect. The derived classes may override this function in order to be informed about the changes of the locale. The derived class may cache the locale and member facets between calls to `imbue()`.

## Parameters


### Parameters


## Return value

1. Previous associated locale.
2. (none)

## Notes

From within the call of `imbue()`,  returns the previous locale.

## Example


## See also

