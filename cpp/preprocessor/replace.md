---
title: #define directive
type: Language
source: https://en.cppreference.com/w/cpp/preprocessor/replace
---


# Replacing text macros

The preprocessor supports text macro replacement. Function-like text macro replacement is also supported.

## Syntax


**Syntax:**

- `*identifier replacement-list* (optional)`
- `identifier**`(`**parameters**`)`** *replacement-list* (optional)`
- `identifier**`(`**parameters**`, ...)`** *replacement-list* (optional)|notes = <sup>(C++11)</sup>`
- `identifier**`(...)`** *replacement-list* (optional)|notes = <sup>(C++11)</sup>`
- `*identifier*`

## Explanation


### `#define` directives

The `#define` directives define the *identifier* as macro, that is instruct the compiler to replace most successive occurrences of *identifier* with *replacement-list*, which will be additionally processed. Exceptions arise from the rules of `scanning and replacement`.
If *identifier* is already defined as a macro by another `#defined` directive, the program is ill-formed unless the definitions are identical.
If *identifier* is a predefined macro name (see below) or the identifier `defined`, <sup>(until C++26)</sup> the behavior is undefined<sup>(since C++26)</sup> the program is ill-formed.

#### Object-like macros

Object-like macros replace every occurrence of defined *identifier* with *replacement-list*. Version (1) of the `#define` directive behaves exactly like that.

#### Function-like macros

Function-like macros replace each occurrence of defined *identifier* with *replacement-list*, additionally taking a number of comma-separated arguments, which then replace corresponding occurrences of any of the *parameters* in the *replacement-list*. If arguments contain a preprocessing directive, <sup>(until C++26)</sup> the behavior is undefined<sup>(since C++26)</sup> the program is ill-formed.
The syntax of a function-like macro invocation is similar to the syntax of a function call: each instance of the macro name followed by a `(` as the next preprocessing token introduces the sequence of preprocessing tokens that is replaced by the *replacement-list*. The sequence is terminated by the matching `)` preprocessing token, skipping intervening matched pairs of left and right parentheses.
For version (2), the number of arguments must be the same as the number of parameters in macro definition. For versions (3,4), the number of arguments must not be less than the number of parameters (<sup>(since C++20)</sup> not counting **`...`**). Otherwise the program is ill-formed. If the identifier is not in functional-notation, i.e. does not have parentheses after itself, it is not replaced at all.
Version (2) of the `#define` directive defines a simple function-like macro.
Version (3) of the `#define` directive defines a function-like macro with variable number of arguments. The additional arguments (called ''variable arguments'') can be accessed using `__VA_ARGS__` identifier, which is then replaced with arguments, supplied with the identifier to be replaced.
Version (4) of the `#define` directive defines a function-like macro with variable number of arguments, but no regular arguments. The arguments (called ''variable arguments'') can be accessed only with `__VA_ARGS__` identifier, which is then replaced with arguments, supplied with the identifier to be replaced.
rrev|since=c++20|
For versions (3,4), *replacement-list* may contain the token sequence **`__VA_OPT__(`**content**`)`**, which is replaced by *content* if `__VA_ARGS__` is non-empty, and expands to nothing otherwise.

```cpp
#define F(...) f(0 __VA_OPT__(,) __VA_ARGS__)
F(a, b, c) // replaced by f(0, a, b, c)
F()        // replaced by f(0)

#define G(X, ...) f(0, X __VA_OPT__(,) __VA_ARGS__)
G(a, b, c) // replaced by f(0, a, b, c)
G(a, )     // replaced by f(0, a)
G(a)       // replaced by f(0, a)

#define SDEF(sname, ...) S sname __VA_OPT__(= { __VA_ARGS__ })
SDEF(foo);       // replaced by S foo;
SDEF(bar, 1, 2); // replaced by S bar = { 1, 2 };
```

Note: if an argument of a function-like macro includes commas that are not protected by matched pairs of left and right parentheses (most commonly found in template argument lists, as in `assert(std::is_same_v<int, int>);` or `BOOST_FOREACH(std::pair<int, int> p, m)`), the comma is interpreted as macro argument separator, causing a compilation failure due to argument count mismatch.

#### Scanning and Replacement

* Scanning keeps track of macros they replaced. If scan finds text matching such macro, it marks it "to be ignored" (all scans will ignore it). This prevents recursion.
* If scanning found function-like macro, arguments are scanned before put inside *replacement-list*. Except `#` and `##` operators take argument without scan.
* After macro was replaced, result text is scanned.
Note, it is possible to define pseudo recursive macro:

### Example


**Output:**
```
EXAMPLE_ ()(5 -1) (5)
EXAMPLE_ ()(5 -1 -1) (5 -1) (5)
```


### Reserved macro names

A translation unit that includes a standard library header may not `#define` or `#undef` names declared in any standard library header.
A translation unit that uses any part of the standard library is not allowed to `#define` or `#undef` names lexically identical to:
* keywords
rrev|since=c++11|
* identifiers with special meaning
* any standard attribute token<sup>(since C++20)</sup> , except that `cpp/language/attributes/likely` and `cpp/language/attributes/likely|unlikely` may be defined as function-like macros
Otherwise, the behavior is undefined.

### `#` and `##` operators

In function-like macros, a `#` operator before an identifier in the *replacement-list* runs the identifier through parameter replacement and encloses the result in quotes, effectively creating a string literal without any prefix.
Let the ''stringizing argument'' be the preprocessing token sequence expanded from the identifier. If the stringizing argument is empty, the result is an empty string literal. Otherwise:
* Whitespace before the first preprocessing token and after the last preprocessing token comprising the stringizing argument is deleted.
* Each occurrence of whitespace between the stringizing argument’s preprocessing tokens becomes a single space character in the character string literal.
* The original spelling of each preprocessing token in the stringizing argument is retained in the character string literal, except that when handling header names, character literals and string literals:
** A backslash character `\` is inserted before each existing `"` and `\` characters.
** Each new-line character is replaced by the two-character sequence `\n`.
If the result is not a valid string literal, <sup>(until C++26)</sup> the behavior is undefined<sup>(since C++26)</sup> the program is ill-formed.
rrev|since=c++11|
When `#` appears before `__VA_ARGS__`, the entire expanded `__VA_ARGS__` is enclosed in quotes:

```cpp
#define showlist(...) puts(#__VA_ARGS__)
showlist();            // expands to puts("")
showlist(1, "x", int); // expands to puts("1, \"x\", int")
```

A `##` operator between any two successive identifiers in the *replacement-list* runs parameter replacement on the two identifiers (which are not macro-expanded first) and then concatenates the result.
Concatenation can result in new preprocessing tokens: forming a longer identifier from short identifiers, forming a number from digits, or forming the operator `1=+=` from operators `+` and `1==`. A comment cannot be formed by concatenating `/` and `*`, because comments are removed from text before macro substitution is considered.
If the result of concatenation is not a valid preprocessing token, <sup>(until C++26)</sup> the behavior is undefined<sup>(since C++26)</sup> the program is ill-formed.

### `#undef` directive

The `#undef` directive undefines the *identifier*, that is cancels previous definition of the *identifier* by `#define` directive. If the identifier does not have associated macro, the directive is ignored.
If *identifier* is a predefined macro name (see below) or the identifier `defined`, <sup>(until C++26)</sup> the behavior is undefined<sup>(since C++26)</sup> the program is ill-formed.

## Predefined macros

The following macro names are predefined in every translation unit:


| dsc macro const|__cplusplus|nolink=true|denotes the version of C++ standard that is being used, expands to value | |
| * `199711L`<sup>(until C++11)</sup>, | |
| * `201103L`, | |
| * `201402L`, | |
| * `201703L`, | |
| * `202002L`, | |
| * `202302L`, or | |
| * `202603L` | |

The following additional macro names may be predefined by the implementations:
The values of these macros (except for `__FILE__` and `__LINE__`) remain constant throughout the translation unit. Attempts to redefine or undefine these macros result in undefined behavior.
rrev|since=c++20|

### Language feature-testing macros

The standard defines a set of preprocessor macros corresponding to C++ language features introduced in C++11 or later. They are intended as a simple and portable way to detect the presence of said features.
See Feature testing for details.

## Notes

Some compilers offer an extension that allows `##` to appear after a comma and before `__VA_ARGS__`, in which case the `##` does nothing when the variable arguments are present, but removes the comma when the variable arguments are not present: this makes it possible to define macros such as `fprintf (stderr, format, ##__VA_ARGS__)`. <sup>(since C++20)</sup> This can also be achieved in a standard manner using `__VA_OPT__`, such as `fprintf (stderr, format __VA_OPT__(, ) __VA_ARGS__)`.
rrev|since=c++11|
The function-local predefined variable `__func__` is not a predefined macro, but it is usually used together with `__FILE__` and `__LINE__`, e.g. by `assert`.

## Example


### Example


**Output:**
```
abcd: 12
fff: 2
qqq: 23
34
output: million
Hello World
Hello WORD World
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-294 | C++98 | a translation unit that includes a standard library header could contain<br>macros that define names declared in other standard library headers | prohibited |


## See also

