---
title: std::type_identity
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/type_identity
---

ddcl|header=type_traits|since=c++20|
template< class T >
struct type_identity;
Provides the member typedef `type` that names `T` (i.e., the identity transformation).

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types

ddcl|since=c++20|1=
template< class T >
using type_identity_t = type_identity<T>::type;

## Possible implementation

eq fun
|1=
template<class T>
struct type_identity { using type = T; };

## Notes

`std::type_identity` can be used to establish non-deduced contexts in template argument deduction.

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

template<class T>
T foo(T a, T b) { return a + b; }

template<class T>
T bar(T a, std::type_identity_t<T> b) { return a + b; }

int main()
{
    // foo(4.2, 1); // error, deduced conflicting types for 'T'
    std::cout << bar(4.2, 1) << '\n';  // OK, calls bar<double>
}
```


**Output:**
```
5.2
```


## See also


| cpp/utility/functional/dsc identity | (see dedicated page) |

