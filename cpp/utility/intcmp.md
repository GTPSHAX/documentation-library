---
title: std::cmp_equal
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/intcmp
---


```cpp
**Header:** `<`utility`>`
dcl|num=1|since=c++20|1=
template< class T, class U >
constexpr bool cmp_equal( T t, U u ) noexcept;
dcl|num=2|since=c++20|1=
template< class T, class U >
constexpr bool cmp_not_equal( T t, U u ) noexcept;
dcl|num=3|since=c++20|1=
template< class T, class U >
constexpr bool cmp_less( T t, U u ) noexcept;
dcl|num=4|since=c++20|1=
template< class T, class U >
constexpr bool cmp_greater( T t, U u ) noexcept;
dcl|num=5|since=c++20|1=
template< class T, class U >
constexpr bool cmp_less_equal( T t, U u ) noexcept;
dcl|num=6|since=c++20|1=
template< class T, class U >
constexpr bool cmp_greater_equal( T t, U u ) noexcept;
```

Compare the values of two integers `t` and `u`. Unlike builtin comparison operators, negative signed integers always compare ''less than'' (and ''not equal to'') unsigned integers: the comparison is safe against non-value-preserving integer conversion.

```cpp
-1 > 0u; // true
std::cmp_greater(-1, 0u); // false
```

It is a compile-time error if either `T` or `U` is a non-integer type, a character type, or `bool`.

## Parameters


### Parameters

- `t` - left-hand argument
- `u` - right-hand argument

## Return value

1. `true` if `t` is equal to `u`.
2. `true` if `t` is not equal to `u`.
3. `true` if `t` is less than `u`.
4. `true` if `t` is greater than `u`.
5. `true` if `t` is less or equal to `u`.
6. `true` if `t` is greater or equal to `u`.

## Possible implementation

eq fun
|1=
template<class T, class U>
constexpr bool cmp_equal(T t, U u) noexcept
{
if constexpr (std::is_signed_v<T> == std::is_signed_v<U>)
return t == u;
else if constexpr (std::is_signed_v<T>)
return t >= 0 && std::make_unsigned_t<T>(t) == u;
else
return u >= 0 && std::make_unsigned_t<U>(u) == t;
}
template<class T, class U>
constexpr bool cmp_not_equal(T t, U u) noexcept
{
return !cmp_equal(t, u);
}
template<class T, class U>
constexpr bool cmp_less(T t, U u) noexcept
{
if constexpr (std::is_signed_v<T> == std::is_signed_v<U>)
return t < u;
else if constexpr (std::is_signed_v<T>)
return t < 0  std::make_unsigned_t<T>(t) < u;
else
return u >= 0 && t < std::make_unsigned_t<U>(u);
}
template<class T, class U>
constexpr bool cmp_greater(T t, U u) noexcept
{
return cmp_less(u, t);
}
template<class T, class U>
constexpr bool cmp_less_equal(T t, U u) noexcept
{
return !cmp_less(u, t);
}
template<class T, class U>
constexpr bool cmp_greater_equal(T t, U u) noexcept
{
return !cmp_less(t, u);
}

## Notes

These functions cannot be used to compare s (including ), `char`, `char8_t`, `char16_t`, `char32_t`, `wchar_t` and `bool`.

## Example


### Example

```cpp
#include <utility>

// Uncommenting the next line will disable "signed/unsigned comparison" warnings:
// #pragma GCC diagnostic ignored "-Wsign-compare"

int main()
{
    static_assert(sizeof(int) == 4); // precondition

    // Quite surprisingly
    static_assert(-1 > 1U); //< warning: sign-unsign comparison
    // because after implicit conversion of -1 to the RHS type (`unsigned int`)
    // the expression is equivalent to:
    static_assert(0xFFFFFFFFU > 1U);
    static_assert(0xFFFFFFFFU == static_cast<unsigned>(-1));

    // In contrast, the cmp_* family compares integers as most expected -
    // negative signed integers always compare less than unsigned integers:
    static_assert(std::cmp_less(-1, 1U));
    static_assert(std::cmp_less_equal(-1, 1U));
    static_assert(!std::cmp_greater(-1, 1U));
    static_assert(!std::cmp_greater_equal(-1, 1U));

    static_assert(-1 == 0xFFFFFFFFU); //< warning: sign-unsign comparison
    static_assert(std::cmp_not_equal(-1, 0xFFFFFFFFU));
}
```


## See also


| cpp/utility/functional/dsc equal_to | (see dedicated page) |
| cpp/utility/functional/dsc not_equal_to | (see dedicated page) |
| cpp/utility/functional/dsc less | (see dedicated page) |
| cpp/utility/functional/dsc greater | (see dedicated page) |
| cpp/utility/functional/dsc less_equal | (see dedicated page) |
| cpp/utility/functional/dsc greater_equal | (see dedicated page) |
| cpp/utility/functional/ranges/dsc equal_to | (see dedicated page) |
| cpp/utility/functional/ranges/dsc not_equal_to | (see dedicated page) |
| cpp/utility/functional/ranges/dsc less | (see dedicated page) |
| cpp/utility/functional/ranges/dsc greater | (see dedicated page) |
| cpp/utility/functional/ranges/dsc less_equal | (see dedicated page) |
| cpp/utility/functional/ranges/dsc greater_equal | (see dedicated page) |
| cpp/utility/compare/dsc compare_three_way | (see dedicated page) |
| cpp/utility/dsc in_range | (see dedicated page) |
| cpp/types/dsc numeric_limits | (see dedicated page) |

