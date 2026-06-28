---
title: std::replace
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/replace
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|notes1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class ForwardIt, class T >
void replace( ForwardIt first, ForwardIt last,
const T& old_value, const T& new_value );
|dcl2=
template< class ForwardIt, class T = typename std::iterator_traits
<ForwardIt>::value_type >
constexpr void replace( ForwardIt first, ForwardIt last,
const T& old_value, const T& new_value );
dcl rev multi|num=2|since1=c++17|until1=c++26
|dcl1=
template< class ExecutionPolicy, class ForwardIt, class T >
void replace( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
const T& old_value, const T& new_value );
|dcl2=
template< class ExecutionPolicy, class ForwardIt,
class T = typename std::iterator_traits
<ForwardIt>::value_type >
void replace( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
const T& old_value, const T& new_value );
dcl rev multi|num=3|notes1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class ForwardIt, class UnaryPred, class T >
void replace_if( ForwardIt first, ForwardIt last,
UnaryPred p, const T& new_value );
|dcl2=
template< class ForwardIt, class UnaryPred,
class T = typename std::iterator_traits
<ForwardIt>::value_type> >
constexpr void replace_if( ForwardIt first, ForwardIt last,
UnaryPred p, const T& new_value );
dcl rev multi|num=4|since1=c++17|until1=c++26
|dcl1=
template< class ExecutionPolicy,
class ForwardIt, class UnaryPred, class T >
void replace_if( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
UnaryPred p, const T& new_value );
|dcl2=
template< class ExecutionPolicy,
class ForwardIt, class UnaryPred,
class T = typename std::iterator_traits
<ForwardIt>::value_type> >
void replace_if( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
UnaryPred p, const T& new_value );
```

Replaces all elements in the range [first, last) with `new_value` if they satisfy specific criteria.
1. Replaces all elements that are equal to `old_value` (using `1=operator==`).
3. Replaces all elements for which predicate `p` returns `true`.
@2,4@ Same as , but executed according to `policy`.
@@
If <sup>(until C++20)</sup> `1=*first = new_value` is invalid<sup>(since C++20)</sup> `new_value` is not writable to `first`, the program is ill-formed.

## Parameters


### Parameters

- `old_value` - the value of elements to replace
- `policy` - execution policy
- `new_value` - the value to use as replacement

**Type requirements:**

- `ForwardIt`
- `UnaryPred`

## Complexity

Given  as `std::distance(first, last)`:
@1,2@ Exactly  comparisons using `1=operator==`.
@3,4@ Exactly  applications of the predicate `p`.

## Exceptions


## Notes

Because the algorithm takes `old_value` and `new_value` by reference, it can have unexpected behavior if either is a reference to an element of the range [first, last).

## Possible implementation

eq impl
|title1=replace (1)|ver1=1|1=
template<class ForwardIt,
class T = typename std::iterator_traits<ForwardIt>::value_type>
void replace(ForwardIt first, ForwardIt last,
const T& old_value, const T& new_value)
{
for (; first != last; ++first)
if (*first == old_value)
*first = new_value;
}
|title2=replace_if (3)|ver2=3|2=
template<class ForwardIt, class UnaryPred,
class T = typename std::iterator_traits<ForwardIt>::value_type>
void replace_if(ForwardIt first, ForwardIt last,
UnaryPred p, const T& new_value)
{
for (; first != last; ++first)
if (p(*first))
*first = new_value;
}

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <complex>
#include <functional>
#include <iostream>

void println(const auto& seq)
{
    for (const auto& e : seq)
        std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    std::array<int, 10> s{5, 7, 4, 2, 8, 6, 1, 9, 0, 3};

    // Replace all occurrences of 8 with 88.
    std::replace(s.begin(), s.end(), 8, 88);
    println(s);

    // Replace all values less than 5 with 55.
    std::replace_if(s.begin(), s.end(), 
                    std::bind(std::less<int>(), std::placeholders::_1, 5), 55);
    println(s);

    std::array<std::complex<double>, 2> nums{<!---->{<!---->{1, 3}, {1, 3}<!---->}<!---->};
    #ifdef __cpp_lib_algorithm_default_value_type
        std::replace(nums.begin(), nums.end(), {1, 3}, {4, 2});
    #else
        std::replace(nums.begin(), nums.end(), std::complex<double>{1, 3},
                                               std::complex<double>{4, 2});
    #endif
    println(nums);
}
```


**Output:**
```
5 7 4 2 88 6 1 9 0 3
5 7 55 55 88 6 55 9 55 55
(4,2), (4,2)
```


## Defect reports


## See also


| cpp/algorithm/dsc replace_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc replace | (see dedicated page) |

