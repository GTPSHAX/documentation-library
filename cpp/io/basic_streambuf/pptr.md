---
title: std::basic_streambuf::pptr
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/pptr
---


```cpp
dcl | num=1 |
protected:
char_type* pbase() const;
dcl | num=2 |
protected:
char_type* pptr() const;
dcl | num=3 |
protected:
char_type* epptr() const;
```

Returns pointers defining the put area.
1) Returns the pointer to the beginning ("base") of the put area.
2) Returns the pointer to the current character (''put pointer'') in the put area.
3) Returns the pointer one past the end of the put area.

## Parameters

(none)

## Return value

1) The pointer to the beginning of the put area.
2) The pointer to the current character (''put pointer'') in the put area.
3) The pointer one past the end of the put area.

## Example


## See also

de:cpp/io/basic streambuf/pptr
es:cpp/io/basic streambuf/pptr
fr:cpp/io/basic streambuf/pptr
it:cpp/io/basic streambuf/pptr
ja:cpp/io/basic streambuf/pptr
pt:cpp/io/basic streambuf/pptr
ru:cpp/io/basic streambuf/pptr
zh:cpp/io/basic streambuf/pptr
