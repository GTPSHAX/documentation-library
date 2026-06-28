---
title: std::basic_ios::init
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/init
---

ddcl |
protected:
void init( std::basic_streambuf<CharT,Traits>* sb );
Sets the associated stream buffer to `sb` and initializes the internal state.
The postconditions are as follows:


| - |
| Element |
| Value |
| - |
| lc | rdbuf() | c | sb |
| - |
| lc | tie() | null pointer |
| - |
| lc | rdstate() | c | goodbit if c | sb is not a null pointer, otherwise c | badbit |
| - |
| lc | exceptions() | c | goodbit |
| - |
| ltf | cpp/io/ios_base/flags | c | skipws | dec |
| - |
| ltf | cpp/io/ios_base/width | c | 0 |
| - |
| ltf | cpp/io/ios_base/precision | c | 6 |
| - |
| lc | fill() | c | widen(' ') |
| - |
| ltf | cpp/io/ios_base/getloc | a copy of the value returned by c | std::locale() |

This member function is protected: it is called by the constructors of the derived stream classes `std::basic_istream` and `std::basic_ostream` once the associated stream buffer is known. Until this function is called, every member function (including the destructor) of the default-constructed `std::basic_ios` invokes undefined behavior. Note that `basic_ios` is a virtual base class, and therefore its constructor is not called by the constructors of those directly derived classes, which is why two-stage initialization is necessary.

## Parameters


### Parameters


## See also

