---
title: std::is_partitioned
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/is_partitioned
---


```cpp
**Header:** `<`algorithm`>`
|
template< class InputIt, class UnaryPred >
bool is_partitioned( InputIt first, InputIt last, UnaryPred p );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class UnaryPred >
bool is_partitioned( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, UnaryPred p );
```

1. Checks whether [first, last) is partitioned by the predicate `p`: all elements satisfy `p` appear before all elements that do not.
2. Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `policy` - execution policy

**Type requirements:**

- `InputIt`
- `ForwardIt`
- `UnaryPred`

## Return value

`true` if the elements `e` of [first, last) are `partitioned` with respect to the expression `p(e)`. `false` otherwise.

## Complexity

At most `std::distance(first, last)` applications of `p`.

## Exceptions


## Possible implementation

eq fun|1=
template<class InputIt, class UnaryPred>
bool is_partitioned(InputIt first, InputIt last, UnaryPred p)
{
for (; first != last; ++first)
if (!p(*first))
break;
for (; first != last; ++first)
if (p(*first))
return false;
return true;
}

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <iostream>

int main()
{
    std::array<int, 9> v {1, 2, 3, 4, 5, 6, 7, 8, 9};

    auto is_even = [](int i) { return i % 2 == 0; };
    std::cout.setf(std::ios_base::boolalpha);
    std::cout << std::is_partitioned(v.begin(), v.end(), is_even) << ' ';

    std::partition(v.begin(), v.end(), is_even);
    std::cout << std::is_partitioned(v.begin(), v.end(), is_even) << ' ';

    std::reverse(v.begin(), v.end());
    std::cout << std::is_partitioned(v.cbegin(), v.cend(), is_even) << ' ';
    std::cout << std::is_partitioned(v.crbegin(), v.crend(), is_even) << '\n';
}
```


**Output:**
```
false true false true
```


## See also


| cpp/algorithm/dsc partition | (see dedicated page) |
| cpp/algorithm/dsc partition_point | (see dedicated page) |
| cpp/algorithm/ranges/dsc is_partitioned | (see dedicated page) |

