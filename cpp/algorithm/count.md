---
title: std::count
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/count
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|notes1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class InputIt, class T >
typename std::iterator_traits<InputIt>::difference_type
count( InputIt first, InputIt last, const T& value );
|dcl2=
template< class InputIt, class T = typename std::iterator_traits
<InputIt>::value_type >
constexpr typename std::iterator_traits<InputIt>::difference_type
count( InputIt first, InputIt last, const T& value );
dcl rev multi|num=2|since1=c++17|until1=c++26
|dcl1=
template< class ExecutionPolicy, class ForwardIt, class T >
typename std::iterator_traits<ForwardIt>::difference_type
count( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, const T& value );
|dcl2=
template< class ExecutionPolicy,
class ForwardIt, class T = typename std::iterator_traits
<ForwardIt>::value_type >
typename std::iterator_traits<ForwardIt>::difference_type
count( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, const T& value );
dcla|num=3|constexpr=c++20|
template< class InputIt, class UnaryPred >
typename std::iterator_traits<InputIt>::difference_type
count_if( InputIt first, InputIt last, UnaryPred p );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class UnaryPred >
typename std::iterator_traits<ForwardIt>::difference_type
count_if( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, UnaryPred p );
```

Returns the number of elements in the range [first, last) satisfying specific criteria.
1. Counts the elements that are equal to `value` (using `1=operator==`).
3. Counts elements for which predicate `p` returns `true`.
@2,4@ Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `value` - the value to search for
- `policy` - execution policy

**Type requirements:**

- `InputIt`
- `ForwardIt`
- `UnaryPred`

## Return value

The number of iterators `it` in the range [first, last) satisfying the following condition:
@1,2@ `1=*it == value` is `true`.
@3,4@ `1=p(*it) != false` is `true`.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@ Exactly  comparisons with `value` using `1=operator==`.
@3,4@ Exactly  applications of the predicate `p`.

## Exceptions


## Notes

For the number of elements in the range [first, last) without any additional criteria, see `std::distance`.

## Possible implementation

See also the implementations of `count` in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L4056 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L1171 libc++].
See also the implementations of `count_if` in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L4079 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L1186 libc++].
eq impl
|title1=count (1)|ver1=1|1=
template<class InputIt, class T = typename std::iterator_traits<InputIt>::value_type>
typename std::iterator_traits<InputIt>::difference_type
count(InputIt first, InputIt last, const T& value)
{
typename std::iterator_traits<InputIt>::difference_type ret = 0;
for (; first != last; ++first)
if (*first == value)
++ret;
return ret;
}
|title2=count_if (3)|ver2=3|2=
template<class InputIt, class UnaryPred>
typename std::iterator_traits<InputIt>::difference_type
count_if(InputIt first, InputIt last, UnaryPred p)
{
typename std::iterator_traits<InputIt>::difference_type ret = 0;
for (; first != last; ++first)
if (p(*first))
++ret;
return ret;
}

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <cassert>
#include <complex>
#include <iostream>
#include <iterator>

int main()
{
    constexpr std::array v{1, 2, 3, 4, 4, 3, 7, 8, 9, 10};
    std::cout << "v: ";
    std::copy(v.cbegin(), v.cend(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';

    // Determine how many integers match a target value.
    for (const int target : {3, 4, 5})
    {
        const int num_items = std::count(v.cbegin(), v.cend(), target);
        std::cout << "number: " << target << ", count: " << num_items << '\n';
    }

    // Use a lambda expression to count elements divisible by 4.
    int count_div4 = std::count_if(v.begin(), v.end(), [](int i) { return i % 4 == 0; });
    std::cout << "numbers divisible by four: " << count_div4 << '\n';

    // A simplified version of `distance` with O(N) complexity:
    auto distance = [](auto first, auto last)
    {
        return std::count_if(first, last, [](auto) { return true; });
    };
    static_assert(distance(v.begin(), v.end()) == 10);

    std::array<std::complex<double>, 3> nums{<!---->{<!---->{4, 2}, {1, 3}, {4, 2}<!---->}<!---->};
    #ifdef __cpp_lib_algorithm_default_value_type
        // T gets deduced making list-initialization possible
        auto c = std::count(nums.cbegin(), nums.cend(), {4, 2});
    #else
        auto c = std::count(nums.cbegin(), nums.cend(), std::complex<double>{4, 2});
    #endif
    assert(c == 2);
}
```


**Output:**
```
v: 1 2 3 4 4 3 7 8 9 10
number: 3, count: 2
number: 4, count: 2
number: 5, count: 0
numbers divisible by four: 3
```


## Defect reports


## See also


| cpp/iterator/dsc distance | (see dedicated page) |
| cpp/algorithm/ranges/dsc count | (see dedicated page) |

