---
title: std::partition_copy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/partition_copy
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|since=c++11|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt, class OutputIt1,
class OutputIt2, class UnaryPred >
std::pair<OutputIt1, OutputIt2>
partition_copy( InputIt first, InputIt last,
OutputIt1 d_first_true, OutputIt2 d_first_false,
UnaryPred p );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt1, class ForwardIt2,
class ForwardIt3, class UnaryPred >
std::pair<ForwardIt2, ForwardIt3>
partition_copy( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last,
ForwardIt2 d_first_true, ForwardIt3 d_first_false,
UnaryPred p );
```

1. Copies the elements from the range [first, last) to two different ranges depending on the value returned by the predicate `p`.
* The elements that satisfy the predicate `p` are copied to the range beginning at `d_first_true`.
* The rest of the elements are copied to the range beginning at `d_first_false`.
2. Same as , but executed according to `policy`.
@@
If `*first` is not writable to `d_first_true` or `d_first_false`, the program is ill-formed.
Among the input range and the two output ranges, if any two ranges overlap, the behavior is undefined.

## Parameters


### Parameters

- `[3=to copy from, range=source}})` - 
- `d_first_true` - the beginning of the output range for the elements that satisfy `p`
- `d_first_false` - the beginning of the output range for the elements that do not satisfy `p`
- `policy` - execution policy

**Type requirements:**

- `InputIt`
- `OutputIt1, OutputIt2`
- `ForwardIt1, ForwardIt2, ForwardIt3`
- `UnaryPred`

## Return value

A `std::pair` constructed from the iterator to the end of the `d_first_true` range and the iterator to the end of the `d_first_false` range.

## Complexity

Exactly `std::distance(first, last)` applications of `p`.
For the overload , there may be a performance cost if `ForwardIt`'s value type is not *CopyConstructible*.

## Exceptions


## Possible implementation

eq impl|title1=partition_copy (1)|ver1=1|1=
template<class InputIt, class OutputIt1,
class OutputIt2, class UnaryPred>
constexpr //< since C++20
std::pair<OutputIt1, OutputIt2>
partition_copy(InputIt first, InputIt last,
OutputIt1 d_first_true, OutputIt2 d_first_false,
UnaryPred p)
{
for (; first != last; ++first)
{
if (p(*first))
{
*d_first_true = *first;
++d_first_true;
}
else
{
*d_first_false = *first;
++d_first_false;
}
}
return std::pair<OutputIt1, OutputIt2>(d_first_true, d_first_false);
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <utility>

void print(auto rem, const auto& v)
{
    for (std::cout << rem; const auto& x : v)
        std::cout << x << ' ';
    std::cout << '\n';
}

int main()
{
    int arr[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int true_arr[5] = {0};
    int false_arr[5] = {0};

    std::partition_copy(std::begin(arr), std::end(arr),
                        std::begin(true_arr), std::begin(false_arr),
                        [](int i) { return 4 < i; });

    print("true_arr:  ", true_arr);
    print("false_arr: ", false_arr);
}
```


**Output:**
```
true_arr:  5 6 7 8 9
false_arr: 0 1 2 3 4
```


## Defect reports


## See also


| cpp/algorithm/dsc partition | (see dedicated page) |
| cpp/algorithm/dsc stable_partition | (see dedicated page) |
| cpp/algorithm/dsc copy | (see dedicated page) |
| cpp/algorithm/dsc remove_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc partition_copy | (see dedicated page) |

