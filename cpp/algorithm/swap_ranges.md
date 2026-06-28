---
title: std::swap_ranges
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/swap_ranges
---


```cpp
**Header:** `<`algorithm`>`
|
template< class ForwardIt1, class ForwardIt2 >
ForwardIt2 swap_ranges( ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2 );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2 >
ForwardIt2 swap_ranges( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2 );
```

1. Exchanges elements between range [first1, last1) and another range of `std::distance(first1, last1)` elements starting at `first2`.
2. Same as , but executed according to `policy`.
@@
If any of the following conditions is satisfied, the behavior is undefined:
* The two ranges overlap.
* There exists a pair of corresponding iterators `iter1` and `iter2` in the two ranges such that `*iter1` is not *Swappable* with `*iter2`.

## Parameters


### Parameters

- `[first1, last1)` - 
- `first2` - beginning of the second range of elements to swap
- `policy` - execution policy

**Type requirements:**

- `ForwardIt1, ForwardIt2`

## Return value

Iterator to the element past the last element exchanged in the range beginning with `first2`.

## Complexity

Exactly `std::distance(first1, last1)` swaps.

## Exceptions


## Notes


## Possible implementation

eq fun|1=
template<class ForwardIt1, class ForwardIt2>
constexpr //< since C++20
ForwardIt2 swap_ranges(ForwardIt1 first1, ForwardIt1 last1, ForwardIt2 first2)
{
for (; first1 != last1; ++first1, ++first2)
std::iter_swap(first1, first2);
return first2;
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <list>
#include <vector>

auto print = [](auto comment, auto const& seq)
{
    std::cout << comment;
    for (const auto& e : seq)
        std::cout << e << ' ';
    std::cout << '\n';
};

int main()
{
    std::vector<char> v{'a', 'b', 'c', 'd', 'e'};
    std::list<char> l{'1', '2', '3', '4', '5'};

    print("Before swap_ranges:\n" "v: ", v);
    print("l: ", l);

    std::swap_ranges(v.begin(), v.begin() + 3, l.begin());

    print("After swap_ranges:\n" "v: ", v);
    print("l: ", l);
}
```


**Output:**
```
Before swap_ranges:
v: a b c d e
l: 1 2 3 4 5
After swap_ranges:
v: 1 2 3 d e
l: a b c 4 5
```


## See also


| cpp/algorithm/dsc iter_swap | (see dedicated page) |
| cpp/algorithm/dsc swap | (see dedicated page) |
| cpp/algorithm/ranges/dsc swap_ranges | (see dedicated page) |

