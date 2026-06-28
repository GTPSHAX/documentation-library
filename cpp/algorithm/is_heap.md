---
title: std::is_heap
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/is_heap
---


```cpp
**Header:** `<`algorithm`>`
|
template< class RandomIt >
bool is_heap( RandomIt first, RandomIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class RandomIt >
bool is_heap( ExecutionPolicy&& policy,
RandomIt first, RandomIt last );
|
template< class RandomIt, class Compare >
bool is_heap( RandomIt first, RandomIt last, Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class RandomIt, class Compare >
bool is_heap( ExecutionPolicy&& policy,
RandomIt first, RandomIt last, Compare comp );
```

Checks whether [first, last) is a `heap`.
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

`true` if the range is a heap with respect to the corresponding comparator, `false` otherwise.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
@3,4@  applications of the comparison function `comp`.

## Exceptions


## Example


### Example

```cpp
#include <algorithm>
#include <bit>
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> v{3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9};

    std::cout << "initially, v:\n";
    for (const auto& i : v)
        std::cout << i << ' ';
    std::cout << '\n';

    if (!std::is_heap(v.begin(), v.end()))
    {
        std::cout << "making heap...\n";
        std::make_heap(v.begin(), v.end());
    }

    std::cout << "after make_heap, v:\n";
    for (auto t{1U}; const auto& i : v)
        std::cout << i << (std::has_single_bit(++t) ? " {{!
```

std::cout << '\n';
}
|output=
initially, v:
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9
making heap...
after make_heap, v:
9 | 6 9 | 5 5 9 7 | 1 1 3 5 8 3 4 2 |

## See also


| cpp/algorithm/dsc is_heap_until | (see dedicated page) |
| cpp/algorithm/dsc make_heap | (see dedicated page) |
| cpp/algorithm/dsc push_heap | (see dedicated page) |
| cpp/algorithm/dsc pop_heap | (see dedicated page) |
| cpp/algorithm/dsc sort_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc is_heap | (see dedicated page) |

