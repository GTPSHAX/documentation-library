---
title: std::partition
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/partition
---


```cpp
**Header:** `<`algorithm`>`
|
template< class ForwardIt, class UnaryPred >
ForwardIt partition( ForwardIt first, ForwardIt last, UnaryPred p );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class UnaryPred >
ForwardIt partition( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, UnaryPred p );
```

1. Reorders the elements in the range [first, last) in such a way that all elements for which the predicate `p` returns `true` precede all elements for which predicate `p` returns `false`. Relative order of the elements is not preserved.
2. Same as , but executed according to `policy`.
@@
If <sup>(until C++11)</sup> the type of `*first` is not *Swappable*<sup>(since C++11)</sup> `ForwardIt` is not *ValueSwappable*, the behavior is undefined.

## Parameters


### Parameters

- `policy` - execution policy

**Type requirements:**

- `ForwardIt`
- `UnaryPred`

## Return value

Iterator to the first element of the second group.

## Complexity

Given  as `std::distance(first, last)`:
1. Exactly  applications of `p`.
@@ At most  swaps if `ForwardIt` meets the requirements of *BidirectionalIterator*, and at most  swaps otherwise.
2.  applications of `p`.
@@  swaps.

## Exceptions


## Possible implementation

Implements overload  preserving C++11 compatibility.
eq fun|1=
template<class ForwardIt, class UnaryPred>
ForwardIt partition(ForwardIt first, ForwardIt last, UnaryPred p)
{
first = std::find_if_not(first, last, p);
if (first == last)
return first;
for (auto i = std::next(first); i != last; ++i)
if (p(*i))
{
std::iter_swap(i, first);
++first;
}
return first;
}

## Example


### Example

```cpp
#include <algorithm>
#include <forward_list>
#include <iostream>
#include <iterator>
#include <vector>

template<class ForwardIt>
void quicksort(ForwardIt first, ForwardIt last)
{
    if (first == last)
        return;

    auto pivot = *std::next(first, std::distance(first, last) / 2);
    auto middle1 = std::partition(first, last, [pivot](const auto& em)
    {
        return em < pivot;
    });
    auto middle2 = std::partition(middle1, last, [pivot](const auto& em)
    {
        return !(pivot < em);
    });

    quicksort(first, middle1);
    quicksort(middle2, last);
}

int main()
{
    std::vector<int> v{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::cout << "Original vector: ";
    for (int elem : v)
        std::cout << elem << ' ';

    auto it = std::partition(v.begin(), v.end(), [](int i) {return i % 2 == 0;});

    std::cout << "\nPartitioned vector: ";
    std::copy(std::begin(v), it, std::ostream_iterator<int>(std::cout, " "));
    std::cout << "* ";
    std::copy(it, std::end(v), std::ostream_iterator<int>(std::cout, " "));

    std::forward_list<int> fl {1, 30, -4, 3, 5, -4, 1, 6, -8, 2, -5, 64, 1, 92};
    std::cout << "\nUnsorted list: ";
    for (int n : fl)
        std::cout << n << ' ';

    quicksort(std::begin(fl), std::end(fl));
    std::cout << "\nSorted using quicksort: ";
    for (int fi : fl)
        std::cout << fi << ' ';
    std::cout << '\n';
}
```


**Output:**
```
Original vector: 0 1 2 3 4 5 6 7 8 9 
Partitioned vector: 0 8 2 6 4 * 5 3 7 1 9 
Unsorted list: 1 30 -4 3 5 -4 1 6 -8 2 -5 64 1 92 
Sorted using quicksort: -8 -5 -4 -4 1 1 1 2 3 5 6 30 64 92
```


## Defect reports


## See also


| cpp/algorithm/dsc is_partitioned | (see dedicated page) |
| cpp/algorithm/dsc stable_partition | (see dedicated page) |
| cpp/algorithm/ranges/dsc partition | (see dedicated page) |

