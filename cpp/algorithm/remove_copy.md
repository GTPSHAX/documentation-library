---
title: std::remove_copy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/remove_copy
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|notes=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class InputIt, class OutputIt, class T >
OutputIt remove_copy( InputIt first, InputIt last,
OutputIt d_first, const T& value );
|dcl2=
template< class InputIt, class OutputIt,
class T = typename std::iterator_traits
<InputIt>::value_type >
constexpr OutputIt remove_copy( InputIt first, InputIt last,
OutputIt d_first, const T& value );
dcl rev multi|num=2|since1=c++17|until1=c++26
|dcl1=
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class T >
ForwardIt2 remove_copy( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last,
ForwardIt2 d_first, const T& value );
|dcl2=
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2,
class T = typename std::iterator_traits
<ForwardIt1>::value_type >
ForwardIt2 remove_copy( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last,
ForwardIt2 d_first, const T& value );
dcla|num=3|constexpr=c++20|
template< class InputIt, class OutputIt, class UnaryPred >
OutputIt remove_copy_if( InputIt first, InputIt last,
OutputIt d_first, UnaryPred p );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class UnaryPred >
ForwardIt2 remove_copy_if( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last,
ForwardIt2 d_first, UnaryPred p );
```

Copies elements from the range [first, last), to another range beginning at `d_first`, omitting the elements which satisfy specific criteria.
1. Ignores all elements that are equal to `value` (using `1=operator==`).
3. Ignores all elements for which predicate `p` returns `true`.
@2,4@ Same as , but executed according to `policy`.
@@
If <sup>(until C++20)</sup> `1=*d_first = *first` is invalid<sup>(since C++20)</sup> `*first` is not writable to `d_first`, the program is ill-formed.
If source and destination ranges overlap, the behavior is undefined.

## Parameters


### Parameters

- `[3=to copy, range=source}})` - 
- `d_first` - the beginning of the destination range
- `value` - the value of the elements not to copy
- `policy` - execution policy

**Type requirements:**

- `InputIt`
- `OutputIt`
- `ForwardIt1, ForwardIt2`
- `UnaryPred`

## Return value

Iterator to the element past the last element copied.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@ Exactly  comparisons with `value` using `1=operator==`.
@3,4@ Exactly  applications of the predicate `p`.
For the overloads with an ExecutionPolicy, there may be a performance cost if `ForwardIt1`'s `value_type` is not *MoveConstructible*.

## Exceptions


## Possible implementation

eq impl|title1=remove_copy (1)|ver1=1|1=
template<class InputIt, class OutputIt,
class T = typename std::iterator_traits<InputIt>::value_type>
constexpr OutputIt remove_copy(InputIt first, InputIt last,
OutputIt d_first, const T& value)
{
for (; first != last; ++first)
if (!(*first == value))
*d_first++ = *first;
return d_first;
}
|title2=remove_copy_if (3)|ver2=3|2=
template<class InputIt, class OutputIt, class UnaryPred>
constexpr OutputIt remove_copy_if(InputIt first, InputIt last,
OutputIt d_first, UnaryPred p)
{
for (; first != last; ++first)
if (!p(*first))
*d_first++ = *first;
return d_first;
}

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <complex>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

int main()
{
    // Erase the hash characters '#' on the fly.
    std::string str = "#Return #Value #Optimization";
    std::cout << "before: " << std::quoted(str) << '\n';

    std::cout << "after:  \"";
    std::remove_copy(str.begin(), str.end(),
                     std::ostream_iterator<char>(std::cout), '#');
    std::cout << "\"\n";

    // Erase {1, 3} value on the fly.
    std::vector<std::complex<double>> nums{<!---->{2, 2}, {1, 3}, {4, 8}, {1, 3}<!---->};
    std::remove_copy(nums.begin(), nums.end(),
                     std::ostream_iterator<std::complex<double>>(std::cout),
    #ifdef __cpp_lib_algorithm_default_value_type
                     {1, 3}); // T gets deduced
    #else
                     std::complex<double>{1, 3});
    #endif
}
```


**Output:**
```
before: "#Return #Value #Optimization"
after:  "Return Value Optimization"
(2,2)(4,8)
```


## Defect reports


## See also


| cpp/algorithm/dsc remove | (see dedicated page) |
| cpp/algorithm/dsc copy | (see dedicated page) |
| cpp/algorithm/dsc partition_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc remove_copy | (see dedicated page) |

