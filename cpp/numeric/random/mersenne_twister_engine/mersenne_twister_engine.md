---
title: std::mersenne_twister_engine::mersenne_twister_engine
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/mersenne_twister_engine/mersenne_twister_engine
---


```cpp
dcl|num=1|since=c++11|
mersenne_twister_engine() : mersenne_twister_engine(default_seed) {}
dcl|num=2|since=c++11|
explicit mersenne_twister_engine( result_type value );
dcl|num=3|since=c++11|
template< class SeedSeq >
explicit mersenne_twister_engine( SeedSeq& seq );
|
mersenne_twister_engine( const mersenne_twister_engine& other );
```

Constructs the pseudo-random number engine.
1. The default constructor.
* If the default-constructed engine is of type `std::mt19937`, the 10000th consecutive invocation of it produces the value `4123659995`.
* If the default-constructed engine is of type `std::mt19937_64`, the 10000th consecutive invocation of it produces the value `9981545732273789042`.
2. Constructs the engine with a seed value `value`. Given  as `p`, the engine's initial `state` is determined as follows:
# Sets } to `value % p`.
# For each integer `i` in , sets  to mathjax-or|\(\scriptsize [f \cdot (X_{i-1}\ \mathsf{xor}\ (X_{i-1}\ \mathsf{rshift}\ (w-2)))+i \mod n] \mod p \)|[f·(X xor (X rshift (w-2)))+i mod n] mod p, where } and } stand for built-in bitwise XOR and bitwise right-shift respectively.
3. Constructs the engine with a seed sequence `seq`. Given `std::size_t(w / 32) + 1` as `k`, the engine's initial `state` is determined as follows:
# Creates an invented array object `a` of length `n * k`.
# Calls `seq.generate(a + 0, a + n * k)`.
# For each integer `i` in , sets } to mathjax-or|1=\(\scriptsize (\sum^{k-1}_{j=0} a_{k(i+n)+j} \cdot 2^{32j}) \mod 2^w \)|2=(∑ a·2) mod 2.
# If the most significant `w − r` bits of } are zero, and if each of the other resulting } is `0`, changes } to }.
@@ .
4. The copy constructor. Upon construction, `1=*this == other` is `true`.

## Parameters


### Parameters

- `value` - seed value to use in the initialization of the internal state
- `seq` - seed sequence to use in the initialization of the internal state

## Complexity

@1,2@ .
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
    std::mt19937 gen32; // overload (1)
    std::mt19937_64 gen64; // overload (1)
    gen32.discard(10000 - 1);
    gen64.discard(10000 - 1);
    assert(gen32() == 4123659995);
    assert(gen64() == 9981545732273789042ull);
}
```


## Defect reports


## See also


| cpp/numeric/random/engine/dsc seed|mersenne_twister_engine | (see dedicated page) |

