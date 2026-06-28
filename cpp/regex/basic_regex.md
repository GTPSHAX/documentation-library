---
title: std::basic_regex
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/basic_regex
---

ddcl|header=regex|since=c++11|1=
template<
class CharT,
class Traits = std::regex_traits<CharT>
> class basic_regex;
The class template `basic_regex` provides a general framework for holding regular expressions.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/regex/basic_regex/dsc constructor | (see dedicated page) |
| cpp/regex/basic_regex/dsc destructor | (see dedicated page) |
| cpp/regex/basic_regex/dsc operator{{= | (see dedicated page) |
| cpp/regex/basic_regex/dsc assign | (see dedicated page) |

#### Observers

| cpp/regex/basic_regex/dsc mark_count | (see dedicated page) |
| cpp/regex/basic_regex/dsc flags | (see dedicated page) |

#### Locale

| cpp/regex/basic_regex/dsc getloc | (see dedicated page) |
| cpp/regex/basic_regex/dsc imbue | (see dedicated page) |

#### Modifiers

| cpp/regex/basic_regex/dsc swap | (see dedicated page) |

The member constants in `basic_regex` are duplicates of the `syntax_option_type` constants defined in the namespace `std::regex_constants`.

## Non-member functions


| cpp/regex/basic_regex/dsc swap2 | (see dedicated page) |


## Deduction guides<sup>(C++17)</sup>

