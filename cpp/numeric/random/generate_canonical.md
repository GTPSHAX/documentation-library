---
title: std::generate_canonical
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/generate_canonical
---

ddcl|header=random|since=c++11|
template< class RealType, std::size_t Bits, class Generator >
RealType generate_canonical( Generator& g );
Generates a random floating point number in range [0, 1).
To generate enough entropy, `generate_canonical()` will call `g()` exactly  times, where mathjax-or|1= \(\small k = \max(1, \lceil \frac{b}{\log_2 R} \rceil)\) |2=k = max(1, ⌈ b / log R ⌉) and
* },
* `1=R = g.max() - g.min() + 1`.

## Parameters


### Parameters

- `g` - generator to use to acquire entropy

## Return value

Floating point value in range [0, 1).

## Exceptions

None except from those thrown by `g`.

## Notes

Some existing implementations have a bug where they may occasionally return `1.0` if `RealType` is `float`  [https://gcc.gnu.org/bugzilla/show_bug.cgi?id=63176 GCC #63176] [https://bugs.llvm.org/show_bug.cgi?id=18767 LLVM #18767] [https://github.com/microsoft/STL/issues/1074 MSVC STL #1074]. This is <!--
http://stackoverflow.com/questions/25668600/is-1-0-a-valid-random-number-->. Some implementations have avoided returning exactly 1.0 by subtracting a small value, infinitesimally skewing the statistical uniformity. The current Standard requirement is that when the random bits obtained would yield exactly 1.0, another whole round must be performed.
The specification provides no default for the number-of-bits argument, and the exact value for maximum precision is the unwieldy (e.g.) `std::numeric_limits<double>::digits`. For almost all uses, the best choice is `-1u`, with the same result.
For cases where the resulting value is close to zero, the Standard prescribes that only a fraction of the bits of entropy obtained should go into the result. The effect is that if all values generated less than, say, 0.001 are placed in a bucket, the number of different values that may appear would be many fewer than could be represented. Most implementations instead preserve as much of the obtained entropy as can be represented in the result.

## Example


### Example

```cpp
#include <iostream>
#include <random>

int main()
{
    std::random_device rd;
    std::mt19937 gen(rd());
    for (int n = 0; n < 10; ++n)
        std::cout << std::generate_canonical<double, -1u>(gen) << ' ';
    std::cout << '\n';
}
```


**Output:**
```
0.208143 0.824147 0.0278604 0.343183 0.0173263 0.864057 0.647037 0.539467 0.0583497 0.609219
```


## See also


| cpp/numeric/random/dsc uniform_real_distribution | (see dedicated page) |

