---
title: operators (std::coroutine_handle)
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/coroutine_handle/operator_cmp
---


# 1=operator==, operator<=><small>(std::coroutine_handle)</small>


```cpp
**Header:** `<`coroutine`>`
dcl|num=1|since=c++20|1=
constexpr bool
operator==( std::coroutine_handle<> x, std::coroutine_handle<> y ) noexcept;
dcl|num=2|since=c++20|1=
constexpr std::strong_ordering
operator<=>( std::coroutine_handle<> x, std::coroutine_handle<> y ) noexcept;
```

Compares two `std::coroutine_handle<>` values `x` and `y` according to their underlying addresses.

## Parameters


### Parameters

- `x, y` - `std::coroutine_handle<>` values to compare

## Return value

1. `1=x.address() == y.address()`
2. }

## Notes

Although these operators are only overloaded for `std::coroutine_handle<>`, other specializations of `std::coroutine_handle` are also equality comparable and three-way comparable, because they are implicitly convertible to `std::coroutine_handle<>`.

## Example

