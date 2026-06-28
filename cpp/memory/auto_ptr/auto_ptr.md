---
title: std::auto_ptr::auto_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/auto_ptr/auto_ptr
---


```cpp
dcl|deprecated=c++11|removed=c++17|num=1|1=
explicit auto_ptr( X* p = 0 ) throw();
dcl|deprecated=c++11|removed=c++17|num=2|
auto_ptr( auto_ptr& r ) throw();
dcl|deprecated=c++11|removed=c++17|num=3|
template< class Y >
auto_ptr( auto_ptr<Y>& r ) throw();
dcl|deprecated=c++11|removed=c++17|num=4|
auto_ptr( auto_ptr_ref<X> m ) throw();
```

Constructs the `auto_ptr` from a pointer that refers to the object to manage.
1. Constructs the `auto_ptr` with pointer `p`.
2. Constructs the `auto_ptr` with the pointer held in `r`. `r.release()` is called to acquire the ownership of the object.
3. Same as (2). `Y*` must be implicitly convertible to `T*`.
4. Constructs the `auto_ptr` with the pointer held in the `auto_ptr` instance referred to by `m`. `p.release()` is called for the `auto_ptr p` that `m` holds to acquire the ownership of the object.
@@ `auto_ptr_ref` is an implementation-defined type that holds a reference to `auto_ptr`. `std::auto_ptr` is implicitly convertible to and assignable from this type. The implementation is allowed to provide the template with a different name or implement equivalent functionality in other ways.

## Parameters


### Parameters

- `p` - a pointer to an object to manage
- `r` - another `auto_ptr` to transfer the ownership of the object from
- `m` - an implementation-defined type that holds a reference to `auto_ptr`

## Notes

