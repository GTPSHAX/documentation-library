---
title: std::is_unbounded_array
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_unbounded_array
---

cpp/types/traits/is|1=is_unbounded_array
|std=c++20
|description=
Checks whether `T` is an . Provides the member constant `value` which is equal to `true`, if `T` is an array type of unknown bound. Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is an array type of unknown bound.

## Possible implementation

eq fun
|1=
template<class T>
struct is_unbounded_array: std::false_type {};
template<class T>
struct is_unbounded_array<T[]> : std::true_type {};

## Notes


## Example


### Example

```cpp
#include <type_traits>

class A {};

static_assert
(""
    && std::is_unbounded_array_v<A> == false
    && std::is_unbounded_array_v<A[]> == true
    && std::is_unbounded_array_v<A[3]> == false
    && std::is_unbounded_array_v<float> == false
    && std::is_unbounded_array_v<int> == false
    && std::is_unbounded_array_v<int[]> == true
    && std::is_unbounded_array_v<int[3]> == false
);

int main() {}
```


## See also


| cpp/types/dsc is_array | (see dedicated page) |
| cpp/types/dsc is_bounded_array | (see dedicated page) |
| cpp/types/dsc extent | (see dedicated page) |

