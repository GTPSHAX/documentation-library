---
title: std::basic_streambuf::eback
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/gptr
---


```cpp
dcl|num=1|
char_type* eback() const;
dcl|num=2|
char_type* gptr() const;
dcl|num=3|
char_type* egptr() const;
```

Returns pointers defining the get area.
1) Returns the pointer to the beginning of the get area.
2) Returns the pointer to the current character (''get pointer'') in the get area.
3) Returns the pointer one past the end of the get area.

## Parameters

(none)

## Return value

1) The pointer to the beginning of the get area.
2) The pointer to the current character (''get pointer'') in the get area.
3) The pointer one past the end of the get area.

## Notes

While the names "gptr" and "egptr" refer to the get area, the name "eback" refers to the end of the putback area: stepping backwards from `gptr`, characters can be put back until `eback`.

## Example


## See also


| cpp/io/basic_streambuf/dsc pptr | (see dedicated page) |

