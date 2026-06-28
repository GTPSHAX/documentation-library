---
title: std::tuple::swap
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple/swap
---


```cpp
**Header:** `<`tuple`>`
|
void swap( tuple& other ) noexcept(/* see below */);
dcl|num=2|since=c++23|
constexpr void swap( const tuple& other ) noexcept(/* see below */) const;
```

Calls `swap` (which might be `std::swap`, or might be found via ADL) for each element in `*this` and its corresponding element in `other`.
rrev multi
|rev1=
If any selected `swap` function call is ill-formed, or does not swap the corresponding elements of both tuples, the behavior is undefined.
|since2=c++23|rev2=
If any selected `swap` function call does not swap the corresponding elements of both tuples, the behavior is undefined.
1. The program is ill-formed if `(std::is_swappable_v<Types> && ...)` is not `true`.
2. The program is ill-formed if `(std::is_swappable_v<const Types> && ...)` is not `true`.

## Parameters


### Parameters

- `other` - tuple of values to swap

## Return value

(none)

## Exceptions

rrev multi|until1=c++17
|rev1=
noexcept|
noexcept(swap(std::declval<T0&>>(), std::declval<T0&>())) &&
noexcept(swap(std::declval<T1&>>(), std::declval<T1&>())) &&
noexcept(swap(std::declval<T2&>>(), std::declval<T2&>())) &&
...
In the expression above, the identifier `swap` is looked up in the same manner as the one used by the C++17 `std::is_nothrow_swappable` trait.
|rev2=
1.
2.

## Example


## See also


| cpp/utility/tuple/dsc swap2 | (see dedicated page) |
| cpp/utility/pair/dsc swap | (see dedicated page) |

