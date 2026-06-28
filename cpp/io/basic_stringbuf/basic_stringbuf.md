---
title: std::basic_stringbuf::basic_stringbuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_stringbuf/basic_stringbuf
---


```cpp
dcl rev multi|num=1|until1=c++11|dcl1=
explicit basic_stringbuf( std::ios_base::openmode which =
std::ios_base::in | std::ios_base::out );
|dcl2=
explicit basic_stringbuf( std::ios_base::openmode which );
dcl|num=2|since=c++11|1=
basic_stringbuf()
: basic_stringbuf( std::ios_base::in | std::ios_base::out ) {}
dcl|num=3|1=
explicit
basic_stringbuf( const std::basic_string<CharT, Traits, Allocator>& s,
std::ios_base::openmode which =
std::ios_base::in | std::ios_base::out );
dcl|num=4|since=c++20|1=
explicit basic_stringbuf( std::basic_string<CharT, Traits, Allocator>&& s,
std::ios_base::openmode which =
std::ios_base::in | std::ios_base::out );
dcl|num=5|since=c++20|1=
basic_stringbuf( std::ios_base::openmode which, const Allocator& a );
dcl|num=6|since=c++20|1=
explicit basic_stringbuf( const Allocator& a )
: basic_stringbuf( std::ios_base::in | std::ios_base::out, a ) {}
dcl|num=7|since=c++20|1=
template< class SAlloc >
explicit basic_stringbuf( const std::basic_string<CharT, Traits, SAlloc>& s,
std::ios_base::openmode which =
std::ios_base::in | std::ios_base::out );
dcl|num=8|since=c++20|1=
template< class SAlloc >
basic_stringbuf( const std::basic_string<CharT, Traits, SAlloc>& s,
std::ios_base::openmode which, const Allocator& a );
dcl|num=9|since=c++20|1=
template< class SAlloc >
basic_stringbuf( const std::basic_string<CharT, Traits, SAlloc>& s,
const Allocator& a )
: basic_stringbuf( s, std::ios_base::in | std::ios_base::out, a ) {}
dcl|num=10|since=c++26|1=
template< class StringViewLike >
explicit basic_stringbuf( const StringViewLike& t,
std::ios_base::openmode which =
std::ios_base::in | std::ios_base::out );
dcl|num=11|since=c++26|1=
template< class StringViewLike >
basic_stringbuf( const StringViewLike& t,
std::ios_base::openmode which, const Allocator& a );
dcl|num=12|since=c++26|1=
template< class StringViewLike >
basic_stringbuf( const StringViewLike& t, const Allocator& a );
dcl|num=13|since=c++11|1=
basic_stringbuf( basic_stringbuf&& rhs );
dcl|num=14|since=c++20|1=
basic_stringbuf( basic_stringbuf&& rhs, const Allocator& a );
dcl|num=15|since=c++11|1=
basic_stringbuf( const basic_stringbuf& rhs ) = delete;
```

The `std::basic_streambuf` base and the `exposition-only data members`  and  are initialized as follows.
After initializing these subobjects, overloads  initialize the input and output sequences as if by calling .


| - |
| Overload |
| lc | std::basic_streambuf base |
| tti | buf |
| tti | mode |
| - |
| v | 1 |
| rowspan=12 | default-initialized |
| rowspan=2 | implementation-defined<br>(see below) |
| c | which |
| - |
| v | 2 |
| style="text-align: left;" | c multi | std::ios_base::in | | std::ios_base::out |
| - |
| v | 3 |
| c | s |
| rowspan=3 | c | which |
| - |
| v | 4 |
| c | std::move(s) |
| - |
| v | 5 |
| rowspan=2 | c | a |
| - |
| v | 6 |
| style="text-align: left;" | c multi | std::ios_base::in | | std::ios_base::out |
| - |
| v | 7 |
| c | s |
| rowspan=2 | c | which |
| - |
| v | 8 |
| rowspan=2 | c | {s, a} |
| - |
| v | 9 |
| style="text-align: left;" | c multi | std::ios_base::in | | std::ios_base::out |
| - |
| v | 10 |
| c | {sv, Allocator()} |
| rowspan=2 | c | which |
| - |
| v | 11 |
| rowspan=2 | c | {sv, a} |
| - |
| v | 12 |
| style="text-align: left;" | c multi | std::ios_base::in | | std::ios_base::out |
| - |
| v | 13 |
| rowspan=2 | c | rhs<br>(copy constructed) |
| c | std::move(rhs).str() |
| rowspan=2 | c | rhs.mode |
| - |
| v | 14 |
| c | {std::move(rhs).str(), a} |

@1,2@ Overload <sup>(until C++11)</sup> <sup>(since C++11)</sup>  is the default constructor. It is implementation-defined whether the sequence pointers (`eback()`, `gptr()`, `egptr()`, `pbase()`, `pptr()`, `epptr()`) are initialized to null pointers.
@5,6@ When the construction is complete, `str.empty()` is `true`.
7. .
@10-12@
@13,14@ Overload  is the move constructor. It is implementation-defined whether the six sequence pointers in `*this` obtain the values which `rhs` had.
@@ When the construction is complete, `rhs` is empty but usable, and
* Let `rhs_p` refer to the state of `rhs` just prior to this construction, the following expressions will evaluate to `true`:
:* `1=str() == rhs_p.str()`
:* `1=getloc() == rhs_p.getloc()`
:* `1=gptr() - eback() == rhs_p.gptr() - rhs_p.eback()`
:* `1=egptr() - eback() == rhs_p.egptr() - rhs_p.eback()`
:* `1=pptr() - pbase() == rhs_p.pptr() - rhs_p.pbase()`
:* `1=epptr() - pbase() == rhs_p.epptr() - rhs_p.pbase()`
* Let `rhs_a` refer to the state of `rhs` just after this construction, the following expressions will evaluate to `true`:
:* `1=!eback()
:* `1=!gptr()
:* `1=!egptr()
:* `1=!pbase()
:* `1=!pptr()
:* `1=!epptr()
15. The copy constructor is deleted; `std::basic_stringbuf` is not *CopyConstructible*.

## Parameters


### Parameters

- `s` - a `std::basic_string` used to initialize the buffer
- `t` - an object (convertible to `std::basic_string_view`) used to initialize the buffer
- `a` - another allocator used to construct the internal `std::basic_string`
- `rhs` - another `basic_stringbuf`
- `which` - specifies stream open mode. It is bitmask type, the following constants are defined: 

## Notes

Typically called by the constructor of `std::basic_stringstream`.
The level of support for the open modes other than `std::ios_base::in` and `std::ios_base::out` varies among implementations. C++11 explicitly specifies the support for `std::ios_base::ate` in `str()` and in this constructor, but `std::ios_base::app`, `std::ios_base::trunc`, and `std::ios_base::binary` have different effects on different implementations.

## Example


### Example

```cpp
#include <iostream>
#include <sstream>

int main()
{
    // default constructor (mode = in {{!
```

std::stringbuf buf1;
buf1.sputc('1');
std::cout << &buf1 << '\n';
// string constructor in at-end mode (C++11)
std::stringbuf buf2("test", std::ios_base::in
| std::ios_base::out
| std::ios_base::ate);
buf2.sputc('1');
std::cout << &buf2 << '\n';
// append mode test (results differ among compilers)
std::stringbuf buf3("test", std::ios_base::in
| std::ios_base::out
| std::ios_base::app);
buf3.sputc('1');
buf3.pubseekpos(1);
buf3.sputc('2');
std::cout << &buf3 << '\n';
}
|output=
1
test1
est12 (Sun Studio) 2st1 (GCC)

## Defect reports


## See also


| cpp/io/basic_stringstream/dsc constructor|basic_stringstream | (see dedicated page) |

