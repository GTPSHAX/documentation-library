---
title: std::is_unsigned
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_unsigned
---

cpp/types/traits/is|1=is_unsigned
|description=
Checks whether `T` is an unsigned arithmetic type.
* If `std::is_arithmetic<T>::value` is `true`, provides the member constant `value` equal to `T(0) < T(-1)`.
* Otherwise, provides the member constant `value` equal to `false`.
|inherit_desc=`T` is an unsigned integral type

## Possible implementation

eq fun|1=
namespace detail
{
template<typename T,bool = std::is_arithmetic<T>::value>
struct is_unsigned : std::integral_constant<bool, T(0) < T(-1)> {};
template<typename T>
struct is_unsigned<T,false> : std::false_type {};
} // namespace detail
template<typename T>
struct is_unsigned : detail::is_unsigned<T>::type {};

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

class A {};
static_assert(std::is_unsigned_v<A> == false);

enum B : unsigned {};
static_assert(std::is_unsigned_v<B> == false);

enum class C : unsigned {};
static_assert(std::is_unsigned_v<C> == false);

struct S { unsigned p : 1; int q : 1; };
static_assert
(
    std::is_unsigned_v<decltype(S::p)> not_eq
    std::is_unsigned_v<decltype(S::q)>
);

static_assert
(
    std::is_unsigned_v<float> == false &&
    std::is_unsigned_v<signed int> == false &&
    std::is_unsigned_v<unsigned int> == true &&
    std::is_unsigned_v<bool> == true
);

int main() 
{
    // signedness of char is implementation-defined:
    std::cout << std::boolalpha << std::is_unsigned<char>::value << '\n';
}
```


**Output:**
```
false
```


## Defect reports


## See also


| cpp/types/dsc is_signed | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_signed | (see dedicated page) |
| cpp/types/dsc is_arithmetic | (see dedicated page) |
| cpp/types/dsc make_signed | (see dedicated page) |
| cpp/types/dsc make_unsigned | (see dedicated page) |

