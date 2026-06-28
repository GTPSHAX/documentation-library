---
title: std::random_device::operator()
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/random_device/operator()
---

ddcl | since=c++11 | 1=
result_type operator()();
Generates a non-deterministic uniformly-distributed random value.

## Parameters

(none)

## Return value

A random number uniformly distributed in [`min()`, `max()`].

## Exceptions

Throws an implementation-defined exception derived from `std::exception` if a random number could not be generated.

## See also

