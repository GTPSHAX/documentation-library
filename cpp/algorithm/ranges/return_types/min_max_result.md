---
title: std::ranges::min_max_result
type: Constrained algorithms
source: https://en.cppreference.com/w/cpp/algorithm/ranges/return_types/min_max_result
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|
template< class T >
struct min_max_result;
```

`ranges::min_max_result` is a class template that provides a way to store two objects or references of the same type as a single unit.

## Template parameters


### Parameters

- `T` - the type of the objects or references that the `ranges::min_max_result` stores.

## Data members


| Item | Description |
|------|-------------|
| **Object** | Description |

All these members are declared with  attribute.

## Member functions

member|operator min_max_result<T2>|2=

```cpp
dcl|num=1|1=
template<class T2>
requires std::convertible_to<const T&, T2>
constexpr operator min_max_result<T2>() const &;
dcl|num=2|1=
template<class T2>
requires std::convertible_to<T, T2>
constexpr operator min_max_result<T2>() &&;
```

Converts `*this` to the result by constructing every data member of the result from the corresponding member of `*this`.
1. Equivalent to }.
2. Equivalent to }.

## Standard library

The following standard library functions use `ranges::min_max_result` as the return type:


#### Algorithm functions

| cpp/algorithm/ranges/dsc minmax | (see dedicated page) |
| cpp/algorithm/ranges/dsc minmax_element | (see dedicated page) |


## Synopsis


```cpp
namespace std::ranges
{
    template<class T>
    struct min_max_result
    {
        [[no_unique_address]] T min;
        [[no_unique_address]] T max;

        template<class T2>
        requires std::convertible_to<const T&, T2>
        constexpr operator min_max_result<T2>() const &
        {
            return {min, max};
        }

        template<class T2>
        requires std::convertible_to<T, T2>
        constexpr operator min_max_result<T2>() &&
        {
            return {std::move(min), std::move(max)};
        }
    };
}
```


## Notes


## Example


## See also


| cpp/utility/dsc pair | (see dedicated page) |
| cpp/utility/dsc tuple | (see dedicated page) |

