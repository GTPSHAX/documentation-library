---
title: std::copy_backward
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/copy_backward
---

ddcl|header=algorithm|notes=<sup>(constexpr C++20)</sup>|
template< class BidirIt1, class BidirIt2 >
BidirIt2 copy_backward( BidirIt1 first, BidirIt1 last, BidirIt2 d_last );
Copies the elements from the range [first, last) to another range ending at `d_last`. The elements are copied in reverse order (the last element is copied first), but their relative order is preserved.
The behavior is undefined if `d_last` is within [first, last|left=(|right=]). `std::copy` must be used instead of `std::copy_backward` in that case.

## Parameters


### Parameters

- `[3=to copy from, range=source}})` - 
- `d_last` - the end of the destination range

**Type requirements:**

- `BidirIt`

## Return value

Iterator to the last element copied.

## Complexity

Exactly `std::distance(first, last)` assignments.

## Notes

When copying overlapping ranges, `std::copy` is appropriate when copying to the left (beginning of the destination range is outside the source range) while `std::copy_backward` is appropriate when copying to the right (end of the destination range is outside the source range).

## Possible implementation

eq fun|1=
template<class BidirIt1, class BidirIt2>
BidirIt2 copy_backward(BidirIt1 first, BidirIt1 last, BidirIt2 d_last)
{
while (first != last)
*(--d_last) = *(--last);
return d_last;
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

int main()
{
    std::vector<int> source(4);
    std::iota(source.begin(), source.end(), 1); // fills with 1, 2, 3, 4

    std::vector<int> destination(6);

    std::copy_backward(source.begin(), source.end(), destination.end());

    std::cout << "destination contains: ";
    for (auto i: destination)
        std::cout << i << ' ';
    std::cout << '\n';
}
```


**Output:**
```
destination contains: 0 0 1 2 3 4
```


## Defect reports


## See also


| cpp/algorithm/dsc copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy_backward | (see dedicated page) |

