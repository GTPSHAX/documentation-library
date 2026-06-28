---
title: Declarations
type: Language
source: https://en.cppreference.com/w/cpp/language/declarations
---


# Declarations

''Declarations'' are how names are introduced (or re-introduced) into the C++ program. Not all declarations actually declare anything, and each kind of entity is declared differently. `Definitions` are declarations that are sufficient to use the entity identified by the name.
A declaration is one of the following:
* `Function definition`
* `Template declaration` (including `Partial template specialization`)
* `Explicit template instantiation`
* `Explicit template specialization`
* `Namespace definition`
* `Linkage specification`
rrev|since=c++11|
* Attribute declaration (*`attr`* **`;`**)
* Empty declaration (**`;`**)
* A function declaration without a decl-specifier-seq:

**Syntax:**

- `sdsc|`
- `*attr* (optional) *declarator* **`;`**`

### Parameters

- `{{spar` - attr|<sup>(C++11)</sup> sequence of any number of `attributes`
- `{{spar` - declarator|a function declarator
: This declaration must declare a constructor, destructor, or user-defined type `conversion function`. It can only be used as part of a `template declaration`, `explicit specialization`, or explicit instantiation.
* *block-declaration* (a declaration that can appear inside a `block`), which, in turn, can be one of the following:
:* `asm declaration`
rrev|since=c++11|
:* `type alias declaration`
:* `namespace alias definition`
:* `using-declaration`
:* `using directive`
rev|since=c++20|
:* `using-enum-declaration`
rev|since=c++11|
:* `static_assert` declaration
:* `opaque enum declaration`
:* simple declaration

## Simple declaration

A simple declaration is a statement that introduces, creates, and optionally initializes one or several identifiers, typically variables.

**Syntax:**

- `sdsc|num=1|`
- `*decl-specifier-seq* *init-declarator-list* (optional) **`;`**`
- `|`
- `*attr* *decl-specifier-seq* *init-declarator-list* (optional) **`;`**`

### Parameters

- `{{spar` - decl-specifier-seq|sequence of specifiers
- `{{spar` - init-declarator-list|comma-separated list of init-declarators (see below)
- `{{spar` - attr|sequence of any number of `attributes`
*init-declarator-list* can only be omitted when declaring a named class or a named enumeration.
rrev|since=c++17|
A `structured binding declaration` is also a simple declaration.
The syntax of *init-declarator* is defined as follows:

**Syntax:**

- `sdsc|num=1|`
- `*declarator* *initializer*`
- `sdsc|num=2|`
- `*declarator* *requires-clause* (optional) *contract-specs* (optional)`
1. A declarator with an initializer.
2. A declarator without an initializer.

### Parameters

- `{{spar` - declarator|a declarator
- `{{spar` - initializer|an `initializer`
- `{{spar` - requires-clause|<sup>(C++20)</sup> a ``requires` clause`
- `{{spar` - contract-specs|<sup>(C++26)</sup> a list of 
rev|since=c++20|
*requires-clause* can only appear if *declarator* declares a `templated function`.
rev|since=c++26|
*contract-specs* can only appear if *declarator* declares a function or function template.

## Specifiers

'''Declaration specifiers''' (*decl-specifier-seq*) is a sequence of the following whitespace-separated specifiers, in any order:
* the `typedef` specifier. If present, the entire declaration is a `typedef declaration` and each declarator introduces a new type name, not an object or a function.
* function specifiers (`inline`, `virtual`, `explicit`), only allowed in `function declarations`.
rrev|since=c++17|
* the `inline` specifier is also allowed on variable declarations.
* the `friend` specifier, allowed in class and function declarations.
rev|since=c++11|
* the `constexpr` specifier, only allowed in variable definitions, function and function template declarations, and the declaration of static data members of literal type.
rev|since=c++20|
* the `consteval` specifier, only allowed in function and function template declarations.
* the `constinit` specifier, only allowed in declaration of a variable with static or thread storage duration. At most one of the `constexpr`, `consteval`, and `constinit` specifiers is allowed to appear in a *decl-specifier-seq*.
* `storage class specifier` (<sup>(until C++17)</sup> `cpp/keyword/register`,  `cpp/keyword/static`, <sup>(since C++11)</sup> `cpp/keyword/thread_local`,  `cpp/keyword/extern`, `cpp/keyword/mutable`). Only one storage class specifier is allowed<sup>(since C++11)</sup> , except that `thread_local` may appear together with `extern` or `static`.
* '''Type specifiers''' (*type-specifier-seq*), a sequence of specifiers that names a type. The type of every entity introduced by the declaration is this type, optionally modified by the declarator (see below). This sequence of specifiers is also used by `type-id`. Only the following specifiers are part of *type-specifier-seq*, in any order:
:* `class specifier`
:* `enum specifier`
:* simple type specifier
::*`cpp/keyword/char`, <sup>(since C++20)</sup> `cpp/keyword/char8_t`,  <sup>(since C++11)</sup> `cpp/keyword/char16_t`, `cpp/keyword/char32_t`,  `cpp/keyword/wchar_t`, `cpp/keyword/bool`, `cpp/keyword/short`, `cpp/keyword/int`, `cpp/keyword/long`, `cpp/keyword/signed`, `cpp/keyword/unsigned`, `cpp/keyword/float`, `cpp/keyword/double`, `cpp/keyword/void`
rev|since=c++11|
::*`auto`
::*`decltype specifier`
rev|since=c++26|
::*`pack indexing specifier`
::*`splice type specifier`
::* previously declared class name (optionally `qualified`)
::* previously declared enum name (optionally `qualified`)
::* previously declared `typedef-name`<sup>(since C++11)</sup>  or `type alias` (optionally `qualified`)
::* template name with template arguments (optionally `qualified`, optionally using `template disambiguator`)
rev|since=c++17|
::*template name without template arguments (optionally `qualified`): see `class template argument deduction`
:* `elaborated type specifier`
::* the keyword `cpp/keyword/class`, `cpp/keyword/struct`, or `cpp/keyword/union`, followed by the identifier (optionally `qualified`), previously defined as the name of a class.
::* the keyword `cpp/keyword/class`, `cpp/keyword/struct`, or `cpp/keyword/union`, followed by template name with template arguments (optionally `qualified`, optionally using ``template` disambiguator`), previously defined as the name of a class template.
::* the keyword `cpp/keyword/enum` followed by the identifier (optionally `qualified`), previously declared as the name of an enumeration.
:* ``typename` specifier`
:* `cv qualifier`
:only one type specifier is allowed in a decl-specifier-seq, with the following exceptions:
:* `const` can be combined with any type specifier except itself.
:* `volatile` can be combined with any type specifier except itself.
:* `signed` or `unsigned` can be combined with `char`, `long`, `short`, or `int`.
:* `short` or `long` can be combined with `int`.
:* `long` can be combined with `double`.
rrev|since=c++11|
:* `long` can be combined with `long`.
`Attributes` may appear in *decl-specifier-seq*, in which case they apply to the type determined by the preceding specifiers.
Repetitions of any specifier in a *decl-specifier-seq*, such as `const static const`, or `virtual inline virtual` are errors<sup>(since C++11)</sup> , except that `long` is allowed to appear twice.

## Declarators

Each *init-declarator* in an *init-declarator-list* `S D1, D2, D3;` is processed as if it were a standalone declaration with the same specifiers: `S D1; S D2; S D3;`.
Each declarator introduces exactly one object, reference, function, or (for typedef declarations) type alias, whose type is provided by *decl-specifier-seq* and optionally modified by operators such as `&` (reference to) or `[]` (array of) or `()` (function returning) in the declarator. These operators can be applied recursively, as shown below.
A *declarator* is one of the following:

**Syntax:**

- `sdsc|num=1|`
- `*unqualified-id* *attr* (optional)`
- `sdsc|num=2|`
- `*qualified-id* *attr* (optional)`
- `|`
- `**`...`** *identifier* *attr* (optional)`
- `sdsc|num=4|`
- `**`*`** *attr* (optional) *cv* (optional) *declarator*`
- `sdsc|num=5|`
- `*nested-name-specifier* **`*`** *attr* (optional) *cv* (optional) *declarator*`
- `sdsc|num=6|`
- `**`&`** *attr* (optional) *declarator*`
- `|`
- `**`&&`** *attr* (optional) *declarator*`
- `sdsc|num=8|`
- `*noptr-declarator* **`[`** *constexpr* (optional) **`]`** *attr* (optional)`
- `sdsc|num=9|`
- `*noptr-declarator* **`(`** *parameter-list* **`)`** *cv* (optional) *ref* (optional) *except* (optional) *attr* (optional)`
1. The `name` that is declared.
2. A declarator that uses a `qualified identifier` (*qualified-id*) defines or redeclares a previously declared `namespace member` or `class member`.
3. `Parameter pack`, only appears in `parameter declarations`.
4. `Pointer declarator`: the declaration `S * D;` declares `D` as a pointer to the type determined by *decl-specifier-seq* `S`.
5. `Pointer to member declaration`: the declaration `S C::* D;` declares `D` as a pointer to member of `C` of type determined by *decl-specifier-seq* `S`. *nested-name-specifier* is a `sequence of names and scope resolution operators **`::`**`
6. `Lvalue reference declarator`: the declaration `S & D;` declares `D` as an lvalue reference to the type determined by *decl-specifier-seq* `S`.
7. `Rvalue reference declarator`: the declaration `S && D;` declares `D` as an rvalue reference to the type determined by *decl-specifier-seq* `S`.
8. `Array declarator`. *noptr-declarator* any valid declarator, but if it begins with *, &, or &&, it has to be surrounded by parentheses.
9. `Function declarator`. *noptr-declarator* any valid declarator, but if it begins with *, &, or &&, it has to be surrounded by parentheses. <sup>(since C++11)</sup> It may end with the optional trailing return type.
rrev|since=c++11|
In all cases, *attr* is an optional sequence of `attributes`. When appearing immediately after the identifier, it applies to the object being declared.
*cv* is a sequence of `const and volatile` qualifiers, where either qualifier may appear at most once in the sequence.

## Notes

When a *block-declaration* appears `inside a block`, and an identifier introduced by a declaration was previously declared in an outer block, the `outer declaration is hidden` for the remainder of the block.
If a declaration introduces a variable with automatic storage duration, it is initialized when its declaration statement is executed. All automatic variables declared in a block are destroyed on exit from the block (regardless how the block is exited: via `exception`, `goto`, or by reaching its end), in order opposite to their order of initialization.

## Example


### Example

```cpp
#include <type_traits>

struct S
{
    int member;
    // decl-specifier-seq is "int"
    // declarator is "member"
} obj, *pObj(&obj);
// decl-specifier-seq is "struct S { int member; }"
// declarator "obj" declares an object of type S
// declarator "*pObj" declares a pointer to S,
//     and initializer "(&obj)" initializes it

int i = 1, *p = nullptr, f(), (*pf)(double);
// decl-specifier-seq is "int"
// declarator "i" declares a variable of type int,
//     and initializer "= 1" initializes it
// declarator "*p" declares a variable of type int*,
//     and initializer "= nullptr" initializes it
// declarator "f()" declares (but doesn't define)
//     a function taking no arguments and returning int
// declarator "(*pf)(double)" declares a pointer to function
//     taking double and returning int

int (*(*var1)(double))[3] = nullptr;
// decl-specifier-seq is "int"
// declarator is "(*(*var1)(double))[3]"
// initializer is "= nullptr"

// 1. declarator "(*(*var1)(double))[3]" is an array declarator:
//    Type declared is: "(*(*var1)(double))" array of 3 elements
// 2. declarator "(*(*var1)(double))" is a pointer declarator:
//    Type declared is: "(*var1)(double)" pointer to array of 3 elements
// 3. declarator "(*var1)(double)" is a function declarator:
//    Type declared is: "(*var1)" function taking "(double)",
//    returning pointer to array of 3 elements.
// 4. declarator "(*var1)" is a pointer declarator:
//    Type declared is: "var1" pointer to function taking "(double)",
//    returning pointer to array of 3 elements.
// 5. declarator "var1" is an identifier.
// This declaration declares the object var1 of type "pointer to function
// taking double and returning pointer to array of 3 elements of type int"
// The initializer "= nullptr" provides the initial value of this pointer.

// C++11 alternative syntax:
auto (*var2)(double) -> int (*)[3] = nullptr;
// decl-specifier-seq is "auto"
// declarator is "(*var2)(double) -> int (*)[3]"
// initializer is "= nullptr"

// 1. declarator "(*var2)(double) -> int (*)[3]" is a function declarator:
//    Type declared is: "(*var2)" function taking "(double)", returning "int (*)[3]"
// ...

int main()
{
    static_assert(std::is_same_v<decltype(var1), decltype(var2)>);
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-482 | C++98 | the declarators of redeclarations could not be qualified | qualified declarators allowed |
| cwg-569 | C++98 | a single standalone semicolon was not a valid declaration | it is an empty declaration,<br>which has no effect |


## See also

