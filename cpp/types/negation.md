---
title: std::negation
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/negation
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++17|1=
template< class B >
struct negation;
```

Forms the logical negation of the type trait `B`.
The type `std::negation<B>` is a *UnaryTypeTrait* with a base characteristic of `std::bool_constant<!bool(B::value)>`.

## Template parameters


### Parameters

- `B` - any type such that the expression `bool(B::value)` is a valid constant expression 

## Helper variable template

ddcl|since=c++17|1=
template< class B >
constexpr bool negation_v = negation<B>::value;

## Possible implementation

eq fun
|1=
template<class B>
struct negation : std::bool_constant<!bool(B::value)> { };

## Notes


## Example


### Example

```cpp
#include <type_traits>

static_assert(
    std::is_same<
        std::bool_constant<false>,
        typename std::negation<std::bool_constant<true>>::type>::value,
    "");
static_assert(
    std::is_same<
        std::bool_constant<true>,
        typename std::negation<std::bool_constant<false>>::type>::value,
    "");

static_assert(std::negation_v<std::bool_constant<true>> == false);
static_assert(std::negation_v<std::bool_constant<false>> == true);

int main() {}
```


## See also


| cpp/types/dsc conjunction | (see dedicated page) |
| cpp/types/dsc disjunction | (see dedicated page) |
| cpp/types/dsc integral_constant | (see dedicated page) |

