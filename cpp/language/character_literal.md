---
title: Character literal
type: Language
source: https://en.cppreference.com/w/cpp/language/character_literal
---


# Character literal


## Syntax


**Syntax:**

- `c-char**`'`**`
- `|**`u8'`**c-char**`'`**`
- `|**`u'`**c-char**`'`**`
- `|**`U'`**c-char**`'`**`
- `c-char**`'`**`
- `c-char-sequence**`'`**`
- `|**`L'`**c-char-sequence**`'`**`

### Parameters

- `{{spar` - c-char|either
- * an escape sequence, as defined in `escape sequences`
- * a universal character name, as defined in `escape sequences`
- `{{spar` - basic-c-char|A character from the <sup>(until C++23)</sup> `basic source character set`<sup>(since C++23)</sup> `translation character set`, except the single-quote `'`, backslash `\`, or new-line character
- `{{spar` - c-char-sequence|two or more *c-char*s

## Explanation

1. Ordinary character literal, e.g. `'a'` or `'\n'` or `'\13'`. Such literal has type `char` and the value equal to <sup>(until C++23)</sup> the representation of *c-char in the `execution character set`*<sup>(since C++23)</sup> the corresponding code point from `ordinary literal encoding`.
2. UTF-8 character literal, e.g. `u8'a'`. Such literal has type <sup>(until C++20)</sup> `char`<sup>(since C++20)</sup> `char8_t` and the value equal to [https://www.iso.org/standard/76835.html ISO/IEC 10646] code point value of *c-char*, provided that the code point value is representable with a single UTF-8 code unit (that is, *c-char* is in the range 0x0-0x7F, inclusive).
3. UTF-16 character literal, e.g. `u'猫'`, but not `u'🍌'` (`u'\U0001f34c'`). Such literal has type `char16_t` and the value equal to [https://www.iso.org/standard/76835.html ISO/IEC 10646] code point value of *c-char*, provided that the code point value is representable with a single UTF-16 code unit (that is, *c-char* is in the range 0x0-0xFFFF, inclusive).
4. UTF-32 character literal, e.g. `U'猫'` or `U'🍌'`. Such literal has type `char32_t` and the value equal to [https://www.iso.org/standard/76835.html ISO/IEC 10646] code point value of *c-char*.
5. Wide character literal, e.g. `L'β'` or `L'猫'`. Such literal has type `wchar_t` and the value equal to <sup>(until C++23)</sup> the value of *c-char in the execution wide character set*<sup>(since C++23)</sup> the corresponding code point from wide literal encoding.
6. <sup>(until C++23)</sup> Ordinary multicharacter literal<sup>(since C++23)</sup> Multicharacter literal, e.g. `'AB'`, is conditionally-supported, has type `int` and implementation-defined value.
7. Wide multicharacter literal, e.g. `L'AB'`, is conditionally-supported, has type `wchar_t` and implementation-defined value.

### Non-encodable characters

@1-5@ Given that *c-char* is not a numeric escape sequence (see below), if *c-char* is not representable in the literal’s associated character encoding or cannot be encoded as a single code unit in that encoding (e.g. a non-BMP value on Windows where `wchar_t` is 16-bit), the program is ill-formed.
6. If any *c-char* in *c-char-sequence* cannot be encoded as a single code unit in `ordinary literal encoding`, the program is ill-formed.
rrev|until=c++23|
7. If any *c-char* in *c-char-sequence* cannot be encoded as a single code unit in `wide literal encoding`, the program is ill-formed.

### Numeric escape sequences

Numeric (octal and hexadecimal) escape sequences can be used for specifying the value of the character.
rrev|since=c++23|
If the character literal contains only one numeric escape sequence, and the value specified by the escape sequence is representable by the unsigned version of its type, the character literal has the same value as the specified value (possibly after conversion to the character type).
A UTF-''N'' character literal can have any value representable by its type. If the value does not correspond to a valid Unicode code point, or if the its corresponding code point is not representable as single code unit in UTF-''N'', it can still be specified by a numeric escape sequence with the value. E.g. `u8'\xff'` is well-formed and equal to `char8_t(0xFF)`.
<br>
rrev multi
|rev1=
If the value specified by a numeric escape sequence used in an ordinary or wide character literal is not representable by `char` or `wchar_t` respectively, the value of the character literal is implementation-defined.
|since2=c++23|rev2=
If the value specified by a numeric escape sequence used in an ordinary or wide character literal with one *c-char* is representable by the unsigned version of the underlying type of `char` or `wchar_t` respectively, the value of the literal is the integer value of that unsigned integer type and the specified value converted to the type of the literal. Otherwise, the program is ill-formed.
<br>
rrev|since=c++11|
If the value specified by a numeric escape sequence used in a UTF-''N'' character literal is not representable by the corresponding `char''N''_t`, <sup>(until C++17)</sup> the value of the character literal is implementation-defined<sup>(since C++17)</sup> the program is ill-formed.

## Notes

In C, character constants such as `'a'` or `'\n'` have type `int`, rather than `char`.

## Example


### Example


**Output:**
```
Ordinary character literals:
'a' 	61 
'*' 	2A 

Ordinary multi-character literals:
'ab' 	62 61 00 00 
'abc' 	63 62 61 00 

UTF-8 character literals:
u8'a' 	61 

UTF-16 character literals:
u'a' 	61 00 
u'¢' 	A2 00 
u'猫' 	2B 73 

UTF-32 character literals:
U'a' 	61 00 00 00 
U'¢' 	A2 00 00 00 
U'猫' 	2B 73 00 00 
U'🍌' 	4C F3 01 00 

Wide character literals:
L'a' 	61 00 00 00 
L'¢' 	A2 00 00 00 
L'猫' 	2B 73 00 00 
L'🍌' 	4C F3 01 00
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-912 | C++98 | non-encodable ordinary character literal was unspecified | specified as conditionally-supported |
| cwg-1024 | C++98 | multicharacter literal was required to be supported | made conditionally-supported |
| cwg-1656 | C++98 | the meaning of numeric escape sequence<br>in a character literal was unclear | specified |


## References


## See also


| cpp/language/dsc user literal | (see dedicated page) |

