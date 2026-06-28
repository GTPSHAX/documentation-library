---
title: std::ranges::rotate_copy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/rotate_copy
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::forward_iterator I, std::sentinel_for<I> S,
std::weakly_incrementable O >
requires std::indirectly_copyable<I, O>
constexpr rotate_copy_result<I, O>
rotate_copy( I first, I middle, S last, O result );
dcl|num=2|since=c++20|1=
template< ranges::forward_range R, std::weakly_incrementable O >
requires std::indirectly_copyable<ranges::iterator_t<R>, O>
constexpr rotate_copy_result<ranges::borrowed_iterator_t<R>, O>
rotate_copy( R&& r, ranges::iterator_t<R> middle, O result );
dcl|num=3|since=c++20|1=
template< class I, class O >
using rotate_copy_result = in_out_result<I, O>;
```

Copies the ''left rotation'' of [first, last) to `result`.
1. Copies the elements from the source range [first, last), such that in the destination range, the elements in [first, middle) are placed after the elements in [middle, last) while the orders of the elements in both ranges are preserved.
@@ The behavior is undefined if either [first, middle) or [middle, last) is not a valid range, or the source and destination ranges overlap.
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to copy from, range=source)` - 
- `r` - the source range of elements to copy from
- `middle` - the iterator to the element that should appear at the beginning of the destination range
- `result` - beginning of the destination range

## Return value

}, where `1=N = ranges::distance(first, last)`.

## Complexity

''Linear'': exactly `N` assignments.

## Notes

If the value type is *TriviallyCopyable* and the iterator types satisfy , implementations of `ranges::rotate_copy` usually avoid multiple assignments by using a "bulk copy" function such as `std::memmove`.

## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/14d8a5ae472ca5743016f37da2dd4770d83dea21/libstdc%2B%2B-v3/include/bits/ranges_algo.h#L1511-L1539 libstdc++] and [https://github.com/microsoft/STL/blob/472161105d596192194d4715ccad307c6c163b4a/stl/inc/algorithm#L4466-L4514 MSVC STL].
eq fun|1=
struct rotate_copy_fn
{
template<std::forward_iterator I, std::sentinel_for<I> S, std::weakly_incrementable O>
requires std::indirectly_copyable<I, O>
constexpr ranges::rotate_copy_result<I, O>
operator()(I first, I middle, S last, O result) const
{
auto c1 {ranges::copy(middle, std::move(last), std::move(result))};
auto c2 {ranges::copy(std::move(first), std::move(middle), std::move(c1.out))};
return {std::move(c1.in), std::move(c2.out)};
}
template<ranges::forward_range R, std::weakly_incrementable O>
requires std::indirectly_copyable<ranges::iterator_t<R>, O>
constexpr ranges::rotate_copy_result<ranges::borrowed_iterator_t<R>, O>
operator()(R&& r, ranges::iterator_t<R> middle, O result) const
{
return (*this)(ranges::begin(r), std::move(middle),
ranges::end(r), std::move(result));
}
};
inline constexpr rotate_copy_fn rotate_copy {};

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

int main()
{
    std::vector<int> src {1, 2, 3, 4, 5};
    std::vector<int> dest(src.size());
    auto pivot = std::ranges::find(src, 3);

    std::ranges::rotate_copy(src, pivot, dest.begin());
    for (int i : dest)
        std::cout << i << ' ';
    std::cout << '\n';

    // copy the rotation result directly to the std::cout
    pivot = std::ranges::find(dest, 1);
    std::ranges::rotate_copy(dest, pivot, std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';
}
```


**Output:**
```
3 4 5 1 2
1 2 3 4 5
```


## See also


| cpp/algorithm/ranges/dsc rotate | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy | (see dedicated page) |
| cpp/algorithm/dsc rotate_copy | (see dedicated page) |

