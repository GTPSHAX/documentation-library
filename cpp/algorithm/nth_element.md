---
title: std::nth_element
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/nth_element
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|constexpr=c++20|
template< class RandomIt >
void nth_element( RandomIt first, RandomIt nth, RandomIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class RandomIt >
void nth_element( ExecutionPolicy&& policy,
RandomIt first, RandomIt nth, RandomIt last );
dcla|num=3|constexpr=c++20|
template< class RandomIt, class Compare >
void nth_element( RandomIt first, RandomIt nth, RandomIt last,
Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class RandomIt, class Compare >
void nth_element( ExecutionPolicy&& policy,
RandomIt first, RandomIt nth, RandomIt last,
Compare comp );
```

`nth_element` rearranges elements in [first, last) such that after the rearrangement:
* The element pointed at by `nth` is changed to whatever element would occur in that position if [first, last) were sorted.
* For every iterator `i` in [first, nth) and every iterator `j` in [nth, last), the following condition is met:
:@1,2@ <sup>(until C++20)</sup> `bool(*j < *i)`rev inl|since=c++20|} is `false`.
:@3,4@ `bool(comp(*j, *i))` is `false`.
1. Elements are hypothetically `sorted` with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
3. Elements are hypothetically sorted with respect to `comp`.
@2,4@ Same as , but executed according to `policy`.
@@
If any of the following conditions is satisfied, the behavior is undefined:
* [first, nth) or [nth, last) is not a valid range.
rev|until=c++11|
* The type of `*first` is not *Swappable*.
rev|since=c++11|
* `RandomIt` is not *ValueSwappable*.
* The type of `*first` is not *MoveConstructible*.
* The type of `*first` is not *MoveAssignable*.

## Parameters


### Parameters

- `nth` - random access iterator defining the sort partition point
- `policy` - execution policy
- `comp` - comparison function

**Type requirements:**

- `RandomIt`
- `Compare`

## Complexity

Given  as `last - first`:
1.  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|} on average.
2.  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}, and  swaps.
3.  applications of the comparator `comp` on average.
4.  applications of the comparator `comp`, and  swaps.

## Exceptions


## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L4718 libstdc++], [https://github.com/llvm/llvm-project/blob/ed2d364/libcxx/include/__algorithm/nth_element.h libc++], and [https://github.com/microsoft/STL/blob/e97bb2b50a12816ce68cc5147b7a3a21fb68bfa3/stl/inc/algorithm#L8849-L8894 MSVC STL].

## Notes

The algorithm used is typically [Introselect](https://en.wikipedia.org/wiki/Introselect) although other [Selection algorithm](https://en.wikipedia.org/wiki/Selection algorithm) with suitable average-case complexity are allowed.

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <functional>
#include <iostream>
#include <numeric>
#include <vector>

void printVec(const std::vector<int>& vec)
{
    std::cout << "v = {";
    for (char sep[]{0, ' ', 0}; const int i : vec)
        std::cout << sep << i, sep[0] = ',';
    std::cout << "};\n";
}

int main()
{
    std::vector<int> v{5, 10, 6, 4, 3, 2, 6, 7, 9, 3};
    printVec(v);

    auto m = v.begin() + v.size() / 2;
    std::nth_element(v.begin(), m, v.end());
    std::cout << "\nThe median is " << v[v.size() / 2] << '\n';
    // The consequence of the inequality of elements before/after the Nth one:
    assert(std::accumulate(v.begin(), m, 0) < std::accumulate(m, v.end(), 0));
    printVec(v);

    // Note: comp function changed
    std::nth_element(v.begin(), v.begin() + 1, v.end(), std::greater{});
    std::cout << "\nThe second largest element is " << v[1] << '\n';
    std::cout << "The largest element is " << v[0] << '\n';
    printVec(v);
}
```


**Output:**
```
v = {5, 10, 6, 4, 3, 2, 6, 7, 9, 3};

The median is 6
v = {3, 2, 3, 4, 5, 6, 10, 7, 9, 6};

The second largest element is 9
The largest element is 10
v = {10, 9, 6, 7, 6, 3, 5, 4, 3, 2};
```


## Defect reports


## See also


| cpp/algorithm/dsc max_element | (see dedicated page) |
| cpp/algorithm/dsc min_element | (see dedicated page) |
| cpp/algorithm/dsc partial_sort_copy | (see dedicated page) |
| cpp/algorithm/dsc stable_sort | (see dedicated page) |
| cpp/algorithm/dsc sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc nth_element | (see dedicated page) |

