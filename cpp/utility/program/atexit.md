---
title: std::atexit
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/program/atexit
---


```cpp
**Header:** `<`cstdlib`>`
dcl rev multi|num=1|until1=c++11|dcl1=
int atexit( /*c-atexit-handler*/* func );
int atexit( /*atexit-handler*/* func );
|dcl2=
int atexit( /*c-atexit-handler*/* func ) noexcept;
int atexit( /*atexit-handler*/* func ) noexcept;
dcla|num=2|expos=yes|1=
extern "C" using /*c-atexit-handler*/ = void();
extern "C++" using /*atexit-handler*/ = void();
```

Registers the function pointed to by `func` to be called on normal program termination (via `std::exit()` or returning from the main function)
rrev multi|until1=c++11|rev1=
The functions will be called during the destruction of the static objects, in reverse order: if A was registered before B, then the call to B is made before the call to A. Same applies to the ordering between static object constructors and the calls to `atexit`: see `std::exit`.|rev2=
The functions may be called concurrently with the destruction of the objects with static storage duration and with each other, maintaining the guarantee that if registration of A was sequenced-before the registration of B, then the call to B is sequenced-before the call to A, same applies to the sequencing between static object constructors and calls to `atexit`: see `std::exit`.
The same function may be registered more than once.
If a function exits via an exception, `std::terminate` is called.
`atexit` is thread-safe: calling the function from several threads does not induce a data race.
The implementation is guaranteed to support the registration of at least 32 functions. The exact limit is implementation-defined.

## Parameters


### Parameters

- `func` - pointer to a function to be called on normal program termination

## Return value

`0` if the registration succeeds, nonzero value otherwise.

## Notes

The two overloads are distinct because the types of the parameter `func` are distinct ( is part of its type).

## Example


### Example

```cpp
#include <cstdlib>
#include <iostream>

void atexit_handler_1()
{
    std::cout << "At exit #1\n";
}

void atexit_handler_2()
{
    std::cout << "At exit #2\n";
}

int main()
{
    const int result_1 = std::atexit(atexit_handler_1);
    const int result_2 = std::atexit(atexit_handler_2);

    if (result_1 {{!!
```

{
std::cerr << "Registration failed!\n";
return EXIT_FAILURE;
}
std::cout << "Returning from main...\n";
return EXIT_SUCCESS;
}
|output=
Returning from main...
At exit #2
At exit #1

## See also


| cpp/utility/program/dsc abort | (see dedicated page) |
| cpp/utility/program/dsc exit | (see dedicated page) |
| cpp/utility/program/dsc quick_exit | (see dedicated page) |
| cpp/utility/program/dsc at_quick_exit | (see dedicated page) |

