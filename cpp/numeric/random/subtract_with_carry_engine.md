---
title: std::subtract_with_carry_engine
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/subtract_with_carry_engine
---


```cpp
**Header:** `<`random`>`
dcl|since=c++11|
template<
class UIntType,
std::size_t w, std::size_t s, std::size_t r
> class subtract_with_carry_engine;
```

Is a random number engine that uses [subtract with carry](https://en.wikipedia.org/wiki/subtract with carry) algorithm.

## Template parameters


### Parameters

- `w` - the word size, in bits, of the state sequence
- `s` - the short lag
- `r` - the long lag
If `w` is not in [1, std::numeric_limits<UIntType>::digits|right=]), or `s` is not in [1, r), the program is ill-formed.

## Generator properties

The `size` of the states of `subtract_with_carry_engine` is , each of them consists of two parts:
* A sequence `X` of `r` integer values, where each value is in .
* An integer `c` (known as the ''carry''), whose value is either `0` or `1`.
Given that  stands for the th value (starting from 0) of `X`, the `transition algorithm` of `subtract_with_carry_engine` ()) is defined as follows:
# Let `Y` be mathjax-or|\(\scriptsize X_{i-s}-X_{i-r}-c\)|X-X-c.
# Let `y` be , and set  to `y`.
# If `Y` is negative, set `c` to `1`, otherwise set `c` to `0`.
The `generation algorithm` of `subtract_with_carry_engine` is ) = y, where `y` is the value produced in step 2 of the transition algorithm.

## Predefined specializations

The following specializations define the random number engine with two commonly used parameter sets:


| Item | Description |
|------|-------------|
| random | |
| **Type** | Definition |
| cpp/numeric/random/dsc ranlux24_base | (see dedicated page) |
| cpp/numeric/random/dsc ranlux48_base | (see dedicated page) |


## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Data members


## Member functions


#### Construction and Seeding

| cpp/numeric/random/engine/dsc constructor|subtract_with_carry_engine | (see dedicated page) |
| cpp/numeric/random/engine/dsc seed|subtract_with_carry_engine | (see dedicated page) |

#### Generation

| cpp/numeric/random/engine/dsc operator()|subtract_with_carry_engine | (see dedicated page) |
| cpp/numeric/random/engine/dsc discard|subtract_with_carry_engine | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/engine/dsc min|subtract_with_carry_engine | (see dedicated page) |
| cpp/numeric/random/engine/dsc max|subtract_with_carry_engine | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/engine/dsc operator cmp|subtract_with_carry_engine | (see dedicated page) |
| cpp/numeric/random/engine/dsc operator ltltgtgt|subtract_with_carry_engine | (see dedicated page) |


## Example

