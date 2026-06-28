---
title: Assignment operators
type: Language
source: https://en.cppreference.com/w/cpp/language/operator_assignment
---


# Assignment operators

Assignment operators modify the value of the object.


| - |
| rowspan="2" | Operator name |
| rowspan="2" | &nbsp;Syntax&nbsp; |
| rowspan="2" | rlp | operators | Over&#8203;load&#8203;able |
| colspan="2" | Prototype examples (for c/core | class T) |
| - |
| Inside class definition |
| Outside class definition |
| - |
| simple assignment |
| tt | 1=a = b |
|  |
| c | 1=T& T::operator =(const T2& b); |
|  |
| - |
| addition assignment |
| tt | 1=a += b |
|  |
| c | 1=T& T::operator +=(const T2& b); |
| c | 1=T& operator +=(T& a, const T2& b); |
| - |
| subtraction assignment |
| tt | 1=a -= b |
|  |
| c | 1=T& T::operator -=(const T2& b); |
| c | 1=T& operator -=(T& a, const T2& b); |
| - |
| multiplication assignment |
| tt | 1=a *= b |
|  |
| c | 1=T& T::operator *=(const T2& b); |
| c | 1=T& operator *=(T& a, const T2& b); |
| - |
| division assignment |
| tt | 1=a /= b |
|  |
| c | 1=T& T::operator /=(const T2& b); |
| c | 1=T& operator /=(T& a, const T2& b); |
| - |
| remainder assignment |
| tt | 1=a %= b |
|  |
| c | 1=T& T::operator %=(const T2& b); |
| c | 1=T& operator %=(T& a, const T2& b); |
| - |
| bitwise AND assignment |
| tt | 1=a &= b |
|  |
| c | 1=T& T::operator &=(const T2& b); |
| c | 1=T& operator &=(T& a, const T2& b); |
| - |
| bitwise OR assignment |
| tt | 1=a &#124;= b |
|  |
| c | 1=T& T::operator |=(const T2& b); |
| c | 1=T& operator |=(T& a, const T2& b); |
| - |
| bitwise XOR assignment |
| tt | 1=a ^= b |
|  |
| c | 1=T& T::operator ^=(const T2& b); |
| c | 1=T& operator ^=(T& a, const T2& b); |
| - |
| bitwise left shift assignment |
| tt | 1=a <<= b |
|  |
| c | 1=T& T::operator <<=(const T2& b); |
| c | 1=T& operator <<=(T& a, const T2& b); |
| - |
| bitwise right shift assignment |
| tt | 1=a >>= b |
|  |
| c | 1=T& T::operator >>=(const T2& b); |
| c | 1=T& operator >>=(T& a, const T2& b); |
| - |
| colspan="5" |  |


## Definitions

''Copy assignment'' replaces the contents of the object `a` with a copy of the contents of `b` (`b` is not modified). For class types, this is performed in a special member function, described in `copy assignment operator`.
rrev|since=c++11|1=
''Move assignment'' replaces the contents of the object `a` with the contents of `b`, avoiding copying if possible (`b` may be modified). For class types, this is performed in a special member function, described in `move assignment operator`.
For non-class types, copy and move assignment are indistinguishable and are referred to as ''direct assignment''.
''Compound assignment'' replace the contents of the object `a` with the result of a binary operation between the previous value of `a` and the value of `b`.

## Assignment operator syntax

The assignment expressions have the form

**Syntax:**

- `**`=`** *new-value*`

### Parameters

- `{{spar` - target-expr|the expression to be assigned to
- `{{spar` - op|one of `*, `/ `%, `+ `-,  `<<, `>>, `&, `^, `1=
- `{{spar` - new-value|the <sup>(until C++11)</sup> expression*<sup>(since C++11)</sup> `initializer clause` to assign to the target
1. Simple assignment expression.
2. Compound assignment expression.
<sup>(since C++11)</sup> If *new-value is not an expression, the assignment expression will never match an overloaded compound assignment operator.*

## Built-in simple assignment operator

For the built-in simple assignment, *target-expr* must be a modifiable lvalue.
The object referred to by *target-expr* is modified by replacing its value with the result of *new-value*. If the object referred is of an integer type `T`, and the result of *new-value* is of the corresponding signed/unsigned integer type, the value of the object is replaced with the value of type `T` with the same value representation of the result of *new-value*.
The result of a built-in simple assignment is an lvalue of the type of *target-expr*, referring to *target-expr*. If *target-expr* is a `bit-field`, the result is also a bit-field.

### Assignment from an expression

If *new-value* is an expression, it is `implicitly converted` to
the cv-unqualified type of *target-expr*. When *target-expr* is a bit-field that cannot represent the value of the expression, the resulting value of the bit-field is implementation-defined.
If *target-expr* and *new-value* identify overlapping objects, the behavior is undefined (unless the overlap is exact and the type is the same).
rrev|since=c++20|
If the type of *target-expr* is volatile-qualified, the assignment is deprecated, unless the (possibly parenthesized) assignment expression is a `discarded-value expression` or an `unevaluated operand`.
rrev|since=c++11|

### Assignment from a non-expression initializer clause

*new-value* is only allowed not to be an expression in following situations:
* *target-expr* is of a scalar type `T`, and *new-value* is empty or has only one element. In this case, given an invented variable `t` declared and initialized as , the meaning of  is `1=x = t`.
* *target-expr* is of class type. In this case, *new-value* is passed as the argument to the assignment operator function selected by `overload resolution`.

```cpp
#include <complex>

std::complex<double> z;
z = {1, 2};  // meaning z.operator=({1, 2})
z += {1, 2}; // meaning z.operator+=({1, 2})

int a, b;
a = b = {1}; // meaning a = b = 1;
a = {1} = b; // syntax error
```

In `overload resolution against user-defined operators`, for every type `T`, the following function signatures participate in overload resolution:

```cpp
(T*&, T*);
(T*volatile &, T*);
```

For every enumeration or pointer to member type `T`, optionally volatile-qualified, the following function signature participates in overload resolution:

```cpp
(T&, T);
```

For every pair `A1` and `A2`, where `A1` is an arithmetic type (optionally volatile-qualified) and `A2` is a promoted arithmetic type, the following function signature participates in overload resolution:

```cpp
(A1&, A2);
```


## Built-in compound assignment operator

The behavior of every built-in compound-assignment expression  is exactly the same as the behavior of the expression , except that *target-expr* is evaluated only once.
The requirements on *target-expr* and *new-value* of built-in simple assignment operators also apply. Furthermore:
* For `1=+=` and `1=-=`, the type of *target-expr* must be an `arithmetic type` or a pointer to a (possibly cv-qualified) completely-defined `object type`.
* For all other compound assignment operators, the type of *target-expr* must be an arithmetic type.
In `overload resolution against user-defined operators`, for every pair `A1` and `A2`, where `A1` is an arithmetic type (optionally volatile-qualified) and `A2` is a promoted arithmetic type, the following function signatures participate in overload resolution:

```cpp
(A1&, A2);
(A1&, A2);
(A1&, A2);
(A1&, A2);
```

For every pair `I1` and `I2`, where `I1` is an integral type (optionally volatile-qualified) and `I2` is a promoted integral type, the following function signatures participate in overload resolution:

```cpp
(I1&, I2);
(I1&, I2);
(I1&, I2);
(I1&, I2);
(I1&, I2);
(I1&, I2);
```

For every optionally cv-qualified object type `T`, the following function signatures participate in overload resolution:

```cpp
(T*&, std::ptrdiff_t);
(T*&, std::ptrdiff_t);
(T*volatile &, std::ptrdiff_t);
(T*volatile &, std::ptrdiff_t);
```


## Example


### Example

```cpp
#include <iostream>

int main()
{
    int n = 0;        // not an assignment

    n = 1;            // direct assignment
    std::cout << n << ' ';

    n = {};           // zero-initialization, then assignment
    std::cout << n << ' ';

    n = 'a';          // integral promotion, then assignment
    std::cout << n << ' ';

    n = {'b'};        // explicit cast, then assignment
    std::cout << n << ' ';

    n = 1.0;          // floating-point conversion, then assignment
    std::cout << n << ' ';

//  n = {1.0};        // compiler error (narrowing conversion)

    int& r = n;       // not an assignment
    r = 2;            // assignment through reference
    std::cout << n << ' ';

    int* p;
    p = &n;           // direct assignment
    p = nullptr;      // null-pointer conversion, then assignment
    std::cout << p << ' ';

    struct { int a; std::string s; } obj;
    obj = {1, "abc"}; // assignment from a braced-init-list
    std::cout << obj.a << ':' << obj.s << '\n';
}
```


**Output:**
```
1 0 97 98 1 2 (nil) 1:abc
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1527 | C++11 | for assignments to class type objects, the right operand<br>could be an initializer list only when the assignment<br>is defined by a user-defined assignment operator | removed user-defined<br>assignment constraint |
| cwg-2654 | C++20 | compound assignment operators for volatile<br>-qualified types were inconsistently deprecated | none of them<br>is deprecated |
| cwg-2768 | C++11 | an assignment from a non-expression initializer clause<br>to a scalar value would perform direct-list-initialization | performs copy-list-<br>initialization instead |


## See also

`Operator precedence`
`Operator overloading`
