---
title: Conflicting declarations
type: Language
source: https://en.cppreference.com/w/cpp/language/conflicting_declarations
---


# Conflicting declarations

Unless otherwise specified, two declarations cannot (re)introduce the same entity. The program is ill-formed if such declarations exist.

## Corresponding declarations

Two declarations ''correspond'' if they (re)introduce the same name, both declare constructors, or both declare destructors, unless
* either is a ``using` declaration`,
* one declares a type (not a `typedef name`) and the other declares a variable, non-static data member other than of an `anonymous union`, enumerator, function, or function template, or
* each declares a function or function template and they do not declare corresponding overloads.

### Corresponding function overloads

Two `function declarations` declare ''corresponding overloads'' if both declare functions satisfying all following conditions:
* They have the same <sup>(since C++23)</sup> , omitting the types of .
rrev|since=c++20|
* They have `equivalent` trailing ``requires` clauses` (if any, except `friend declarations`).
* If both of them are non-static member functions, they need to additionally satisfy one of the following requirements:
rrev|since=c++23|
:* Exactly one of them is an `implicit object member function` without ref-qualifier and the types of their object parameters, after removing top-level references, are the same.
:* Their object parameters have the same type.

### Corresponding function template overloads

Two `function template declarations` declare ''corresponding overloads'' if both declare function templates satisfying all following conditions:
* Their template parameter lists have the same length.
* Their corresponding template parameters are `equivalent`.
* They have equivalent s<sup>(since C++23)</sup> , omitting the types of .
* They have equivalent return types.
rrev|since=c++20|
* Their corresponding template parameters are either both declared without `constraint`, or both declared with equivalent constraints.
* They have equivalent trailing ``requires` clauses` (if any).
* If both are non-static members function templates, they need to additionally satisfy one of the following requirements:
rrev|since=c++23|
:* Exactly one of them is an `implicit object member function` template without ref-qualifier and the types of their object parameters, after removing all references, are equivalent.
:* Their object parameters have equivalent types.

```cpp
struct A
{
    friend void c();   // #1
};

struct B
{
    friend void c() {} // corresponds to, and defines, #1
};

typedef int Int;

enum E : int { a };

void f(int);   // #2
void f(Int) {} // defines #2
void f(E) {}   // OK, another overload

struct X
{
    static void f();
    void f() const;   // error: redeclaration

    void g();
    void g() const;   // OK
    void g() &;       // error: redeclaration

    void h(this X&, int);
    void h(int) &&;   // OK, another overload

    void j(this const X&);
    void j() const &; // error: redeclaration

    void k();
    void k(this X&);  // error: redeclaration
};
```


## Multiple declarations of the same entity

rrev|since=c++26|
A declaration is ''name-independent'' if its name is `_` and it declares
* a variable with automatic `storage duration`,
* a `structured binding` with no `storage class specifier` and not `inhabiting` a namespace scope,
* a `result binding`,
* the variable introduced by a  with an initializer, or
* a non-static `data member` of other than an `anonymous union`.
Unless otherwise specified, two declarations of entities ''declare the same entity'' if all following conditions are satisfied, considering declarations of unnamed types to introduce their `typedef names` and `enumeration names` for linkage purposes (if any exists):
* They correspond.
* They have the same `target scope`, which is not a  or a .
rrev|since=c++26|
* Neither is a name-independent declaration.
* One of the following conditions is satisfied:
:* They appear in the same translation unit.
rrev|since=c++20|
:* They both declare names with  and are `attached to the same module`.
:* They both declare names with .
A declaration of an entity or typedef name `X` is a ''redeclaration'' of `X` if another declaration of `X` is reachable from it; otherwise, it is a  of `X`.

### Restrictions

If any two declarations of an entity `E` violate the corresponding restriction below, the program is ill-formed:
* If one declares `E` to be a variable, the other must also declare `E` as a variable of the same type.
* If one declares `E` to be a `function`, the other must also declare `E` as a function of the same type.
* If one declares `E` to be an `enumerator`, the other must also declare `E` as an enumerator.
* If one declares `E` to be a `namespace`, the other must also declare `E` as a namespace.
* If one declares `E` to be a `class type`, the other must also declare `E` as a class type.
* If one declares `E` to be an `enumeration type`, the other must also declare `E` as an enumeration type.
* If one declares `E` to be a `class template`, the other must also declare `E` as a class template with an equivalent template parameter list (see ).
* If one declares `E` to be a `function template`, the other must also declare `E` as a function template with an equivalent template parameter list and type.
rev|since=c++11|
* If one declares `E` to be an `alias template`, the other must also declare `E` as an alias template with an equivalent template parameter list and *type-id*.
rev|since=c++14|
* If one declares `E` to be a (partial specialization of a) `variable template`, the other must also declare `E` as a (partial specialization of a) variable template with an equivalent template parameter list and type.
rev|since=c++20|
* If one declares `E` to be a `concept`, the other must also declare `E` as a concept.
Types are compared after all adjustments of types (during which `typedefs` are replaced by their definitions). Declarations for an array object can specify array types that differ by the presence or absence of a major array bound. No diagnostic is required if neither declaration is reachable from the other.

```cpp
void g();      // #1
void g(int);   // OK, different entity from #1 (they do not correspond)
int g();       // Error: same entity as #1 with different type

void h();      // #2
namespace h {} // Error: same entity as #2, but not a function
```

If a declaration `H` that declares a name with  precedes a declaration `D` in another translation unit `U` and would declare the same entity as `D` if it appeared in `U`, the program is ill-formed.

## Potentially-conflicting declarations

Two declarations ''potentially conflict'' if they correspond but declare different entities.
If, in any scope, a name is bound to two declarations `A` and `B` that potentially conflict<sup>(since C++26)</sup> , `B` is not name-independent, and `A` precedes `B`, the program is ill-formed:

```cpp
void f()
{
    int x, y;
    void x(); // Error: different entity for x
    int y;    // Error: redefinition
}

enum { f };   // Error: different entity for ::f

namespace A {}
namespace B = A;
namespace B = A; // OK, no effect
namespace B = B; // OK, no effect
namespace A = B; // OK, no effect
namespace B {}   // Error: different entity for B

void g()
{
    int _;
    _ = 0; // OK
    int _; // OK since C++26, name-independent declaration
    _ = 0; // Error: two non-function declarations in the lookup set
}

void h ()
{
    int _;        // #1
    _ ++;         // OK
    static int _; // Error: conflicts with #1 because
                  // static variables are not name-independent
}
```


## Defect reports

