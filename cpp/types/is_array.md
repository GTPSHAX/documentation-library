---
title: std::is_array
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_array
---

cpp/types/traits/is|1=is_array
|description=
Checks whether `T` is an array type. Provides the member constant `value` which is equal to `true`, if `T` is an array type. Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is an array type

## Possible implementation

eq fun
|1=
template<class T>
struct is_array : std::false_type {};
template<class T>
struct is_array<T[]> : std::true_type {};
template<class T, std::size_t N>
struct is_array<T[N]> : std::true_type {};

## Example


### Example

```cpp
#include <array>
#include <type_traits>

class A {};
static_assert(std::is_array<A>::value == false);
static_assert(std::is_array<A[]>::value == true);
static_assert(std::is_array<A[3]>::value == true);

static_assert(std::is_array<float>::value == false);
static_assert(std::is_array<int>::value == false);
static_assert(std::is_array<int[]>::value == true);
static_assert(std::is_array<int[3]>::value == true);
static_assert(std::is_array<std::array<int, 3>>::value == false);

int main() {}
```


## See also


| cpp/types/dsc is_bounded_array | (see dedicated page) |
| cpp/types/dsc is_unbounded_array | (see dedicated page) |
| cpp/types/dsc rank | (see dedicated page) |
| cpp/types/dsc extent | (see dedicated page) |
| cpp/types/dsc remove_extent | (see dedicated page) |
| cpp/types/dsc remove_all_extents | (see dedicated page) |

