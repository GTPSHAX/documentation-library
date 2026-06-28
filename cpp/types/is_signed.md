---
title: std::is_signed
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_signed
---

cpp/types/traits/is|1=is_signed
|description=
Checks whether `T` is a signed arithmetic type.
* If `std::is_arithmetic<T>::value` is `true`, provides the member constant `value` equal to `T(-1) < T(0)`.
* Otherwise, provides the member constant `value` equal to `false`.
|inherit_desc=`T` is a signed arithmetic type

## Possible implementation

eq fun|1=
namespace detail
{
template<typename T, bool = std::is_arithmetic<T>::value>
struct is_signed : std::integral_constant<bool, T(-1) < T(0)> {};
template<typename T>
struct is_signed<T, false> : std::false_type {};
}
template<typename T>
struct is_signed : detail::is_signed<T>::type {};

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

class A {};
static_assert(std::is_signed_v<A> == false);

class B { int i; };
static_assert(std::is_signed_v<B> == false);

enum C : int {};
static_assert(std::is_signed_v<C> == false);

enum class D : int {};
static_assert(std::is_signed_v<D> == false);

static_assert
(
    std::is_signed<signed int>::value == true and // C++11
    std::is_signed<signed int>() == true and      // C++11
    std::is_signed<signed int>{} == true and      // C++11
    std::is_signed_v<signed int> == true and      // C++17
    std::is_signed_v<unsigned int> == false and
    std::is_signed_v<float> == true and
    std::is_signed_v<bool> == false and
    std::is_signed_v<signed char> == true and
    std::is_signed_v<unsigned char> == false
);

int main()
{
    // signedness of char is implementation-defined:
    std::cout << std::boolalpha << std::is_signed_v<char> << '\n';
}
```


**Output:**
```
true
```


## Defect reports


## See also


| cpp/types/dsc is_unsigned | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_signed | (see dedicated page) |
| cpp/types/dsc is_arithmetic | (see dedicated page) |
| cpp/types/dsc make_signed | (see dedicated page) |
| cpp/types/dsc make_unsigned | (see dedicated page) |

