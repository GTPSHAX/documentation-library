---
title: std::sub_match
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/sub_match
---

ddcl|header=regex|since=c++11|
template< class BidirIt >
class sub_match;
The class template `std::sub_match` is used by the regular expression engine to denote sequences of characters matched by marked sub-expressions.
A match is a [begin, end) pair within the target range matched by the regular expression, but with additional observer functions to enhance code clarity.
Only the default constructor is publicly accessible. Instances of `std::sub_match` are normally constructed and populated as a part of a `std::match_results` container during the processing of one of the regex algorithms.
The member functions return defined default values unless the `matched` member is `true`.
`std::sub_match` inherits from `std::pair<BidirIt, BidirIt>`, although it cannot be treated as a `std::pair` object because member functions such as assignment will not work as expected.

## Type requirements


### Parameters

- `BidirIt`

## Specializations

Several specializations for common character sequence types are provided:


| Item | Description |
|------|-------------|
| regex | |
| **Type** | Definition |


## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |

inherited|pair|

## Member functions


| cpp/regex/sub_match/dsc constructor | (see dedicated page) |

#### Observers

| cpp/regex/sub_match/dsc length | (see dedicated page) |
| cpp/regex/sub_match/dsc str | (see dedicated page) |
| cpp/regex/sub_match/dsc compare | (see dedicated page) |

#### Modifiers

| cpp/regex/sub_match/dsc swap | (see dedicated page) |


## Non-member functions


| cpp/regex/sub_match/dsc operator_cmp | (see dedicated page) |
| cpp/regex/sub_match/dsc operator_ltlt | (see dedicated page) |


## Example


### Example

```cpp
#include <cassert>
#include <iostream>
#include <regex>
#include <string>

int main()
{
    std::string sentence{"Friday the thirteenth."};
    const std::regex re{"([A-z]+) ([a-z]+) ([a-z]+)"};
    std::smatch words;
    std::regex_search(sentence, words, re);
    std::cout << std::boolalpha;
    for (const auto& m : words)
    {
        assert(m.matched);
        std::cout << "m: [" << m << "], m.length(): " << m.length() << ", "
                     "*m.first: '" << *m.first << "', "
                     "*m.second: '" << *m.second << "'\n";
    }
}
```


**Output:**
```
m: [Friday the thirteenth], m.length(): 21, *m.first: 'F', *m.second: '.'
m: [Friday], m.length(): 6, *m.first: 'F', *m.second: ' '
m: [the], m.length(): 3, *m.first: 't', *m.second: ' '
m: [thirteenth], m.length(): 10, *m.first: 't', *m.second: '.'
```


## See also


| cpp/regex/dsc regex_token_iterator | (see dedicated page) |

