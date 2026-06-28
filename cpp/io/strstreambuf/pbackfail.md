---
title: std::strstreambuf::pbackfail
type: Input/output
source: https://en.cppreference.com/w/cpp/io/strstreambuf/pbackfail
---

ddcl|deprecated=c++98|removed=c++26|1=
protected:
virtual int_type pbackfail( int_type c = EOF );
This protected virtual function is called by the public functions  and  (which, in turn, are called by  and ).
1. The caller is requesting that the get area is backed up by one character (`pbackfail()` is called with no arguments or with `EOF` as the argument)
:@a@ First, checks if there is a putback position, and if there really isn't, fails (`strstreambuf` has no external character source to re-read).
:@b@ If the caller was wrong and the putback position is in fact available, simply decrements , e.g. by calling `gbump(-1)`.
2. The caller attempts to putback a different character from the one retrieved earlier (`pbackfail()` is called with the character that needs to be put back), in which case
:@a@ First, checks if there is a putback position, and if there isn't, fails.
:@b@ Then checks what character is in the putback position. If the character held there is already equal to `(char)c`, then simply decrements .
:@c@ Otherwise, if the buffer is unmodifiable (this strstreambuf was constructed with a string literal or some other `const` array), fails.
:@d@ Otherwise, decrements  and writes `c` to the location pointed to `gptr()` after adjustment.

## Parameters


### Parameters

- `c` - the character to put back, or `Traits::eof()` to indicate that backing up of the get area is requested

## Return value

`c` on success except if `c` was `EOF`, in which case unspecified value other than `EOF` is returned.
`EOF` on failure.

## Example


## See also


| cpp/io/basic_streambuf/dsc pbackfail | (see dedicated page) |
| cpp/io/basic_streambuf/dsc sungetc | (see dedicated page) |
| cpp/io/basic_streambuf/dsc sputbackc | (see dedicated page) |
| cpp/io/basic_istream/dsc unget | (see dedicated page) |
| cpp/io/basic_istream/dsc putback | (see dedicated page) |

