---
title: std::breakpoint
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/breakpoint
---

ddcl|header=debugging|since=c++26|
void breakpoint() noexcept;
Unconditional breakpoint: Attempts to temporarily stop program execution and pass control to the debugger, regardless of whether the presence of a debugger can be detected. The behavior of this function is implementation-defined.

## Notes

The intent of this function is allowing for runtime control of breakpoints beyond what might be available from a debugger while not causing the program to exit. For example, breaking when an infrequent non-critical condition is detected, allowing programmatic control with complex runtime sensitive conditions, breaking on user input to inspect context in interactive programs without needing to switch to the debugger application, etc.
This function standardizes many similar existing facilities: [https://clang.llvm.org/docs/LanguageExtensions.html#builtin-debugtrap `__builtin_debugtrap`] from LLVM, [https://learn.microsoft.com/en-us/windows/win32/api/debugapi/nf-debugapi-debugbreak `DebugBreak()`] from Win32 API, [https://learn.microsoft.com/en-us/cpp/intrinsics/debugbreak `__debugbreak`] Microsoft Specific C/C++ extension, [https://github.com/boostorg/test/blob/develop/include/boost/test/impl/debug.ipp#L716 `debugger_break`] from [https://www.boost.org/doc/libs/release/libs/test/doc/html/index.html boost.test], `assert(false)`, } (MSVC) and `asm("int3")` (GCC/clang) for x86 targets, etc.

## Example


## External links

