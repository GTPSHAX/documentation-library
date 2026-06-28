---
title: std::regex_match
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_match
---


```cpp
**Header:** `<`regex`>`
dcl|num=1|since=c++11|1=
template< class BidirIt, class Alloc, class CharT, class Traits >
bool regex_match( BidirIt first, BidirIt last,
std::match_results<BidirIt, Alloc>& m,
const std::basic_regex<CharT, Traits>& e,
std::regex_constants::match_flag_type flags =
std::regex_constants::match_default );
dcl|num=2|since=c++11|1=
template< class BidirIt, class CharT, class Traits >
bool regex_match( BidirIt first, BidirIt last,
const std::basic_regex<CharT, Traits>& e,
std::regex_constants::match_flag_type flags =
std::regex_constants::match_default );
dcl|num=3|since=c++11|1=
template< class CharT, class Alloc, class Traits >
bool regex_match( const CharT* str,
std::match_results<const CharT*, Alloc>& m,
const std::basic_regex<CharT, Traits>& e,
std::regex_constants::match_flag_type flags =
std::regex_constants::match_default );
dcl|num=4|since=c++11|1=
template< class CharT, class Traits >
bool regex_match( const CharT* str, const std::basic_regex<CharT, Traits>& e,
std::regex_constants::match_flag_type flags =
std::regex_constants::match_default );
dcl|num=5|since=c++11|1=
template< class STraits, class SAlloc, class Alloc,
class CharT, class Traits >
bool regex_match
( const std::basic_string<CharT, STraits, SAlloc>& s,
std::match_results
<typename std::basic_string<CharT, STraits, SAlloc>::const_iterator,
Alloc>& m,
const std::basic_regex<CharT, Traits>& e,
std::regex_constants::match_flag_type flags =
std::regex_constants::match_default );
dcl|num=6|since=c++11|1=
template< class STraits, class SAlloc, class CharT, class Traits >
bool regex_match( const std::basic_string<CharT, STraits, SAlloc>& s,
const std::basic_regex<CharT, Traits>& e,
std::regex_constants::match_flag_type flags =
std::regex_constants::match_default );
dcl|num=7|since=c++11|1=
template< class STraits, class SAlloc, class Alloc,
class CharT, class Traits >
bool regex_match
( const std::basic_string<CharT, STraits, SAlloc>&&,
std::match_results
<typename std::basic_string<CharT, STraits, SAlloc>::const_iterator,
Alloc>&,
const std::basic_regex<CharT, Traits>&,
std::regex_constants::match_flag_type flags =
std::regex_constants::match_default ) = delete;
```

Determines if the regular expression `e` matches the entire target character sequence. The detailed match result is stored in `m` (if present).
@1,2@ The target character sequence is represented by the range [first, last).
rev|until=c++23|
If `BidirIt` does not satisfy the requirements of *BidirectionalIterator*, the behavior is undefined.
rev|since=c++23|
If `BidirIt` does not model , the behavior is undefined.
@3,4@ The target character sequence is represented by the range [str, str + std::char_traits<CharT>::length(str)).
@5,6@ The target character sequence is represented by the string `s`.
7. The target character sequence cannot be represented by a `std::string` rvalue.
If the match does not exist, the following expressions involving `m` (if exists) should yield the specified values:


| Expression |
| Value |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/readyc/core | () |
| c | true |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/sizec/core | () |
| c | 0 |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/emptyc/core | () |
| c | true |

If the match exists, given any integer in  as `n`, the following expressions involving `m` should yield the specified values for each overload listed below:


| rowspan=2 | nbsp | 6Expressionnbsp | 6 |
| colspan=3 | Value |
| - |
| nbsp | 11Overload v | 1nbsp | 11 |
| nbsp | 11Overload v | 3nbsp | 11 |
| nbsp | 11Overload v | 5nbsp | 11 |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/readyc/core | () |
| colspan=3 | c | true |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/sizec/core | () |
| colspan=3 | box | c/core | 1 + e.ltt | cpp/regex/basic_regex/mark_countc/core | () |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/emptyc/core | () |
| colspan=3 | c | false |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/prefixc/core | ().first |
| rowspan=2 | c | first |
| rowspan=2 | c | str |
| rowspan=2 | c | s.begin() |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/prefixc/core | ().second |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/prefixc/core | ().matched |
| colspan=3 | nbsp | 4c | false |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/suffixc/core | ().first |
| rowspan=2 | c | last |
| rowspan=2 | <span style="text-align: start;">c multi | std::char_traits<CharT>:: | length(str) + str</span> |
| rowspan=2 | c | s.end() |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/suffixc/core | ().second |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/suffixc/core | ().matched |
| colspan=3 | nbsp | 4c | false |
| - |
| box | c/core | mltt | cpp/regex/match_results/operator at | [0]c/core | .first |
| c | first |
| c | str |
| c | s.begin() |
| - |
| box | c/core | mltt | cpp/regex/match_results/operator at | [0]c/core | .second |
| c | last |
| <span style="text-align: start;">c multi | std::char_traits<CharT>:: | length(str) + str</span> |
| c | s.end() |
| - |
| box | c/core | mltt | cpp/regex/match_results/operator at | [0]c/core | .matched |
| colspan=3 | nbsp | 4c | true |
| - |
| box | c/core | mltt | cpp/regex/match_results/operator at | [n]c/core | .first |
| colspan=3 |  |
| - |
| box | c/core | mltt | cpp/regex/match_results/operator at | [n]c/core | .second |
| colspan=3 |  |
| - |
| box | c/core | mltt | cpp/regex/match_results/operator at | [n]c/core | .matched |
| colspan=3 |  |


## Parameters


### Parameters

- `first, last` - the target character range
- `str` - the target null-terminated C-style string
- `s` - the target `std::basic_string`
- `m` - the match results
- `e` - the regular expression
- `flags` - flags used to determine how the match will be performed

## Return value

Returns `true` if the entire target sequence matches `e`, `false` otherwise.

## Notes

Because `regex_match` only considers full matches, the same regex may give different matches between `regex_match` and `std::regex_search`:

```cpp
std::regex re("Get{{!
```

std::cmatch m;
std::regex_search("GetValue", m, re);  // returns true, and m[0] contains "Get"
std::regex_match ("GetValue", m, re);  // returns true, and m[0] contains "GetValue"
std::regex_search("GetValues", m, re); // returns true, and m[0] contains "Get"
std::regex_match ("GetValues", m, re); // returns false

## Example


### Example

```cpp
#include <cstddef>
#include <iostream>
#include <regex>
#include <string>

int main()
{
    // Simple regular expression matching
    const std::string fnames[] = {"foo.txt", "bar.txt", "baz.dat", "zoidberg"};
    const std::regex txt_regex("[a-z]+\\.txt");

    for (const auto& fname : fnames)
        std::cout << fname << ": " << std::regex_match(fname, txt_regex) << '\n';

    // Extraction of a sub-match
    const std::regex base_regex("([a-z]+)\\.txt");
    std::smatch base_match;

    for (const auto& fname : fnames)
        if (std::regex_match(fname, base_match, base_regex))
            // The first sub_match is the whole string; the next
            // sub_match is the first parenthesized expression.
            if (base_match.size() == 2)
            {
                std::ssub_match base_sub_match = base_match[1];
                std::string base = base_sub_match.str();
                std::cout << fname << " has a base of " << base << '\n';
            }

    // Extraction of several sub-matches
    const std::regex pieces_regex("([a-z]+)\\.([a-z]+)");
    std::smatch pieces_match;

    for (const auto& fname : fnames)
        if (std::regex_match(fname, pieces_match, pieces_regex))
        {
            std::cout << fname << '\n';
            for (std::size_t i = 0; i < pieces_match.size(); ++i)
            {
                std::ssub_match sub_match = pieces_match[i];
                std::string piece = sub_match.str();
                std::cout << "  submatch " << i << ": " << piece << '\n';
            }
        }
}
```


**Output:**
```
foo.txt: 1
bar.txt: 1
baz.dat: 0
zoidberg: 0
foo.txt has a base of foo
bar.txt has a base of bar
foo.txt
  submatch 0: foo.txt
  submatch 1: foo
  submatch 2: txt
bar.txt
  submatch 0: bar.txt
  submatch 1: bar
  submatch 2: txt
baz.dat
  submatch 0: baz.dat
  submatch 1: baz
  submatch 2: dat
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2273 | C++11 | it was unclear whether partial matches are considered | only considers full matches |


## See also


| cpp/regex/dsc basic_regex | (see dedicated page) |
| cpp/regex/dsc match_results | (see dedicated page) |
| cpp/regex/dsc regex_search | (see dedicated page) |

