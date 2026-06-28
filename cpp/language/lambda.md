---
title: Lambda expressions
type: Language
source: https://en.cppreference.com/w/cpp/language/lambda
---


# Lambda expressions mark since c++11

Constructs a [Closure (computer science)|closure](https://en.wikipedia.org/wiki/Closure (computer science)|closure) (an unnamed function object capable of capturing variables in scope).

## Syntax


#### Lambda expressions without an explicit template parameter list (possibly non-generic)


**Syntax:**

- `sdsc|num=1|`
- `**`[`**captures**`]`** *front-attr* (optional) **`(`**params**`)`** *specs* (optional) *except* (optional)<br>*back-attr* (optional) *trailing* (optional) *requires* (optional) *contract-specs* (optional) **`{`** *body* }`
- `|`
- `**`[`**captures**`] {`** *body* }`
- `|`
- `**`[`**captures**`]`** *front-attr* (optional) *trailing* (optional) *contract-specs* (optional) **`{`** *body* }`
- `|`
- `**`[`**captures**`]`** *front-attr* (optional) *except*<br>*back-attr* (optional) *trailing* (optional) *contract-specs* (optional) **`{`** *body* }`
- `|`
- `**`[`**captures**`]`** *front-attr* (optional) *specs* *except* (optional)<br>*back-attr* (optional) *trailing* (optional) *contract-specs* (optional) **`{`** *body* }`

#### Lambda expressions with an explicit template parameter list (always generic) <sup>(C++20)</sup>


**Syntax:**

- `sdsc|num=1|`
- `**`[`**captures**`] <`**tparams**`>`** *t-requires* (optional)<br>*front-attr* (optional) **`(`**params**`)`** *specs* (optional) *except* (optional)<br>*back-attr* (optional) *trailing* (optional) *requires* (optional) *contract-specs* (optional) **`{`** *body* }`
- `|`
- `**`[`**captures**`] <`**tparams**`>`** *t-requires* (optional) **`{`** *body* }`
- `|`
- `**`[`**captures**`] <`**tparams**`>`** *t-requires* (optional)<br>*front-attr* (optional) *trailing* (optional) *contract-specs* (optional) **`{`** *body* }`
- `|`
- `**`[`**captures**`] <`**tparams**`>`** *t-requires* (optional) *front-attr* (optional) *except*<br>*back-attr* (optional) *trailing* (optional) *contract-specs* (optional) **`{`** *body* }`
- `|`
- `**`[`**captures**`] <`**tparams**`>`** *t-requires* (optional) *front-attr* (optional) *specs* *except* (optional)<br>*back-attr* (optional) *trailing* (optional) *contract-specs* (optional) **`{`** *body* }`
1. The lambda expression with a parameter list.
@2-4@ The lambda expression without a parameter list.
:@2@ The simplest syntax. *back-attr* cannot be applied.
:@3,4@ *back-attr* can only be applied if any of *specs* and *except* is present.

## Explanation


### Parameters

- `{{spar` - captures|Specifies the entities to be captured.
- `{{spar` - tparams|A non-empty comma-separated list of `template parameters`, used to provide names to the template parameters of a generic lambda (see `ClosureType::operator()` below).
- `{{spar` - t-requires|Adds `constraints` to *tparams*.
- rrev|since=c++23|
- `t-requires}} ends with an attribute specifier sequence, the attributes in the sequence are treated as attributes in {{spar` - front-attr.
- `{{spar` - front-attr|<sup>(C++23)</sup> An `attribute specifier sequence` applies to `operator()` of the closure type (and thus the  attribute can be used).
- `{{spar` - params|The  of `operator()` of the closure type.
- rrev|since=c++23|
- `{{spar` - specs|A list of the following specifiers, each specifier is allowed at most once in each sequence.
- `{{spar` - except|Provides<sup>(until C++17)</sup>  the `dynamic exception specification or` the `noexcept specifier` for `operator()` of the closure type.
- `{{spar` - back-attr|An `attribute specifier sequence` applies to the type of `operator()` of the closure type (and thus the  attribute cannot be used).
- `{{spar` - trailing|**`->`** *ret*, where *ret* specifies the return type.
- `{{spar` - requires|<sup>(C++20)</sup> Adds `constraints` to `operator()` of the closure type.
- `{{spar` - contract-specs|<sup>(C++26)</sup> A list of  for `operator()` of the closure type.
- `{{spar` - body|The function body.
<sup>(since C++14)</sup> If `auto is used as a type of a parameter<sup>(since C++20)</sup>  or an explicit template parameter list is provided, the lambda is a ''generic lambda''.`
A variable `__func__` is implicitly defined at the beginning of *body*, with semantics as described `here`.

## Closure type

The lambda expression is a prvalue expression of unique unnamed non-`union` non-`aggregate` class type, known as ''closure type'', which is declared (for the purposes of `ADL`) in the smallest block scope, class scope, or namespace scope that contains the lambda expression.
rrev|since=c++20|
The closure type is a `structural` type if and only if *captures* is empty.
The closure type has the following members, they cannot be <sup>(since C++14)</sup> `explicitly instantiated, `template specialization|explicitly specialized`, or` named in a `friend declaration`:
member|operator()(*params*)|2=

```cpp
|1=
ret operator()(params) { body }
|1=
template<template-params>
ret operator()(params) { body }
```

Executes the body of the lambda expression, when invoked. When accessing a variable, accesses its captured copy (for the entities captured by copy), or the original object (for the entities captured by reference).
The parameter list of `operator()` is *params* if it is provided, otherwise the parameter list is empty.
The return type of `operator()` is the type specified in trailing.
If *trailing* is not provided, the return type of `operator()` is automatically `deduced`.
Unless the keyword `mutable` was used in the lambda specifiers<sup>(since C++23)</sup> , or an explicit object parameter is present, the cv-qualifier of `operator()` is `const` and the objects that were captured by copy are non-modifiable from inside this `operator()`. Explicit `const` qualifier is not allowed. `operator()` is never virtual and cannot have the `volatile` qualifier.
rev|since=c++17|
`operator()` is always constexpr if it satisfies the requirements of a `constexpr function`. It is also constexpr if the keyword `constexpr` was used in the lambda specifiers.
rev|since=c++20|
`operator()` is an `immediate function` if the keyword `consteval` was used in the lambda specifiers.
rev|since=c++23|
`operator()` is a `static member function` if the keyword `static` was used in the lambda specifiers.
`operator()` is an `explicit object member function` if *params* contains an explicit object parameter.
rrev|since=c++14|
For each parameter in *params* whose type is specified as `auto`, an invented template parameter is added to *template-params*, in order of appearance. The invented template parameter may be a `parameter pack` if the corresponding function member of *params* is a function parameter pack.
<source style="width:45em; overflow-x: hidden;" lang=cpp>
// generic lambda, operator() is a template with two parameters
auto glambda = [](auto a, auto&& b) { return a < b; };
bool b = glambda(3, 3.14); // OK
// generic lambda, operator() is a template with one parameter
auto vglambda = [](auto printer)
{
return [=](auto&&... ts) // generic lambda, ts is a parameter pack
{
printer(std::forward<decltype(ts)>(ts)...);
// nullary lambda (takes no parameters):
return [=] { printer(ts...); };
};
};
auto p = vglambda([](auto v1, auto v2, auto v3)
{
std::cout << v1 << v2 << v3;
});
auto q = p(1, 'a', 3.14); // outputs 1a3.14
q();                      // outputs 1a3.14
</source>
rrev|since=c++20|
If the lambda definition uses an explicit template parameter list, that template parameter list is used with `operator()`. For each parameter in *params* whose type is specified as `auto`, an additional invented template parameter is appended to the end of that template parameter list:
<source style="width:45em; overflow-x: hidden;" lang=cpp>
// generic lambda, operator() is a template with two parameters
auto glambda = []<class T>(T a, auto&& b) { return a < b; };
// generic lambda, operator() is a template with one parameter pack
auto f = []<typename... Ts>(Ts&&... ts)
{
return foo(std::forward<Ts>(ts)...);
};
</source>
The exception specification *except* on the lambda expression applies to `operator()`.
For the purpose of `name lookup`, determining the type and value of the ``this` pointer` and for accessing non-static class members, the body of the closure type's `operator()` is considered in the context of the lambda expression.

```cpp
struct X
{
    int x, y;
    int operator()(int);
    void f()
    {
        // the context of the following lambda is the member function X::f
        [=]() -> int
        {
            return operator()(this->x + y); // X::operator()(this->x + (*this).y)
                                            // this has type X*
        };
    }
};
```


## Dangling references

If a non-reference entity is captured by reference, implicitly or explicitly, and `operator()` of the closure object is invoked after the entity's lifetime has ended, undefined behavior occurs. The C++ closures do not extend the lifetimes of objects captured by reference.
Same applies to the lifetime of the current `*this` object captured via **`this`**.
member|operator *ret*(*)(*params*)()|2=

```cpp
dcl rev multi
|dcl1=
using F = ret(*)(params);
operator F() const noexcept;
|since2=c++17|dcl2=
using F = ret(*)(params);
constexpr operator F() const noexcept;
dcl rev multi
|since1=c++14|dcl1=
template<template-params> using fptr_t = /* see below */;
template<template-params>
operator fptr_t<template-params>() const noexcept;
|since2=c++17|dcl2=
template<template-params> using fptr_t = /* see below */;
template<template-params>
constexpr operator fptr_t<template-params>() const noexcept;
```

This `user-defined conversion function` is only defined if the lambda expression has no captures<sup>(since C++23)</sup>  and has no explicit object parameter. It is a public, <sup>(since C++17)</sup> constexpr, non-virtual, non-explicit, const noexcept member function of the closure object.
rrev|since=c++20|
This function is an `immediate function` if the function call operator (or specialization, for generic lambdas) is an immediate function.
rrev|since=c++14|
A generic capture-less lambda has a user-defined conversion function template with the same invented template parameter list as  `operator()`.
<source style="width:45em; overflow-x: hidden;" lang=cpp>
void f1(int (*)(int)) {}
void f2(char (*)(int)) {}
void h(int (*)(int)) {}  // #1
void h(char (*)(int)) {} // #2
auto glambda = [](auto a) { return a; };
f1(glambda); // OK
f2(glambda); // error: not convertible
h(glambda);  // OK: calls #1 since #2 is not convertible
int& (*fpi)(int*) = [](auto* a) -> auto& { return *a; }; // OK
</source>
rev|until=c++14|
The value returned by the conversion function is a pointer to a function with C++ `language linkage` that, when invoked, has the same effect as invoking the closure type's function call operator on a default-constructed instance of the closure type.
rev|since=c++14|until=c++23|
The value returned by the conversion function (template) is a pointer to a function with C++ `language linkage` that, when invoked, has the same effect as:
* for non-generic lambdas, invoking the closure type's `operator()` on a default-constructed instance of the closure type.
* for generic lambdas, invoking the generic lambda's corresponding `operator()` specialization on a default-constructed instance of the closure type.
rev|since=c++23|
The value returned by the conversion function (template) is
* if `operator()` is static, a pointer to that `operator()` with C++ `language linkage`,
* otherwise, a pointer to a function with C++ `language linkage` that, when invoked, has the same effect as:
** for non-generic lambdas, invoking the closure type's `operator()` on a default-constructed instance of the closure type.
** for generic lambdas, invoking the generic lambda's corresponding `operator()` specialization on a default-constructed instance of the closure type.
rrev|since=c++17|
This function is constexpr if the function call operator (or specialization, for generic lambdas) is constexpr.
<source style="width:45em; overflow-x: hidden;" lang=cpp>
auto Fwd = [](int(*fp)(int), auto a) { return fp(a); };
auto C = [](auto a) { return a; };
static_assert(Fwd(C, 3) == 3);  // OK
auto NC = [](auto a) { static int s; return a; };
static_assert(Fwd(NC, 3) == 3); // error: no specialization can be
// constexpr because of static s
</source>
If the closure object's `operator()` has a non-throwing exception specification, then the pointer returned by this function has the type pointer to noexcept function.
member|ClosureType()|2=

```cpp
|1=
ClosureType() = default;
dcl|1=
ClosureType(const ClosureType&) = default;
dcl|1=
ClosureType(ClosureType&&) = default;
```

rrev multi|
until1=c++20|rev1=
Closure types are not *DefaultConstructible*. Closure types have no default constructor.
|rev2=If no *captures* are specified, the closure type has a defaulted default constructor. Otherwise, it has no default constructor (this includes the case when there is a capture-default, even if it does not actually capture anything).
The copy constructor and the move constructor are declared as defaulted and may be implicitly-defined according to the usual rules for `copy constructors` and `move constructors`.
member|operator(const ClosureType&)|2=

```cpp
dcl|until=c++20|1=
ClosureType& operator=(const ClosureType&) = delete;
|1=
ClosureType& operator=(const ClosureType&) = default;
ClosureType& operator=(ClosureType&&) = default;
|1=
ClosureType& operator=(const ClosureType&) = delete;
```

rrev multi|
until1=c++20|rev1=
The copy assignment operator is defined as deleted (and the move assignment operator is not declared). Closure types are not *CopyAssignable*.
|rev2=If no *captures* are specified, the closure type has a defaulted copy assignment operator and a defaulted move assignment operator. Otherwise, it has a deleted copy assignment operator (this includes the case when there is a capture-default, even if it does not actually capture anything).
member|~ClosureType()|2=
ddcl|1=
~ClosureType() = default;
The destructor is implicitly-declared.
member|*Captures*|2=
ddcl|1=
T1 a;
T2 b;
...
If the lambda expression captures anything by copy (either implicitly with capture clause **`[ or explicitly with a capture that does not include the character &, e.g. **`[a, b, c]`**), the closure type includes unnamed non-static data members, declared in unspecified order, that hold copies of all entities that were so captured.
Those data members that correspond to captures without initializers are `direct-initialized` when the lambda expression is evaluated. Those that correspond to captures with initializers are initialized as the initializer requires (could be copy- or direct-initialization). If an array is captured, array elements are direct-initialized in increasing index order. The order in which the data members are initialized is the order in which they are declared (which is unspecified).
The type of each data member is the type of the corresponding captured entity, except if the entity has reference type (in that case, references to functions are captured as lvalue references to the referenced functions, and references to objects are captured as copies of the referenced objects).
For the entities that are captured by reference (with the *capture-default* **`[&]`** or when using the character &, e.g. **`[&a, &b, &c]`**), it is unspecified if additional data members are declared in the closure type<sup>(since C++17)</sup> , but any such additional members must satisfy *LiteralType*.
Lambda expressions are not allowed in , `template arguments`, `alias declarations`, `typedef declarations`, and anywhere in a function (or function template) declaration except the function body and the function's `default arguments`.

## Lambda capture

The *captures* defines the outside variables that are accessible from within the lambda function body. Its syntax is defined as follows:

**Syntax:**

- `**`,`** *capture-list*`

### Parameters

- `{{spar` - capture-default|one of **`&`** and **`=`**
- `{{spar` - capture-list|a comma-separated list of captures
The syntax of *capture* is defined as follows:

**Syntax:**

- `**`...`**`
- `|*identifier* *initializer*`
- `*identifier*`
- `*identifier* **`...`**`
- `|**`&`** *identifier* *initializer*`
- `|**`*`** **`this`**`
- `|**`...`** *identifier* *initializer*`
- `|**`&`** **`...`** *identifier* *initializer*`
1. simple by-copy capture
2. simple by-copy capture that is a `pack expansion`
3. by-copy capture with an `initializer`
4. simple by-reference capture
5. simple by-reference capture that is a `pack expansion`
6. by-reference capture with an initializer
7. simple by-reference capture of the current object
8. simple by-copy capture of the current object
9. by-copy capture with an initializer that is a pack expansion
10. by-reference capture with an initializer that is a pack expansion
If the *capture-default* is **`&`**, subsequent simple captures must not begin with **`&`**.

```cpp
struct S2 { void f(int i); };
void S2::f(int i)
{
    [&] {};          // OK: by-reference capture default
    [&, i] {};       // OK: by-reference capture, except i is captured by copy
    [&, &i] {};      // Error: by-reference capture when by-reference is the default
    [&, this] {};    // OK, equivalent to [&]
    [&, this, i] {}; // OK, equivalent to [&, i]
}
```

If the *capture-default* is **`=`**, subsequent simple captures must begin with **`&`**<sup>(since C++17)</sup>  or be **`*this`** <sup>(since C++20)</sup> or **`this`**.

```cpp
struct S2 { void f(int i); };
void S2::f(int i)
{
    [=] {};        // OK: by-copy capture default
    [=, &i] {};    // OK: by-copy capture, except i is captured by reference
    [=, *this] {}; // until C++17: Error: invalid syntax
                   // since C++17: OK: captures the enclosing S2 by copy
    [=, this] {};  // until C++20: Error: this when = is the default
                   // since C++20: OK, same as [=]
}
```

Any capture may appear only once, and its name must be different from any parameter name:

```cpp
struct S2 { void f(int i); };
void S2::f(int i)
{
    [i, i] {};        // Error: i repeated
    [this, *this] {}; // Error: "this" repeated (C++17)

    [i] (int i) {};   // Error: parameter and capture have the same name
}
```

A lambda expression can use a variable without capturing it if the variable
* is a non-local variable or has static or thread local `storage duration` (in which case the variable cannot be captured), or
* is a reference that has been initialized with a .
A lambda expression can read the value of a variable without capturing it if the variable
* has const non-volatile integral or enumeration type and has been initialized with a , or
* is constexpr and has no mutable members.
The current object (`*this`) can be implicitly captured if either capture default is present. If implicitly captured, it is always captured by reference, even if the capture default is **`=`**. <sup>(since C++20)</sup> The implicit capture of `*this` when the capture default is **`=`** is deprecated.
Only lambda expressions satisfying any of the following conditions may have a *capture-default* or *capture* without initializers:
* Its innermost `enclosing scope` is a .
* It appears within a `default member initializer`, and its innermost enclosing scope is the corresponding .
rrev|since=c++26|
* It appears within a `contract assertion`, and its innermost enclosing scope is the corresponding .
For such lambda expression, the ''reaching scope'' is defined as the set of enclosing scopes up to and including the innermost enclosing function (and its parameters). This includes nested block scopes and the scopes of enclosing lambdas if this lambda is nested.
The *identifier* in any capture without an initializer (other than the `this`-capture) is looked up using usual `unqualified name lookup` in the ''reaching scope'' of the lambda. The result of the lookup must be a `variable` with automatic storage duration declared in the reaching scope<sup>(since C++20)</sup> , or a `structured binding whose corresponding variable satisfies such requirements`. The entity is ''explicitly captured''.
rrev|since=c++14|
A capture with an initializer, called ''init-capture'', acts as if it declares and explicitly captures a variable declared with type specifier `auto` and the same initializer, whose declarative region is the body of the lambda expression (that is, it is not in scope within its initializer), except that:
* if the capture is by-copy, the introduced non-static data member of the closure object is another way to refer to that variable;
** in other words, the source variable does not actually exist, and the type deduction via `auto` and the initialization are applied to the non-static data member;
* if the capture is by-reference, the reference variable's lifetime ends when the lifetime of the closure object ends.
This is used to capture move-only types with a capture such as `1=x = std::move(x)`.
This also makes it possible to capture by const reference, with `1=&cr = std::as_const(x)` or similar.

```cpp
int x = 4;

auto y = [&r = x, x = x + 1]() -> int
{
    r += 2;
    return x * x;
}(); // updates ::x to 6 and initializes y to 25.
```

If *captures* has a *capture-default* and does not explicitly capture the enclosing object (as `this` or `*this`), or an automatic variable that is `odr-usable` in the lambda body<sup>(since C++20)</sup> , or a `structured binding whose corresponding variable has atomic storage duration`, it captures the entity ''implicitly'' if the entity is named in a `potentially-evaluated` expression within an expression (including when the implicit `this->` is added before a use of non-static class member).
For the purpose of determining implicit captures, `typeid` is never considered to make its operands unevaluated.
rrev|since=c++17|
Entities might be implicitly captured even if they are only named within a `discarded statement` after instantiation of the lambda body.

```cpp
void f(int, const int (&)[2] = {}) {}   // #1
void f(const int&, const int (&)[1]) {} // #2

struct NoncopyableLiteralType
{
    constexpr explicit NoncopyableLiteralType(int n) : n_(n) {}
    NoncopyableLiteralType(const NoncopyableLiteralType&) = delete;

    int n_;
};

void test()
{
    const int x = 17;

    auto l0 = []{ f(x); };           // OK: calls #1, does not capture x
    auto g0 = [](auto a) { f(x); };  // same as above

    auto l1 = [=]{ f(x); };          // OK: captures x (since P0588R1) and calls #1
                                     // the capture can be optimized away
    auto g1 = [=](auto a) { f(x); }; // same as above

    auto ltid = [=]{ typeid(x); };   // OK: captures x (since P0588R1)
                                     // even though x is unevaluated
                                     // the capture can be optimized away

    auto g2 = [=](auto a)
    {
        int selector[sizeof(a) == 1 ? 1 : 2] = {};
        f(x, selector); // OK: is a dependent expression, so captures x
    };

    auto g3 = [=](auto a)
    {
        typeid(a + x);  // captures x regardless of
                        // whether a + x is an unevaluated operand
    };

    constexpr NoncopyableLiteralType w{42};
    auto l4 = []{ return w.n_; };      // OK: w is not odr-used, capture is unnecessary
    // auto l5 = [=]{ return w.n_; };  // error: w needs to be captured by copy
}
```

If the body of a lambda `odr-uses` an entity captured by copy, the member of the closure type is accessed. If it is not odr-using the entity, the access is to the original object:

```cpp
void f(const int*);
void g()
{
    const int N = 10;
    [=]
    { 
        int arr[N]; // not an odr-use: refers to g's const int N
        f(&N); // odr-use: causes N to be captured (by copy)
               // &N is the address of the closure object's member N, not g's N
    }();
}
```

If a lambda odr-uses a reference that is captured by reference, it is using the object referred-to by the original reference, not the captured reference itself:
Within the body of a lambda with capture default **`=`**, the type of any capturable entity is as if it were captured (and thus const-qualification is often added if the lambda is not `mutable`), even though the entity is in an unevaluated operand and not captured (e.g. in `decltype`):

```cpp
void f3()
{
    float x, &r = x;
    [=]
    { // x and r are not captured (appearance in a decltype operand is not an odr-use)
        decltype(x) y1;        // y1 has type float
        decltype((x)) y2 = y1; // y2 has type float const& because this lambda
                               // is not mutable and x is an lvalue
        decltype(r) r1 = y1;   // r1 has type float& (transformation not considered)
        decltype((r)) r2 = y2; // r2 has type float const&
    };
}
```

Any entity captured by a lambda (implicitly or explicitly) is odr-used by the lambda expression (therefore, implicit capture by a nested lambda triggers implicit capture in the enclosing lambda).
All implicitly-captured variables must be declared within the ''reaching scope'' of the lambda.
If a lambda captures the enclosing object (as `this` or `*this`), either the nearest enclosing function must be a non-static member function or the lambda must be in a `default member initializer`:

```cpp
struct s2
{
    double ohseven = .007;
    auto f() // nearest enclosing function for the following two lambdas
    {
        return [this]      // capture the enclosing s2 by reference
        {
            return [*this] // capture the enclosing s2 by copy (C++17)
            {
                return ohseven; // OK
            }
        }();
    }

    auto g()
    {
        return [] // capture nothing
        { 
            return [*this] {}; // error: *this not captured by outer lambda expression
        }();
    }
};
```

If a lambda expression <sup>(since C++14)</sup> (or a specialization of a generic lambda's function call operator) ODR-uses `*this` or any variable with automatic storage duration, it must be captured by the lambda expression.

```cpp
void f1(int i)
{
    int const N = 20;
    auto m1 = [=]
    {
        int const M = 30;
        auto m2 = [i]
        {
            int x[N][M]; // N and M are not odr-used 
                         // (ok that they are not captured)
            x[0][0] = i; // i is explicitly captured by m2
                         // and implicitly captured by m1
        };
    };

    struct s1 // local class within f1()
    {
        int f;
        void work(int n) // non-static member function
        {
            int m = n * n;
            int j = 40;
            auto m3 = [this, m]
            {
                auto m4 = [&, j] // error: j is not captured by m3
                {
                    int x = n; // error: n is implicitly captured by m4
                               // but not captured by m3
                    x += m;    // OK: m is implicitly captured by m4
                               // and explicitly captured by m3
                    x += i;    // error: i is outside of the reaching scope
                               // (which ends at work())
                    x += f;    // OK: this is captured implicitly by m4
                               // and explicitly captured by m3
                };
            };
        }
    };
}
```

Class members cannot be captured explicitly by a capture without initializer (as mentioned above, only `variables` are permitted in the capture-list):

```cpp
class S
{
    int x = 0;

    void f()
    {
        int i = 0;
    //  auto l1 = [i, x] { use(i, x); };      // error: x is not a variable
        auto l2 = [i, x = x] { use(i, x); };  // OK, copy capture
        i = 1; x = 1; l2(); // calls use(0,0)
        auto l3 = [i, &x = x] { use(i, x); }; // OK, reference capture
        i = 2; x = 2; l3(); // calls use(1,2)
    }
};
```

When a lambda captures a member using implicit by-copy capture, it does not make a copy of that member variable: the use of a member variable `m` is treated as an expression `(*this).m`, and `*this` is always implicitly captured by reference:

```cpp
class S
{
    int x = 0;

    void f()
    {
        int i = 0;

        auto l1 = [=] { use(i, x); }; // captures a copy of i and
                                      // a copy of the this pointer
        i = 1; x = 1; l1();           // calls use(0, 1), as if
                                      // i by copy and x by reference

        auto l2 = [i, this] { use(i, x); }; // same as above, made explicit
        i = 2; x = 2; l2();           // calls use(1, 2), as if
                                      // i by copy and x by reference

        auto l3 = [&] { use(i, x); }; // captures i by reference and
                                      // a copy of the this pointer
        i = 3; x = 2; l3();           // calls use(3, 2), as if
                                      // i and x are both by reference

        auto l4 = [i, *this] { use(i, x); }; // makes a copy of *this,
                                             // including a copy of x
        i = 4; x = 4; l4();           // calls use(3, 2), as if
                                      // i and x are both by copy
    }
};
```

If a lambda expression appears in a `default argument`, it cannot explicitly or implicitly capture anything<sup>(since C++14)</sup> , unless all captures have initializers which satisfy the constraints of an expression appearing in a default argument:

```cpp
void f2()
{
    int i = 1;

    void g1( int = [i] { return i; }() ); // error: captures something
    void g2( int = [i] { return 0; }() ); // error: captures something
    void g3( int = [=] { return i; }() ); // error: captures something

    void g4( int = [=] { return 0; }() );       // OK: capture-less
    void g5( int = [] { return sizeof i; }() ); // OK: capture-less

    // C++14
    void g6( int = [x = 1] { return x; }() ); // OK: 1 can appear
                                              //     in a default argument
    void g7( int = [x = i] { return x; }() ); // error: i cannot appear
                                              //        in a default argument
}
```

Members of `anonymous unions` members cannot be captured. `Bit-fields` can only be captured by copy.
If a nested lambda `m2` captures something that is also captured by the immediately enclosing lambda `m1`, then `m2`'s capture is transformed as follows:
* if the enclosing lambda `m1` captures by copy, `m2` is capturing the non-static member of `m1`'s closure type, not the original variable or `*this`; if `m1` is not mutable, the non-static data member is considered to be const-qualified.
* if the enclosing lambda `m1` captures by reference, `m2` is capturing the original variable or `*this`.

### Example

```cpp
#include <iostream>

int main()
{
    int a = 1, b = 1, c = 1;

    auto m1 = [a, &b, &c]() mutable
    {
        auto m2 = [a, b, &c]() mutable
        {
            std::cout << a << b << c << '\n';
            a = 4; b = 4; c = 4;
        };
        a = 3; b = 3; c = 3;
        m2();
    };

    a = 2; b = 2; c = 2;

    m1();                             // calls m2() and prints 123
    std::cout << a << b << c << '\n'; // prints 234
}
```

rrev|since=c++23|
If a lambda captures anything, the type of the explicit object parameter (if any) of the function call operator can only be
* the closure type,
* a class type publicly and unambiguously derived from the closure type, or
* a reference to a possibly cv-qualified such type.

```cpp
struct C 
{
    template<typename T>
    C(T);
};

void func(int i) 
{
    int x = [=](this auto&&) { return i; }();  // OK
    int y = [=](this C) { return i; }();       // error
    int z = [](this C) { return 42; }();       // OK

    auto lambda = [n = 42] (this auto self) { return n; };
    using Closure = decltype(lambda);
    struct D : private Closure {
        D(Closure l) : Closure(l) {}
        using Closure::operator();
        friend Closure;
    };
    D{lambda}(); // error
}
```


## Notes

The rule for implicit lambda capture is slightly changed by defect report `P0588R1`. As of 2023-10, some major implementations have not completely implemented the DR, and thus the old rule, which detects odr-using, is still used in some cases.
If *captures* has a *capture-default* and does not explicitly capture the enclosing object (as **`this`** or **`*this`**), or an automatic variable that is `odr-usable` in the lambda body<sup>(since C++20)</sup> , or a `structured binding whose corresponding variable has atomic storage duration`, it captures the entity ''implicitly'' if the entity is
rrev|since=c++14|
* named in a `potentially-evaluated` expression within an expression that depends on a template parameter of a generic lambda, or
* `odr-used` by the body of the lambda.

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> c{1, 2, 3, 4, 5, 6, 7};
    int x = 5;
    c.erase(std::remove_if(c.begin(), c.end(), [x](int n) { return n < x; }), c.end());

    std::cout << "c: ";
    std::for_each(c.begin(), c.end(), [](int i) { std::cout << i << ' '; });
    std::cout << '\n';

    // the type of a closure cannot be named, but can be inferred with auto
    // since C++14, lambda could own default arguments
    auto func1 = [](int i = 6) { return i + 4; };
    std::cout << "func1: " << func1() << '\n';

    // like all callable objects, closures can be captured in std::function
    // (this may incur unnecessary overhead)
    std::function<int(int)> func2 = [](int i) { return i + 4; };
    std::cout << "func2: " << func2(6) << '\n';

    constexpr int fib_max {8};
    std::cout << "Emulate `recursive lambda` calls:\nFibonacci numbers: ";
    auto nth_fibonacci = [](int n)
    {
        std::function<int(int, int, int)> fib = [&](int n, int a, int b)
        {
            return n ? fib(n - 1, a + b, a) : b;
        };
        return fib(n, 0, 1);
    };

    for (int i{1}; i <= fib_max; ++i)
        std::cout << nth_fibonacci(i) << (i < fib_max ? ", " : "\n");

    std::cout << "Alternative approach to lambda recursion:\nFibonacci numbers: ";
    auto nth_fibonacci2 = [](auto self, int n, int a = 0, int b = 1) -> int
    {
        return n ? self(self, n - 1, a + b, a) : b;
    };

    for (int i{1}; i <= fib_max; ++i)
        std::cout << nth_fibonacci2(nth_fibonacci2, i) << (i < fib_max ? ", " : "\n");

#ifdef __cpp_explicit_this_parameter
    std::cout << "C++23 approach to lambda recursion:\n";
    auto nth_fibonacci3 = [](this auto self, int n, int a = 0, int b = 1) -> int
    {
         return n ? self(n - 1, a + b, a) : b;
    };

    for (int i{1}; i <= fib_max; ++i)
        std::cout << nth_fibonacci3(i) << (i < fib_max ? ", " : "\n");
#endif
}
```


**Output:**
```
c: 5 6 7
func1: 10
func2: 10
Emulate `recursive lambda` calls:
Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13
Alternative approach to lambda recursion:
Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-974 | C++11 | default argument was not allowed in the<br>parameter list of a lambda expression | allowed |
| cwg-1557 | C++11 | the language linkage of the returned function type of<br>the closure type's conversion function was not specified | it has C++<br>language linkage |
| cwg-1607 | C++11 | lambda expressions could appear in<br>function and function template signatures | not allowed |
| cwg-1612 | C++11 | members of anonymous unions could be captured | not allowed |
| cwg-1722 | C++11 | the conversion function for capture-less lambdas<br>had unspecified exception specification | conversion function<br>is noexcept |
| cwg-1780 | C++14 | it was unclear whether the members of the closure types of generic<br>lambdas can be explicitly instantiated or explicitly specialized | neither is allowed |
| cwg-1891 | C++11 | closure had a deleted default constructor<br>and implicit copy/move constructors | no default and defaulted<br>copy/move constructors |
| cwg-2011 | C++11 | for a reference captured by reference, it was unspecified<br>which entity the identifier of the capture refers to | it refers to the originally<br>referenced entity |
| cwg-2095 | C++11 | the behavior of capturing rvalue references<br>to functions by copy was not clear | made clear |
| cwg-2211 | C++11 | the behavior was unspecified if a capture<br>has the same name as a parameter | the program is ill-<br>formed in this case |
| cwg-2358 | C++14 | lambda expressions appearing in default arguments had<br>to be capture-less even if all captures are initialized with<br>expressions which can appear in default arguments | allow such lambda<br>expressions with captures |
| cwg-2509 | C++17 | each specifier could have multiple<br>occurrences in the specifier sequence | each specifier can only<br>appear at most once in<br>the specifier sequence |
| cwg-2561 | C++23 | a lambdas with explicit object parameter could have a<br>conversion function to an undesired function pointer type | it does not have such<br>a conversion funtion |


## See also


| cpp/language/dsc auto | (see dedicated page) |
| cpp/utility/functional/dsc function | (see dedicated page) |
| cpp/utility/functional/dsc move_only_function | (see dedicated page) |


## External links

