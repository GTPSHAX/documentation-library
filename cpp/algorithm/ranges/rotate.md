---
title: std::ranges::rotate
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/rotate
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::permutable I, std::sentinel_for<I> S >
constexpr ranges::subrange<I>
rotate( I first, I middle, S last );
dcl|num=2|since=c++20|1=
template< ranges::forward_range R >
requires std::permutable<ranges::iterator_t<R>>
constexpr ranges::borrowed_subrange_t<R>
rotate( R&& r, ranges::iterator_t<R> middle );
```

1. Performs a ''left rotation'' on a range of elements. Specifically, `ranges::rotate` swaps the elements in the range [first, last) in such a way that the element `*middle` becomes the first element of the new range and `*(middle - 1)` becomes the last element.
@@ The behavior is undefined if [first, last) is not a valid range or `middle` is not in [first, last).
2. Same as , but uses `r` as the range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to rotate, sentinel=yes}})` - 
- `r` - the range of elements to rotate
- `middle` - the iterator to the element that should appear at the beginning of the rotated range

## Return value

}, where `''new_first''` compares equal to `1=ranges::next(first, ranges::distance(middle, last))` and designates a new location of the element pointed by `first`.

## Complexity

''Linear'' at worst: `ranges::distance(first, last)` swaps.

## Notes

`ranges::rotate` has better efficiency on common implementations if `I` models  or (better) .

## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/14d8a5ae472ca5743016f37da2dd4770d83dea21/libstdc%2B%2B-v3/include/bits/ranges_algo.h#L1361-L1506 libstdc++] and [https://github.com/microsoft/STL/blob/472161105d596192194d4715ccad307c6c163b4a/stl/inc/algorithm#L4407-L4434 MSVC STL].
eq fun|1=
struct rotate_fn
{
template<std::permutable I, std::sentinel_for<I> S>
constexpr ranges::subrange<I>
operator()(I first, I middle, S last) const
{
if (first == middle)
{
auto last_it = ranges::next(first, last);
return {last_it, last_it};
}
if (middle == last)
return {std::move(first), std::move(middle)};
if constexpr (std::bidirectional_iterator<I>)
{
ranges::reverse(first, middle);
auto last_it = ranges::next(first, last);
ranges::reverse(middle, last_it);
if constexpr (std::random_access_iterator<I>)
{
ranges::reverse(first, last_it);
return {first + (last_it - middle), std::move(last_it)};
}
else
{
auto mid_last = last_it;
do
{
ranges::iter_swap(first, --mid_last);
++first;
}
while (first != middle && mid_last != middle);
ranges::reverse(first, mid_last);
if (first == middle)
return {std::move(mid_last), std::move(last_it)};
else
return {std::move(first), std::move(last_it)};
}
}
else
{ // I is merely a forward_iterator
auto next_it = middle;
do
{ // rotate the first cycle
ranges::iter_swap(first, next_it);
++first;
++next_it;
if (first == middle)
middle = next_it;
}
while (next_it != last);
auto new_first = first;
while (middle != last)
{ // rotate subsequent cycles
next_it = middle;
do
{
ranges::iter_swap(first, next_it);
++first;
++next_it;
if (first == middle)
middle = next_it;
}
while (next_it != last);
}
return {std::move(new_first), std::move(middle)};
}
}
template<ranges::forward_range R>
requires std::permutable<ranges::iterator_t<R>>
constexpr ranges::borrowed_subrange_t<R>
operator()(R&& r, ranges::iterator_t<R> middle) const
{
return (*this)(ranges::begin(r), std::move(middle), ranges::end(r));
}
};
inline constexpr rotate_fn rotate {};

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

int main()
{
    std::string s(16, ' ');

    for (int k {}; k != 5; ++k)
    {
        std::iota(s.begin(), s.end(), 'A');
        std::ranges::rotate(s, s.begin() + k);
        std::cout << "Rotate left (" << k << "): " << s << '\n';
    }
    std::cout << '\n';

    for (int k {}; k != 5; ++k)
    {
        std::iota(s.begin(), s.end(), 'A');
        std::ranges::rotate(s, s.end() - k);
        std::cout << "Rotate right (" << k << "): " << s << '\n';
    }

    std::cout << "\nInsertion sort using `rotate`, step-by-step:\n";

    s = {'2', '4', '2', '0', '5', '9', '7', '3', '7', '1'};

    for (auto i = s.begin(); i != s.end(); ++i)
    {
        std::cout << "i = " << std::ranges::distance(s.begin(), i) << ": ";
        std::ranges::rotate(std::ranges::upper_bound(s.begin(), i, *i), i, i + 1);
        std::cout << s << '\n';
    }
    std::cout << (std::ranges::is_sorted(s) ? "Sorted!" : "Not sorted.") << '\n';
}
```


**Output:**
```
Rotate left (0): ABCDEFGHIJKLMNOP
Rotate left (1): BCDEFGHIJKLMNOPA
Rotate left (2): CDEFGHIJKLMNOPAB
Rotate left (3): DEFGHIJKLMNOPABC
Rotate left (4): EFGHIJKLMNOPABCD

Rotate right (0): ABCDEFGHIJKLMNOP
Rotate right (1): PABCDEFGHIJKLMNO
Rotate right (2): OPABCDEFGHIJKLMN
Rotate right (3): NOPABCDEFGHIJKLM
Rotate right (4): MNOPABCDEFGHIJKL

Insertion sort using `rotate`, step-by-step:
i = 0: 2420597371
i = 1: 2420597371
i = 2: 2240597371
i = 3: 0224597371
i = 4: 0224597371
i = 5: 0224597371
i = 6: 0224579371
i = 7: 0223457971
i = 8: 0223457791
i = 9: 0122345779
Sorted!
```


## See also


| cpp/algorithm/ranges/dsc rotate_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc reverse | (see dedicated page) |
| cpp/algorithm/dsc rotate | (see dedicated page) |

