---
title: std::function::function
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function/function
---


```cpp
dcl|num=1|since=c++11|
function() noexcept;
dcl|num=2|since=c++11|
function( std::nullptr_t ) noexcept;
dcl|num=3|since=c++11|
function( const function& other );
dcl rev multi|num=4|since1=c++11|until1=c++20|dcl1=
function( function&& other );
|dcl2=
function( function&& other ) noexcept;
dcla|num=5|since=c++11|
template< class F >
function( F&& f );
dcla|num=6|since=c++11|removed=c++17|
template< class Alloc >
function( std::allocator_arg_t, const Alloc& alloc ) noexcept;
dcl|num=7|since=c++11|removed=c++17|
template< class Alloc >
function( std::allocator_arg_t, const Alloc& alloc,
std::nullptr_t ) noexcept;
dcl|num=8|since=c++11|removed=c++17|
template< class Alloc >
function( std::allocator_arg_t, const Alloc& alloc,
const function& other );
dcl|num=9|since=c++11|removed=c++17|
template< class Alloc >
function( std::allocator_arg_t, const Alloc& alloc,
function&& other );
dcl|num=10|since=c++11|removed=c++17|
template< class F, class Alloc >
function( std::allocator_arg_t, const Alloc& alloc, F f );
```

Constructs a `std::function` from a variety of sources.
@1,2@ Creates an `empty` `std::function`.
3. Copies the `target` of `other` to the target of `*this`.
@@ If `other` is empty, `*this` will be empty right after the call too.
4. Moves the target of `other` to the target of `*this`.
@@ If `other` is empty, `*this` will be empty right after the call too.
@@ `other` is in a valid but unspecified state right after the call.
5. Initializes the target with `std::forward<F>(f)`. The target is of type `std::decay<F>::type`.
@@ If `f` is a null pointer to function, a null pointer to member, or an empty value of some `std::function` specialization, `*this` will be empty right after the call.
@@ :
rrev|since=c++23|
* `std::is_same_v<std::remove_cvref_t<F>, std::function<R(Args...)>` is `false`.
* An lvalue of type `std::decay<F>::type` is callable for argument types `Args...` and return type `R`.
rrev|since=c++23|
If `std::is_copy_constructible_v<std::decay_t<F>>` or `std::is_constructible_v<std::decay_t<F>, F>` is `false`, the program is ill-formed.
@@ If `F` is not *CopyConstructible*, the behavior is undefined.
@6-10@ Same as  except that `alloc` is used to allocate memory for any internal data structures that the `std::function` might use.
When the target is a function pointer or a `std::reference_wrapper`, small object optimization is guaranteed, that is, these targets are always directly stored inside the `std::function` object, no dynamic allocation takes place. Other large objects may be constructed in dynamic allocated storage and accessed by the `std::function` object through a pointer.

## Parameters


### Parameters

- `other` - the function object used to initialize `*this`
- `f` - a callable object used to initialize `*this`
- `alloc` - an *Allocator* used for internal memory allocation

**Type requirements:**

- `Alloc`

## Exceptions

@3,8,9@ Does not throw if `other`'s target is a function pointer or a `std::reference_wrapper`, otherwise may throw `std::bad_alloc` or any exception thrown by the constructor used to copy or move the stored callable object.
rrev|until=c++20|
4. Does not throw if `other`'s target is a function pointer or a `std::reference_wrapper`, otherwise may throw `std::bad_alloc` or any exception thrown by the constructor used to copy or move the stored callable object.
@5,10@ Does not throw if `f` is a function pointer or a `std::reference_wrapper`, otherwise may throw `std::bad_alloc` or any exception thrown by the copy constructor of the stored callable object.

## Notes

`std::function`'s allocator support was poorly specified and inconsistently implemented. Some implementations do not provide overloads  at all, some provide the overloads but ignore the supplied allocator argument, and some provide the overloads and use the supplied allocator for construction but not when the `std::function` is reassigned. As a result, allocator support was removed in C++17.

## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <utility>

void print_num(int i) { std::cout << "print_num(" << i << ")\n"; }

int main()
{
    std::function<void(int)> func1; // (1) empty constructor
    try
    {
        func1(333 << 1);
    }
    catch (const std::bad_function_call& ex)
    {
        std::cout << "1) " << ex.what() << '\n';
    }

    std::function<void(int)> func2{nullptr}; // (2) empty constructor
    try
    {
        func1(222 * 3);
    }
    catch (const std::bad_function_call& ex)
    {
        std::cout << "2) " << ex.what() << '\n';
    }

    func1 = print_num; // initializes func1 using assignment operator

    std::function<void(int)> func3{func1}; // (3) copy constructor
    func3(33);

    std::function<void(int)> func4{std::move(func3)}; // (4) move constructor,
                                                      // func3 in unspecified state
    func4(44);

    std::function<void(int)> func5{print_num}; // (5) constructor with function
    func5(55);

    // (5) constructor with lambda
    std::function<void(int)> func6([](int i) { std::cout << "lambda(" << i << ")\n"; });
    func6(66);
}
```


**Output:**
```
1) bad_function_call
2) bad_function_call
print_num(33)
print_num(44)
print_num(55)
lambda(66)
```


## Defect reports


## See also


| cpp/utility/functional/move_only_function/dsc constructor | (see dedicated page) |

