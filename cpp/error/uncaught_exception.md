---
title: std::uncaught_exceptions
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/uncaught_exception
---


```cpp
**Header:** `<`exception`>`
dcl rev multi|num=1|until1=c++11|dcl1=
bool uncaught_exception() throw();
|notes2=|dcl2=
bool uncaught_exception() noexcept;
dcla|num=2|since=c++17|constexpr=c++26|
int uncaught_exceptions() noexcept;
```

1. Detects if the current thread has a live exception object, that is, an exception has been thrown or rethrown and not yet entered a matching catch clause, `std::terminate` or `std::unexpected`. In other words, `std::uncaught_exception` detects if  is currently in progress.
2. Detects how many exceptions in the current thread have been thrown or rethrown and not yet entered their matching catch clauses.
Sometimes it's safe to throw an exception even while <sup>(until C++17)</sup> `1=std::uncaught_exception() == true` <sup>(since C++17)</sup> `1=std::uncaught_exceptions() > 0`. For example, if  causes an object to be destructed, the destructor for that object could run code that throws an exception as long as the exception is caught by some catch block before escaping the destructor.

## Return value

1. `true` if stack unwinding is currently in progress in this thread, `false` otherwise.
2. The number of uncaught exception objects in the current thread.

## Notes

An example where int-returning `uncaught_exceptions` is used is the [https://www.boost.org/doc/libs/release/libs/log/doc/html/index.html boost.log] library: the expression `BOOST_LOG(logger) << foo();` first creates a guard object and records the number of uncaught exceptions in its constructor. The output is performed by the guard object's destructor unless `foo()` throws (in which case the number of uncaught exceptions in the destructor is greater than what the constructor observed).
`cpp/experimental/scope_fail|std::experimental::scope_fail` and `cpp/experimental/scope_success|std::experimental::scope_success` in LFTS v3 rely on the functionality of `uncaught_exceptions`, because their destructors need to do different things that depend on whether is called during stack unwinding.

## Example


### Example

```cpp
#include <exception>
#include <iostream>
#include <stdexcept>

struct Foo
{
    char id{'?'};
    int count = std::uncaught_exceptions();

    ~Foo()
    {
        count == std::uncaught_exceptions()
            ? std::cout << id << ".~Foo() called normally\n"
            : std::cout << id << ".~Foo() called during stack unwinding\n";
    }
};

int main()
{
    Foo f{'f'};

    try
    {
        Foo g{'g'};
        std::cout << "Exception thrown\n";
        throw std::runtime_error("test exception");
    }
    catch (const std::exception& e)
    {
        std::cout << "Exception caught: " << e.what() << '\n';
    }
}
```


**Output:**
```
Exception thrown
g.~Foo() called during stack unwinding
Exception caught: test exception
f.~Foo() called normally
```


## Defect reports


## See also


| cpp/error/dsc terminate | (see dedicated page) |
| cpp/error/dsc exception_ptr | (see dedicated page) |
| cpp/error/dsc current_exception | (see dedicated page) |


## External links

