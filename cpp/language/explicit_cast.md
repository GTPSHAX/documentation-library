---
title: Explicit type conversion
type: Language
source: https://en.cppreference.com/w/cpp/language/explicit_cast
---


# Explicit type conversion

Converts between types using a combination of explicit and implicit conversions.

## Syntax


**Syntax:**

- `*type-id* **`)`** *unary-expression*`
- `**`(`** *expression-list* (optional) **`)`**<br>*simple-type-specifier* **`(`** *initializer-list* (optional) **`)`**|notes=<sup>(until C++11)</sup><br><sup>(C++11)</sup>`
- `**`{`** *initializer-list* (optional) }|notes=<sup>(C++11)</sup>`
- `**`{`** *designated-initializer-list* }|notes=<sup>(C++20)</sup>`
- `*identifier* **`(`** *initializer-list* (optional) **`)`**|notes=<sup>(C++11)</sup>`
- `*identifier* **`{`** *initializer-list* (optional) }|notes=<sup>(C++11)</sup>`
- `*identifier* **`{`** *designated-initializer-list* }|notes=<sup>(C++20)</sup>`
Explicitly converts any number of values to a value of the target type.
1. Explicit type conversion (cast notation), also called ''C-style cast''.
@2-7@ Explicit type conversion (functional notation), also called ''function-style cast''.

### Parameters

- `{{spar` - type-id|a `type-id`
- `{{spar` - unary-expression|an unary expression (whose top-level operator does not have a `precedence` higher than that of C-style cast)
- `{{spar` - simple-type-specifier|a `simple type specifier`
- `{{spar` - expression-list|a comma-separated list of expressions (except unparenthesized `comma expressions`)
- `{{spar` - initializer-list|a comma-separated list of `initializer clauses`
- `{{spar` - designated-initializer-list|a comma-separated list of `designated initializer clauses`
- `{{spar` - identifier|a (possibly qualified) identifier (including )

## Explanation

1. When the C-style cast is encountered, the compiler attempts to interpret it as the following cast expressions, in this order:
:@a@ ;
:@b@ , with extensions: pointer or reference to a `derived class` is additionally allowed to be cast to pointer or reference to unambiguous base class (and vice versa) even if the base class is `inaccessible` (that is, this cast ignores the private inheritance specifier). Same applies to casting `pointer to member` to pointer to member of unambiguous non-virtual base;
:@c@ a `static_cast` (with extensions) followed by `const_cast`;
:@d@ ;
:@e@ a `reinterpret_cast` followed by `const_cast`.
@@ The first choice that satisfies the requirements of the respective cast operator is selected, even if it is ill-formed (see example). If a `static_cast` followed by a `const_cast` is used and the conversion can be interpreted in more than one way as such, the conversion is ill-formed.
@@ In addition, C-style casts can cast from, to, and between pointers to incomplete class type. If both *type-id* and the type of *unary-expression* are pointers to incomplete class types, it is unspecified whether `static_cast` or `reinterpret_cast` gets selected.
@2-7@ A function-style cast specifies a '''type''' (simple-type-specifier<sup>(since C++11)</sup>  or identifier) and an '''initializer''' (the remaining parts), it constructs a value of the target type `T`, which is determined from the specified type<sup>(since C++17)</sup>  and initializer:
rev|until=c++17|
`T` is the specified type.
rev|since=c++17|
`T` is determined as follows:
* If the specified type is a placeholder for a deduced class type, `T` is the return type of the function selected by overload resolution for `class template deduction`.
rrev|since=c++23|
* Otherwise, if the specified type contains a `placeholder type`, `T` is the deduced type.
* Otherwise, `T` is the specified type.
@@ The conversion result is determined as follows:
* If the function-style cast is of syntax , and there is exactly one expression in parentheses, this cast is equivalent to the corresponding C-style cast.
* Otherwise, if `T` is (possibly cv-qualified) `void`, the result is <sup>(until C++11)</sup> an rvalue<sup>(since C++11)</sup> a prvalue of type `void` that performs no initialization.
rev|until=c++11|
:* If the initializer is not `()`, the program is ill-formed.
rev|since=c++11|
:* If the initializer is not `()` or } after `pack expansion` (if any), the program is ill-formed.
* Otherwise, if `T` is a reference type, the function-style cast has the same effect as `direct-initializing` an invented variable `t` of type `T` from the specified initializer, and the result is the initialized `t`.
rev|until=c++11|
:* The result is an lvalue.
rev|since=c++11|
:* If `T` is an lvalue reference type or an rvalue reference to function type, the result is an lvalue.
:* Otherwise, the result is an xvalue.
* Otherwise, the result is <sup>(until C++11)</sup> an rvalue<sup>(since C++11)</sup> a prvalue of of type `T` <sup>(until C++17)</sup> designating a temporary<sup>(since C++17)</sup> whose result object is `direct-initialized` with the specified initializer.

## Ambiguity Resolution


### Ambiguous declaration statement

In the case of an ambiguity between an expression statement with a function-style cast expression as its leftmost subexpression and a declaration statement, the ambiguity is resolved by treating it as a declaration. This disambiguation is purely syntactic: it does not consider the meaning of names occurring in the statement other than whether they are type names:

```cpp
struct M {};
struct L { L(M&); };

M n;
void f()
{
    M(m);    // declaration, equivalent to M m;
    L(n);    // ill-formed declaration, equivalent to L n;
    L(l)(m); // still a declaration, equivalent to L l((m));
}
```

rrev|since=c++11|
However, if the outermost declarator in the ambiguous declaration statement has a `trailing return type`, the statement will only be treated as a declaration statement if the trailing return type starts with `auto`:

```cpp
struct M;

struct S
{
    S* operator()();
    int N;
    int M;

    void mem(S s)
    {
        auto(s)()->M; // expression (S::M hides ::M), invalid before C++23
    }
};

void f(S s)
{
    {
        auto(s)()->N; // expression, invalid before C++23
        auto(s)()->M; // function declaration, equivalent to M s();
    }
    {
        S(s)()->N;    // expression
        S(s)()->M;    // expression
    }
}
```


### Ambiguous function parameter

The ambiguity above can also occur in the context of a declaration. In that context, the choice is between an object declaration with a function-style cast as the initializer and a declaration involving a function declarator with a redundant set of parentheses around a parameter name. The resolution is also to consider any construct, such as the potential parameter declaration, that could possibly be a declaration to be a declaration:

```cpp
struct S
{
    S(int);
};

void foo(double a)
{
    S w(int(a)); // function declaration: has a parameter `a` of type int
    S x(int());  // function declaration: has an unnamed parameter of type int(*)() 
                 // that is adjusted from int()

    // Ways to avoid ambiguity:
    S y((int(a))); // object declaration: extra pair of parentheses
    S y((int)a);   // object declaration: C-style cast
    S z = int(a);  // object declaration: no ambiguity for this syntax
}
```

rrev|since=c++11|
However, if the outermost declarator in the ambiguous parameter declaration has a `trailing return type`, the ambiguity will only be resolved by treating it as a declaration if it starts with `auto`:

```cpp
typedef struct BB { int C[2]; } *B, C;

void foo()
{
    S a(B()->C);    // object declaration: B()->C cannot declare a parameter
    S b(auto()->C); // function declaration: has an unnamed parameter of type C(*)()
                    // that is adjusted from C()
}
```


### Ambiguous type-id

An ambiguity can arise from the similarity between a function-style cast and a `type-id`. The resolution is that any construct that could possibly be a type-id in its syntactic context shall be considered a type-id:

```cpp
// `int()` and `int(unsigned(a))` can both be parsed as type-id:
// `int()`            represents a function returning int
//                    and taking no argument
// `int(unsigned(a))` represents a function returning int
//                    and taking an argument of type unsigned
void foo(signed char a)
{
    sizeof(int());            // type-id (ill-formed)
    sizeof(int(a));           // expression
    sizeof(int(unsigned(a))); // type-id (ill-formed)

    (int()) + 1;            // type-id (ill-formed)
    (int(a)) + 1;           // expression
    (int(unsigned(a))) + 1; // type-id (ill-formed)
}
```

rrev|since=c++11|
However, if the outermost *abstract-declarator* in the ambiguous `type-id` has a `trailing return type`, the ambiguity will only be resolved by treating it as a type-id if it starts with `auto`:

```cpp
typedef struct BB { int C[2]; } *B, C;

void foo()
{
    sizeof(B()->C[1]);    // OK, sizeof(expression)
    sizeof(auto()->C[1]); // error: sizeof of a function returning an array
}
```


## Notes

feature test macro|__cpp_auto_cast|`auto(x)` and }|value=202110L|std=C++23

## Example


### Example

```cpp
#include <cassert>
#include <iostream>

double f = 3.14;
unsigned int n1 = (unsigned int)f; // C-style cast
unsigned int n2 = unsigned(f);     // function-style cast

class C1;
class C2;
C2* foo(C1* p)
{
    return (C2*)p; // casts incomplete type to incomplete type
}

void cpp23_decay_copy_demo()
{
    auto inc_print = [](int& x, const int& y)
    {
        ++x;
        std::cout << "x:" << x << ", y:" << y << '\n';
    };

    int p{1};
    inc_print(p, p); // prints x:2 y:2, because param y here is an alias of p
    int q{1};
    inc_print(q, auto{q}); // prints x:2 y:1, auto{q} (C++23) casts to prvalue,
                           // so the param y is a copy of q (not an alias of q)
}

// In this example, C-style cast is interpreted as static_cast
// even though it would work as reinterpret_cast
struct A {};
struct I1 : A {};
struct I2 : A {};
struct D : I1, I2 {};

int main()
{
    D* d = nullptr;
//  A* a = (A*)d;                   // compile-time error
    A* a = reinterpret_cast<A*>(d); // this compiles
    assert(a == nullptr);

    cpp23_decay_copy_demo();
}
```


**Output:**
```
x:2 y:2
x:2 y:1
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1893 | C++11 | function-style cast did not consider pack expansions | considers them |
| cwg-2620 | C++98 | the resolution of ambiguous function<br>parameters might be misinterpreted | improved the wording |
| cwg-2894 | C++98 | function-style casts could create reference rvalues | can only create reference lvalues |


## References


## See also


| cpp/language/dsc const_cast | (see dedicated page) |
| cpp/language/dsc static_cast | (see dedicated page) |
| cpp/language/dsc dynamic_cast | (see dedicated page) |
| cpp/language/dsc reinterpret_cast | (see dedicated page) |
| cpp/language/dsc implicit cast | (see dedicated page) |

