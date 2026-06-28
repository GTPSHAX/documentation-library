---
title: Identifiers
type: Language
source: https://en.cppreference.com/w/cpp/language/identifiers
---


# Identifiers

An ''identifier'' is an arbitrarily long sequence of digits, underscores, lowercase and uppercase Latin letters, and most Unicode characters.

## Syntax

The first character of a valid identifier must be one of the following:
* uppercase Latin letters A-Z
* lowercase Latin letters a-z
* underscore
* any Unicode character with the Unicode property [https://www.unicode.org/reports/tr31/#Table_Lexical_Classes_for_Identifiers XID_Start]
Any other character of a valid identifier must be one of the following:
* digits 0-9
* uppercase Latin letters A-Z
* lowercase Latin letters a-z
* underscore
* any Unicode character with the Unicode property [https://www.unicode.org/reports/tr31/#Table_Lexical_Classes_for_Identifiers XID_Continue]
The lists of characters with properties XID_Start and XID_Continue can be found in [https://www.unicode.org/Public/UCD/latest/ucd/DerivedCoreProperties.txt DerivedCoreProperties.txt].
Identifiers are case-sensitive (lowercase and uppercase letters are distinct), and every character is significant. Every identifier must conform to [https://www.unicode.org/charts/normalization/ Normalization Form C].
Note: Support of Unicode identifiers is limited in most implementations, e.g. [https://gcc.gnu.org/wiki/FAQ#What_is_the_status_of_adding_the_UTF-8_support_for_identifier_names_in_GCC.3F gcc (until 10)].

## In declarations

An identifier can be used `to name` objects, references, functions, enumerators, types, class members, namespaces, templates, template specializations,<sup>(since C++11)</sup>  parameter packs, goto labels, and other entities, with the following exceptions:
* The identifiers that are keywords cannot be used for other purposes.
rrev|since=c++11|
:* The only place they can be used as non-keywords is in an *attribute-token* (e.g. `private` is a valid `attribute`).
* The identifiers that are `alternative representations` for certain operators and punctuators cannot be used for other purposes.
rrev|since=c++11|
* The identifiers with special meaning (`final`<sup>(since C++20)</sup> , `import`, `module` and `override`) are used explicitly in a certain context rather than being regular identifiers.
** Unless otherwise specified, any ambiguity as to whether a given identifier has a special meaning is resolved to interpret the token as a regular identifier.
* Identifiers <sup>(since C++11)</sup> that appear as a token or preprocessing token (i.e., not in *user-defined-string-literal like `operator ""id`)* of one of the following forms are reserved:
** in the global namespace, identifiers that begin with an underscore
** identifiers that contain a double underscore or begin with an underscore followed by an uppercase letter, except the following identifiers:
::* <sup>(since C++20)</sup>  (including language feature test macros)
rrev|since=c++11|
::* `std::_Exit`
::* ``__func__``
::* the following macros defined in the standard library:
:::* the C-style I/O library macros <sup>(since C++26)</sup> `_PRINTF_NAN_LEN_MAX`, `_IOFBF`, `_IOLBF` and `_IONBF`
rev|since=c++11|
:::* the C compatibility macros `__alignas_is_defined` and `__alignof_is_defined` (defined in `cpp/header/cstdalign|<stdalign.h>`)
:::* the C compatibility macro `__bool_true_false_are_defined` (defined in `cpp/header/cstdbool|<stdbool.h>`)
rev|since=c++20|
:::* library feature test macros
“Reserved” here means that the standard library headers `#define` or declare such identifiers for their internal needs, the compiler may predefine non-standard identifiers of that kind, and that name mangling algorithm may assume that some of these identifiers are not in use. If the programmer uses such identifiers, the program is ill-formed, no diagnostic required.
In addition, it is undefined behavior to `#define` or `#undef` certain names in a translation unit, see reserved macro names for more details.

### Zombie identifiers

As of C++14, some identifiers are removed from the C++ standard library. They are listed in the list of zombie names.
However, these identifiers are still reserved for previous standardization in a certain context. Removed member function names may not be used as a name for function-like macros, and other removed member names may not be used as a name for object-like macros in portable code.

## In expressions

An identifier that names a variable, a function, <sup>(since C++20)</sup> specialization of a `concept,` or an enumerator can be used as an `expression`. The result of an expression consisting of just the identifier is the entity named by the identifier. The `value category` of the expression is ''lvalue'' if the identifier names a function, a variable<sup>(since C++20)</sup> , a `template parameter object`, or a data member, and <sup>(until C++11)</sup> ''rvalue''<sup>(since C++11)</sup> ''prvalue'' otherwise (e.g. an `enumerator` is <sup>(until C++11)</sup> an rvalue<sup>(since C++11)</sup> a prvalue expression<sup>(since C++20)</sup> , a specialization of a concept is a bool prvalue).

### Type

The type of an identifier expression is the same as the type of the entity it names.
rrev|since=c++11|
The following exceptions exist:
* If the entity named by the (unqualified) identifier is a local entity, and would result in an intervening `lambda expression` capturing it by copy if it were named outside of an unevaluated operand in the declarative region in which the identifier appears, then the type of the expression is the type of a `class member access expression` naming the non-static data member that would be declared for such a capture in the closure object of the innermost such intervening lambda expression.

```cpp
void f()
{
    float x, &r = x;

    [=]
    {
        decltype(x) y1;        // y1 has type float
        decltype((x)) y2 = y1; // y2 has type float const& because this lambda
                               // is not mutable and x is an lvalue
        decltype(r) r1 = y1;   // r1 has type float&
        decltype((r)) r2 = y2; // r2 has type float const&
    };
}
```

rrev|since=c++20|
* If the entity named is a  for a template parameter of type `T`, the type of the expression is `const T`.

### Unqualified identifiers

Besides suitably declared identifiers, the following can be used in expressions in the same role:
* an `overloaded operator` name in function notation, such as `operator+` or `operator new`;
* a `user-defined conversion function` name, such as `operator bool`;
rrev|since=c++11|
* a `user-defined literal operator` name, such as `operator "" _km`;
* a `template` name followed by its argument list, such as `MyTemplate<int>`;
* the character `~` followed by a class name, such as `~MyClass`;
rrev|since=c++11|
* the character `~` followed by a `decltype` specifier, such as `~decltype(str)`.
rrev|since=c++26|
* the character `~` followed by a , such as `~pack...[0]`.
Together with identifiers they are known as ''unqualified identifier expressions''.

### Qualified identifiers

A ''qualified identifier expression'' is an unqualified identifier expression prepended by a scope resolution operator `::`, and optionally, a sequence of any of the following separated by scope resolution operators:
* a namespace name;
* a class name;
rrev|since=c++11|
* an enumeration name;
* a ``decltype` specifier` denoting a class or enumeration type.
rrev|since=c++26|
* a  denoting a class or enumeration type.
* a `splice specifier` designating a class or enumeration type, or a namespace.
* a `splice specifier` designating a class template or alias template, followed by a template argument list, collectively denoting a class or enumeration type.
For example, the expression `std::string::npos` is an expression that names the static member `npos` in the class `string` in namespace `std`. The expression `::tolower` names the function `tolower` in the global namespace. The expression `::std::cout` names the global variable `cout` in namespace `std`, which is a top-level namespace. The expression `boost::signals2::connection` names the type `connection` declared in namespace `signals2`, which is declared in namespace `boost`.
The keyword `cpp/keyword/template` may appear in qualified identifiers as necessary to disambiguate `dependent template names`.
See `qualified lookup` for the details of the name lookup for qualified identifiers.

## Implicit member access transformation

If an identifier expression `E` denotes a non-static non-type member of some class `C` and all following conditions are satisfied, `E` is transformed into the class member access expression `this->E`:
* `E` is not the right operand of a `member access operator`.
* If `E` is a qualified identifier expression, `E` is not the un-parenthesized operand of an `address-of operator`.
* Any of the following conditions is satisfied:
:* `E` is `potentially evaluated`.
:* `C` is the innermost enclosing class at `E`.
:* `C` is a base class of the innermost enclosing class at `E`.
This transformation does not apply in the template definition context (see `dependent name`s).

```cpp
struct X
{
    int x;
};

struct B
{
    int b;
};

struct D : B
{
    X d;

    void func()
    {
        d;   // OK, will be transformed into this->d
        b;   // OK, will be transformed into this->b
        x;   // Error: this->x is ill-formed

        d.x; // OK, will be transformed into this->d.x
             // instead of d.this->x or this->d.this->x
    }
};
```


## Names

A ''name'' is the use of one of the following to refer to an entity:
* an identifier
* an overloaded operator name in function notation (`operator+`, `operator new`)
* a user-defined conversion function name (`operator bool`)
rrev|since=c++11|
* a user-defined literal operator name (`operator ""_km`)
* a template name followed by its argument list (`MyTemplate<int>`)
Every name is introduced into the program by a `declaration`. A name used in more than one translation unit may refer to the same or different entities, depending on .
When the compiler encounters an unknown name in a program, it associates it with the declaration that introduced the name by means of `name lookup`, except for the `dependent name`s in template declarations and definitions (for those names, the compiler determines whether they name a type, a template, or some other entity, which may require `explicit disambiguation`).

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1963 | C++11 | implementation-defined characters other than digits, non-digits<br>and universal character names could be used in an identifier | prohibited |
| cwg-2777 | C++20 | the type of an identifier expression was unclear<br>if it names a template parameter object | made clear |
| cwg-2818 | C++98 | predefined macro names are reserved | they are not reserved |


## See also

