---
title: std::is_arithmetic
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_arithmetic
---

cpp/types/traits/is| 1=is_arithmetic
|std=c++11
|description=If `T` is an arithmetic type (that is, an integral type or a floating-point type) or a `cv-qualified` version thereof, provides the member constant `value` equal to `true`. For any other type, `value` is `false`.
|inherit_desc= `T` is an arithmetic type

## Notes

Arithmetic types are the built-in types for which the arithmetic operators (`+`, `-`, `*`, `/`) are defined (possibly in combination with the usual arithmetic conversions).
Specializations of `std::numeric_limits` are provided for all arithmetic types.

## Possible implementation

eq fun
|1=
template<class T>
struct is_arithmetic : std::integral_constant<bool,
std::is_integral<T>::value
std::is_floating_point<T>::value> {};

## Example


### Example

```cpp
#include <atomic>
#include <cstddef>
#include <type_traits>

class A {};

enum class B : int { e };

static_assert(
    std::is_arithmetic_v<bool>            == true  and
    std::is_arithmetic_v<char>            == true  and
    std::is_arithmetic_v<char const>      == true  and
    std::is_arithmetic_v<int>             == true  and
    std::is_arithmetic_v<int const>       == true  and
    std::is_arithmetic_v<float>           == true  and
    std::is_arithmetic_v<float const>     == true  and
    std::is_arithmetic_v<std::size_t>     == true  and

    std::is_arithmetic_v<char&>           == false and
    std::is_arithmetic_v<char*>           == false and
    std::is_arithmetic_v<int&>            == false and
    std::is_arithmetic_v<int*>            == false and
    std::is_arithmetic_v<float&>          == false and
    std::is_arithmetic_v<float*>          == false and
    std::is_arithmetic_v<A>               == false and
    std::is_arithmetic_v<B>               == false and
    std::is_arithmetic_v<decltype(B::e)>  == false and
    std::is_arithmetic_v<std::byte>       == false and
    std::is_arithmetic_v<std::atomic_int> == false
);

int main() {}
```


## See also


| cpp/types/dsc is_integral | (see dedicated page) |
| cpp/types/dsc is_floating_point | (see dedicated page) |

