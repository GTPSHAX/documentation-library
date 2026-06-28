---
title: std::regex_search
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_search
---


```cpp
**Header:** `<`regex`>`
dcl|num=1|since=c++11|1=
template< class BidirIt, class Alloc, class CharT, class Traits >
bool regex_search( BidirIt first, BidirIt last,
std::match_results<BidirIt, Alloc>& m,
const std::basic_regex<CharT, Traits>& e,
std::regex_constants::match_flag_type flags =
std::regex_constants::match_default );
dcl|num=2|since=c++11|1=
template< class BidirIt, class CharT, class Traits >
bool regex_search( BidirIt first, BidirIt last,
const std::basic_regex<CharT, Traits>& e,
std::regex_constants::match_flag_type flags =
std::regex_constants::match_default );
dcl|num=3|since=c++11|1=
template< class CharT, class Alloc, class Traits >
bool regex_search( const CharT* str,
std::match_results<const CharT*, Alloc>& m,
const std::basic_regex<CharT, Traits>& e,
std::regex_constants::match_flag_type flags =
std::regex_constants::match_default );
dcl|num=4|since=c++11|1=
template< class CharT, class Traits >
bool regex_search( const CharT* str, const std::basic_regex<CharT, Traits>& e,
std::regex_constants::match_flag_type flags =
std::regex_constants::match_default );
dcl|num=5|since=c++11|1=
template< class STraits, class SAlloc, class Alloc,
class CharT, class Traits >
bool regex_search
( const std::basic_string<CharT, STraits, SAlloc>& s,
std::match_results
<typename std::basic_string<CharT, STraits, SAlloc>::const_iterator,
Alloc>& m,
const std::basic_regex<CharT, Traits>& e,
std::regex_constants::match_flag_type flags =
std::regex_constants::match_default );
dcl|num=6|since=c++11|1=
template< class STraits, class SAlloc, class CharT, class Traits >
bool regex_search( const std::basic_string<CharT, STraits, SAlloc>& s,
const std::basic_regex<CharT, Traits>& e,
std::regex_constants::match_flag_type flags =
std::regex_constants::match_default );
dcl|num=7|since=c++11|1=
template< class STraits, class SAlloc, class Alloc,
class CharT, class Traits >
bool regex_search
( const std::basic_string<CharT, STraits, SAlloc>&&,
std::match_results
<typename std::basic_string<CharT, STraits, SAlloc>::const_iterator,
Alloc>&,
const std::basic_regex<CharT, Traits>&,
std::regex_constants::match_flag_type flags =
std::regex_constants::match_default ) = delete;
```

Determines if there is a match between the regular expression `e` and some subsequence in the target character sequence. The detailed match result is stored in `m` (if present).
@1,2@ The target character sequence is represented by the range [first, last).
rev|until=c++23|
If `BidirIt` does not satisfy the requirements of *BidirectionalIterator*, the behavior is undefined.
rev|since=c++23|
If `BidirIt` does not model , the behavior is undefined.
@3,4@ The target character sequence is represented by the range [str, str + std::char_traits<CharT>::length(str)).
@5,6@ The target character sequence is represented by the string `s`.
7. The target character sequence cannot be represented by a `std::string` rvalue.
If a match does not exist, the following expressions involving `m` (if exists) should yield the specified values:


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

If a match exists, given any integer in  as `n`, the following expressions involving `m` should yield the specified values for each overload listed below:


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
| c | first |
| c | str |
| c | s.begin() |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/prefixc/core | ().second |
| colspan=3 | c | m[0].first |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/prefixc/core | ().matched |
| colspan=3 | c | 1=m.prefix().first != m.prefix().second |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/suffixc/core | ().first |
| colspan=3 | c | m[0].second |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/suffixc/core | ().second |
| c | last |
| <span style="text-align: start;">c multi | std::char_traits<CharT>:: | length(str) + str</span> |
| c | s.end() |
| - |
| box | c/core | m.ltt | cpp/regex/match_results/suffixc/core | ().matched |
| colspan=3 | c | 1=m.suffix().first != m.suffix().second |
| - |
| box | c/core | mltt | cpp/regex/match_results/operator at | [0]c/core | .first |
| colspan=3 | the start of the sequence that matched c | e |
| - |
| box | c/core | mltt | cpp/regex/match_results/operator at | [0]c/core | .second |
| colspan=3 | the end of the sequence that matched c | e |
| - |
| box | c/core | mltt | cpp/regex/match_results/operator at | [0]c/core | .matched |
| colspan=3 | c | true |
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

Returns `true` if a match exists, `false` otherwise.

## Notes

In order to examine all matches within the target sequence, `std::regex_search` may be called in a loop, restarting each time from `m[0].second` of the previous call. `std::regex_iterator` offers an easy interface to this iteration.

## Example


### Example

```cpp
#include <cstddef>
#include <iostream>
#include <regex>
#include <string>

int main()
{
    std::string lines[] = {"Roses are #ff0000",
                           "violets are #0000ff",
                           "all of my base are belong to you"};

    std::regex color_regex("#([a-f0-9]{2})"
                            "([a-f0-9]{2})"
                            "([a-f0-9]{2})");

    // simple match
    for (const auto& line : lines)
        std::cout << line << ": " << std::boolalpha
                  << std::regex_search(line, color_regex) << '\n';
    std::cout << '\n';

    // show contents of marked subexpressions within each match
    std::smatch color_match;
    for (const auto& line : lines)
        if (std::regex_search(line, color_match, color_regex))
        {
            std::cout << "matches for '" << line << "'\n";
            std::cout << "Prefix: '" << color_match.prefix() << "'\n";
            for (std::size_t i = 0; i < color_match.size(); ++i) 
                std::cout << i << ": " << color_match[i] << '\n';
            std::cout << "Suffix: '" << color_match.suffix() << "\'\n\n";
        }

    // repeated search (see also std::regex_iterator)
    std::string log(R"(
        Speed:	366
        Mass:	35
        Speed:	378
        Mass:	32
        Speed:	400
	Mass:	30)");
    std::regex r(R"(Speed:\t\d*)");
    for (std::smatch sm; regex_search(log, sm, r);)
    {
        std::cout << sm.str() << '\n';
        log = sm.suffix();
    }

    // C-style string demo
    std::cmatch cm;
    if (std::regex_search("this is a test", cm, std::regex("test"))) 
        std::cout << "\nFound " << cm[0] << " at position "
                  << cm.prefix().length() << '\n';
}
```


**Output:**
```
Roses are #ff0000: true
violets are #0000ff: true
all of my base are belong to you: false

matches for 'Roses are #ff0000'
Prefix: 'Roses are '
0: #ff0000
1: ff
2: 00
3: 00
Suffix: ''

matches for 'violets are #0000ff'
Prefix: 'violets are '
0: #0000ff
1: 00
2: 00
3: ff
Suffix: ''

Speed:	366
Speed:	378
Speed:	400

Found test at position 10
```


## Defect reports


## See also


| cpp/regex/dsc basic_regex | (see dedicated page) |
| cpp/regex/dsc match_results | (see dedicated page) |
| cpp/regex/dsc regex_match | (see dedicated page) |

