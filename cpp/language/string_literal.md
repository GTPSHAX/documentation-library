---
title: String literal
type: Language
source: https://en.cppreference.com/w/cpp/language/string_literal
---


# String literal


## Syntax


**Syntax:**

- `*s-char-seq* (optional)**`"`**`
- `*d-char-seq* (optional)**`(`***r-char-seq* (optional)**`)`***d-char-seq* (optional)**`"`**|notes=<sup>(C++11)</sup>`
- `*s-char-seq* (optional)**`"`**`
- `*d-char-seq* (optional)**`(`***r-char-seq* (optional)**`)`***d-char-seq* (optional)**`"`**|notes=<sup>(C++11)</sup>`
- `*s-char-seq* (optional)**`"`**|notes=<sup>(C++11)</sup>`
- `*d-char-seq* (optional)**`(`***r-char-seq* (optional)**`)`***d-char-seq* (optional)**`"`**|notes=<sup>(C++11)</sup>`
- `*s-char-seq* (optional)**`"`**|notes=<sup>(C++11)</sup>`
- `*d-char-seq* (optional)**`(`***r-char-seq* (optional)**`)`***d-char-seq* (optional)**`"`**|notes=<sup>(C++11)</sup>`
- `*s-char-seq* (optional)**`"`**|notes=<sup>(C++11)</sup>`
- `*d-char-seq* (optional)**`(`***r-char-seq* (optional)**`)`***d-char-seq* (optional)**`"`**|notes=<sup>(C++11)</sup>`

## Explanation


### Parameters

- `{{spar` - s-char-seq|A sequence of one or more s-chars
- `{{spar` - s-char|One of
- * an escape sequence, as defined in `escape sequences`
- * a universal character name, as defined in `escape sequences`
- `{{spar` - basic-s-char|A character from the `translation character set`, except the double-quote `"`, backslash `\`, or new-line character
- `{{spar` - d-char-seq|A sequence of one or more d-chars, at most 16 characters long
- `{{spar` - d-char|A character from the `basic character set`, except parentheses, backslash and spaces
- `{{spar` - r-char-seq|A sequence of one or more r-chars, except that it must not contain the closing sequence 
- `{{spar` - r-char|A character from the `translation character set`


| Syntax |
| Kind |
| Type |
| Encoding |
| - |
| v | 1,2 |
| ordinary string literal |
| c/core | const char[N] |
| rlp | charset#Code unit and literal encoding | ordinary literal encoding |
| - |
| v | 3,4 |
| wide string literal |
| c/core | const wchar_t[N] |
| rlp | charset#Code unit and literal encoding | wide literal encoding |
| - |
| v | 5,6 |
| UTF-8 string literal |
| rrev multi | until1=c++20 | rev1=c/core | const char[N] | rev2=c/core | const char8_t[N] |
| UTF-8 |
| - |
| v | 7,8 |
| UTF-16 string literal |
| c/core | const char16_t[N] |
| UTF-16 |
| - |
| v | 9,10 |
| UTF-32 string literal |
| c/core | const char32_t[N] |
| UTF-32 |

In the types listed in the table above, `N` is the number of encoded code units, which is determined below.
Ordinary<sup>(since C++11)</sup>  and UTF-8 string literals are collectively referred to as narrow string literals.
Evaluating a string literal results in a string literal object with static `storage duration`. Whether all string literals are stored in `nonoverlapping objects` and whether successive evaluations of a string literal yield the same or a different object is unspecified.
The effect of attempting to modify a string literal object is undefined.

```cpp
bool b = "bar" == 3 + "foobar"; // can be true or false, unspecified

const char* pc = "Hello";
char* p = const_cast<char*>(pc);
p[0] = 'M'; // undefined behavior
```

rrev|since=c++11|

## Raw string literals

Raw string literals are string literals with a prefix containing  (syntaxes ). They do not escape any character, which means anything between the delimiters  and  becomes part of the string. The terminating *d-char-seq* is the same sequence of characters as the initial *d-char-seq*.

```cpp
// OK: contains one backslash,
// equivalent to "\\"
R"(\)";

// OK: contains four \n pairs,
// equivalent to "\\n\\n\\n\\n"
R"(\n\n\n\n)";

// OK: contains one close-parenthesis, two double-quotes and one open-parenthesis,
// equivalent to ")\"\"("
R"-()""()-";

// OK: equivalent to "\n)\\\na\"\"\n"
R"a(
)\
a""
)a";

// OK: equivalent to "x = \"\"\\y\"\""
R"(x = ""\y"")";

// R"<<(-_-)>>"; // Error: begin and end delimiters do not match
// R"-()-"-()-"; // Error: )-" appears in the middle and terminates the literal
```


## Initialization

String literal objects are initialized with the sequence of code unit values corresponding to the string literal’s sequence of s-chars<sup>(since C++11)</sup>  and r-chars, plus a terminating null character (U+0000), in order as follows:
1. For each contiguous sequence of basic-s-chars,<sup>(since C++11)</sup>  r-chars, `simple escape sequences` and `universal character names`, the sequence of character it denotes is encoded to a code unit sequence using the string literal’s associated character encoding. If a character lacks representation in the associated character encoding, then the program is ill-formed.
@@ If the associated character encoding is stateful, the first such sequence is encoded beginning with the initial encoding state and each subsequent sequence is encoded beginning with the final
encoding state of the prior sequence.
2. For each `numeric escape sequence`, given `v` as the integer value represented by the octal or hexadecimal number comprising the sequence of digits in the escape sequence, and `T` as the string literal’s array element type (see the table above):
* If `v` does not exceed the range of representable values of `T`, then the escape sequence contributes a single code unit with value `v`.
* Otherwise, if<sup>(since C++11)</sup>  the string literal is of syntax  `v` does not exceed the range of representable values of the corresponding unsigned type for the underlying type of `T`, then the escape sequence contributes a single code unit with a unique value of type `T`, that is congruent to $v mod 2, where `S` is the width of `T`.
* Otherwise, the program is ill-formed.
@@ If the associated character encoding is stateful, all such sequences have no effect on encoding state.
3. Each `conditional escape sequence` contributes an implementation-defined code unit sequence.
@@ If the associated character encoding is stateful, it is implementation-defined what effect these sequences have on encoding state.

## Concatenation

Adjacent string literals are concatenated at `translation phase 6` (after preprocessing):
* If the two string literals are of the same kind, the concatenated string literal is also of that kind.
rev|until=c++11|
* If an ordinary string literal is adjacent to a wide string literal, the behavior is undefined.
rev|since=c++11|
* If an ordinary string literal is adjacent to a non-ordinary string literal, the concatenated string literal is of the kind of the latter.
* If a UTF-8 string literal is adjacent to a wide string literal, the program is ill-formed.
rev|until=c++23|
* Any other combination is conditionally supported with implementation-defined semantics.
rev|since=c++23|
* Any other combination is ill-formed.

```cpp
"Hello, " "world!" // at phase 6, the 2 string literals form "Hello, world!"

L"Δx = %" PRId16   // at phase 4, PRId16 expands to "d"
                   // at phase 6, L"Δx = %" and "d" form L"Δx = %d"
```


## Unevaluated strings

The following contexts expect a string literal, but do not evaluate it:
* `language linkage` specification
rev|since=c++11|
* `static_assert`
* `literal operator` name
rev|since=c++14|
*
rev|since=c++20|
*
rev|since=c++26|
* `deleted function body`
rev|until=c++26|
It is unspecified whether non-ordinary string literals are allowed in these contexts<sup>(since C++11)</sup> , except that a literal operator name must use an ordinary string literal.
rev|since=c++26|
Only ordinary string literals are allowed in these contexts.
Each `universal character name` and each `simple escape sequence` in an unevaluated string is replaced by the member of the `translation character set` it denotes. An unevaluated string that contains a numeric escape sequence or a conditional escape sequence is ill-formed.

## Notes

String literals can be used to `initialize character arrays`. If an array is initialized like `1=char str[] = "foo";`, `str` will contain a copy of the string `"foo"`.
rev|until=c++11|
String literals are convertible and assignable to non-const `char*` or `wchar_t*` in order to be compatible with C, where string literals are of types `char[N]` and `wchar_t[N]`. Such implicit conversion is deprecated.
rev|since=c++11|
String literals are not convertible or assignable to non-const `CharT*`. An explicit cast (e.g. `const_cast`) must be used if such conversion is wanted.
A string literal is not necessarily a null-terminated character sequence: if a string literal has embedded null characters, it represents an array which contains more than one string.

```cpp
const char* p = "abc\0def"; // std::strlen(p) == 3, but the array has size 8
```

If a valid hexadecimal digit follows a hexadecimal escape sequence in a string literal, it would fail to compile as an invalid escape sequence. String concatenation can be used as a workaround:

```cpp
//const char* p = "\xfff"; // error: hexadecimal escape sequence out of range
const char* p = "\xff""f"; // OK: the literal is const char[3] holding {'\xff','f','\0'}
```


## Example


### Example

```cpp
#include <iostream>

// array1 and array2 contains the same values:
char array1[] = "Foo" "bar";
char array2[] = {'F', 'o', 'o', 'b', 'a', 'r', '\0'};

const char* s1 = R"foo(
Hello
  World
)foo";
// same as
const char* s2 = "\nHello\n  World\n";
// same as
const char* s3 = "\n"
                 "Hello\n"
                 "  World\n";

const wchar_t* s4 = L"ABC" L"DEF"; // OK, same as
const wchar_t* s5 = L"ABCDEF";
const char32_t* s6 = U"GHI" "JKL"; // OK, same as
const char32_t* s7 = U"GHIJKL";
const char16_t* s9 = "MN" u"OP" "QR"; // OK, same as
const char16_t* sA = u"MNOPQR";

// const auto* sB = u"Mixed" U"Types";
        // before C++23 may or may not be supported by
        // the implementation; ill-formed since C++23

const wchar_t* sC = LR"--(STUV)--"; // OK, raw string literal

int main()
{
    std::cout << array1 << ' ' << array2 << '\n'
              << s1 << s2 << s3 << std::endl;
    std::wcout << s4 << ' ' << s5 << ' ' << sC
               << std::endl;
}
```


**Output:**
```
Foobar Foobar

Hello
  World

Hello
  World

Hello
  World

ABCDEF ABCDEF STUV
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1823 | C++98 | whether string literals are distinct<br>was implementation-defined | distinctness is unspecified, and same<br>string literal can yield different object |


## References


## See also


| cpp/language/dsc user literal | (see dedicated page) |

