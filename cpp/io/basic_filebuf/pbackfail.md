---
title: std::basic_filebuf::pbackfail
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/pbackfail
---

ddcl |1=
protected:
virtual int_type pbackfail( int_type c = Traits::eof() )
This protected virtual function is called by the public functions  and  (which, in turn, are called by  and ).
1. The caller is requesting that the get area is backed up by one character (`pbackfail()` is called with no arguments), in which case, this function re-reads the file starting one byte earlier and decrements , e.g. by calling `gbump(-1)`.
2. The caller attempts to putback a different character from the one retrieved earlier (`pbackfail()` is called with the character that needs to be put back), in which case
:@a@ First, checks if there is a putback position, and if there isn't, backs up the get area by re-reading the file starting one byte earlier.
:@a@ Then checks what character is in the putback position. If the character held there is already equal to `c`, as determined by `Traits::eq(to_char_type(c), gptr()[-1])`, then simply decrements .
:@b@ Otherwise, if the buffer is allowed to modify its own get area, decrements  and writes `c` to the location pointed to gptr() after adjustment.
This function never modifies the file, only the get area of the in-memory buffer.
If the file is not open (`1=is_open()==false`, this function returns `Traits::eof()` immediately.

## Parameters


### Parameters


## Return value

`c` on success except if `c` was `Traits::eof()`, in which case `Traits::not_eof(c)` is returned.
`Traits::eof()` on failure.

## Example


## See also

de:cpp/io/basic filebuf/pbackfail
es:cpp/io/basic filebuf/pbackfail
fr:cpp/io/basic filebuf/pbackfail
it:cpp/io/basic filebuf/pbackfail
ja:cpp/io/basic filebuf/pbackfail
pt:cpp/io/basic filebuf/pbackfail
ru:cpp/io/basic filebuf/pbackfail
zh:cpp/io/basic filebuf/pbackfail
