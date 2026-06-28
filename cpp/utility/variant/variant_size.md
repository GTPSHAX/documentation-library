---
title: std::variant_size_v
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/variant_size
---


```cpp
**Header:** `<`variant`>`
dcl|since=c++17|num=1|
template< class T >
struct variant_size; /* undefined */
dcl|since=c++17|num=2|
template< class... Types >
struct variant_size<std::variant<Types...>>
: std::integral_constant<std::size_t, sizeof...(Types)> {};
dcl|since=c++17|num=3|
template< class T >
class variant_size<const T>;
dcl|since=c++17|num=4|deprecated=c++20|
template< class T >
class variant_size<volatile T>;
dcl|since=c++17|num=5|deprecated=c++20|
template< class T >
class variant_size<const volatile T>;
```

Provides access to the number of alternatives in a possibly cv-qualified variant as a compile-time constant expression.
Formally,
2. meets the *UnaryTypeTrait* requirements with a base characteristic of `std::integral_constant<std::size_t, sizeof...(Types)>`
@3-5@ meets the *UnaryTypeTrait* requirements with a base characteristic of `std::integral_constant<std::size_t, std::variant_size<T>::value>`

## Helper variable template

ddcl|since=c++17|1=
template< class T >
constexpr std::size_t variant_size_v = std::variant_size<T>::value;

## Notes

All specializations of `std::variant_size` satisfy *UnaryTypeTrait* with  ''base characteristic'' `std::integral_constant<std::size_t, N>` for some `N`.

## Example


### Example

```cpp
#include <any>
#include <variant>

static_assert(std::variant_size_v<std::variant<>> == 0);
static_assert(std::variant_size_v<std::variant<int>> == 1);
static_assert(std::variant_size_v<std::variant<int, int>> == 2);
static_assert(std::variant_size_v<std::variant<int, int, int>> == 3);
static_assert(std::variant_size_v<std::variant<int, float, double>> == 3);
static_assert(std::variant_size_v<std::variant<std::monostate, void>> == 2);
static_assert(std::variant_size_v<std::variant<const int, const float>> == 2);
static_assert(std::variant_size_v<std::variant<std::variant<std::any>>> == 1);

int main() {}
```


## See also


| cpp/utility/variant/dsc variant_alternative | (see dedicated page) |
| cpp/utility/tuple/dsc tuple_size | (see dedicated page) |

