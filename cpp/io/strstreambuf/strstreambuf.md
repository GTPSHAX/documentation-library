---
title: std::strstreambuf::strstreambuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/strstreambuf/strstreambuf
---


```cpp
dcl rev multi|num=1|notes1=<sup>(deprecated C++98)</sup><br><sup>(until C++11)</sup>|dcl1=
explicit strstreambuf( std::streamsize alsize = 0 );
|notes2=|dcl2=
strstreambuf() : strstreambuf(0) {}
explicit strstreambuf( std::streamsize alsize );
dcl|num=2|deprecated=c++98|removed=c++26|1=
strstreambuf( void* (*palloc)(std::size_t), void (*pfree)(void*) );
dcl|num=3|deprecated=c++98|removed=c++26|1=
strstreambuf( char* gnext, std::streamsize n, char* pbeg = 0 );
dcl|num=4|deprecated=c++98|removed=c++26|1=
strstreambuf( signed char* gnext, std::streamsize n, signed char* pbeg = 0 );
dcl|num=5|deprecated=c++98|removed=c++26|1=
strstreambuf( unsigned char* gnext, std::streamsize n, unsigned char* pbeg = 0 );
dcl|num=6|deprecated=c++98|removed=c++26|1=
strstreambuf( const char* gnext, std::streamsize n );
dcl|num=7|deprecated=c++98|removed=c++26|1=
strstreambuf( const signed char* gnext, std::streamsize n );
dcl|num=8|deprecated=c++98|removed=c++26|1=
strstreambuf( const unsigned char* gnext, std::streamsize n );
```

1. Constructs a `std::strstreambuf` object: initializes the base class by calling the default constructor of `std::streambuf`, initializes the buffer state to "dynamic" (the buffer will be allocated as needed), initializes allocated size to the provided `alsize`, initializes the allocation and the deallocation functions to null (will use `new[]` and `delete[]`).
2. Constructs a `std::strstreambuf` object: initializes the base class by calling the default constructor of `std::streambuf`, initializes the buffer state to "dynamic" (the buffer will be allocated as needed), initializes allocated size to unspecified value, initializes the allocation function to `palloc` and the deallocation function to `pfree`.
@3-5@ Constructs a `std::strstreambuf` object in following steps:
:@a@ Initializes the base class by calling the default constructor of `std::streambuf`.
:@b@ Initializes the buffer state to "constant" (the buffer is a user-provided fixed-size buffer).
:@c@ Determines the number of elements in the user-provided array as follows: if `n` is greater than zero, `n` is used. If `n` is zero, `std::strlen(gnext)` is executed to determine the buffer size. If `n` is negative, `INT_MAX` is used.
:@d@ Configures the `std::basic_streambuf` pointers as follows: If `pbeg` is a null pointer, calls `setg(gnext, gnext, gnext + N)`. If `pbeg` is not a null pointer, executes `setg(gnext, gnext, pbeg)` and `setp(pbeg, pbeg + N)`, where N is the number of elements in the array as determined earlier.
@6-8@ Same as `strstreambuf((char*)gnext, n)`, except the "constant" bit is set in the buffer state bitmask (output to this buffer is not allowed).

## Parameters


### Parameters

- `alsize` - the initial size of the dynamically allocated buffer
- `palloc` - pointer to user-provided allocation function
- `pfree` - pointer to user-provided deallocation function
- `gnext` - pointer to the start of the get area in the user-provided array
- `pbeg` - pointer to the start of the put area in the user-provided array
- `n` - the number of bytes in the get area (if pbeg is null) or in the put area (if pbeg is not null) of the user-provided array

## Notes

These constructors are typically called by the constructors of `std::strstream`.

## Defect reports


## Example


### Example

```cpp
#include <iostream>
#include <strstream>

int main()
{
    std::strstreambuf dyn; // dynamic
    std::strstream dyn_s; // equivalent stream
    dyn_s << 1.23 << std::ends;
    std::cout << dyn_s.str() << '\n';
    dyn_s.freeze(false);

    char buf[10];
    std::strstreambuf user(buf, 10, buf); // user-provided output buffer
    std::ostrstream user_s(buf, 10); // equivalent stream
    user_s << 1.23 << std::ends;
    std::cout << buf << '\n';

    std::strstreambuf lit("1 2 3", 5); // constant
    std::istrstream lit_s("1 2 3"); // equivalent stream
    int i, j, k;
    lit_s >> i >> j >> k;
    std::cout << i << ' ' << j << ' ' << k << '\n';
}
```


**Output:**
```
1.23
1.23
1 2 3
```


## See also


| cpp/io/strstream/dsc constructor|strstream | (see dedicated page) |

