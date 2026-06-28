---
title: std::independent_bits_engine
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/independent_bits_engine
---

ddcl|header=random|since=c++11|
template<
class Engine,
std::size_t W,
class UIntType
> class independent_bits_engine;
is a random number engine adaptor that produces random numbers with different number of bits than that of the wrapped engine.

## Template parameters


### Parameters

- `Engine` - the type of the wrapped engine
- `W` - the number of bits the generated numbers should have
- `UIntType` - the type of the generated random numbers. The effect is undefined unless the parameter is cv-unqualified and is one of `unsigned short`, `unsigned int`, `unsigned long`, or `unsigned long long`.

**Type requirements:**

- `Engine`

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/adaptor/dsc constructor|independent_bits_engine | (see dedicated page) |
| cpp/numeric/random/adaptor/dsc seed|independent_bits_engine | (see dedicated page) |
| cpp/numeric/random/adaptor/dsc base|independent_bits_engine | (see dedicated page) |

#### Generation

| cpp/numeric/random/adaptor/dsc operator()|independent_bits_engine | (see dedicated page) |
| cpp/numeric/random/adaptor/dsc discard|independent_bits_engine | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/adaptor/dsc min|independent_bits_engine | (see dedicated page) |
| cpp/numeric/random/adaptor/dsc max|independent_bits_engine | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/adaptor/dsc operator_cmp|independent_bits_engine | (see dedicated page) |
| cpp/numeric/random/adaptor/dsc operator_ltltgtgt|independent_bits_engine | (see dedicated page) |


## Example

