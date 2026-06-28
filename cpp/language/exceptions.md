---
title: Exceptions
type: Language
source: https://en.cppreference.com/w/cpp/language/exceptions
---


# Exceptions

Exception handling provides a way of transferring control and information from some point in the execution of a program to a handler associated with a point previously passed by the execution (in other words, exception handling transfers control up the call stack).
Evaluating a ``throw` expression` will throw an exception. Exceptions can also be thrown in `other contexts`.
In order for an exception to be caught, the `throw` expression has to be inside a ``try` block`, and the `try` block has to contain a `handler` that matches the type of the exception object.
When declaring a function, the following specification(s) may be provided to limit the types of the exceptions a function may throw:
<sup>(since C++11)</sup> * `noexcept specifications`
Errors that arise during exception handling are handled by `std::terminate`<sup>(until C++17)</sup>  and `std::unexpected`.

## Usage

While `throw` expression can be used to transfer control to an arbitrary block of code up the execution stack, for arbitrary reasons (similar to `std::longjmp`), its intended usage is error handling.

### Error handling

Throwing an exception is used to signal errors from functions, where "errors" are typically limited to only the following:
# Failures to meet the postconditions, such as failing to produce a valid return value object.
# Failures to meet the preconditions of another function that must be called.
# (for non-private member functions) Failures to (re)establish a class invariant.
In particular, this implies that the failures of constructors (see also RAII) and most operators should be reported by throwing exceptions.
In addition, so-called ''wide contract'' functions use exceptions to indicate unacceptable inputs, for example, `std::basic_string::at` has no preconditions, but throws an exception to indicate index out of range.

### Exception safety

After the error condition is reported by a function, additional guarantees may be provided with regards to the state of the program. The following four levels of exception guarantee are generally recognized, which are strict supersets of each other:
# ''Nothrow (or nofail) exception guarantee'' — the function never throws exceptions. Nothrow (errors are reported by other means or concealed) is expected of `destructor`s and other functions that may be called during stack unwinding. <sup>(since C++11)</sup> The `noexcept` by default. Nofail (the function always succeeds) is expected of swaps, `move constructor`s, and other functions used by those that provide strong exception guarantee.
# ''Strong exception guarantee'' — If the function throws an exception, the state of the program is rolled back to the state just before the function call (for example, `std::vector::push_back`).
# ''Basic exception guarantee'' — If the function throws an exception, the program is in a valid state. No resources are leaked, and all objects' invariants are intact.
# ''No exception guarantee'' — If the function throws an exception, the program may not be in a valid state: resource leaks, memory corruption, or other invariant-destroying errors may have occurred.
Generic components may, in addition, offer ''exception-neutral guarantee'': if an exception is thrown from a template parameter (e.g. from the `Compare` function object of `std::sort` or from the constructor of `T` in `std::make_shared`), it is propagated, unchanged, to the caller.

## Exception objects

While objects of any complete type and cv pointers to `void` may be thrown as exception objects, all standard library functions throw unnamed objects by value, and the types of those objects are derived (directly or indirectly) from `std::exception`. User-defined exceptions usually follow this pattern.
To avoid unnecessary copying of the exception object and object slicing, the best practice for handlers is to catch by reference.

## Notes


## External links

