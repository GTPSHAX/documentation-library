---
title: std::bad_exception
type: Utilities
source: https://en.cppreference.com/w/cpp/error/bad_exception
---

ddcl|header=exception|
class bad_exception;
`std::bad_exception` is the type of the exception thrown by the C++ runtime in the following situations:
rev|since=c++11|
* If `std::exception_ptr` stores a copy of the caught exception and if the copy constructor of the exception object caught by `std::current_exception` throws an exception, the captured exception is an instance of `std::bad_exception`.
rev|until=c++17|
* If a dynamic exception specification is violated and `std::unexpected` throws or rethrows an exception that still violates the exception specification, but the exception specification allows `std::bad_exception`, `std::bad_exception` is thrown.
<sup>(since C++26)</sup> All member functions of `std::bad_exception` are `constexpr`.

## Member functions


## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_constexpr_exceptions` | 202411L | C++26 | `constexpr` for exception types |


## Example


### Example

```cpp
#include <exception>
#include <iostream>
#include <stdexcept>

void my_unexp()
{
    throw;
}

void test()
    throw(std::bad_exception) // Dynamic exception specifications
                              // are deprecated in C++11
{
    throw std::runtime_error("test");
}

int main()
{
    std::set_unexpected(my_unexp); // Deprecated in C++11, removed in C++17

    try
    {
        test();
    }
    catch (const std::bad_exception& e)
    {
        std::cerr << "Caught " << e.what() << '\n';
    }
}
```


**Output:**
```
Caught std::bad_exception
```

