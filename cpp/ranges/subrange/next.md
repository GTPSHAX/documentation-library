---
title: std::ranges::subrange::next
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/subrange/next
---


```cpp
dcl|num=1|since=c++20|1=
constexpr subrange next( std::iter_difference_t<I> n = 1 ) const&
requires std::forward_iterator<I>;
dcla|num=2|since=c++20|1=
constexpr subrange next( std::iter_difference_t<I> n = 1 ) &&;
```

Returns a `subrange` whose  is incremented (or decremented if `n` is negative). The actual increment (or decrement) operation is performed by .
1. Returns a copy of `*this`.
@@ Equivalent to: c multi
|1=auto tmp = *this;
|2=tmp.advance(n);
|3=return tmp;
.
2. Returns a `subrange` moved from `*this`.
@@ Equivalent to: c multi
|1=advance(n);
|2=return std::move(*this);
.

## Parameter


### Parameters

- `n` - number of maximal increments of the iterator

## Return value

As described above.

## Notes

The difference between this function and  is that the latter performs the increment (or decrement) in place.

## Example


### Example

```cpp
#include <array>
#include <iterator>
#include <print>
#include <ranges>

int main()
{
    std::array arr{1, 2, 3, 4, 5, 6, 7};
    std::ranges::subrange sub{std::next(arr.begin(), 2), std::prev(arr.end(), 2)};
    std::println("1) sub: {}", sub);
    std::println("2) sub: {}", sub.next());
    std::println("3) sub: {}", sub.next(2));
}
```


**Output:**
```
1) sub: [3, 4, 5]
2) sub: [4, 5]
3) sub: [5]
```


## See also


| cpp/ranges/subrange/dsc prev | (see dedicated page) |
| cpp/ranges/subrange/dsc advance | (see dedicated page) |
| cpp/iterator/dsc next | (see dedicated page) |
| cpp/iterator/ranges/dsc next | (see dedicated page) |

