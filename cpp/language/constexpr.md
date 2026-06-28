---
title: constexpr specifier
type: Language
source: https://en.cppreference.com/w/cpp/language/constexpr
---


# tt|constexpr

:***`constexpr`** - specifies that the value of a variable<sup>(since C++26)</sup> , `structured binding` or function can appear in `constant expression`s

## Explanation

The `constexpr` specifier declares that it is possible to evaluate the value of the entities at compile time. Such entities can then be used where only compile time `constant expression`s are allowed (provided that appropriate function arguments are given).
A `constexpr` specifier used in an object declaration<sup>(until C++14)</sup>  or non-static member function implies `const`.
A `constexpr` specifier used in the first declaration of a function<sup>(since C++17)</sup>  or `static data member` implies `inline`. If any declaration of a function or function template has a `constexpr` specifier, then every declaration must contain that specifier.

## `constexpr` variable

A variable<sup>(since C++14)</sup>  or variable template can be declared `constexpr` if all following conditions are satisfied:
* The declaration is a `definition`.
* It is of a .
* It is initialized (by the declaration).
rev|until=c++26|
* The `full-expression` of its initialization is a `constant expression`.
rev|since=c++26|
* It is `constant-initializable`.
<sup>(since C++20)</sup> anchor|Constant destruction
* It has constant destruction, which means one of the following conditions needs to be satisfied:
:* It is not of class type nor (possibly multi-dimensional) array thereof.
:* It is of a class type with a `constexpr` destructor or (possibly multi-dimensional) array thereof, and for a hypothetical expression `e` whose only effect is to destroy the object, `e` would be a  if the lifetime of the object and its non-mutable subobjects (but not its mutable subobjects) were considered to start within `e`.
If a `constexpr` variable is not `translation-unit-local`, it should not be initialized to refer to a translation-unit-local entity that is usable in constant expressions, nor have a subobject that refers to such an entity. Such initialization is disallowed in a `module interface unit` (outside its , if any) or a module partition, and is deprecated in any other context.

## `constexpr` function

A function or function template can be declared `constexpr`.
A function is ''constexpr-suitable'' if all following conditions are satisfied:
rev|until=c++20|
* It is not a `virtual` function.
rev|until=c++23|
* Its return type (if exists) is a .
* Each of its parameter types is a literal type.
rev|until=c++26|
* If it is a constructor<sup>(since C++20)</sup>  or destructor, extra conditions need to be satisfied (see below).
rev|since=c++20|
* It is not a `coroutine`.
rev|until=c++14|
* Its function body is `1== default`, `1== delete`, or a compound statement `enclosing` only the following:
:* `null statements`
:* `static_assert` declarations
:* `typedef` declarations and `alias` declarations that do not define classes or enumerations
:* ``using` declarations`
:* ``using` directives`
:* exactly one `return` statement if the function is not a constructor
rev|since=c++14|until=c++23|
* Its function body is `1== default`, `1== delete`, or<sup>(until C++20)</sup>  a compound statement that does '''not''' `enclose` the following:
:* `goto` statements
:* statements with `labels` other than `case` and `default`
rrev|until=c++20|
:* ``try` blocks`
:* `inline assembly` declarations
:* definitions of variables for which `no initialization is performed`
:* definitions of variables of non-literal types
:* definitions of variables of static or thread `storage duration`
Except for instantiated `constexpr` functions, non-templated `constexpr` functions must be constexpr-suitable.
rrev|until=c++23|
For a non-constructor `constexpr` function that is neither defaulted nor templated, if no argument values exist such that an invocation of the function could be an evaluated subexpression of a , the program is ill-formed, no diagnostic required.
For a templated `constexpr` function, if no specialization of the function/class template would make the templated function constexpr-suitable when considered as a non-templated function, the program is ill-formed, no diagnostic required.
An invocation of a `constexpr` function in a given context produces the same result as an invocation of an equivalent non-`constexpr` function in the same context in all respects, with the following exceptions:
* An invocation of a `constexpr` function can appear in a `constant expression`.
* `Copy elision` is not performed in a constant expression.

## `constexpr` constructor

rev|until=c++26|
On top of the requirements of `constexpr` functions, a constructor also needs to satisfy all following conditions to be constexpr-suitable:
rrev|until=c++23|
*Its function body is `1== delete` or satisfies the following additional requirements:
rrev|until=c++20|
:* If the class is a `union` having variant members, exactly one of them is initialized.
:* If the class is a `union-like class`, but is not a union, for each of its anonymous union members having variant members, exactly one of them is initialized.
:* Every non-variant non-static data member and base class subobject is initialized.
:* If the constructor is a , the target constructor is a `constexpr` constructor.
:* If the constructor is a non-delegating constructor, every constructor selected to initialize non-static data members and base class subobjects is a `constexpr` constructor.
* The class does not have any `virtual base class`.
rev|since=c++26|
Constructors do not need to satisfy any extra condition to be constexpr-suitable.
rrev|until=c++23|
For a `constexpr` constructor that is neither defaulted nor templated, if no argument values exist such that an invocation of the function could be an evaluated subexpression of the initialization full-expression of some object subject to `constant expression`, the program is ill-formed, no diagnostic required.

## `constexpr` destructor

rev|until=c++20|
Destructors cannot be `constexpr`, but a `trivial destructor` can be implicitly called in constant expressions.
rev|since=c++20|until=c++26|
On top of the requirements of `constexpr` functions, a destructor also needs to satisfy all following conditions to be constexpr-suitable:
rrev|until=c++23|
* For every subobject of class type or (possibly multi-dimensional) array thereof, that class type has a `constexpr` destructor.
* The class does not have any virtual base class.
rev|since=c++26|
Destructors do not need to satisfy any extra condition to be constexpr-suitable.

## Notes

rrev|until=c++17|
Because the `noexcept` operator always returns `true` for a constant expression, it can be used to check if a particular invocation of a constexpr function takes the constant expression branch:

```cpp
constexpr int f(); 
constexpr bool b1 = noexcept(f()); // false, undefined constexpr function
constexpr int f() { return 0; }
constexpr bool b2 = noexcept(f()); // true, f() is a constant expression
```

rrev|since=c++23|
It is possible to write a constexpr function whose invocation can never satisfy the requirements of a core constant expression:

```cpp
void f(int& i) // not a constexpr function
{
    i = 0;
}

constexpr void g(int& i) // well-formed since C++23
{
    f(i); // unconditionally calls f, cannot be a constant expression
}
```

Constexpr constructors are permitted for classes that are not literal types. For example, the default constructor of `std::shared_ptr` is constexpr, allowing `constant initialization`.
Reference variables can be declared constexpr (their initializers have to be `reference constant expressions`):

```cpp
static constexpr int const& x = 42; // constexpr reference to a const int object
                                    // (the object has static storage duration
                                    //  due to life extension by a static reference)
```

rrev|since=c++20|1=
Even though `try` blocks and inline assembly are allowed in constexpr functions, throwing exceptions <sup>(since C++26)</sup> that are uncaught or executing the assembly is still disallowed in a constant expression.
If a variable has constant destruction, there is no need to generate machine code in order to call destructor for it, even if its destructor is not trivial.
A non-lambda, non-special-member, and non-templated constexpr function cannot implicitly become an immediate function. Users need to explicitly mark it `consteval` to make such an intended function definition well-formed.

## Keywords

`cpp/keyword/constexpr`

## Example


### Example

```cpp
#include <iostream>
#include <stdexcept>

// C++11 constexpr functions use recursion rather than iteration
constexpr int factorial(int n)
{
    return n <= 1 ? 1 : (n * factorial(n - 1));
}

// C++14 constexpr functions may use local variables and loops
#if __cplusplus >= 201402L
constexpr int factorial_cxx14(int n)
{
    int res = 1;
    while (n > 1)
        res *= n--;
    return res;
}
#endif // C++14

// A literal class
class conststr
{
    const char* p;
    std::size_t sz;
public:
    template<std::size_t N>
    constexpr conststr(const char(&a)[N]): p(a), sz(N - 1) {}

    // constexpr functions signal errors by throwing exceptions
    // in C++11, they must do so from the conditional operator ?:
    constexpr char operator[](std::size_t n) const
    {
        return n < sz ? p[n] : throw std::out_of_range("");
    }

    constexpr std::size_t size() const { return sz; }
};

// C++11 constexpr functions had to put everything in a single return statement
// (C++14 does not have that requirement)
constexpr std::size_t countlower(conststr s, std::size_t n = 0,
                                             std::size_t c = 0)
{
    return n == s.size() ? c :
        'a' <= s[n] && s[n] <= 'z' ? countlower(s, n + 1, c + 1)
                                   : countlower(s, n + 1, c);
}

// An output function that requires a compile-time constant, for testing
template<int n>
struct constN
{
    constN() { std::cout << n << '\n'; }
};

int main()
{
    std::cout << "4! = ";
    constN<factorial(4)> out1; // computed at compile time

    volatile int k = 8; // disallow optimization using volatile
    std::cout << k << "! = " << factorial(k) << '\n'; // computed at run time

    std::cout << "The number of lowercase letters in \"Hello, world!\" is ";
    constN<countlower("Hello, world!")> out2; // implicitly converted to conststr

    constexpr int a[12] = {0, 1, 2, 3, 4, 5, 6, 7, 8};
    constexpr int length_a = sizeof a / sizeof(int); // std::size(a) in C++17,
                                                      // std::ssize(a) in C++20
    std::cout << "Array of length " << length_a << " has elements: ";
    for (int i = 0; i < length_a; ++i)
        std::cout << a[i] << ' ';
    std::cout << '\n';
}
```


**Output:**
```
4! = 24
8! = 40320
The number of lowercase letters in "Hello, world!" is 9
Array of length 12 has elements: 0 1 2 3 4 5 6 7 8 0 0 0
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-2004 | c++11 | copy/move of a union with a mutable member<br>was allowed in a constant expression | mutable variants disqualify<br>implicit copy/move |


## See also


| cpp/language/dsc consteval | (see dedicated page) |
| cpp/language/dsc constinit | (see dedicated page) |

