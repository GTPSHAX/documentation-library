---
title: std::numeric_limits::is_specialized
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/is_specialized
---


```cpp
dcl rev multi
|dcl1=
static const bool is_specialized;
|since2=c++11|dcl2=
static constexpr bool is_specialized;
```

The value of `std::numeric_limits<T>::is_specialized` is `true` for all `T` for which there exists a specialization of `std::numeric_limits`.

## Standard specializations


## Example


### Example

```cpp
#include <iostream>
#include <limits>
#include <type_traits>

int main()
{
    enum E{};

    std::cout << std::boolalpha
              << std::numeric_limits<bool>::is_specialized << '\n'
              << std::numeric_limits<long long>::is_specialized << '\n'
              << std::numeric_limits<std::true_type>::is_specialized << '\n'
              << std::numeric_limits<E>::is_specialized << '\n';
}
```


**Output:**
```
true
true
false
false
```


## See also


| cpp/types/numeric_limits/dsc is_integer | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_iec559 | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_exact | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_bounded | (see dedicated page) |

