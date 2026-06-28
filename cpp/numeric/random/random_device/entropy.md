---
title: std::random_device::entropy
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/random_device/entropy
---

ddcl|since=c++11|1=
double entropy() const noexcept;
Obtains an estimate of the random number device entropy, which is a floating-point value between $0$ and $log (which is equal to `std::numeric_limits<unsigned int>::digits`). If the device has $n$ states whose individual probabilities are $P, the device entropy $S$ is defined as
$1=S = −∑
A deterministic random number generator (e.g. a pseudo-random engine) has entropy zero.

## Return value

The value of the device entropy, or zero if not applicable.

## Notes

This function is not fully implemented in some standard libraries. For example, [https://github.com/llvm-mirror/libcxx/blob/master/src/random.cpp#L174 LLVM libc++] prior to version 12 always returns zero even though the device is non-deterministic. In comparison, Microsoft Visual C++ implementation always returns `32`, and [https://github.com/boostorg/random/blob/master/src/random_device.cpp#L242 boost.random] returns `10`.
The entropy of the Linux kernel device `/dev/urandom` may be obtained using [https://man7.org/linux/man-pages/man4/random.4.html `ioctl RNDGETENTCNT`] &mdash; that is what `std::random_device::entropy()` in [https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/src/c%2B%2B11/random.cc#L188 GNU libstdc++] uses as of version 8.1.

## Example


### Example

```cpp
#include <iostream>
#include <random>

int main()
{
    std::random_device rd;
    std::cout << rd.entropy() << '\n';
}
```


**Output:**
```
32
```

