---
title: std::linear_congruential_engine
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/linear_congruential_engine
---


```cpp
**Header:** `<`random`>`
dcl|since=c++11|
template<
class UIntType,
UIntType a,
UIntType c,
UIntType m
> class linear_congruential_engine;
```

`linear_congruential_engine` is a random number engine based on [Linear congruential generator](https://en.wikipedia.org/wiki/Linear congruential generator) (LCG).

## Template parameters


### Parameters

- `a` - the multiplier term
- `c` - the increment term
- `m` - the modulus term
When `m` is not zero, if `1=a >= m` or `1=c >= m` is `true`, the program is ill-formed.

## Generator properties

The `size` of the states of `linear_congruential_engine` is `1`, each of them consists of a single integer.
The actual modulus  is defined as follows:
* If `m` is not zero,  is `m`.
* If `m` is zero,  is the value of `std::numeric_limits<result_type>::max()` plus `1` (which means  need not be representable as `result_type`).
The `transition algorithm` of `linear_congruential_engine` is ) = (a·x+c) mod m.
The `generation algorithm` of `linear_congruential_engine` is ) = (a·x+c) mod m.
The pseudo-random number generated with the current state is also the successor state.

## Predefined specializations

The following specializations define the random number engine with two commonly used parameter sets:


| Item | Description |
|------|-------------|
| random | |
| **Type** | Definition |
| cpp/numeric/random/dsc minstd_rand0 | (see dedicated page) |
| cpp/numeric/random/dsc minstd_rand | (see dedicated page) |


## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Data members


## Member functions


#### Construction and Seeding

| cpp/numeric/random/engine/dsc constructor|linear_congruential_engine | (see dedicated page) |
| cpp/numeric/random/engine/dsc seed|linear_congruential_engine | (see dedicated page) |

#### Generation

| cpp/numeric/random/engine/dsc operator()|linear_congruential_engine | (see dedicated page) |
| cpp/numeric/random/engine/dsc discard|linear_congruential_engine | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/engine/dsc min|linear_congruential_engine | (see dedicated page) |
| cpp/numeric/random/engine/dsc max|linear_congruential_engine | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/engine/dsc operator cmp|linear_congruential_engine | (see dedicated page) |
| cpp/numeric/random/engine/dsc operator ltltgtgt|linear_congruential_engine | (see dedicated page) |


## Example

