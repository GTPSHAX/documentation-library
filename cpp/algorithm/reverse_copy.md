---
title: std::reverse_copy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/reverse_copy
---


```cpp
**Header:** `<`algorithm`>`
|
template< class BidirIt, class OutputIt >
OutputIt reverse_copy( BidirIt first, BidirIt last,
OutputIt d_first );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class BidirIt, class ForwardIt >
ForwardIt reverse_copy( ExecutionPolicy&& policy,
BidirIt first, BidirIt last,
ForwardIt d_first );
```

1. Given  as `std::distance(first, last)`. Copies the elements from the range [first, last) (source range) to another range of  elements beginning at `d_first` (destination range) in such a way that the elements in the destination range are in reverse order.
@@ Behaves as if by executing the assignment `1=*(d_first + N - 1 - i) = *(first + i)` once for each integer `i` in [0, N).
@@ If source and destination ranges overlap, the behavior is undefined.
2. Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `[3=to copy, range=source}})` - 
- `d_first` - the beginning of the destination range

**Type requirements:**

- `BidirIt`
- `OutputIt`
- `ForwardIt`

## Return value

Output iterator to the element past the last element copied.

## Complexity

Exactly  assignments.

## Exceptions


## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/14d8a5ae472ca5743016f37da2dd4770d83dea21/libstdc%2B%2B-v3/include/bits/stl_algo.h#L1170-L1190 libstdc++], [https://github.com/llvm/llvm-project/tree/134723edd5bf06ff6ec8aca7b87c56e5bd70ccae/libcxx/include/__algorithm/reverse_copy.h libc++], and [https://github.com/microsoft/STL/blob/472161105d596192194d4715ccad307c6c163b4a/stl/inc/algorithm#L4184-L4229 MSVC STL].
eq fun|1=
template<class BidirIt, class OutputIt>
constexpr // since C++20
OutputIt reverse_copy(BidirIt first, BidirIt last, OutputIt d_first)
{
for (; first != last; ++d_first)
*d_first = *(--last);
return d_first;
}

## Notes

Implementations (e.g. [https://github.com/microsoft/STL/blob/main/stl/src/vector_algorithms.cpp MSVC STL]) may enable vectorization when the both iterator types satisfy *ContiguousIterator* and have the same value type, and the value type is *TriviallyCopyable*.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main()
{
    auto print = [](const std::vector<int>& v)
    {
        for (const auto& value : v)
            std::cout << value << ' ';
        std::cout << '\n';
    };

    std::vector<int> v{1, 2, 3};
    print(v);

    std::vector<int> destination(3);
    std::reverse_copy(std::begin(v), std::end(v), std::begin(destination));
    print(destination);

    std::reverse_copy(std::rbegin(v), std::rend(v), std::begin(destination));
    print(destination);
}
```


**Output:**
```
1 2 3 
3 2 1 
1 2 3
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2150 | C++98 | only one element was required to be assigned | corrected the requirement |


## See also


| cpp/algorithm/dsc reverse | (see dedicated page) |
| cpp/algorithm/ranges/dsc reverse_copy | (see dedicated page) |

