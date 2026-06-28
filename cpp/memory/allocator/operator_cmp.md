---
title: operators (std::allocator)
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator/operator_cmp
---


# 1=operator==,!=petty|(std::allocator)


```cpp
dcl rev multi|num=1
|until1=c++11|dcl1=
template< class T1, class T2 >
bool operator==( const allocator<T1>& lhs, const allocator<T2>& rhs ) throw();
|until2=c++20|dcl2=
template< class T1, class T2 >
bool operator==( const allocator<T1>& lhs, const allocator<T2>& rhs ) noexcept;
|dcl3=
template< class T1, class T2 >
constexpr bool
operator==( const allocator<T1>& lhs, const allocator<T2>& rhs ) noexcept;
dcl rev multi|num=2
|until1=c++11|dcl1=
template< class T1, class T2 >
bool operator!=( const allocator<T1>& lhs, const allocator<T2>& rhs ) throw();
|until2=c++20|dcl2=
template< class T1, class T2 >
bool operator!=( const allocator<T1>& lhs, const allocator<T2>& rhs ) noexcept;
```

Compares two default allocators. Since default allocators are stateless, two default allocators are always equal.
1. Returns `true`.
2. Returns `false`.
rrev|since=c++20|

## Parameters


### Parameters

- `lhs, rhs` - default allocators to compare

## Return value

1. `true`
2. `false`
