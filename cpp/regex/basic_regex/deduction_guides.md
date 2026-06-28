---
title: deduction guides for std::basic_regex
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/basic_regex/deduction_guides
---


# deduction guides for tt|std::basic_regex

ddcl|header=regex|since=c++17|1=
template< class ForwardIt >
basic_regex( ForwardIt, ForwardIt,
std::regex_constants::syntax_option_type = std::regex_constants::ECMAScript )
-> basic_regex<typename std::iterator_traits<ForwardIt>::value_type>;
This deduction guide is provided for `std::basic_regex` to allow deduction from an iterator range.

## Example


### Example

```cpp
#include <regex>
#include <vector>

int main()
{
    std::vector<char> v = {'a', 'b', 'c'};
    std::basic_regex re(v.begin(), v.end()); // uses explicit deduction guide
}
```

