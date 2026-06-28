---
title: std::counting_semaphore::max
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/counting_semaphore/max
---


```cpp
dcl|since=c++20|
constexpr std::ptrdiff_t max() noexcept;
```

Returns the internal counter's maximum possible value, which is greater than or equal to `LeastMaxValue`.

## Return value

The internal counter's maximum possible value, as a `std::ptrdiff_t`.

## Notes

For specialization `binary_semaphore`, `LeastMaxValue` is equal to `1`.
As its name indicates, the `LeastMaxValue` is the ''minimum'' max value, not the ''actual'' max value. Thus `max()` can yield a number larger than `LeastMaxValue`.
