---
title: std::ranges::in_value_result
type: Constrained algorithms
source: https://en.cppreference.com/w/cpp/algorithm/ranges/return_types/in_value_result
---

ddcl|header=algorithm|since=c++23|
template< class I, class T >
struct in_value_result;
`ranges::in_value_result` is a class template that provides a way to store an iterator and a value as a single unit.

## Template parameters


### Parameters

- `I, T` - the types of the objects that the `ranges::in_value_result` stores.

## Data members


| Item | Description |
|------|-------------|
| **Object** | Description |

All these members are declared with  attribute.

## Member functions

member|operator in_value_result<I2, T2>|2=

```cpp
dcl|num=1|1=
template<class I2, class T2>
requires convertible_to<const I&, I2> && convertible_to<const T&, T2>
constexpr operator in_value_result<I2, T2>() const &;
dcl|num=2|1=
template<class I2, class T2>
requires convertible_to<I, I2> && convertible_to<T, T2>
constexpr operator in_value_result<I2, T2>() &&;
```

Converts `*this` to the result by constructing every data member of the result from the corresponding member of `*this`.
1. Equivalent to }.
2. Equivalent to }.

## Standard library

The following standard library functions use `ranges::in_value_result` as the return type:


#### Algorithm functions

| cpp/algorithm/ranges/dsc fold_left_with_iter | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_first_with_iter | (see dedicated page) |


## Synopsis


```cpp
namespace std::ranges
{
    template<class I, class T>
    struct in_value_result
    {
        [[no_unique_address]] I in;
        [[no_unique_address]] T value;

        template<class I2, class T2>
        requires convertible_to<const I&, I2> && convertible_to<const T&, T2>
        constexpr operator in_value_result<I2, T2>() const &
        {
            return {in, value};
        }

        template<class I2, class T2>
        requires convertible_to<I, I2> && convertible_to<T, T2>
        constexpr operator in_value_result<I2, T2>() &&
        {
            return {std::move(in), std::move(value)};
        }
    };
}
```


## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <functional>

int main()
{
    static constexpr auto v = {1, 2, 3};
    constexpr auto ret = std::ranges::fold_left_with_iter(v, 4, std::plus<>());
    static_assert(ret.in == v.end());
    static_assert(ret.value == 1 + 2 + 3 + 4);
}
```


## See also


| cpp/utility/dsc pair | (see dedicated page) |
| cpp/utility/dsc tuple | (see dedicated page) |

