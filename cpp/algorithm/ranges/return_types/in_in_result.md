---
title: std::ranges::in_in_result
type: Constrained algorithms
source: https://en.cppreference.com/w/cpp/algorithm/ranges/return_types/in_in_result
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|1=
template< class I1, class I2 >
struct in_in_result;
```

`ranges::in_in_result` is a class template that provides a way to store two iterators as a single unit.

## Template parameters


### Parameters

- `I1, I2` - the types of the iterators that the `ranges::in_in_result` stores.

## Data members


| Item | Description |
|------|-------------|
| **Object** | Description |

All these members are declared with  attribute.

## Member functions

member|operator in_in_result<II1, II2>|2=

```cpp
dcl|num=1|1=
template<class II1, class II2>
requires std::convertible_to<const I1&, II1> && std::convertible_to<const I2&, II2>
constexpr operator in_in_result<II1, II2>() const &;
dcl|num=2|1=
template<class II1, class II2>
requires std::convertible_to<I1, II1> && std::convertible_to<I2, II2>
constexpr operator in_in_result<II1, II2>() &&;
```

Converts `*this` to the result by constructing every data member of the result from the corresponding member of `*this`.
1. Equivalent to }.
2. Equivalent to }.

## Standard library

The following standard library functions use `ranges::in_in_result` as the return type:


#### Algorithm functions

| cpp/algorithm/ranges/dsc mismatch | (see dedicated page) |
| cpp/algorithm/ranges/dsc swap_ranges | (see dedicated page) |


## Synopsis


```cpp
namespace std::ranges
{
    template<class I1, class I2>
    struct in_in_result
    {
        [[no_unique_address]] I1 in1;
        [[no_unique_address]] I2 in2;

        template<class II1, class II2>
        requires std::convertible_to<const I1&, II1> && std::convertible_to<const I2&, II2>
        constexpr operator in_in_result<II1, II2>() const &
        {
            return {in1, in2};
        }

        template<class II1, class II2>
        requires std::convertible_to<I1, II1> && std::convertible_to<I2, II2>
        constexpr operator in_in_result<II1, II2>() &&
        {
            return {std::move(in1), std::move(in2)};
        }
    };
}
```


## Notes


## Example


## See also


| cpp/utility/dsc pair | (see dedicated page) |
| cpp/utility/dsc tuple | (see dedicated page) |

