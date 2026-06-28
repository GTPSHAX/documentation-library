---
title: std::ranges::reverse
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/reverse
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::bidirectional_iterator I, std::sentinel_for<I> S >
requires std::permutable<I>
constexpr I
reverse( I first, S last );
dcl|num=2|since=c++20|1=
template< ranges::bidirectional_range R >
requires std::permutable<ranges::iterator_t<R>>
constexpr ranges::borrowed_iterator_t<R>
reverse( R&& r );
```

1. Reverses the order of the elements in the range [first, last).
@@ Behaves as if applying `ranges::iter_swap` to every pair of iterators `first + i, last - i - 1` for each integer `i`, where `1=0 ≤ i < (last - first) / 2`.
2. Same as , but uses `r` as the range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to reverse, sentinel=yes}})` - 
- `r` - the range of elements to reverse

## Return value

An iterator equal to `last`.

## Complexity

Exactly `(last - first) / 2` swaps.

## Notes


## Possible implementation

See also implementations in [https://github.com/gcc-mirror/gcc/blob/14d8a5ae472ca5743016f37da2dd4770d83dea21/libstdc%2B%2B-v3/include/bits/ranges_algo.h#L1278-L1325 libstdc++] and [https://github.com/microsoft/STL/blob/472161105d596192194d4715ccad307c6c163b4a/stl/inc/algorithm#L4154-L4180 MSVC STL].
eq fun|1=
struct reverse_fn
{
template<std::bidirectional_iterator I, std::sentinel_for<I> S>
requires std::permutable<I>
constexpr I operator()(I first, S last) const
{
auto last2 {ranges::next(first, last)};
for (auto tail {last2}; !(first == tail or first == --tail); ++first)
ranges::iter_swap(first, tail);
return last2;
}
template<ranges::bidirectional_range R>
requires std::permutable<ranges::iterator_t<R>>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r) const
{
return (*this)(ranges::begin(r), ranges::end(r));
}
};
inline constexpr reverse_fn reverse {};

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string>

int main()
{
    std::string s {"ABCDEF"};
    std::cout << s << " → ";
    std::ranges::reverse(s.begin(), s.end());
    std::cout << s << " → ";
    std::ranges::reverse(s);
    std::cout << s << " │ ";

    std::array a {1, 2, 3, 4, 5};
    for (auto e : a)
        std::cout << e << ' ';
    std::cout << "→ ";
    std::ranges::reverse(a);
    for (auto e : a)
        std::cout << e << ' ';
    std::cout << '\n';
}
```


**Output:**
```
ABCDEF → FEDCBA → ABCDEF │ 1 2 3 4 5 → 5 4 3 2 1
```


## See also


| cpp/algorithm/ranges/dsc reverse_copy | (see dedicated page) |
| cpp/ranges/dsc reverse_view | (see dedicated page) |
| cpp/algorithm/dsc reverse | (see dedicated page) |

