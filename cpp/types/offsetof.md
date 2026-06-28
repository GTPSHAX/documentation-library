---
title: offsetof
type: Utilities
source: https://en.cppreference.com/w/cpp/types/offsetof
---


# offsetof


```cpp
**Header:** `<`cstddef`>`
dcl|
#define offsetof(type, member) /* implementation-defined */
```

The macro `offsetof` expands to an integral constant expression of type `std::size_t`, the value of which is the offset, in bytes, from the beginning of an object of specified type to its specified subobject, including padding bits if any.
Given an object `o` of type `type` and static storage duration, `o.member` shall be an lvalue constant expression that refers to a subobject of `o`. Otherwise, the behavior is undefined. Particularly, if `member` is a static data member, a bit-field, or a member function, the behavior is undefined.
If `type` is not a <sup>(until C++11)</sup> *PODType*<sup>(since C++11)</sup> , <sup>(until C++17)</sup> the result of `offsetof` is undefined<sup>(since C++17)</sup> use of the `offsetof` macro is conditionally-supported.
The expression `offsetof(type, member)` is never type-dependent and it is value-dependent if and only if `type` is dependent.

## Exceptions

`offsetof` throws no exceptions.
rrev|since=c++11|
The expression `noexcept(offsetof(type, member))` always evaluates to `true`.

## Notes

rrev|since=c++11|
The offset of the first member of a standard-layout type is always zero (empty-base optimization is mandatory).
`offsetof` cannot be implemented in standard C++ and requires compiler support: [https://github.com/gcc-mirror/gcc/blob/68ec60c4a377b532ec2d265ea542107c36b1d15c/gcc/ginclude/stddef.h#L406 GCC], [https://github.com/llvm-mirror/clang/blob/release_70/lib/Headers/stddef.h#L120 LLVM].
`member` is not restricted to a direct member. It can denote a subobject of a given member, such as an element of an array member. This is specified by .
It is specified in C23 that defining a new type containing an unparenthesized comma in `offsetof` is undefined behavior, and such usage is generally not supported by implementations in C++ modes: } is rejected by all known implementations.

## Example


### Example

```cpp
#include <cstddef>
#include <iostream>

struct S
{
    char   m0;
    double m1;
    short  m2;
    char   m3;
//  private: int z; // warning: 'S' is a non-standard-layout type
};

int main()
{
    std::cout
        << "offset of char   m0 = " << offsetof(S, m0) << '\n'
        << "offset of double m1 = " << offsetof(S, m1) << '\n'
        << "offset of short  m2 = " << offsetof(S, m2) << '\n'
        << "offset of char   m3 = " << offsetof(S, m3) << '\n';
}
```


**Output:**
```
offset of char   m0 = 0
offset of double m1 = 8
offset of short  m2 = 16
offset of char   m3 = 18
```


## Defect reports


## See also


| cpp/types/dsc size_t | (see dedicated page) |
| cpp/types/dsc is_standard_layout | (see dedicated page) |

