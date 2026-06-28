---
title: std::linear_congruential_engine::linear_congruential_engine
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/linear_congruential_engine/linear_congruential_engine
---


```cpp
dcl|num=1|since=c++11|
linear_congruential_engine() : linear_congruential_engine(default_seed) {}
dcl|num=2|since=c++11|
explicit linear_congruential_engine( result_type value );
dcla|num=3|since=c++11|
template< class SeedSeq >
explicit linear_congruential_engine( SeedSeq& seq );
|
linear_congruential_engine( const linear_congruential_engine& other );
```

Constructs the pseudo-random number engine.
1. The default constructor.
* If the default-constructed engine is of type `std::minstd_rand0`, the 10000th consecutive invocation of it produces the value `1043618065`.
* If the default-constructed engine is of type `std::minstd_rand`, the 10000th consecutive invocation of it produces the value `399268537`.
2. Constructs the engine with a seed value `value`. The engine's initial `state` is determined as follows:
* If `1=c % m == 0` and `1=value % m == 0` are both `true`, the state is `1`.
* Otherwise, the state is `value % m`.
3. Constructs the engine with a seed sequence `seq`. Given `std::size_t(std::log2(m) / 32) + 1` as `k`, the engine's initial `state` is determined as follows:
# Creates an invented array object `a` of length `k + 3`.
# Calls `seq.generate(a + 0, a + k + 3)`.
# Let `S` be mathjax-or|1=\(\scriptsize (\sum^{k-1}_{j=0} a_{j+3} \cdot 2^{32j}) \mod m \)|2=(∑ a·2) mod m.
# If both `1=c % m == 0` and `1=S == 0` are `true`, sets the engine's state to `1`. Otherwise, sets the engine’s state to `S`.
@@ .
4. The copy constructor. Upon construction, `1=*this == other` is `true`.

## Parameters


### Parameters

- `value` - seed value to use in the initialization of the internal state
- `seq` - seed sequence to use in the initialization of the internal state

## Complexity

@1,2@ Constant.
3. Same as the complexity of the `seq.generate` call.
4. Constant.

## Exceptions

3. If `SeedSeq` is not `std::seed_seq`, throws the exceptions thrown by the `seq.generate` call.

## Defect reports


## See also


| cpp/numeric/random/engine/dsc seed|linear_congruential_engine | (see dedicated page) |

