---
title: std::in_range
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/in_range
---


```cpp
**Header:** `<`utility`>`
dcl|since=c++20|1=
template< class R, class T >
constexpr bool in_range( T t ) noexcept;
```

Returns `true` if the value of `t` is in the range of values that can be represented in `R`, that is, if `t` can be converted to `R` in a value-preserving manner.
It is a compile-time error if either `T` or `U` is a non-integer type, a character type, or `bool`.

## Parameters


### Parameters

- `t` - value to test

## Return value

`true` if the value of `t` is representable in `R`, `false` otherwise.

## Possible implementation

eq fun|1=
template<class R, class T>
constexpr bool in_range(T t) noexcept
{
return std::cmp_greater_equal(t, std::numeric_limits<R>::min()) &&
std::cmp_less_equal(t, std::numeric_limits<R>::max());
}

## Notes

This function cannot be used with enums (including ), `char`, `char8_t`, `char16_t`, `char32_t`, `wchar_t` and `bool`.

## Example


### Example

```cpp
#include <iostream>
#include <utility>

int main()
{
    std::cout << std::boolalpha;

    std::cout << std::in_range<std::size_t>(-1) << '\n';
    std::cout << std::in_range<std::size_t>(42) << '\n';
}
```


**Output:**
```
false
true
```


## See also


| cpp/algorithm/ranges/dsc min | (see dedicated page) |
| cpp/algorithm/ranges/dsc max | (see dedicated page) |
| cpp/algorithm/ranges/dsc clamp | (see dedicated page) |
| cpp/numeric/dsc lerp | (see dedicated page) |

