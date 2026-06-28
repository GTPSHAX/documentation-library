---
title: std::make_signed
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/make_signed
---

ddcl|header=type_traits|since=c++11|1=
template< class T >
struct make_signed;
If `T` is an integral (except `bool`) or enumeration type, provides the member typedef `type` which is the signed integer type corresponding to `T`, with the same cv-qualifiers.
If `T` is signed or unsigned `char`, `short`, `int`, `long`, `long long`, the signed type from this list corresponding to `T` is provided.
If `T` is an enumeration type or `char`, `wchar_t`<sup>(since C++20)</sup> , `char8_t`, `char16_t`, `char32_t`, the signed integer type with the smallest rank having the same `sizeof` as `T` is provided.
rrev multi|until1=c++20
|rev1=Otherwise, the behavior is undefined.
|rev2=Otherwise, the program is ill-formed.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types


```cpp
dcl|since=c++14|1=
template< class T >
using make_signed_t = typename make_signed<T>::type;
```


## Example


### Example

```cpp
#include <type_traits>

enum struct E : unsigned short {};

int main()
{
    using char_type = std::make_signed_t<unsigned char>;
    using int_type  = std::make_signed_t<unsigned int>;
    using long_type = std::make_signed_t<volatile unsigned long>;
    using enum_type = std::make_signed_t<E>;

    static_assert(
        std::is_same_v<char_type, signed char> and
        std::is_same_v<int_type, signed int> and
        std::is_same_v<long_type, volatile signed long> and
        std::is_same_v<enum_type, signed short>
    );
}
```


## See also


| cpp/types/dsc is_signed | (see dedicated page) |
| cpp/types/dsc is_unsigned | (see dedicated page) |
| cpp/types/dsc make_unsigned | (see dedicated page) |

