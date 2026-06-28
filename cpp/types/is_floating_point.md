---
title: std::is_floating_point
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_floating_point
---

cpp/types/traits/is|1=is_floating_point
|description=
Checks whether `T` is a floating-point type. Provides the member constant `value` which is equal to `true`, if `T` is the type `float`, `double`, `long double`<sup>(since C++23)</sup> , or any extended floating-point types (`std::float16_t`, `std::float32_t`, `std::float64_t`, `std::float128_t`, or `std::bfloat16_t`), including any cv-qualified variants. Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is a floating-point type (possibly cv-qualified)

## Possible implementation

eq fun
|1=
template<class T>
struct is_floating_point
: std::integral_constant<
bool,
// Note: standard floating-point types
std::is_same<float, typename std::remove_cv<T>::type>::value
std::is_same<double, typename std::remove_cv<T>::type>::value
std::is_same<long double, typename std::remove_cv<T>::type>::value
// Note: extended floating-point types (C++23, if supported)
std::is_same<std::float16_t, typename std::remove_cv<T>::type>::value
std::is_same<std::float32_t, typename std::remove_cv<T>::type>::value
std::is_same<std::float64_t, typename std::remove_cv<T>::type>::value
std::is_same<std::float128_t, typename std::remove_cv<T>::type>::value
std::is_same<std::bfloat16_t, typename std::remove_cv<T>::type>::value
> {};

## Example


### Example

```cpp
#include <type_traits>

class A {};
static_assert(!std::is_floating_point_v<A>);

static_assert(std::is_floating_point_v<float>);
static_assert(!std::is_floating_point_v<float&>);
static_assert(std::is_floating_point_v<double>);
static_assert(!std::is_floating_point_v<double&>);
static_assert(!std::is_floating_point_v<int>);

int main() {}
```


## See also


| cpp/types/numeric_limits/dsc is_iec559 | (see dedicated page) |
| cpp/types/dsc is_integral | (see dedicated page) |
| cpp/types/dsc is_arithmetic | (see dedicated page) |
| cpp/concepts/dsc floating_point | (see dedicated page) |

