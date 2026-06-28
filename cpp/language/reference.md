---
title: Reference declaration
type: Language
source: https://en.cppreference.com/w/cpp/language/reference
---


# Reference declaration

Declares a named variable as a reference, that is, an alias to an already-existing object or function.

## Syntax

A reference variable declaration is any simple declaration whose `declarator` has the form

**Syntax:**

- `sdsc|num=1|`
- `**`&`** *attr* (optional) *declarator*`
- `|`
- `**`&&`** *attr* (optional) *declarator*`
1. '''Lvalue reference declarator''': the declaration `S& D;` declares `D` as an ''lvalue reference'' to the type determined by *decl-specifier-seq* `S`.
2. '''Rvalue reference declarator''': the declaration `S&& D;` declares `D` as an ''rvalue reference'' to the type determined by *decl-specifier-seq* `S`.

### Parameters

- `{{spar` - declarator|any `declarator` except another reference declarator (there are no references to references)
- `{{spar` - attr|<sup>(C++11)</sup> list of `attributes`
A reference is required to be initialized to refer to a valid object or function: see `reference initialization`.
The type “reference to (possibly cv-qualified) `void`” cannot be formed.
Reference types cannot be `cv-qualified` at the top level; there is no syntax for that in declaration, and if a qualification is added to a typedef-name<sup>(since C++11)</sup>  or `decltype specifier,` or `type template parameter`, it is ignored.
References are not objects; they do not necessarily occupy storage, although the compiler may allocate storage if it is necessary to implement the desired semantics (e.g. a non-static data member of reference type usually increases the size of the class by the amount necessary to store a memory address).
Because references are not objects, there are no arrays of references, no pointers to references, and no references to references:

```cpp
int& a[3]; // error
int&* p;   // error
int& &r;   // error
```

rrev|since=c++11|

## Reference collapsing

It is permitted to form references to references through type manipulations in templates or typedefs, in which case the ''reference collapsing'' rules apply: rvalue reference to rvalue reference collapses to rvalue reference, all other combinations form lvalue reference:

```cpp
typedef int&  lref;
typedef int&& rref;
int n;

lref&  r1 = n; // type of r1 is int&
lref&& r2 = n; // type of r2 is int&
rref&  r3 = n; // type of r3 is int&
rref&& r4 = 1; // type of r4 is int&&
```

(This, along with special rules for `template argument deduction` when `T&&` is used in a function template, forms the rules that make `std::forward` possible.)

## Lvalue references

Lvalue references can be used to alias an existing object (optionally with different cv-qualification):
They can also be used to implement pass-by-reference semantics in function calls:
When a function's return type is lvalue reference, the function call expression becomes an `lvalue` expression:
rrev|since=c++11|

## Rvalue references

Rvalue references can be used to `extend the lifetimes` of temporary objects (note, lvalue references to const can extend the lifetimes of temporary objects too, but they are not modifiable through them):
More importantly, when a function has both rvalue reference and lvalue reference `overloads`, the rvalue reference overload binds to rvalues (including both prvalues and xvalues), while the lvalue reference overload binds to lvalues:
This allows `move constructor`s, `move assignment` operators, and other move-aware functions (e.g. `std::vector::push_back()`) to be automatically selected when suitable.
Because rvalue references can bind to xvalues, they can refer to non-temporary objects:

```cpp
int i2 = 42;
int&& rri = std::move(i2); // binds directly to i2
```

This makes it possible to move out of an object in scope that is no longer needed:

```cpp
std::vector<int> v{1, 2, 3, 4, 5};
std::vector<int> v2(std::move(v)); // binds an rvalue reference to v
assert(v.empty());
```


## Forwarding references

Forwarding references are a special kind of references that preserve the value category of a function argument, making it possible to ''forward'' it by means of `std::forward`. Forwarding references are either:
1. function parameter of a function template declared as rvalue reference to cv-unqualified `type template parameter` of that same function template:

```cpp
template<class T>
int f(T&& x)                      // x is a forwarding reference
{
    return g(std::forward<T>(x)); // and so can be forwarded
}

int main()
{
    int i;
    f(i); // argument is lvalue, calls f<int&>(int&), std::forward<int&>(x) is lvalue
    f(0); // argument is rvalue, calls f<int>(int&&), std::forward<int>(x) is rvalue
}

template<class T>
int g(const T&& x); // x is not a forwarding reference: const T is not cv-unqualified

template<class T>
struct A
{
    template<class U>
    A(T&& x, U&& y, int* p); // x is not a forwarding reference: T is not a
                             // type template parameter of the constructor,
                             // but y is a forwarding reference
};
```

2. `auto&&` except when deduced from a brace-enclosed initializer list<sup>(since C++17)</sup>  or, when representing a template parameter of a class template during `class template argument deduction`:

```cpp
auto&& vec = foo();       // foo() may be lvalue or rvalue, vec is a forwarding reference
auto i = std::begin(vec); // works either way
(*i)++;                   // works either way

g(std::forward<decltype(vec)>(vec)); // forwards, preserving value category

for (auto&& x: f())
{
    // x is a forwarding reference; this is a common way to use range for in generic code
}

auto&& z = {1, 2, 3}; // *not* a forwarding reference (special case for initializer lists)
```

See also `template argument deduction` and `std::forward`.

## Dangling references

Although references always refer to valid objects or functions upon initialization, it is possible to create a program where the `lifetime` of the referred-to object ends, but the reference remains accessible (''dangling'').
Given an expression `expr` of reference type and let `target` be the object or function denoted by the reference:
* If a pointer to `target` would be `valid` in the context of the evalution of `expr`, the result designates `target`.
* Otherwise, the behavior is undefined.

```cpp
std::string& f()
{
    std::string s = "Example";
    return s; // exits the scope of s:
              // its destructor is called and its storage deallocated
}

std::string& r = f(); // dangling reference
std::cout << r;       // undefined behavior: reads from a dangling reference
std::string s = f();  // undefined behavior: copy-initializes from a dangling reference
```

Note that rvalue references and lvalue references to const extend the lifetimes of temporary objects (see `Reference initialization` for rules and exceptions).
If the referred-to object was destroyed (e.g. by explicit destructor call), but the storage was not deallocated, a reference to the out-of-lifetime object may be used in limited ways, and may become valid if the object is recreated in the same storage (see `Access outside of lifetime` for details).

## Type-inaccessible references

Attempting to bind a reference to an object where the converted initializer is <sup>(until C++11)</sup> an lvalue<sup>(since C++11)</sup> a glvalue through which the object is not `type-accessible` results in undefined behavior:

```cpp
char x alignas(int);

int& ir = *reinterpret_cast<int*>(&x); // undefined behavior:
                                       // initializer refers to char object
```


## Call-incompatible references

Attempting to bind a reference to a function where the converted initializer is <sup>(until C++11)</sup> an lvalue<sup>(since C++11)</sup> a glvalue whose type is not `call-compatible` with the type of the function's definition results in undefined behavior:

```cpp
void f(int);

using F = void(float);
F& ir = *reinterpret_cast<F*>(&f); // undefined behavior:
                                   // initializer refers to void(int) function
```


## Notes


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-453 | C++98 | it was unclear which object or function a reference cannot be bound to | made clear |
| cwg-2933 | C++98 | the behavior of accessing dangling references was unclear | made clear |


## External links

