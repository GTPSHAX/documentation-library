---
title: std::numeric_limits::has_infinity
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/has_infinity
---


```cpp
dcl rev multi|until1=c++11|dcl1=
static const bool has_infinity;
|dcl2=
static constexpr bool has_infinity;
```

The value of `std::numeric_limits<T>::has_infinity` is `true` for all types `T` capable of representing the positive infinity as a distinct special value. This constant is meaningful for all floating-point types and is guaranteed to be `true` if `1=std::numeric_limits<T>::is_iec559 == true`.

## Standard specializations


| Item | Description |
|------|-------------|
| **{{tt** | T |


## Example


### Example

```cpp
#include <iostream>
#include <limits>

int main()
{
    std::cout << std::boolalpha
              << std::numeric_limits<int>::has_infinity << '\n'
              << std::numeric_limits<long>::has_infinity << '\n'
              << std::numeric_limits<float>::has_infinity << '\n'
              << std::numeric_limits<double>::has_infinity << '\n';
}
```


**Output:**
```
false
false
true
true
```


## See also


| cpp/types/numeric_limits/dsc infinity | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_quiet_NaN | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_signaling_NaN | (see dedicated page) |

