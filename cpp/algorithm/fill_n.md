---
title: std::fill_n
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/fill_n
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|notes1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class OutputIt, class Size, class T >
OutputIt fill_n( OutputIt first, Size count, const T& value );
|dcl2=
template< class OutputIt, class Size,
class T = typename std::iterator_traits
<OutputIt>::value_type >
constexpr OutputIt fill_n( OutputIt first, Size count,
const T& value );
dcl rev multi|num=2|since1=c++17|until1=c++26
|dcl1=
template< class ExecutionPolicy,
class ForwardIt, class Size, class T >
ForwardIt fill_n( ExecutionPolicy&& policy,
ForwardIt first, Size count, const T& value );
|dcl2=
template< class ExecutionPolicy,
class ForwardIt, class Size,
class T = typename std::iterator_traits
<OutputIt>::value_type >
ForwardIt fill_n( ExecutionPolicy&& policy,
ForwardIt first, Size count, const T& value );
```

1. Assigns the given `value` to the first `count` elements in the range beginning at `first` if `count > 0`. Does nothing otherwise.
2. Same as , but executed according to `policy`.
@@
If any of the following conditions is satisfied, the program is ill-formed:
* `value` is not writable to `first`.
* `Size` is not convertible to an integral type.

## Parameters


### Parameters

- `first` - the beginning of the range of elements to modify
- `count` - number of elements to modify
- `value` - the value to be assigned
- `policy` - execution policy

**Type requirements:**

- `OutputIt`
- `ForwardIt`

## Return value

Iterator one past the last element assigned if `count > 0`, `first` otherwise.

## Complexity

Exactly `std::max(0, count)` assignments.

## Exceptions


## Possible implementation

eq impl|ver1=1|title1=fill_n|1=
template<class OutputIt, class Size,
class T = typename std::iterator_traits<OutputIt>::value_type>
OutputIt fill_n(OutputIt first, Size count, const T& value)
{
for (Size i = 0; i < count; i++)
*first++ = value;
return first;
}

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <complex>
#include <iostream>
#include <iterator>
#include <vector>

int main()
{
    std::vector<int> v1{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    // replace values of the first 5 elements with -1
    std::fill_n(v1.begin(), 5, -1);

    std::copy_n(v1.cbegin(), v1.size(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';

    std::vector<std::complex<double>> nums{<!---->{1, 3}, {2, 2}, {4, 8}<!---->};
    #ifdef __cpp_lib_algorithm_default_value_type
        std::fill_n(nums.begin(), 2, {4, 2});
    #else
        std::fill_n(nums.begin(), 2, std::complex<double>{4, 2});
    #endif
    std::copy_n(nums.cbegin(), nums.size(),
                std::ostream_iterator<std::complex<double>>(std::cout, " "));
    std::cout << '\n';
}
```


**Output:**
```
-1 -1 -1 -1 -1 5 6 7 8 9
(4,2) (4,2) (4,8)
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-865 | C++98 | the location of the first element following<br>the filling range was not returned | returned |


## See also


| cpp/algorithm/dsc fill | (see dedicated page) |
| cpp/algorithm/ranges/dsc fill_n | (see dedicated page) |

