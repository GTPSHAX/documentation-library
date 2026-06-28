---
title: Escape sequences
type: Language
source: https://en.cppreference.com/w/cpp/language/escape
---


# Escape sequences

Escape sequences are used to represent certain special characters within `string literal`s and `character literal`s.
The following escape sequences are available:


| - |
| Escape<br> sequence |
| Description |
| Representation |
| - |
| colspan="3" | Simple escape sequences |
| - |
| ttb | <nowiki>\'</nowiki> |
| single quote |
| byte tt | 0x27 in ASCII encoding |
| - |
| ttb | \" |
| double quote |
| byte tt | 0x22 in ASCII encoding |
| - |
| ttb | \? |
| question mark |
| byte tt | 0x3f in ASCII encoding |
| - |
| ttb | \\ |
| backslash |
| byte tt | 0x5c in ASCII encoding |
| - |
| ttb | \a |
| audible bell |
| byte tt | 0x07 in ASCII encoding |
| - |
| ttb | \b |
| backspace |
| byte tt | 0x08 in ASCII encoding |
| - |
| ttb | \f |
| form feed - new page |
| byte tt | 0x0c in ASCII encoding |
| - |
| ttb | \n |
| line feed - new line |
| byte tt | 0x0a in ASCII encoding |
| - |
| ttb | \r |
| carriage return |
| byte tt | 0x0d in ASCII encoding |
| - |
| ttb | \t |
| horizontal tab |
| byte tt | 0x09 in ASCII encoding |
| - |
| ttb | \v |
| vertical tab |
| byte tt | 0x0b in ASCII encoding |
| - |
| colspan="3" | Numeric escape sequences |
| - |
| ttb | \small | ''nnn'' |
| rowspan="2" | arbitrary octal value |
| code unit tt | ''nnn'' (1~3 octal digits) |
| - |
| ttb | \o{small | ''n...''} <sup>(C++23)</sup> |
| code unit tt | ''n...'' (arbitrary number of octal digits) |
| - |
| ttb | \xsmall | ''n...'' |
| rowspan="2" | arbitrary hexadecimal value |
| rowspan="2" | code unit tt | ''n...'' (arbitrary number of hexadecimal digits) |
| - |
| ttb | \x{small | ''n...''} <sup>(C++23)</sup> |
| - |
| colspan="3" | Conditional escape sequences<ref>Conditional escape sequences are conditionally-supported. The character ttb | small | ''c'' in each conditional escape sequence is a member of rev inl | until=c++23 | rlp | charset#Basic source character set | basic source character setrev inl | since=c++23 | rlp | charset#Basic character set | basic character set that is not the character following the ttb | \ in any other escape sequence.</ref> |
| - |
| ttb | \small | ''c'' |
| Implementation-defined |
| Implementation-defined |
| - |
| colspan="3" | Universal character names |
| - |
| ttb | \usmall | ''nnnn'' |
| rowspan="3" | arbitrary enwiki | Unicode value;<br>may result in several code units |
| code point tt | U+''nnnn'' (4 hexadecimal digits) |
| - |
| ttb | \u{small | ''n...''} <sup>(C++23)</sup> |
| code point tt | U+''n...'' (arbitrary number of hexadecimal digits) |
| - |
| ttb | \Usmall | ''nnnnnnnn'' |
| code point tt | U+''nnnnnnnn'' (8 hexadecimal digits) |
| - |
| ttb | \N{small | ''NAME''} <sup>(C++23)</sup> |
| arbitrary Unicode character |
| character named by tt | ''NAME'' (see [[#Named universal character escapes | below]]) |


## Range of universal character names

rrev multi
|rev1=
If a universal character name corresponds to a code point that is not 0x24 (`$`), 0x40 (`@`), nor 0x60 (```) and less than 0xA0, the program is ill-formed. In other words, members of `basic source character set` and control characters (in ranges 0x0-0x1F and 0x7F-0x9F) cannot be expressed in universal character names.
|since2=c++11|rev2=
If a universal character name corresponding to a code point of a member of `basic source character set` or control characters appear outside a `character` or `string literal`, the program is ill-formed.
If a universal character name corresponds surrogate code point (the range 0xD800-0xDFFF, inclusive), the program is ill-formed.
If a universal character name used in a UTF-16/32 string literal does not correspond to a code point in [https://www.iso.org/standard/76835.html ISO/IEC 10646] (the range 0x0-0x10FFFF, inclusive), the program is ill-formed.
|since3=c++20|rev3=
If a universal character name corresponding to a code point of a member of `basic source character set` or control characters appear outside a `character` or `string literal`, the program is ill-formed.
If a universal character name does not correspond to a code point in [https://www.iso.org/standard/76835.html ISO/IEC 10646] (the range 0x0-0x10FFFF, inclusive) or corresponds to a surrogate code point (the range 0xD800-0xDFFF, inclusive), the program is ill-formed.
|since4=c++23|rev4=
If a universal character name corresponding to a scalar value of a character in the `basic character set` or a control character appear outside a `character` or `string literal`, the program is ill-formed.
If a universal character name does not correspond to a scalar value of a character in the `translation character set`, the program is ill-formed.
rrev|since=c++23|

### Named universal character escapes


**Syntax:**

- `sdsc|1=`
- `**`\N{`** *n-char-sequence* }`

### Parameters

- `{{spar` - n-char-sequence|one or more *n-char*s
- `{{spar` - n-char|a character from the `translation character set`, except the right curly bracket } or new-line character
A universal character name of the syntax above is a ''named universal character''. It designates the corresponding character in the [https://www.unicode.org/versions/latest/ Unicode Standard] ([https://www.unicode.org/versions/latest/ch04.pdf chapter 4.8 Name]) if the *n-char-sequence* is equal to its character name or to one of its character name aliases; otherwise, the program is ill-formed.
These aliases are listed in the [https://www.unicode.org/reports/tr44/ Unicode Character Database]’s [https://www.unicode.org/Public/UCD/latest/ucd/NameAliases.txt NameAliases.txt]. None of these names or aliases have leading or trailing spaces.
A valid *n-char-sequence* must contain only uppercase Latin letters A through Z, digits, space, and hyphen-minus. Other characters never occur in a Unicode character name, and thus their appearance in a *n-char-sequence* always renders the program ill-formed.

## Notes

`\0` is the most commonly used octal escape sequence, because it represents the terminating null character in null-terminated strings.
The new-line character `\n` has special meaning when used in text mode I/O: it is converted to the OS-specific newline representation, usually a byte or byte sequence. Some systems mark their lines with length fields instead.
Octal escape sequences have a limit of three octal digits, but terminate at the first character that is not a valid octal digit if encountered sooner.
Hexadecimal escape sequences have no length limit and terminate at the first character that is not a valid hexadecimal digit. If the value represented by a single hexadecimal escape sequence does not fit the range of values represented by the character type used in this string literal (`char`, <sup>(since C++20)</sup> `char8_t`, <sup>(since C++11)</sup> `char16_t`, `char32_t`, or `wchar_t`), the result is unspecified.
rrev|since=c++11|
A universal character name in a narrow string literal or a 16-bit string literal may map to more than one code unit, e.g. `\U0001f34c` is 4 `char` code units in UTF-8 (`\xF0\x9F\x8D\x8C`) and 2 `char16_t` code units in UTF-16 (`\xD83C\xDF4C`).
The question mark escape sequence `\?` is used to prevent `trigraphs` from being interpreted inside string literals: a string such as `"??/"` is compiled as `"\"`, but if the second question mark is escaped, as in `"?\?/"`, it becomes `"??/"`. <sup>(since C++17)</sup> As trigraphs have been removed from C++, the question mark escape sequence is no longer necessary. It is preserved for compatibility with C++14 (and former revisions) and C.

## Example


### Example

```cpp
#include <iostream>

int main()
{
    std::cout << "This\nis\na\ntest\n\n";
    std::cout << "She said, \"Sells she seashells on the seashore?\"\n";
}
```


**Output:**
```
This
is
a
test

She said, "Sells she seashells on the seashore?"
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-505 | C++98 | the behavior was undefined if the character following<br>a backslash was not one of those specified in the table | made conditionally supported<br>(semantic is implementation-defined) |


## See also

* `ASCII chart`
