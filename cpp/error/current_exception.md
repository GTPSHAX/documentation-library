---
title: std::current_exception
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/current_exception
---

ddcla|header=exception|since=c++11|constexpr=c++26|
std::exception_ptr current_exception() noexcept;
If called during exception handling (typically, in a `catch` clause), captures the current exception object and creates an `std::exception_ptr` that holds either a copy or a reference to that exception object (depending on the implementation). The referenced object remains valid at least as long as there is an `exception_ptr` object that refers to it.
If the implementation of this function requires a call to `new` and the call fails, the returned pointer will hold a reference to an instance of `std::bad_alloc`.
If the implementation of this function requires copying the captured exception object and its copy constructor throws an exception, the returned pointer will hold a reference to the exception thrown. If the copy constructor of the thrown exception object also throws, the returned pointer may hold a reference to an instance of `std::bad_exception` to break the endless loop.
If the function is called when no exception is being handled, an empty `std::exception_ptr` is returned.
This function can be called in a `std::terminate_handler` to retrieve the exception which has provoked the invocation of `std::terminate`.

## Return value

An instance of `std::exception_ptr` holding a reference to the exception object, or a copy of the exception object, or to an instance of `std::bad_alloc` or to an instance of `std::bad_exception`.

## Notes

On the implementations that follow [https://itanium-cxx-abi.github.io/cxx-abi/abi.html Itanium C++ ABI] (GCC, Clang, etc), exceptions are allocated on the heap when thrown (except for `std::bad_alloc` in some cases), and this function simply creates the smart pointer referencing the previously-allocated object, On MSVC, exceptions are allocated on stack when thrown, and this function performs the heap allocation and copies the exception object.
On Windows in managed CLR environments [https://learn.microsoft.com/en-us/cpp/dotnet/exceptions-in-cpp-cli], the implementation will store a `std::bad_exception` when the current exception is a managed exception ([https://github.com/microsoft/STL/blob/65aab97a8e75e7ba409002e518ed799006dfb285/stl/src/excptptr.cpp#L367]). Note that `catch(...)` catches also managed exceptions:

```cpp
#include <exception>

int main()
{
    try
    {
        throw gcnew System::Exception("Managed exception");
    }
    catch (...)
    {
        std::exception_ptr ex = std::current_exception();
        try
        {
            std::rethrow_exception(ex);
        }
        catch (std::bad_exception const &)
        {
            // This will be printed.
            std::cout << "Bad exception" << std::endl;
        }
    }
}
```


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_constexpr_exceptions` | 202411L | C++26 | `constexpr` for exception types |


## Example


## See also


| cpp/error/dsc exception_ptr | (see dedicated page) |
| cpp/error/dsc rethrow_exception | (see dedicated page) |
| cpp/error/dsc make_exception_ptr | (see dedicated page) |
| cpp/error/dsc uncaught_exception | (see dedicated page) |

