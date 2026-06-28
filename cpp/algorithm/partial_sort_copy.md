---
title: std::partial_sort_copy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/partial_sort_copy
---


```cpp
**Header:** `<`algorithm`>`
|
template< class InputIt, class RandomIt >
RandomIt partial_sort_copy( InputIt first, InputIt last,
RandomIt d_first, RandomIt d_last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt, class RandomIt >
RandomIt partial_sort_copy( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
RandomIt d_first, RandomIt d_last );
|
template< class InputIt, class RandomIt, class Compare >
RandomIt partial_sort_copy( InputIt first, InputIt last,
RandomIt d_first, RandomIt d_last,
Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt, class RandomIt, class Compare >
RandomIt partial_sort_copy( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
RandomIt d_first, RandomIt d_last,
Compare comp );
```

Sorts some of the elements in the range [first, last) in ascending order, storing the result in the range [d_first, d_last).
At most `d_last - d_first` of the elements are placed sorted to the range [d_first, d_first + n). `n` is the number of elements to sort (`std::min(std::distance(first, last), d_last - d_first)`). The order of equal elements is not guaranteed to be preserved.
1. Elements are `sorted` with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
3. Elements are sorted with respect to `comp`.
@2,4@ Same as , but executed according to `policy`.
@@
If `*first` is not writable to `d_first`, the program is ill-formed.
If any of the following conditions is satisfied, the behavior is undefined:
rev|until=c++11|
* The type of `*d_first` is not *Swappable*.
rev|since=c++11|
* `RandomIt` is not *ValueSwappable*.
* The type of `*d_first` is not *MoveConstructible*.
* The type of `*d_first` is not *MoveAssignable*.

## Parameters


### Parameters

- `[d_first, d_last)` - 
- `policy` - execution policy
- `comp` - comparison function

**Type requirements:**

- `InputIt`
- `ForwardIt`
- `RandomIt`
- `Compare`

## Return value

An iterator to the element defining the upper boundary of the sorted range, i.e. `d_first + std::min(std::distance(first, last), d_last - d_first)`.

## Complexity

Given  as `std::distance(first, last)`,  as `d_last - d_first`:
@1,2@ Approximately  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
@3,4@ Approximately  applications of the comparator `comp`.

## Exceptions


## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L1669 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L5064 libc++].

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <string_view>
#include <type_traits>
#include <vector>

void println(std::string_view rem, const auto& v)
{
    std::cout << rem;
    if constexpr (std::is_scalar_v<std::decay_t<decltype(v)>>)
        std::cout << v;
    else
        for (int e : v)
            std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    const auto v0 = {4, 2, 5, 1, 3};
    std::vector<int> v1{10, 11, 12};
    std::vector<int> v2{10, 11, 12, 13, 14, 15, 16};
    std::vector<int>::iterator it;

    it = std::partial_sort_copy(v0.begin(), v0.end(), v1.begin(), v1.end());
    println("Writing to the smaller vector in ascending order gives: ", v1);

    if (it == v1.end())
        println("The return value is the end iterator", ' ');

    it = std::partial_sort_copy(v0.begin(), v0.end(), v2.begin(), v2.end(),
                                std::greater<int>());

    println("Writing to the larger vector in descending order gives: ", v2);
    println("The return value is the iterator to ", *it);
}
```


**Output:**
```
Writing to the smaller vector in ascending order gives: 1 2 3
The return value is the end iterator
Writing to the larger vector in descending order gives: 5 4 3 2 1 15 16
The return value is the iterator to 15
```


## Defect reports


## See also


| cpp/algorithm/dsc partial_sort | (see dedicated page) |
| cpp/algorithm/dsc sort | (see dedicated page) |
| cpp/algorithm/dsc stable_sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc partial_sort_copy | (see dedicated page) |

