---
title: std::function
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function
---


```cpp
**Header:** `<`functional`>`
dcl|since=c++11|
template< class >
class function; /* undefined */
dcl|since=c++11|
template< class R, class... Args >
class function<R(Args...)>;
```

Class template `std::function` is a general-purpose polymorphic function wrapper. Instances of `std::function` can store, copy, and invoke any *CopyConstructible* *Callable* ''target'' -- functions (via pointers thereto), lambda expressions, bind expressions, or other function objects, as well as pointers to member functions and pointers to data members.
The stored callable object is called the ''target'' of `std::function`. If a `std::function` contains no target, it is called ''empty''. Invoking the ''target'' of an ''empty'' `std::function` results in `std::bad_function_call` exception being thrown.
`std::function` satisfies the requirements of *CopyConstructible* and *CopyAssignable*.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/utility/functional/function/dsc constructor | (see dedicated page) |
| cpp/utility/functional/function/dsc destructor | (see dedicated page) |
| cpp/utility/functional/function/dsc operator{{= | (see dedicated page) |
| cpp/utility/functional/function/dsc swap | (see dedicated page) |
| cpp/utility/functional/function/dsc assign | (see dedicated page) |
| cpp/utility/functional/function/dsc operator_bool | (see dedicated page) |
| cpp/utility/functional/function/dsc operator() | (see dedicated page) |

#### Target access

| cpp/utility/functional/function/dsc target_type | (see dedicated page) |
| cpp/utility/functional/function/dsc target | (see dedicated page) |


## Non-member functions


| cpp/utility/functional/function/dsc swap2 | (see dedicated page) |
| cpp/utility/functional/function/dsc operator_cmp | (see dedicated page) |


## Helper classes


| cpp/utility/functional/function/dsc uses_allocator | (see dedicated page) |


## Deduction guides<sup>(C++17)</sup>


## Notes

rrev multi
|rev1=
Care should be taken when a `std::function`, whose result type is a reference, is initialized from a lambda expression without a trailing-return-type. Due to the way auto deduction works, such lambda expression will always return a prvalue. Hence, the resulting reference will usually bind to a temporary whose lifetime ends when  returns.
|since2=c++23|rev2=
If a `std::function` returning a reference is initialized from a function or function object returning a prvalue (including a lambda expression without a trailing-return-type), the program is ill-formed because binding the returned reference to a temporary object is forbidden.

```cpp
std::function<const int&()> F([] { return 42; }); // Error since C++23: can't bind
                                                  // the returned reference to a temporary
int x = F(); // Undefined behavior until C++23: the result of F() is a dangling reference

std::function<int&()> G([]() -> int& { static int i{0x2A}; return i; }); // OK

std::function<const int&()> H([i{052}] -> const int& { return i; }); // OK
```


## Example


### Example

```cpp
#include <functional>
#include <iostream>

struct Foo
{
    Foo(int num) : num_(num) {}
    void print_add(int i) const { std::cout << num_ + i << '\n'; }
    int num_;
};

void print_num(int i)
{
    std::cout << i << '\n';
}

struct PrintNum
{
    void operator()(int i) const
    {
        std::cout << i << '\n';
    }
};

int main()
{
    // store a free function
    std::function<void(int)> f_display = print_num;
    f_display(-9);

    // store a lambda
    std::function<void()> f_display_42 = []() { print_num(42); };
    f_display_42();

    // store the result of a call to std::bind
    std::function<void()> f_display_31337 = std::bind(print_num, 31337);
    f_display_31337();

    // store a call to a member function
    std::function<void(const Foo&, int)> f_add_display = &Foo::print_add;
    const Foo foo(314159);
    f_add_display(foo, 1);
    f_add_display(314159, 1);

    // store a call to a data member accessor
    std::function<int(Foo const&)> f_num = &Foo::num_;
    std::cout << "num_: " << f_num(foo) << '\n';

    // store a call to a member function and object
    using std::placeholders::_1;
    std::function<void(int)> f_add_display2 = std::bind(&Foo::print_add, foo, _1);
    f_add_display2(2);

    // store a call to a member function and object ptr
    std::function<void(int)> f_add_display3 = std::bind(&Foo::print_add, &foo, _1);
    f_add_display3(3);

    // store a call to a function object
    std::function<void(int)> f_display_obj = PrintNum();
    f_display_obj(18);

    auto factorial = [](int n)
    {
        // store a lambda object to emulate "recursive lambda"; aware of extra overhead
        std::function<int(int)> fac = [&](int n) { return (n < 2) ? 1 : n * fac(n - 1); };
        // note that "auto fac = [&](int n) {...};" does not work in recursive calls
        return fac(n);
    };
    for (int i{5}; i != 8; ++i)
        std::cout << i << "! = " << factorial(i) << ";  ";
    std::cout << '\n';
}
-9
42
31337
314160
314160
num_: 314159
314161
314162
18
5! = 120;  6! = 720;  7! = 5040;
```


## See also


| cpp/utility/functional/dsc move_only_function | (see dedicated page) |
| cpp/utility/functional/dsc copyable_function | (see dedicated page) |
| cpp/utility/functional/dsc function_ref | (see dedicated page) |
| cpp/utility/functional/dsc bad_function_call | (see dedicated page) |
| cpp/utility/functional/dsc mem_fn | (see dedicated page) |

