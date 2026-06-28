---
title: std::reverse
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/reverse
---


```cpp
**Header:** `<`algorithm`>`
|
template< class BidirIt >
void reverse( BidirIt first, BidirIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class BidirIt >
void reverse( ExecutionPolicy&& policy, BidirIt first, BidirIt last );
```

1. Reverses the order of the elements in the range [first, last).
@@ Behaves as if applying `std::iter_swap` to every pair of iterators `first + i` and `(last - i) - 1` for each integer `i` in [0, std::distance(first, last) / 2).
2. Same as , but executed according to `policy`.
@@
If <sup>(until C++20)</sup> `*first` is not *Swappable*<sup>(since C++20)</sup> `BidirIt` is not *ValueSwappable*, the behavior is undefined.

## Parameters


### Parameters

- `policy` - execution policy

**Type requirements:**

- `BidirIt`

## Complexity

Exactly `std::distance(first, last) / 2` swaps.

## Exceptions


## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/14d8a5ae472ca5743016f37da2dd4770d83dea21/libstdc%2B%2B-v3/include/bits/stl_algo.h#L1087-L1152 libstdc++], [https://github.com/llvm/llvm-project/blob/6adbc83ee9e46b476e0f75d5671c3a21f675a936/libcxx/include/__algorithm/reverse.h libc++], and [https://github.com/microsoft/STL/blob/472161105d596192194d4715ccad307c6c163b4a/stl/inc/xutility#L5335-L5370 MSVC STL].
eq fun|1=
template<class BidirIt>
constexpr // since C++20
void reverse(BidirIt first, BidirIt last)
{
using iter_cat = typename std::iterator_traits<BidirIt>::iterator_category;
// Tag dispatch, e.g. calling reverse_impl(first, last, iter_cat()),
// can be used in C++14 and earlier modes.
if constexpr (std::is_base_of_v<std::random_access_iterator_tag, iter_cat>)
{
if (first == last)
return;
for (--last; first < last; (void)++first, --last)
std::iter_swap(first, last);
}
else
while (first != last && first != --last)
std::iter_swap(first++, last);
}

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

void println(auto rem, auto const& v)
{
    for (std::cout << rem; auto e : v)
        std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    std::vector<int> v {1, 2, 3};
    std::reverse(v.begin(), v.end());
    println("after reverse, v = ", v);

    int a[] = {4, 5, 6, 7};
    std::reverse(std::begin(a), std::end(a));
    println("after reverse, a = ", a);
}
```


**Output:**
```
after reverse, v = 3 2 1
after reverse, a = 7 6 5 4
```


## Defect reports


## See also


| cpp/algorithm/dsc reverse_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc reverse | (see dedicated page) |

