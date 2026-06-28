---
title: std::iter_swap
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/iter_swap
---

ddcl|header=algorithm|notes=<sup>(constexpr C++20)</sup>|
template< class ForwardIt1, class ForwardIt2 >
void iter_swap( ForwardIt1 a, ForwardIt2 b );
Swaps the values of the elements the given iterators are pointing to.
If any of the following conditions is satisfied, the behavior is undefined:
* `a` or `b` is not dereferenceable.
* `*a` is not *Swappable* with `*b`.

## Parameters


### Parameters

- `a, b` - iterators to the elements to swap

**Type requirements:**

- `ForwardIt1, ForwardIt2`

## Return value

(none)

## Complexity

Constant.

## Notes

This function template models the semantics of the swap operation given by *Swappable*. That is, overloads of `swap` found by ADL and the fall back of `std::swap` are considered.

## Possible implementation

eq fun|1=
template<class ForwardIt1, class ForwardIt2>
constexpr //< since C++20
void iter_swap(ForwardIt1 a, ForwardIt2 b)
{
using std::swap;
swap(*a, *b);
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <random>
#include <string_view>
#include <vector>

template<class ForwardIt>
void selection_sort(ForwardIt begin, ForwardIt end)
{
    for (ForwardIt it = begin; it != end; ++it)
        std::iter_swap(it, std::min_element(it, end));
}

void println(std::string_view rem, std::vector<int> const& v)
{
    std::cout << rem;
    for (int e : v)
        std::cout << e << ' ';
    std::cout << '\n';
}

template<int min, int max>
int rand_int()
{
    static std::uniform_int_distribution dist(min, max);
    static std::mt19937 gen(std::random_device{}());
    return dist(gen);
}

int main()
{
    std::vector<int> v;
    std::generate_n(std::back_inserter(v), 20, rand_int<-9, +9>);

    std::cout << std::showpos;
    println("Before sort: ", v);
    selection_sort(v.begin(), v.end());
    println("After sort:  ", v);
}
```


**Output:**
```
Before sort: -9 -3 +2 -8 +0 -1 +8 -4 -5 +1 -4 -5 +4 -9 -8 -6 -6 +8 -4 -6 
After sort:  -9 -9 -8 -8 -6 -6 -6 -5 -5 -4 -4 -4 -3 -1 +0 +1 +2 +4 +8 +8
```


## Defect reports


## See also


| cpp/algorithm/dsc swap | (see dedicated page) |
| cpp/algorithm/dsc swap_ranges | (see dedicated page) |
| cpp/iterator/adaptor/dsc iter_swap|reverse_iterator | (see dedicated page) |
| cpp/iterator/adaptor/dsc iter_swap|move_iterator | (see dedicated page) |
| cpp/iterator/ranges/dsc iter_swap | (see dedicated page) |

