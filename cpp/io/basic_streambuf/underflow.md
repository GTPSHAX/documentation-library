---
title: std::basic_streambuf::underflow
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/underflow
---

ddcl | 1=
protected:
virtual int_type underflow();
Ensures that at least one character is available in the input area by updating the pointers to the input area (if needed) and reading more data in from the input sequence (if applicable). Returns the value of that character (converted to `int_type` with `Traits::to_int_type(c)`) on success or `Traits::eof()` on failure.
The function may update `gptr`, `egptr` and `eback` pointers to define the location of newly loaded data (if any). On failure, the function ensures that either `gptr()  or `gptr() .
The base class version of the function does nothing. The derived classes may override this function to allow updates to the get area in the case of exhaustion.

## Parameters

(none)

## Return value

The value of the character pointed to by the ''get pointer'' after the call on success, or `Traits::eof()` otherwise.
The base class version of the function returns `traits::eof()`.

## Note

The public functions of `std::streambuf` call this function only if `1=gptr() == nullptr` or `1=gptr() >= egptr()`.

## Example


## See also

de:cpp/io/basic streambuf/underflow
es:cpp/io/basic streambuf/underflow
fr:cpp/io/basic streambuf/underflow
it:cpp/io/basic streambuf/underflow
ja:cpp/io/basic streambuf/underflow
pt:cpp/io/basic streambuf/underflow
ru:cpp/io/basic streambuf/underflow
zh:cpp/io/basic streambuf/underflow
