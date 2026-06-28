---
title: Variadic arguments
type: Language
source: https://en.cppreference.com/w/cpp/language/variadic_arguments
---


# Variadic arguments

Allows a function to accept any number of extra arguments.
A function is a variadic if the last parameter of its  is an ellipsis (`...`).
<tr class="t-rev">
<td>The comma preceding the ellipsis can be omitted.</td>
<td><sup>(deprecated C++26)</sup></td>
</tr>

```cpp
// the function declared as follows
int printx(const char* fmt, ...);
int printx(const char* fmt...); // same as above, but deprecated since C++26

// may be called with one or more arguments:
printx("hello world");
printx("a=%d b=%d", a, b);

int printy(..., const char* fmt); // error: ... can only be the last parameter
int printz(...); // valid, but the arguments cannot be accessed portably <!-- before C++26 per P2537 -->
```

rrev|since=c++11|
This is different from a function `parameter pack` expansion, which is indicated by an ellipsis that is a part of a parameter declarator, rather than an ellipsis being a parameter alone. Both parameter pack expansion and the “variadic” ellipsis may appear in the declaration of a function template, as in the case of `std::is_function`.

## Default argument promotions

When a variadic function is called, after lvalue-to-rvalue, array-to-pointer, and function-to-pointer `conversions`, each argument that is a part of the variable argument list undergoes additional conversions known as ''default argument promotions'':
rrev|since=c++11|
* `std::nullptr_t` is converted to `void*`.
* `float` arguments are converted to `double` as in .
* `bool`, `char`, `short`, and unscoped enumerations are converted to `int` or wider integer types as in .
<sup>(until C++11)</sup> Non-POD class types<sup>(since C++11)</sup> Scoped enumerations and class types with an eligible non-trivial copy constructor, an eligible non-trivial move constructor, or a non-trivial destructor are conditionally-supported in potentially-evaluated calls with implementation-defined semantics (these types are always supported in `unevaluated calls`).
Because variadic parameters have the lowest rank for the purpose of `overload resolution`, they are commonly used as the catch-all fallbacks in `SFINAE`.
Within the body of a function that uses variadic arguments, the values of these arguments may be accessed using the `<cstdarg>` library facilities:


| cstdarg | |
| cpp/utility/variadic/dsc va_start | (see dedicated page) |
| cpp/utility/variadic/dsc va_arg | (see dedicated page) |
| cpp/utility/variadic/dsc va_copy | (see dedicated page) |
| cpp/utility/variadic/dsc va_end | (see dedicated page) |
| cpp/utility/variadic/dsc va_list | (see dedicated page) |

The behavior of the `va_start` macro is undefined if the last parameter before the ellipsis has reference type, or has type that is not  with the type that results from default argument promotions.
rrev|since=c++11|
If the a  or an entity resulting from a  is used as the last parameter in `va_start`, the program is ill-formed, no diagnostic required.

## Alternatives

rrev|since=c++11|
* `Variadic templates` can also be used to create functions that take variable number of arguments.  They are often the better choice because they do not impose restrictions on the types of the arguments, do not perform integral and floating-point promotions, and are type safe.
* If all variable arguments share a common type, a `std::initializer_list` provides a convenient mechanism (albeit with a different syntax) for accessing variable arguments. In this case however the arguments cannot be modified since `std::initializer_list` can only provide a const pointer to its elements.

## Notes

In the C programming language until C23, at least one named parameter must appear before the ellipsis parameter, so `R printz(...);` is not valid until C23. In C++, this form is allowed even though the arguments passed to such function are not accessible, and is commonly used as the fallback overload in `SFINAE`, exploiting the lowest priority of the ellipsis conversion in `overload resolution`.
This syntax for variadic arguments was introduced in 1983 C++ without the comma before the ellipsis. When C89 adopted function prototypes from C++, it replaced the syntax with one requiring the comma. For compatibility, C++98 accepts both C++-style `f(int n...)` and C-style `f(int n, ...)`. The original C++-style grammar is deprecated since C++26.
rrev|since=c++20|
The comma can be used in abbreviated function templates to make the ellipsis signify a variadic function instead of a variadic template:
c multi
|void f1(auto...);   // same as template<class... Ts> void f3(Ts...)
|void f2(auto, ...); // same as template<class T> void f3(T, ...)

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-506 | C++98 | passing non-POD class arguments to an<br>ellipsis resulted in undefined behavior | passing such arguments is<br>conditionally-supported with<br>implementation-defined semantics |
| cwg-634 | C++98 | conditionally-supported class types<br>made some SFINAE idioms not work | always supported if unevaluated |
| cwg-2347 | C++11 | it was unclear whether scoped enumerations passed to<br>an ellipsis are subject to default argument promotions | passing scoped enumerations<br>is conditionally-supported with<br>implementation-defined semantics |


## See also

