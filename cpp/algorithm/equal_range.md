---
title: std::equal_range
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/equal_range
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|notes1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class ForwardIt, class T >
std::pair<ForwardIt, ForwardIt>
equal_range( ForwardIt first, ForwardIt last, const T& value );
|dcl2=
template< class ForwardIt, class T = typename std::iterator_traits
<ForwardIt>::value_type >
constexpr std::pair<ForwardIt, ForwardIt>
equal_range( ForwardIt first, ForwardIt last, const T& value );
dcl rev multi|num=2|notes1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class ForwardIt, class T, class Compare >
std::pair<ForwardIt, ForwardIt>
equal_range( ForwardIt first, ForwardIt last,
const T& value, Compare comp );
|dcl2=
template< class ForwardIt, class T = typename std::iterator_traits
<ForwardIt>::value_type,
class Compare >
constexpr std::pair<ForwardIt, ForwardIt>
equal_range( ForwardIt first, ForwardIt last,
const T& value, Compare comp );
```

Returns a range containing all elements equivalent to `value` in the partitioned range [first, last).
1. The equivalence is checked using `operator<`:
rev|until=c++20|
Returns the results of `std::lower_bound(first, last, value)` and `std::upper_bound(first, last, value)`.
If any of the following conditions is satisfied, the behavior is undefined:
* For any element `elem` of [first, last), `bool(elem < value)` does not imply `!bool(value < elem)`.
* The elements `elem` of [first, last) are not `partitioned` with respect to expressions `bool(elem < value)` and `!bool(value < elem)`.
rev|since=c++20|
Equivalent to }.
2. The equivalence is checked using `comp`:
@@ Returns the results of `std::lower_bound(first, last, value, comp)` and `std::upper_bound(first, last, value, comp)`.
@@ If any of the following conditions is satisfied, the behavior is undefined:
* For any element `elem` of [first, last), `bool(comp(elem, value))` does not imply `!bool(comp(value, elem))`.
* The elements `elem` of [first, last) are not `partitioned` with respect to expressions `bool(comp(elem, value))` and `!bool(comp(value, elem))`.

## Parameters


### Parameters

- `[3=to examine, range=partitioned}})` - 
- `value` - value to compare the elements to

**Type requirements:**

- `ForwardIt`
- `Compare`

## Return value

A `std::pair` containing a pair of iterators, where
* `first` is an iterator to the first element of the range [first, last) not ordered before `value` (or `last` if no such element is found), and
* `second` is an iterator to the first element of the range [first, last) ordered after `value` (or `last` if no such element is found).

## Complexity

Given  as `std::distance(first, last)`:
1. At most } comparisons with `value` using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
2. At most } applications of the comparator `comp`.
However, if `ForwardIt` is not a *RandomAccessIterator*, the number of iterator increments is linear in . Notably, `std::set` and `std::multiset` iterators are not random access, and so their member functions `std::set::equal_range` (resp. `std::multiset::equal_range`) should be preferred.

## Notes

Although `std::equal_range` only requires [first, last) to be partitioned, this algorithm is usually used in the case where [first, last) is sorted, so that the binary search is valid for any `value`.
On top of the requirements of `std::lower_bound` and `std::upper_bound`, `std::equal_range` also requires `operator<` or `comp` to be asymmetric (i.e., `a < b` and `b < a` always have different results).
Therefore, the intermediate results of binary search can be shared by `std::lower_bound` and `std::upper_bound`. For example, the result of the `std::lower_bound` call can be used as the argument of `first` in the `std::upper_bound` call.

## Possible implementation

eq impl|title1=equal_range (1)|ver1=1|1=
template<class ForwardIt,
class T = typename std::iterator_traits<ForwardIt>::value_type>
constexpr std::pair<ForwardIt, ForwardIt>
equal_range(ForwardIt first, ForwardIt last, const T& value)
{
return std::equal_range(first, last, value, std::less{});
}
|title2=equal_range (2)|ver2=2|2=
template<class ForwardIt,
class T = typename std::iterator_traits<ForwardIt>::value_type,
class Compare>
constexpr std::pair<ForwardIt, ForwardIt>
equal_range(ForwardIt first, ForwardIt last, const T& value, Compare comp)
{
return std::make_pair(std::lower_bound(first, last, value, comp),
std::upper_bound(first, last, value, comp));
}

## Example


### Example

```cpp
#include <algorithm>
#include <complex>
#include <iostream>
#include <vector>

struct S
{
    int number;
    char name;
    // note: name is ignored by this comparison operator
    bool operator<(const S& s) const { return number < s.number; }
};

struct Comp
{
    bool operator()(const S& s, int i) const { return s.number < i; }
    bool operator()(int i, const S& s) const { return i < s.number; }
};

int main()
{
    // note: not ordered, only partitioned w.r.t. S defined below
    const std::vector<S> vec{<!---->{1, 'A'}, {2, 'B'}, {2, 'C'},
                             {2, 'D'}, {4, 'G'}, {3, 'F'}<!---->};
    const S value{2, '?'};

    std::cout << "Compare using S::operator<(): ";
    const auto p = std::equal_range(vec.begin(), vec.end(), value);

    for (auto it = p.first; it != p.second; ++it)
        std::cout << it->name << ' ';
    std::cout << '\n';

    std::cout << "Using heterogeneous comparison: ";
    const auto p2 = std::equal_range(vec.begin(), vec.end(), 2, Comp{});

    for (auto it = p2.first; it != p2.second; ++it)
        std::cout << it->name << ' ';
    std::cout << '\n';

    using CD = std::complex<double>;
    std::vector<CD> nums{<!---->{1, 0}, {2, 2}, {2, 1}, {3, 0}, {3, 1}<!---->};
    auto cmpz = [](CD x, CD y) { return x.real() < y.real(); };
    #ifdef __cpp_lib_algorithm_default_value_type
        auto p3 = std::equal_range(nums.cbegin(), nums.cend(), {2, 0}, cmpz);
    #else
        auto p3 = std::equal_range(nums.cbegin(), nums.cend(), CD{2, 0}, cmpz);
    #endif

    for (auto it = p3.first; it != p3.second; ++it)
        std::cout << *it << ' ';
    std::cout << '\n';
}
```


**Output:**
```
Compare using S::operator<(): B C D 
Using heterogeneous comparison: B C D
(2,2) (2, 1)
```


## Defect reports


## See also


| cpp/algorithm/dsc lower_bound | (see dedicated page) |
| cpp/algorithm/dsc upper_bound | (see dedicated page) |
| cpp/algorithm/dsc binary_search | (see dedicated page) |
| cpp/algorithm/dsc partition | (see dedicated page) |
| cpp/algorithm/dsc equal | (see dedicated page) |
| cpp/container/dsc equal_range|set | (see dedicated page) |
| cpp/container/dsc equal_range|multiset | (see dedicated page) |
| cpp/algorithm/ranges/dsc equal_range | (see dedicated page) |

