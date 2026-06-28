---
title: std::next_permutation
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/next_permutation
---


```cpp
**Header:** `<`algorithm`>`
|
template< class BidirIt >
bool next_permutation( BidirIt first, BidirIt last );
|
template< class BidirIt, class Compare >
bool next_permutation( BidirIt first, BidirIt last, Compare comp );
```

Permutes the range [first, last) into the next [permutation](https://en.wikipedia.org/wiki/permutation). Returns `true` if such a “next permutation” exists; otherwise transforms the range into the lexicographically first permutation (an ascending order) and returns `false`.
1. The set of all permutations is ordered lexicographically with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
2. The set of all permutations is ordered lexicographically with respect to `comp`.
If <sup>(until C++11)</sup> the type of `*first` is not *Swappable*<sup>(since C++11)</sup> `BidirIt` is not *ValueSwappable*, the behavior is undefined.

## Parameters


### Parameters


**Type requirements:**

- `BidirIt`

## Return value

`true` if the new permutation is lexicographically greater than the old. `false` if the last permutation was reached and the range was reset to the first permutation.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@ At most mathjax-or|\(\scriptsize \frac{N}{2}\)| swaps.

## Exceptions

Any exceptions thrown from iterator operations or the element swap.

## Possible implementation

eq fun
|1=
template<class BidirIt>
bool next_permutation(BidirIt first, BidirIt last)
{
auto r_first = std::make_reverse_iterator(last);
auto r_last = std::make_reverse_iterator(first);
auto left = std::is_sorted_until(r_first, r_last);
if (left != r_last)
{
auto right = std::upper_bound(r_first, left, *left);
std::iter_swap(left, right);
}
std::reverse(left.base(), last);
return left != r_last;
}

## Notes

Averaged over the entire sequence of permutations, typical implementations use about 3 comparisons and 1.5 swaps per call.

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>

int main()
{
    std::string s = "ABBA";
    std::sort(s.begin(), s.end());

    do
        std::cout << s << '\n';
    while (std::next_permutation(s.begin(), s.end()));

    assert(std::is_sorted(s.begin(), s.end()));
}
```


**Output:**
```
AABB
ABAB
ABBA
BAAB
BABA
BBAA
```


## See also


| cpp/algorithm/dsc is_permutation | (see dedicated page) |
| cpp/algorithm/dsc prev_permutation | (see dedicated page) |
| cpp/algorithm/ranges/dsc next_permutation | (see dedicated page) |

