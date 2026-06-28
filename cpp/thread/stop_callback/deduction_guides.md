---
title: deduction guides for std::stop_callback
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_callback/deduction_guides
---


# deduction guides for tt|std::stop_callback


```cpp
**Header:** `<`stop_token`>`
dcl|since=c++20|
template< class Callback >
stop_callback( std::stop_token, Callback ) -> stop_callback<Callback>;
```

One deduction guide is provided for `std::stop_callback` to permit deduction from argument of invocable types.

## Example

