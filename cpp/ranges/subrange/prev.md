---
title: std::ranges::subrange::prev
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/subrange/prev
---

ddcl|since=c++20|1=
constexpr subrange prev( std::iter_difference_t<I> n = 1 ) const
requires std::bidirectional_iterator<I>;
Returns a copy of `*this` whose  is decremented (or incremented if `n` is negative). The actual decrement (or increment) operation is performed by .
Equivalent to:c multi
|1=auto tmp = *this;
|2=tmp.advance(-n);
|3=return tmp;
.

## Parameters


### Parameters

- `n` - number of decrements of the iterator

## Return value

As described above.

## Notes

The difference between this function and  is that the latter performs the decrement (or increment) in place.

## Example


### Example

```cpp
#include <iterator>
#include <list>
#include <print>
#include <ranges>

int main()
{
    std::list list{1, 2, 3, 4, 5};
    std::ranges::subrange sub{std::next(list.begin(), 2), std::prev(list.end(), 2)};
    std::println("{} {} {}", sub, sub.prev(), sub.prev(2));
}
```


**Output:**
```
[3] [2, 3] [1, 2, 3]
```


## See also


| cpp/ranges/subrange/dsc next | (see dedicated page) |
| cpp/ranges/subrange/dsc advance | (see dedicated page) |
| cpp/iterator/dsc prev | (see dedicated page) |
| cpp/iterator/ranges/dsc prev | (see dedicated page) |

