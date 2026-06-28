---
title: Type
type: Language
source: https://en.cppreference.com/w/cpp/language/type
---


# Type

`Objects`, `reference`s, `functions` including `function template specializations`, and `expressions` have a property called ''type'', which both restricts the operations that are permitted for those entities and provides semantic meaning to the otherwise generic sequences of bits.

## Type classification

The C++ type system consists of the following types:
* `fundamental types` (see also `std::is_fundamental`):
:* the type `void` (see also `std::is_void`);
rev|since=c++11|
:* the type `std::nullptr_t` (see also `std::is_null_pointer`);
rev|since=c++26|
:* the type `cpp/meta/info|std::meta::info` (see also `std::is_reflection`);
:* arithmetic types (see also `std::is_arithmetic`):
::* integral types (including `cv-qualified versions`, see also `std::is_integral`, a synonym for integral type is integer type):
:::* the type `bool`;
:::* character types:
::::* narrow character types:
:::::* ordinary character types: `char`, `signed char`, `unsigned char`
rrev|since=c++20|
:::::* the type `char8_t`
::::* wide character types: <sup>(since C++11)</sup> `char16_t`, `char32_t`, `wchar_t`;
:::* signed integer types:
::::* standard signed integer types: `signed char`, `short`, `int`, `long`, `long long`;
rrev|since=c++11|
::::* extended signed integer types (implementation-defined);
:::* unsigned integer types:
::::* standard unsigned integer types: `unsigned char`, `unsigned short`, `unsigned`, `unsigned long`, `unsigned long long`;
rrev|since=c++11|
::::* extended unsigned integer types (each corresponds to an extended signed integer type, and vice versa);
::* floating-point types (see also `std::is_floating_point`):
:::* standard floating-point types: `float`, `double`, `long double` and their `cv-qualified versions`;
rrev|since=c++23|
:::* extended floating-point types (including `cv-qualified versions`):
::::* fixed width floating-point types;
::::* other implementation-defined extended floating-point types;
* compound types (see also `std::is_compound`):
:* `reference types` (see also `std::is_reference`):
::* `lvalue reference types` (see also `std::is_lvalue_reference`):
:::* lvalue reference to object types;
:::* lvalue reference to function types;
rrev|since=c++11|
::* `rvalue reference types` (see also `std::is_rvalue_reference`):
:::* rvalue reference to object types;
:::* rvalue reference to function types;
:* `pointer types` (see also `std::is_pointer`):
::* `pointer-to-object types`;
::* `pointer-to-function types`;
:* `pointer-to-member types` (see also `std::is_member_pointer`):
::* `pointer-to-data-member` types (see also `std::is_member_object_pointer`);
::* `pointer-to-member-function` types (see also `std::is_member_function_pointer`);
:* `array types` (see also `std::is_array`);
:* `function types` (see also `std::is_function`);
:* `enumeration types` (see also `std::is_enum`);
::* `unscoped enumeration types`;
rrev|since=c++11|
::* `scoped enumeration types` (see also );
:* `class types`:
::* non-union types (see also `std::is_class`);
::* `union types` (see also `std::is_union`).
For every non-cv-qualified type other than reference and function, the type system supports three additional `cv-qualified versions` of that type (`const`, `volatile`, and `const volatile`).

## Other categories

An ''object type'' (see also `std::is_object`) is a (possibly cv-qualified) type that is not a function type, not a reference type, and not (possibly cv-qualified) `void`.
The following types are collectively called ''scalar types'' (see also `std::is_scalar`):
* arithmetic types
* enumeration types
* pointer types
* pointer-to-member types
rev|since=c++11|
* `std::nullptr_t`
rev|since=c++26|
* `cpp/meta/info|std::meta::info`
* cv-qualified versions of these types
The following types are collectively called ''implicit-lifetime types'':
* scalar types
* implicit-lifetime class types
* array types
* cv-qualified versions of these types
rrev|since=c++11|
The following types are collectively called ''trivially copyable types'':
* scalar types
* trivially copyable class types
* arrays of such types
* cv-qualified versions of these types
The following types are collectively called ''standard-layout types'':
* scalar types
* standard-layout class types
* arrays of such types
* cv-qualified versions of these types
<div style="overflow-x: scroll;">
File:cpp_types_v3.svg
</div>
''Note: Elements of SVG image are clickable, but you must open the diagram in a new browser tab first''

### Deprecated categories

<tr class="t-rev">
<td>
The following types are collectively called ''POD types'' (see also `std::is_pod`):
* scalar types
* POD classes
* arrays of such types
* cv-qualified versions of these types
</td>
<td><sup>(deprecated C++20)</sup></td>
</tr>
<tr class="t-rev">
<td>
The following types are collectively called ''trivial types'' (see also `std::is_trivial`):
* scalar types
* trivial class types
* arrays of such types
* cv-qualified versions of these types
</td>
<td><sup>(C++11)</sup><br><sup>(deprecated C++26)</sup></td>
</tr>

## Program-defined type

A ''program-defined specialization'' is an `explicit specialization` or `partial specialization` that is not part of the C++  and not defined by the implementation.
A ''program-defined type'' is one of the following types:
* A<sup>(since C++11)</sup>  non-`closure` `class type` or `enumeration type` that is not part of the C++ standard library and not defined by the implementation.
rrev|since=c++11|
* A closure type of a non-implementation-provided `lambda expression`.
* An `instantiation` of a program-defined specialization.

## Type naming

A `name` can be declared to refer to a type by means of:
* `class` declaration;
* `union` declaration;
* `enum` declaration;
* `typedef` declaration;
* `type alias` declaration.
Types that do not have names often need to be referred to in C++ programs; the syntax for that is known as *type-id*. The syntax of the type-id that names type `T` is exactly the syntax of a `declaration` of a variable or function of type `T`, with the identifier omitted, except that *decl-specifier-seq* of the declaration grammar is constrained to *type-specifier-seq*, and that new types may be defined only if the type-id appears on the right-hand side of a non-template type alias declaration.

```cpp
int* p;               // declaration of a pointer to int
static_cast<int*>(p); // type-id is "int*"

int a[3];   // declaration of an array of 3 int
new int[3]; // type-id is "int[3]" (called new-type-id)

int (*(*x[2])())[3];      // declaration of an array of 2 pointers to functions
                          // returning pointer to array of 3 int
new (int (*(*[2])())[3]); // type-id is "int (*(*[2])())[3]"

void f(int);                    // declaration of a function taking int and returning void
std::function<void(int)> x = f; // type template parameter is a type-id "void(int)"
std::function<auto(int) -> void> y = f; // same

std::vector<int> v;       // declaration of a vector of int
sizeof(std::vector<int>); // type-id is "std::vector<int>"

struct { int x; } b;         // creates a new type and declares an object b of that type
sizeof(struct { int x; });   // error: cannot define new types in a sizeof expression
using t = struct { int x; }; // creates a new type and declares t as an alias of that type

sizeof(static int); // error: storage class specifiers not part of type-specifier-seq
std::function<inline void(int)> f; // error: neither are function specifiers
```

The *declarator* part of the declaration grammar with the name removed is referred to as *abstract-declarator*.
Type-id may be used in the following situations:
* to specify the target type in `cast expressions`;
* as arguments to `sizeof`, `alignof`, `alignas`, `new`, and `typeid`;
* on the right-hand side of a `type alias` declaration;
* as the trailing return type of a `function` declaration;
* as the default argument of a `template type parameter`;
* as the template argument for a `template type parameter`;
rrev|until=c++17|
* in `dynamic exception specification`.
Type-id can be used with some modifications in the following situations:
* in the parameter list of a `function` (when the parameter name is omitted), type-id uses *decl-specifier-seq* instead of *type-specifier-seq* (in particular, some storage class specifiers are allowed);
* in the name of a `user-defined conversion function`, the abstract declarator cannot include function or array operators.

## Elaborated type specifier

Elaborated type specifiers may be used to refer to a previously-declared class name (class, struct, or union) or to a previously-declared enum name even if the name was `hidden by a non-type declaration`. They may also be used to declare new class names.
See `elaborated type specifier` for details.

## Static type

The type of an expression that results from the compile-time analysis of the program is known as the ''static type'' of the expression. The static type does not change while the program is executing.

## Dynamic type

If some `glvalue expression` refers to a `polymorphic object`, the type of its most derived object is known as the dynamic type.

```cpp
// given
struct B { virtual ~B() {} }; // polymorphic type
struct D : B {};               // polymorphic type

D d; // most-derived object
B* ptr = &d;

// the static type of (*ptr) is B
// the dynamic type of (*ptr) is D
```

For prvalue expressions, the dynamic type is always the same as the static type.

## Incomplete type

The following types are ''incomplete types'':
* the type `void` (possibly `cv`-qualified);
* ''incompletely-defined object types'':
** class type that has been declared (e.g. by ) but not defined;
** `array of unknown bound`;
** array of elements of incomplete type;
** `enumeration type` from the point of declaration until its underlying type is determined.
All other types are complete.
Any of the following contexts requires type `T` to be complete:
* `definition` of or call to a function with return type `T` or argument type `T`;
* `definition` of an object of type `T`;
* declaration of a `non-static class data member` of type `T`;
* ``new` expression` for an object of type `T` or an array whose element type is `T`;
* `lvalue-to-rvalue conversion` applied to a glvalue of type `T`;
* an `implicit` or `explicit` conversion to type `T`;
* a `standard conversion`, `dynamic_cast`, or `static_cast` to type `T*` or `T&`, except when converting from the `null pointer constant` or from a `pointer to possibly cv-qualified void`;
* `class member access operator` applied to an expression of type `T`;
* `typeid`, `sizeof`, or `alignof` operator applied to type `T`;
* `arithmetic operator` applied to a pointer to `T`;
* definition of a class with base class `T`;
* assignment to an lvalue of type `T`;
* a `handler` of type `T`, `T&`, or `T*`.
(In general, when the size and layout of `T` must be known.)
If any of these situations occur in a translation unit, the definition of the type must appear in the same translation unit. Otherwise, it is not required.
An incompletely-defined object type can be completed:
* A class type (such as `class X`) might be regarded as incomplete at one point in a translation unit and regarded as complete later on; the type `class X` is the same type at both points:

```cpp
struct X;            // declaration of X, no definition provided yet
extern X* xp;        // xp is a pointer to an incomplete type:
                     // the definition of X is not reachable

void foo()
{
    xp++;            // ill-formed: X is incomplete
}

struct X { int i; }; // definition of X
X x;                 // OK: the definition of X is reachable

void bar()
{
    xp = &x;         // OK: type is “pointer to X”
    xp++;            // OK: X is complete
}
```

* The declared type of an array object might be an array of incomplete class type and therefore incomplete; if the class type is completed later on in the translation unit, the array type becomes complete; the array type at those two points is the same type.
* The declared type of an array object might be an array of unknown bound and therefore be incomplete at one point in a translation unit and complete later on; the array types at those two points ("array of unknown bound of `T`" and "array of `N` `T`") are different types.
The type of a pointer or reference to array of unknown bound permanently points to or refers to an incomplete type. An array of unknown bound named by a `typedef` declaration permanently refers to an incomplete type. In either case, the array type cannot be completed:

```cpp
extern int arr[];   // the type of arr is incomplete
typedef int UNKA[]; // UNKA is an incomplete type

UNKA* arrp;         // arrp is a pointer to an incomplete type
UNKA** arrpp;

void foo()
{
    arrp++;         // error: UNKA is an incomplete type
    arrpp++;        // OK: sizeof UNKA* is known
}

int arr[10];        // now the type of arr is complete

void bar()
{
    arrp = &arr;    // OK: qualification conversion (since C++20)
    arrp++;         // error: UNKA cannot be completed
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-328 | C++98 | class members of incomplete type were not prohibited<br>if an object of the class type was never created | non-static class data members<br>need to be complete |
| cwg-977 | C++98 | the point when an enumeration type becomes<br>complete in its definition was unclear | the type is complete once the<br>underlying type is determined |
| cwg-2448 | C++98 | only cv-unqualified types could be integral and floating-point types | allows cv-qualified types |
| cwg-2630 | C++98 | it was unclear whether a class is considered complete outside<br>the translation unit where the definition of the class appears | the class is complete<br>if its definition is<br>reachable in this case |
| cwg-2643 | C++98 | the type of a pointer to array of unknown bound<br>could not be completed (but it is already complete) | the pointed-to array type<br>cannot be completed |
| lwg-2139 | C++98 | the meaning of “user-defined type” was unclear | defines and uses “program-<br>defined type” instead |
| lwg-3119 | C++11 | it was unclear whether closure types are program-defined types | made clear |


## References


## See also


## External links

