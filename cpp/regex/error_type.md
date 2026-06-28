---
title: std::regex_constants::error_type
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/error_type
---


```cpp
**Header:** `<`regex`>`
dcl|num=1|since=c++11|1=
using error_type = /* implementation-defined */;
|1=
constexpr error_type error_collate =    /* unspecified */;
constexpr error_type error_ctype =      /* unspecified */;
constexpr error_type error_escape =     /* unspecified */;
constexpr error_type error_backref =    /* unspecified */;
constexpr error_type error_brack =      /* unspecified */;
constexpr error_type error_paren =      /* unspecified */;
constexpr error_type error_brace =      /* unspecified */;
constexpr error_type error_badbrace =   /* unspecified */;
constexpr error_type error_range =      /* unspecified */;
constexpr error_type error_space =      /* unspecified */;
constexpr error_type error_badrepeat =  /* unspecified */;
constexpr error_type error_complexity = /* unspecified */;
constexpr error_type error_stack =      /* unspecified */;
```

1. The `error_type` is a type that describes errors that may occur during regular expression parsing.

## Constants


| Item | Description |
|------|-------------|
| **Name** | Explanation |
| dsc|`error_brace`|the expression contains mismatched curly braces (`'{'` and c|'}') | |
| dsc|`error_badbrace`|the expression contains an invalid range in a } expression | |


## Example


### Example

```cpp
#include <cstddef>
#include <iomanip>
#include <iostream>
#include <regex>
#include <sstream>
#include <string>

void regular_expression_checker(const std::string& text,
                                const std::string& regex,
                                const std::regex::flag_type flags)
{
    std::cout << "Text: " << std::quoted(text) << '\n'
              << "Regex: " << std::quoted(regex) << '\n';

    try
    {
        const std::regex re{regex, flags};
        const bool matched = std::regex_match(text, re);

        std::stringstream out;
        out << (matched ? "MATCH!\n" : "DOES NOT MATCH!\n");

        std::smatch m;
        if (std::regex_search(text, m, re); !m.empty())
        {
            out << "prefix = [" << m.prefix().str().data() << "]\n";

            for (std::size_t i{}; i != m.size(); ++i)
                out << "  m[" << i << "] = [" << m[i].str().data() << "]\n";

            out << "suffix = [" << m.suffix().str().data() << "]\n";
        }
        std::cout << out.str() << '\n';
    }
    catch (std::regex_error& e)
    {
        std::cout << "Error: " << e.what() << ".\n\n";
    }
}

int main()
{
    constexpr std::regex::flag_type your_flags
        = std::regex::flag_type{0}
    // Choose one of the supported grammars:
        {{!
```

//  | std::regex::basic
//  | std::regex::extended
//  | std::regex::awk
//  | std::regex::grep
//  | std::regex::egrep
// Choose any of the next options:
//  | std::regex::icase
//  | std::regex::nosubs
//  | std::regex::optimize
//  | std::regex::collate
//  | std::regex::multiline
;
const std::string your_text = "Hello regular expressions.";
const std::string your_regex = R"(([a-zA-Z]+) ([a-z]+) ([a-z]+)\.)";
regular_expression_checker(your_text, your_regex, your_flags);
regular_expression_checker("Invalid!", R"(((.)(.))", your_flags);
regular_expression_checker("Invalid!", R"([.)", your_flags);
regular_expression_checker("Invalid!", R"([.]{})", your_flags);
regular_expression_checker("Invalid!", R"([1-0])", your_flags);
}
|p=true
|output=
Text: "Hello regular expressions."
Regex: "([a-zA-Z]+) ([a-z]+) ([a-z]+)\\."
MATCH!
prefix = []
m[0] = [Hello regular expressions.]
m[1] = [Hello]
m[2] = [regular]
m[3] = [expressions]
suffix = []
Text: "Invalid!"
Regex: "((.)(.)"
Error: Mismatched '(' and ')' in regular expression.
Text: "Invalid!"
Regex: "[."
Error: Unexpected character within '[...]' in regular expression.
Text: "Invalid!"
Regex: "[.]{}"
Error: Invalid range in '{}' in regular expression.
Text: "Invalid!"
Regex: "[1-0]"
Error: Invalid range in bracket expression..

## Defect reports


## See also


| cpp/regex/dsc regex_error | (see dedicated page) |

