---
title: std::basic_filebuf::basic_filebuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/basic_filebuf
---


```cpp
dcl|num=1|
basic_filebuf();
dcl|num=2|since=c++11|1=
basic_filebuf( const std::basic_filebuf& rhs ) = delete;
dcl|num=3|since=c++11|
basic_filebuf( std::basic_filebuf&& rhs );
```

Constructs new `std::basic_filebuf` object.
1. Constructs a `std::basic_filebuf` object, initializing the base class by calling the default constructor of `std::basic_streambuf`. The created `basic_filebuf` is not associated with a file, and `is_open()` returns `false`.
2. The copy constructor is deleted; `std::basic_filebuf` is not *CopyConstructible*.
3. Move-constructs a `std::basic_filebuf` object by moving all contents from another `std::basic_filebuf` object `rhs`, including the buffers, the associated file, the locale, the openmode, the is_open variable, and all other state. After move, `rhs` is not associated with a file and `1=rhs.is_open() == false`. The member pointers of the base class `std::basic_streambuf` of `rhs` and of the base class of `*this` are guaranteed to point to different buffers (unless null).

## Parameters


### Parameters

- `rhs` - another `basic_filebuf`

## Notes

Typically called by the constructor of `std::basic_fstream`.

## Example


## See also


| cpp/io/basic_filebuf/dsc operator{{= | (see dedicated page) |
| cpp/io/basic_filebuf/dsc ~basic_filebuf | (see dedicated page) |

