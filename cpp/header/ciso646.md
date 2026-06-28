---
title: ciso646>
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/ciso646
---

Compatibility header, in C defines alternative operator representations which are keywords in C++.
This means that in a conforming implementation, including this header has no effect.

## Notes

In old or nonconforming compilers, using the alternative operator representations may still require including this header.
`<ciso646>` is removed in C++20. Corresponding `<iso646.h>` is still available in C++20.
Prior to C++20, including `<ciso646>` was sometimes used as a technique for obtaining definitions of implementation-specific library version macros without causing other effects.
As of C++20, the header  was added for this purpose.
