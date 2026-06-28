---
title: Definitions and ODR
type: Language
source: https://en.cppreference.com/w/cpp/language/definition
---


# Definitions and ODR (One Definition Rule)

''Definitions'' are `declarations` that fully define the entity introduced by the declaration. Every declaration is a definition, except for the following:
* A function declaration without a function body:

```cpp
int f(int); // declares, but does not define f
```

* Any declaration with an `extern` `storage class specifier` or with a `language linkage` specifier (such as `extern "C"`) without an initializer:

```cpp
extern const int a;     // declares, but does not define a
extern const int b = 1; // defines b
```

* Declaration of a <sup>(since C++17)</sup> non-inline `static data member` inside a class definition:

```cpp
struct S
{
    int n;               // defines S::n
    static int i;        // declares, but does not define S::i
    inline static int x; // defines S::x
};                       // defines S

int S::i;                // defines S::i
```

rrev|since=c++17|
*  Namespace scope declaration of a static data member that was defined within the class with the `constexpr` specifier:

```cpp
struct S
{
    static constexpr int x = 42; // implicitly inline, defines S::x
};

constexpr int S::x; // declares S::x, not a redefinition
```

* Declaration of a class name (by  or by the use of the elaborated type specifier in another declaration):

```cpp
struct S;             // declares, but does not define S

class Y f(class T p); // declares, but does not define Y and T (and also f and p)
```

rrev|since=c++11|
* An `opaque declaration` of an enumeration:

```cpp
enum Color : int; // declares, but does not define Color
```

* Declaration of a `template parameter`:

```cpp
template<typename T> // declares, but does not define T
```

* A parameter declaration in a function declaration that isn't a definition:

```cpp
int f(int x); // declares, but does not define f and x

int f(int x)  // defines f and x
{
    return x + a;
}
```

* A `typedef` declaration:

```cpp
typedef S S2; // declares, but does not define S2 (S may be incomplete)
```

rrev|since=c++11|
* An `alias-declaration`:

```cpp
using S2 = S; // declares, but does not define S2 (S may be incomplete)
```

* A `using-declaration`:

```cpp
using N::d; // declares, but does not define d
```

rev|since=c++17|
* Declaration of a `deduction guide` (does not define any entities)
rev|since=c++11|
* A `static_assert` declaration (does not define any entities)
* An `attribute declaration` (does not define any entities)
* An `empty declaration` (does not define any entities)
* A `using-directive` (does not define any entities)
rrev|since=c++11|
* An `explicit instantiation declaration` (an "extern template"):

```cpp
extern template
f<int, char>; // declares, but does not define f<int, char>
```

* An `explicit specialization` whose declaration is not a definition:

```cpp
template<>
struct A<int>; // declares, but does not define A<int>
```

An `asm declaration` does not define any entities, but it is classified as a definition.
Where necessary, the compiler may implicitly define the `default constructor`, `copy constructor`, `move constructor`, `copy assignment operator`, `move assignment operator`, and the `destructor`.
If the definition of any object results in an object of `incomplete type` or `abstract class type`, the program is ill-formed.

## One Definition Rule

Only one definition of any variable, function, class type, enumeration type<sup>(since C++20)</sup> `, concept` or template is allowed in any one translation unit (some of these may have multiple declarations, but only one definition is allowed).
One and only one definition of every non-`inline` function or variable that is ''odr-used'' (see below) is required to appear in the entire program (including any standard and user-defined libraries). The compiler is not required to diagnose this violation, but the behavior of the program that violates it is undefined.
For an inline function<sup>(since C++17)</sup>  or inline variable, a definition is required in every translation unit where it is ''odr-used''.
For a class, a definition is required wherever the class is used in a way that requires it to be `complete`.
There can be more than one definition in a program of each of the following: class type, enumeration type, inline function<sup>(since C++17)</sup> , inline variable,  (template or member of template, but not full `template specialization`), as long as all following conditions are satisfied:
* Each definition appears in a different translation unit.
rrev|since=c++20|
* The definitions are not `attached to a named module`.
* Each definition consists of the same sequence of  (typically, appears in the same header).
* Name lookup from within each definition finds the same entities (after `overload resolution`), except that:
:* Constants with internal or no linkage may refer to different objects as long as they are not odr-used and have the same values in every definition.
rrev|since=c++11|
:* `Lambda expressions` that are not in a default argument<sup>(since C++20)</sup>  or a default template argument are uniquely identified by the sequence of tokens used to define them.
* Overloaded operators, including conversion, allocation, and deallocation functions refer to the same function from each definition (unless referring to one defined within the definition).
* Corresponding entities have the same language linkage in each definition (e.g. the include file is not inside an `extern "C"` block).
* If a `const` object is `constant-initialized` in any of the definitions, it is constant-initialized in each definition.
* The rules above apply to every default argument used in each definition.
* If the definition is for a class with an implicitly-declared constructor, every translation unit where it is odr-used must call the same constructor for the base and members.
rrev|since=c++20|
* If the definition is for a class with a defaulted `three-way comparison`, every translation unit where it is odr-used must call the same comparison operator for the base and members.
* If the definition is for a template, then all these requirements apply to both names at the point of definition and dependent names at the point of instantiation.
If all these requirements are satisfied, the program behaves as if there is only one definition in the entire program. Otherwise, the program is ill-formed, no diagnostic required.
Note: in C, there is no program-wide ODR for types, and even extern declarations of the same variable in different translation units may have different types as long as they are compatible. In C++, the source-code tokens used in declarations of the same type must be the same as described above: if one .cpp file defines } and the other .cpp file defines }, the behavior of the program that links them together is undefined. This is usually resolved with `unnamed namespaces`.

### Naming an entity

A variable is ''named'' by an expression if the expression is an identifier expression that denotes it.
A function is ''named'' by an expression or conversion in following cases:
* A function whose name appears as an expression or conversion (including named function, overloaded operator, `user-defined conversion`, user-defined placement forms of `cpp/memory/new/operator new`, non-default initialization) is named by that expression if it is selected by overload resolution, except when it is an unqualified pure virtual member function or a pointer-to-member to a pure virtual function.
* An allocation or deallocation function for a class is named by a `new expression` appearing in an expression.
* A deallocation function for a class is named by a `delete expression` appearing in an expression.
* A constructor selected to copy or move an object is considered to be named by the expression or conversion even if `copy elision` takes place. <sup>(since C++17)</sup> Using a prvalue in some contexts does not copy or move an object, see `mandatory elision.`
A potentially evaluated expression or conversion odr-uses a function if it names it.
rrev|since=c++11|
A potentially constant evaluated expression or conversion that names a constexpr function makes it `needed for constant evaluation`, which triggers definition of a defaulted function or instantiation of a function template specialization, even if the expression is unevaluated.

### Potential results

The set of ''potential results'' of an expression `E` is a (possibly empty) set of identifier expressions that appear within `E`, combined as follows:
* If `E` is an `identifier expression`, the expression `E` is its only potential result.
* If `E` is a subscript expression (`E1[E2]`) where one of the operands is an array, the potential results of that operand is included in the set.
* If `E` is a class member access expression of the form `E1.E2` or `E1.template E2` naming a non-static data member, the potential results of `E1` is included in the set.
* If `E` is a class member access expression naming a static data member, the identifier expression designating the data member is included in the set.
* If `E` is a pointer-to-member access expression of the form `E1.*E2` or `E1.*template E2` whose second operand is a constant expression, the potential results of `E1` are included in the set.
* If `E` is an expression in parentheses (`(E1)`), the potential results of `E1` are included in the set.
* If `E` is a glvalue conditional expression (`E1 ? E2 : E3`, where `E2` and `E3` are glvalues), the union of the potential results of `E2` and `E3` are both included in the set.
* If `E` is a comma expression (`E1, E2`), the potential results of `E2` are in the set of potential results.
* Otherwise, the set is empty.

### ODR-use (informal definition)

An object is odr-used if its value is read (unless it is a compile time constant) or written, its address is taken, or a reference is bound to it,
A reference is odr-used if it is used and its referent is not known at compile time,
A function is odr-used if a function call to it is made or its address is taken.
If an entity is odr-used, its definition must exist somewhere in the program; a violation of that is usually a link-time error.

```cpp
struct S
{
    static const int x = 0; // static data member
    // a definition outside of class is required if it is odr-used
};

const int& f(const int& r);

int n = b ? (1, S::x) // S::x is not odr-used here
          : f(S::x);  // S::x is odr-used here: a definition is required
```


### ODR-use (formal definition)

A variable `x` that is named by a `potentially-evaluated expression` `expr` that appears at a point `P` is odr-used by `expr`, unless any of the following conditions is satisfied:
* `x` is a reference that is  at `P`.
* <sup>(until C++26)</sup> `x` is not a reference and `expr` is an element of the set of potential results of an expression `E`, and any of the following conditions is satisfied:
** `E` is a `discarded-value expression`, and no lvalue-to-rvalue conversion is applied to it.
** `x` is a<sup>(since C++26)</sup>  non-volatile object that is usable in constant expressions at `P` and has no mutable subobjects, and any of the following conditions is satisfied:
rrev|since=c++26|
::* `E` is a `class member access expression` naming a `non-static data member` of reference type and whose object expression has non-volatile-qualified type.
::* `E` has non-volatile-qualified non-class type, and the lvalue-to-rvalue conversion is applied to it.

```cpp
struct S { static const int x = 1; }; // applying lvalue-to-rvalue conversion
                                      // to S::x yields a constant expression

int f()
{
    S::x;        // discarded-value expression does not odr-use S::x

    return S::x; // expression where lvalue-to-rvalue conversion
                 // applies does not odr-use S::x
}
```

`*this` is odr-used if `this` appears as a potentially-evaluated expression (including the implicit `this` in a non-static member function call expression).
rrev|since=c++17|
A `structured binding` is odr-used if it appears as a potentially-evaluated expression.
A function is odr-used in following cases:
* A function is odr-used if it is named by (see below) a potentially-evaluated expression or conversion.
* A `virtual member function` is odr-used if it is not a pure virtual member function (addresses of virtual member functions are required to construct the vtable).
* A non-placement allocation or deallocation function for a class is odr-used by the definition of a constructor of that class.
* A non-placement deallocation function for a class is odr-used by the definition of the destructor of that class, or by being selected by the lookup at the point of definition of a virtual destructor.
* An assignment operator in a class `T` that is a member or base of another class `U` is odr-used by an implicitly-defined copy-assignment or move-assignment functions of `U`.
* A constructor (including default constructors) for a class is odr-used by the `initialization` that selects it.
* A destructor for a class is odr-used if it is `potentially invoked`.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-261 | C++98 | a deallocation function for a polymorphic class<br>might be odr-used even if there were no relevant<br>new or delete expressions in the program | supplemented the<br>odr-use cases to cover<br>constructors and destructors |
| cwg-678 | C++98 | an entity could have definitions<br>with different language linkages | the behavior is<br>undefined in this case |
| cwg-1472 | C++98 | reference variables which satisfy the requirements for<br>appearing in a constant expression were odr-used even<br>if the lvalue-to-rvalue conversion is immediately applied | they are not<br>odr-used in this case |
| cwg-1614 | C++98 | taking address of a pure virtual function odr-used it | the function is not odr-used |
| cwg-1741 | C++98 | constant objects that are immediately lvalue-to-rvalue<br>converted in potentially-evaluated expressions were odr-used | they are not odr-used |
| cwg-1926 | C++98 | array subscript expressions did not propagate potential results | they propagate |
| cwg-2300 | C++11 | lambda expressions in different translation<br>units could never have the same closure type | the closure type can be the<br>same under one definition rule |
| cwg-2353 | C++98 | a static data member was not a potential result<br>of a member access expression accessing it | it is |
| cwg-2433 | C++14 | a variable template could not have<br>multiple definitions in a program | it can |


## References

