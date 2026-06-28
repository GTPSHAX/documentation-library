---
title: std::mem_fun
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/mem_fun
---


```cpp
**Header:** `<`functional`>`
dcl|deprecated=c++11|until=c++17|num=1|
template< class Res, class T >
std::mem_fun_t<Res,T> mem_fun( Res (T::*f)() );
dcl|deprecated=c++11|until=c++17|num=1|
template< class Res, class T >
std::const_mem_fun_t<Res,T> mem_fun( Res (T::*f)() const );
dcl|deprecated=c++11|until=c++17|num=2|
template< class Res, class T, class Arg >
std::mem_fun1_t<Res,T,Arg> mem_fun( Res (T::*f)(Arg) );
dcl|deprecated=c++11|until=c++17|num=2|
template< class Res, class T, class Arg >
std::const_mem_fun1_t<Res,T,Arg> mem_fun( Res (T::*f)(Arg) const );
```

Creates a member function wrapper object, deducing the target type from the template arguments. The wrapper object expects a pointer to an object of type `T` as the first parameter to its `operator()`.
1. Effectively calls `std::mem_fun_t<Res,T>(f)` or `std::const_mem_fun_t<Res,T>(f)`.
2. Effectively calls `std::mem_fun1_t<Res,T,Arg>(f)` or `std::const_mem_fun1_t<Res,T,Arg>(f)`.
This function and the related types were deprecated in C++11 and removed in C++17 in favor of the more general `std::mem_fn` and `std::bind`, both of which create callable adaptor-compatible function objects from member functions.

## Parameters


### Parameters

- `f` - pointer to a member function to create a wrapper for

## Return value

A function object wrapping `f`.

## Notes

The difference between `std::mem_fun` and `std::mem_fun_ref` is that the former produces a function wrapper that expects a pointer to an object, whereas the latter &mdash; a reference.

## Example


### Example

```cpp
#include <functional>
#include <iostream>

struct S
{
    int get_data() const { return data; }
    void no_args() const { std::cout << "void S::no_args() const\n"; }
    void one_arg(int) { std::cout << "void S::one_arg()\n"; }
    void two_args(int, int) { std::cout << "void S::two_args(int, int)\n"; }
#if __cplusplus > 201100
    int data{42};
#else
    int data;
    S() : data(42) {}
#endif
};

int main()
{
    S s;

    std::const_mem_fun_t<int, S> p = std::mem_fun(&S::get_data);
    std::cout << "s.get_data(): " << p(&s) << '\n';

    std::const_mem_fun_t<void, S> p0 = std::mem_fun(&S::no_args);
    p0(&s);

    std::mem_fun1_t<void, S, int> p1 = std::mem_fun(&S::one_arg);
    p1(&s, 1);

#if __cplusplus > 201100
//  auto p2 = std::mem_fun(&S::two_args); // Error: mem_fun supports only member functions
                                          // without parameters or with only one parameter.
                                          // Thus, std::mem_fn is a better alternative:
    auto p2 = std::mem_fn(&S::two_args);
    p2(s, 1, 2);

//  auto pd = std::mem_fun(&S::data); // Error: pointers to data members are not supported.
                                      // Use std::mem_fn instead:
    auto pd = std::mem_fn(&S::data);
    std::cout << "s.data = " << pd(s) << '\n';
#endif
}
```


**Output:**
```
s.get_data(): 42
void S::no_args() const
void S::one_arg(int)
void S::two_args(int, int)
s.data = 42
```


## See also


| cpp/utility/functional/dsc mem_fn | (see dedicated page) |
| cpp/utility/functional/dsc mem_fun_ref | (see dedicated page) |

