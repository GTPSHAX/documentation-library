---
title: std::floating_point
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/floating_point
---

ddcl|header=concepts|since=c++20|1=
template< class T >
concept floating_point = std::is_floating_point_v<T>;
The concept `floating_point<T>` is satisfied if and only if `T` is a floating-point type.

## Example


### Example

```cpp
#include <concepts>
#include <iostream>
#include <type_traits>

constexpr std::floating_point auto x2(std::floating_point auto x)
{
    return x + x;
}

constexpr std::integral auto x2(std::integral auto x)
{
    return x << 1;
}

int main()
{
    constexpr auto d = x2(1.1);
    static_assert(std::is_same_v<double const, decltype(d)>);
    std::cout << d << '\n';

    constexpr auto f = x2(2.2f);
    static_assert(std::is_same_v<float const, decltype(f)>);
    std::cout << f << '\n';

    constexpr auto i = x2(444);
    static_assert(std::is_same_v<int const, decltype(i)>);
    std::cout << i << '\n';
}
```


**Output:**
```
2.2
4.4
888
```


## References


## See also


| cpp/types/dsc is_floating_point | (see dedicated page) |

