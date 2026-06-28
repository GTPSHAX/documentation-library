---
title: std::is_volatile
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_volatile
---

cpp/types/traits/is|1=is_volatile
|description=
If `T` is a volatile-qualified type (that is, `volatile`, or `const volatile`), provides the member constant `value` equal to `true`. For any other type, `value` is `false`.
|inherit_desc=`T` is a volatile-qualified type

## Possible implementation

eq fun
|1=
template<class T> struct is_volatile : std::false_type {};
template<class T> struct is_volatile<volatile T> : std::true_type {};

## Example


### Example

```cpp
#include <type_traits>
#include <valarray>

static_assert(!std::is_volatile_v<int>);
static_assert(std::is_volatile_v<volatile int>);
static_assert(std::is_volatile_v<volatile const int>);
static_assert(std::is_volatile_v<volatile std::valarray<float>>);
static_assert(!std::is_volatile_v<std::valarray<volatile float>>);

int main() {}
```


## See also


| cpp/types/dsc is_const | (see dedicated page) |

