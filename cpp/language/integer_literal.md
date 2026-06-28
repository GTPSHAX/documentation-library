---
title: Integer literal
type: Language
source: https://en.cppreference.com/w/cpp/language/integer_literal
---


# Integer literal

Allows values of integer type to be used in expressions directly.

## Syntax

An integer literal has the form

**Syntax:**

- `*integer-suffix* (optional)`
- `*integer-suffix* (optional)`
- `*integer-suffix* (optional)`
- `|*binary-literal* *integer-suffix* (optional)`
where
* *decimal-literal* is a non-zero decimal digit (`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`), followed by zero or more decimal digits (`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`)
* *octal-literal* is the digit zero (`0`) followed by zero or more octal digits (`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`)
* *hex-literal* is the character sequence `0x` or the character sequence `0X` followed by one or more hexadecimal digits (`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `a`, `A`, `b`, `B`, `c`, `C`, `d`, `D`, `e`, `E`, `f`, `F`)
* *binary-literal* is the character sequence `0b` or the character sequence `0B` followed by one or more binary digits (`0`, `1`)
* *integer-suffix*, if provided, may contain one or both of the following (if both are provided, they may appear in any order:
:* *unsigned-suffix* (the character `u` or the character `U`)
:* one of
::* *long-suffix* (the character `l` or the character `L`)
rrev|since=c++11|
::* *long-long-suffix* (the character sequence `ll` or the character sequence `LL`)
rrev|since=c++23|
::* *size-suffix* (the character `z` or the character `Z`)
rrev|since=c++14|
Optional single quotes (`'`) may be inserted between the digits as a separator; they are ignored when determining the value of the literal.
An integer literal (as any literal) is a `primary expression`.

## Explanation

1. Decimal integer literal (base 10).
2. Octal integer literal (base 8).
3. Hexadecimal integer literal (base 16, the letters `'a'` through `'f'` represent values (decimal) 10 through 15).
4. Binary integer literal (base 2).
The first digit of an integer literal is the most significant.
Example. The following variables are initialized to the same value:

```cpp
int d = 42;
int o = 052;
int x = 0x2a;
int X = 0X2A;
int b = 0b101010; // C++14
```

Example. The following variables are also initialized to the same value:

```cpp
unsigned long long l1 = 18446744073709550592ull;       // C++11
unsigned long long l2 = 18'446'744'073'709'550'592llu; // C++14
unsigned long long l3 = 1844'6744'0737'0955'0592uLL;   // C++14
unsigned long long l4 = 184467'440737'0'95505'92LLU;   // C++14
```


## The type of the literal

The type of the integer literal is the first type in which the value can fit, from the list of types which depends on which numeric base and which *integer-suffix* was used:


| -style="text-align:center" |
| Suffix |
| Decimal bases |
| Binary, octal, or hexadecimal bases |
| -style="text-align:left" |
| (no suffix) |
|  |
|  |
| - |
| tt | u or tt | U |
|  |
|  |
| - |
| tt | l or tt | L |
|  |
|  |
| - |
| both tt | l/tt | L<br>and tt | u/tt | U |
|  |
|  |
| - |
| tt | ll or tt | LL |
|  |
|  |
| - |
| both tt | ll/tt | LL<br>and tt | u/tt | U |
|  |
|  |
| - |
| tt | z or tt | Z |
|  |
|  |
| - |
| both tt | z/tt | Z<br>and tt | u/tt | U |
|  |
|  |

If the value of the integer literal <sup>(since C++23)</sup> that does not have *size-suffix* is too big to fit in any of the types allowed by suffix/base combination and the compiler supports an extended integer type (such as `__int128`) which can represent the value of the literal, the literal may be given that extended integer type, otherwise the program is ill-formed.

## Notes

Letters in the integer literals are case-insensitive: `0xDeAdBeEfU` and `0XdeadBEEFu` represent the same number <sup>(since C++11)</sup> (one exception is the *long-long-suffix, which is either `ll` or `LL`, never `lL` or `Ll`)*.
There are no negative integer literals. Expressions such as `-1` apply the `unary minus operator` to the value represented by the literal, which may involve implicit type conversions.
In C prior to C99 (but not in C++), unsuffixed decimal values that do not fit in `long int` are allowed to have the type `unsigned long int`.
rrev|since=c++11|
When used in a controlling expression of `cpp/preprocessor/conditional|#if` or `cpp/preprocessor/conditional|#elif`, all signed integer constants act as if they have type `std::intmax_t` and all unsigned integer constants act as if they have type `std::uintmax_t`.
Due to `maximal munch`, hexadecimal integer literals ending in **`e`** and **`E`**, when followed by the operators **`+`** or **`-`**, must be separated from the operator with whitespace or parentheses in the source:

```cpp
auto x = 0xE+2.0;   // error
auto y = 0xa+2.0;   // OK
auto z = 0xE +2.0;  // OK
auto q = (0xE)+2.0; // OK
```

Otherwise, a single invalid preprocessing number token is formed, which causes further analysis to fail.

## Example


### Example


**Output:**
```
123
83
291
2
12345678901234567890
12345678901234567890
9223372036854775808
-9223372036854775808
```


## Defect reports


## References

<!--
This is the source for the claim "An integer literal (as any literal) is a primary expression. "
It could be added here, but it should probably be added to the expressions page instead-->
<!--
-->

## See also


| cpp/language/dsc user literal | (see dedicated page) |

