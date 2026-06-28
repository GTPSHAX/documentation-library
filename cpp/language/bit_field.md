---
title: Bit-field
type: Language
source: https://en.cppreference.com/w/cpp/language/bit_field
---


# Bit-field

Declares a class data member with explicit size, in bits. Adjacent bit-field members may (or may not) be packed to share and straddle the individual bytes.
A bit-field declaration is a `class data member declaration` which uses the following declarator:

**Syntax:**

- `sdsc|num=1|`
- `*identifier* (optional) *attr* (optional) **`:`** *size*`
- `|`
- `*identifier* (optional) *attr* (optional) **`:`** *size* *brace-or-equal-initializer*`
The ''type'' of the bit-field is introduced by the *decl-specifier-seq* of the `declaration syntax`.

### Parameters

- `{{spar` - attr|<sup>(C++11)</sup> sequence of any number of `attributes`
- `{{spar` - identifier|the name of the bit-field that is being declared. The name is optional: unnamed bit-fields introduce the specified number of `padding bits`.
- `{{spar` - size|an `integral constant expression` with a value greater or equal to zero. When greater than zero, this is the number of bits that this bit-field will occupy. The value zero is only allowed for nameless bit-fields and has special meaning.
- `{{spar` - brace-or-equal-initializer|`default member initializer` to be used with this bit-field

## Explanation

The type of a bit-field can only be integral (including `bool`) or (possibly cv-qualified) enumeration type, an unnamed bit-field cannot be declared with a cv-qualified type.
A bit-field cannot be a `static data member`.
There are no bit-field `prvalues`: lvalue-to-rvalue conversion always produces an object of the underlying type of the bit-field.
The number of bits in a bit-field sets the limit to the range of values it can hold:

### Example

```cpp
#include <iostream>

struct S
{
    // three-bit unsigned field, allowed values are 0...7
    unsigned int b : 3;
};

int main()
{
    S s = {6};

    ++s.b; // store the value 7 in the bit-field
    std::cout << s.b << '\n';

    ++s.b; // the value 8 does not fit in this bit-field
    std::cout << s.b << '\n'; // formally implementation-defined, typically 0
}
```


**Output:**
```
7
0
```

Multiple adjacent bit-fields are usually packed together (although this behavior is implementation-defined):

### Example

```cpp
#include <bit>
#include <cstdint>
#include <iostream>

struct S
{
    // will usually occupy 2 bytes:
    unsigned char b1 : 3; // 1st 3 bits (in 1st byte) are b1
    unsigned char    : 2; // next 2 bits (in 1st byte) are blocked out as unused
    unsigned char b2 : 6; // 6 bits for b2 - doesn't fit into the 1st byte => starts a 2nd
    unsigned char b3 : 2; // 2 bits for b3 - next (and final) bits in the 2nd byte
};

int main()
{
    std::cout << sizeof(S) << '\n'; // usually prints 2

    S s;
    // set distinguishable field values
    s.b1 = 0b111;
    s.b2 = 0b101111;
    s.b3 = 0b11;

    // show layout of fields in S
    auto i = std::bit_cast<std::uint16_t>(s);
    // usually prints 1110000011110111
    // breakdown is:  └┬┘├┘└┬┘└─┬──┘└┤
    //                b1 u  a   b2  b3
    // where “u” marks the unused :2 specified in the struct, and
    // “a” marks compiler-added padding to byte-align the next field.
    // Byte-alignment is happening because b2's type is declared unsigned char;
    // if b2 were declared uint16_t there would be no “a”, b2 would abut “u”.
    for (auto b = i; b; b >>= 1) // print LSB-first
        std::cout << (b & 1);
    std::cout << '\n';
}
```


**Output:**
```
2
1110000011110111
```

The special unnamed bit-field of size zero can be forced to break up padding. It specifies that the next bit-field begins at the beginning of its allocation unit:

### Example

```cpp
#include <iostream>

struct S
{
    // will usually occupy 2 bytes:
    // 3 bits: value of b1
    // 5 bits: unused
    // 2 bits: value of b2
    // 6 bits: unused
    unsigned char b1 : 3;
    unsigned char :0; // start a new byte
    unsigned char b2 : 2;
};

int main()
{
    std::cout << sizeof(S) << '\n'; // usually prints 2
                                    // would usually print 1 if not for
                                    // the padding break in line 11
}
```


**Output:**
```
2
```

If the specified size of the bit-field is greater than the size of its type, the value is limited by the type: a `std::uint8_t b : 1000;` would still hold values in the range . The extra bits are `padding bits`.
Because bit-fields do not necessarily begin at the beginning of a byte, address of a bit-field cannot be taken. Pointers and non-const references to bit-fields are not possible. When `initializing a const reference` from a bit-field, a temporary is created (its type is the type of the bit-field), copy initialized with the value of the bit-field, and the reference is bound to that temporary.
rrev multi
|rev1=
There are no `default member initializers` for bit-fields: `1=int b : 1 = 0;` and } are ill-formed.
|since2=c++20|rev2=
In case of ambiguity between the size of the bit-field and the default member initializer, the longest sequence of tokens that forms a valid size is chosen:

```cpp
int a;
const int b = 0;

struct S
{
    // simple cases
    int x1 : 8 = 42; // OK; "= 42" is brace-or-equal-initializer
    int x2 : 8 {42}; // OK; "{42}" is brace-or-equal-initializer

    // ambiguities
    int y1 : true ? 8 : a = 42;   // OK; brace-or-equal-initializer is absent
    int y2 : true ? 8 : b = 42;   // error: cannot assign to const int
    int y3 : (true ? 8 : b) = 42; // OK; "= 42" is brace-or-equal-initializer
    int z : 1 {{!!
```

};

## Notes

The following properties of bit-fields are ''implementation-defined'':
* The value that results from assigning or initializing a signed bit-field with a value out of range, or from incrementing a signed bit-field past its range.
* Everything about the actual allocation details of bit-fields within the class object.
:* For example, on some platforms, bit-fields don't straddle bytes, on others they do.
:* Also, on some platforms, bit-fields are packed left-to-right, on others right-to-left.
In the C programming language, the width of a bit-field cannot exceed the width of the underlying type, and whether `int` bit-fields that are not explicitly `signed` or `unsigned` are signed or unsigned is implementation-defined. For example, `int b : 3;` may have the range of values  or  in C, but only the latter choice is allowed in C++.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-324 | C++98 | it was unspecified whether the return value<br>of an assignment to a bit-field is a bit-field | added bit-field specifications for<br>operators which may return lvalues |
| cwg-2229 | C++98 | unnamed bit-fields could be declared with a cv-qualified type | prohibited |
| cwg-2511 | C++98 | cv-qualifications were not allowed in bit-field types | bit-fields can have cv-qualified<br>enumeration types |


## References


## See also


| cpp/utility/dsc bitset | (see dedicated page) |
| cpp/container/dsc vector_bool | (see dedicated page) |

