---
title: std::is_bounded_array
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_bounded_array
---

cpp/types/traits/is|1=is_bounded_array
|std=c++20
|description=
Checks whether `T` is an array type of known bound. Provides the member constant `value` which is equal to `true`, if `T` is an array type of known bound. Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is an array type of known bound

## Possible implementation

eq fun
|1=
template<class T>
struct is_bounded_array : std::false_type {};
template<class T, std::size_t N>
struct is_bounded_array<T[N]> : std::true_type {};

## Notes


## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

#define OUT(...) std::cout << #__VA_ARGS__ << " : " << __VA_ARGS__ << '\n'

class A {};

int main()
{
    std::cout << std::boolalpha;
    OUT(std::is_bounded_array_v<A>);
    OUT(std::is_bounded_array_v<A[]>);
    OUT(std::is_bounded_array_v<A[3]>);
    OUT(std::is_bounded_array_v<float>);
    OUT(std::is_bounded_array_v<int>);
    OUT(std::is_bounded_array_v<int[]>);
    OUT(std::is_bounded_array_v<int[3]>);
}
```


**Output:**
```
std::is_bounded_array_v<A> : false
std::is_bounded_array_v<A[]> : false
std::is_bounded_array_v<A[3]> : true
std::is_bounded_array_v<float> : false
std::is_bounded_array_v<int> : false
std::is_bounded_array_v<int[]> : false
std::is_bounded_array_v<int[3]> : true
```


## See also


| cpp/types/dsc is_array | (see dedicated page) |
| cpp/types/dsc is_unbounded_array | (see dedicated page) |
| cpp/types/dsc extent | (see dedicated page) |

