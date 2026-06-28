---
title: Arithmetic operators
type: Language
source: https://en.cppreference.com/w/cpp/language/operator_arithmetic
---


# Arithmetic operators

Returns the result of specific arithmetic operation.


| - |
| rowspan="2" | Operator name |
| rowspan="2" | Syntax |
| colspan="2" | Prototype examples (for c/core | class T) |
| - |
| Inside class definition |
| Outside class definition |
| - |
| Unary plus |
| co | +a |
| c | T T::operator+() const; |
| c | T operator+(const T& a); |
| - |
| Unary minus |
| co | -a |
| c | T T::operator-() const; |
| c | T operator-(const T& a); |
| - |
| Addition |
| co | a + b |
| c | T T::operator+(const T2& b) const; |
| c | T operator+(const T& a, const T2& b); |
| - |
| Subtraction |
| co | a - b |
| c | T T::operator-(const T2& b) const; |
| c | T operator-(const T& a, const T2& b); |
| - |
| Multiplication |
| co | a * b |
| c | T T::operator*(const T2& b) const; |
| c | T operator*(const T& a, const T2& b); |
| - |
| Division |
| co | a / b |
| c | T T::operator/(const T2& b) const; |
| c | T operator/(const T& a, const T2& b); |
| - |
| Remainder |
| co | a % b |
| c | T T::operator%(const T2& b) const; |
| c | T operator%(const T& a, const T2& b); |
| - |
| Bitwise NOT |
| co | ~a |
| c | T T::operator~() const; |
| c | T operator~(const T& a); |
| - |
| Bitwise AND |
| co | a & b |
| c | T T::operator&(const T2& b) const; |
| c | T operator&(const T& a, const T2& b); |
| - |
| Bitwise OR |
| co | a | b |
| c | T T::operator|(const T2& b) const; |
| c | T operator|(const T& a, const T2& b); |
| - |
| Bitwise XOR |
| co | a ^ b |
| c | T T::operator^(const T2& b) const; |
| c | T operator^(const T& a, const T2& b); |
| - |
| Bitwise left shift |
| co | a << b |
| c | T T::operator<<(const T2& b) const; |
| c | T operator<<(const T& a, const T2& b); |
| - |
| Bitwise right shift |
| co | a >> b |
| c | T T::operator>>(const T2& b) const; |
| c | T operator>>(const T& a, const T2& b); |
| - |
| colspan="5" |  |


## General explanation

All built-in arithmetic operators compute the result of specific arithmetic operation and returns its result. The arguments are not modified.

### Conversions

If the operand passed to a built-in arithmetic operator is integral or unscoped enumeration type, then before any other action (but after lvalue-to-rvalue conversion, if applicable), the operand undergoes . If an operand has array or function type, `array-to-pointer` and  conversions are applied.
For the binary operators (except shifts), if the promoted operands have different types, `usual arithmetic conversions` are applied.

### Overflows

Unsigned integer arithmetic is always performed $modulo 2 where n is the number of bits in that particular integer. E.g. for `unsigned int`, adding one to `UINT_MAX` gives `0`, and subtracting one from `0` gives `UINT_MAX`.
When signed integer arithmetic operation overflows (the result does not fit in the result type), the behavior is undefined, — the possible manifestations of such an operation include:
* it wraps around according to the rules of the representation (typically `two's complement`),
* it traps — on some platforms or due to compiler options (e.g. `-ftrapv` in GCC and Clang),
* it saturates to minimal or maximal value (on many DSPs),
* it is completely [https://blog.llvm.org/2011/05/what-every-c-programmer-should-know_14.html optimized out by the compiler].

### Floating-point environment

If `cpp/preprocessor/impl|#pragma STDC FENV_ACCESS` is supported and set to `ON`, all floating-point arithmetic operators obey the current floating-point rounding direction and report floating-point arithmetic errors as specified in `cpp/numeric/math/math_errhandling` unless part of a `static initializer` (in which case floating-point exceptions are not raised and the rounding mode is to nearest).

### Floating-point contraction

Unless `cpp/preprocessor/impl|#pragma STDC FP_CONTRACT` is supported and set to `OFF`, all floating-point arithmetic may be performed as if the intermediate results have infinite range and precision, that is, optimizations that omit rounding errors and floating-point exceptions are allowed. For example, C++ allows the implementation of `(x * y) + z` with a single fused multiply-add CPU instruction or optimization of `1=a = x * x * x * x;` as `1=tmp = x * x; a = tmp * tmp`.
Unrelated to contracting, intermediate results of floating-point arithmetic may have range and precision that is different from the one indicated by its type, see `FLT_EVAL_METHOD`.
Formally, the C++ standard makes no guarantee on the accuracy of floating-point operations.

## Unary arithmetic operators

The unary arithmetic operator expressions have the form

**Syntax:**

- `*expression*`
- `*expression*`
1. Unary plus (promotion).
2. Unary minus (negation).
Unary `+` and `-` operators have higher `precedence` than all binary arithmetic operators, so *expression* cannot contain top-level binary arithmetic operators. These operators associate from right to left:

```cpp
+a - b; // equivalent to (+a) - b, NOT +(a - b)
-c + d; // equivalent to (-c) + d, NOT -(c + d)

+-e; // equivalent to +(-e), the unary + is a no-op if “e” is a built-in type
     // because any possible promotion is performed during negation already
```


### Built-in unary arithmetic operators

1. For the built-in unary plus operator, *expression* must be a prvalue of arithmetic, unscoped enumeration, or pointer type. Integral promotion is performed on *expression* if it has integral or unscoped enumeration type. The type of the result is the (possibly promoted) type of *expression*.
@@ The result of the built-in promotion is the value of *expression*. The built-in unary operation is no-op if the operand is a prvalue of a promoted integral type or a pointer type. Otherwise, the type or value category of the operand is changed by integral promotion or lvalue-to-rvalue, array-to-pointer, function-to-pointer, or user-defined conversion. For example, `char` is converted to `int` <sup>(since C++11)</sup> , and non-generic captureless `lambda expression is converted to function pointer` in unary plus expressions.
2. For the built-in unary minus operator, *expression* must be a prvalue of arithmetic or unscoped enumeration type. Integral promotion is performed on *expression*. The type of the result is the type of the promoted type of *expression*.
@@ The result of the built-in negation is the negative of the promoted *expression*. For unsigned `a`, the value of `-a` is }, where `N` is the number of bits after promotion.
* In other words, the result is the two’s complement of the operand (where operand and result are considered as unsigned).

### Overloads

In `overload resolution against user-defined operators`, for every cv-unqualified promoted arithmetic type `A` and for every type `T`, the following function signatures participate in overload resolution:

```cpp
```


### Example

```cpp
#include <iostream>

int main()
{
    char c = 0x6a;
    int n1 = 1;
    unsigned char n2 = 1;
    unsigned int n3 = 1;
    std::cout << "char: " << c << " int: " << +c << "\n"
                 "-1, where 1 is signed: " << -n1 << "\n"
                 "-1, where 1 is unsigned char: " << -n2 << "\n"
                 "-1, where 1 is unsigned int: " << -n3 << '\n';
    char a[3];
    std::cout << "size of array: " << sizeof a << "\n"
                 "size of pointer: " << sizeof +a << '\n';
}
```


**Output:**
```
char: j int: 106
-1, where 1 is signed: -1
-1, where 1 is unsigned char: -1
-1, where 1 is unsigned int: 4294967295
size of array: 3
size of pointer: 8
```


## Additive operators

The additive operator expressions have the form

**Syntax:**

- `**`+`** *rhs*`
- `**`-`** *rhs*`
1. Binary plus (addition).
2. Binary minus (subtraction).
Binary `+` and `-` operators have higher `precedence` than all other binary arithmetic operators except `*`, `/` and `%`. These operators associate from left to right:

```cpp
a + b * c;  // equivalent to a + (b * c),  NOT (a + b) * c
d / e - f;  // equivalent to (d / e) - f,  NOT d / (e - f)
g + h >> i; // equivalent to (g + h) >> i, NOT g + (h >> i)

j - k + l - m; // equivalent to ((j - k) + l) - m
```


### Built-in additive operators

For built-in binary plus and binary minus operators, both of *lhs* and *rhs* must be prvalues, and one of the following conditions must be satisfied:
* Both operands have arithmetic or unscoped enumeration type. In this case, `usual arithmetic conversions` are performed on both operands.
* Exactly one operand has integral or unscoped enumeration type. In this case, integral promotion is applied to that operand.
In the remaining description in this section, "operand(s)", *lhs* and *rhs* refer to the converted or promoted operand(s).
1. For built-in addition, one of the following conditions must be satisfied:
* Both operands have arithmetic type. In this case, the result is the sum of the operands.
* One operand is a pointer to a completely-defined object type, and the other operand has integral type. In this case, the integral value is added to the pointer (see ).
2. For built-in subtraction, one of the following conditions must be satisfied:
* Both operands have arithmetic type. In this case, the result is the difference resulting from the subtraction of *rhs* from *lhs*.
* *lhs* is a pointer to a completely-defined object type, and *rhs* has integral type. In this case, the integral value is subtracted from the pointer (see ).
* Both operands are pointers to cv-qualified or cv-unqualified versions of the same completely-defined object type. In this case *rhs* is subtracted from *lhs* (see ).
If both operands have a floating-point type, and the type supports IEEE floating-point arithmetic (see `std::numeric_limits::is_iec559`):
* If one operand is NaN, the result is NaN.
* Infinity minus infinity is NaN, and `FE_INVALID` is raised.
* Infinity plus the negative infinity is NaN, and `FE_INVALID` is raised.

### Pointer arithmetic

When an expression `J` that has integral type is added to or subtracted from an expression `P` of pointer type, the result has the type of `P`.
* If `P` evaluates to a `null pointer value` and `J` evaluates to `0`, the result is a null pointer value.
* Otherwise, if `P` points to the `i`th element of an array object `x` with `n` elements, given the value of `J` as `j`, `P` is added or subtracted as follows:
:* The expressions `P + J` and `J + P`
::* point to the `i+j`th element of `x` if `i + j` is in [0, n), and
::* are pointers past the end of the last element of `x` if `i + j` is `n`.
:* The expression `P - J`
::* points to the `i-j`th element of `x` if `i - j` is in [0, n), and
::* is a pointer past the end of the last element of `x` if `i - j` is `n`.
:* Other `j` values result in undefined behavior.
* Otherwise, if `P` points to a complete object, a base class subobject or a member subobject `y`, given the value of `J` as `j`, `P` is added or subtracted as follows:
:* The expressions `P + J` and `J + P`
::* point to `y` if `j` is `0`, and
::* are pointers past the end of `y` if `j` is `1`.
:* The expression `P - J`
::* points to `y` if `j` is `0`, and
::* is a pointer past the end of `y` if `j` is `-1`.
:* Other `j` values result in undefined behavior.
* Otherwise, if `P` is a pointer past the end of an object `z`, given the value of `J` as `j`:
:* If `z` is an array object with `n` elements, `P` is added or subtracted as follows:
::* The expressions `P + J` and `J + P`
:::* point to the `n+j`th element of `z` if `n + j` is in [0, n), and
:::* are pointers past the end of the last element of `z` if `j` is `0`.
::* The expression `P - J`
:::* points to the `n-j`th element of `z` if `n - j` is in [0, n), and
:::* is a pointer past the end of the last element of `z` if `j` is `0`.
::* Other `j` values result in undefined behavior.
:* Otherwise, `P` is added or subtracted as follows:
::* The expressions `P + J` and `J + P`
:::* point to `z` if `j` is `-1`, and
:::* are pointers past the end of `z` if `j` is `0`.
::* The expression `P - J`
:::* points to `z` if `j` is `1`, and
:::* is a pointer past the end of `z` if `j` is `0`.
::* Other `j` values result in undefined behavior.
* Otherwise, the behavior is undefined.
When two pointer expressions `P` and `Q` are subtracted, the type of the result is  `std::ptrdiff_t`.
* If `P` and `Q` both evaluate to `null pointer values`, the result is `0`.
* Otherwise, if `P` and `Q` point to, respectively, the `i`th and `j`th array elements of the same array object `x`, the expression `P - Q` has the value `i − j`.
:* If `i − j` is not representable by `std::ptrdiff_t`, the behavior is undefined.
* Otherwise, if `P` and `Q` point to the same complete object, base class subobject or member subobject, the result is `0`.
* Otherwise, the behavior is undefined.
These pointer arithmetic operators allow pointers to satisfy the *RandomAccessIterator* requirements.
For addition and subtraction, if `P` or `Q` have type “pointer to (possibly cv-qualified) `T`”, where `T` and the array element type are not `similar`, the behavior is undefined:

```cpp
int arr[5] = {1, 2, 3, 4, 5};
unsigned int *p = reinterpret_cast<unsigned int*>(arr + 1);
unsigned int k = *p; // OK, the value of “k” is 2
unsigned int *q = p + 1; // undefined behavior: “p” points to int, not unsigned int
```


### Overloads

In `overload resolution against user-defined operators`, for every pair of promoted arithmetic types `L` and `R` and for every object type `T`, the following function signatures participate in overload resolution:

```cpp
```

where `LR` is the result of `usual arithmetic conversions` on `L` and `R`.

### Example

```cpp
#include <iostream>

int main()
{
    char c = 2;
    unsigned int un = 2;
    int n = -10;
    std::cout << " 2 + (-10), where 2 is a char    = " << c + n << "\n"
                 " 2 + (-10), where 2 is unsigned  = " << un + n << "\n"
                 " -10 - 2.12  = " << n - 2.12 << '\n';

    char a[4] = {'a', 'b', 'c', 'd'};
    char* p = &a[1];
    std::cout << "Pointer addition examples: " << *p << *(p + 2)
              << *(2 + p) << *(p - 1) << '\n';
    char* p2 = &a[4];
    std::cout << "Pointer difference: " << p2 - p << '\n';
}
```


**Output:**
```
<nowiki/>
 2 + (-10), where 2 is a char    = -8
 2 + (-10), where 2 is unsigned  = 4294967288
 -10 - 2.12  = -12.12
Pointer addition examples: bdda
Pointer difference: 3
```


### Multiplicative operators

The multiplicative operator expressions have the form

**Syntax:**

- `**`*`** *rhs*`
- `**`/`** *rhs*`
- `**`%`** *rhs*`
1. Multiplication.
2. Division.
3. Remainder.
Multiplicative operators have higher `precedence` than all other binary arithmetic operators. These operators associate from left to right:

```cpp
a + b * c;  // equivalent to a + (b * c),  NOT (a + b) * c
d / e - f;  // equivalent to (d / e) - f,  NOT d / (e - f)
g % h >> i; // equivalent to (g % h) >> i, NOT g % (h >> i)

j * k / l % m; // equivalent to ((j * k) / l) % m
```


### Built-in multiplicative operators

For built-in multiplication and division operators, both operands must have arithmetic or unscoped enumeration type. For the built-in remainder operator, both operands must have integral or unscoped enumeration type. `Usual arithmetic conversions` are performed on both operands.
In the remaining description in this section, "operand(s)", *lhs* and *rhs* refer to the converted operand(s).
1. The result of built-in multiplication is the product of the operands.
@@ If both operands have a floating-point type, and the type supports IEEE floating-point arithmetic (see `std::numeric_limits::is_iec559`):
* Multiplication of a NaN by any number gives NaN.
* Multiplication of infinity by zero gives NaN and `FE_INVALID` is raised.
2. The result of built-in division is *lhs* divided by *rhs*. If *rhs* is zero, the behavior is undefined.
@@ If both operands have an integral type, the result is the algebraic quotient (performs integer division): the quotient is truncated towards zero (fractional part is discarded).
@@ If both operands have a floating-point type, and the type supports IEEE floating-point arithmetic (see `std::numeric_limits::is_iec559`):
* If one operand is NaN, the result is NaN.
* Dividing a non-zero number by ±0.0 gives the correctly-signed infinity and `FE_DIVBYZERO` is raised.
* Dividing 0.0 by 0.0 gives NaN and `FE_INVALID` is raised.
3. The result of built-in remainder is the remainder of the integer division of *lhs* by *rhs*. If *rhs* is zero, the behavior is undefined.
@@ If `a / b` is representable in the result type, `1=(a / b) * b + a % b == a`.
@@ If `a / b` is not representable in the result type, the behavior of both `a / b` and `a % b` is undefined (that means `INT_MIN % -1` is undefined on two's complement systems).
Note: Until  was resolved (), if one or both operands to binary operator % were negative, the sign of the remainder was implementation-defined, as it depends on the rounding direction of integer division. The function `std::div` provided well-defined behavior in that case.
Note: for floating-point remainder, see `std::remainder` and `std::fmod`.

### Overloads

In `overload resolution against user-defined operators`, for every pair of promoted arithmetic types `LA` and `RA` and for every pair of promoted integral types `LI` and `RI` the following function signatures participate in overload resolution:

```cpp
```

where `LRx` is the result of `usual arithmetic conversions` on `Lx` and `Rx`.

### Example

```cpp
#include <iostream>

int main()
{
    char c = 2;
    unsigned int un = 2;
    int  n = -10;
    std::cout << "2 * (-10), where 2 is a char    = " << c * n << "\n"
                 "2 * (-10), where 2 is unsigned  = " << un * n << "\n"
                 "-10 / 2.12  = " << n / 2.12 << "\n"
                 "-10 / 21  = " << n / 21 << "\n"
                 "-10 % 21  = " << n % 21 << '\n';
}
```


**Output:**
```
2 * (-10), where 2 is a char    = -20
2 * (-10), where 2 is unsigned  = 4294967276
-10 / 2.12  = -4.71698
-10 / 21  = 0
-10 % 21  = -10
```


## Bitwise logic operators

The bitwise logic operator expressions have the form

**Syntax:**

- `*rhs*`
- `**`&`** *rhs*`
- `**` *rhs*`
- `**`^`** *rhs*`
1. Bitwise NOT.
2. Bitwise AND.
3. Bitwise OR.
4. Bitwise XOR.
The bitwise NOT operator has higher `precedence` than all binary arithmetic operators. It associates from right to left:

```cpp
~a - b; // equivalent to (~a) - b, NOT ~(a - b)
~c * d; // equivalent to (~c) * d, NOT ~(c * d)

~-e; // equivalent to ~(-e)
```

There is an ambiguity in the grammar when `~` is followed by a `type name`<sup>(since C++11)</sup>  or `decltype specifier`: it can either be operator~ or start a `destructor` identifier). The ambiguity is resolved by treating `~` as operator~. `~` can start a destructor identifier only in places where forming an operator~ is syntactically invalid.
All other bitwise logic operators have lower `precedence` than all other binary arithmetic operators. Bitwise AND has higher precedence than bitwise XOR, which has higher precedence than bitwise OR. They associate from left to right:

```cpp
a & b * c;  // equivalent to a & (b * c),  NOT (a & b) * c
d / e ^ f;  // equivalent to (d / e) ^ f,  NOT d / (e ^ f)
g << h {{!
```

j & k & l; // equivalent to (j & k) & l
m | n ^ o  // equivalent to m | (n ^ o)

### Built-in bitwise logic operators

For the built-in bitwise NOT operator, *rhs* must be a prvalue of integral or unscoped enumeration type, and integral promotion is performed on *rhs*. For other built-in bitwise logic operators, both operands must have integral or unscoped enumeration type, and `usual arithmetic conversions` are performed on both operands.
In the remaining description in this section, "operand(s)", *lhs* and *rhs* refer to the converted or promoted operand(s).
1. Given the operand as `x` and the result of the built-in bitwise NOT operation as `r`. For each coefficient `x_i` of the base-2 representation of `x`, the corresponding coefficient `r_i` of the base-2 representation of `r` is `1` if `x_i` is `0`, and `0` otherwise.
* In other words, the result is the one’s complement of the operand (where operand and result are considered as unsigned).
@@ The type of the result `r` is the type of the operand `x`.
@2-4@ Given the operands as `x` and `y` respectively and the result of the built-in binary bitwise logic operations as `r`. For each pair of coefficients `x_i` and `y_i` of the base-2 representations of `x` and `y` respectively, the corresponding coefficient `r_i` of the base-2 representation of `r` is
:@2@ `1` if both `x_i` and `y_i` are `1`, and `0` otherwise.
:@3@ `1` if at least one of `x_i` and `y_i` is `1`, and `0` otherwise.
:@4@ `1` if either (but not both) of `x_i` and `y_i` is `1`, and `0` otherwise.
@@ The type of the result `r` is the type of the operands `x` and `y`.

### Overloads

In `overload resolution against user-defined operators`, for every pair of promoted integral types `L` and `R` the following function signatures participate in overload resolution:

```cpp
(L, R)
```

where `LR` is the result of `usual arithmetic conversions` on `L` and `R`.

### Example

```cpp
#include <bitset>
#include <cstdint>
#include <iomanip>
#include <iostream>

int main()
{
    std::uint16_t mask = 0x00f0;
    std::uint32_t x0 = 0x12345678;
    std::uint32_t x1 = x0 {{!
```

std::uint32_t x2 = x0 & ~mask;
std::uint32_t x3 = x0 & mask;
std::uint32_t x4 = x0 ^ mask;
std::uint32_t x5 = ~x0;
using bin16 = std::bitset<16>;
using bin32 = std::bitset<32>;
std::cout << std::hex << std::showbase
<< "Mask: " << mask << std::setw(49) << bin16(mask) << "\n"
"Value: " << x0 << std::setw(42) << bin32(x0) << "\n"
"Setting bits: " << x1 << std::setw(35) << bin32(x1) << "\n"
"Clearing bits: " << x2 << std::setw(34) << bin32(x2) << "\n"
"Selecting bits: " << x3 << std::setw(39) << bin32(x3) << "\n"
"XOR-ing bits: " << x4 << std::setw(35) << bin32(x4) << "\n"
"Inverting bits: " << x5 << std::setw(33) << bin32(x5) << '\n';
}
|output=
Mask: 0xf0                                 0000000011110000
Value: 0x12345678          00010010001101000101011001111000
Setting bits: 0x123456f8   00010010001101000101011011111000
Clearing bits: 0x12345608  00010010001101000101011000001000
Selecting bits: 0x70       00000000000000000000000001110000
XOR-ing bits: 0x12345688   00010010001101000101011010001000
Inverting bits: 0xedcba987 11101101110010111010100110000111

## Bitwise shift operators

The bitwise shift operator expressions have the form

**Syntax:**

- `**`<<`** *rhs*`
- `**`>>`** *rhs*`
1. Bitwise left-shift.
2. Bitwise right-shift.
Bitwise shift operators have higher `precedence` than bitwise logic operators, but have lower precedence than additive and multiplicative operators. These operators associate from left to right:

```cpp
a >> b * c;  // equivalent to a >> (b * c),  NOT (a >> b) * c
d << e & f;  // equivalent to (d << e) & f,  NOT d << (e & f)

g << h >> i; // equivalent to (g << h) >> i, NOT g << (h >> i)
```


### Built-in bitwise shift operators

For the built-in bitwise shift operators, both operands must be prvalues of integral or unscoped enumeration type. Integral promotions are performed on both operands.
In the remaining description in this section, "operand(s)", `a`, `b`, *lhs* and *rhs* refer to the converted or promoted operand(s).
If the value of *rhs* is negative or is not less than the number of bits in *lhs*, the behavior is undefined.
rrev multi|until1=c++20|rev1=
For unsigned `a`, the value of `a << b` is the value of $a * 2, reduced modulo $2 where N is the number of bits in the return type (that is, bitwise left shift is performed and the bits that get shifted out of the destination type are discarded).
For signed and non-negative `a`, if $a * 2 is representable in the unsigned version of the return type, then that value, `converted` to signed, is the value of `a << b` (this makes it legal to create `INT_MIN` as `1 << 31`); otherwise the behavior is undefined.
For negative `a`, the behavior of `a << b` is undefined.
For unsigned `a` and for signed and non-negative `a`, the value of `a >> b` is the integer part of $a/2.
For negative `a`, the value of `a >> b` is implementation-defined (in most implementations, this performs arithmetic right shift, so that the result remains negative).
|rev2=
The value of `a << b` is the unique value congruent to $a * 2 modulo $2 where N is the number of bits in the return type (that is, bitwise left shift is performed and the bits that get shifted out of the destination type are discarded).
The value of `a >> b` is $a/2, rounded towards negative infinity (in other words, right shift on signed `a` is arithmetic right shift).
The type of the result is that of *lhs*.

### Overloads

In `overload resolution against user-defined operators`, for every pair of promoted integral types `L` and `R`, the following function signatures participate in overload resolution:

```cpp
```


### Example

```cpp
#include <iostream>

enum { ONE = 1, TWO = 2 };

int main()
{
    std::cout << std::hex << std::showbase;
    char c = 0x10;
    unsigned long long ull = 0x123;
    std::cout << "0x123 << 1 = " << (ull << 1) << "\n"
                 "0x123 << 63 = " << (ull << 63) << "\n" // overflow in unsigned
                 "0x10 << 10 = " << (c << 10) << '\n';   // char is promoted to int
    long long ll = -1000;
    std::cout << std::dec << "-1000 >> 1 = " << (ll >> ONE) << '\n';
}
```


**Output:**
```
0x123 << 1 = 0x246
0x123 << 63 = 0x8000000000000000
0x10 << 10 = 0x4000
-1000 >> 1 = -500
```


## Standard library

Arithmetic operators are overloaded for many standard library types.

### Unary arithmetic operators


| cpp/chrono/duration/dsc operator arith | (see dedicated page) |
| cpp/numeric/complex/dsc operator arith2 | (see dedicated page) |
| cpp/numeric/valarray/dsc operator arith | (see dedicated page) |


### Additive operators


| cpp/chrono/time_point/dsc operator arith2 | (see dedicated page) |
| cpp/chrono/duration/dsc operator arith4 | (see dedicated page) |
| cpp/chrono/year_month_day/dsc operator arith 2 | (see dedicated page) |
| cpp/string/basic_string/dsc operator+ | (see dedicated page) |
| cpp/numeric/complex/dsc operator arith3 | (see dedicated page) |
| cpp/numeric/valarray/dsc operator arith3 | (see dedicated page) |


### Multiplicative operators


| cpp/chrono/duration/dsc operator arith4 | (see dedicated page) |
| cpp/numeric/complex/dsc operator arith3 | (see dedicated page) |
| cpp/numeric/valarray/dsc operator arith3 | (see dedicated page) |


### Bitwise logic operators


| cpp/utility/bitset/dsc operator logic | (see dedicated page) |
| cpp/utility/bitset/dsc operator logic2 | (see dedicated page) |
| cpp/numeric/valarray/operator arith3|title=operator^<br>operator&<br>operator | |


### Bitwise shift operators


| cpp/numeric/valarray/operator arith3|title=operator<<<br>operator>>|applies binary operators to each element of two valarrays, or a valarray and a value | |


### Stream insertion/extraction operators

Throughout the standard library, bitwise shift operators are commonly overloaded with I/O stream (`std::ios_base&` or one of the classes derived from it) as both the left operand and return type. Such operators are known as ''stream insertion'' and ''stream extraction'' operators:


| cpp/io/basic_istream/dsc operator gtgt | (see dedicated page) |
| cpp/io/basic_istream/dsc operator gtgt2 | (see dedicated page) |
| cpp/io/basic_ostream/dsc operator ltlt | (see dedicated page) |
| cpp/io/basic_ostream/dsc operator ltlt2 | (see dedicated page) |
| cpp/numeric/complex/dsc operator ltltgtgt | (see dedicated page) |
| cpp/utility/bitset/dsc operator ltltgtgt2 | (see dedicated page) |
| cpp/string/basic_string/dsc operator ltltgtgt | (see dedicated page) |
| cpp/numeric/random/engine/dsc operator ltltgtgt|linear_congruential_engine | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator ltltgtgt|uniform_int_distribution | (see dedicated page) |


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-614 | C++98 | the algebraic quotient of integer division was<br>rounded in implementation-defined direction | the algebraic quotient of integer<br>division is truncated towards zero<br>(fractional part is discarded) |
| cwg-1504 | C++98 | a pointer to a base class subobject of an array<br>element could be used in pointer arithmetic | the behavior is<br>undefined in this case |
| cwg-1642 | C++98 | arithmetic operators allow their operands to be lvalues | some operands must be rvalues |
| cwg-2724 | C++20 | the rounding direction of arithmetic right shift was unclear | made clear |
| cwg-2853 | C++98 | a pointer past the end of an object could<br>not be added or subtracted with an integer | it can |


## See also

`Operator precedence`
`Operator overloading`
