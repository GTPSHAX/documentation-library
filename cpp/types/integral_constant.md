---
title: std::integral_constant
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/integral_constant
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|1=
template< class T, T v >
struct integral_constant;
```

`std::integral_constant` wraps a static constant of specified type. It is the base class for the C++ type traits.

## Helper alias templates

A helper alias template `std::bool_constant` is defined for the common case where `T` is `bool`.
ddcl|since=c++17|1=
template< bool B >
using bool_constant = integral_constant<bool, B>;

## Specializations

Two typedefs for the common case where `T` is `bool` are provided:


| Item | Description |
|------|-------------|
| type_traits | |
| **Name** | Definition |


## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Member constants


| Item | Description |
|------|-------------|
| **Name** | Value |


## Member functions


| cpp/types/integral_constant/dsc operator value_type | (see dedicated page) |
| cpp/types/integral_constant/dsc operator() | (see dedicated page) |

member|operator value_type|2=
ddcl|1=
constexpr operator value_type() const noexcept;
Conversion function. Returns the wrapped value.
member|operator()|2=
ddcl|since=c++14|1=
constexpr value_type operator()() const noexcept;
Returns the wrapped value. This function enables `std::integral_constant` to serve as a source of compile-time function objects.

## Possible implementation

eq fun
|1=
template<class T, T v>
struct integral_constant
{
static constexpr T value = v;
using value_type = T;
using type = integral_constant; // using injected-class-name
constexpr operator value_type() const noexcept { return value; }
constexpr value_type operator()() const noexcept { return value; } // since c++14
};

## Notes


## Example


### Example

```cpp
#include <type_traits>

using two_t = std::integral_constant<int, 2>;
using four_t = std::integral_constant<int, 4>;

static_assert(not std::is_same_v<two_t, four_t>);
static_assert(two_t::value * 2 == four_t::value, "2*2 != 4");
static_assert(two_t() << 1 == four_t() >> 0, "2*2 != 4");

enum class E{ e1, e2 };
using c1 = std::integral_constant<E, E::e1>;
using c2 = std::integral_constant<E, E::e2>;
static_assert(c1::value != E::e2);
static_assert(c1() == E::e1);
static_assert(std::is_same_v<c2, c2>);

int main() {}
```


## See also


| cpp/utility/dsc integer_sequence | (see dedicated page) |

