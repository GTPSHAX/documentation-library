---
title: std::is_invocable
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_invocable
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++17|num=1|1=
template< class Fn, class... ArgTypes >
struct is_invocable;
dcl|since=c++17|num=2|1=
template< class R, class Fn, class... ArgTypes >
struct is_invocable_r;
dcl|since=c++17|num=3|1=
template< class Fn, class... ArgTypes >
struct is_nothrow_invocable;
dcl|since=c++17|num=4|1=
template< class R, class Fn, class... ArgTypes >
struct is_nothrow_invocable_r;
```

1. Determines whether  is well formed when treated as an unevaluated operand.
2. Determines whether  is well formed when treated as an unevaluated operand.
3. Determines whether  is well formed when treated as an unevaluated operand, and is known not to throw any exceptions.
4. Determines whether  is well formed when treated as an unevaluated operand, and is known not to throw any exceptions.

## Helper variable templates


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++17|num=1|1=
template< class Fn, class... ArgTypes >
inline constexpr bool is_invocable_v =
std::is_invocable<Fn, ArgTypes...>::value;
dcl|since=c++17|num=2|1=
template< class R, class Fn, class... ArgTypes >
inline constexpr bool is_invocable_r_v =
std::is_invocable_r<R, Fn, ArgTypes...>::value;
dcl|since=c++17|num=3|1=
template< class Fn, class... ArgTypes >
inline constexpr bool is_nothrow_invocable_v =
std::is_nothrow_invocable<Fn, ArgTypes...>::value;
dcl|since=c++17|num=4|1=
template< class R, class Fn, class... ArgTypes >
inline constexpr bool is_nothrow_invocable_r_v =
std::is_nothrow_invocable_r<R, Fn, ArgTypes...>::value;
```


## Notes


## Examples


### Example

```cpp
#include <type_traits>

auto func2(char) -> int (*)()
{
    return nullptr;
}

int main()
{
    static_assert(std::is_invocable_v<int()>);
    static_assert(not std::is_invocable_v<int(), int>);
    static_assert(std::is_invocable_r_v<int, int()>);
    static_assert(not std::is_invocable_r_v<int*, int()>);
    static_assert(std::is_invocable_r_v<void, void(int), int>);
    static_assert(not std::is_invocable_r_v<void, void(int), void>);
    static_assert(std::is_invocable_r_v<int(*)(), decltype(func2), char>);
    static_assert(not std::is_invocable_r_v<int(*)(), decltype(func2), void>);
}
```


## See also


| cpp/utility/functional/dsc invoke | (see dedicated page) |
| cpp/types/dsc result_of | (see dedicated page) |
| cpp/utility/dsc declval | (see dedicated page) |
| cpp/concepts/dsc invocable | (see dedicated page) |

