---
title: Regular expressions library
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex
---


# Regular expressions library mark since c++11

The regular expressions library provides a class that represents [Regular expression|regular expressions](https://en.wikipedia.org/wiki/Regular expression|regular expressions), which are a kind of mini-language used to perform pattern matching within strings. Almost all operations with regexes can be characterized by operating on several of the following objects:
* '''Target sequence'''. The character sequence that is searched for a pattern. This may be a range specified by two iterators, a null-terminated character string or a `std::string`.
* '''Pattern'''. This is the regular expression itself. It determines what constitutes a match. It is an object of type `std::basic_regex`, constructed from a string with special grammar.
* '''Matched array'''. The information about matches may be retrieved as an object of type `std::match_results`.
* '''Replacement string'''. This is a string that determines how to replace the matches.

## Regular expression grammars

Patterns and replacement strings support the following regular expression grammars:
* Modified ECMAScript regular expression grammar. This is the default grammar.
* [https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html#tag_09_03 Basic POSIX regular expression grammar].
* [https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html#tag_09_04 Extended POSIX regular expression grammar].
* The regular expression grammar used by the  utility in POSIX.
* The regular expression grammar used by the  utility in POSIX. This is effectively the same as the basic POSIX regular expression grammar, with the addition of newline `'\n'` as an alternation separator.
* The regular expression grammar used by the `grep` utility, with the `-E` option, in POSIX. This is effectively the same as the extended POSIX regular expression grammar, with the addition of newline `'\n'` as an alternation separator in addition to `'.
Some grammar variations (such as case-insensitive matching) are also avaliable, see  for details.

## Main classes

These classes encapsulate a regular expression and the results of matching a regular expression within a target sequence of characters.


| cpp/regex/dsc basic_regex | (see dedicated page) |
| cpp/regex/dsc sub_match | (see dedicated page) |
| cpp/regex/dsc match_results | (see dedicated page) |


## Algorithms

These functions are used to apply the regular expression encapsulated in a regex to a target sequence of characters.


| cpp/regex/dsc regex_match | (see dedicated page) |
| cpp/regex/dsc regex_search | (see dedicated page) |
| cpp/regex/dsc regex_replace | (see dedicated page) |


## Iterators

The regex iterators are used to traverse the entire set of regular expression matches found within a sequence.


| cpp/regex/dsc regex_iterator | (see dedicated page) |
| cpp/regex/dsc regex_token_iterator | (see dedicated page) |


## Exceptions

This class defines the type of objects thrown as exceptions to report errors from the regular expressions library.


| cpp/regex/dsc regex_error | (see dedicated page) |


## Traits

The regex traits class is used to encapsulate the localizable aspects of a regex.


| cpp/regex/dsc regex_traits | (see dedicated page) |


## Constants


| std::regex_constants | |
| cpp/regex/dsc syntax_option_type | (see dedicated page) |
| cpp/regex/dsc match_flag_type | (see dedicated page) |
| cpp/regex/dsc error_type | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <iterator>
#include <regex>
#include <string>

int main()
{
    std::string s = "Some people, when confronted with a problem, think "
        "\"I know, I'll use regular expressions.\" "
        "Now they have two problems.";

    std::regex self_regex("REGULAR EXPRESSIONS",
        std::regex_constants::ECMAScript {{!
```

if (std::regex_search(s, self_regex))
std::cout << "Text contains the phrase 'regular expressions'\n";
std::regex word_regex("(\\w+)");
auto words_begin =
std::sregex_iterator(s.begin(), s.end(), word_regex);
auto words_end = std::sregex_iterator();
std::cout << "Found "
<< std::distance(words_begin, words_end)
<< " words\n";
const int N = 6;
std::cout << "Words longer than " << N << " characters:\n";
for (std::sregex_iterator i = words_begin; i != words_end; ++i)
{
std::smatch match = *i;
std::string match_str = match.str();
if (match_str.size() > N)
std::cout << "  " << match_str << '\n';
}
std::regex long_word_regex("(\\w{7,})");
std::string new_s = std::regex_replace(s, long_word_regex, "[$&]");
std::cout << new_s << '\n';
}
|output=
Text contains the phrase 'regular expressions'
Found 20 words
Words longer than 6 characters:
confronted
problem
regular
expressions
problems
Some people, when [confronted] with a [problem], think
"I know, I'll use [regular] [expressions]." Now they have two [problems].
