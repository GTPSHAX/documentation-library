---
title: Expressions
type: Language
source: https://en.cppreference.com/w/cpp/language/expressions
---


# Expressions

An expression is a sequence of ''operators'' and ''operands'', that specifies a computation.
Expression evaluation may produce a result (e.g., evaluation of `2 + 2` produces the result `4`) and may generate side-effects (e.g. evaluation of `std::printf("%d", 4)` prints the character `'4'` on the standard output).
Each C++ expression is characterized by two independent properties: A type and a value category.

### General

* `value categories` (lvalue, rvalue<sup>(since C++11)</sup> , glvalue, prvalue, xvalue) classify expressions by their values
* `order of evaluation` of arguments and subexpressions specify the order in which intermediate results are obtained

## Operators

* `operator precedence` defines the order in which operators are bound to their arguments
* `alternative representations` are alternative spellings for some operators
* `operator overloading` makes it possible to specify the behavior of the operators with user-defined classes.

### Conversions

* `standard conversions` implicit conversions from one type to another
* ``const_cast` conversion`
* ``static_cast` conversion`
* ``dynamic_cast` conversion`
* ``reinterpret_cast` conversion`
* `explicit cast` conversion using C-style cast notation and function-style notation
* `user-defined conversion` makes it possible to specify conversion from user-defined classes

### Memory allocation

* `new expression` allocates memory dynamically
* `delete expression` deallocates memory dynamically

### Other

* `constant expression`s can be evaluated at compile time and used in compile-time context (template arguments, array sizes, etc)
* `sizeof`
* `alignof`
* `typeid`
* `throw-expression`

## Primary expressions

The operands of any operator may be other expressions or primary expressions (e.g. in `1 + 2 * 3`, the operands of operator+ are the subexpression `2 * 3` and the primary expression `1`).
Primary expressions are any of the following:
* `this`
* literals (e.g. `2` or `"Hello, world"`)
* identifier expressions, including
** suitably declared  (e.g. `n` or `cout`),
** suitably declared  (e.g. `std::string::npos`), and
** identifiers to be declared in
rrev|since=c++26|
:*
rev|since=c++11|
* `lambda expressions`
rev|since=c++17|
* `fold expressions`
rev|since=c++20|
* `requires expressions`
rev|since=c++26|
* `splice expressions`
Any expression in parentheses is also classified as a primary expression: this guarantees that the parentheses have higher precedence than any operator. Parentheses preserve value, type, and value category.

### Literals

Literals are the tokens of a C++ program that represent constant values embedded in the source code.
* `integer literal`s are decimal, octal, hexadecimal or binary numbers of integer type.
* `character literal`s are individual characters of type
:* `char` or `wchar_t`
rev|since=c++11|
:* `char16_t` or `char32_t`
rev|since=c++20|
:* `char8_t`
* `floating-point literals` are values of type `float`, `double`, or `long double`
* `string literal`s are sequences of characters of type
:* `const char[]` or `const wchar_t[]`
rev|since=c++11|
:* `const char16_t[]` or `const char32_t[]`
rev|since=c++20|
:* `const char8_t[]`
* `boolean literals` are values of type `bool`, that is `true` and `false`
rrev|since=c++11|
* `nullptr` is the pointer literal which specifies a null pointer value
* `user-defined literals` are constant values of user-specified type

## Full-expressions

The following expressions are :
* unevaluated operands
* `constant expression`s
rrev|since=c++20|
* `immediate invocations`
* declarators of s or `member initializers`, including the ''constituent expressions'' of the initializers
* invocations of `destructor`s generated at the end of the `lifetime` of objects other than temporary objects whose lifetime have not been extended
rrev|since=c++26|
* the predicates of `contract assertions`
* expressions that are not a ''subexpression'' of any another expression and that are not otherwise part of any full-expression
If a language construct is defined to produce an implicit call of a function, a use of the language construct is considered to be an expression for the purposes of this definition. Conversions applied to the result of an expression in order to satisfy the requirements of the language construct in which the expression appears are also considered to be part of the full-expression.
For an initializer, performing the initialization of the entity <sup>(since C++14)</sup> (including evaluating default member initializers of an aggregate) is also considered part of the full-expression.
A ''subexpression'' of an expression `E` is an ''immediate subexpression'' of `E` or a subexpression of an ''immediate subexpression'' of `E`. <sup>(since C++11)</sup> Note that expressions appearing in the “function body” of lambda expressions are not subexpressions of the lambda expression.
The ''immediate subexpressions'' of an expression `E` are
* the ''constituent expressions'' of `E`’s operands,
rev|since=c++14|
* if `E` creates an `aggregate` object, the constituent expressions of each `default member initializer` used in the initialization,
rev|since=c++11|
* if `E` is a `lambda expression`, the initialization of the entities captured by copy and the constituent expressions of the initializer of the captures,
* any function call that `E` implicitly invokes, or
* if `E` is a function call or implicitly invokes a function, the constituent expressions of each `default argument` used in the call.
A ''constituent expression'' is defined as follows:
* The constituent expression of an expression is that expression.
* The constituent expressions of a `brace-enclosed initializer list` or of a (possibly parenthesized) expression list are the constituent expressions of the elements of the respective list.
* The constituent expressions of an `initializer` that begins with **` are the constituent expressions of the *initializer-clause*.

```cpp
int num1 = 0;
num1 += 1; // Case 1: the constituent expression of “num += 1” is “num += 1”

int arr2[2] = {2, 22} // Case 2: the constituent expressions
                      //         of “{2, 22}” are “2” and “22”
                      // Case 3: the constituent expressions of “= {2, 22}”
                      //         are the constituent expressions of “{2, 22}”
                      //         (i.e. also “2” and “22”)
```


## Potentially-evaluated expressions

rev|until=c++11|
An expression is ''potentially evaluated'' unless
* it is the operand of the `sizeof` operator, or
* it is the operand of the `typeid` operator and does not designate an lvalue of `polymorphic` class type.
rev|since=c++11|
The following operands are ''unevaluated operands'', they are not evaluated:
* expressions which the `typeid` operator applies to, except glvalues of `polymorphic` class types
* expressions which are operands of the `sizeof` operator
* operands of the `noexcept` operator
* operands of the `decltype` specifier
rrev|since=c++20|
* *constraint-expression* of `concept` definitions
* expressions following the `requires` keyword of ``requires` clauses`
* expressions appearing in *requirement-seq* of ``requires` expressions`
rrev|since=c++26|
* operands of the `reflection operator` (`^^`)
An expression is ''potentially evaluated'' unless
* it is an unevaluated operand, or
* it is a subexpression of an unevaluated operand.
Potentially-evaluated expressions are .

## Discarded-value expressions

A ''discarded-value expression'' is an expression that is used for its side-effects only. The value calculated from such expression is discarded. Such expressions include the full-expression of any `expression statement`, the left-hand operand of the built-in comma operator, or the operand of a cast-expression that casts to the type `void`.
Array-to-pointer and function-to-pointer conversions are never applied to the value calculated by a discarded-value expression. The lvalue-to-rvalue conversion is applied if and only if the expression is a `volatile-qualified` glvalue and has one of the following forms (built-in meaning required, possibly parenthesized):
* id-expression,
rrev|since=c++26|
* `splice expression`,
* array subscript expression,
* class member access expression,
* indirection,
* pointer-to-member operation,
* conditional expression where both the second and the third operands are one of these expressions,
* comma expression where the right operand is one of these expressions.
In addition, if the lvalue is of volatile-qualified class type, a volatile copy constructor is required to initialize the resulting rvalue temporary.
rrev|since=c++17|
If the expression is a non-void prvalue (after any lvalue-to-rvalue conversion that might have taken place),  occurs.
Compilers may issue warnings when an expression other than cast to `void` discards a value declared .
<br>
rrev|since=c++20|

## Expression-equivalence

A number of expressions `e1`, `e2`, ..., `eN` are ''expression-equivalent'' if all following conditions are satisfied:
# They have the same effects.
# Either they are all s or neither is.
# Either they are all `noexcept` or else neither is.
`e1` is ''expression-equivalent to'' `e2` if and only if `e1` and `e2` are expression-equivalent (which means `e2` is also expression-equivalent to `e1`).

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1054 | C++98 | assigning a value to a volatile variable might<br>result in an unnecessary read due to the lvalue-to-<br>rvalue conversion applied to the assignment result | introduce discarded-value expressions<br>and exclude this case from the list<br>of cases that require the conversion |
| cwg-1383 | C++98 | the list of expressions where lvalue-to-rvalue<br>conversion is applied to discarded-value<br>expressions also covered overloaded operators | only cover operators<br>with built-in meaning |
| cwg-1576 | C++11 | lvalue-to-rvalue conversions were not applied<br>to discarded-value volatile xvalue expressions | apply the conversion<br>in this case |
| cwg-2249 | C++98 | identifiers to be declared in declarators<br>were not id-expressions | they are |
| cwg-2431 | C++11 | the invocations of the destructors of temporaries that<br>are bound to references were not full-expressions | they are |


## See also

