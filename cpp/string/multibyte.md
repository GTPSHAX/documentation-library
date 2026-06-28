---
title: Null-terminated multibyte strings
type: Strings
source: https://en.cppreference.com/w/cpp/string/multibyte
---


# Null-terminated multibyte strings

A null-terminated multibyte string (NTMBS), or "multibyte string", is a sequence of nonzero bytes followed by a byte with value zero (the terminating null character).
Each character stored in the string may occupy more than one byte. The encoding used to represent characters in a multibyte character string is locale-specific: it may be UTF-8, GB18030, EUC-JP, Shift-JIS, etc. For example, the char array } is an NTMBS holding the string `"你好"` in UTF-8 multibyte encoding: the first three bytes encode the character 你, the next three bytes encode the character 好. The same string encoded in GB18030 is the char array }, where each of the two characters is encoded as a two-byte sequence.
In some multibyte encodings, any given multibyte character sequence may represent different characters depending on the previous byte sequences, known as "shift sequences". Such encodings are known as state-dependent: knowledge of the current shift state is required to interpret each character. An NTMBS is only valid if it begins and ends in the initial shift state: if a shift sequence was used, the corresponding unshift sequence has to be present before the terminating null character. Examples of such encodings are the 7-bit JIS, BOCU-1 and [https://www.unicode.org/reports/tr6 SCSU].
A multibyte character string is layout-compatible with null-terminated byte string (NTBS), that is, can be stored, copied, and examined using the same facilities, except for calculating the number of characters. If the correct locale is in effect, I/O functions also handle multibyte strings. Multibyte strings can be converted to and from wide strings using the `std::codecvt` member functions, `std::wstring_convert`, or the following locale-dependent conversion functions:

## Functions


#### Multibyte/wide character conversions

| cstdlib | |
| cpp/string/multibyte/dsc mblen | (see dedicated page) |
| cpp/string/multibyte/dsc mbtowc | (see dedicated page) |
| cpp/string/multibyte/dsc wctomb | (see dedicated page) |
| cpp/string/multibyte/dsc mbstowcs | (see dedicated page) |
| cpp/string/multibyte/dsc wcstombs | (see dedicated page) |
| cwchar | |
| cpp/string/multibyte/dsc mbrlen | (see dedicated page) |
| cpp/string/multibyte/dsc mbsinit | (see dedicated page) |
| cpp/string/multibyte/dsc btowc | (see dedicated page) |
| cpp/string/multibyte/dsc wctob | (see dedicated page) |
| cpp/string/multibyte/dsc mbrtowc | (see dedicated page) |
| cpp/string/multibyte/dsc wcrtomb | (see dedicated page) |
| cpp/string/multibyte/dsc mbsrtowcs | (see dedicated page) |
| cpp/string/multibyte/dsc wcsrtombs | (see dedicated page) |
| cuchar | |
| cpp/string/multibyte/dsc mbrtoc8 | (see dedicated page) |
| cpp/string/multibyte/dsc c8rtomb | (see dedicated page) |
| cpp/string/multibyte/dsc mbrtoc16 | (see dedicated page) |
| cpp/string/multibyte/dsc c16rtomb | (see dedicated page) |
| cpp/string/multibyte/dsc mbrtoc32 | (see dedicated page) |
| cpp/string/multibyte/dsc c32rtomb | (see dedicated page) |


## Types


| cwchar | |
| cpp/string/multibyte/dsc mbstate_t | (see dedicated page) |


## Macros


| climits | |
| cpp/string/multibyte/dsc MB_LEN_MAX | (see dedicated page) |
| cstdlib | |
| cpp/string/multibyte/dsc MB_CUR_MAX | (see dedicated page) |
| cuchar | |


## See also

