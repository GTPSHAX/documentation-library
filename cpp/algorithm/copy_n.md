---
title: std::copy_n
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/copy_n
---


```cpp
**Header:** `<`algorithm`>`
|
template< class InputIt, class Size, class OutputIt >
OutputIt copy_n( InputIt first, Size count, OutputIt result );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class Size, class ForwardIt2 >
ForwardIt2 copy_n( ExecutionPolicy&& policy,
ForwardIt1 first, Size count, ForwardIt2 result );
```

1. Copies exactly `count` values from the range beginning at `first` to the range beginning at `result`. Formally, for each integer `i` in [0, count), performs `1=*(result + i) = *(first + i)`.
@@ Overlap of ranges is formally permitted, but leads to unpredictable ordering of the results.
2. Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `first` - the beginning of the range of elements to copy from
- `count` - number of the elements to copy
- `result` - the beginning of the destination range
- `policy` - execution policy

**Type requirements:**

- `InputIt`
- `OutputIt`
- `ForwardIt1, ForwardIt2`

## Return value

Iterator in the destination range, pointing past the last element copied if `count > 0` or `result` otherwise.

## Complexity

Zero assignments if `count < 0`; `count` assignments otherwise.

## Exceptions


## Possible implementation

eq fun|1=
template<class InputIt, class Size, class OutputIt>
constexpr //< since C++20
OutputIt copy_n(InputIt first, Size count, OutputIt result)
{
if (count > 0)
{
*result = *first;
++result;
for (Size i = 1; i != count; ++i, (void)++result)
*result = *++first;
}
return result;
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <string>
#include <vector>

int main()
{
    std::string in {"1234567890"};
    std::string out;

    std::copy_n(in.begin(), 4, std::back_inserter(out));
    std::cout << out << '\n';

    std::vector<int> v_in(128);
    std::iota(v_in.begin(), v_in.end(), 1);
    std::vector<int> v_out(v_in.size());

    std::copy_n(v_in.cbegin(), 100, v_out.begin());
    std::cout << std::accumulate(v_out.begin(), v_out.end(), 0) << '\n';
}
```


**Output:**
```
1234
5050
```


## See also


| cpp/algorithm/dsc copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy_n | (see dedicated page) |

