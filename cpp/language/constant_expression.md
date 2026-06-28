---
title: Constant expressions
type: Language
source: https://en.cppreference.com/w/cpp/language/constant_expression
---


# Constant expressions

Defines an `expression` that can be evaluated at compile time.
Such expressions can be used as non-type template arguments, array sizes, and in other contexts that require constant expressions, e.g.

```cpp
int n = 1;
std::array<int, n> a1;  // Error: “n” is not a constant expression
const int cn = 2;
std::array<int, cn> a2; // OK: “cn” is a constant expression
```


## Definition

rev|until=c++11|
An expression that belongs to any of the constant expression categories listed below is a ''constant expression''.

### Integral constant expression (C++98)

In the following places, C++ requires expressions that evaluate to an integral or enumeration constant:
* `array bounds` (including the dimensions in ``new` expressions` other than the first)
* ``case` label` constants
* `bit-field` lengths
* `enumerator` initializers
* `static data member` initializers
*  of integral or enumeration type
An expression satisfying all following conditions is an ''integral constant-expression'':
* It only involves the following entities:
:* literals of arithmetic types
:* enumerators
:* variables or static data members satisfying all following conditions:
::* They are const-qualified.
::* They are not volatile-qualified.
::* They are of integral or enumeration types.
::* They are initialized with constant expressions.
:*  of integral or enumeration types
:* `sizeof` expressions
* It does not use any floating-point literals, unless they are `explicitly converted` to integral or enumeration types.
* It does not apply any conversion to non-integral and non-enumeration types.
* It does not use any of the following entities except in the operands of `sizeof`:
:* function
:* class object
:* pointer
:* reference
:* assignment operator
:* increment operator
:* decrement operator
:* function-call operator
:* comma operator

### Other constant expression categories

Other expressions are considered constant expressions only for the purpose of `constant initialization`. Such a constant expression must be one of the following expressions:
* an expression that evaluates to a `null pointer value`
* an expression that evaluates to a null pointer-to-member value
* an arithmetic constant expression
* an address constant expression
* a reference constant expression
* an address constant expression for a complete object type, plus or minus an integral constant expression
* a pointer-to-member constant expression
An ''arithmetic constant expression'' is an expression satisfying the requirements for an integral constant expression, with the following exceptions:
* Floating-point literals can be used without explicit conversion.
* Conversions to floating-point types can be applied.
An ''address constant expression'' is an expression of pointer type satisfying all following conditions:
* The pointer points to an lvalue designating an object of , a `string literal`, or a `function`. The object is not a `subobject` of non- type.
* The pointer is created by one of the following methods:
:* explicitly using the address-of operator
:* implicitly using a non-type template parameter of pointer type
:* using an expression of array or function type
* The expression does not call any function.
* The expression uses explicit pointer conversions (except `dynamic_cast`) and the following operators without accessing the result object:
:* subscript operator
:* indirection operator
:* address-of operator
:* member access operator
* If the subscript operator is used, one of its operands is an integral constant expression.
A ''reference constant expression'' is an expression of reference type satisfying all following conditions:
* The reference designates an object of static storage duration, a non-type template parameter of reference type, or a function. The reference does not designate a member or base class of non-POD class type.
* The expression does not call any function.
* The expression uses explicit reference conversions (except `dynamic_cast`) and the following operators without accessing the result object:
:* subscript operator
:* indirection operator
:* address-of operator
:* member access operator
* If the subscript operator is used, one of its operands is an integral constant expression.
A ''pointer-to-member constant expression'' is an expression of pointer-to-member type where the pointer is created by applying the address-of operator to a qualified identifier, optionally preceded by an explicit pointer-to-member conversion.
rev|since=c++11|until=c++26|
The following entities are ''permitted results of a constant expression'':
* temporary objects with  whose values satisfy the constraints listed below
* non-temporary objects with static storage duration
* <sup>(since C++20)</sup> non-`immediate `functions
A ''constant expression'' is either a glvalue core constant expression that refers to an entity that is a permitted result of a constant expression, or a prvalue core constant expression whose value satisfies the following constraints:
* Each constituent reference refers to an entity that is a permitted result of a constant expression.
* No constituent value of scalar type is an `indeterminate value`.
* Each constituent value of `pointer type` is one of the following values:
:* the address of an object with static storage duration
:* the address past the end of an object with static storage duration
:* the address of a<sup>(since C++20)</sup>  non-immediate function
:* a `null pointer value`
* No constituent value of pointer-to-member type designates an immediate function.
rev|since=c++26|
A ''constant expression'' is either a glvalue core constant expression that refers to an object or a non-`immediate` function, or a prvalue core constant expression whose value satisfies the following constraints:
* Each constituent reference refers to an object or a non-immediate function.
* No constituent value of scalar type is an `indeterminate or erroneous value`.
* No constituent value of pointer type is a pointer to an immediate function or an `invalid pointer value`.
* No constituent value of pointer-to-member type designates an immediate function.
When determining whether an expression is a constant expression, `copy elision` is assumed not to be performed.
The C++98 definition of constant expressions is entirely within the collpase box. The following description applies to C++11 and later C++ versions.

## Literal type

The following types are collectively called ''literal types'':
<sup>(since C++14)</sup> * possibly cv-qualified `void`
* scalar type
* `reference type`
* an `array` of literal type
* possibly cv-qualified class type that satisfies all following conditions:
:* It has a <sup>(until C++20)</sup> <sup>(since C++20)</sup> `constexpr destructor`.
:* All of its non-static non-variant data members and base classes are of non-volatile literal types.
:* It is one of the following types:
rrev|since=c++17|
::* a
::* an `aggregate` union type that satisfies one of the following conditions:
:::* It has no `variant member`.
:::* It has at least one variant member of non-volatile literal type.
::* a non-union aggregate type, and each of its `anonymous union` members satisfies one of the following conditions:
:::* It has no variant member.
:::* It has at least one variant member of non-volatile literal type.
::* a type with at least one constexpr constructor (template) that is not a copy or move constructor
Only objects of literal types can be created within a constant expression.

## Core constant expression

A ''core constant expression'' is any expression whose evaluation '''would not''' evaluate any one of the following language constructs:
<ol>
<li> the `this` pointer, except in a `constexpr function` that is being evaluated as part of the expression, or when appearing in an implicit or explicit class member access expression
<li> <sup>(C++23)</sup> a control flow that passes through a declaration of a `block variable` with static or thread `storage duration` that is not usable in constant expressions
<li> a function call expression that calls a function (or a constructor) that is not declared `constexpr`

```cpp
constexpr int n = std::numeric_limits<int>::max(); // OK: max() is constexpr
constexpr int m = std::time(nullptr); // Error: std::time() is not constexpr
```

<li> a function call to a constexpr function which is declared, but not defined
<li> a function call to a constexpr function/constructor template instantiation where the instantiation fails to satisfy `constexpr function/constructor` requirements.
<li> a function call to a constexpr virtual function, invoked on an object whose dynamic type is constexpr-unknown
<li> an expression that would exceed the implementation-defined limits
<li> an expression whose evaluation leads to any form of core language `undefined`<sup>(since C++26)</sup>  or erroneous behavior, except for any potential undefined behavior introduced by .

```cpp
constexpr double d1 = 2.0 / 1.0; // OK
constexpr double d2 = 2.0 / 0.0; // Error: not defined
constexpr int n = std::numeric_limits<int>::max() + 1; // Error: overflow
int x, y, z[30];
constexpr auto e1 = &y - &x;        // Error: undefined
constexpr auto e2 = &z[20] - &z[3]; // OK
constexpr std::bitset<2> a; 
constexpr bool b = a[2]; // UB, but unspecified if detected
```

<li> <sup>(until C++17)</sup> a `lambda expression`
<li> an lvalue-to-rvalue `implicit conversion` unless applied to...
<ol type="a">
<li> a glvalue of type (possibly cv-qualified) `std::nullptr_t`
<li> a non-volatile literal-type glvalue that designates an object that is usable in constant expressions

```cpp
int main()
{
    const std::size_t tabsize = 50;
    int tab[tabsize]; // OK: tabsize is a constant expression
                      // because tabsize is usable in constant expressions
                      // because it has const-qualified integral type, and
                      // its initializer is a constant initializer

    std::size_t n = 50;
    const std::size_t sz = n;
    int tab2[sz]; // Error: sz is not a constant expression
                  // because sz is not usable in constant expressions
                  // because its initializer was not a constant initializer
}
```

<li> a non-volatile literal-type glvalue that refers to a non-volatile object whose lifetime began within the evaluation of this expression
</ol>
<li> an lvalue-to-rvalue `implicit conversion` or modification applied to a non-active member of a `union` or its subobject (even if it shares a common initial sequence with the active member)
<li> an lvalue-to-rvalue implicit conversion on an object `whose value is indeterminate`
<li> an invocation of implicit copy/move constructor/assignment for a union whose active member is mutable (if any), with lifetime beginning outside the evaluation of this expression
<li> <sup>(until C++20)</sup> an assignment expression that would change the active member of a union
<li> conversion from pointer to `void` to a pointer-to-object type `T*`<sup>(since C++26)</sup>  unless the pointer holds a null pointer value or points to an object whose type is `similar to `T``
<li> `dynamic_cast` <sup>(since C++20)</sup> whose operand is a glvalue that refers to an object whose dynamic type is constexpr-unknown
<li> `reinterpret_cast`
<li> <sup>(until C++20)</sup> pseudo-destructor call
<li> <sup>(until C++14)</sup> an increment or a decrement operator
<li>
<sup>(C++14)</sup> modification of an object, unless the object has non-volatile literal type and its lifetime began within the evaluation of the expression

```cpp
constexpr int incr(int& n)
{
    return ++n;
}

constexpr int g(int k)
{
    constexpr int x = incr(k); // Error: incr(k) is not a core constant
                               // expression because lifetime of k
                               // began outside the expression incr(k)
    return x;
}

constexpr int h(int k)
{
    int x = incr(k); // OK: x is not required to be initialized
                     // with a core constant expression
    return x;
}

constexpr int y = h(1); // OK: initializes y with the value 2
                        // h(1) is a core constant expression because
                        // the lifetime of k begins inside the expression h(1)
```

<li> <sup>(C++20)</sup> a destructor call or pseudo destructor call for an object whose lifetime did not begin within the evaluation of this expression
<li> a `typeid` expression applied to a glvalue of polymorphic type <sup>(since C++20)</sup> and that glvalue refers to an object whose dynamic type is constexpr-unknown
<li> a ``new` expression`<sup>(since C++20)</sup> , unless one of the following conditions is satisfied:
rev|since=c++20|
* The selected allocation function is a replaceable global allocation function and the allocated storage is deallocated within the evaluation of this expression.
rev|since=c++26|
* The selected allocation function is a non-allocating form with an allocated type `T`, and the placement argument satisfies all following conditions:
:* It points to:
::* an object whose type is similar to `T`, if `T` is not an array type, or
::* the first element of an object of a type similar to `T`, if `T` is an array type.
:* It points to storage whose duration began within the evaluation of this expression.
<li> a ``delete` expression`<sup>(since C++20)</sup> , unless it deallocates a region of storage allocated within the evaluation of this expression
<li> <sup>(C++20)</sup> Coroutines: an `await-expression` or a `yield-expression`
<li> <sup>(C++20)</sup> a  when the result is unspecified
<li> an equality or relational operator whose result is unspecified
<li> <sup>(until C++14)</sup> an assignment or a compound assignment operator
<li> <sup>(until C++26)</sup> a throw expression
<li> <sup>(C++26)</sup> a construction of an exception object, unless the exception object and all of its implicit copies created by invocations of `std::current_exception` or `std::rethrow_exception` are destroyed within the evaluation of this expression

```cpp
constexpr void check(int i)
{
    if (i < 0)
        throw i;
}

constexpr bool is_ok(int i)
{
    try {
        check(i);
    } catch (...) {
        return false;
    }
    return true;
}

constexpr bool always_throw()
{
    throw 12;
    return true;
}

static_assert(is_ok(5)); // OK
static_assert(!is_ok(-1)); // OK since C++26
static_assert(always_throw()); // Error: uncaught exception
```

<li> an `asm-declaration`
<li> an invocation of the `va_arg` macro
<li> a `goto` statement
<li> a `dynamic_cast` or `typeid` expression <sup>(since C++26)</sup> or ``new` expression` that would throw an exception <sup>(since C++26)</sup> where no definition of the exception type is reachable
<li> inside a lambda expression, a reference to `this` or to a variable defined outside that lambda, if that reference would be an odr-use

```cpp
void g()
{
    const int n = 0;

    constexpr int j = *&n; // OK: outside of a lambda-expression

    [=]
    {
        constexpr int i = n;   // OK: 'n' is not odr-used and not captured here.
        constexpr int j = *&n; // Ill-formed: '&n' would be an odr-use of 'n'.
    };
}
```

rrev|since=c++17|
note that if the ODR-use takes place in a function call to a closure, it does not refer to `this` or to an enclosing variable, since it accesses a closure's data member instead

```cpp
// OK: 'v' & 'm' are odr-used but do not occur in a constant-expression
// within the nested lambda
auto monad = [](auto v){ return [=]{ return v; }; };
auto bind = [](auto m){ return [=](auto fvm){ return fvm(m()); }; };

// OK to have captures to automatic objects created during constant expression evaluation.
static_assert(bind(monad(2))(monad)() == monad(2)());
```

</ol>

### Extra requirements

Even if an expression `E` does not evaluate anything stated above, it is implementation-defined whether `E` is a core constant expression if evaluating `E` would result in `runtime-undefined behavior` due to the use of  or .
Even if an expression `E` does not evaluate anything stated above, it is unspecified whether `E` is a core constant expression if evaluating `E` would evalute any of the following:
* An operation with undefined behavior in the .
* An invocation of the `va_start` macro.
For the purposes of determining whether an expression is a core constant expression, the evaluation of the body of a member function of `std::allocator<T>` is ignored if `T` is a literal type.
For the purposes of determining whether an expression is a core constant expression, the evaluation of a call to a trivial copy/move constructor or copy/move assignment operator of a `union` is considered to copy/move the active member of the union, if any.
rrev|since=c++26|
For the purposes of determining whether an expression is a core constant expression, the evaluation of an identifier expression that names a `structured binding` `bd` has the following semantics:
* If `bd` is an lvalue referring to the object bound to an invented reference `ref`, the behavior is as if `ref` were nominated.
* Otherwise, if `bd` names an array element, the behavior is that of evaluating `e[i]`, where `e` is the name of the variable initialized from the initializer of the structured binding declaration, and `i` is the index of the element referred to by `bd`.
* Otherwise, if `bd` names a class member, the behavior is that of evaluating `e.m`, where `e` is the name of the variable initialized from the initializer of the structured binding declaration, and `m` is the name of the member referred to by `bd`.
During the evaluation of the expression as a core constant expression, all names and uses of `*this` that refer to an object or reference whose lifetime began outside the evaluation of the expression are treated as referring to a specific instance of that object or reference whose lifetime and that of all subobjects (including all union members) includes the entire constant evaluation.
* For such an object<sup>(since C++20)</sup>  that is not usable in constant expressions, the dynamic type of the object is ''constexpr-unknown''.
* For such a reference<sup>(since C++20)</sup>  that is not usable in constant expressions, the reference is treated as binding to an unspecified object of the referenced type whose lifetime and that of all subobjects includes the entire constant evaluation and whose dynamic type is constexpr-unknown.

## Integral constant expression

''Integral constant expression'' is an expression of integral or unscoped enumeration type implicitly converted to a prvalue, where the converted expression is a core constant expression.
If an expression of class type is used where an integral constant expression is expected, the expression is `contextually implicitly converted` to an integral or unscoped enumeration type.

## Converted constant expression

A ''converted constant expression'' of type `T` is an expression `implicitly converted` to type `T`, where the converted expression is a constant expression, and the implicit conversion sequence contains only:
:* constexpr `user-defined conversions`
:* s
:* s
:* non-narrowing
:* s
:* non-narrowing
rev|since=c++17|
:* s
:* s
:*
:*
:* `null pointer conversions` from `std::nullptr_t`
:* `null member pointer conversions` from `std::nullptr_t`
And if any `reference binding` takes place, it can only be .
The following contexts require a converted constant expression:
* the *constant-expression* of ``case` labels`
* `enumerator initializers` when the underlying type is fixed
* <sup>(until C++17)</sup> integral and enumeration non-type `template arguments`
rev|since=c++14|
* `array bounds`
* the dimensions in ``new` expressions` other than the first
rev|since=c++26|
* the index of `pack indexing expression` and `pack indexing specifier`
A ''contextually converted constant expression of type `bool`'' is an expression,  `contextually converted to `bool``, where the converted expression is a constant expression and the conversion sequence contains only the conversions above.
The following contexts require a contextually converted constant expression of type `bool`:
* ``noexcept` specifications`
rev|until=c++23|
* ``static_assert` declarations`
rev|since=c++17|until=c++23|
* `constexpr if-statements`
rev|since=c++20|
* `conditional `explicit` specifiers`

## Constituent entities

Informally, the ''constituent values'' and ''constituent references'' of an object `obj` are the scalar values and references that make up `obj`.
Formally, the ''constituent values'' of an object `obj` are defined as follows:
* If `obj` has scalar type, the constituent value is the value of `obj`.
* Otherwise, the constituent values are the constituent values of any direct  of `obj` other than `inactive union members`.
The ''constituent references'' of an object `obj` include the following references:
* any direct members of `obj` that have reference type
* the constituent references of any direct subobjects of `obj` other than inactive union members
The ''constituent values'' and ''constituent references'' of a variable `var` are defined as follows:
* If `var` declares an object, the constituent values and references are the constituent values and references of that object.
* If `var` declares a reference, the constituent reference is that reference.
For any constituent reference `ref` of a variable `var`, if `ref` is bound to a temporary object or subobject thereof whose lifetime is extended to that of `ref`, the constituent values and references of that temporary object are also constituent values and references of `var`, recursively.

## Constexpr-representable entities

Every object with static storage duration is ''constexpr-referenceable'' at any point in the program.
rrev|since=c++26|
An object with automatic storage duration is ''constexpr-referenceable'' from a point **`P`** if
the object is defined in the function body that directly contains **`P`**.

```cpp
void f() {
    constexpr int x = 42;
    constexpr const int& ref = x; // OK, x is constexpr-referenceable here

    const int& r = 42; // r binds to a temporary object with automatic storage duration
    constexpr const int& ref2 = r; // OK, the temporary is constexpr-referenceable here

    [&] {
        constexpr const int& ref = x; // Error: x is not constexpr-referenceable here
    };
}
```

Other objects (e.g. those with thread storage duration) are never constexpr-referenceable.
An object or reference `x` is ''constexpr-representable'' at a point **`P`** if all following conditions are satisfied:
* For each constituent value of `x` that points to an object `obj`, `obj` is constexpr-referenceable from **`P`**.
* For each constituent value of `x` that points past an object `obj`, `obj` is constexpr-referenceable from **`P`**.
* For each constituent reference of `x` that refers to an object `obj`, `obj` is constexpr-referenceable from **`P`**.

## Constant-initialized entities

rev|until=c++26|
A variable or temporary object `obj` is ''constant-initialized'' if all following conditions are satisfied:
* Either it has an initializer, or its type is `const-default-constructible`.
* The `full-expression` of its initialization is a constant expression in the context of requiring a constant expression, except that if `obj` is an object, that full-expression may also invoke `constexpr constructors` for `obj` and its subobjects even if those objects are of non-literal class types.
rev|since=c++26|
A variable `var` is ''constant-initializable'' if all following conditions are satisfied:
* The `full-expression` of its initialization is a constant expression in the context of requiring a constant expression, where all `contract assertions` use the “ignore” evaluation semantic.
* Immediately after the initializing declaration of `var`, the object or reference declared by `var` is constexpr-representable.
* If the object or reference `x` declared by `var` has static or thread storage duration, `x` is constexpr-representable at the nearest point whose immediate scope is a namespace scope that follows the initializing declaration of `var`.
A constant-initializable variable is ''constant-initialized'' if either it has an initializer, or its type is `const-default-constructible`.

```cpp
void f() {
    int ax = 0; // ax is constant-initialized
    thread_local int tx = 0; // tx is constant-initialized
    static int sx; // sx is not constant-initialized (it doesn't have an initializer)

    constexpr int& raa = ax; // OK, raa is constant-initialized

    constexpr int& rat = tx;
    // Error: rat is not constant-initialized
    // because it's not constexpr-representable here

    static constexpr int& rsa = ax;
    // Error: rsa is not constant-initialized
    // because it's not constexpr-representable at the nearest namespace scope
}
```


## Usable in constant expressions

A variable is ''potentially-constant'' if it is a ``constexpr` variable` or it has reference or non-volatile const-qualified integral or enumeration type.
A variable `var` is ''usable in constant expressions'' at a point **`P`** if:
* `var` is constant-initialized,
* `var` is potentially-constant,
* `var`’s initializing declaration **`D`** is reachable from **`P`** and,
* any of the following conditions is satisfied:
:* `var` is a `constexpr` variable.
:* `var` is not initialized to a `TU-local` value.
:* **`P`** is in the same translation unit as **`D`**.
An object or reference is ''usable in constant expressions'' at a point **`P`** if <sup>(since C++26)</sup> it is constexpr-representable at **`P`** and it is one of the following entities:
* a variable that is usable in constant expressions at **`P`**
* a temporary object of non-volatile const-qualified literal type whose lifetime is extended to that of a variable that is usable in constant expressions at **`P`**
rrev|since=c++20|
* a
* a `string literal` object
* a non-mutable subobject of any of the above
* a reference member of any of the above
rrev|since=c++20|

## Manifestly constant-evaluated expressions

The following expressions (including conversions to the destination type) are ''manifestly constant-evaluated'':
* `array bounds`
* the dimensions in ``new` expressions` other than the first
* `bit-field` lengths
* `enumeration` initializers
* `alignments`
* the *constant-expression* of ``case` labels`
* non-type `template arguments`
* expressions in ``noexcept` specifications`
* expressions in ``static_assert` declarations`
* initializers of `constexpr variables`
* conditions of `constexpr if-statements`
* expressions in `conditional `explicit` specifiers`
* `immediate invocations`
* constraint expressions in `concept` definitions, `nested requirements`, and ``requires` clauses`, when determining whether the constraints are satisfied
* initializers of variables with reference type or const-qualified integral or enumeration type, but only if the initializers are constant expressions
* initializers of static and thread local variables, but only if all subexpressions of the initializers (including constructor calls and implicit conversions) are constant expressions (that is, if the initializers are `constant initializers`)
Whether an evaluation occurs in a manifestly constant-evaluated context can be detected by `std::is_constant_evaluated`<sup>(since C++23)</sup>  and `if consteval`.

## Functions and variables needed for constant evaluation

Following expressions or conversions are ''potentially constant evaluated'':
* manifestly constant-evaluated expressions
* potentially-evaluated expressions
* immediate subexpressions of a `braced-enclosed initializer list` (constant evaluation may be necessary to determine whether `a conversion is narrowing`)
* address-of expressions that occur within a `templated entity` (constant evaluation may be necessary to determine whether such an expression is `value-dependent`)
* subexpressions of one of the above that are not a subexpression of a nested `unevaluated operand`
A function is ''needed for constant evaluation'' if it is a constexpr function and `named by` an expression that is potentially constant evaluated.
A variable is ''needed for constant evaluation'' if it is either a constexpr variable or is of non-volatile const-qualified integral type or of reference type and the `identifier expression` that denotes it is potentially constant evaluated.
Definition of a defaulted function and instantiation of a `function template` specialization <sup>(since C++14)</sup> or `variable template specialization` are triggered if the function <sup>(since C++14)</sup> or variable is needed for constant evaluation.
===Constant subexpression===
A ''constant subexpression'' is an expression whose evaluation as `subexpression` of an expression `e` would not prevent `e` from being a core constant expression, where `e` is not any of the following expressions:
* ``throw` expression`
rrev|since=c++20|
* `yield expression`
* `assignment expression`
* `comma expression`

## Notes


## Example


## See also


| cpp/language/dsc constexpr | (see dedicated page) |
| cpp/types/dsc is_literal_type | (see dedicated page) |

