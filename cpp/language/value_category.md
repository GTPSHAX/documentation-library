---
title: Value categories
type: Language
source: https://en.cppreference.com/w/cpp/language/value_category
---


# Value categories

Each C++ `expression` (an operator with its operands, a literal, a variable name, etc.) is characterized by two independent properties: a ''`type`'' and a ''value category''. Each expression has some non-reference type, and each expression belongs to exactly one of the three primary value categories: ''prvalue'', ''xvalue'', and ''lvalue''.
* a  (“generalized” lvalue) is an expression whose evaluation determines the identity of an object or function;
* a  (“pure” rvalue) is an expression whose evaluation
:* computes the value of an operand of a built-in operator (such prvalue has no ''result object''), or
:* initializes an object (such prvalue is said to have a ''result object'').
:: The result object may be a variable, an object created by `new-expression`, a temporary created by , or a member thereof. Note that non-`void` `discarded` expressions have a result object (the materialized temporary). Also, every class and array prvalue has a result object except when it is the operand of `decltype`;
* an  (an “eXpiring” value) is a glvalue that denotes an object whose resources can be reused;
* an  is a glvalue that is not an xvalue;
So-called, historically, because lvalues could appear on the left-hand side of an assignment expression. In general, it's not always the case:

```cpp
void foo();

void baz()
{
    int a; // Expression `a` is lvalue
    a = 4; // OK, could appear on the left-hand side of an assignment expression

    int &b{a}; // Expression `b` is lvalue
    b = 5; // OK, could appear on the left-hand side of an assignment expression

    const int &c{a}; // Expression `c` is lvalue
    c = 6;           // ill-formed, assignment of read-only reference

    // Expression `foo` is lvalue
    // address may be taken by built-in address-of operator
    void (*p)() = &foo;

    foo = baz; // ill-formed, assignment of function
}
```

* an  is a prvalue or an xvalue;
So-called, historically, because rvalues could appear on the right-hand side of an assignment expression. In general, it's not always the case:

### Example

```cpp
#include <iostream>

struct S
{
    S() : m{42} {}
    S(int a) : m{a} {}
    int m;
};

int main()
{
    S s;

    // Expression `S{}` is prvalue
    // May appear on the right-hand side of an assignment expression
    s = S{};

    std::cout << s.m << '\n';

    // Expression `S{}` is prvalue
    // Can be used on the left-hand side too
    std::cout << (S{} = S{7}).m << '\n';
}
```


**Output:**
```
42
7
```

Note: this taxonomy went through significant changes with past C++ standard revisions, see  below for details.
Despite their names, these terms classify expressions, not values.

### Example

```cpp
#include <type_traits>
#include <utility>

template <class T> struct is_prvalue : std::true_type {};
template <class T> struct is_prvalue<T&> : std::false_type {};
template <class T> struct is_prvalue<T&&> : std::false_type {};

template <class T> struct is_lvalue : std::false_type {};
template <class T> struct is_lvalue<T&> : std::true_type {};
template <class T> struct is_lvalue<T&&> : std::false_type {};

template <class T> struct is_xvalue : std::false_type {};
template <class T> struct is_xvalue<T&> : std::false_type {};
template <class T> struct is_xvalue<T&&> : std::true_type {};

int main()
{
    int a{42};
    int& b{a};
    int&& r{std::move(a)};

    // Expression `42` is prvalue
    static_assert(is_prvalue<decltype((42))>::value);

    // Expression `a` is lvalue
    static_assert(is_lvalue<decltype((a))>::value);

    // Expression `b` is lvalue
    static_assert(is_lvalue<decltype((b))>::value);

    // Expression `std::move(a)` is xvalue
    static_assert(is_xvalue<decltype((std::move(a)))>::value);

    // Type of variable `r` is rvalue reference
    static_assert(std::is_rvalue_reference<decltype(r)>::value);

    // Type of variable `b` is lvalue reference
    static_assert(std::is_lvalue_reference<decltype(b)>::value);

    // Expression `r` is lvalue
    static_assert(is_lvalue<decltype((r))>::value);
}
```


## Primary categories


### lvalue

The following expressions are ''lvalue expressions'':
* the name of a variable, a function<sup>(since C++20)</sup> , a `template parameter object`, or a data member, regardless of type, such as `std::cin` or `std::endl`. Even if the variable's type is rvalue reference, the expression consisting of its name is an lvalue expression (but see );

```cpp
void foo() {}

void baz()
{
    // `foo` is lvalue
    // address may be taken by built-in address-of operator
    void (*p)() = &foo;
}
```


```cpp
struct foo {};

template <foo a>
void baz()
{
    const foo* obj = &a;  // `a` is an lvalue, template parameter object
}
```

* a function call or an overloaded operator expression, whose return type is lvalue reference, such as `std::getline(std::cin, str)`, `std::cout << 1`, `1=str1 = str2`, or `++it`;

```cpp
int& a_ref()
{
    static int a{3};
    return a;
}

void foo()
{
    a_ref() = 5;  // `a_ref()` is lvalue, function call whose return type is lvalue reference
}
```

* `1=a = b`, `1=a += b`, `1=a %= b`, and all other built-in `assignment and compound assignment` expressions;
* `++a` and `--a`, the built-in `pre-increment and pre-decrement` expressions;
* `*p`, the built-in `indirection` expression;
* `a[n]` and `p[n]`, the built-in `subscript` expressions<sup>(since C++11)</sup> , where one operand in `a[n]` is an array lvalue;
* `a.m`, the `member of object` expression, except where `m` is a member enumerator or a non-static member function, or where `a` is an rvalue and `m` is a non-static data member of object type;

```cpp
struct foo
{
    enum bar
    {
        m // member enumerator
    };
};

void baz()
{
    foo a;
    a.m = 42; // ill-formed, lvalue required as left operand of assignment
}
```


```cpp
struct foo
{
    void m() {} // non-static member function
};

void baz()
{
    foo a;

    // `a.m` is a prvalue, hence the address cannot be taken by built-in
    // address-of operator
    void (foo::*p1)() = &a.m; // ill-formed

    void (foo::*p2)() = &foo::m; // OK: pointer to member function
}
```


```cpp
struct foo
{
    static void m() {} // static member function
};

void baz()
{
    foo a;
    void (*p1)() = &a.m;     // `a.m` is an lvalue
    void (*p2)() = &foo::m;  // the same
}
```

* `p->m`, the built-in `member of pointer` expression, except where `m` is a member enumerator or a non-static member function;
* `a.*mp`, the `pointer to member of object` expression, where `a` is an lvalue and `mp` is a pointer to data member;
* `p->*mp`, the built-in `pointer to member of pointer` expression, where `mp` is a pointer to data member;
* `a, b`, the built-in `comma` expression, where `b` is an lvalue;
* `a ? b : c`, the `ternary conditional` expression for certain `b` and `c` (e.g., when both are lvalues of the same type, but see `definition` for detail);
* a `string literal`, such as `"Hello, world!"`;
* a cast expression to lvalue reference type, such as `static_cast<int&>(x)` or `static_cast<void(&)(int)>(x)`;
* a non-type `template parameter` of an lvalue reference type;

```cpp
template <int& v>
void set()
{
    v = 5; // template parameter is lvalue
}

int a{3}; // static variable, fixed address is known at compile-time

void foo()
{
    set<a>();
}
```

rrev|since=c++11|
* a function call or an overloaded operator expression, whose return type is rvalue reference to function;
* a cast expression to rvalue reference to function type, such as `static_cast<void(&&)(int)>(x)`.
Properties:
* Same as  (below).
* Address of an lvalue may be taken by built-in address-of operator: `&++i` and `&std::endl` are valid expressions.
* A modifiable lvalue may be used as the left-hand operand of the built-in assignment and compound assignment operators.
* An lvalue may be used to `initialize an lvalue reference`; this associates a new name with the object identified by the expression.

### prvalue

The following expressions are ''prvalue expressions'':
* a `literal` (except for `string literal`), such as `42`, `true` or `nullptr`;
* a function call or an overloaded operator expression, whose return type is non-reference, such as `str.substr(1, 2)`, `str1 + str2`, or `it++`;
* `a++` and `a--`, the built-in  `post-increment and post-decrement` expressions;
* `a + b`, `a % b`, `a & b`, `a << b`, and all other built-in `arithmetic` expressions;
* `a && b`, `a , `!a`, the built-in `logical` expressions;
* `a < b`, `1=a == b`, `1=a >= b`, and all other built-in `comparison` expressions;
* `&a`, the built-in `address-of` expression;
* `a.m`, the `member of object` expression, where `m` is a member enumerator or a non-static member function;
* `p->m`, the built-in `member of pointer` expression, where `m` is a member enumerator or a non-static member function<ref name=pmfc/>;
* `a.*mp`, the `pointer to member of object` expression, where `mp` is a pointer to member function<ref name=pmfc/>;
* `p->*mp`, the built-in `pointer to member of pointer` expression, where `mp` is a pointer to member function<ref name=pmfc/>;
* `a, b`, the built-in `comma` expression, where `b` is an prvalue;
* `a ? b : c`, the `ternary conditional` expression for certain `b` and `c` (see `definition` for detail);
* a cast expression to non-reference type, such as `static_cast<double>(x)`, }, or `(int)42`;
* the `this` pointer;
* an `enumerator`;
* a non-type `template parameter` of a scalar type;

```cpp
template <int v>
void foo()
{
    // not an lvalue, `v` is a template parameter of scalar type int
    const int* a = &v; // ill-formed

    v = 3; // ill-formed: lvalue required as left operand of assignment
}
```

rev|since=c++11|
* a `lambda expression`, such as };
rev|since=c++20|
* a `requires-expression`, such as };
* a specialization of a `concept`, such as `std::equality_comparable<int>`.
Properties:
* Same as  (below).
* A prvalue cannot be `polymorphic`: the  of the object it denotes is always the type of the expression.
* A non-class non-array prvalue cannot be `cv-qualified`<sup>(since C++17)</sup> , unless it is `materialized in order to be `reference initialization|bound to a reference` to a cv-qualified type`. (Note: a function call or cast expression may result in a prvalue of non-class cv-qualified type, but the cv-qualifier is generally immediately stripped out.)
* A prvalue cannot have  (except for type `void`, see below, or when used in `decltype` specifier).
* A prvalue cannot have `abstract class type` or an array thereof.

### xvalue

The following expressions are ''xvalue expressions'':
* `a.m`, the `member of object` expression, where `a` is an rvalue and `m` is a non-static data member of an object type;
* `a.*mp`, the `pointer to member of object` expression, where `a` is an rvalue and `mp` is a pointer to data member;
* `a, b`, the built-in `comma` expression, where `b` is an xvalue;
* `a ? b : c`, the `ternary conditional` expression for certain `b` and `c` (see `definition` for detail);
rev|since=c++11|
* a function call or an overloaded operator expression, whose return type is rvalue reference to object, such as `std::move(x)`;
* `a[n]`, the built-in `subscript` expression, where one operand is an array rvalue;
* a cast expression to rvalue reference to object type, such as `static_cast<char&&>(x)`;
rev|since=c++17|
* any expression that designates a temporary object, after ;
rev|since=c++23|
* a move-eligible expression.
Properties:
* Same as rvalue (below).
* Same as glvalue (below).
In particular, like all rvalues, xvalues bind to rvalue references, and like all glvalues, xvalues may be `polymorphic`, and non-class xvalues may be `cv-qualified`.

### Example

```cpp
#include <type_traits>

template <class T> struct is_prvalue : std::true_type {};
template <class T> struct is_prvalue<T&> : std::false_type {};
template <class T> struct is_prvalue<T&&> : std::false_type {};

template <class T> struct is_lvalue : std::false_type {};
template <class T> struct is_lvalue<T&> : std::true_type {};
template <class T> struct is_lvalue<T&&> : std::false_type {};

template <class T> struct is_xvalue : std::false_type {};
template <class T> struct is_xvalue<T&> : std::false_type {};
template <class T> struct is_xvalue<T&&> : std::true_type {};

// Example from C++23 standard: 7.2.1 Value category [basic.lval]
struct A
{
    int m;
};

A&& operator+(A, A);
A&& f();

int main()
{
    A a;
    A&& ar = static_cast<A&&>(a);

    // Function call with return type rvalue reference is xvalue
    static_assert(is_xvalue<decltype( (f()) )>::value);

    // Member of object expression, object is xvalue, `m` is a non-static data member
    static_assert(is_xvalue<decltype( (f().m) )>::value);

    // A cast expression to rvalue reference
    static_assert(is_xvalue<decltype( (static_cast<A&&>(a)) )>::value);

    // Operator expression, whose return type is rvalue reference to object
    static_assert(is_xvalue<decltype( (a + a) )>::value);

    // Expression `ar` is lvalue, `&ar` is valid
    static_assert(is_lvalue<decltype( (ar) )>::value);
    [[maybe_unused]] A* ap = &ar;
}
```


## Mixed categories


### glvalue

A ''glvalue expression'' is either lvalue or xvalue.
Properties:
* A glvalue may be implicitly converted to a prvalue with lvalue-to-rvalue, array-to-pointer, or function-to-pointer `implicit conversion`.
* A glvalue may be `polymorphic`: the  of the object it identifies is not necessarily the static type of the expression.
* A glvalue can have , where permitted by the expression.

### rvalue

An ''rvalue expression'' is either prvalue or xvalue.
Properties:
* Address of an rvalue cannot be taken by built-in address-of operator: `&int()`, `&i++`, `&42`, and `&std::move(x)` are invalid.
* An rvalue can't be used as the left-hand operand of the built-in assignment or compound assignment operators.
* An rvalue may be used to `initialize a const lvalue reference`, in which case the lifetime of the temporary object identified by the rvalue is `extended` until the scope of the reference ends.
rrev|since=c++11|
* An rvalue may be used to `initialize an rvalue reference`, in which case the lifetime of the temporary object identified by the rvalue is `extended` until the scope of the reference ends.
* When used as a function argument and when `two overloads` of the function are available, one taking rvalue reference parameter and the other taking lvalue reference to const parameter, an rvalue binds to the rvalue reference overload (thus, if both copy and move constructors are available, an rvalue argument invokes the `move constructor`, and likewise with copy and move assignment operators).

## Special categories


### Pending member function call

The expressions `a.mf` and `p->mf`, where `mf` is a `non-static member function`, and the expressions `a.*pmf` and `p->*pmf`, where `pmf` is a `pointer to member function`, are classified as prvalue expressions, but they cannot be used to initialize references, as function arguments, or for any purpose at all, except as the left-hand argument of the function call operator, e.g. `(p->*pmf)(args)`.

### Void expressions

Function call expressions returning `void`, cast expressions to `void`, and `throw-expressions` are classified as prvalue expressions, but they cannot be used to initialize references or as function arguments. They can be used in discarded-value contexts (e.g. on a line of its own, as the left-hand operand of the comma operator, etc.) and in the `return` statement in a function returning `void`. In addition, throw-expressions may be used as the second and the third operands of the `conditional operator ?:`.
rrev|since=c++17|
Void expressions have no ''result object''.

### Bit-fields

An expression that designates a `bit-field` (e.g. `a.m`, where `a` is an lvalue of type }) is a glvalue expression: it may be used as the left-hand operand of the assignment operator, but its address cannot be taken and a non-const lvalue reference cannot be bound to it. A const lvalue reference or rvalue reference can be initialized from a bit-field glvalue, but a temporary copy of the bit-field will be made: it won't bind to the bit-field directly.
rrev|since=c++11|

### Move-eligible expressions

Although an expression consisting of the name of any variable is an lvalue expression, such expression may be move-eligible if it appears as the operand of
* a `return` statement
* a `co_return` statement <sup>(C++20)</sup>
* a `throw` expression <sup>(C++17)</sup>
If an expression is move-eligible, it is treated <sup>(until C++23)</sup> either as an rvalue or as an lvalue<sup>(since C++23)</sup> as an rvalue for the purpose of `overload resolution`  (thus it may select the `move constructor`). See  for details.

## History


### CPL

The programming language CPL was first to introduce value categories for expressions: all CPL expressions can be evaluated in "right-hand mode", but only certain kinds of expression are meaningful in "left-hand mode". When evaluated in right-hand mode, an expression is regarded as being a rule for the computation of a value (the right-hand value, or ''rvalue''). When evaluated in left-hand mode an expression effectively gives an address (the left-hand value, or ''lvalue''). "Left" and "Right" here stood for "left of assignment" and "right of assignment".

### C

The C programming language followed a similar taxonomy, except that the role of assignment was no longer significant: C expressions are categorized between "lvalue expressions" and others (functions and non-object values), where "lvalue" means an expression that identifies an object, a "locator value".

### C++98

Pre-2011 C++ followed the C model, but restored the name "rvalue" to non-lvalue expressions, made functions into lvalues, and added the rule that references can bind to lvalues, but only references to const can bind to rvalues. Several non-lvalue C expressions became lvalue expressions in C++.

### C++11

With the introduction of move semantics in C++11, value categories were redefined to characterize two independent properties of expressions:
* ''has identity'': it's possible to determine whether the expression refers to the same entity as another expression, such as by comparing addresses of the objects or the functions they identify (obtained directly or indirectly);
* ''can be moved from'': `move constructor`, `move assignment operator`, or another function overload that implements move semantics can bind to the expression.
In C++11, expressions that:
* have identity and cannot be moved from are called ''lvalue'' expressions;
* have identity and can be moved from are called ''xvalue'' expressions;
* do not have identity and can be moved from are called ''prvalue'' ("pure rvalue") expressions;
* do not have identity and cannot be moved from are not used.
The expressions that have identity are called "glvalue expressions" (glvalue stands for "generalized lvalue"). Both lvalues and xvalues are glvalue expressions.
The expressions that can be moved from are called "rvalue expressions". Both prvalues and xvalues are rvalue expressions.

### C++17

In C++17, `copy elision` was made mandatory in some situations, and that required separation of prvalue expressions from the temporary objects initialized by them, resulting in the system we have today. Note that, in contrast with the C++11 scheme, prvalues are no longer moved from.

## Footnotes


## References


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-616 | C++11 | member access and member access through<br>pointer to member of an rvalue resulted in prvalue | reclassified as xvalue |
| cwg-1059 | C++11 | array prvalues could not be cv-qualified | allowed |
| cwg-1213 | C++11 | subscripting an array rvalue resulted in  lvalue | reclassified as xvalue |


## See also


## External links

