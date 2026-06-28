---
title: decay-copy
type: Standard
source: https://en.cppreference.com/w/cpp/standard_library/decay-copy
---


# ''decay-copy''


```cpp
dcl rev multi|since1=c++11|notes1=|dcl1=
template< class T >
typename std::decay<T>::type /*decay-copy*/( T&& value );
|since2=c++20|notes2=|dcl2=
template< class T >
requires std::convertible_to<T, std::decay_t<T>>
constexpr std::decay_t<T> /*decay-copy*/( T&& value )
noexcept(std::is_nothrow_convertible_v<T, std::decay_t<T>>);
```

Returns `std::forward<T>(value)` (implicitly converted to the decayed type), a decayed prvalue copy of `value`.

## Parameters


### Parameters

- `value` - the value to be copied

## Return value

A decayed copy of `value` as a prvalue.

## Notes

was introduced by the resolution of . It is initially used in the concurrency support library to ensure that arguments are decayed when passing-by-value, and is later used in the ranges library.
The language feature `cpp/language/explicit cast|auto``(x)` introduced in C++23 also allows decayed copies to be created as prvalues. The only difference is that  always materializes `value` and produces a copy, while `auto(expr)` is a no-op if `expr` is a prvalue.
All usages of  in the standard library (see below) except `cpp/ranges/all_view|views::all`,  and  are replaced with `auto(x)` since C++23.

## Defect reports


## See also


| cpp/thread/thread/dsc constructor | (see dedicated page) |
| cpp/thread/jthread/dsc constructor | (see dedicated page) |
| cpp/thread/dsc async | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |
| cpp/ranges/dsc rbegin | (see dedicated page) |
| cpp/ranges/dsc rend | (see dedicated page) |
| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc data | (see dedicated page) |
| cpp/ranges/dsc all_view | (see dedicated page) |
| cpp/ranges/dsc take_view | (see dedicated page) |
| cpp/ranges/dsc drop_view | (see dedicated page) |

