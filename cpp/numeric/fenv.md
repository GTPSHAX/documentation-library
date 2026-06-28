---
title: Floating-point environment
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/fenv
---


# Floating-point environment mark since c++11

The floating-point environment is the set of floating-point status flags and control modes supported by the implementation. It is thread-local. Each thread inherits the initial state of its floating-point environment from the parent thread. Floating-point operations modify the floating-point status flags to indicate abnormal results or auxiliary information. The state of floating-point control modes affects the outcomes of some floating-point operations.
The floating-point environment access and modification is only meaningful when `cpp/preprocessor/impl|#pragma STDC FENV_ACCESS` is supported and is set to `ON`. Otherwise the implementation is free to assume that floating-point control modes are always the default ones and that floating-point status flags are never tested or modified. In practice, few current compilers, such as HP aCC, Oracle Studio, or IBM XL, support the `#pragma` explicitly, but most compilers allow meaningful access to the floating-point environment anyway.

## Types


| cfenv | |
| cpp/numeric/fenv/dsc fenv_t | (see dedicated page) |
| cpp/numeric/fenv/dsc fexcept_t | (see dedicated page) |


## Functions


| cpp/numeric/fenv/dsc feclearexcept | (see dedicated page) |
| cpp/numeric/fenv/dsc fetestexcept | (see dedicated page) |
| cpp/numeric/fenv/dsc feraiseexcept | (see dedicated page) |
| cpp/numeric/fenv/dsc feexceptflag | (see dedicated page) |
| cpp/numeric/fenv/dsc feround | (see dedicated page) |
| cpp/numeric/fenv/dsc feenv | (see dedicated page) |
| cpp/numeric/fenv/dsc feholdexcept | (see dedicated page) |
| cpp/numeric/fenv/dsc feupdateenv | (see dedicated page) |


## Macros


| cpp/numeric/fenv/dsc FE_exceptions | (see dedicated page) |
| cpp/numeric/fenv/dsc FE_round | (see dedicated page) |
| cpp/numeric/fenv/dsc FE_DFL_ENV | (see dedicated page) |


## Notes

The floating-point exceptions are not related to the C++ exceptions. When a floating-point operation raises a floating-point exception, the status of the floating-point environment changes, which can be tested with `std::fetestexcept`, but the execution of a C++ program on most implementations continues uninterrupted.
There are compiler extensions that may be used to generate C++ exceptions automatically whenever a floating-point exception is raised:
* GNU libc function [https://www.gnu.org/savannah-checkouts/gnu/libc/manual/html_node/Control-Functions.html `feenableexcept()`] enables trapping of the floating-point exceptions, which generates the signal `SIGFPE`. If the compiler option `-fnon-call-exceptions` was used, the handler for that signal may throw a user-defined C++ exception.
* MSVC function [https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/control87-controlfp-control87-2 `_control87()`] enables trapping of the floating-point exceptions, which generates a hardware exception, which can be converted to C++ exceptions with [https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/set-se-translator `_set_se_translator`].

## See also

