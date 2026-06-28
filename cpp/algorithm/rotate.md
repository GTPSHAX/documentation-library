---
title: std::rotate
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/rotate
---


```cpp
**Header:** `<`algorithm`>`
|
template< class ForwardIt >
ForwardIt rotate( ForwardIt first, ForwardIt middle, ForwardIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt >
ForwardIt rotate( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt middle, ForwardIt last );
```

1. Performs a left rotation on a range of elements.
@@ Specifically, `std::rotate` swaps the elements in the range [first, last) in such a way that the elements in [first, middle) are placed after the elements in [middle, last) while the orders of the elements in both ranges are preserved.
2. Same as , but executed according to `policy`.
@@
If any of the following conditions is satisfied, the behavior is undefined:
* [first, middle) or [middle, last) is not a valid range.
rev|until=c++11|
* The type of `*first` is not *Swappable*.
rev|since=c++11|
* `ForwardIt` is not *ValueSwappable*.
* The type of `*first` is not *MoveConstructible*.
* The type of `*first` is not *MoveAssignable*.

## Parameters


### Parameters

- `middle` - the element that should appear at the beginning of the rotated range
- `policy` - execution policy

**Type requirements:**

- `ForwardIt`

## Return value

The iterator to the element originally referenced by `*first`, i.e. the `std::distance(middle, last)` next iterator of `first`.

## Complexity

At most `std::distance(first, last)` swaps.

## Exceptions


## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/14d8a5ae472ca5743016f37da2dd4770d83dea21/libstdc%2B%2B-v3/include/bits/stl_algo.h#L1213-L1416 libstdc++], [https://github.com/llvm/llvm-project/tree/6adbc83ee9e46b476e0f75d5671c3a21f675a936/libcxx/include/__algorithm/rotate.h libc++], and [https://github.com/microsoft/STL/blob/472161105d596192194d4715ccad307c6c163b4a/stl/inc/xutility#L5392-L5446 MSVC STL].
eq fun|1=
template<class ForwardIt>
constexpr // since C++20
ForwardIt rotate(ForwardIt first, ForwardIt middle, ForwardIt last)
{
if (first == middle)
return last;
if (middle == last)
return first;
ForwardIt write = first;
ForwardIt next_read = first; // read position for when “read” hits “last”
for (ForwardIt read = middle; read != last; ++write, ++read)
{
if (write == next_read)
next_read = read; // track where “first” went
std::iter_swap(write, read);
}
// rotate the remaining sequence into place
rotate(write, next_read, last);
return write;
}

## Notes

`std::rotate` has better efficiency on common implementations if `ForwardIt` satisfies *BidirectionalIterator* or (better) *RandomAccessIterator*.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

auto print = [](const auto remark, const auto& v)
{
    std::cout << remark;
    for (auto n : v)
        std::cout << n << ' ';
    std::cout << '\n';
};

int main()
{
    std::vector<int> v{2, 4, 2, 0, 5, 10, 7, 3, 7, 1};
    print("before sort:\t\t", v);

    // insertion sort
    for (auto i = v.begin(); i != v.end(); ++i)
        std::rotate(std::upper_bound(v.begin(), i, *i), i, i + 1);
    print("after sort:\t\t", v);

    // simple rotation to the left
    std::rotate(v.begin(), v.begin() + 1, v.end());
    print("simple rotate left:\t", v);

    // simple rotation to the right
    std::rotate(v.rbegin(), v.rbegin() + 1, v.rend());
    print("simple rotate right:\t", v);
}
```


**Output:**
```
before sort:		2 4 2 0 5 10 7 3 7 1
after sort:		0 1 2 2 3 4 5 7 7 10
simple rotate left:	1 2 2 3 4 5 7 7 10 0
simple rotate right:	0 1 2 2 3 4 5 7 7 10
```


## Defect reports


## See also


| cpp/algorithm/dsc rotate_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc rotate | (see dedicated page) |

