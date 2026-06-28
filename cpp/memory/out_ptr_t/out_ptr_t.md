---
title: std::out_ptr_t::out_ptr_t
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/out_ptr_t/out_ptr_t
---


```cpp
dcla|num=1|since=c++23|constexpr=c++26|
explicit out_ptr_t( Smart& sp, Args... args );
dcl|num=2|since=c++23|1=
out_ptr_t( const out_ptr_t& ) = delete;
```

1. Creates an `out_ptr_t`.
* Adapts `sp` as if binds it to the `Smart&` member, captures every argument `t` in `args` as if initializes the corresponding member of type `T` in `Args` with `std::forward<T>(t)`, then value-initializes the stored `Pointer`.
* Then evaluates `sp.reset()` if the expression is well-formed; otherwise, evaluates `1=sp = Smart()` if `std::is_default_constructible_v<Smart>` is `true`. .
2. Copy constructor is explicitly deleted. `out_ptr_t` is neither copyable nor movable.

## Parameters


### Parameters

- `sp` - the object (typically a smart pointer) to adapt
- `args` - the arguments used for resetting to capture

## Notes

After construction, the `Pointer` or `void*` object pointed by the return value of either conversion function is equal to `nullptr`.
Every argument in `args` is moved into the created `out_ptr_t` if it is of an object type, or transferred into the created `out_ptr_t` as-is if it is of a reference type.
The constructor of `out_ptr_t` is allowed to throw exceptions. For example, when `sp` is a `std::shared_ptr`, the allocation for the new control block may be performed within the constructor rather than the destructor.

## Example

