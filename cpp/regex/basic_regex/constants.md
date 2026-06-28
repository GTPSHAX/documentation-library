---
title: std::basic_regex constants
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/basic_regex/constants
---


```cpp
**Header:** `<`regex`>`
dcl|1=
static constexpr std::regex_constants::syntax_option_type icase =
std::regex_constants::icase;
static constexpr std::regex_constants::syntax_option_type nosubs =
std::regex_constants::nosubs;
static constexpr std::regex_constants::syntax_option_type optimize =
std::regex_constants::optimize;
static constexpr std::regex_constants::syntax_option_type collate =
std::regex_constants::collate;
static constexpr std::regex_constants::syntax_option_type ECMAScript =
std::regex_constants::ECMAScript;
static constexpr std::regex_constants::syntax_option_type basic =
std::regex_constants::basic;
static constexpr std::regex_constants::syntax_option_type extended =
std::regex_constants::extended;
static constexpr std::regex_constants::syntax_option_type awk =
std::regex_constants::awk;
static constexpr std::regex_constants::syntax_option_type grep =
std::regex_constants::grep;
static constexpr std::regex_constants::syntax_option_type egrep =
std::regex_constants::egrep;
dcl|since=c++17|1=
static constexpr std::regex_constants::syntax_option_type multiline =
std::regex_constants::multiline;
```

`std::basic_regex` defines several constants that govern general regex matching syntax.
These constants are duplicated from `std::regex_constants`:

## See also


| cpp/regex/dsc syntax_option_type | (see dedicated page) |

