---
title: std::basic_streambuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf
---

ddcl|header=streambuf|1=
template<
class CharT,
class Traits = std::char_traits<CharT>
> class basic_streambuf;
The class `basic_streambuf` controls input and output to a character sequence. It includes and provides access to
# The ''controlled character sequence'', also called the ''buffer'', which may contain ''input sequence'' (also called ''get area'') for buffering the input operations and/or ''output sequence'' (also called ''put area'') for buffering the output operations.
# The ''associated character sequence'', also called ''source'' (for input) or ''sink'' (for output). This may be an entity that is accessed through OS API (file, TCP socket, serial port, other character device), or it may be an object (`std::vector`, , ), that can be interpreted as a character source or sink.
The I/O stream objects `std::basic_istream` and `std::basic_ostream`, as well as all objects derived from them (`std::ofstream`, `std::stringstream`, etc), are implemented entirely in terms of `std::basic_streambuf`.
The controlled character sequence is an array of `CharT` which, at all times, represents a subsequence, or a "window" into the associated character sequence. Its state is described by three pointers:
# The ''beginning pointer'', always points at the lowest element of the buffer.
# The ''next pointer'', points at the element that is the next candidate for reading or writing.
# The ''end pointer'', points one past the end of the buffer.
A `basic_streambuf` object may support input (in which case the buffer described by the beginning, next, and end pointers is called ''get area''), output (''put area''), or input and output simultaneously. In latter case, six pointers are tracked, which may all point to elements of the same character array or two individual arrays.
If the next pointer is less than the end pointer in the put area, a ''write position'' is available. The next pointer can be dereferenced and assigned to.
If the next pointer is less than the end pointer in the get area, a ''read position'' is available. The next pointer can be dereferenced and read from.
If the next pointer is greater than the beginning pointer in a get area, a ''putback position'' is available, and the next pointer may be decremented, dereferenced, and assigned to, in order to put a character back into the get area.
The character representation and encoding in the controlled sequence may be different from the character representations in the associated sequence, in which case a `std::codecvt` locale facet is typically used to perform the conversion. Common examples are UTF-8 (or other multibyte) files accessed through `std::wfstream` objects: the controlled sequence consists of `wchar_t` characters, but the associated sequence consists of bytes.
Typical implementation of the `std::basic_streambuf` base class holds only the six `CharT*` pointers and a copy of `std::locale` as data members. In addition, implementations may keep cached copies of locale facets, which are invalidated whenever `imbue()` is called. The concrete buffers such as `std::basic_filebuf` or `std::basic_stringbuf` are derived from `std::basic_streambuf`.

## Member functions


| cpp/io/basic_streambuf/dsc ~basic_streambuf | (see dedicated page) |

#### Locales

| cpp/io/basic_streambuf/dsc pubimbue | (see dedicated page) |
| cpp/io/basic_streambuf/dsc getloc | (see dedicated page) |

#### Positioning

| cpp/io/basic_streambuf/dsc pubsetbuf | (see dedicated page) |
| cpp/io/basic_streambuf/dsc pubseekoff | (see dedicated page) |
| cpp/io/basic_streambuf/dsc pubseekpos | (see dedicated page) |
| cpp/io/basic_streambuf/dsc pubsync | (see dedicated page) |

#### Get area

| cpp/io/basic_streambuf/dsc in_avail | (see dedicated page) |
| cpp/io/basic_streambuf/dsc snextc | (see dedicated page) |
| cpp/io/basic_streambuf/dsc sbumpc | (see dedicated page) |
| cpp/io/basic_streambuf/dsc sgetc | (see dedicated page) |
| cpp/io/basic_streambuf/dsc sgetn | (see dedicated page) |

#### Put area

| cpp/io/basic_streambuf/dsc sputc | (see dedicated page) |
| cpp/io/basic_streambuf/dsc sputn | (see dedicated page) |

#### Putback

| cpp/io/basic_streambuf/dsc sputbackc | (see dedicated page) |
| cpp/io/basic_streambuf/dsc sungetc | (see dedicated page) |
| cpp/io/basic_streambuf/dsc basic_streambuf | (see dedicated page) |
| cpp/io/basic_streambuf/dsc operator{{= | (see dedicated page) |
| cpp/io/basic_streambuf/dsc swap | (see dedicated page) |

#### Locales

| cpp/io/basic_streambuf/dsc imbue | (see dedicated page) |

#### Positioning

| cpp/io/basic_streambuf/dsc setbuf | (see dedicated page) |
| cpp/io/basic_streambuf/dsc seekoff | (see dedicated page) |
| cpp/io/basic_streambuf/dsc seekpos | (see dedicated page) |
| cpp/io/basic_streambuf/dsc sync | (see dedicated page) |

#### Get area

| cpp/io/basic_streambuf/dsc showmanyc | (see dedicated page) |
| cpp/io/basic_streambuf/dsc underflow | (see dedicated page) |
| cpp/io/basic_streambuf/dsc uflow | (see dedicated page) |
| cpp/io/basic_streambuf/dsc xsgetn | (see dedicated page) |
| cpp/io/basic_streambuf/dsc gptr | (see dedicated page) |
| cpp/io/basic_streambuf/dsc gbump | (see dedicated page) |
| cpp/io/basic_streambuf/dsc setg | (see dedicated page) |

#### Put area

| cpp/io/basic_streambuf/dsc xsputn | (see dedicated page) |
| cpp/io/basic_streambuf/dsc overflow | (see dedicated page) |
| cpp/io/basic_streambuf/dsc pptr | (see dedicated page) |
| cpp/io/basic_streambuf/dsc pbump | (see dedicated page) |
| cpp/io/basic_streambuf/dsc setp | (see dedicated page) |

#### Putback

| cpp/io/basic_streambuf/dsc pbackfail | (see dedicated page) |


## See also


| cpp/io/c/dsc FILE | (see dedicated page) |

