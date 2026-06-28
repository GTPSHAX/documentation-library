---
title: std::auto_ptr::operator auto_ptr<Y>
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/auto_ptr/operator_auto_ptr
---


```cpp
dcl|deprecated=c++11|removed=c++17|num=1|
template< class Y >
operator auto_ptr_ref<Y>() throw();
dcl|deprecated=c++11|removed=c++17|num=2|
template< class Y >
operator auto_ptr<Y>() throw();
```

Converts `*this` to an `auto_ptr` for a different type `Y`.
1. Returns an implementation-defined type that holds a reference to `*this`. `std::auto_ptr` is convertible and assignable from this template. The implementation is allowed to provide the template with a different name or implement equivalent functionality in other ways.
2. Constructs a new `auto_ptr` with a pointer obtained by calling `release()`.

## Parameters

(none)

## Return value

1. An implementation-defined type that holds a reference to `*this`.
2. An `auto_ptr` with a pointer obtained by calling `release()`.

## Notes

