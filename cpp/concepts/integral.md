---
title: std::integral
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/integral
---

ddcl|header=concepts|since=c++20|1=
template< class T >
concept integral = std::is_integral_v<T>;
The concept `integral<T>` is satisfied if and only if `T` is an integral type.

## Example


### Example

```cpp
#include <concepts>
#include <iostream>

void print(std::integral auto i)
{
    std::cout << "Integral: " << i << '\n';
}

void print(auto x)
{
    std::cout << "Non-integral: " << x << '\n';
}

int main()
{
    std::cout << std::boolalpha;

    static_assert(std::integral<bool>);
    print(true);

    static_assert(std::integral<char>);
    print('o');

    static_assert(std::integral<int>);
    print(007);

    static_assert( ! std::integral<double> );
    print(2e2);

    static_assert( ! std::integral<decltype("")> );
    print("∫∫∫");
}
```


**Output:**
```
Integral: true
Integral: o
Integral: 7
Non-integral: 200
Non-integral: ∫∫∫
```


## References


## See also


| cpp/types/dsc is_integral | (see dedicated page) |

