---
title: std::unique_ptr::unique_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/unique_ptr/unique_ptr
---


```cpp
dcl|num=1|
constexpr unique_ptr() noexcept;
constexpr unique_ptr( std::nullptr_t ) noexcept;
dcla|num=2|constexpr=c++23|
explicit unique_ptr( pointer p ) noexcept;
dcla|num=3|constexpr=c++23|
unique_ptr( pointer p, /* see below */ d1 ) noexcept;
dcla|num=4|constexpr=c++23|
unique_ptr( pointer p, /* see below */ d2 ) noexcept;
dcla|num=5|constexpr=c++23|
unique_ptr( unique_ptr&& u ) noexcept;
dcla|num=6|constexpr=c++23|
template< class U, class E >
unique_ptr( unique_ptr<U, E>&& u ) noexcept;
dcl|num=7|1=
unique_ptr( const unique_ptr& ) = delete;
dcl|num=8|removed=c++17|
template< class U >
unique_ptr( std::auto_ptr<U>&& u ) noexcept;
dcl|num=1|
constexpr unique_ptr() noexcept;
constexpr unique_ptr( std::nullptr_t ) noexcept;
dcla|num=2|anchor=no|constexpr=c++23|
template< class U >
explicit unique_ptr( U p ) noexcept;
dcla|num=3|anchor=no|constexpr=c++23|
template< class U >
unique_ptr( U p, /* see below */ d1 ) noexcept;
dcla|num=4|anchor=no|constexpr=c++23|
template< class U >
unique_ptr( U p, /* see below */ d2 ) noexcept;
dcla|num=5|anchor=no|constexpr=c++23|
unique_ptr( unique_ptr&& u ) noexcept;
dcla|num=6|anchor=no|constexpr=c++23|
template< class U, class E >
unique_ptr( unique_ptr<U, E>&& u ) noexcept;
dcl|num=7|1=
unique_ptr( const unique_ptr& ) = delete;
```

1. Constructs a `std::unique_ptr` that owns nothing. Value-initializes the stored pointer and the stored deleter. Requires that `Deleter` is *DefaultConstructible* and that construction does not throw an exception. .
2. Constructs a `std::unique_ptr` which owns `p`, initializing the stored pointer with `p` and value-initializing the stored deleter. Requires that `Deleter` is *DefaultConstructible* and that construction does not throw an exception. .
rrev|since=c++17|
This constructor is not selected by class template argument deduction.
@3,4@ Constructs a `std::unique_ptr` object which owns `p`, initializing the stored pointer with `p` and initializing a deleter `D` as below (depends upon whether `D` is a reference type).
:@a@ If `D` is non-reference type `A`, then the signatures are:

```cpp
is nothrow-*CopyConstructible*)
is nothrow-*MoveConstructible*)
```

:@b@ If `D` is an lvalue-reference type `A&`, then the signatures are:

```cpp
```

:@c@ If `D` is an lvalue-reference type `const A&`, then the signatures are:

```cpp
```

@@ In all cases the deleter is initialized from `std::forward<decltype(d)>(d)`. .
rrev|since=c++17|
These two constructors are not selected by class template argument deduction.
@2-4@ In the specialization for arrays behave the same as the constructors that take a pointer parameter in the primary template except that they additionally do not participate in overload resolution unless one of the following is true:
* `U` is the same type as `pointer`, or
* `U` is `std::nullptr_t`, or
* `pointer` is the same type as `element_type*` and `U` is some pointer type `V*` such that `V(*)[]` is implicitly convertible to `element_type(*)[]`.
5. Constructs a `unique_ptr` by transferring ownership from `u` to `*this` and stores the null pointer in `u`. This constructor only participates in overload resolution if `std::is_move_constructible<Deleter>::value` is `true`. If `Deleter` is not a reference type, requires that it is nothrow-*MoveConstructible* (if `Deleter` is a reference, `get_deleter()` and `u.get_deleter()` after move construction reference the same value).
6. Constructs a `unique_ptr` by transferring ownership from `u` to `*this`, where `u` is constructed with a specified deleter (`E`). It depends upon whether `E` is a reference type, as following:
:@a@ if `E` is a reference type, this deleter is copy constructed from `u`'s deleter (requires that this construction does not throw),
:@b@ if `E` is a non-reference type, this deleter is move constructed from `u`'s deleter (requires that this construction does not throw).
@@ This constructor only participates in overload resolution if all of the following is true:
:@a@ `unique_ptr<U, E>::pointer` is implicitly convertible to `pointer`,
:@b@ U is not an array type,
:@c@ either `Deleter` is a reference type and `E` is the same type as `Deleter`, or `Deleter` is not a reference type and `E` is implicitly convertible to `Deleter`.
6. In the specialization for arrays behaves the same as in the primary template, except that it will only participate in overload resolution if all of the following is true:
* `U` is an array type,
* `pointer` is the same type as `element_type*`,
* `unique_ptr<U,E>::pointer` is the same type as `unique_ptr<U,E>::element_type*`,
* `unique_ptr<U,E>::element_type(*)[]` is convertible to `element_type(*)[]`,
* either `Deleter` is a reference type and `E` is the same type as `Deleter`, or `Deleter` is not a reference type and `E` is implicitly convertible to `Deleter`.
7. Copy constructor is explicitly deleted.
8. Constructs a `unique_ptr` where the stored pointer is initialized with  and the stored deleter is value-initialized. This constructor only participates in overload resolution if `U*` is implicitly convertible to `T*` and `Deleter` is the same type as `std::default_delete<T>`.

## Parameters


### Parameters

- `p` - a pointer to an object to manage
- `d1, d2` - a deleter to use to destroy the object
- `u` - another smart pointer to acquire the ownership from

## Notes

rrev|since=c++14|
Instead of using the overload  together with new, it is often a better idea to use `std::make_unique|std::make_unique<T>`.
`std::unique_ptr<Derived>` is implicitly convertible to `std::unique_ptr<Base>` through the overload  (because both the managed pointer and `std::default_delete` are implicitly convertible).
Because the default constructor is `constexpr`, static unique_ptrs are initialized as part of static non-local initialization, before any dynamic non-local initialization begins. This makes it safe to use a unique_ptr in a constructor of any static object.
<sup>(since C++17)</sup> There is no class template argument deduction from pointer type because it is impossible to distinguish a pointer obtained from array and non-array forms of `new`.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

struct Foo // object to manage
{
    Foo() { std::cout << "Foo ctor\n"; }
    Foo(const Foo&) { std::cout << "Foo copy ctor\n"; }
    Foo(Foo&&) { std::cout << "Foo move ctor\n"; }
    ~Foo() { std::cout << "~Foo dtor\n"; }
};

struct D // deleter
{
    D() {};
    D(const D&) { std::cout << "D copy ctor\n"; }
    D(D&) { std::cout << "D non-const copy ctor\n"; }
    D(D&&) { std::cout << "D move ctor \n"; }
    void operator()(Foo* p) const
    {
        std::cout << "D is deleting a Foo\n";
        delete p;
    };
};

int main()
{
    std::cout << "Example constructor(1)...\n";
    std::unique_ptr<Foo> up1; // up1 is empty
    std::unique_ptr<Foo> up1b(nullptr); // up1b is empty

    std::cout << "Example constructor(2)...\n";
    {
        std::unique_ptr<Foo> up2(new Foo); //up2 now owns a Foo
    } // Foo deleted

    std::cout << "Example constructor(3)...\n";
    D d;
    {   // deleter type is not a reference
        std::unique_ptr<Foo, D> up3(new Foo, d); // deleter copied
    }
    {   // deleter type is a reference
        std::unique_ptr<Foo, D&> up3b(new Foo, d); // up3b holds a reference to d
    }

    std::cout << "Example constructor(4)...\n";
    {   // deleter is not a reference
        std::unique_ptr<Foo, D> up4(new Foo, D()); // deleter moved
    }

    std::cout << "Example constructor(5)...\n";
    {
        std::unique_ptr<Foo> up5a(new Foo);
        std::unique_ptr<Foo> up5b(std::move(up5a)); // ownership transfer
    }

    std::cout << "Example constructor(6)...\n";
    {
        std::unique_ptr<Foo, D> up6a(new Foo, d); // D is copied
        std::unique_ptr<Foo, D> up6b(std::move(up6a)); // D is moved

        std::unique_ptr<Foo, D&> up6c(new Foo, d); // D is a reference
        std::unique_ptr<Foo, D> up6d(std::move(up6c)); // D is copied
    }

#if (__cplusplus < 201703L)
    std::cout << "Example constructor(7)...\n";
    {
        std::auto_ptr<Foo> up7a(new Foo);
        std::unique_ptr<Foo> up7b(std::move(up7a)); // ownership transfer
    }
#endif

    std::cout << "Example array constructor...\n";
    {
        std::unique_ptr<Foo[]> up(new Foo[3]);
    } // three Foo objects deleted
}
```


**Output:**
```
Example constructor(1)...
Example constructor(2)...
Foo ctor
~Foo dtor
Example constructor(3)...
Foo ctor
D copy ctor
D is deleting a Foo
~Foo dtor
Foo ctor
D is deleting a Foo
~Foo dtor
Example constructor(4)...
Foo ctor
D move ctor
D is deleting a Foo
~Foo dtor
Example constructor(5)...
Foo ctor
~Foo dtor
Example constructor(6)...
Foo ctor
D copy ctor
D move ctor
Foo ctor
D non-const copy ctor
D is deleting a Foo
~Foo dtor
D is deleting a Foo
~Foo dtor
Example constructor(7)...
Foo ctor
~Foo dtor
Example array constructor...
Foo ctor
Foo ctor
Foo ctor
~Foo dtor
~Foo dtor
~Foo dtor
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2801 | C++11 | The default constructor was not constrained. | Constrained. |
| lwg-2899 | C++11 | The move constructor was not constrained. | Constrained. |
| lwg-2905 | C++11 | Constraint on the constructor from a pointer and a deleter was wrong. | Corrected. |
| lwg-2944 | C++11 | Some preconditions were accidentally dropped by LWG 2905 | Restored. |

