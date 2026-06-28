---
title: std::allocator::address
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator/address
---


```cpp
dcl rev multi|num=1|until1=c++11|dcl1=
pointer address( reference x ) const;
|notes2=|dcl2=
pointer address( reference x ) const noexcept;
dcl rev multi|num=2|until1=c++11|dcl1=
const_pointer address( const_reference x ) const;
|notes2=|dcl2=
const_pointer address( const_reference x ) const noexcept;
```

Returns the actual address of `x` even in presence of overloaded `operator&`.

## Parameters


### Parameters

- `x` - the object to acquire address of

## Return value

The actual address of `x`.

## Defect reports

