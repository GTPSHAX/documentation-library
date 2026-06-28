---
title: setjmp
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/program/setjmp
---


# setjmp

ddcl|header=csetjmp|
#define setjmp(env) /* implementation-defined */
Saves the current execution context into a variable `env` of type `std::jmp_buf`. This variable can later be used to restore the current execution context by `std::longjmp` function. That is, when a call to `std::longjmp` function is made, the execution continues at the particular call site that constructed the `std::jmp_buf` variable passed to `std::longjmp`. In that case `setjmp` returns the value passed to `std::longjmp`.
The invocation of `setjmp` must appear only in one of the following contexts:
# the entire controlling expression of `cpp/language/if`, `cpp/language/switch`, `cpp/language/while`, `cpp/language/do|do-while`, `cpp/language/for`.<!--

```cpp
switch (setjmp(env)) { // ...
```

# one operand of a relational or equality operator with the other operand an integer constant expression, with the resulting expression being the entire controlling expression of `cpp/language/if`, `cpp/language/switch`, `cpp/language/while`, `cpp/language/do|do-while`, `cpp/language/for`.<!--

```cpp
if (setjmp(env) > 0) { // ...
```

# the operand of a unary ! operator with the resulting expression being the entire controlling expression of `cpp/language/if`, `cpp/language/switch`, `cpp/language/while`, `cpp/language/do|do-while`, `cpp/language/for`.<!--

```cpp
while (!setjmp(env)) { // ...
```

# the entire expression of an expression statement (possibly cast to `void`).<!--

```cpp
setjmp(env);
```

If `setjmp` appears in any other context, the behavior is undefined.
rev|since=c++20|
Additionally, the behavior is undefined if `setjmp` is invoked in a coroutine in a place where the `co_await` operator may be used.
Upon return to the scope of `setjmp`:
* all accessible objects, floating-point status flags, and other components of the abstract machine have the same values as they had when `std::longjmp` was executed,
* except for the non-volatile local variables in the function containing the invocation of `setjmp`, whose values are indeterminate if they have been changed since the `setjmp` invocation.

## Parameters


### Parameters

- `env` - variable to save the execution state of the program to

## Return value

`0` if the macro was called by the original code and the execution context was saved to `env`.
Non-zero value if a non-local jump was just performed. The return value is the same as passed to `std::longjmp`.

## Notes

Above requirements forbid using return value of `setjmp` in data flow (e.g. to initialize or assign an object with it). The return value can only be either used in control flow or discarded.

## Example


## See also


| cpp/utility/program/dsc longjmp | (see dedicated page) |

