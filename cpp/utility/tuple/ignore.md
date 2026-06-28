---
title: std::ignore
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple/ignore
---


```cpp
**Header:** `<`tuple`>`
**Header:** `<`utility`>`
dcl rev multi|num=1
|since1=c++11|dcl1=
const /*ignore-type*/ ignore;
|since2=c++14|notes2=|dcl2=
constexpr /*ignore-type*/ ignore;
dcl rev multi|num=2
|since1=c++11|notes1=|dcl1=
struct /*ignore-type*/
{
template< class T >
const /*ignore-type*/& operator=( const T& ) const noexcept
{
return *this;
}
};
|since2=c++14|notes2=|dcl2=
struct /*ignore-type*/
{
template< class T >
constexpr const /*ignore-type*/& operator=( const T& ) const noexcept
{
return *this;
}
};
```

1. An object such that any value can be assigned to it with no effect.
2. The type of `std::ignore`.

## Notes

A `void` expression or a volatile bit-field value cannot be assigned to `std::ignore`.
`std::ignore` is intended for use with `std::tie` when unpacking a `std::tuple`, as a placeholder for the arguments that are not used, but can be used for any unwanted assignment.
Some code guides recommend using `std::ignore` to avoid warnings from unused return values of  functions, even though an assignment isn't required.
For ignoring values not requiring assignment, one may cast to `void`. For variables that have names, but whose value is unused, one may cast those to `void` or declare those variables with .

## Example

# Demonstrates the use of `std::ignore` together with a  function.
# Unpacks a `std::pair<iterator, bool>` returned by , but only saves the boolean.

### Example

```cpp
#include <iostream>
#include <set>
#include <string>
#include <tuple>

[[nodiscard]] int dontIgnoreMe()
{
    return 42;
}

int main()
{
    std::ignore = dontIgnoreMe();

    std::set<std::string> set_of_str;
    if (bool inserted{false};
        std::tie(std::ignore, inserted) = set_of_str.insert("Test"),
        inserted)
        std::cout << "Value was inserted successfully.\n";
}
```


**Output:**
```
Value was inserted successfully.
```


## Defect reports


## See also


| cpp/utility/tuple/dsc tie | (see dedicated page) |

