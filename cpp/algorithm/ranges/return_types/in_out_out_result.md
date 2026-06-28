---
title: std::ranges::in_out_out_result
type: Constrained algorithms
source: https://en.cppreference.com/w/cpp/algorithm/ranges/return_types/in_out_out_result
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|1=
template< class I, class O1, class O2 >
struct in_out_out_result;
```

`ranges::in_out_out_result` is a class template that provides a way to store three iterators as a single unit.

## Template parameters


### Parameters

- `I, O1, O2` - the types of the objects that the `ranges::in_out_out_result` stores.

## Data members


| Item | Description |
|------|-------------|
| **Object** | Description |

All these members are declared with  attribute.

## Member functions

member|operator in_out_out_result<II, OO1, OO2>|2=

```cpp
dcl|num=1 |1=
template<class II, class OO1, class OO2>
requires std::convertible_to<const I&, II> &&
std::convertible_to<const O1&, OO1> &&
std::convertible_to<const O2&, OO2>
constexpr operator in_out_out_result<II, OO1, OO2>() const &;
dcl|num=2|1=
template<class II, class OO1, class OO2>
requires std::convertible_to<I, II> &&
std::convertible_to<O1, OO1> &&
std::convertible_to<O2, OO2>
constexpr operator in_out_out_result<II, OO1, OO2>() &&;
```

Converts `*this` to the result by constructing every data member of the result from the corresponding member of `*this`.
1. Equivalent to }.
2. Equivalent to }.

## Standard library

The following standard library functions use `ranges::in_out_out_result` as the return type:


#### Algorithm functions

| cpp/algorithm/ranges/dsc partition_copy | (see dedicated page) |


## Synopsis


```cpp
namespace std::ranges
{
    template<class I, class O1, class O2>
    struct in_out_out_result
    {
        [[no_unique_address]] I  in;
        [[no_unique_address]] O1 out1;
        [[no_unique_address]] O2 out2;

        template<class II, class OO1, class OO2>
        requires std::convertible_to<const I&, II> &&
                 std::convertible_to<const O1&, OO1> &&
                 std::convertible_to<const O2&, OO2>
        constexpr operator in_out_out_result<II, OO1, OO2>() const &
        {
            return {in, out1, out2};
        }

        template<class II, class OO1, class OO2>
        requires std::convertible_to<I, II> &&
                 std::convertible_to<O1, OO1> &&
                 std::convertible_to<O2, OO2>
        constexpr operator in_out_out_result<II, OO1, OO2>() &&
        {
            return {std::move(in), std::move(out1), std::move(out2)};
        }
    };
}
```


## Notes


## Example


### Example


**Output:**
```
in: { T v E e N c S t O o R r }
o1: { T E N S O R }
o2: { v e c t o r }
```


## See also


| cpp/utility/dsc pair | (see dedicated page) |
| cpp/utility/dsc tuple | (see dedicated page) |

