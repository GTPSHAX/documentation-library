---
title: std::ranges::in_found_result
type: Constrained algorithms
source: https://en.cppreference.com/w/cpp/algorithm/ranges/return_types/in_found_result
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|
template< class I >
struct in_found_result;
```

`ranges::in_found_result` is a class template that provides a way to store an iterator and a boolean flag as a single unit.

## Template parameters


### Parameters

- `I` - the type of the iterator that the `ranges::in_found_result` stores.

## Data members


| Item | Description |
|------|-------------|
| **Object** | Description |


## Member functions

member|operator in_found_result<I2>|2=

```cpp
dcl|num=1|1=
template<class I2>
requires std::convertible_to<const I&, I2>
constexpr operator in_found_result<I2>() const &;
dcl|num=2|1=
template<class I2>
requires std::convertible_to<I, I2>
constexpr operator in_found_result<I2>() &&;
```

Converts `*this` to the result by constructing every data member of the result from the corresponding member of `*this`.
1. Equivalent to }.
2. Equivalent to }.

## Standard library

The following standard library functions use `ranges::in_found_result` as the return type:


#### Algorithm functions

| cpp/algorithm/ranges/dsc next_permutation | (see dedicated page) |
| cpp/algorithm/ranges/dsc prev_permutation | (see dedicated page) |


## Synopsis


```cpp
namespace std::ranges
{
    template<class I>
    struct in_found_result
    {
        [[no_unique_address]] I in;
        bool found;

        template<class I2>
        requires std::convertible_to<const I&, I2>
        constexpr operator in_found_result<I2>() const &
        {
            return {in, found};
        }

        template<class I2>
        requires std::convertible_to<I, I2>
        constexpr operator in_found_result<I2>() &&
        {
            return {std::move(in), found};
        }
    };
}
```


## Notes


## Example


### Example


**Output:**
```
1 3 2 
result.found = true
```


## See also


| cpp/utility/dsc pair | (see dedicated page) |
| cpp/utility/dsc tuple | (see dedicated page) |

