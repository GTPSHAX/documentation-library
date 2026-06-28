---
title: std::generator::promise_type::operator new
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/generator/promise_type/operator_new
---


# small|generator<Ref,V,Allocator>::promise_type::

operator new

```cpp
dcl|num=1|since=c++23|
void* operator new( std::size_t size )
requires std::same_as<Allocator, void>
std::default_initializable<Allocator>;
dcla|num=2|since=c++23|
template< class Alloc, class... Args >
void* operator new( std::size_t size, std::allocator_arg_t,
const Alloc& alloc, const Args&... );
dcl|num=3|since=c++23|
template< class This, class Alloc, class... Args >
void* operator new( std::size_t size, const This&, std::allocator_arg_t,
const Alloc& alloc, const Args&... );
```

Allocates `size` bytes of uninitialized storage using default or user-provided allocator.
Let `A` be
* `Allocator`, if it is not `void`,
* `Alloc` for , or
* `std::allocator<void>` otherwise.
Let `B` be `std::allocator_traits<A>::template rebind_alloc<U>` where `U` is an unspecified type whose size and alignment are both `cpp/preprocessor/replace#Predefined macros|__STDCPP_DEFAULT_NEW_ALIGNMENT__`.
Initializes an allocator `b` of type `B` with:
1. `A()`,
@2,3@ `A(alloc)`.
Uses `b` to allocate storage for the smallest array of `U` sufficient to provide storage for a coroutine state of size `size`, and unspecified additional state necessary to ensure that `operator delete` can later deallocate this memory block with an allocator equal to `b`.
The program is ill-formed unless `std::allocator_traits<B>::pointer` is a pointer type and for overloads , `std::same_as<Allocator, void>  is modeled.

## Parameters


### Parameters

- `size` - the size of the storage to allocate
- `alloc` - a user provided allocator of type `Alloc`

## Return value

A pointer to the allocated storage.

## Exceptions

@1-3@ May throw.

## Defect reports

