---
title: #pragma directive
type: Language
source: https://en.cppreference.com/w/cpp/preprocessor/impl
---


# Implementation defined behavior control

Implementation defined behavior is controlled by `#pragma` directive.

## Syntax


**Syntax:**

- `*pragma-params*`
- `|**`_Pragma(`** *string-literal* **`)`**`
1. Behaves in implementation-defined manner.
2. Removes the `L` prefix (if any), the outer quotes, and leading/trailing whitespace from *string-literal*, replaces each `\"` with `"` and each `\\` with `\`, then tokenizes the result (as in translation phase 3), and then uses the result as if the input to `#pragma` in .

## Explanation

Pragma directive controls implementation-specific behavior of the compiler, such as disabling compiler warnings or changing alignment requirements. Any pragma that is not recognized is ignored.

## Non-standard pragmas

The ISO C++ language standard does not require the compilers to support any pragmas. However, several non-standard pragmas are supported by multiple implementations:

### `#pragma STDC`

ISO C language standard requires that C compilers support the following three pragmas, and some C++ compiler vendors support them, to varying degrees, in their C++ frontends:

**Syntax:**

- `*arg*`
- `*arg*`
- `*arg*`
where *arg* is either **`ON`**, **`OFF`**, or **`DEFAULT`**.
1. If set to **`ON`**, informs the compiler that the program will access or modify floating-point environment, which means that optimizations that could subvert flag tests and mode changes (e.g., global common subexpression elimination, code motion, and constant folding) are prohibited. The default value is implementation-defined, usually **`OFF`**.
2. Allows ''contracting'' of floating-point expressions, that is optimizations that omit rounding errors and floating-point exceptions that would be observed if the expression was evaluated exactly as written. For example, allows the implementation of `(x * y) + z` with a single fused multiply-add CPU instruction. The default value is implementation-defined, usually **`ON`**.
3. Informs the compiler that multiplication, division, and absolute value of complex numbers may use simplified mathematical formulas $1= (x+iy)×(u+iv) = (xu-yv)+i(yu+xv)$, $1= (x+iy)/(u+iv) = [(xu+yv)+i(yu-xv)]/(u, and $1= , despite the possibility of intermediate overflow. In other words, the programmer guarantees that the range of the values that will be passed to those function is limited. The default value is **`OFF`**.
The behavior of the program is undefined if any of the three pragmas above appear in any context other than outside all external declarations or preceding all explicit declarations and statements inside a compound statement.
Note: compilers that do not support these pragmas may provide equivalent compile-time options, such as gcc's `-fcx-limited-range` and `-ffp-contract`.

### `#pragma once`


### `#pragma pack`


## References


## See also


## External links

