---
title: Input/output library
type: Input/output
source: https://en.cppreference.com/w/cpp/io
---


# Input/output library

C++ includes the following input/output libraries: an OOP-style stream-based I/O library<sup>(since C++23)</sup> , print-based family of functions, and the standard set of C-style I/O functions.

## Stream-based I/O

The stream-based input/output library is organized around abstract input/output devices. These abstract devices allow the same code to handle input/output to files, memory streams, or custom adaptor devices that perform arbitrary operations (e.g. compression) on the fly.
Most of the classes are templated, so they can be adapted to any basic character type. Separate typedefs are provided for the most common basic character types (`char` and `wchar_t`). The classes are organized into the following hierarchy:


#### Abstraction

| ios | |
| cpp/io/dsc ios_base | (see dedicated page) |
| cpp/io/dsc basic_ios | (see dedicated page) |
| streambuf | |
| cpp/io/dsc basic_streambuf | (see dedicated page) |
| ostream | |
| cpp/io/dsc basic_ostream | (see dedicated page) |
| istream | |
| cpp/io/dsc basic_istream | (see dedicated page) |
| cpp/io/dsc basic_iostream | (see dedicated page) |

#### File I/O implementation

| fstream | |
| cpp/io/dsc basic_filebuf | (see dedicated page) |
| cpp/io/dsc basic_ifstream | (see dedicated page) |
| cpp/io/dsc basic_ofstream | (see dedicated page) |
| cpp/io/dsc basic_fstream | (see dedicated page) |

#### String I/O implementation

| sstream | |
| cpp/io/dsc basic_stringbuf | (see dedicated page) |
| cpp/io/dsc basic_istringstream | (see dedicated page) |
| cpp/io/dsc basic_ostringstream | (see dedicated page) |
| cpp/io/dsc basic_stringstream | (see dedicated page) |

#### Array I/O implementations

| spanstream | |
| cpp/io/dsc basic_spanbuf | (see dedicated page) |
| cpp/io/dsc basic_ispanstream | (see dedicated page) |
| cpp/io/dsc basic_ospanstream | (see dedicated page) |
| cpp/io/dsc basic_spanstream | (see dedicated page) |
| strstream | |
| cpp/io/dsc strstreambuf | (see dedicated page) |
| cpp/io/dsc istrstream | (see dedicated page) |
| cpp/io/dsc ostrstream | (see dedicated page) |
| cpp/io/dsc strstream | (see dedicated page) |

#### Synchronized output {{mark since c++20

| syncstream | |
| cpp/io/dsc basic_syncbuf | (see dedicated page) |
| cpp/io/dsc basic_osyncstream | (see dedicated page) |


### Typedefs

The following typedefs for common character types are provided in namespace `std`:


| Item | Description |
|------|-------------|
| **Type** | Definition |
| ios | |
| streambuf | |
| istream | |
| ostream | |
| fstream | |
| sstream | |
| spanstream | |
| syncstream | |


### Predefined standard stream objects


| iostream | |
| cpp/io/dsc cin | (see dedicated page) |
| cpp/io/dsc cout | (see dedicated page) |
| cpp/io/dsc cerr | (see dedicated page) |
| cpp/io/dsc clog | (see dedicated page) |


### 

The stream-based I/O library uses  (e.g. `std::boolalpha`, `std::hex`, etc.) to control how streams behave.

### Types

The following auxiliary types are defined:


| ios | |
| cpp/io/dsc streamoff | (see dedicated page) |
| cpp/io/dsc streamsize | (see dedicated page) |
| cpp/io/dsc fpos | (see dedicated page) |

The following typedef names for `std::fpos<std::mbstate_t>` are provided:


| Item | Description |
|------|-------------|
| iosfwd | |
| **Type** | Definition |


### Error category interface <sup>(C++11)</sup>


| ios | |
| cpp/io/dsc io_errc | (see dedicated page) |
| cpp/io/dsc iostream_category | (see dedicated page) |


## Print functions <sup>(C++23)</sup>

The Unicode-aware print-family functions that perform formatted I/O on text that is already formatted. They bring all the performance benefits of `std::format`, are locale-independent by default, reduce global state, avoid allocating a temporary `std::string` object and calling `operator<<`, and in general make formatting more efficient compared to iostreams and stdio.
The following print-like functions are provided:


| print | |
| cpp/io/dsc print | (see dedicated page) |
| cpp/io/dsc println | (see dedicated page) |
| cpp/io/dsc vprint_unicode | (see dedicated page) |
| cpp/io/dsc vprint_nonunicode | (see dedicated page) |
| ostream | |
| cpp/io/basic_ostream/dsc print | (see dedicated page) |
| cpp/io/basic_ostream/dsc println | (see dedicated page) |


## 

C++ also includes the , such as `std::fopen`, `std::getc`, etc.

## See also

