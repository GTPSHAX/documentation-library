---
title: std::ranges::out_value_result
type: Constrained algorithms
source: https://en.cppreference.com/w/cpp/algorithm/ranges/return_types/out_value_result
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++23|1=
template< class O, class T >
struct out_value_result;
```

`ranges::out_value_result` is a class template that provides a way to store an iterator and a value as a single unit.

## Template parameters


### Parameters

- `O, T` - the types of the objects that the `ranges::out_value_result` stores.

## Data members


| Item | Description |
|------|-------------|
| **Object** | Description |

All these members are declared with  attribute.

## Member functions

member|operator out_value_result<O2, T2>|2=

```cpp
dcl|num=1|1=
template<class O2, class T2>
requires convertible_to<const O&, O2> && convertible_to<const T&, T2>
constexpr operator out_value_result<O2, T2>() const &;
dcl|num=2|1=
template<class O2, class T2>
requires convertible_to<O, O2> && convertible_to<T, T2>
constexpr operator out_value_result<O2, T2>() &&;
```

Converts `*this` to the result by constructing every data member of the result from the corresponding member of `*this`.
1. Equivalent to }.
2. Equivalent to }.

## Standard library

The following standard library functions use `ranges::out_value_result` as the return type:


#### Algorithm functions

| cpp/algorithm/ranges/dsc iota | (see dedicated page) |


## Synopsis


```cpp
namespace std::ranges
{
    template<class O, class T>
    struct out_value_result
    {
        [[no_unique_address]] O out;
        [[no_unique_address]] T value;

        template<class O2, class T2>
        requires convertible_to<const O&, O2> && convertible_to<const T&, T2>
        constexpr operator out_value_result<O2, T2>() const &
        {
            return {out, value};
        }

        template<class O2, class T2>
        requires convertible_to<O, O2> && convertible_to<T, T2>
        constexpr operator out_value_result<O2, T2>() &&
        {
            return {std::move(out), std::move(value)};
        }
    };
}
```


## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <cassert>
#include <numeric>
#include <ranges>

int main()
{
    std::array<int, 4> a{};
    constexpr std::array expected{2, 3, 4, 5};
    const auto result = std::ranges::iota(a, 2);
    assert(std::ranges::distance(a.cbegin(), result.out) == 4);
    assert(result.value == 6);
    assert(a == expected);
}
```


## See also


| cpp/utility/dsc pair | (see dedicated page) |
| cpp/utility/dsc tuple | (see dedicated page) |

