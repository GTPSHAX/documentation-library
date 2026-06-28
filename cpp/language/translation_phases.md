---
title: Phases of translation
type: Language
source: https://en.cppreference.com/w/cpp/language/translation_phases
---


# Phases of translation

C++ source files are processed by the compiler to produce C++ programs.

## Translation process

The text of a C++ program is kept in units called ''source files''.
C++ source files undergo ''translation'' to become a ''translation unit'', consisting of the following steps:
# Maps each source file to a character sequence.
# Converts each character sequence to a preprocessing token sequence, separated by whitespace.
# Converts each preprocessing token to a token, forming a token sequence.
# Converts each token sequence to a translation unit.
A C++ program can be formed from translated translation units. Translation units can be separately translated and then later linked to produce an executable program.
The process above can be organized into 9 translation phases.

## Preprocessing tokens

A ''preprocessing token'' is the minimal lexical element of the language in translation phases 3 through 6.
The categories of preprocessing token are:
* header names (such as `<iostream>` or `"myfile.h"`)
rrev|since=c++20|
* placeholder tokens produced by preprocessing ``import` and `module` directives` (i.e. `import XXX;` and `module XXX;`)
* `identifiers`
* preprocessing numbers (see below)
* `character literal`s<sup>(since C++11)</sup> , including `user-defined character literals`
* `string literal`s<sup>(since C++11)</sup> , including `user-defined string literals`
* `operators and punctuators`, including `alternative tokens`
* individual non-whitespace characters that do not fit in any other category
: The program is ill-formed if the character matching this category is
:* apostrophe (`'`, U+0027),
:* quotation mark (`"`, U+0022), or
:* a character not in the `basic character set`.

### Preprocessing numbers

The set of preprocessing tokens of preprocessing number is a superset of the union of the sets of tokens of `integer literal`s and `floating-point literals`:

**Syntax:**

- `sdsc|`
- `**`.`** *digit* *pp-continue-seq* (optional)`

### Parameters

- `{{spar` - digit|one of digits 0-9
- `{{spar` - pp-continue-seq|a sequence of pp-continues
Each *pp-continue* is one of the following:

**Syntax:**

- `sdsc|num=1|`
- `*identifier-continue*`
- `sdsc|num=2|`
- `*exp-char* *sign-char*`
- `sdsc|num=3|`
- `**`.`**`
- `|`
- `**`’`** *digit*`
- `|`
- `**`’`** *nondigit*`

### Parameters

- `{{spar` - identifier-continue|any non-first character of a valid `identifier`
- `{{spar` - exp-char|one of<sup>(since C++11)</sup>  **`P`**, **`p`**, **`E`** and **`e`**
- `{{spar` - sign-char|one of **`+`** and **`-`**
- `{{spar` - digit|one of digits 0-9
- `{{spar` - nondigit|one of Latin letters A/a-Z/z and underscore
A preprocessing number does not have a type or a value; it acquires both after a successful conversion an integer/floating-point literal token.

### Whitespace

''Whitespace'' consists of comments, whitespace characters, or both.
The following characters are whitespace characters:
* character tabulation (U+0009)
* line feed / new-line character (U+000A)
* line tabulation (U+000B)
* form feed (U+000C)
* space (U+0020)
Whitespace is usually used to separate preprocessing tokens, with the following exceptions:
* It is not a separator in header name, character literal and string literal.
* Preprocessing tokens separated by whitespace containing new-line characters cannot form preprocessing directives.

```cpp
#include "my header"        // OK, using a header name containing whitespace

#include/*hello*/<iostream> // OK, using a comment as whitespace

#include
<iostream> // Error: #include cannot span across multiple lines

"str ing"  // OK, a single preprocessing token (string literal)
' '        // OK, a single preprocessing token (character literal)
```


### Maximal munch

If the input has been parsed into preprocessing tokens up to a given character, the next preprocessing token is generally taken to be the longest sequence of characters that could constitute a preprocessing token, even if that would cause subsequent analysis to fail. This is commonly known as ''maximal munch''.

```cpp
int foo = 1;
int bar = 0xE+foo;   // Error: invalid preprocessing number 0xE+foo
int baz = 0xE + foo; // OK
```

In other words, the maximal munch rule is in favor of :

```cpp
int foo = 1;
int bar = 2;

int num1 = foo+++++bar; // Error: treated as “foo++ ++ +baz”, not “foo++ + ++baz”
int num2 = -----foo;    // Error: treated as “-- -- -foo”, not “- -- --foo”
```

The maximal munch rule has the following exceptions:
* Header name preprocessing tokens are only formed in the following cases:
:* after the `include` preprocessing token in an `#include` directive
rev|since=c++17|
:* in a `cpp/preprocessor/include|__has_include` expression
rev|since=c++20|
:* after the `import` preprocessing token in an `import` directive

```cpp
std::vector<int> x; // OK, “int” is not a header name
```

* If the next three characters are `<::` and the subsequent character is neither `:` nor `>`, the `<` is treated as a preprocessing token by itself instead of the first character of the `alternative token` `<:`.

```cpp
struct Foo { static const int v = 1; };
std::vector<::Foo> x;  // OK, <: not taken as the alternative token for [
extern int y<::>;      // OK, same as “extern int y[];”
int z<:::Foo::value:>; // OK, same as “int z[::Foo::value];”
```

rrev|since=c++11|
* If the next two characters are `>>` and one of the `>` character can complete a `template identifier`, the character is treated as a preprocessing token alone instead of being part of the preprocessing token `>>`.

```cpp
template<int i> class X { /* ... */ };
template<class T> class Y { /* ... */ };

Y<X<1>> x3;      // OK, declares a variable “x3” of type “Y<X<1> >”
Y<X<6>>1>> x4;   // Syntax error
Y<X<(6>>1)>> x5; // OK
```

* If the next character begins a sequence of characters that could be the prefix and initial double quote of a `raw string literal`, the next preprocessing token is a raw string literal. The literal consists of the shortest sequence of characters that matches the raw-string pattern.

```cpp
#define R "x"
const char* s = R"y";         // ill-formed raw string literal, not "x" "y"
const char* s2 = R"(a)" "b)"; // a raw string literal followed by a normal string literal
```


## Tokens

A ''token'' is the minimal lexical element of the language in translation phase 7.
The categories of token are:
* `identifiers`
* s
*
* `operators and punctuators` (except preprocessing operators)

## Translation phases

Translation is performed `as if` in the order from phase 1 to phase 9. Implementations behave as if these separate phases occur, although in practice different phases can be folded together.

### Phase 1: Mapping source characters

rev|until=c++23|
1. The individual bytes of the source code file are mapped (in implementation-defined manner) to the characters of the `basic source character set`. In particular, OS-dependent end-of-line indicators are replaced by newline characters.
2. <sup>(since C++11)</sup> The set of source file characters accepted is implementation-defined. Any source file character that cannot be mapped to a character in the `basic source character set` is replaced by its `universal character name` (escaped with `\u` or `\U`) or by some implementation-defined form that is handled equivalently.
rrev|until=c++17|
3. `Trigraph sequences` are replaced by corresponding single-character representations.
rev|since=c++23|
Input files that are a sequence of UTF-8 code units (UTF-8 files) are guaranteed to be supported. The set of other supported kinds of input files is implementation-defined. If the set is non-empty, the kind of an input file is determined in an implementation-defined manner that includes a means of designating input files as UTF-8 files, independent of their content (recognizing the byte order mark is not sufficient).
* If an input file is determined to be a UTF-8 file, then it shall be a well-formed UTF-8 code unit sequence and it is decoded to produce a sequence of Unicode scalar values. A sequence of `translation character set` elements is then formed by mapping each Unicode scalar value to the corresponding translation character set element. In the resulting sequence, each pair of characters in the input sequence consisting of carriage return (U+000D) followed by line feed (U+000A), as well as each carriage return (U+000D) not immediately followed by a line feed (U+000A), is replaced by a single new-line character.
* For any other kind of input file supported by the implementation, characters are mapped (in implementation-defined manner) to a sequence of translation character set elements. In particular, OS-dependent end-of-line indicators are replaced by new-line characters.

### Phase 2: Splicing lines

1. <sup>(since C++23)</sup> If the first translation character is byte order mark (U+FEFF), it is deleted. Whenever backslash (`\`) appears at the end of a line (immediately followed by <sup>(since C++23)</sup> zero or more whitespace characters other than new-line followed by the newline character), these characters are deleted, combining two physical source lines into one logical source line. This is a single-pass operation; a line ending in two backslashes followed by an empty line does not combine three lines into one.
2. If a non-empty source file does not end with a newline character after this step (end-of-line backslashes are no longer splices at this point), a terminating newline character is added.

### Phase 3: Lexing

1. The source file is decomposed into preprocessing tokens and whitespace:

```cpp
// The following #include directive can de decomposed into 5 preprocessing tokens:

//     punctuators (#, < and >)
//          │
// ┌────────┼────────┐
// │        │        │
   #include <iostream>
//     │        │
//     │        └── header name (iostream)
//     │
//     └─────────── identifier (include)
```

@@ If a source file ends in a partial preprocessing token or in a partial comment, the program is ill-formed:

```cpp
// Error: partial string literal
"abc
```


```cpp
// Error: partial comment
/* comment
```

rrev|since=c++23|
@@ As characters from the source file are consumed to form the next preprocessing token (i.e., not being consumed as part of a comment or other forms of whitespace), universal character names are recognized and replaced by the designated element of the , except when matching a character sequence in one of the following preprocessing tokens:
:* a character literal (*c-char-sequence*)
:* a string literal (*s-char-sequence* and *r-char-sequence*), excluding delimiters (*d-char-sequence*)
:* a header name (*h-char-sequence* and *q-char-sequence*)
rrev|since=c++11|
2. Any transformations performed during<sup>(until C++23)</sup>  phase 1 and phase 2 between the initial and the final double quote of any `raw string literal` are reverted.
3. Whitespace is transformed:
* Each comment is replaced by one space character.
* New-line characters are retained.
* Whether each nonempty sequence of whitespace characters other than new-line is retained or replaced by one space character is unspecified.

### Phase 4: Preprocessing

1. The  is executed.
2. Each file introduced with the `#include` directive goes through phases 1 through 4, recursively.
3. At the end of this phase, all preprocessor directives are removed from the source.

### Phase 5: Determining common string literal encodings

rev|until=c++23|
1. All characters in `character literal`s and `string literal`s are converted from the source character set to the `encoding|literal encoding` (which may be a multibyte character encoding such as UTF-8, as long as the 96 characters of the `basic character set` have single-byte representations).
2. `Escape sequences` and universal character names in character literals and non-raw string literals are expanded and converted to the literal encoding.
If the character specified by a universal character name cannot be encoded as a single code point in the corresponding literal encoding, the result is implementation-defined, but is guaranteed not to be a null (wide) character.
rev|since=c++23|
For a sequence of two or more adjacent `string literal` tokens, a common encoding prefix is determined as described `here`. Each such string literal token is then considered to have that common encoding prefix.
(Character conversion is moved to phase 3)

### Phase 6: Concatenating string literals

Adjacent `string literals` are concatenated.

### Phase 7: Compiling

Compilation takes place: each preprocessing token is converted to a token. The tokens are syntactically and semantically analyzed and translated as a translation unit.

### Phase 8: Instantiating templates

Each translation unit is examined to produce a list of required template instantiations, including the ones requested by `explicit instantiations`. The definitions of the templates are located, and the required instantiations are performed to produce ''instantiation units''.

### Phase 9: Linking

Translation units, instantiation units, and library components needed to satisfy external references are collected into a program image which contains information needed for execution in its execution environment.

## Notes

Source files, translation units and translated translation units need not necessarily be stored as files, nor need there be any one-to-one correspondence between these entities and any external representation. The description is conceptual only, and does not specify any particular implementation.
rrev|until=c++23|
The conversion performed at phase 5 can be controlled by command line options in some implementations: gcc and clang use `-finput-charset` to specify the encoding of the source character set, `-fexec-charset` and `-fwide-exec-charset` to specify the ordinary and wide literal encodings respectively, while Visual Studio 2015 Update 2 and later uses `/source-charset` and `/execution-charset` to specify the source character set and literal encoding respectively.
Some compilers do not implement instantiation units (also known as [https://docs.oracle.com/cd/E18659_01/html/821-1383/bkagr.html#scrolltoc template repositories] or [http://www-01.ibm.com/support/knowledgecenter/SSXVZZ_12.1.0/com.ibm.xlcpp121.linux.doc/compiler_ref/fcat_template.html?lang=en template registries]) and simply compile each template instantiation at phase 7, storing the code in the object file where it is implicitly or explicitly requested, and then the linker collapses these compiled instantiations into one at phase 9.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-787 | C++98 | the behavior was undefined if a non-empty source file does<br>not end with a newline character at the end of phase 2 | add a terminating newline<br>character in this case |
| cwg-1775 | C++11 | forming a universal character name inside a raw<br>string literal in phase 2 resulted in undefined behavior | made well-defined |
| cwg-2747 | C++98 | phase 2 checked the end-of-file splice after splicing, this is unnecessary | removed the check |


## References


## See also

