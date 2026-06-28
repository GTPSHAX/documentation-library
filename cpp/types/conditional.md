---
title: std::conditional
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/conditional
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|1=
template< bool B, class T, class F >
struct conditional;
```

Provides member typedef `type`, which is defined as `T` if `B` is `true` at compile time, or as `F` if `B` is `false`.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Helper types


```cpp
dcl|since=c++14|1=
template< bool B, class T, class F >
using conditional_t = typename conditional<B,T,F>::type;
```


## Possible implementation

eq fun
|1=
template<bool B, class T, class F>
struct conditional { using type = T; };
template<class T, class F>
struct conditional<false, T, F> { using type = F; };

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>
#include <typeinfo>

int main()
{
    using Type1 = std::conditional<true, int, double>::type;
    using Type2 = std::conditional<false, int, double>::type;
    using Type3 = std::conditional<sizeof(int) >= sizeof(double), int, double>::type;

    std::cout << typeid(Type1).name() << '\n';
    std::cout << typeid(Type2).name() << '\n';
    std::cout << typeid(Type3).name() << '\n';
}
```


**Output:**
```
int
double
double
```


## See also


| cpp/types/dsc enable_if | (see dedicated page) |

