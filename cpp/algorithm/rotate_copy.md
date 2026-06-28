---
title: std::rotate_copy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/rotate_copy
---


```cpp
**Header:** `<`algorithm`>`
|
template< class ForwardIt, class OutputIt >
OutputIt rotate_copy( ForwardIt first, ForwardIt middle,
ForwardIt last, OutputIt d_first );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2 >
ForwardIt2 rotate_copy( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 middle,
ForwardIt1 last, ForwardIt2 d_first );
```

Copies the ''left rotation'' of [first, last) to `d_first`.
1. Copies the elements from the range [first, last), such that in the destination range beginning at `d_first`, the elements in [first, middle) are placed after the elements in [middle, last) while the orders of the elements in both ranges are preserved.
2. Same as , but executed according to `policy`.
@@
If any of the following conditions is satisfied, the behavior is undefined:
* [first, middle) or [middle, last) is not a valid range.
* The source and destination ranges overlap.

## Parameters


### Parameters

- `[3=to copy, range=source}})` - 
- `middle` - an iterator to an element in [first, last) that should appear at the beginning of the new range
- `d_first` - beginning of the destination range
- `policy` - execution policy

**Type requirements:**

- `ForwardIt, ForwardIt1, ForwardIt2`
- `OutputIt`

## Return value

Output iterator to the element past the last element copied.

## Complexity

Exactly `std::distance(first, last)` assignments.

## Exceptions


## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/14d8a5ae472ca5743016f37da2dd4770d83dea21/libstdc%2B%2B-v3/include/bits/stl_algo.h#L1440-L1455 libstdc++], [https://github.com/llvm/llvm-project/tree/f221d905b131158cbe3cbc4320d1ecd1376c3f22/libcxx/include/__algorithm/rotate_copy.h libc++], and [https://github.com/microsoft/STL/blob/472161105d596192194d4715ccad307c6c163b4a/stl/inc/algorithm#L4438-L4459 MSVC STL].
eq fun|1=
template<class ForwardIt, class OutputIt>
constexpr // since C++20
OutputIt rotate_copy(ForwardIt first, ForwardIt middle,
ForwardIt last, OutputIt d_first)
{
d_first = std::copy(middle, last, d_first);
return std::copy(first, middle, d_first);
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

int main()
{
    std::vector<int> src{1, 2, 3, 4, 5};
    std::vector<int> dest(src.size());
    auto pivot = std::find(src.begin(), src.end(), 3);

    std::rotate_copy(src.begin(), pivot, src.end(), dest.begin());
    for (int i : dest)
        std::cout << i << ' ';
    std::cout << '\n';

    // copy the rotation result directly to the std::cout
    pivot = std::find(dest.begin(), dest.end(), 1);
    std::rotate_copy(dest.begin(), pivot, dest.end(),
                     std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';
}
```


**Output:**
```
3 4 5 1 2
1 2 3 4 5
```


## See also


| cpp/algorithm/dsc rotate | (see dedicated page) |
| cpp/algorithm/ranges/dsc rotate_copy | (see dedicated page) |

