---
title: std::longjmp
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/program/longjmp
---


```cpp
**Header:** `<`csetjmp`>`
dcl rev multi|until1=c++17|dcl1=
void longjmp( std::jmp_buf env, int status );
|dcl2=
noreturn void longjmp( std::jmp_buf env, int status );
```

Loads the execution context `env` saved by a previous call to `setjmp`. This function does not return. Control is transferred to the call site of the macro `setjmp` that set up `env`. That `setjmp` then returns the value, passed as the `status`.
If the function that called `setjmp` has exited, the behavior is undefined (in other words, only long jumps up the call stack are allowed).

## Extra restrictions in C++

On top of C `c/program/longjmp`, C++ `std::longjmp` has more restricted behavior.
If replacing `std::longjmp` with `throw` and `setjmp` with `catch` would invoke a non-trivial destructor for any automatic object, the behavior of such `std::longjmp` is undefined.
rev|since=c++20|
The behavior is undefined if `std::longjmp` is called in a coroutine in a place where the `co_await` operator may be used.

## Parameters


### Parameters

- `env` - variable referring to the execution state of the program saved by `setjmp`
- `status` - the value to return from `setjmp`. If it is equal to `0`, `1` is used instead

## Notes

`std::longjmp` is the mechanism used in C to handle unexpected error conditions where the function cannot return meaningfully. C++ generally uses exception handling for this purpose.

## Example


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-619 | C++98 | the wording of the extra restrictions in C++ was vague | improved the wording |


## See also


| cpp/utility/program/dsc setjmp | (see dedicated page) |

