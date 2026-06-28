---
title: std::type_index::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/types/type_index/operator_cmp
---


```cpp
dcl|num=1|since=c++11|1=
bool operator==( const type_index& rhs ) const noexcept;
dcl|num=2|since=c++11|until=c++20|1=
bool operator!=( const type_index& rhs ) const noexcept;
dcl|num=3|since=c++11|1=
bool operator<( const type_index& rhs ) const noexcept;
dcl|num=4|since=c++11|1=
bool operator<=( const type_index& rhs ) const noexcept;
dcl|num=5|since=c++11|1=
bool operator>( const type_index& rhs ) const noexcept;
dcl|num=6|since=c++11|1=
bool operator>=( const type_index& rhs ) const noexcept;
dcl|num=7|since=c++20|1=
std::strong_ordering operator<=>( const type_index& rhs ) const noexcept;
```

Compares the underlying `std::type_info` objects.
@1,2@ Checks whether the underlying `std::type_info` objects refer to the same type.
@3-7@ Compares the underlying `std::type_info` objects as defined by an implementation-defined ordering. The comparison is done by .
rrev|since=c++20|

## Parameters


### Parameters

- `rhs` - another `type_index` object to compare to

## Return value

1. `true` if the underlying `std::type_info` objects refer to the same type, `false` otherwise.
2. `true` if the underlying `std::type_info` objects refer not to the same type, `false` otherwise.
@3-6@ `true` if the types referred by the underlying `std::type_info` objects are ordered by corresponding order, `false` otherwise.
7. `std::strong_ordering::equal` if the underlying `std::type_info` objects refer to the same type, otherwise `std::strong_ordering::less` if `*this`'s underlying `std::type_info` object precedes `rhs`'s in the implementation-defined ordering, otherwise `std::strong_ordering::greater`.
