---
title: Functions
type: Language
source: https://en.cppreference.com/w/cpp/language/functions
---


# Functions

Functions are C++ entities that associate a sequence of `statements` (a ''function body'') with a ''name'' and a list of zero or more ''function parameters''.

```cpp
// function name: "isodd"
// parameter list has one parameter, with name "n" and type int
// the return type is bool
bool isodd(int n)
{                 // the body of the function begins
    return n % 2;
}                 // the body of the function ends
```

When a function is invoked, e.g. in a `function-call expression`, the parameters are initialized from the arguments (either provided at the place of call or `defaulted`) and the statements in the function body are executed. If the `parameter list` ends with `...`, extra arguments can be supplied to the function, such a function is called `variadic function`.

```cpp
int main()
{
    for (int arg : {-3, -2, -1, 0, 1, 2, 3})
        std::cout << isodd(arg) << ' '; // isodd called 7 times, each
                                        // time n is copy-initialized from arg
}
```

`Unqualified` function names in function-call expressions are looked up with an extra set of rules called `"argument-dependent lookup" (ADL)`.
A function can terminate by `returning` or by `throwing` an `exception`.
rrev|since=c++20|
A function may be a `coroutine`, in which case it can suspend execution to be resumed later.
A `function declaration` may appear in any scope, but a `function definition` may only appear in namespace scope or, for `member` and `friend` functions, in class scope. A function that is declared in a class body without a friend specifier is a class member function. Such functions have many additional properties, see `member functions` for details.
Functions are not objects: there are no arrays of functions and functions cannot be passed by value or returned from other functions. Pointers and references to functions (except for `the main function`<sup>(since C++20)</sup>  and `most standard library functions`) are allowed, and may be used where these functions themselves cannot. Therefore we say these functions are "addressable".
Each function has a type, which consists of the function's return type, the types of all parameters (after array-to-pointer and function-to-pointer transformations, see `parameter list`) <sup>(since C++17)</sup> , whether the function is `noexcept or not`, and, for non-static member functions, cv-qualification<sup>(since C++11)</sup>  and ref-qualification. Function types also have `language linkage`. There are no cv-qualified function types (not to be confused with the types of `cv-qualified functions` such as `int f() const;` or functions returning `cv-qualified types`, such as `std::string const f();`). Any cv-qualifier is ignored if it is added to an alias for a function type.
Multiple functions in the same scope may have the same name, as long as their parameter lists and, for non-static member functions, cv<sup>(since C++11)</sup> /ref-qualifications are different. This is known as `function overloading`. Function declarations that differ only in the return type <sup>(since C++17)</sup> and the noexcept specification cannot be overloaded. The `address of an overloaded function` is determined differently.
rrev|since=c++11|
C++ implements [anonymous function](https://en.wikipedia.org/wiki/anonymous function)s using `lambda-expressions`.

## Function objects

Besides function lvalues, the function call expression supports pointers to functions, and any value of class type that overloads the function-call operator or is convertible to function pointer<sup>(since C++11)</sup>  (including `lambda-expressions)`. Together, these types are known as *FunctionObject*s, and they are used ubiquitously through the C++ standard library, see for example, usages of *BinaryPredicate* and *Compare*.
The standard library also provides a number of predefined function object templates as well as the methods to compose new ones (including `std::less`<sup>(since C++11)</sup> , `std::mem_fn`, `std::bind`, `std::function`<sup>(since C++17)</sup> , `std::not_fn`<sup>(since C++20)</sup> , `std::bind_front`<sup>(since C++23)</sup> , `std::bind_back`, `std::move_only_function`<sup>(since C++26)</sup> , `std::copyable_function`, and `std::function_ref`).
