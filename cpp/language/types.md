---
title: Fundamental types
type: Language
source: https://en.cppreference.com/w/cpp/language/types
---


# Fundamental types

The following types are collectively called ''fundamental types'':
* (possibly cv-qualified) `void`
rrev|since=c++11|
* (possibly cv-qualified) `std::nullptr_t`
* integral types
* floating-point types

## `void`

:**`void`** — type with an empty set of values. It is an `incomplete type` that cannot be completed (consequently, objects of type `void` are disallowed). There are no `array`s of `void`, nor `reference`s to `void`. However, `pointers to `void`` and `function`s returning type `void` (''procedures'' in other languages) are permitted.
<sup>(since C++11)</sup> anchor|nullptr_t

## `std::nullptr_t`

`std::nullptr_t` names the type of the null pointer literal, `nullptr`. It is a distinct type that is not itself a pointer type or a pointer to member type. All its prvalues are `null pointer constants`. `sizeof(std::nullptr_t)` is equal to `sizeof(void*)`.
The name `std::nullptr_t` is declared in .
rrev|since=c++26|

## `std::meta::info`

`std::meta::info` names the type of reflection values. There exists a unique ''null reflection''. Every other reflection represents a language construct.
The name `std::meta::info` is declared in .

## Integral types


### Standard integer types

:**`int`** — basic integer type. The keyword `int` may be omitted if any of the modifiers listed below are used. If no length modifiers are present, it's guaranteed to have a width of at least 16 bits. However, on 32/64 bit systems it is almost exclusively guaranteed to have width of at least 32 bits (see below).

#### Modifiers

Modifies the basic integer type. Can be mixed in any order. Only one of each group can be present in type name.
* Signedness:
:**`signed`** — target type will have signed representation (this is the default if omitted)
:**`unsigned`** — target type will have unsigned representation
* Size:
:**`short`** — target type will be optimized for space and will have width of at least 16 bits.
:**`long`** — target type will have width of at least 32 bits.
rrev|since=c++11|
:**`long long`** — target type will have width of at least 64 bits.
Note: as with all type specifiers, any order is permitted: `unsigned long long int` and `long int unsigned long` name the same type.

#### Properties

The following table summarizes all available standard integer types and their properties in various common data models:


| - |
| rowspan="2" | Type specifier |
| rowspan="2" | Equivalent type |
| colspan="5" | Width in bits by [[#Data models | data model]] |
| - |
| C++ standard |
| LP32 |
| ILP32 |
| LLP64 |
| LP64 |
| - |
| left | c/core | signed char |
| c/core | signed char |
| rowspan="2" | at least<br> '''8''' |
| rowspan="2" | '''8''' |
| rowspan="2" | '''8''' |
| rowspan="2" | '''8''' |
| rowspan="2" | '''8''' |
| - |
| left | c/core | unsigned char |
| c/core | unsigned char |
| - |
| left | c/core | short |
| rowspan="4" | c/core | short int |
| rowspan="6" | at least<br> '''16''' |
| rowspan="6" | '''16''' |
| rowspan="6" | '''16''' |
| rowspan="6" | '''16''' |
| rowspan="6" | '''16''' |
| - |
| left | c/core | short int |
| - |
| left | c/core | signed short |
| - |
| left | c/core | signed short int |
| - |
| left | c/core | unsigned short |
| rowspan="2" | c/core | unsigned short int |
| - |
| left | c/core | unsigned short int |
| - |
| left | c/core | int |
| rowspan="3" | c/core | int |
| rowspan="5" | at least<br> '''16''' |
| rowspan="5" | '''16''' |
| rowspan="5" | '''32''' |
| rowspan="5" | '''32''' |
| rowspan="5" | '''32''' |
| - |
| left | c/core | signed |
| - |
| left | c/core | signed int |
| - |
| left | c/core | unsigned |
| rowspan="2" | c/core | unsigned int |
| - |
| left | c/core | unsigned int |
| - |
| left | c/core | long |
| rowspan="4" | c/core | long int |
| rowspan="6" | at least<br> '''32''' |
| rowspan="6" | '''32''' |
| rowspan="6" | '''32''' |
| rowspan="6" | '''32''' |
| rowspan="6" | '''64''' |
| - |
| left | c/core | long int |
| - |
| left | c/core | signed long |
| - |
| left | c/core | signed long int |
| - |
| left | c/core | unsigned long |
| rowspan="2" | c/core | unsigned long int |
| - |
| left | c/core | unsigned long int |
| - |
| left | c/core | long long |
| rowspan="4" | c/core | long long int<br> |
| rowspan="6" | at least<br> '''64''' |
| rowspan="6" | '''64''' |
| rowspan="6" | '''64''' |
| rowspan="6" | '''64''' |
| rowspan="6" | '''64''' |
| - |
| left | c/core | long long int |
| - |
| left | c/core | signed long long |
| - |
| left | c/core | signed long long int |
| - |
| left | c/core | unsigned long long |
| rowspan="2" | c/core | unsigned long long int<br> |
| - |
| left | c/core | unsigned long long int |

Note: integer arithmetic is defined differently for the signed and unsigned integer types. See `arithmetic operators`, in particular  `integer overflows`.
`std::size_t` is the unsigned integer type of the result of the `sizeof` operator<sup>(since C++11)</sup>  as well as the `alignof` operator.
rrev|since=c++11|

### Extended integer types

The extended integer types are implementation-defined. Note that fixed width integer types are typically aliases of the standard integer types.

### Boolean type

:**`bool`** — integer type, capable of holding one of the two values: `true` or `false`. The value of `sizeof(bool)` is implementation defined and might differ from `1`.

### Character types

Character types are integer types used for a character representation.
:**`signed char`** — type for signed character representation.
:**`unsigned char`** — type for unsigned character representation. Also used to inspect `object representations` (raw memory).
:**`char`** — type for character representation which can be most efficiently processed on the target system (has the same representation and alignment as either `signed char` or `unsigned char`, but is always a distinct type). Multibyte characters strings use this type to represent code units. <sup>(since C++11)</sup> For every value of type `unsigned char` in range  The signedness of `char` depends on the compiler and the target platform: the defaults for ARM and PowerPC are typically unsigned, the defaults for x86 and x64 are typically signed.
:**`wchar_t`** — type for wide character representation (see wide strings). It has the same size, signedness, and alignment as one of the integer types, but is a distinct type. In practice, it is 32 bits and holds UTF-32 on Linux and many other non-Windows systems, but 16 bits and holds UTF-16 code units on Windows. The standard used to require `wchar_t` to be large enough to represent any supported character code point. However, such requirement cannot be fulfilled on Windows, and thus it is considered as a defect and removed.
rrev|since=c++11|
:**`char16_t`** — type for UTF-16 character representation, required to be large enough to represent any UTF-16 code unit (16 bits). It has the same size, signedness, and alignment as `std::uint_least16_t`, but is a distinct type.
:**`char32_t`** — type for UTF-32 character representation, required to be large enough to represent any UTF-32 code unit (32 bits). It has the same size, signedness, and alignment as `std::uint_least32_t`, but is a distinct type.
<p>
rrev|since=c++20|
:**`char8_t`** — type for UTF-8 character representation, required to be large enough to represent any UTF-8 code unit (8 bits). It has the same size, signedness, and alignment as `unsigned char` (and therefore, the same size and alignment as `char` and `signed char`), but is a distinct type.
Besides the minimal bit counts, the C++ Standard guarantees that
:`1` == `sizeof(char)` &le; `sizeof(short)` &le; `sizeof(int)` &le; `sizeof(long)` &le; `sizeof(long long)`.
Note: this allows the extreme case in which [Byte|bytes](https://en.wikipedia.org/wiki/Byte|bytes) are sized 64 bits, all types (including `char`) are 64 bits wide, and `sizeof` returns `1` for every type.

## Floating-point types


### Standard floating-point types

The following three types and their cv-qualified versions are collectively called standard floating-point types.
:**`float`** — single precision floating-point type. Usually [Single-precision floating-point format|IEEE-754 binary32 format](https://en.wikipedia.org/wiki/Single-precision floating-point format|IEEE-754 binary32 format).
:**`double`** — double precision floating-point type. Usually [Double-precision floating-point format|IEEE-754 binary64 format](https://en.wikipedia.org/wiki/Double-precision floating-point format|IEEE-754 binary64 format).
:**`long double`** — extended precision floating-point type. Does not necessarily map to types mandated by IEEE-754.
:* [Quadruple-precision floating-point format|IEEE-754 binary128 format](https://en.wikipedia.org/wiki/Quadruple-precision floating-point format|IEEE-754 binary128 format) is used by some HP-UX, SPARC, MIPS, ARM64, and z/OS implementations.
:* The most well known [Extended precision|IEEE-754 binary64-extended format](https://en.wikipedia.org/wiki/Extended precision|IEEE-754 binary64-extended format) is [Extended precision#x86 extended precision format|x87 80-bit extended precision format](https://en.wikipedia.org/wiki/Extended precision#x86 extended precision format|x87 80-bit extended precision format). It is used by many x86 and x86-64 implementations (a notable exception is MSVC, which implements `long double` in the same format as `double`, i.e. binary64).
:* On PowerPC [Quadruple-precision floating-point format#Double-double arithmetic|double-double](https://en.wikipedia.org/wiki/Quadruple-precision floating-point format#Double-double arithmetic|double-double) can be used.
rrev|since=c++23|

### Extended floating-point types

The extended floating-point types are implementation-defined. They may include fixed width floating-point types.

### Properties

Floating-point types may support special values:
* ''infinity'' (positive and negative), see `INFINITY`
* the ''negative zero'', `-0.0`. It compares equal to the positive zero, but is meaningful in some arithmetic operations, e.g. `1=1.0 / 0.0 == INFINITY`, but `1=1.0 / -0.0 == -INFINITY`), and for some mathematical functions, e.g. `cpp/numeric/complex/sqrt|sqrt
* ''not-a-number'' (NaN), which does not compare equal with anything (including itself). Multiple bit patterns represent NaNs, see `std::nan`, `NAN`. Note that C++ takes no special notice of signalling NaNs other than detecting their support by `std::numeric_limits::has_signaling_NaN`, and treats all NaNs as quiet.
Floating-point numbers may be used with `arithmetic operators` `+`, `-`, `/`, and `*` as well as various mathematical functions from . Both built-in operators and library functions may raise floating-point exceptions and set `errno` as described in `cpp/numeric/math/math errhandling`.
Floating-point expressions may have greater range and precision than indicated by their types, see `FLT_EVAL_METHOD`. Floating-point expressions may also be ''contracted'', that is, calculated as if all intermediate values have infinite range and precision, see `cpp/preprocessor/impl##pragma STDC|#pragma STDC FP_CONTRACT`. Standard C++ does not restrict the accuracy of floating-point operations.
Some operations on floating-point numbers are affected by and modify the state of the floating-point environment (most notably, the rounding direction).
`Implicit conversions` are defined between floating types and integer types.
See  and `std::numeric_limits` for additional details, limits, and properties of the floating-point types.

## Range of values

The following table provides a reference for the limits of common numeric representations.
Prior to C++20, the C++ Standard allowed any signed integer representation, and the minimum guaranteed range of N-bit signed integers was from } to } (e.g. '''−127''' to '''127''' for a signed 8-bit type), which corresponds to the limits of [Ones' complement|ones' complement](https://en.wikipedia.org/wiki/Ones' complement|ones' complement) or [Signed number representations#Sign-and-magnitude method|sign-and-magnitude](https://en.wikipedia.org/wiki/Signed number representations#Sign-and-magnitude method|sign-and-magnitude).
However, all C++ compilers use [Two's complement|two's complement](https://en.wikipedia.org/wiki/Two's complement|two's complement) representation, and as of C++20, it is the only representation allowed by the standard, with the guaranteed range from } to } (e.g. '''−128''' to '''127''' for a signed 8-bit type).
8-bit ones' complement and sign-and-magnitude representations for `char` have been disallowed since C++11 (via the resolution of ), because a UTF-8 code unit of value 0x80 used in a `UTF-8 string literal` must be storable in a `char` type object.
The range for a floating-point type `T` is defined as follows:
* The minimum guaranteed range is the most negative finite floating-point number representable in `T` through the most positive finite floating-point number representable in `T`.
* If negative infinity is representable in `T`, the range of `T` is extended to all negative real numbers.
* If positive infinity is representable in `T`, the range of `T` is extended to all positive real numbers.
Since negative and positive infinity are representable in [https://www.iso.org/standard/80985.html ISO/IEC/IEEE 60559] formats, all real numbers lie within the range of representable values of a floating-point type adhering to ISO/IEC/IEEE 60559.
Note: actual (as opposed to guaranteed minimal) limits on the values representable by these types are available in C numeric limits interface and `std::numeric_limits`.

## Data models

The choices made by each implementation about the sizes of the fundamental types are collectively known as ''data model''. Four data models found wide acceptance:
32 bit systems:
:*'''LP32''' or '''2/4/4''' (`int` is 16-bit, `long` and pointer are 32-bit)
::* Win16 API
:*'''ILP32''' or '''4/4/4''' (`int`, `long`, and pointer are 32-bit);
::* Win32 API
::* Unix and Unix-like systems (Linux, macOS)
64 bit systems:
:* '''LLP64''' or '''4/4/8''' (`int` and `long` are 32-bit, pointer is 64-bit)
::* [https://learn.microsoft.com/en-us/windows/win32/desktop-programming Win32 API] (also called the Windows API) with compilation target [AArch64|64-bit ARM](https://en.wikipedia.org/wiki/AArch64|64-bit ARM) (AArch64) or [x86-64](https://en.wikipedia.org/wiki/x86-64) (a.k.a. x64)
:* '''LP64''' or '''4/8/8''' (`int` is 32-bit, `long` and pointer are 64-bit)
::* Unix and Unix-like systems (Linux, macOS)
Other models are very rare. For example, '''ILP64''' ('''8/8/8''': `int`, `long`, and pointer are 64-bit) only appeared in some early 64-bit Unix systems (e.g. [UNICOS|UNICOS on Cray](https://en.wikipedia.org/wiki/UNICOS|UNICOS on Cray)).

## Notes


## Keywords

`cpp/keyword/void`,
`cpp/keyword/bool`,
`cpp/keyword/true`,
`cpp/keyword/false`,
`cpp/keyword/char`,
`cpp/keyword/char8_t`,
`cpp/keyword/char16_t`,
`cpp/keyword/char32_t`,
`cpp/keyword/wchar_t`,
`cpp/keyword/int`,
`cpp/keyword/short`,
`cpp/keyword/long`,
`cpp/keyword/signed`,
`cpp/keyword/unsigned`,
`cpp/keyword/float`,
`cpp/keyword/double`

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-238 | C++98 | the constraints placed on a floating-point implementation was unspecified | specified as<br>no constraint |
| cwg-2723 | C++98 | the ranges of representable values for floating-point types were not specified | specified |


## References


## See also

* `The C++ type system overview`
* `Const-volatility (cv) specifiers and qualifiers`
* `Storage duration specifiers`
