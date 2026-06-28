---
title: std::ctype::widen
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/ctype/widen
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
CharT widen( char c ) const;
dcl|num=2|1=
public:
const char* widen( const char* beg, const char* end, CharT* dst ) const;
dcl|num=3|1=
protected:
virtual CharT do_widen( char c ) const;
dcl|num=4|1=
protected:
virtual const char* do_widen( const char* beg, const char* end, CharT* dst ) const;
```

@1,2@ Public member function, calls the corresponding protected virtual member function `do_widen` overload of the most derived class. Overload (1) calls `do_widen(c)`, overload (2) calls `do_widen(beg, end, dst)`.
3. Converts the single-byte character `c` to the corresponding wide character representation using the simplest reasonable transformation. Typically, this applies only to the characters whose multibyte encoding is a single byte (e.g. U+0000-U+007F in UTF-8).
4. For every character in the character array [beg, end), writes the corresponding widened character to the successive locations in the character array pointed to by `dst`.
Widening always returns a wide character, but only the characters from the <sup>(until C++23)</sup> basic source character set<sup>(since C++23)</sup> basic character set are guaranteed to have a unique, well-defined, widening transformation, which is also guaranteed to be reversible (by `narrow()`). In practice, all characters whose multibyte representation is a single byte are usually widened to their wide character counterparts, and the rest of the possible single-byte values are usually mapped into the same placeholder value, typically `CharT(-1)`.
Widening, if successful, preserves all character classification categories known to `is()`.

## Parameters


### Parameters

- `c` - character to convert
- `dflt` - default value to produce if the conversion fails
- `beg` - pointer to the first character in an array of characters to convert
- `end` - one past the end pointer for the array of characters to convert
- `dst` - pointer to the first element of the array of characters to fill

## Return value

@1,3@ Widened character.
@2,4@ `end`

## Example


### Example

```cpp
#include <iostream>
#include <locale>

void try_widen(const std::ctype<wchar_t>& f, char c)
{
    wchar_t w = f.widen(c);
    std::cout << "The single-byte character " << +(unsigned char)c
              << " widens to " << +w << '\n';
}

int main()
{
    std::locale::global(std::locale("cs_CZ.iso88592"));
    auto& f = std::use_facet<std::ctype<wchar_t>>(std::locale());
    std::cout << std::hex << std::showbase << "In Czech ISO-8859-2 locale:\n";
    try_widen(f, 'a');
    try_widen(f, '\xdf'); // German letter ß (U+00df) in ISO-8859-2
    try_widen(f, '\xec'); // Czech letter ě (U+011b) in ISO-8859-2

    std::locale::global(std::locale("cs_CZ.utf8"));
    auto& f2 = std::use_facet<std::ctype<wchar_t>>(std::locale());
    std::cout << "In Czech UTF-8 locale:\n";
    try_widen(f2, 'a');
    try_widen(f2, '\xdf'); 
    try_widen(f2, '\xec'); 
}
```


**Output:**
```
In Czech ISO-8859-2 locale:
The single-byte character 0x61 widens to 0x61
The single-byte character 0xdf widens to 0xdf
The single-byte character 0xec widens to 0x11b
In Czech UTF-8 locale:
The single-byte character 0x61 widens to 0x61
The single-byte character 0xdf widens to 0xffffffff
The single-byte character 0xec widens to 0xffffffff
```


## Defect reports


## See also


| cpp/locale/ctype/dsc narrow | (see dedicated page) |
| cpp/io/basic_ios/dsc widen | (see dedicated page) |
| cpp/string/multibyte/dsc btowc | (see dedicated page) |

