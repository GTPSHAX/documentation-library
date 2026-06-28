---
title: Punctuation
type: Language
source: https://en.cppreference.com/w/cpp/language/punctuators
---


# Punctuation

These are the punctuation symbols in C++. The meaning of each symbol is detailed in the linked pages.

## Preprocessing operators

Preprocessing operators are recognized by s.

### `#`

Alternative spelling is `%:`.
* Introduce a preprocessing directive.
* The preprocessing operator for stringification.

### `##`

Alternative spelling is `%:%:`.
* The preprocessing operator for token pasting.

## Single-character operators and punctuators


### `{` and }

Alternative spellings are `<%` and `%>` respectively.
* In a `class` definition, delimit the .
* In an `enumeration` definition, delimit the enumerator list.
* Delimit a `compound statement`. The compound statement may be part of
:* a
:* a ``try` block`
rrev|since=c++11|
:* a `lambda expression`
* Part of the <sup>(until C++11)</sup> `aggregate initialization`<sup>(since C++11)</sup> `list-initialization` syntax of an `initializer`.
* In a `namespace definition`, delimit the namespace body.
* In a `language linkage specification`, delimit the declarations.
rrev|since=c++20|
* In a ``requires` expression`, delimit the requirements.
* In a `compound requirement`, delimit the expression.
* In an `export declaration`, delimit the declarations.

### `[` and `]`

Alternative spellings are `<:` and `:>` respectively.
* `Subscript operator`; part of `operator[]` in `operator overloading`.
* Part of `array declarator` in a `declaration` or a `type-id` (e.g. in a ``new` expression`).
* Part of `new[]` operator in operator overloading (allocation function).
* Part of `delete[]` operator in `delete expression` and operator overloading (deallocation function).
rev|since=c++11|
* In a `lambda expression`, delimit the `captures`.
* In an `attribute specifier`, delimit the attributes.
rev|since=c++17|
* In a `structured binding declaration`, delimit the identifier list.
rev|since=c++26|
* In a `pack indexing`, delimit `converted constant expression` representing an index.

### `(` and `)`

* In an expression, `indicate grouping`.
* `Function call operator`; part of `operator()` in `operator overloading`.
* In a `function-style type cast`, delimit the expression/initializers.
* In a `static_cast`, `const_cast`, `reinterpret_cast`, or `dynamic_cast`, delimit the expression.
* Delimit the operand of the following operators:
:* `typeid`
:* `sizeof`
rrev|since=c++11|
:* `sizeof...`
:* `alignof`
:* `noexcept`
* In a `placement `new` expression`, delimit the placement arguments.
* In a ``new` expression`, optionally delimit the type-id.
* In a ``new` expression`, delimit the initializers.
* In a `C-style cast`, delimit the type-id.
* In a `declaration` or a `type-id`, indicate grouping.
* Delimit the parameter list in
:* a `function declarator` (in a `declaration` or a `type-id`)
rev|since=c++11|
:* a `lambda expression`
rev|since=c++17|
:* a `user-defined deduction guide`
rev|since=c++20|
:* a ``requires` expression`
* Part of the `direct-initialization` syntax of an `initializer`.
* In an `asm declaration`, delimit the string literal.
* In a `member initializer list`, delimit the initializers to a base or member.
* Delimit the controlling clause of a selection statement or iteration statement, including:
:* `if`<sup>(since C++23)</sup>  (except
:* `switch`
:* `while`
:* `do-while`
:* `for`
rrev|since=c++11|
:* `range-based `for``
* In a `handler`, delimit the parameter declaration.
* In a function-like macro definition, delimit the macro parameters.
* In a function-like macro invocation, delimit the macro arguments or prevent commas from being interpreted as argument separators.
* Part of a `defined`<sup>(since C++17)</sup> , `__has_include`<sup>(since C++20)</sup> , `__has_cpp_attribute` preprocessing operator.
rev|since=c++11|
* In a `static_assert` declaration, delimit the operands.
* Delimit the operand of the following specifiers:
:* `decltype`
:* `noexcept`
:* `alignas`
rrev|since=c++20|
:* `explicit`
* In an `attribute`, delimit the attribute arguments.
rev|since=c++14|
* Part of `decltype(auto)` specifier.
rev|since=c++17|
* Delimit a `fold expression`.
rev|since=c++20|
* Part of `cpp/preprocessor/replace|__VA_OPT__` replacement in a variadic macro definition.

### `;`

* Indicate the end of
:* a `statement`
:* a `declaration` or `member declaration`
rrev|since=c++20|
:* a `module declaration`, import declaration, global module fragment introducer, or private module fragment introducer
:* a `requirement`
* Separate the *condition* and *statement* of a ``for` statement`.

### `:`

* Part of .
* Part of `label declaration`.
* In the *base-clause* of a `class definition`, introduce the `base class`.
* Part of `access specifier` in member specification.
* In a `bit-field member declaration`, introduce the width.
* In a `constructor` definition, introduce the member initializer list.
rev|since=c++11|
* In a `range-based `for`` statement, separate the *item-declaration* and the *range-initializer*.
* In the *enum-base* of an `enumeration declaration`, introduce the underlying type.
rev|since=c++17|
* In an `attribute specifier`, separate the *attribute-namespace* and the *attribute-list*.
rev|since=c++20|
* In a `module declaration` or import declaration of module partition, introduce the module partition name.
* Part of a  introducer (`module :private;`).

### `?`

* Part of .

### `.`

* `Member access operator`.
rrev|since=c++20|
* In `aggregate initialization`, introduce a designator.
* Part of `module name or module partition name`.

### `~`

Alternative spelling is `compl`.
* `Unary complement operator (a.k.a. bitwise not operator)`; part of `operator~` in `operator overloading`.
* Part of an `identifier expression` to name a `destructor` or pseudo-destructor.

### `!`

Alternative spelling is `not`.
* `Logical not operator`; part of `operator!` in `operator overloading`.
rrev|since=c++23|
* Part of  statement.

### `+`

* `Unary plus operator`; part of `operator+` in `operator overloading`.
* `Binary plus operator`; part of `operator+` in `operator overloading`.

### `-`

* `Unary minus operator`; part of `operator-` in `operator overloading`.
* `Binary minus operator`; part of `operator-` in `operator overloading`.

### `*`

* `Indirection operator`; part of `operator*` in `operator overloading`.
* `Multiplication operator`; part of `operator*` in `operator overloading`.
* Pointer operator or part of pointer-to-member operator in a `declarator` or in a `type-id`.
rrev|since=c++17|
* Part of `*this` in a  list, to capture the current object by copy.

### `/`

* `Division operator`; part of `operator/` in `operator overloading`.

### `%`

* `Modulo operator`; part of `operator%` in `operator overloading`.

### `^`

Alternative spelling is `xor`.
* `Bitwise xor operator`; part of `operator^` in `operator overloading`.

### `&`

Alternative spelling is `bitand`.
* `Address-of operator`; part of `operator&` in `operator overloading`.
* `Bitwise and operator`; part of `operator&` in `operator overloading`.
* Lvalue-reference operator in a `declarator` or in a `type-id`.
rrev|since=c++11|
* In a , indicate by-reference capture.
* `Ref-qualifier` in `member function declaration`.

### `

Alternative spelling is `bitor`.
* `Bitwise or operator`; part of `operator in `operator overloading`.

### `1==`

* `Simple assignment operator`; part of `1=operator=` in `operator overloading`, which might be a special member function (`copy assignment operator`<sup>(since C++11)</sup> or `move assignment operator`).
* Part of the `copy-initialization` and <sup>(until C++11)</sup> `aggregate initialization`<sup>(since C++11)</sup> `copy-list-initialization` syntax of an `initializer`.
* In a `function declaration`, introduce a `default argument`.
* In a `template parameter list`, introduce a `default template argument`.
* In a `namespace alias definition`, separate the alias and the aliased namespace.
* In an `enum definition`, introduce the value of enumerator.
* Part of *pure-specifier* in a `pure virtual function declaration`.
rev|since=c++11|
* Capture default in , to indicate by-copy capture.
* Part of defaulted definition (`1==default;`) or deleted definition (`1==delete;`) in `function definition`.
* In a `type alias declaration`, separate the alias and the aliased type.
rev|since=c++20|
* In a `concept definition`, separate the concept name and the constraint expression.

### `<`

* `Less-than operator`; part of `operator<` in `operator overloading`.
* In a `static_cast`, `const_cast`, `reinterpret_cast`, or `dynamic_cast`, introduce the type-id.
* Introduce a `template argument list`.
* Introduce a `template parameter list` in
:* a `template declaration`
:* a `partial specialization`
rrev|since=c++20|
:* a `lambda expression`
* Part of `template<>` in `template specialization declaration`.
* Introduce a header name in
:* a `#include` directive
rev|since=c++17|
:* a `__has_include` preprocessing expression
rev|since=c++20|
:* an ``import` declaration`

### `>`

* `Greater-than operator`; part of `operator>` in `operator overloading`.
* `static_cast`, `const_cast`, `reinterpret_cast`, or `dynamic_cast`, indicate the end of type-id.
* Indicate the end of a `template argument list`.
* Indicate the end of a `template parameter list` in
:* a `template declaration`
:* a `partial specialization`
rrev|since=c++20|
:* a `lambda expression`
* Part of `template<>` in `template specialization declaration`.
* Indicate the end of a header name in
:* a `#include` directive
rev|since=c++17|
:* a `__has_include` preprocessing expression
rev|since=c++20|
:* an ``import` declaration`

### `,`

* `Comma operator`; part of `operator,` in `operator overloading`.
* List separator in
:* the declarator list in a `declaration`
:* initializer list in `initialization`
:* the placement argument list in a `placement new`
:* the argument list in a `function call expression`
:* the enumerator list in an `enum` declaration
:* the `base class` list in a `class` declaration
:* the member initializer list in a `constructor` definition
:* a `function parameter list`
:* a `template parameter list`
:* a `template argument list`
rev|since=c++11|
:* a  list
:* an `attribute` list
rev|since=c++17|
:* the declarator list in a `using-declaration`
:* the identifier list in a `structured binding` declaration
rev|since=c++23|
:* the argument list in a `multi-argument subscript expression`
:* the macro parameter list in a function-like macro definition
:* the macro argument list in a function-like macro invocation, unless found between the parentheses of an argument
rrev|since=c++11|
* In a `static_assert` declaration, separate the arguments.

## Multi-character operators and punctuators


### `[:` and `:]` <sup>(C++26)</sup>

* Delimit a `splice specifier`.

### `^^` <sup>(C++26)</sup>

* `Reflection operator`.

### `...`

* In the  of a function declarator<sup>(since C++11)</sup>  or lambda expression<sup>(since C++17)</sup>  or user-defined deduction guide, signify a `variadic function`.
* In a `handler`, signify catch-all handler.
rev|since=c++11|
* In a macro definition, signify a variadic macro.
* Indicate `pack` declaration and expansion.
rev|since=c++26|
* In `pack indexing` expression and specifier.

### `::`

* Scope resolution operator in
:* a `qualified name`
:* a `pointer-to-member declaration`
:* a `new` or `delete` expression, to indicate that only global allocation or deallocation functions are looked up
rev|since=c++11|
* In an `attribute`, indicate attribute scope.
rev|since=c++17|
* Part of `nested namespace definition`.

### `.*`

* `Pointer-to-member access operator`.

### `->`

* `Member access operator`; part of `operator->` in `operator overloading`.
rev|since=c++11|
* In a `function declarator` or `lambda expression`, introduce the trailing return type.
rev|since=c++17|
* In a `user-defined deduction guide`, introduce the result type.
rev|since=c++20|
* In a `compound requirement`, introduce the return type requirement.

### `->*`

* `Pointer-to-member access operator`; part of `operator->*` in `operator overloading`.

### `1=+=`

* `Compound assignment operator`; part of `1=operator+=` in `operator overloading`.

### `1=-=`

* `Compound assignment operator`; part of `1=operator-=` in `operator overloading`.

### `1=*=`

* `Compound assignment operator`; part of `1=operator*=` in `operator overloading`.

### `1=/=`

* `Compound assignment operator`; part of `1=operator/=` in `operator overloading`.

### `1=%=`

* `Compound assignment operator`; part of `1=operator%=` in `operator overloading`.

### `1=^=`

Alternative spelling is `xor_eq`.
* `Compound assignment operator`; part of `1=operator^=` in `operator overloading`.

### `1=&=`

Alternative spelling is `and_eq`.
* `Compound assignment operator`; part of `1=operator&=` in `operator overloading`.

### `

Alternative spelling is `or_eq`.
* `Compound assignment operator`; part of `operator in `operator overloading`.

### `1===`

* `Equality operator`; part of `1=operator==` in `operator overloading`.

### `1=!=`

Alternative spelling is `not_eq`.
* `Inequality operator`; part of `1=operator!=` in `operator overloading`.

### `1=<=`

* `Less-than-or-equal-to operator`; part of `1=operator<=` in `operator overloading`.

### `1=>=`

* `Greater-than-or-equal-to operator`; part of `1=operator>=` in `operator overloading`.
rrev|since=c++20|

### `1=<=>`

* `Three-way comparison (spaceship) operator`; part of `1=operator<=>` in `operator overloading`.

### `&&`

Alternative spelling is `and`.
* `Logical and operator`; part of `operator&&` in `operator overloading`.
rrev|since=c++11|
* Rvalue-reference operator in a `declarator` or in a `type-id`.
* `Ref-qualifier` in `member function declaration`.

### `

Alternative spelling is `or`.
* `Logical or operator`; part of `operator in `operator overloading`.

### `<<`

* `Bitwise shift operator`; part of `operator<<` in operator overloading (`bitwise operator` or `stream insertion operator`).

### `>>`

* `Bitwise shift operator`; part of `operator>>` in operator overloading (`bitwise operator` or `stream extraction operator`).

### `1=<<=`

* `Compound assignment operator`; part of `1=operator<<=` in `operator overloading`.

### `1=>>=`

* `Compound assignment operator`; part of `1=operator>>=` in `operator overloading`.

### `++`

* `Increment operator`; part of `operator++` in `operator overloading`.

### `--`

* `Decrement operator`; part of `operator--` in `operator overloading`.

## References


## See also


| cpp/language/dsc operator alternative | (see dedicated page) |

