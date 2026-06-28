---
title: std::sscanf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/fscanf
---


```cpp
**Header:** `<`cstdio`>`
dcl|num=1|
int scanf( const char* format, ... );
dcl|num=2|
int fscanf( std::FILE* stream, const char* format, ... );
dcl|num=3|
int sscanf( const char* buffer, const char* format, ... );
```

Reads data from a variety of sources, interprets it according to `format` and stores the results into given locations.
1. Reads the data from `stdin`.
2. Reads the data from file stream `stream`.
3. Reads the data from null-terminated character string `buffer`.

## Parameters


### Parameters

- `stream` - input file stream to read from
- `buffer` - pointer to a null-terminated character string to read from
- `format` - pointer to a null-terminated character string specifying how to read the input
- `...` - receiving arguments

## Return value

Number of receiving arguments successfully assigned (which may be zero in case a matching failure occurred before the first receiving argument was assigned), or `EOF` if input failure occurs before the first receiving argument was assigned.

## Complexity

Not guaranteed. Notably, some implementations of `std::sscanf` are $O(N)$, where `1=N = std::strlen(buffer)` [https://sourceware.org/bugzilla/show_bug.cgi?id=17577]. For performant string parsing, see `std::from_chars`.

## Notes

Because most conversion specifiers first consume all consecutive whitespace, code such as

```cpp
std::scanf("%d", &a);
std::scanf("%d", &b);
```

will read two integers that are entered on different lines (second `%d` will consume the newline left over by the first) or on the same line, separated by spaces or tabs (second `%d` will consume the spaces or tabs).

```cpp
std::scanf("%d", &a);
std::scanf(" %c", &c); // ignore the endline after %d, then read a char
```

Note that some implementations of `std::sscanf` involve a call to `std::strlen`, which makes their runtime linear on the length of the entire string. This means that if `std::sscanf` is called in a loop to repeatedly parse values from the front of a string, your code might run in quadratic time ([https://nee.lv/2021/02/28/How-I-cut-GTA-Online-loading-times-by-70/#Problem-one-It%E2%80%99s%E2%80%A6-strlen example]).

## Example


### Example

```cpp
#include <clocale>
#include <cstdio>
#include <iostream>

int main()
{
    int i, j;
    float x, y;
    char str1[10], str2[4];
    wchar_t warr[2];
    std::setlocale(LC_ALL, "en_US.utf8");

    char input[] = "25 54.32E-1 Thompson 56789 0123 56ß水";
    // parse as follows:
    // %d: an integer 
    // %f: a floating-point value
    // %9s: a string of at most 9 non-whitespace characters
    // %2d: two-digit integer (digits 5 and 6)
    // %f: a floating-point value (digits 7, 8, 9)
    // %*d an integer which isn't stored anywhere
    // ' ': all consecutive whitespace
    // %3[0-9]: a string of at most 3 digits (digits 5 and 6)
    // %2lc: two wide characters, using multibyte to wide conversion
    const int ret = std::sscanf(input, "%d%f%9s%2d%f%*d %3[0-9]%2lc",
                                &i, &x, str1, &j, &y, str2, warr);

    std::cout << "Converted " << ret << " fields:\n"
                 "i = " << i << "\n"
                 "x = " << x << "\n"
                 "str1 = " << str1 << "\n"
                 "j = " << j << "\n"
                 "y = " << y << "\n"
                 "str2 = " << str2 << std::hex << "\n"
                 "warr[0] = U+" << (int)warr[0] << "\n"
                 "warr[1] = U+" << (int)warr[1] << '\n';
}
```


**Output:**
```
Converted 7 fields:
i = 25
x = 5.432
str1 = Thompson
j = 56
y = 789
str2 = 56
warr[0] = U+df
warr[1] = U+6c34
```


## See also


| cpp/io/c/dsc vfscanf | (see dedicated page) |
| cpp/io/c/dsc fgets | (see dedicated page) |
| cpp/io/c/dsc fprintf | (see dedicated page) |
| cpp/utility/dsc from_chars | (see dedicated page) |

