---
title: std::basic_streambuf::pbackfail
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/pbackfail
---


```cpp
dcl|1=
protected:
virtual int_type pbackfail( int_type c = Traits::eof() );
```

This function can only be called if any of the following condition is satisfied:
* `gptr()` is null,
* `1=gptr() == eback()`, or
* `traits::eq(traits::to_char_type(c), gptr()[-1])` returns `false`.
This function is called by the public functions `sungetc()` and `sputbackc()` (which, in turn, are called by  and ) when either:
1. There is no putback position in the get area (`pbackfail()` is called with no arguments). In this situation, the purpose of `pbackfail()` is to back up the get area by one character, if the associated character sequence allows this (e.g. a file-backed streambuf may reload the buffer from a file, starting one character earlier).
2. The caller attempts to putback a different character from the one retrieved earlier (`pbackfail()` is called with the character that needs to be put back). In this situation, the purpose of `pbackfail()` is to place the character `c` into the get area at the position just before , and, if possible, to modify the associated character sequence to reflect this change. This may involve backing up the get area as in the first variant.
The default base class version of this function does nothing and returns `Traits::eof()` in all situations. This function is overridden by the derived classes: , , , and is expected to be overridden by user-defined and third-party library stream classes.

## Parameters


### Parameters

- `ch` - character to put back or `Traits::eof()` if only back out is requested

## Return value

`Traits::eof()` in case of failure, some other value to indicate success. The base class version always fails.

## Example


## Defect reports


## See also


| cpp/io/basic_filebuf/dsc pbackfail | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc pbackfail | (see dedicated page) |
| cpp/io/strstreambuf/dsc pbackfail | (see dedicated page) |
| cpp/io/basic_streambuf/dsc sungetc | (see dedicated page) |
| cpp/io/basic_streambuf/dsc sputbackc | (see dedicated page) |

