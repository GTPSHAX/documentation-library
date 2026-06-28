---
title: std::is_permutation
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/is_permutation
---


```cpp
**Header:** `<`algorithm`>`
|
template< class ForwardIt1, class ForwardIt2 >
bool is_permutation( ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2 );
|
template< class ForwardIt1, class ForwardIt2,
class BinaryPredicate >
bool is_permutation( ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, BinaryPredicate p );
|
template< class ForwardIt1, class ForwardIt2 >
bool is_permutation( ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2 );
|
template< class ForwardIt1, class ForwardIt2,
class BinaryPredicate >
bool is_permutation( ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2,
BinaryPredicate p );
```

Checks whether [first1, last1) is a [permutation](https://en.wikipedia.org/wiki/permutation) of a range starting from `first2`:
* For overloads , the second range has `std::distance(first1, last1)` elements.
* For overloads , the second range is [first2, last2).
@1,3@ Elements are compared using `1=operator==`.
@2,4@ Elements are compared using the given binary predicate `p`.
If `ForwardIt1` and `ForwardIt2` have different value types, the program is ill-formed.
If the comparison function is not an [equivalence relation](https://en.wikipedia.org/wiki/equivalence relation), the behavior is undefined.

## Parameters


### Parameters

- `[first1, last1)` - 
- `[first2, last2)` - 

**Type requirements:**

- `ForwardIt1, ForwardIt2`

## Return value

`true` if the range [first1, last1) is a permutation of the range [first2, last2), `false` otherwise.

## Complexity

Given  as `std::distance(first1, last1)`:
1. Exactly  comparisons using `1=operator==` if the two ranges are equal, otherwise ) comparisons in the worst case.</div>
2. Exactly  applications of the predicate `p` if the two ranges are equal, otherwise ) applications in the worst case.</div>
@3,4@ If `ForwardIt1` and `ForwardIt2` are both *RandomAccessIterator*, and `1=last1 - first1 != last2 - first2` is `true`, no comparison will be made.
@@ Otherwise:</div>
:@3@ Exactly  comparisons using `1=operator==` if the two ranges are equal, otherwise ) comparisons in the worst case.</div>
:@4@ Exactly  applications of the predicate `p` if the two ranges are equal, otherwise ) applications in the worst case.</div>

## Possible implementation

eq fun|1=
template<class ForwardIt1, class ForwardIt2>
bool is_permutation(ForwardIt1 first, ForwardIt1 last,
ForwardIt2 d_first)
{
// skip common prefix
std::tie(first, d_first) = std::mismatch(first, last, d_first);
// iterate over the rest, counting how many times each element
// from [first, last) appears in [d_first, d_last)
if (first != last)
{
ForwardIt2 d_last = std::next(d_first, std::distance(first, last));
for (ForwardIt1 i = first; i != last; ++i)
{
if (i != std::find(first, i, *i))
continue; // this *i has been checked
auto m = std::count(d_first, d_last, *i);
if (m == 0  std::count(i, last, *i) != m)
return false;
}
}
return true;
}

## Note

The `std::is_permutation` can be used in ''testing'', namely to check the correctness of rearranging algorithms (e.g. sorting, shuffling, partitioning). If `x` is an original range and `y` is a ''permuted'' range then `1=std::is_permutation(x, y) == true` means that `y` consist of ''"the same"'' elements, maybe staying at other positions.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>

template<typename Os, typename V>
Os& operator<<(Os& os, const V& v)
{
    os << "{ ";
    for (const auto& e : v)
        os << e << ' ';
    return os << '}';
}

int main()
{
    static constexpr auto v1 = {1, 2, 3, 4, 5};
    static constexpr auto v2 = {3, 5, 4, 1, 2};
    static constexpr auto v3 = {3, 5, 4, 1, 1};

    std::cout << v2 << " is a permutation of " << v1 << ": " << std::boolalpha
              << std::is_permutation(v1.begin(), v1.end(), v2.begin()) << '\n'
              << v3 << " is a permutation of " << v1 << ": "
              << std::is_permutation(v1.begin(), v1.end(), v3.begin()) << '\n';
}
```


**Output:**
```
{ 3 5 4 1 2 } is a permutation of { 1 2 3 4 5 }: true
{ 3 5 4 1 1 } is a permutation of { 1 2 3 4 5 }: false
```


## See also


| cpp/algorithm/dsc next_permutation | (see dedicated page) |
| cpp/algorithm/dsc prev_permutation | (see dedicated page) |
| cpp/concepts/dsc equivalence_relation | (see dedicated page) |
| cpp/algorithm/ranges/dsc is_permutation | (see dedicated page) |

