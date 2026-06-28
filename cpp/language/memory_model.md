---
title: Memory model
type: Language
source: https://en.cppreference.com/w/cpp/language/memory_model
---


# Memory model

Defines the semantics of computer memory storage for the purpose of the C++ abstract machine.
The memory available to a C++ program is one or more contiguous sequences of ''bytes''. Each byte in memory has a unique ''address''.

## Byte

A ''byte'' is the smallest addressable unit of memory. It is defined as a contiguous sequence of bits, large enough to hold
* the value of any `UTF-8` code unit (256 distinct values) and of
rrev multi
|rev1=
* any member of the .
|since2=c++23|rev2=
* the ordinary literal encoding of any element of the .
Similar to C, C++ supports bytes of sizes 8 bits and greater.
The `types` `char`, `unsigned char`, and `signed char` use one byte for both storage and `value representation`. The number of bits in a byte is accessible as `CHAR_BIT` or `std::numeric_limits<unsigned char>::digits`.

## Memory location

A ''memory location'' is the storage occupied by the `object representation` of either an object of scalar type that is not a `bit-field`, or the largest contiguous sequence of bit-fields of non-zero length.
Note: Various features of the language, such as `reference`s and `virtual functions`, might involve additional memory locations that are not accessible to programs but are managed by the implementation.

```cpp
struct S
{
    char a;     // memory location #1
    int b : 5;  // memory location #2
    int c : 11, // memory location #2 (continued)
          : 0,
        d : 8;  // memory location #3
    struct
    {
        int ee : 8; // memory location #4
    } e;
} obj; // The object “obj” consists of 4 separate memory locations
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1953 | C++98 | objects occupying the same storage were<br>considered as different memory locations | memory location<br>now refers to storage |


## See also

