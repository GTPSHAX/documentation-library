---
title: std::is_fundamental
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_fundamental
---

cpp/types/traits/is|1=is_fundamental
|description=
If `T` is a fundamental type (that is, arithmetic type, `void`, `std::nullptr_t`<sup>(since C++26)</sup> , `std::meta::info`), provides the member constant `value` equal `true`. For any other type, `value` is `false`.
|inherit_desc=`T` is a fundamental type

## Possible implementation

eq fun
|1=
template<class T>
struct is_fundamental
: std::integral_constant<
bool,
std::is_arithmetic<T>::value
std::is_void<T>::value
std::is_same<std::nullptr_t, typename std::remove_cv<T>::type>::value
// you can also use 'std::is_null_pointer<T>::value' instead in C++14
#if __cpp_impl_reflection > 0
std::is_reflection_v<T>
#endif
> {};

## Example


### Example

```cpp
#include <type_traits>

static_assert(std::is_fundamental_v<int> == true);
static_assert(std::is_fundamental_v<int&> == false);
static_assert(std::is_fundamental_v<int*> == false);
static_assert(std::is_fundamental_v<void> == true);
static_assert(std::is_fundamental_v<void*> == false);
static_assert(std::is_fundamental_v<float> == true);
static_assert(std::is_fundamental_v<float&> == false);
static_assert(std::is_fundamental_v<float*> == false);
static_assert(std::is_fundamental_v<std::nullptr_t> == true);
static_assert(std::is_fundamental_v<std::is_fundamental<int>> == false);

class A {};
static_assert(std::is_fundamental_v<A> == false);
static_assert(std::is_fundamental_v<std::is_fundamental<A>::value_type>);

int main() {}
```


## See also


| cpp/types/dsc is_compound | (see dedicated page) |
| cpp/types/dsc is_arithmetic | (see dedicated page) |
| cpp/types/dsc is_void | (see dedicated page) |
| cpp/types/dsc is_null_pointer | (see dedicated page) |
| cpp/types/dsc is_reflection | (see dedicated page) |

