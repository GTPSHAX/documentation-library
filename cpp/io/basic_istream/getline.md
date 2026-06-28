---
title: std::basic_istream::getline
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream/getline
---


```cpp
dcl|num=1|
basic_istream& getline( char_type* s, std::streamsize count );
dcl|num=2|
basic_istream& getline( char_type* s, std::streamsize count, char_type delim );
```

Extracts characters from stream until end of line or the specified delimiter `delim`.
The first overload is equivalent to `getline(s, count, widen('\n'))`.
Behaves as *UnformattedInputFunction*. After constructing and checking the sentry object, extracts characters from `*this` and stores them in successive locations of the array whose first element is pointed to by `s`, until any of the following occurs (tested in the order shown):
# end of file condition occurs in the input sequence.
# the next available character `c` is the delimiter, as determined by `Traits::eq(c, delim)`. The delimiter is extracted (unlike `basic_istream::get()`) and counted towards `gcount()`, but is not stored.
# `count` is non-positive, or `count - 1` characters have been extracted (`setstate(failbit)` is called in this case).
If the function extracts no characters, ​`failbit` is set in the local error state before  is called.
In any case, if `count > 0`, it then stores a null character `CharT()` into the next successive location of the array and updates `gcount()`.

## Notes

Because condition #2 is tested before condition #3, the input line that exactly fits the buffer does not trigger `failbit`.
Because the terminating character is counted as an extracted character, an empty input line does not trigger `failbit`.

## Parameters


### Parameters

- `s` - pointer to the character string to store the characters to
- `count` - size of character string pointed to by `s`
- `delim` - delimiting character to stop the extraction at. It is extracted but not stored.

## Return value

`*this`

## Exceptions


## Example


### Example

```cpp
#include <array>
#include <iostream>
#include <sstream>
#include <vector>

int main()
{
    std::istringstream input("abc{{!
```

std::vector<std::array<char, 4>> v;
// note: the following loop terminates when std::ios_base::operator bool()
// on the stream returned from getline() returns false
for (std::array<char, 4> a; input.getline(&a[0], 4, '|');)
v.push_back(a);
for (auto& a : v)
std::cout << &a[0] << '\n';
}
|output=
abc
def
gh

## Defect reports


## See also


| cpp/string/basic_string/dsc getline | (see dedicated page) |
| cpp/io/basic_istream/dsc operator_gtgt | (see dedicated page) |
| cpp/io/basic_istream/dsc get | (see dedicated page) |
| cpp/io/basic_istream/dsc read | (see dedicated page) |

