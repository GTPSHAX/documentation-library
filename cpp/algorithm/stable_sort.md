---
title: std::stable_sort
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/stable_sort
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|constexpr=c++26|
template< class RandomIt >
void stable_sort( RandomIt first, RandomIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class RandomIt >
void stable_sort( ExecutionPolicy&& policy,
RandomIt first, RandomIt last );
dcla|num=3|constexpr=c++26|
template< class RandomIt, class Compare >
void stable_sort( RandomIt first, RandomIt last, Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class RandomIt, class Compare >
void stable_sort( ExecutionPolicy&& policy,
RandomIt first, RandomIt last, Compare comp );
```

Sorts the elements in the range [first, last) in non-descending order. The order of equivalent elements is guaranteed to be preserved.
1. Elements are `sorted` with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
3. Elements are sorted with respect to `comp`.
@2,4@ Same as , but executed according to `policy`.
@@
If any of the following conditions is satisfied, the behavior is undefined:
rev|until=c++11|
* The type of `*first` is not *Swappable*.
rev|since=c++11|
* `RandomIt` is not *ValueSwappable*.
* The type of `*first` is not *MoveConstructible*.
* The type of `*first` is not *MoveAssignable*.

## Parameters


### Parameters

- `policy` - execution policy
- `comp` - comparison function

**Type requirements:**

- `RandomIt`
- `Compare`

## Complexity

Given  as `last - first`:
@1,2@  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|} if enough extra memory is available, otherwise } comparisons.
@3,4@  applications of the comparator `comp` if enough extra memory is available, otherwise } applications.

## Exceptions


## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L4977 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L4696 libc++].

## Notes

This function attempts to allocate a temporary buffer equal in size to the sequence to be sorted. If the allocation fails, the less efficient algorithm is chosen.

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <vector>

struct Employee
{
    int age;
    std::string name; // Does not participate in comparisons
};

bool operator<(const Employee& lhs, const Employee& rhs)
{
    return lhs.age < rhs.age;
}

#if __cpp_lib_constexpr_algorithms >= 202306L
consteval auto get_sorted()
{
    auto v = std::array{3, 1, 4, 1, 5, 9};
    std::stable_sort(v.begin(), v.end());
    return v;
}
static_assert(std::ranges::is_sorted(get_sorted()));
#endif

int main()
{
    std::vector<Employee> v{<!---->{108, "Zaphod"}, {32, "Arthur"}, {108, "Ford"}<!---->};

    std::stable_sort(v.begin(), v.end());

    for (const Employee& e : v)
        std::cout << e.age << ", " << e.name << '\n';
}
```


**Output:**
```
32, Arthur
108, Zaphod
108, Ford
```


## See also


| cpp/algorithm/dsc sort | (see dedicated page) |
| cpp/algorithm/dsc partial_sort | (see dedicated page) |
| cpp/algorithm/dsc stable_partition | (see dedicated page) |
| cpp/algorithm/ranges/dsc stable_sort | (see dedicated page) |

