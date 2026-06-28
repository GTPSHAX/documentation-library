---
title: std::ranges::in_in_out_result
type: Constrained algorithms
source: https://en.cppreference.com/w/cpp/algorithm/ranges/return_types/in_in_out_result
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|1=
template< class I1, class I2, class O >
struct in_in_out_result;
```

`ranges::in_in_out_result` is a class template that provides a way to store three iterators as a single unit.

## Template parameters


### Parameters

- `I1, I2, O` - the types of the iterators that the `ranges::in_in_out_result` stores.

## Data members


| Item | Description |
|------|-------------|
| **Object** | Description |

All these members are declared with  attribute.

## Member functions

member|operator in_in_out_result<II1, II2, OO>|2=

```cpp
dcl|num=1|1=
template<class II1, class II2, class OO>
requires std::convertible_to<const I1&, II1> &&
std::convertible_to<const I2&, II2> &&
std::convertible_to<const O&, OO>
constexpr operator in_in_out_result<II1, II2, OO>() const &;
dcl|num=2|1=
template<class II1, class II2, class OO>
requires std::convertible_to<I1, II1> &&
std::convertible_to<I2, II2> &&
std::convertible_to<O, OO>
constexpr operator in_in_out_result<II1, II2, OO>() &&;
```

Converts `*this` to the result by constructing every data member of the result from the corresponding member of `*this`.
1. Equivalent to }.
2. Equivalent to }.

## Standard library

The following standard library functions use `ranges::in_in_out_result` as the return type:


#### Algorithm functions

| cpp/algorithm/ranges/dsc transform | (see dedicated page) |
| cpp/algorithm/ranges/dsc merge | (see dedicated page) |
| cpp/algorithm/ranges/dsc set_union | (see dedicated page) |
| cpp/algorithm/ranges/dsc set_intersection | (see dedicated page) |
| cpp/algorithm/ranges/dsc set_symmetric_difference | (see dedicated page) |


## Synopsis


```cpp
namespace std::ranges
{
    template<class I1, class I2, class O>
    struct in_in_out_result
    {
        [[no_unique_address]] I1 in1;
        [[no_unique_address]] I2 in2;
        [[no_unique_address]] O  out;

        template<class II1, class II2, class OO>
        requires std::convertible_to<const I1&, II1> &&
                 std::convertible_to<const I2&, II2> &&
                 std::convertible_to<const O&, OO>
        constexpr operator in_in_out_result<II1, II2, OO>() const &
        {
            return {in1, in2, out};
        }

        template<class II1, class II2, class OO>
        requires std::convertible_to<I1, II1> &&
                 std::convertible_to<I2, II2> &&
                 std::convertible_to<O, OO>
        constexpr operator in_in_out_result<II1, II2, OO>() &&
        {
            return {std::move(in1), std::move(in2), std::move(out)};
        }
    };
}
```


## Notes


## Example


### Example


**Output:**
```
in1: 1 2 3 4 5 5 
in2: 3 4 5 6 7 
out: 1 2 3 3 4 4 5 5 5 6 7
```


## See also


| cpp/utility/dsc pair | (see dedicated page) |
| cpp/utility/dsc tuple | (see dedicated page) |

