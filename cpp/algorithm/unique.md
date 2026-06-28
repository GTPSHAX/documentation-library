---
title: std::unique
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/unique
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class ForwardIt >
ForwardIt unique( ForwardIt first, ForwardIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt >
ForwardIt unique( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last );
dcla|num=3|notes=<sup>(constexpr C++20)</sup>|
template< class ForwardIt, class BinaryPred >
ForwardIt unique( ForwardIt first, ForwardIt last, BinaryPred p );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt, class BinaryPred >
ForwardIt unique( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, BinaryPred p );
```

Removes all except the first element from every consecutive group of equivalent elements from the range [first, last) and returns a past-the-end iterator for the new end of the range.
1. Elements are compared using `1=operator==`.
@@ If `1=operator==` does not establish an [equivalence relation](https://en.wikipedia.org/wiki/equivalence relation), the behavior is undefined.
3. Elements are compared using the given binary predicate `p`.
@@ If `p` does not establish an equivalence relation, the behavior is undefined.
@2,4@ Same as , but executed according to `policy`.
@@

## Explanation

Removing is done by shifting the elements in the range in such a way that the elements that are not to be removed appear in the beginning of the range.
* Shifting is done by <sup>(until C++11)</sup> <sup>(since C++11)</sup> .
* The removing operation is stable: the relative order of the elements not to be removed stays the same.
* The underlying sequence of [first, last) is not shortened by the removing operation. Given `result` as the returned iterator:
:* All iterators in [result, last) are still dereferenceable.
rrev|since=c++11|
:* Each element of [result, last) has a valid but unspecified state, because move assignment can eliminate elements by moving from elements that were originally in that range.

## Parameters


### Parameters

- `policy` - execution policy

**Type requirements:**

- `ForwardIt`

## Return value

A `ForwardIt` to the new end of the range.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@ Exactly  comparisons using `1=operator==`.
@3,4@ Exactly  applications of the predicate `p`.

## Exceptions


## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/7f2f4b87910506effb8dffffc60eeb2451573126/libstdc%2B%2B-v3/include/bits/stl_algo.h#L919-L1000 libstdc++], [https://github.com/llvm/llvm-project/blob/5ba396011377bdf4086757d56cd48fc7d3c9f2ad/libcxx/include/__algorithm/unique.h libc++], and [https://github.com/microsoft/STL/blob/472161105d596192194d4715ccad307c6c163b4a/stl/inc/algorithm#L3804-L3848 MSVC STL].
eq impl
|title1=unique (1)|ver1=1|1=
template<class ForwardIt>
ForwardIt unique(ForwardIt first, ForwardIt last)
{
if (first == last)
return last;
ForwardIt result = first;
while (++first != last)
if (!(*result == *first) && ++result != first)
*result = std::move(*first);
return ++result;
}
|title2=unique (3)|ver2=3|2=
template<class ForwardIt, class BinaryPredicate>
ForwardIt unique(ForwardIt first, ForwardIt last, BinaryPredicate p)
{
if (first == last)
return last;
ForwardIt result = first;
while (++first != last)
if (!p(*result, *first) && ++result != first)
*result = std::move(*first);
return ++result;
}

## Notes

A call to `unique` is typically followed by a call to a container's `erase` member function to actually remove elements from the container.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main()
{
    // a vector containing several duplicate elements
    std::vector<int> v{1, 2, 1, 1, 3, 3, 3, 4, 5, 4};
    auto print = [&](int id)
    {
        std::cout << "@" << id << ": ";
        for (int i : v)
            std::cout << i << ' ';
        std::cout << '\n';
    };
    print(1);

    // remove consecutive (adjacent) duplicates
    auto last = std::unique(v.begin(), v.end());
    // v now holds {1 2 1 3 4 5 4 x x x}, where 'x' is indeterminate
    v.erase(last, v.end());
    print(2);

    // sort followed by unique, to remove all duplicates
    std::sort(v.begin(), v.end()); // {1 1 2 3 4 4 5}
    print(3);

    last = std::unique(v.begin(), v.end());
    // v now holds {1 2 3 4 5 x x}, where 'x' is indeterminate
    v.erase(last, v.end());
    print(4);
}
```


**Output:**
```
@1: 1 2 1 1 3 3 3 4 5 4
@2: 1 2 1 3 4 5 4
@3: 1 1 2 3 4 4 5
@4: 1 2 3 4 5
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-202 | C++98 | the behavior was unclear if the elements are<br>compared using a non-equivalence relation | the behavior is<br>undefined in this case |


## See also


| cpp/algorithm/dsc adjacent_find | (see dedicated page) |
| cpp/algorithm/dsc unique_copy | (see dedicated page) |
| cpp/algorithm/dsc remove | (see dedicated page) |
| cpp/container/dsc unique|list | (see dedicated page) |
| cpp/container/dsc unique|forward_list | (see dedicated page) |
| cpp/algorithm/ranges/dsc unique | (see dedicated page) |

