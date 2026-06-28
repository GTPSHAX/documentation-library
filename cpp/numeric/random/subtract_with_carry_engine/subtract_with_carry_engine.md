---
title: std::subtract_with_carry_engine::subtract_with_carry_engine
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/subtract_with_carry_engine/subtract_with_carry_engine
---


```cpp
dcl|num=1|since=c++11|
subtract_with_carry_engine() : subtract_with_carry_engine(0u) {}
dcl|num=2|since=c++11|
explicit subtract_with_carry_engine( result_type value );
dcl|num=3|since=c++11|
template< class SeedSeq >
explicit subtract_with_carry_engine( SeedSeq& seq );
|
subtract_with_carry_engine( const subtract_with_carry_engine& other );
```

Constructs the pseudo-random number engine.
1. The default constructor.
* If the default-constructed engine is of type `std::ranlux24_base`, the 10000th consecutive invocation of it produces the value `7937952`.
* If the default-constructed engine is of type `std::ranlux48_base`, the 10000th consecutive invocation of it produces the value `61839128582725`.
2. Constructs the engine with a seed value `value`. The sequence `X` of the engine's initial `state` is determined as follows:
# Constructs a `std::linear_congruential_engine<std::uint_least32_t, 40014u, 0u, 2147483563u>` object `e` with argument `1=value == 0u ? default_seed : static_cast<std::uint_least32_t>(value % 2147483563u)`.
# Let `n` be `std::size_t(w / 32) + 1`.
# Sets the values of }, ..., }, in that order. Each value  is set as specified below:
:# Successively calls `e` for `n` times, the return values are denoted as  ... }.
:# Sets  to mathjax-or|1=\(\scriptsize (\sum^{n-1}_{j=0} z_j \cdot 2^{32j}) \mod m \)|2=(∑ z·2) mod m.
@@ If } is `0`, sets the carry value `c` of the engine's initial state to `1`. Otherwise, sets `c` to `0`.
3. Constructs the engine with a seed sequence `seq`. Given `std::size_t(w / 32) + 1` as `k`, the sequence `X` of the engine's initial `state` is determined as follows:
# Creates an invented array object `a` of length `r * k`.
# Calls `seq.generate(a + 0, a + r * k)`.
# For each integer `i` in , sets } to mathjax-or|1=\(\scriptsize (\sum^{k-1}_{j=0} a_{k(i+r)+j} \cdot 2^{32j}) \mod m \)|2=(∑ a·2) mod m.
@@ If } is `0`, sets the carry value `c` of the engine's initial state to `1`. Otherwise, sets `c` to `0`.
@@ .
4. The copy constructor. Upon construction, `1=*this == other` is `true`.

## Parameters


### Parameters

- `value` - seed value to use in the initialization of the internal state
- `seq` - seed sequence to use in the initialization of the internal state

## Complexity

@1,2@ `(std::size_t(w / 32) + 1) * r` invocations of `e`.
3. Same as the complexity of the `seq.generate` call.
4. .

## Exceptions

3. If `SeedSeq` is not `std::seed_seq`, throws the exceptions thrown by the `seq.generate` call.

## Example


### Example

```cpp
#include <cassert>
#include <random>

int main()
{
    std::ranlux24_base gen24; // overload (1)
    std::ranlux48_base gen48; // overload (1)
    gen24.discard(10000 - 1);
    gen48.discard(10000 - 1);
    assert(gen24() == 7'937'952);
    assert(gen48() == 61'839'128'582'725);
}
```


## Defect reports


## See also


| cpp/numeric/random/engine/dsc seed|subtract_with_carry_engine | (see dedicated page) |

