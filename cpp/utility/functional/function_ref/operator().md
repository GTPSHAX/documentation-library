---
title: std::function_ref::operator()
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function_ref/operator()
---

ddcl|since=c++26|
R operator()( Args... args ) const noexcept(/*noex*/);
Invokes the stored  with  as its first parameter and the rest of the parameters `args`. The `/*noex*/` part of `operator()` is identical to those of the template parameter of `std::function_ref`.
Equivalent to .

## Parameters


### Parameters

- `args` - rest parameters to pass to the stored 

## Return value

.

## Exceptions

Propagates the exception thrown by the underlying function call.

## Example

