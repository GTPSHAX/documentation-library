---
title: std::ios_base
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base
---

ddcl|header=ios|
class ios_base;
The class `ios_base` is a multipurpose class that serves as the base class for all I/O stream classes. It maintains several kinds of data:
1. state information: stream status flags.
2. control information: flags that control formatting of both input and output sequences and the imbued locale.
3. private storage: indexed extensible data structure that allows both `long` and `void*` members, which may be implemented as two arbitrary-length arrays or a single array of two-element structs or another container.
4. callbacks: arbitrary number of user-defined functions to be called from , `std::basic_ios::copyfmt()`, and .
Typical implementation holds member constants corresponding to all values of `cpp/io/ios_base/fmtflags`, `cpp/io/ios_base/iostate`, `cpp/io/ios_base/openmode`, and `cpp/io/ios_base/seekdir` shown below, member variables to maintain current precision, width, and formatting flags, the exception mask, the buffer error state, a resizeable container holding the callbacks, the currently imbued locale, the private storage, and a static integer variable for .

## Member functions


| cpp/io/ios_base/dsc constructor | (see dedicated page) |
| cpp/io/ios_base/dsc destructor | (see dedicated page) |
| cpp/io/ios_base/dsc operator{{= | (see dedicated page) |

#### Formatting

| cpp/io/ios_base/dsc flags | (see dedicated page) |
| cpp/io/ios_base/dsc setf | (see dedicated page) |
| cpp/io/ios_base/dsc unsetf | (see dedicated page) |
| cpp/io/ios_base/dsc precision | (see dedicated page) |
| cpp/io/ios_base/dsc width | (see dedicated page) |

#### Locales

| cpp/io/ios_base/dsc imbue | (see dedicated page) |
| cpp/io/ios_base/dsc getloc | (see dedicated page) |

#### Internal extensible array

| cpp/io/ios_base/dsc xalloc | (see dedicated page) |
| cpp/io/ios_base/dsc iword | (see dedicated page) |
| cpp/io/ios_base/dsc pword | (see dedicated page) |

#### Miscellaneous

| cpp/io/ios_base/dsc register_callback | (see dedicated page) |
| cpp/io/ios_base/dsc sync_with_stdio | (see dedicated page) |
| cpp/io/ios_base/dsc failure | (see dedicated page) |
| cpp/io/ios_base/dsc Init | (see dedicated page) |


| Item | Description |
|------|-------------|
| **Type** | Explanation |
| cpp/io/ios_base/dsc openmode | (see dedicated page) |
| cpp/io/ios_base/dsc fmtflags | (see dedicated page) |
| cpp/io/ios_base/dsc iostate | (see dedicated page) |
| cpp/io/ios_base/dsc seekdir | (see dedicated page) |
| cpp/io/ios_base/dsc event | (see dedicated page) |
| cpp/io/ios_base/dsc event_callback | (see dedicated page) |

rev|until=c++17|


| Item | Description |
|------|-------------|

#### Deprecated member types

| **Type** | Explanation |


## Defect reports


## See also


| cpp/io/dsc basic_ios | (see dedicated page) |

