---
title: std::make_unsigned
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/make_unsigned
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|1=
template< class T >
struct make_unsigned;
```

If `T` is an integral (except `bool`) or enumeration type, provides the member typedef `type` which is the unsigned integer type corresponding to `T`, with the same cv-qualifiers.
If `T` is signed or unsigned `char`, `short`, `int`, `long`, `long long`; the unsigned type from this list corresponding to `T` is provided.
If `T` is an enumeration type or `char`, `wchar_t`<sup>(since C++20)</sup> , `char8_t`, `char16_t`, `char32_t`; the unsigned integer type with the smallest rank having the same `sizeof` as `T` is provided.
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
using make_unsigned_t = typename make_unsigned<T>::type;
```


## Example


### Example

```cpp
#include <type_traits>

int main()
{
    using uchar_type = std::make_unsigned_t<char>;
    using uint_type  = std::make_unsigned_t<int>;
    using ulong_type = std::make_unsigned_t<volatile long>;

    static_assert(
        std::is_same_v<uchar_type, unsigned char> and
        std::is_same_v<uint_type, unsigned int> and
        std::is_same_v<ulong_type, volatile unsigned long>
    );
}
```


## See also


| cpp/types/dsc is_signed | (see dedicated page) |
| cpp/types/dsc is_unsigned | (see dedicated page) |
| cpp/types/dsc make_signed | (see dedicated page) |

