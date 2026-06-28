---
title: std::is_heap_until
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/is_heap_until
---


```cpp
**Header:** `<`algorithm`>`
|
template< class RandomIt >
RandomIt is_heap_until( RandomIt first, RandomIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class RandomIt >
RandomIt is_heap_until( ExecutionPolicy&& policy,
RandomIt first, RandomIt last );
|
template< class RandomIt, class Compare >
RandomIt is_heap_until( RandomIt first, RandomIt last, Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class RandomIt, class Compare >
RandomIt is_heap_until( ExecutionPolicy&& policy,
RandomIt first, RandomIt last, Compare comp );
```

Examines the range [first, last) and finds the largest range beginning at `first` which is a `heap`.
1. The heap property to be checked is with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
3. The heap property to be checked is with respect to `comp`.
@2,4@ Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `policy` - execution policy

**Type requirements:**

- `RandomIt`
- `Compare`

## Return value

The last iterator `it` for which range [first, it) is a heap.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
@3,4@  applications of the comparison function `comp`.

## Exceptions


## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> v{3, 1, 4, 1, 5, 9};

    std::make_heap(v.begin(), v.end());

    // probably mess up the heap
    v.push_back(2);
    v.push_back(6);

    auto heap_end = std::is_heap_until(v.begin(), v.end());

    std::cout << "all of v:  ";
    for (const auto& i : v)
        std::cout << i << ' ';
    std::cout << '\n';

    std::cout << "only heap: ";
    for (auto i = v.begin(); i != heap_end; ++i)
        std::cout << *i << ' ';
    std::cout << '\n';
}
```


**Output:**
```
all of v:  9 5 4 1 1 3 2 6
only heap: 9 5 4 1 1 3 2
```


## See also


| cpp/algorithm/dsc is_heap | (see dedicated page) |
| cpp/algorithm/dsc make_heap | (see dedicated page) |
| cpp/algorithm/dsc push_heap | (see dedicated page) |
| cpp/algorithm/dsc pop_heap | (see dedicated page) |
| cpp/algorithm/dsc sort_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc is_heap_until | (see dedicated page) |

