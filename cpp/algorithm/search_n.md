---
title: std::search_n
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/search_n
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|notes1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class ForwardIt, class Size, class T >
ForwardIt search_n( ForwardIt first, ForwardIt last,
Size count, const T& value );
|dcl2=
template< class ForwardIt, class Size,
class T = typename std::iterator_traits
<ForwardIt>::value_type >
constexpr ForwardIt search_n( ForwardIt first, ForwardIt last,
Size count, const T& value );
dcl rev multi|num=2|since1=c++17|until1=c++26
|dcl1=
template< class ExecutionPolicy,
class ForwardIt, class Size, class T >
ForwardIt search_n( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
Size count, const T& value );
|dcl2=
template< class ExecutionPolicy,
class ForwardIt, class Size,
class T = typename std::iterator_traits
<ForwardIt>::value_type >
ForwardIt search_n( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
Size count, const T& value );
dcl rev multi|num=3|constexpr1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class ForwardIt, class Size, class T, class BinaryPred >
ForwardIt search_n( ForwardIt first, ForwardIt last,
Size count, const T& value, BinaryPred p );
|dcl2=
template< class ForwardIt, class Size,
class T = typename std::iterator_traits
<ForwardIt>::value_type,
class BinaryPred >
constexpr ForwardIt search_n( ForwardIt first, ForwardIt last,
Size count, const T& value, BinaryPred p );
dcl rev multi|num=4|since1=c++17|until1=c++26
|dcl1=
template< class ExecutionPolicy, class ForwardIt, class Size,
class T, class BinaryPred >
ForwardIt search_n( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
Size count, const T& value, BinaryPred p );
|dcl2=
template< class ExecutionPolicy, class ForwardIt, class Size,
class T = typename std::iterator_traits
<ForwardIt>::value_type,
class BinaryPred >
ForwardIt search_n( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
Size count, const T& value, BinaryPred p );
```

Searches the range [first, last) for the first sequence of `count` identical elements, each equal to the given `value`.
1. Elements are compared using `1=operator==`.
3. Elements are compared using the given binary predicate `p`.
@2,4@ Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `count` - the length of the sequence to search for
- `value` - the value of the elements to search for
- `policy` - execution policy

**Type requirements:**

- `ForwardIt`
- `BinaryPred`

## Return value

If `count` is positive, returns an iterator to the beginning of the first sequence found in the range [first, last). Each iterator `it` in the sequence should satisfy the following condition:
@1,2@ `1=*it == value` is `true`.
@3,4@ `1=p(*it, value) != false` is `true`.
If no such sequence is found, `last` is returned.
If `count` is zero or negative, `first` is returned.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@ At most  comparisons using `1=operator==`.
@3,4@ At most  applications of the predicate `p`.

## Exceptions


## Possible implementation

eq impl
|title1=search_n (1)|ver1=1|1=
template<class ForwardIt, class Size,
class T = typename std::iterator_traits<ForwardIt>::value_type>
ForwardIt search_n(ForwardIt first, ForwardIt last, Size count, const T& value)
{
if (count <= 0)
return first;
for (; first != last; ++first)
{
if (!(*first == value))
continue;
ForwardIt candidate = first;
for (Size cur_count = 1; true; ++cur_count)
{
if (cur_count >= count)
return candidate; // success
++first;
if (first == last)
return last; // exhausted the list
if (!(*first == value))
break; // too few in a row
}
}
return last;
}
|title2=search_n (3)|ver2=3|2=
template<class ForwardIt, class Size,
class T = typename std::iterator_traits<ForwardIt>::value_type,
class BinaryPred>
ForwardIt search_n(ForwardIt first, ForwardIt last, Size count, const T& value,
BinaryPred p)
{
if (count <= 0)
return first;
for (; first != last; ++first)
{
if (!p(*first, value))
continue;
ForwardIt candidate = first;
for (Size cur_count = 1; true; ++cur_count)
{
if (cur_count >= count)
return candidate; // success
++first;
if (first == last)
return last; // exhausted the list
if (!p(*first, value))
break; // too few in a row
}
}
return last;
}

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <complex>
#include <iostream>
#include <iterator>
#include <vector>

template<class Container, class Size, class T>
constexpr bool consecutive_values(const Container& c, Size count, const T& v)
{
    return std::search_n(std::begin(c), std::end(c), count, v) != std::end(c);
}

int main()
{
    constexpr char sequence[] = ".0_0.000.0_0.";

    static_assert(consecutive_values(sequence, 3, '0'));

    for (int n : {4, 3, 2})
        std::cout << std::boolalpha
                  << "Has " << n << " consecutive zeros: "
                  << consecutive_values(sequence, n, '0') << '\n';

    std::vector<std::complex<double>> nums{{4, 2}, {4, 2}, {1, 3
```

#ifdef __cpp_lib_algorithm_default_value_type
auto it = std::search_n(nums.cbegin(), nums.cend(), 2, {4, 2});
#else
auto it = std::search_n(nums.cbegin(), nums.cend(), 2, std::complex<double>{4, 2});
#endif
assert(it == nums.begin());
}
|output=
Has 4 consecutive zeros: false
Has 3 consecutive zeros: true
Has 2 consecutive zeros: true

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2150 | C++98 | the condition of “sequence occurence” was incorrect | corrected |


## See also


| cpp/algorithm/dsc find_end | (see dedicated page) |
| cpp/algorithm/dsc find | (see dedicated page) |
| cpp/algorithm/dsc search | (see dedicated page) |
| cpp/algorithm/ranges/dsc search_n | (see dedicated page) |

