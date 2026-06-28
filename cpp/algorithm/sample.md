---
title: std::sample
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/sample
---

ddcl|header=algorithm|since=c++17|
template< class PopulationIt, class SampleIt, class Distance, class URBG >
SampleIterator sample( PopulationIt first, PopulationIt last,
SampleIt out, Distance n, URBG&& g );
Selects `n` elements from the sequence [first, last) (without replacement) such that each possible sample has equal probability of appearance, and writes those selected elements into the output iterator `out`. Random numbers are generated using the random number generator `g`.
If `n` is greater than the number of elements in the sequence, selects all elements in the sequence.
The algorithm is stable (preserves the relative order of the selected elements) only if `PopulationIt` meets the requirements of *ForwardIterator*.
If <sup>(until C++20)</sup> the value type of `first`<sup>(since C++20)</sup> `*first` is not writable to `out`, the program is ill-formed.
If any of the following conditions is satisfied, the behavior is undefined:
* `out` is in [first, last).
* `PopulationIt` does not meet the requirements of *InputIterator*.
* `SampleIt` does not meet the requirements of *OutputIterator*.
* All following conditions are satisfied:
rev|until=c++23|
:* `PopulationIt` does not meet the requirements of *ForwardIterator*.
rev|since=c++23|
:* `PopulationIt` does not model .
:* `SampleIt` does not meet the requirements of *RandomAccessIterator*.
* Given the type `T` as `std::remove_reference_t<URBG>`, any of the following conditions is satisfied:
:* `T` does not meet the requirements of *UniformRandomBitGenerator*.
rrev|until=c++20|
:* The return type of `T` is not convertible to `Distance`.

## Parameters


### Parameters

- `out` - the output iterator where the samples are written
- `n` - number of samples to make
- `g` - the random number generator used as the source of randomness

**Type requirements:**


## Return value

Returns a copy of `out` after the last sample that was output, that is, end of the sample range.

## Complexity

Linear in `std::distance(first, last)`.

## Possible implementation

See the implementations in [https://github.com/gcc-mirror/gcc/blob/14d8a5ae472ca5743016f37da2dd4770d83dea21/libstdc%2B%2B-v3/include/bits/stl_algo.h#L5743-L5869 libstdc++], [https://github.com/llvm/llvm-project/blob/f221d905b131158cbe3cbc4320d1ecd1376c3f22/libcxx/include/__algorithm/sample.h libc++] and [https://github.com/microsoft/STL/blob/472161105d596192194d4715ccad307c6c163b4a/stl/inc/algorithm#L4518-L4600 MSVC STL].

## Notes

This function may implement selection sampling or [reservoir sampling](https://en.wikipedia.org/wiki/reservoir sampling).

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <random>
#include <string>

int main()
{
    std::string in {"ABCDEFGHIJK"}, out;
    std::sample(in.begin(), in.end(), std::back_inserter(out), 4,
                std::mt19937 {std::random_device{}()});
    std::cout << "Four random letters out of " << in << " : " << out << '\n';
}
```


**Output:**
```
Four random letters out of ABCDEFGHIJK: EFGK
```


## See also


| cpp/algorithm/dsc random_shuffle | (see dedicated page) |
| cpp/algorithm/ranges/dsc sample | (see dedicated page) |

