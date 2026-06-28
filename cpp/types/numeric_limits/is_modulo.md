---
title: std::numeric_limits::is_modulo
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/is_modulo
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
static const bool is_modulo;
|dcl2=
static constexpr bool is_modulo;
```

The value of `std::numeric_limits<T>::is_modulo` is `true` for all arithmetic types `T` that handle overflows with modulo arithmetic, that is, if the result of addition, subtraction, multiplication, or division of this type would fall outside the range `[``min()``,&nbsp;``max()``]`, the value returned by such operation differs from the expected value by a multiple of `max() - min() + 1`.
`is_modulo` is `false` for signed integer types, unless the implementation defines signed integer overflow to wrap.

## Standard specializations


## Notes

The standard said "On most machines, this is `true` for signed integers." before the resolution of . See [http://gcc.gnu.org/bugzilla/show_bug.cgi?id=22200 GCC PR 22200] for a related discussion.

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>
#include <limits>

template<class T>
typename std::enable_if<std::numeric_limits<T>::is_modulo>::type
    check_overflow()
{
    std::cout << "max value is " << std::numeric_limits<T>::max() << '\n'
              << "min value is " << std::numeric_limits<T>::min() << '\n'
              << "max value + 1 is " << std::numeric_limits<T>::max()+1 << '\n';
}

int main()
{
    check_overflow<int>();
    std::cout << '\n';
    check_overflow<unsigned long>();
//  check_overflow<float>(); // compile-time error, not a modulo type
}
```


**Output:**
```
max value is 2147483647
min value is -2147483648
max value + 1 is -2147483648

max value is 18446744073709551615
min value is 0
max value + 1 is 0
```


## Defect reports


## See also


| cpp/types/numeric_limits/dsc is_integer | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_iec559 | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_exact | (see dedicated page) |

