---
title: std::is_integral
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_integral
---

cpp/types/traits/is|1=is_integral
|description=
Checks whether `T` is an integral type. Provides the member constant `value` which is equal to `true`, if `T` is the type `bool`, `char`<sup>(since C++20)</sup> , `char8_t`, `char16_t`, `char32_t`, `wchar_t`, `short`, `int`, `long`, `long long`, or any implementation-defined extended integer types, including any signed, unsigned, and cv-qualified variants. Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is an integral type

## Possible implementation

eq fun|1=
// Note: this implementation uses C++20 facilities
template<class T>
struct is_integral : std::bool_constant<
requires (T t, T* p, void (*f)(T)) // T* parameter excludes reference types
{
reinterpret_cast<T>(t); // Exclude class types
f(0); // Exclude enumeration types
p + t; // Exclude everything not yet excluded but integral types
}> {};

## Example


### Example

```cpp
#include <type_traits>

static_assert
(
    std::is_integral_v<float> == false &&
    std::is_integral_v<int*> == false &&
    std::is_integral_v<int> == true &&
    std::is_integral_v<const int> == true &&
    std::is_integral_v<bool> == true &&
    std::is_integral_v<char> == true
);

class A {};
static_assert(std::is_integral_v<A> == false);

struct B { int x:4; };
static_assert(std::is_integral_v<B> == false);
using BF = decltype(B::x); // bit-field's type
static_assert(std::is_integral_v<BF> == true);

enum E : int {};
static_assert(std::is_integral_v<E> == false);

template <class T>
constexpr T same(T i)
{
    static_assert(std::is_integral<T>::value, "Integral required.");
    return i;
}
static_assert(same('"') == 042);

int main() {}
```


## See also


| cpp/concepts/dsc integral | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_integer | (see dedicated page) |
| cpp/types/dsc is_floating_point | (see dedicated page) |
| cpp/types/dsc is_arithmetic | (see dedicated page) |
| cpp/types/dsc is_enum | (see dedicated page) |

