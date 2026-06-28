---
title: Preprocessor
type: Language
source: https://en.cppreference.com/w/cpp/preprocessor
---


# Preprocessor

The preprocessor is executed at translation phase 4, before the compilation. The result of preprocessing is a single file which is then passed to the actual compiler.

## Directives

The preprocessing directives control the behavior of the preprocessor. Each directive occupies one line and has the following format:
* the `#` character.
* a sequence of:
:* a standard-defined directive name (listed below) followed by the corresponding arguments, or
:* one or more preprocessing tokens where the beginning token is not a standard-defined directive name, in this case the directive is conditionally-supported with implementation-defined semantics<sup>(until C++23)</sup>  (e.g. a common non-standard extension is the directive `#warning` which emits a user-defined message during compilation), or
:* nothing, in this case the directive has no effect.
* a line break.
rrev|since=c++20|
The module and import directives are also preprocessing directives.
Preprocessing directives must not come from macro expansion.

```cpp
#define EMPTY
EMPTY   #   include <file.h> // not a preprocessing directive
```


## Capabilities

The preprocessor has the source file translation capabilities:
* '''''' compile parts of source file (controlled by directive `#if`, `#ifdef`, `#ifndef`, `#else`, `#elif`<sup>(since C++23)</sup> , `#elifdef`, `#elifndef`, and `#endif`).
* '''''' text macros while possibly concatenating or quoting identifiers (controlled by directives `#define` and `#undef`, and operators `#` and `##`).
* '''''' other files (controlled by directive `#include` <sup>(since C++17)</sup> and checked with `__has_include`).
* cause an '''''' <sup>(since C++23)</sup> or ''' (controlled by directive `#error`<sup>(since C++23)</sup>  or `#warning` respectively).
The following aspects of the preprocessor can be controlled:
* '''''' behavior (controlled by directive `#pragma` <sup>(since C++11)</sup> and operator `_Pragma`). In addition, some compilers support (to varying degrees) the operator `__pragma` as a ''non-standard'' extension.
* '''''' available to the preprocessor (controlled by directive `#line`).

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-2001 | C++98 | the behavior of using non-standard-defined directives was not clear | made conditionally-supported |


## See also

