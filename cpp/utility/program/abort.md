---
title: std::abort
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/program/abort
---


```cpp
**Header:** `<`cstdlib`>`
dcl rev multi|until1=c++11|dcl1=
void abort();
|dcl2=
noreturn void abort() noexcept;
```

Causes abnormal program termination unless `SIGABRT` is being caught by a signal handler passed to `std::signal` and the handler does not return.
Destructors of variables with automatic<sup>(since C++11)</sup> , thread local and static s are not called. Functions registered with `std::atexit()` <sup>(since C++11)</sup> and `std::at_quick_exit` are also not called. Whether open resources such as files are closed is implementation defined. An implementation defined status is returned to the host environment that indicates unsuccessful execution.

## Return value

None because it does not return.

## Exceptions

Throws nothing.

## Notes

POSIX specifies that the  function overrides blocking or ignoring the `SIGABRT` signal.
Some compiler intrinsics, e.g. [https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html `__builtin_trap`] (gcc, clang, and icc) or [https://learn.microsoft.com/en-us/cpp/intrinsics/fastfail `__fastfail`]/[https://learn.microsoft.com/en-us/cpp/intrinsics/debugbreak `__debugbreak`] (msvc), can be used to terminate the program as fast as possible.

## Example


### Example

```cpp
#include <csignal>
#include <cstdlib>
#include <iostream>

class Tester
{
public:
    Tester()  { std::cout << "Tester ctor\n"; }
    ~Tester() { std::cout << "Tester dtor\n"; }
};

Tester static_tester; // Destructor not called

void signal_handler(int signal)
{
    if (signal == SIGABRT)
        std::cerr << "SIGABRT received\n";
    else
        std::cerr << "Unexpected signal " << signal << " received\n";
    std::_Exit(EXIT_FAILURE);
}

int main()
{
    Tester automatic_tester; // Destructor not called

    // Setup handler
    auto previous_handler = std::signal(SIGABRT, signal_handler);
    if (previous_handler == SIG_ERR)
    {
        std::cerr << "Setup failed\n";
        return EXIT_FAILURE;
    }

    std::abort(); // Raise SIGABRT
    std::cout << "This code is unreachable\n";
}
```


**Output:**
```
Tester ctor
Tester ctor
SIGABRT received
```


## See also


| cpp/utility/program/dsc exit | (see dedicated page) |
| cpp/utility/program/dsc atexit | (see dedicated page) |
| cpp/utility/program/dsc quick_exit | (see dedicated page) |
| cpp/utility/program/dsc at_quick_exit | (see dedicated page) |
| cpp/utility/program/dsc signal | (see dedicated page) |
| cpp/error/dsc terminate | (see dedicated page) |

