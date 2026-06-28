---
title: std::prev_permutation
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/prev_permutation
---


```cpp
**Header:** `<`algorithm`>`
|
template< class BidirIt >
bool prev_permutation( BidirIt first, BidirIt last );
|
template< class BidirIt, class Compare >
bool prev_permutation( BidirIt first, BidirIt last, Compare comp );
```

Transforms the range [first, last) into the previous [permutation](https://en.wikipedia.org/wiki/permutation). Returns `true` if such permutation exists, otherwise transforms the range into the last permutation (a descending order) and returns `false`.
1. The set of all permutations is ordered lexicographically with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
2. The set of all permutations is ordered lexicographically with respect to `comp`.
If <sup>(until C++11)</sup> the type of `*first` is not *Swappable*<sup>(since C++11)</sup> `BidirIt` is not *ValueSwappable*, the behavior is undefined.

## Parameters


### Parameters


**Type requirements:**

- `BidirIt`

## Return value

`true` if the new permutation precedes the old in lexicographical order. `false` if the first permutation was reached and the range was reset to the last permutation.

## Exceptions

Any exceptions thrown from iterator operations or the element swap.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@ At most mathjax-or|\(\scriptsize \frac{N}{2}\)| swaps.

## Possible implementation

eq fun
|1=
template<class BidirIt>
bool prev_permutation(BidirIt first, BidirIt last)
{
if (first == last)
return false;
BidirIt i = last;
if (first == --i)
return false;
while (1)
{
BidirIt i1, i2;
i1 = i;
if (*i1 < *--i)
{
i2 = last;
while (!(*--i2 < *i))
;
std::iter_swap(i, i2);
std::reverse(i1, last);
return true;
}
if (i == first)
{
std::reverse(first, last);
return false;
}
}
}

## Notes

Averaged over the entire sequence of permutations, typical implementations use about 3 comparisons and 1.5 swaps per call.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <string>

int main()
{
    std::string s = "cab";

    do
    {
        std::cout << s << ' ';
    }
    while (std::prev_permutation(s.begin(), s.end()));

    std::cout << s << '\n';
}
```


**Output:**
```
cab bca bac acb abc cba
```


## See also


| cpp/algorithm/dsc is_permutation | (see dedicated page) |
| cpp/algorithm/dsc next_permutation | (see dedicated page) |
| cpp/algorithm/ranges/dsc prev_permutation | (see dedicated page) |

