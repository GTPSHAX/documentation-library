---
title: std::strtok
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strtok
---

ddcl|header=cstring|
char* strtok( char* str, const char* delim );
Tokenizes a null-terminated byte string.
A sequence of calls to `std::strtok` breaks the string pointed to by `str` into a sequence of tokens, each of which is delimited by a character from the string pointed to by `delim`. Each call in the sequence has a :
* If `str` is non-null, the call is the ''first call'' in the sequence. The search target is null-terminated byte string pointed to by `str`.
* If `str` is null, the call is one of the ''subsequent calls'' in the sequence. The search target is determined by the previous call in the sequence.
Each call in the sequence searches the search target for the first character that is '''not''' contained in the ''separator string'' pointed to by `delim`, the separator string can be different from call to call.
* If no such character is found, then there are no tokens in the search target. The search target for the next call in the sequence is unchanged.
* If such a character is found, it is the start of the current token. `std::strtok` then searches from there for the first character that is contained in the separator string.
** If no such character is found, the current token extends to the end of search target. The search target for the next call in the sequence is an empty string.
** If such a character is found, it is overwritten by a null character, which terminates the current token. The search target for the next call in the sequence starts from the following character.
If `str` or `delim` is not a pointer to a null-terminated byte string, the behavior is undefined.

## Parameters


### Parameters

- `str` - pointer to the null-terminated byte string to tokenize
- `delim` - pointer to the null-terminated byte string identifying delimiters

## Return value

Returns a pointer to the first character of the next token, or a null pointer if there is no token.

## Notes

This function is destructive: it writes the `'\0'` characters in the elements of the string `str`. In particular, a string literal cannot be used as the first argument of `std::strtok`.
Each call to this function modifies a static variable: is not thread safe.
Unlike most other tokenizers, the delimiters in `std::strtok` can be different for each subsequent token, and can even depend on the contents of the previous tokens.

## Possible implementation

eq fun|1=
char* strtok(char* str, const char* delim)
{
static char* buffer;
if (str != nullptr)
buffer = str;
buffer += std::strspn(buffer, delim);
if (*buffer == '\0')
return nullptr;
char* const tokenBegin = buffer;
buffer += std::strcspn(buffer, delim);
if (*buffer != '\0')
*buffer++ = '\0';
return tokenBegin;
}
Actual C++ library implementations of this function delegate to the C library, where it may be implemented directly (as in [https://github.com/bminor/musl/blob/master/src/string/strtok.c MUSL libc]), or in terms of its reentrant version (as in [https://github.com/bminor/glibc/blob/master/string/strtok.c GNU libc]).

## Example


### Example

```cpp
#include <cstring>
#include <iomanip>
#include <iostream>

int main() 
{
    char input[] = "one + two * (three - four)!";
    const char* delimiters = "! +- (*)";
    char* token = std::strtok(input, delimiters);
    while (token)
    {
        std::cout << std::quoted(token) << ' ';
        token = std::strtok(nullptr, delimiters);
    }

    std::cout << "\nContents of the input string now:\n\"";
    for (std::size_t n = 0; n < sizeof input; ++n)
    {
        if (const char c = input[n]; c != '\0')
            std::cout << c;
        else
            std::cout << "\\0";
    }
    std::cout << "\"\n";
}
```


**Output:**
```
"one" "two" "three" "four" 
Contents of the input string now:
"one\0+ two\0* (three\0- four\0!\0"
```


## See also


| cpp/string/byte/dsc strpbrk | (see dedicated page) |
| cpp/string/byte/dsc strcspn | (see dedicated page) |
| cpp/string/byte/dsc strspn | (see dedicated page) |
| cpp/ranges/dsc split_view | (see dedicated page) |

