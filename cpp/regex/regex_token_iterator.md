---
title: std::regex_token_iterator
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_token_iterator
---

ddcl|header=regex|since=c++11|1=
template<
class BidirIt,
class CharT = typename std::iterator_traits<BidirIt>::value_type,
class Traits = std::regex_traits<CharT>
> class regex_token_iterator
`std::regex_token_iterator` is a read-only *ForwardIterator* that accesses the individual sub-matches of every match of a regular expression within the underlying character sequence. It can also be used to access the parts of the sequence that were not matched by the given regular expression (e.g. as a tokenizer).
On construction, it constructs an `std::regex_iterator` and on every increment it steps through the requested sub-matches from the current match_results, incrementing the underlying `std::regex_iterator` when incrementing away from the last submatch.
The default-constructed `std::regex_token_iterator` is the end-of-sequence iterator. When a valid `std::regex_token_iterator` is incremented after reaching the last submatch of the last match, it becomes equal to the end-of-sequence iterator. Dereferencing or incrementing it further invokes undefined behavior.
Just before becoming the end-of-sequence iterator, a `std::regex_token_iterator` may become a ''suffix iterator'', if the index `-1` (non-matched fragment) appears in the list of the requested submatch indices. Such iterator, if dereferenced, returns a match_results corresponding to the sequence of characters between the last match and the end of sequence.
A typical implementation of `std::regex_token_iterator` holds the underlying `std::regex_iterator`, a container (e.g. `std::vector<int>`) of the requested submatch indices, the internal counter equal to the index of the submatch, a pointer to `std::sub_match`, pointing at the current submatch of the current match, and a `std::match_results` object containing the last non-matched character sequence (used in tokenizer mode).

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
| **Member type** | Definition |


## Member functions


| cpp/regex/regex_token_iterator/dsc constructor | (see dedicated page) |
| cpp/regex/regex_token_iterator/dsc destructor | (see dedicated page) |
| cpp/regex/regex_token_iterator/dsc operator{{= | (see dedicated page) |
| cpp/regex/regex_token_iterator/dsc operator cmp | (see dedicated page) |
| cpp/regex/regex_token_iterator/dsc operator* | (see dedicated page) |
| cpp/regex/regex_token_iterator/dsc operator arith | (see dedicated page) |


## Notes

It is the programmer's responsibility to ensure that the `std::basic_regex` object passed to the iterator's constructor outlives the iterator. Because the iterator stores a `std::regex_iterator` which stores a pointer to the regex, incrementing the iterator after the regex was destroyed results in undefined behavior.

## Example


### Example

```cpp
#include <algorithm>
#include <fstream>
#include <iostream>
#include <iterator>
#include <regex>

int main()
{
    // Tokenization (non-matched fragments)
    // Note that regex is matched only two times; when the third value is obtained
    // the iterator is a suffix iterator.
    const std::string text = "Quick brown fox.";
    const std::regex ws_re("\\s+"); // whitespace
    std::copy(std::sregex_token_iterator(text.begin(), text.end(), ws_re, -1),
              std::sregex_token_iterator(),
              std::ostream_iterator<std::string>(std::cout, "\n"));

    std::cout << '\n';

    // Iterating the first submatches
    const std::string html = R"(<p><a href="http://google.com">google</a> )"
                             R"(< a HREF ="http://cppreference.com">cppreference</a>\n</p>)";
    const std::regex url_re(R"!!(<\s*A\s+[^>]*href\s*=\s*"([^"]*)")!!", std::regex::icase);
    std::copy(std::sregex_token_iterator(html.begin(), html.end(), url_re, 1),
              std::sregex_token_iterator(),
              std::ostream_iterator<std::string>(std::cout, "\n"));
}
```


**Output:**
```
Quick
brown
fox.

http://google.com
http://cppreference.com
```


## Defect reports

