---
title: #include directive
type: Language
source: https://en.cppreference.com/w/cpp/preprocessor/include
---


# Source file inclusion

Includes other source file into current source file at the line immediately after the directive.

## Syntax


**Syntax:**

- `*h-char-sequence* **`&gt;`** *new-line*`
- `*q-char-sequence* **`"`** *new-line*`
- `*pp-tokens* *new-line*`
- `|**`__has_include`** **`(`** **`"`** *q-char-sequence* **`"`** **`)`**<br>**`__has_include`** **`(`** **`&lt;`** *h-char-sequence* **`&gt;`** **`)`**`
- `|**`__has_include`** **`(`** *string-literal* **`)`**<br>**`__has_include`** **`(`** **`&lt;`** *h-pp-tokens* **`&gt;`** **`)`**`
1. Searches for a header identified uniquely by *h-char-sequence* and replaces the directive by the entire contents of the header.
2. Searches for a source file identified by *q-char-sequence* and replaces the directive by the entire contents of the source file. It may fallback to  and treat *q-char-sequence* as a header identifier.
3. If neither  nor  is matched, *pp-tokens* will undergo macro replacement. The directive after replacement will be tried to match with  or  again.
4. Checks whether a header or source file is available for inclusion.
5. If  is not matched, *h-pp-tokens* will undergo macro replacement. The directive after replacement will be tried to match with  again.

### Parameters

- `{{spar` - new-line|The new-line character
- `{{spar` - h-char-sequence|A sequence of one or more h-chars, where the appearance of any of the following is conditionally-supported with implementation-defined semantics:
- * the character `'`
- * the character `"`
- * the character `\`
- * the character sequence `//`
- * the character sequence `/*`
- `{{spar` - h-char|Any member of the <sup>(until C++23)</sup> source character set<sup>(since C++23)</sup> translation character set except new-line and `>`
- `{{spar` - q-char-sequence|A sequence of one or more q-chars, where the appearance of any of the following is conditionally-supported with implementation-defined semantics:
- * the character `'`
- * the character `\`
- * the character sequence `//`
- * the character sequence `/*`
- `{{spar` - q-char|Any member of the <sup>(until C++23)</sup> source character set<sup>(since C++23)</sup> translation character set except new-line and `"`
- `{{spar` - pp-tokens|A sequence of one or more 
- `{{spar` - string-literal|A string literal
- `{{spar` - h-pp-tokens|A sequence of one or more  except `>`

## Explanation

1. Searches a sequence of places for a header identified uniquely by h-char-sequence, and causes the replacement of that directive by the entire contents of the header. How the places are specified or the header identified is implementation-defined.
2. Causes the replacement of that directive by the entire contents of the source file identified by q-char-sequence. The named source file is searched for in an implementation-defined manner.
@@ If this search is not supported, or if the search fails, the directive is reprocessed as if it reads syntax  with the identical contained sequence (including `>` characters, if any) from the original directive.
3. The preprocessing tokens after **`include`** in the directive are processed just as in normal text (i.e., each identifier currently defined as a macro name is replaced by its replacement list of preprocessing tokens).
@@ If the directive resulting after all replacements does not match one of the two previous forms, <sup>(until C++26)</sup> the behavior is undefined<sup>(since C++26)</sup> the program is ill-formed, no diagnostic required.
@@ The method by which a sequence of preprocessing tokens between a `<` and a `>` preprocessing token pair or a pair of `"` characters is combined into a single header name preprocessing token is implementation-defined.
4. The header or source file identified by *h-char-sequence* or *q-char-sequence* is searched for as if that preprocessing token sequence were the *pp-tokens* in syntax , except that no further macro expansion is performed.
* If such a directive would not satisfy the syntactic requirements of an `#include` directive, the program is ill-formed.
* Otherwise, the `__has_include` expression evaluates to `1` if the search for the source file succeeds, and to `0` if the search fails.
5. This form is considered only if syntax  does not match, in which case the preprocessing tokens are processed just as in normal text.
rrev|since=c++20|
If the header identified by the *header-name* (i.e., **`&lt;`** *h-char-sequence* **`&gt;`** or **`"`** *q-char-sequence* **`"`**) denotes an importable header, it is implementation-defined whether the `#include` preprocessing directive is instead replaced by an import directive of the form
**`import`** *header-name* **`;`** *new-line*
`__has_include` can be expanded in the expression of `cpp/preprocessor/conditional|#if` and `cpp/preprocessor/conditional|#elif`. It is treated as a defined macro by `cpp/preprocessor/conditional|#ifdef`, `cpp/preprocessor/conditional|#ifndef`<sup>(since C++23)</sup> , `cpp/preprocessor/conditional|#elifdef`, `cpp/preprocessor/conditional|#elifndef` and `cpp/preprocessor/conditional|defined` but cannot be used anywhere else.

## Notes

Typical implementations search only standard include directories for syntax . The standard C++ library and the standard C library are implicitly included in these standard include directories. The standard include directories usually can be controlled by the user through compiler options.
The intent of syntax  is to search for the files that are not controlled by the implementation. Typical implementations first search the directory where the current file resides then falls back to .
When a file is included, it is processed by translation phases 1-4, which may include, recursively, expansion of the nested `#include` directives, up to an implementation-defined nesting limit. To avoid repeated inclusion of the same file and endless recursion when a file includes itself, perhaps transitively, ''header guards'' are commonly used: the entire header is wrapped in

```cpp
#ifndef FOO_H_INCLUDED /* any name uniquely mapped to file name */
#define FOO_H_INCLUDED
// contents of the file are here
#endif
```

Many compilers also implement the non-standard `cpp/preprocessor/impl|pragma` `#pragma once` with similar effects: it disables processing of a file if the same file (where file identity is determined in OS-specific way) has already been included.
A sequence of characters that resembles an escape sequence in *q-char-sequence* or *h-char-sequence* might result in an error, be interpreted as the character corresponding to the escape sequence, or have a completely different meaning, depending on the implementation.
A `__has_include` result of `1` only means that a header or source file with the specified name exists. It does not mean that the header or source file, when included, would not cause an error or would contain anything useful. For example, on a C++ implementation that supports both C++14 and C++17 modes (and provides `__has_include` in its C++14 mode as a conforming extension), `__has_include(<optional>)` may be `1` in C++14 mode, but actually `#include <optional>` may cause an error.

## Example


### Example


**Output:**
```
<optional> is present
op = -1
op = 42
```


## Defect reports


## See also

* Resource inclusion <sup>(C++26)</sup>
