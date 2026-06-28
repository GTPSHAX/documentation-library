---
title: std::ranges::copy_backward
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/copy_backward
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|num=1|1=
template< std::bidirectional_iterator I1, std::sentinel_for<I1> S1,
std::bidirectional_iterator I2 >
requires std::indirectly_copyable<I1, I2>
constexpr copy_backward_result<I1, I2>
copy_backward( I1 first, S1 last, I2 d_last );
dcl|since=c++20|num=2|1=
template< ranges::bidirectional_range R, std::bidirectional_iterator I >
requires std::indirectly_copyable<ranges::iterator_t<R>, I>
constexpr copy_backward_result<ranges::borrowed_iterator_t<R>, I>
copy_backward( R&& r, I d_last );
dcl|since=c++20|num=3|1=
template< class I1, class I2 >
using copy_backward_result = ranges::in_out_result<I1, I2>;
```

1. Copies the elements from the range, defined by [first, last), to another range [d_last - N, d_last), where `1=N = ranges::distance(first, last)`. The elements are copied in reverse order (the last element is copied first), but their relative order is preserved. The behavior is undefined if `d_last` is within `'''('''`first`, `last`''']'''`. In such a case `std::ranges::copy` can be used instead.
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first`, and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to copy from, sentinel=yes}})` - 
- `r` - the range of the elements to copy from
- `d_last` - the end of the destination range

## Return value

}

## Complexity

Exactly `N` assignments.

## Notes

When copying overlapping ranges, `ranges::copy` is appropriate when copying to the left (beginning of the destination range is outside the source range) while `ranges::copy_backward` is appropriate when copying to the right (end of the destination range is outside the source range).

## Possible implementation

eq fun|1=
struct copy_backward_fn
{
template<std::bidirectional_iterator I1, std::sentinel_for<I1> S1,
std::bidirectional_iterator I2>
requires std::indirectly_copyable<I1, I2>
constexpr ranges::copy_backward_result<I1, I2>
operator()(I1 first, S1 last, I2 d_last) const
{
I1 last1 {ranges::next(first, std::move(last))};
for (I1 i {last1}; i != first;)
*--d_last = *--i;
return {std::move(last1), std::move(d_last)};
}
template<ranges::bidirectional_range R, std::bidirectional_iterator I>
requires std::indirectly_copyable<ranges::iterator_t<R>, I>
constexpr ranges::copy_backward_result<ranges::borrowed_iterator_t<R>, I>
operator()(R&& r, I d_last) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(d_last));
}
};
inline constexpr copy_backward_fn copy_backward{};

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <ranges>
#include <string_view>
#include <vector>

void print(std::string_view rem, std::ranges::forward_range auto const& r)
{
    for (std::cout << rem << ": "; auto const& elem : r)
        std::cout << elem << ' ';
    std::cout << '\n';
}

int main()
{
    const auto src = {1, 2, 3, 4};
    print("src", src);

    std::vector<int> dst(src.size() + 2);
    std::ranges::copy_backward(src, dst.end());
    print("dst", dst);

    std::ranges::fill(dst, 0);
    const auto [in, out] =
        std::ranges::copy_backward(src.begin(), src.end() - 2, dst.end());
    print("dst", dst);

    std::cout
        << "(in - src.begin) == " << std::distance(src.begin(), in) << '\n'
        << "(out - dst.begin) == " << std::distance(dst.begin(), out) << '\n';
}
```


**Output:**
```
src: 1 2 3 4
dst: 0 0 1 2 3 4
dst: 0 0 0 0 1 2
(in - src.begin) == 2
(out - dst.begin) == 4
```


## See also


| cpp/algorithm/ranges/dsc copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy_n | (see dedicated page) |
| cpp/algorithm/ranges/dsc remove_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc replace_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc reverse_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc rotate_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc unique_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc move | (see dedicated page) |
| cpp/algorithm/ranges/dsc move_backward | (see dedicated page) |
| cpp/algorithm/dsc copy_backward | (see dedicated page) |

