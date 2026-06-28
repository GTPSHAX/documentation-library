---
title: std::monostate
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/monostate
---


```cpp
**Header:** `<`variant`>`
**Header:** `<`utility|notes=
dcl|since=c++17|
struct monostate { };
```

Unit type intended for use as a well-behaved empty alternative in `std::variant`. In particular, a variant of non-default-constructible types may list `std::monostate` as its first alternative: this makes the variant itself default-constructible.

## Member functions


## Non-member functions

member|1=operator==, !=, <, <=, >, >=, <=>|2=

```cpp
dcl|since=c++17|num=1|1=
constexpr bool operator==( monostate, monostate ) noexcept { return true; }
dcl rev multi|num=2|since1=c++17|until1=c++20|dcl1=
constexpr bool operator!=( monostate, monostate ) noexcept { return false; }
constexpr bool operator< ( monostate, monostate ) noexcept { return false; }
constexpr bool operator> ( monostate, monostate ) noexcept { return false; }
constexpr bool operator<=( monostate, monostate ) noexcept { return true; }
constexpr bool operator>=( monostate, monostate ) noexcept { return true; }
|dcl2=
constexpr std::strong_ordering operator<=>( monostate, monostate ) noexcept
{
return std::strong_ordering::equal;
}
```

All instances of `std::monostate` compare equal.
rrev|since=c++20|

## Helper classes

member|hash|2=
ddcl|since=c++17|
template <>
struct std::hash<monostate>;
Specializes the `std::hash` algorithm for `std::monostate`.

## Example


### Example

```cpp
#include <cassert>
#include <iostream>
#include <variant>

struct S
{
    S(int i) : i(i) {}
    int i;
};

int main()
{
    // Without the monostate type this declaration will fail.
    // This is because S is not default-constructible.
    std::variant<std::monostate, S> var;
    assert(var.index() == 0);

    try
    {
        std::get<S>(var); // throws! We need to assign a value
    }
    catch(const std::bad_variant_access& e)
    {
        std::cout << e.what() << '\n';
    }

    var = 42;
    std::cout << "std::get: " << std::get<S>(var).i << '\n'
              << "std::hash: " << std::hex << std::showbase
              << std::hash<std::monostate>{}(std::monostate{}) << '\n';
}
```


**Output:**
```
std::get: wrong index for variant
std::get: 42
std::hash: 0xffffffffffffe19f
```


## See also


| cpp/utility/variant/dsc constructor | (see dedicated page) |

