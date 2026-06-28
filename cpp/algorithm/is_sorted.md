---
title: std::is_sorted
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/is_sorted
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|since=c++11|notes=<sup>(constexpr C++20)</sup>|
template< class ForwardIt >
bool is_sorted( ForwardIt first, ForwardIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt >
bool is_sorted( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last );
dcla|num=3|since=c++11|notes=<sup>(constexpr C++20)</sup>|
template< class ForwardIt, class Compare >
bool is_sorted( ForwardIt first, ForwardIt last, Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class Compare >
bool is_sorted( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, Compare comp );
```

Checks if the elements in range [first, last) are sorted in non-descending order.
1. Checks if the elements are `sorted` with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
3. Checks if the elements are sorted with respect to `comp`.
@2,4@ Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `policy` - execution policy
- `comp` - comparison function

**Type requirements:**

- `ForwardIt`
- `Compare`

## Return value

`true` if the elements in the range are sorted in non-descending order, `false` otherwise.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
@3,4@  applications of the comparator `comp`.

## Exceptions


## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L3184 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L3642 libc++].
eq impl
|title1=is_sorted (1)|ver1=1|1=
template<class ForwardIt>
bool is_sorted(ForwardIt first, ForwardIt last)
{
return std::is_sorted_until(first, last) == last;
}
|title2=is_sorted (3)|ver2=3|2=
template<class ForwardIt, class Compare>
bool is_sorted(ForwardIt first, ForwardIt last, Compare comp)
{
return std::is_sorted_until(first, last, comp) == last;
}

## Notes

`std::is_sorted` returns `true` for empty ranges and ranges of length one.

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <functional>
#include <iterator>
#include <vector>

int main()
{
    std::vector<int> v;
    assert(std::is_sorted(v.cbegin(), v.cend()) && "an empty range is always sorted");
    v.push_back(42);
    assert(std::is_sorted(v.cbegin(), v.cend()) && "a range of size 1 is always sorted");

    int data[] = {3, 1, 4, 1, 5};
    assert(not std::is_sorted(std::begin(data), std::end(data)));

    std::sort(std::begin(data), std::end(data));
    assert(std::is_sorted(std::begin(data), std::end(data)));
    assert(not std::is_sorted(std::begin(data), std::end(data), std::greater<>{}));
}
```


## See also


| cpp/algorithm/dsc is_sorted_until | (see dedicated page) |
| cpp/algorithm/ranges/dsc is_sorted | (see dedicated page) |

