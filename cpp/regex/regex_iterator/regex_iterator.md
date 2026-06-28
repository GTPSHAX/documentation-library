---
title: std::regex_iterator::regex_iterator
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_iterator/regex_iterator
---


```cpp
dcl|num=1|since=c++11|1=
regex_iterator();
dcl|num=2|since=c++11|1=
regex_iterator( BidirIt a, BidirIt b,
const regex_type& re,
std::regex_constants::match_flag_type m =
std::regex_constants::match_default );
dcl|num=3|since=c++11|1=
regex_iterator( const regex_iterator& );
dcl|num=4|since=c++11|1=
regex_iterator( BidirIt, BidirIt,
const regex_type&&,
std::regex_constants::match_flag_type =
std::regex_constants::match_default ) = delete;
```

Constructs a new `regex_iterator`:
1. Default constructor. Constructs an end-of-sequence iterator.
2. Constructs a `regex_iterator` from the sequence of characters [a, b), the regular expression `re`, and a flag `m` that governs matching behavior. This constructor performs an initial call to `std::regex_search` with this data. If the result of this initial call is `false`, `*this` is set to an end-of-sequence iterator.
3. Copies a `regex_iterator`.
4. The overload  is not allowed to be called with a temporary regex, since the returned iterator would be immediately invalidated.

## Parameters


### Parameters

- `a` - *BidirectionalIterator* to the beginning of the target character sequence
- `b` - *BidirectionalIterator* to the end of the target character sequence
- `re` - regular expression used to search the target character sequence
- `m` - flags that govern the behavior of `re`

## Example


### Example

```cpp
#include <iostream>
#include <regex>
#include <string_view>

int main()
{
    constexpr std::string_view str{R"(
        #ONE: *p = &Mass;
        #Two: MOV %rd, 42
    )"};
    const std::regex re("[a-w]");

    // create regex_iterator, overload (2)
    auto it = std::regex_iterator<std::string_view::iterator>
    {
        str.cbegin(), str.cend(),
        re // re is lvalue; if an immediate expression was used
           // instead, e.g. std::regex{"[a-z]"}, this would
           // produce an error since overload (4) is deleted
    };

    for (decltype(it) last /* overload (1) */; it != last; ++it)
        std::cout << (*it).str();
    std::cout << '\n';
}
```


**Output:**
```
password
```


## Defect reports

