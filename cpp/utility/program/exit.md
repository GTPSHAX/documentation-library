---
title: std::exit
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/program/exit
---


```cpp
**Header:** `<`cstdlib`>`
dcl rev multi|until1=c++11|dcl1=
void exit( int exit_code );
|dcl2=
noreturn void exit( int exit_code );
```

Causes normal program termination to occur.
Several cleanup steps are performed:
rrev multi|until1=c++11
|rev1=
1. Objects with static storage duration are destroyed and functions registered by calling `std::atexit` are called:
:@a@ Non-local objects with static storage duration are destroyed in the reverse order of the completion of their constructor.
:@b@ Functions registered with `std::atexit` are called in the reverse order of their registration, except that a function is called after any previously registered functions that had already been called at the time it was registered.
:@c@ For each function `f` registered with `std::atexit` and each non-local object `obj` of static storage duration,
:* if `f` is registered before the initialization of `obj`, `f` will only be called after the destruction of `obj`;
:* if `f` is registered after the initialization of `obj`, `f` will only be called before the destruction of `obj`.
:@d@ For each local object `obj` with static storage duration, `obj` is destroyed as if a function calling the destructor of `obj` were registered with `std::atexit` at the completion of the constructor of `obj`.
|rev2=
1. The destructors of objects with thread local storage duration that are associated with the current thread, the destructors of objects with static storage duration, and the functions registered with `std::atexit` are executed concurrently, while maintaining the following guarantees:
:@a@ The last destructor for thread-local objects is sequenced-before the first destructor for a static object.
:@b@ If the completion of the constructor or dynamic initialization for thread-local or static object A was sequenced-before thread-local or static object B, the completion of the destruction of B is sequenced-before the start of the destruction of A.
:@c@ If the completion of the initialization of a static object A was sequenced-before the call to `std::atexit` for some function F, the call to F during termination is sequenced-before the start of the destruction of A.
:@d@ If the call to `std::atexit` for some function F was sequenced-before the completion of initialization of a static object A, the start of the destruction of A is sequenced-before the call to F during termination.
:@e@ If a call to `std::atexit` for some function F1 was sequenced-before the call to `std::atexit` for some function F2, then the call to F2 during termination is sequenced-before the call to F1.
:* In the above,
::* If any function registered with `atexit` or any destructor of static/thread-local object throws an exception, `std::terminate` is called.
::* If the compiler opted to lift dynamic initialization of an object to the static initialization phase of non-local initialization, the sequencing of destruction honors its would-be dynamic initialization.
::* If a function-local (block-scope) static object was destroyed and then that function is called from the destructor of another static object and the control flow passes through the definition of that object (or if it is used indirectly, via pointer or reference), the behavior is undefined.
::* If a function-local (block-scope) static object was initialized during construction of a subobject of a class or array, it is only destroyed after all subobjects of that class or all elements of that array were destroyed.
2. All C streams are flushed and closed.
3. Files created by `std::tmpfile` are removed.
4. Control is returned to the host environment. If `exit_code` is `0` or `EXIT_SUCCESS`, an implementation-defined status indicating successful termination is returned. If `exit_code` is `EXIT_FAILURE`, an implementation-defined status indicating unsuccessful termination is returned. In other cases implementation-defined status value is returned.
Stack is not unwound: destructors of variables with automatic storage duration are not called.

## Relationship with the main function

Returning from the main function, either by a `return` statement or by reaching the end of the function performs the normal function termination (calls the destructors of the variables with automatic storage durations) and then executes `std::exit`, passing the argument of the return statement (or `0` if implicit return was used) as `exit_code`.

## Parameters


### Parameters

- `exit_code` - exit status of the program

## Example


### Example

```cpp
#include <cstdlib>
#include <iostream>

struct Static
{
    ~Static() 
    {
        std::cout << "Static destructor\n";
    }
};

struct Local
{
    ~Local() 
    {
        std::cout << "Local destructor\n";
    }
};

Static static_variable; // Destructor of this object *will* be called

void atexit_handler()
{
    std::cout << "atexit handler\n";
}

int main()
{
    Local local_variable; // Destructor of this object will *not* be called
    const int result = std::atexit(atexit_handler); // Handler will be called

    if (result != 0)
    {
        std::cerr << "atexit registration failed\n";
        return EXIT_FAILURE;
    }

    std::cout << "test\n";
    std::exit(EXIT_FAILURE);

    std::cout << "this line will *not* be executed\n";
}
```


**Output:**
```
test
atexit handler
Static destructor
```


## Defect reports


## See also


| cpp/utility/program/dsc abort | (see dedicated page) |
| cpp/utility/program/dsc atexit | (see dedicated page) |
| cpp/utility/program/dsc quick_exit | (see dedicated page) |
| cpp/utility/program/dsc at_quick_exit | (see dedicated page) |

