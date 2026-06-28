---
title: std::replace_copy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/replace_copy
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|constexpr=c++20|
template< class InputIt, class OutputIt, class T >
OutputIt replace_copy( InputIt first, InputIt last, OutputIt d_first,
const T& old_value, const T& new_value );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class T >
ForwardIt2 replace_copy
( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last, ForwardIt2 d_first,
const T& old_value, const T& new_value );
dcl rev multi|num=3|notes1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class InputIt, class OutputIt, class UnaryPred, class T >
OutputIt replace_copy_if
( InputIt first, InputIt last, OutputIt d_first,
UnaryPred p, const T& new_value );
|dcl2=
template< class InputIt, class OutputIt, class UnaryPred,
class T = typename std::iterator_traits
<OutputIt>::value_type >
constexpr OutputIt replace_copy_if
( InputIt first, InputIt last, OutputIt d_first,
UnaryPred p, const T& new_value );
dcl rev multi|num=4|since1=c++17|until1=c++26
|dcl1=
template< class ExecutionPolicy, class ForwardIt1, class ForwardIt2,
class UnaryPred, class T >
ForwardIt2 replace_copy_if
( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last, ForwardIt2 d_first,
UnaryPred p, const T& new_value );
|dcl2=
template< class ExecutionPolicy, class ForwardIt1, class ForwardIt2,
class UnaryPred, class T = typename std::iterator_traits
<ForwardIt2>::value_type >
ForwardIt2 replace_copy_if
( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last, ForwardIt2 d_first,
UnaryPred p, const T& new_value );
```

Copies the elements from the range [first, last) to another range beginning at `d_first`, while replacing all elements satisfying specific criteria with `new_value`.
1. Replaces all elements that are equal to `old_value` (using `1=operator==`).
3. Replaces all elements for which predicate `p` returns `true`.
@2,4@ Same as , but executed according to `policy`.
@@
If any of the results of the expressions `*first` and `new_value` is not writable to `d_first`, the program is ill-formed.
If the source and destination ranges overlap, the behavior is undefined.

## Parameters


### Parameters

- `[3=to copy, range=source}})` - 
- `d_first` - the beginning of the destination range
- `old_value` - the value of elements to replace
- `policy` - execution policy
- `new_value` - the value to use as replacement

**Type requirements:**

- `InputIt`
- `OutputIt`
- `ForwardIt1, ForwardIt2`

## Return value

Iterator to the element past the last element copied.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@ Exactly  comparisons using `1=operator==`.
@3,4@ Exactly  applications of the predicate `p`.

## Exceptions


## Possible implementation

eq impl
|title1=replace_copy (1)|ver1=1|1=
template<class InputIt, class OutputIt, class T>
OutputIt replace_copy(InputIt first, InputIt last, OutputIt d_first,
const T& old_value, const T& new_value)
{
for (; first != last; ++first)
*d_first++ = (*first == old_value) ? new_value : *first;
return d_first;
}
|title2=replace_copy_if (3)|ver2=3|2=
template<class InputIt, class OutputIt, class UnaryPred,
class T = typename std::iterator_traits<ForwardIt>::value_type>
OutputIt replace_copy_if(InputIt first, InputIt last, OutputIt d_first,
UnaryPred p, const T& new_value)
{
for (; first != last; ++first)
*d_first++ = p(*first) ? new_value : *first;
return d_first;
}

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <complex>
#include <iostream>
#include <vector>

void println(const auto& seq)
{
    for (const auto& e : seq)
        std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    std::vector<short> src{3, 1, 4, 1, 5, 9, 2, 6, 5};
    println(src);
    std::vector<int> dst(src.size());
    std::replace_copy_if(src.cbegin(), src.cend(),
                         dst.begin(),
                         [](short n){ return n > 5; }, 0);
    println(dst);

    std::vector<std::complex<double>> src2{<!---->{1, 3}, {2, 4}, {3, 5}<!---->},
                                      dst2(src2.size());
    println(src2);
    #ifdef __cpp_lib_algorithm_default_value_type
        std::replace_copy_if(src2.cbegin(), src2.cend(), dst2.begin(),
            [](std::complex<double> z){ return std::abs(z) < 5; },
            {4, 2}); // Possible, since the T is deduced.
    #else
        std::replace_copy_if(src2.cbegin(), src2.cend(), dst2.begin(),
            [](std::complex<double> z){ return std::abs(z) < 5; },
            std::complex<double>{4, 2});
    #endif
    println(dst2);
}
```


**Output:**
```
3 1 4 1 5 9 2 6 5 
3 1 4 1 5 0 2 0 5 
(1,3) (2,4) (3,5) 
(4,2) (4,2) (3,5)
```


## Defect reports


## See also


| cpp/algorithm/dsc replace | (see dedicated page) |
| cpp/algorithm/dsc remove | (see dedicated page) |
| cpp/algorithm/ranges/dsc replace_copy | (see dedicated page) |

