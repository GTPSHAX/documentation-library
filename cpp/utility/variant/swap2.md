---
title: std::swap(std::variant)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/swap2
---


# swapsmall|(std::variant)


```cpp
**Header:** `<`variant`>`
dcla|anchor=no|since=c++17|constexpr=c++20|
template< class... Types >
void swap( std::variant<Types...>& lhs,
std::variant<Types...>& rhs ) noexcept(/* see below */);
```

Overloads the `std::swap` algorithm for `std::variant`. Effectively calls `lhs.swap(rhs)`.
.

## Parameters


### Parameters

- `lhs, rhs` - `variant` objects whose values to swap

## Return value

(none)

## Exceptions


## Notes


## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <variant>

void print(auto const& v, char term = '\n')
{
    std::visit([](auto&& o) { std::cout << o; }, v);
    std::cout << term;
}

int main()
{
    std::variant<int, std::string> v1{123}, v2{"XYZ"};
    print(v1, ' ');
    print(v2);

    std::swap(v1, v2);
    print(v1, ' ');
    print(v2);

    std::variant<double, std::string> v3{3.14};
    // std::swap(v1, v3); // ERROR: ~ inconsistent parameter packs
}
```


**Output:**
```
123 XYZ
XYZ 123
```


## Defect reports


## See also


| cpp/utility/variant/dsc swap | (see dedicated page) |

