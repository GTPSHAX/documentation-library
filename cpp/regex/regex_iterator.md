---
title: std::regex_iterator
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_iterator
---

ddcl|header=regex|since=c++11|1=
template<
class BidirIt,
class CharT = typename std::iterator_traits<BidirIt>::value_type,
class Traits = std::regex_traits<CharT>
> class regex_iterator
`std::regex_iterator` is a read-only iterator that accesses the individual matches of a regular expression within the underlying character sequence. It meets the requirements of a *ForwardIterator*, except that for dereferenceable values `a` and `b` with `1=a == b`, `*a` and `*b` will not be bound to the same object.
On construction, and on every increment, it calls `std::regex_search` and remembers the result (that is, saves a copy of the `std::match_results<BidirIt>` value). The first object may be read when the iterator is constructed or when the first dereferencing is done. Otherwise, dereferencing only returns a copy of the most recently obtained regex match.
The default-constructed `std::regex_iterator` is the end-of-sequence iterator. When a valid `std::regex_iterator` is incremented after reaching the last match (`std::regex_search` returns `false`), it becomes equal to the end-of-sequence iterator. Dereferencing or incrementing it further invokes undefined behavior.
A typical implementation of `std::regex_iterator` holds the begin and the end iterators for the underlying sequence (two instances of `BidirIt`), a pointer to the regular expression (`const regex_type*`), the match flags (`std::regex_constants::match_flag_type`), and the current match (`std::match_results<BidirIt>`).

## Type requirements


### Parameters

- `BidirIt`

## Specializations

Several specializations for common character sequence types are defined:


| Item | Description |
|------|-------------|
| regex | |
| **Type** | Definition |


## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/regex/regex_iterator/dsc constructor | (see dedicated page) |
| cpp/regex/regex_iterator/dsc destructor | (see dedicated page) |
| cpp/regex/regex_iterator/dsc operator{{= | (see dedicated page) |
| cpp/regex/regex_iterator/dsc operator_cmp | (see dedicated page) |
| cpp/regex/regex_iterator/dsc operator* | (see dedicated page) |
| cpp/regex/regex_iterator/dsc operator_arith | (see dedicated page) |


## Notes

It is the programmer's responsibility to ensure that the `std::basic_regex` object passed to the iterator's constructor outlives the iterator. Because the iterator stores a pointer to the regex, incrementing the iterator after the regex was destroyed accesses a dangling pointer.
If the part of the regular expression that matched is just an assertion (`^`, `$`, `\b`, `\B`), the match stored in the iterator is a zero-length match, that is, `1=match[0].first == match[0].second`.

## Example


### Example

```cpp
#include <iostream>
#include <iterator>
#include <regex>
#include <string>

int main()
{
    const std::string s = "Quick brown fox.";

    std::regex words_regex("[^\\s]+");
    auto words_begin = std::sregex_iterator(s.begin(), s.end(), words_regex);
    auto words_end = std::sregex_iterator();

    std::cout << "Found " << std::distance(words_begin, words_end) << " words:\n";

    for (std::sregex_iterator i = words_begin; i != words_end; ++i)
    {
        std::smatch match = *i;
        std::string match_str = match.str();
        std::cout << match_str << '\n';
    }
}
```


**Output:**
```
Found 3 words:
Quick
brown
fox.
```


## Defect reports


## See also


| cpp/regex/dsc match_results | (see dedicated page) |
| cpp/regex/dsc regex_search | (see dedicated page) |

