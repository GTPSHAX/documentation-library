---
title: std::min_element
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/min_element
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++17)</sup>|
template< class ForwardIt >
ForwardIt min_element( ForwardIt first, ForwardIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt >
ForwardIt min_element( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last );
dcla|num=3|notes=<sup>(constexpr C++17)</sup>|
template< class ForwardIt, class Compare >
ForwardIt min_element( ForwardIt first, ForwardIt last,
Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class Compare >
ForwardIt min_element( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
Compare comp );
```

Finds the smallest element in the range [first, last).
1. Elements are compared using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
3. Elements are compared using the comparison function `comp`.
@2,4@ Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `policy` - execution policy

**Type requirements:**

- `ForwardIt`

## Return value

Iterator to the smallest element in the range [first, last). If several elements in the range are equivalent to the smallest element, returns the iterator to the first such element. Returns `last` if the range is empty.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@ Exactly  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
@3,4@ Exactly  applications of the comparison function `comp`.

## Exceptions


## Possible implementation

eq impl
|title1=min_element (1)|ver1=1|1=
template<class ForwardIt>
ForwardIt min_element(ForwardIt first, ForwardIt last)
{
if (first == last)
return last;
ForwardIt smallest = first;
while (++first != last)
if (*first < *smallest)
smallest = first;
return smallest;
}
|title2=min_element (3)|ver2=3|2=
template<class ForwardIt, class Compare>
ForwardIt min_element(ForwardIt first, ForwardIt last, Compare comp)
{
if (first == last)
return last;
ForwardIt smallest = first;
while (++first != last)
if (comp(*first, *smallest))
smallest = first;
return smallest;
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> v{3, 1, -4, 1, 5, 9};

    std::vector<int>::iterator result = std::min_element(v.begin(), v.end());
    std::cout << "min element has value " << *result << " and index ["
              << std::distance(v.begin(), result) << "]\n";
}
```


**Output:**
```
min element has value -4 and index [2]
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2150 | C++98 | the iterator to the first non-greatest element was returned | corrected the return value |


## See also


| cpp/algorithm/dsc max_element | (see dedicated page) |
| cpp/algorithm/dsc minmax_element | (see dedicated page) |
| cpp/algorithm/dsc min | (see dedicated page) |
| cpp/algorithm/ranges/dsc min_element | (see dedicated page) |

