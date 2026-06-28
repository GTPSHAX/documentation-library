---
title: std::regex_constants::syntax_option_type
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/syntax_option_type
---


```cpp
**Header:** `<`regex`>`
dcl|num=1|since=c++11|1=
using syntax_option_type = /* implementation-defined */;
|1=
constexpr syntax_option_type icase      = /* unspecified */;
constexpr syntax_option_type nosubs     = /* unspecified */;
constexpr syntax_option_type optimize   = /* unspecified */;
constexpr syntax_option_type collate    = /* unspecified */;
constexpr syntax_option_type ECMAScript = /* unspecified */;
constexpr syntax_option_type basic      = /* unspecified */;
constexpr syntax_option_type extended   = /* unspecified */;
constexpr syntax_option_type awk        = /* unspecified */;
constexpr syntax_option_type grep       = /* unspecified */;
constexpr syntax_option_type egrep      = /* unspecified */;
dcl|num=3|since=c++17|1=
inline constexpr syntax_option_type multiline = /* unspecified */;
```

1. The `syntax_option_type` is a *BitmaskType* that contains options that govern how regular expressions behave.
@2,3@ The possible values (`icase`, `optimize`, etc.) for type  are duplicated inside `cpp/regex/basic_regex/constants|std::basic_regex`.

## Constants


## Notes

Because POSIX uses "leftmost longest" matching rule (the longest matching subsequence is matched, and if there are several such subsequences, the first one is matched), it is not suitable, for example, for parsing markup languages: a POSIX regex such as `"<tag[^>]*>.*</tag>"` would match everything from the first `"<tag"` to the last `"</tag>"`, including every `"</tag>"` and `"<tag>"` in-between. On the other hand, ECMAScript supports non-greedy matches, and the ECMAScript regex `"<tag[^>]*>.*?</tag>"` would match only until the first closing tag.

## Example


### Example

```cpp
#include <iostream>
#include <regex>
#include <string>

int main()
{
    std::string str = "zzxayyzz";
    std::regex re1(".*(a{{!
```

std::regex re2(".*(a|xayy)", std::regex::extended); // POSIX
std::cout << "Searching for .*(a|xayy) in zzxayyzz:\n";
std::smatch m;
std::regex_search(str, m, re1);
std::cout << "  ECMA (depth first search) match: " << m[0] << '\n';
std::regex_search(str, m, re2);
std::cout << "  POSIX (leftmost longest)  match: " << m[0] << '\n';
}
|output=
Searching for .*(a|xayy) in zzxayyzz:
ECMA (depth first search) match: zzxa
POSIX (leftmost longest)  match: zzxayy

## Defect reports


## See also


| cpp/regex/dsc basic_regex | (see dedicated page) |

