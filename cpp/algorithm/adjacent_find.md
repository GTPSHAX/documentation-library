---
title: std::adjacent_find
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/adjacent_find
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|constexpr=c++20|
template< class ForwardIt >
ForwardIt adjacent_find( ForwardIt first, ForwardIt last );
dcla|num=2|constexpr=c++20|
template< class ForwardIt, class BinaryPred >
ForwardIt adjacent_find( ForwardIt first, ForwardIt last,
BinaryPred p );
dcl|num=3|since=c++17|
template< class ExecutionPolicy, class ForwardIt >
ForwardIt adjacent_find( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class BinaryPred >
ForwardIt adjacent_find( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
BinaryPred p );
```

Searches the source range [first, last) for the first pair of adjacent elements satisfying the specified condition.
1. Searches for the first pair of adjacent equal elements. Equality is determined by `1=operator==`.
2. Searches for the first pair of adjacent elements satisfying the given binary predicate `p`.
@3,4@ Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `[range=source, simple=yes}})` - 
- `policy` - execution policy

**Type requirements:**

- `ForwardIt`
- `BinaryPred`

## Return value

The first iterator `iter` in the source range such that the following expression evaluates to `true`:
@1,3@ `1=bool(*iter == *std::next(iter))`
@2,4@ `bool(p(*iter, std::next(iter))`
If no such iterator is found, `last` is returned.

## Complexity

Given `result` as the return value of `adjacent_find`,  as `std::distance(first, result)` and  as `std::distance(first, last)`:
1. Exactly  comparisons using `1=operator==`.
2. Exactly  applications of the predicate `p`.
3. } comparisons using `1=operator==`.
4. } applications of the predicate `p`.

## Exceptions

@3,4@

## Possible implementation

eq impl
|title1=adjacent_find (1)|ver1=1|1=
template<class ForwardIt>
ForwardIt adjacent_find(ForwardIt first, ForwardIt last)
{
if (first == last)
return last;
ForwardIt next = first;
++next;
for (; next != last; ++next, ++first)
if (*first == *next)
return first;
return last;
}
|title2=adjacent_find (2)|ver2=2|2=
template<class ForwardIt, class BinaryPred>
ForwardIt adjacent_find(ForwardIt first, ForwardIt last, BinaryPred p)
{
if (first == last)
return last;
ForwardIt next = first;
++next;
for (; next != last; ++next, ++first)
if (p(*first, *next))
return first;
return last;
}

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> v1{0, 1, 2, 3, 40, 40, 41, 41, 5};

    auto i1 = std::adjacent_find(v1.begin(), v1.end());

    if (i1 == v1.end())
        std::cout << "No matching adjacent elements\n";
    else
        std::cout << "The first adjacent pair of equal elements is at "
                  << std::distance(v1.begin(), i1) << ", *i1 = "
                  << *i1 << '\n';

    auto i2 = std::adjacent_find(v1.begin(), v1.end(), std::greater<int>());
    if (i2 == v1.end())
        std::cout << "The entire vector is sorted in ascending order\n";
    else
        std::cout << "The last element in the non-decreasing subsequence is at "
                  << std::distance(v1.begin(), i2) << ", *i2 = " << *i2 << '\n';
}
```


**Output:**
```
The first adjacent pair of equal elements is at 4, *i1 = 40
The last element in the non-decreasing subsequence is at 7, *i2 = 41
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-240 | C++98 | the complexity requirement was unclear | made clear |


## See also


| cpp/algorithm/ranges/dsc adjacent_find | (see dedicated page) |
| cpp/algorithm/dsc unique | (see dedicated page) |

