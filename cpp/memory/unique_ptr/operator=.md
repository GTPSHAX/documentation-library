---
title: std::unique_ptr::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/unique_ptr/operator=
---


```cpp
dcla|num=1|constexpr=c++23|1=
unique_ptr& operator=( unique_ptr&& r ) noexcept;
dcla|num=2|constexpr=c++23|1=
template< class U, class E >
unique_ptr& operator=( unique_ptr<U, E>&& r ) noexcept;
dcla|num=3|constexpr=c++23|1=
unique_ptr& operator=( std::nullptr_t ) noexcept;
dcl|num=4|1=
unique_ptr& operator=( const unique_ptr& ) = delete;
```

1. Move assignment operator. Transfers ownership from `r` to `*this` as if by calling `reset(r.release())` followed by assigning `get_deleter()` from `std::forward<Deleter>(r.get_deleter())`.
@@ .
@@ If `Deleter` is not a reference type, the behavior is undefined if
* `Deleter` is not *MoveAssignable*, or
* assigning `get_deleter()` from an rvalue of type `Deleter` would throw an exception.
@@ Otherwise (`Deleter` is a reference type), the behavior is undefined if
* `std::remove_reference<Deleter>::type` is not *CopyAssignable*, or
* assigning `get_deleter()` from an lvalue of type `Deleter` would throw an exception.
2. Converting assignment operator. Transfers ownership from `r` to `*this` as if by calling `reset(r.release())` followed by assigning `get_deleter()` from `std::forward<E>(r.get_deleter())`.
@@ :
* `std::is_assignable<Deleter&, E&&>::value` is `true`.
* For the primary template, all following conditions are satisfied:
** `U` is not an array type.
** `unique_ptr<U, E<nowiki>></nowiki>::pointer` is implicitly convertible to `pointer`, and.
* For the array specialization (`unique_ptr<T[]>`), all following conditions are satisfied:
** `U` is an array type.
** `pointer` is the same type as `element_type*`.
** `unique_ptr<U, E<nowiki>></nowiki>::pointer` is the same type as `unique_ptr<U, E<nowiki>></nowiki>::element_type*`.
** `unique_ptr<U, E<nowiki>></nowiki>::element_type(*)[]` is convertible to `element_type(*)[]`.
@@ If `E` is not a reference type, the behavior is undefined if assigning `get_deleter()` from an rvalue of type `E` is ill-formed or would throw an exception.
@@ Otherwise (`E` is a reference type), the behavior is undefined if assigning `get_deleter()` from an lvalue of type `E` is ill-formed or would throw an exception.
3. Effectively the same as calling `reset()`.
4. Copy assignment operator is explicitly deleted.

## Parameters


### Parameters

- `r` - smart pointer from which ownership will be transferred

## Return value

`*this`

## Notes

As a move-only type, `unique_ptr`'s assignment operator only accepts rvalues arguments (e.g. the result of `std::make_unique` or a `std::move`'d `unique_ptr` variable).

## Example


### Example

```cpp
#include <iostream>
#include <memory>

struct Foo
{
    int id;
    Foo(int id) : id(id) { std::cout << "Foo " << id << '\n'; }
    ~Foo() { std::cout << "~Foo " << id << '\n'; }
};

int main() 
{
    std::unique_ptr<Foo> p1(std::make_unique<Foo>(1));

    {
        std::cout << "Creating new Foo...\n";
        std::unique_ptr<Foo> p2(std::make_unique<Foo>(2));
        // p1 = p2; // Error ! can't copy unique_ptr
        p1 = std::move(p2);
        std::cout << "About to leave inner block...\n";

        // Foo instance will continue to live, 
        // despite p2 going out of scope
    }

    std::cout << "About to leave program...\n";
}
```


**Output:**
```
Foo 1
Creating new Foo...
Foo 2
~Foo 1
About to leave inner block...
About to leave program...
~Foo 2
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2899 | C++11 | the move assignment operator was not constrained | constrained |

