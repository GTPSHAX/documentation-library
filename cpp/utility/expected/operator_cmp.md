---
title: operator==(std::expected)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/operator_cmp
---


# 1=operator==petty|(std::expected)


```cpp
dcl|num=1|since=c++23|1=
template< class T2, class E2 >
requires (!std::is_void_v<T2>)
friend constexpr bool operator==( const expected& lhs,
const std::expected<T2, E2>& rhs );
dcl|num=2|since=c++23|1=
template< class E2 >
friend constexpr bool operator==( const expected& lhs,
const std::unexpected<E2>& unex );
dcl|num=3|since=c++23|1=
template< class T2 >
friend constexpr bool operator==( const expected& lhs, const T2& val );
dcl|num=4|since=c++23|1=
template< class T2, class E2 >
requires std::is_void_v<T2>
friend constexpr bool operator==( const expected& lhs,
const std::expected<T2, E2>& rhs );
dcl|num=5|since=c++23|1=
template< class E2 >
friend constexpr bool operator==( const expected& lhs,
const std::unexpected<E2>& unex );
```

Performs comparison operations on `std::expected` objects.
1. Compares two `std::expected` objects. The objects compare equal if and only if both `lhs` and `rhs` contain expected values that are equal, or both contain unexpected values that are equal.
rev|until=c++26|
If any of the following expressions is ill-formed, or its result is not convertible to `bool`, the program is ill-formed:
rev|since=c++26|
:
* `1=*lhs == *rhs`
* `1=lhs.error() == rhs.error()`
2. Compares `std::expected` object with an `std::unexpected` object. The objects compare equal if and only if `lhs` contains an unexpected value that is equal to `unex.error()`.
rev|until=c++26|
If the expression `1=lhs.error() == unex.error()` is ill-formed, or its result is not convertible to `bool`, the program is ill-formed.
rev|since=c++26|
.
3. Compares `std::expected` object with an expected value. The objects compare equal if and only if `lhs` contains an expected value that is equal to `val`.
rev|until=c++26|
If the expression `1=*lhs == val` is ill-formed, or its result is not convertible to `bool`, the program is ill-formed.
rev|since=c++26|
cpp/enable if|all following conditions are satisfied:
* `T2` is not a specialization of `std::expected`.
* The expression `1=*lhs == val` is well-formed, and its result is convertible to `bool`.
4. Compares two `std::expected` objects. The objects compare equal if and only if `lhs` and `rhs` both represent expected values, or both contain unexpected values that are equal.
rev|until=c++26|
If the expression `1=lhs.error() == rhs.error()` is ill-formed, or its result is not convertible to `bool`, the program is ill-formed.
rev|since=c++26|
.
5. Compares `std::expected` object with an `std::unexpected` object. The objects compare equal if and only if `lhs` contains an unexpected value that is equal to `unex.error()`.
rev|until=c++26|
If the expression `1=lhs.error() == unex.error()` is ill-formed, or its result is not convertible to `bool`, the program is ill-formed.
rev|since=c++26|
.

## Parameters


### Parameters

- `lhs, rhs` - `std::expected` object(s) to compare
- `unex` - `std::unexpected` value to compare to `lhs`
- `val` - value to compare to the expected value contained in `lhs`

## Return value

1.
2. `1=!lhs.has_value() && static_cast<bool>(lhs.error() == unex.error())`
3. `1=lhs.has_value() && static_cast<bool>(*lhs == val)`
4.
5. `1=!lhs.has_value() && static_cast<bool>(lhs.error() == unex.error())`

## Exceptions

Throws when and what the comparison throws.

## Notes


## Example


### Example

```cpp
#include <expected>
#include <iostream>
#include <string_view>

using namespace std::string_view_literals;

int main()
{
    auto x1{"\N{GREEN HEART}"sv};
    auto x2{"\N{CROSS MARK}"sv};
    std::expected<std::string_view, int> e1{x1}, e2{x1}, e3{x2};
    std::unexpected u1{13};

    std::cout << "Overload (1):\n"
              << e1.value() << (e1 == e2 ? " == " : " != ") << *e2 << '\n'
              << e1.value() << (e1 != e3 ? " != " : " == ") << *e3 << "\n\n";

    std::cout << "Overload (2):\n"
              << e1.value() << (e1 == u1 ? " == " : " != ") << u1.error() << '\n';
    e1 = std::unexpected{13};
    std::cout << e1.error() << (e1 == u1 ? " == " : " != ") << u1.error() << '\n';
    e1 = std::unexpected{31};
    std::cout << e1.error() << (e1 != u1 ? " != " : " == ") << u1.error() << '\n';

    std::cout << "Overload (3):\n"
              << *e1 << (e1 == x1 ? " == " : " != ") << x1 << '\n'
              << *e1 << (e1 != x2 ? " != " : " == ") << x2 << "\n\n";
}
```


**Output:**
```
Overload (1):
💚 == 💚
💚 != ❌

Overload (2):
💚 != 13
13 == 13
31 != 13

Overload (3):
💚 == 💚
💚 != ❌
```


## See also


| cpp/utility/expected/dsc unexpected | (see dedicated page) |

