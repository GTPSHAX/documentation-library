---
title: Character sets and encodings
type: Language
source: https://en.cppreference.com/w/cpp/language/charset
---


# Character sets and encodings

This page describes several character sets specified by the C++ standard.
rrev|since=c++23|

## Translation character set

The ''translation character set'' consists of the following elements:
* each abstract character assigned a code point in the [https://www.unicode.org/versions/latest/ Unicode] codespace, and
* a distinct character for each Unicode scalar value not assigned to an abstract character.
The translation character set is a superset of the basic character set and the basic literal character set (see below).

## Basic character set

The ''basic character set'' consists of the following <sup>(until C++26)</sup> 96<sup>(since C++26)</sup> 99 characters:
rrev|since=c++26|
The following characters are added to the basic character set since C++26:

## Basic literal character set

The ''basic literal character set'' consists of all characters of the basic character set, plus the following control characters:


| - |
| Code unit | Character |
| - |
| U+0000 | Null |
| - |
| U+0007 | Bell |
| - |
| U+0008 | Backspace |
| - |
| U+000D | Carriage return (CR) |


## Execution character set

The execution character set and the execution wide-character set are supersets of the basic literal
character set. The encodings of the execution character sets and the sets of additional elements
(if any) are locale-specific. Each element of execution wide-character set must be representable as a distinct `wchar_t` code unit.

## Code unit and literal encoding

A ''code unit'' is an integer value of character type. Characters in a `character literal` other than a multicharacter or non-encodable character literal or in a `string literal` are encoded as a sequence of one or more code units, as determined by the encoding prefix; this is termed the respective ''literal encoding''.
A literal encoding or a locale-specific encoding of one of the execution character sets encodes
each element of the basic literal character set as a single code unit with non-negative value, distinct from the code unit for any other such element. A character not in the basic literal character set can be encoded with more than one code unit; the value of such a code unit can be the same as that of a code unit for an element of the basic literal character set. The encodings of the execution character sets can be unrelated to any literal encoding.
The ordinary literal encoding is the encoding applied to an ordinary character or string literal. The wide literal encoding is the encoding applied to a wide character or string literal.
The U+0000 NULL character is encoded as the value 0. No other element of the translation character set is encoded with a code unit of value 0. The code unit value of each decimal digit character after the digit 0 (U+0030) shall be one greater than the value of the previous. The ordinary and wide literal encodings are otherwise implementation-defined.
For a UTF-8, UTF-16, or UTF-32 literal, the UCS scalar value corresponding to each character of the translation character set is encoded as specified in ISO/IEC 10646 for the respective UCS encoding form.

## Notes

The standard names of some character sets are changed in C++23 via `P2314R4`.


| - |
| New name(s) | Old name(s) |
| - |
| basic character set | basic source character set |
| - |
| basic literal character set | basic execution character set<br>basic execution wide-character set |

Mapping from source file <sup>(since C++23)</sup> (other than a UTF-8 source file) characters to the <sup>(until C++23)</sup> basic character set<sup>(since C++23)</sup> translation character set during `translation phase 1` is implementation-defined, so an implementation is required to document how the basic source characters are represented in source files.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-788 | C++98 | the values of the members of the execution character sets<br>were implementation-defined, but were not locale-specific | they are locale-specific |
| cwg-1796 | C++98 | the representation of the null (wide) character in<br>basic execution (wide-)character set had all zero bits | only required value to be zero |


## See also


| cpp/locale/dsc text_encoding | (see dedicated page) |

