---
title: std::streamoff
type: Input/output
source: https://en.cppreference.com/w/cpp/io/streamoff
---


```cpp
dcl | 1=
typedef /*implementation-defined*/ streamoff;
```

The type `std::streamoff` is an implementation-defined <sup>(since C++11)</sup> signed integral type of sufficient size to represent the maximum possible file size supported by the operating system. <sup>(since C++11)</sup> Typically, this is an alias for `long long`.
It is used to represent offsets from stream positions (values of type `std::fpos`). A `std::streamoff` value constructed from `-1` is also used to represent error conditions by some of the I/O library functions.

## Relationship with std::fpos

* the difference between two `std::fpos` objects is a value of type `std::streamoff`
* a value of type `std::streamoff` may be added or subtracted from `std::fpos` yielding a different `std::fpos`.
* a value of type `std::fpos` is implicitly convertible to `std::streamoff` (the conversion result is the offset from the beginning of the file).
* a value of type `std::fpos` is constructible from a value of type `std::streamoff`

## See also

