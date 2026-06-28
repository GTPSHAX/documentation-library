---
title: std::basic_filebuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf
---

ddcl|header=fstream|1=
template<
class CharT,
class Traits = std::char_traits<CharT>
> class basic_filebuf : public std::basic_streambuf<CharT, Traits>
`std::basic_filebuf` is a `std::basic_streambuf` whose associated character sequence is a file. Both the input sequence and the output sequence are associated with the same file, and a joint file position is maintained for both operations. The restrictions on reading and writing a sequence with `std::basic_filebuf` are the same as `std::FILE`s.
The functions `underflow()` and `overflow()` / `sync()` perform the actual I/O between the file and the get and put areas of the buffer. When `CharT` is not `char`, most implementations store multibyte characters in the file and a `std::codecvt` facet is used to perform wide/multibyte character conversion.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| cpp/io/dsc char_type | (see dedicated page) |
| cpp/io/dsc traits_type | (see dedicated page) |
| cpp/io/dsc int_type | (see dedicated page) |
| cpp/io/dsc off_type | (see dedicated page) |
| cpp/io/dsc native_handle_type | (see dedicated page) |


## Member functions


| cpp/io/basic_filebuf/dsc basic_filebuf | (see dedicated page) |
| cpp/io/basic_filebuf/dsc operator{{= | (see dedicated page) |
| cpp/io/basic_filebuf/dsc swap | (see dedicated page) |
| cpp/io/basic_filebuf/dsc native_handle | (see dedicated page) |
| cpp/io/basic_filebuf/dsc ~basic_filebuf | (see dedicated page) |
| cpp/io/basic_filebuf/dsc is_open | (see dedicated page) |
| cpp/io/basic_filebuf/dsc open | (see dedicated page) |
| cpp/io/basic_filebuf/dsc close | (see dedicated page) |
| cpp/io/basic_filebuf/dsc showmanyc | (see dedicated page) |
| cpp/io/basic_filebuf/dsc underflow | (see dedicated page) |
| cpp/io/basic_filebuf/dsc uflow | (see dedicated page) |
| cpp/io/basic_filebuf/dsc pbackfail | (see dedicated page) |
| cpp/io/basic_filebuf/dsc overflow | (see dedicated page) |
| cpp/io/basic_filebuf/dsc setbuf | (see dedicated page) |
| cpp/io/basic_filebuf/dsc seekoff | (see dedicated page) |
| cpp/io/basic_filebuf/dsc seekpos | (see dedicated page) |
| cpp/io/basic_filebuf/dsc sync | (see dedicated page) |
| cpp/io/basic_filebuf/dsc imbue | (see dedicated page) |


## Non-member functions


| cpp/io/basic_filebuf/dsc swap2 | (see dedicated page) |


## Notes


## See also


| cpp/io/c/dsc FILE | (see dedicated page) |

