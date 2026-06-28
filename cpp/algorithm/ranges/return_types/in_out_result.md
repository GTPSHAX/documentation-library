---
title: std::ranges::in_out_result
type: Constrained algorithms
source: https://en.cppreference.com/w/cpp/algorithm/ranges/return_types/in_out_result
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|1=
template< class I, class O >
struct in_out_result;
```

`ranges::in_out_result` is a class template that provides a way to store two iterators as a single unit.

## Template parameters


### Parameters

- `I, O` - the types of the objects that the `ranges::in_out_result` stores.

## Data members


| Item | Description |
|------|-------------|
| **Object** | Description |

All these members are declared with  attribute.

## Member functions

member|operator in_out_result<I2, O2>|2=

```cpp
dcl|num=1|1=
template<class I2, class O2>
requires std::convertible_to<const I&, I2> && std::convertible_to<const O&, O2>
constexpr operator in_out_result<I2, O2>() const &;
dcl|num=2|1=
template<class I2, class O2>
requires std::convertible_to<I, I2> && std::convertible_to<O, O2>
constexpr operator in_out_result<I2, O2>() &&;
```

Converts `*this` to the result by constructing every data member of the result from the corresponding member of `*this`.
1. Equivalent to }.
2. Equivalent to }.

## Standard library

The following standard library functions use `ranges::in_out_result` as the return type:


#### Algorithm functions

| cpp/algorithm/ranges/dsc copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy_n | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy_backward | (see dedicated page) |
| cpp/algorithm/ranges/dsc move | (see dedicated page) |
| cpp/algorithm/ranges/dsc move_backward | (see dedicated page) |
| cpp/algorithm/ranges/dsc transform | (see dedicated page) |
| cpp/algorithm/ranges/dsc replace_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc remove_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc unique_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc reverse_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc rotate_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc partial_sort_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc set_difference | (see dedicated page) |

#### Memory functions

| cpp/memory/ranges/dsc uninitialized_copy | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_copy_n | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_move | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_move_n | (see dedicated page) |


## Synopsis


```cpp
namespace std::ranges
{
    template<class I, class O>
    struct in_out_result
    {
        [[no_unique_address]] I in;
        [[no_unique_address]] O out;

        template<class I2, class O2>
        requires std::convertible_to<const I&, I2> && std::convertible_to<const O&, O2>
        constexpr operator in_out_result<I2, O2>() const &
        {
            return {in, out};
        }

        template<class I2, class O2>
        requires std::convertible_to<I, I2> && std::convertible_to<O, O2>
        constexpr operator in_out_result<I2, O2>() &&
        {
            return {std::move(in), std::move(out)};
        }
    };
}
```


## Notes


## Example


### Example


**Output:**
```
transform
TRANSFORM
```


## See also


| cpp/utility/dsc pair | (see dedicated page) |
| cpp/utility/dsc tuple | (see dedicated page) |

