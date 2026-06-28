---
title: std::auto_ptr::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/auto_ptr/operator=
---


```cpp
dcl|deprecated=c++11|removed=c++17|num=1|1=
auto_ptr& operator=( auto_ptr& r ) throw();
dcl|deprecated=c++11|removed=c++17|num=2|1=
template< class Y >
auto_ptr& operator=( auto_ptr<Y>& r ) throw();
dcl|deprecated=c++11|removed=c++17|num=3|1=
auto_ptr& operator=( auto_ptr_ref<T> m ) throw();
```

Replaces the managed object with the one managed by `r` or `m`.
1. Effectively calls `reset(r.release())`.
2. Effectively calls `reset(r.release())`. `Y*` must be implicitly convertible to `T*`.
3. Effectively calls `reset(m.release())`. `auto_ptr_ref` is an implementation-defined type that holds a reference to `auto_ptr`. `std::auto_ptr` is implicitly convertible to and from this type. The implementation is allowed to provide the template with a different name or implement equivalent functionality in other ways.

## Parameters


### Parameters

- `r` - another `auto_ptr` to transfer the ownership of the object from
- `m` - an object of implementation-defined type that holds a reference to `auto_ptr`

## Return value

`*this`.

## Notes


## Defect reports

