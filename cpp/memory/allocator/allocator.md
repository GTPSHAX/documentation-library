---
title: std::allocator::allocator
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator/allocator
---


```cpp
dcl rev multi| num=1 | until1=c++11|until2=c++20|dcl1=
allocator() throw();
|dcl2=
allocator() noexcept;
|dcl3=
constexpr allocator() noexcept;
dcl rev multi| num=2 | until1=c++11|until2=c++20|dcl1=
allocator( const allocator& other ) throw();
|dcl2=
allocator( const allocator& other ) noexcept;
|dcl3=
constexpr allocator( const allocator& other ) noexcept;
dcl rev multi| num=3 | until1=c++11|until2=c++20|dcl1=
template< class U >
allocator( const allocator<U>& other ) throw();
|dcl2=
template< class U >
allocator( const allocator<U>& other ) noexcept;
|dcl3=
template< class U >
constexpr allocator( const allocator<U>& other ) noexcept;
```

Constructs the default allocator. Since the default allocator is stateless, the constructors have no visible effect.

## Parameters


### Parameters

