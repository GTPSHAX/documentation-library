---
title: std::fill
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/fill
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|notes1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class ForwardIt, class T >
void fill( ForwardIt first, ForwardIt last, const T& value );
|dcl2=
template< class ForwardIt, class T = typename std::iterator_traits
<ForwardIt>::value_type >
constexpr void fill( ForwardIt first, ForwardIt last,
const T& value );
dcl rev multi|num=2|since1=c++17|until1=c++26
|dcl1=
template< class ExecutionPolicy, class ForwardIt, class T >
void fill( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, const T& value );
|dcl2=
template< class ExecutionPolicy,
class ForwardIt, class T = typename std::iterator_traits
<ForwardIt>::value_type >
void fill( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, const T& value );
```

1. Assigns the given `value` to all elements in the range [first, last).
2. Same as , but executed according to `policy`.
@@
If `value` is not writable to `first`, the program is ill-formed.

## Parameters


### Parameters

- `value` - the value to be assigned
- `policy` - execution policy

**Type requirements:**

- `ForwardIt`

## Complexity

Exactly `std::distance(first, last)` assignments.

## Exceptions


## Possible implementation

eq impl|title1=fill (1)|ver1=1|1=
template<class ForwardIt,
class T = typename std::iterator_traits<ForwardIt>::value_type>
void fill(ForwardIt first, ForwardIt last, const T& value)
{
for (; first != last; ++first)
*first = value;
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
    std::vector<int> v{0, 1, 2, 3, 4, 5, 6, 7, 8};
    println(v);

    // set all of the elements to 8
    std::fill(v.begin(), v.end(), 8);
    println(v);

    std::vector<std::complex<double>> nums{<!---->{1, 3}, {2, 2}, {4, 8}<!---->};
    println(nums);
    #ifdef __cpp_lib_algorithm_default_value_type
        std::fill(nums.begin(), nums.end(), {4, 2});
    #else
        std::fill(nums.begin(), nums.end(), std::complex<double>{4, 2});
    #endif
    println(nums);
}
```


**Output:**
```
0 1 2 3 4 5 6 7 8
8 8 8 8 8 8 8 8 8
(1,3) (2,2) (4,8) 
(4,2) (4,2) (4,2)
```


## Defect reports


## See also


| cpp/algorithm/dsc fill_n | (see dedicated page) |
| cpp/algorithm/dsc copy | (see dedicated page) |
| cpp/algorithm/dsc generate | (see dedicated page) |
| cpp/algorithm/dsc transform | (see dedicated page) |
| cpp/algorithm/ranges/dsc fill | (see dedicated page) |

