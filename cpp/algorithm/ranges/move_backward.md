---
title: std::ranges::move_backward
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/move_backward
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|num=1|1=
template< std::bidirectional_iterator I1, std::sentinel_for<I1> S1,
std::bidirectional_iterator I2 >
requires std::indirectly_movable<I1, I2>
constexpr move_backward_result<I1, I2>
move_backward( I1 first, S1 last, I2 d_last );
dcl|since=c++20|num=2|1=
template< ranges::bidirectional_range R, std::bidirectional_iterator I >
requires std::indirectly_movable<ranges::iterator_t<R>, I>
constexpr move_backward_result<ranges::borrowed_iterator_t<R>, I>
move_backward( R&& r, I d_last );
dcl|since=c++20|num=3|1=
template< class I, class O >
using move_backward_result = ranges::in_out_result<I, O>;
```

1. Moves the elements in the range, defined by [first, last), to another range [d_last - N, d_last), where `1=N = ranges::distance(first, last)`. The elements are moved in reverse order (the last element is moved first), but their relative order is preserved. The behavior is undefined if `d_last` is within `'''('''first, last''']'''`. In such a case, `ranges::move` may be used instead.
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first`, and `ranges::end(r)` as `last`.
The elements in the ''moved-from'' range will still contain valid values of the appropriate type, but not necessarily the same values as before the move, as if using `1=*(d_last - n) = ranges::iter_move(last - n)` for each integer `n`, where `1=0 ≤ n < N`.

## Parameters


### Parameters

- `[3=to move, sentinel=yes}})` - 
- `r` - the range of the elements to move
- `d_last` - the end of the destination range

## Return value

}.

## Complexity

1. Exactly `N` move assignments.
2. Exactly `ranges::distance(r)` move assignments.

## Notes

When moving overlapping ranges, `ranges::move` is appropriate when moving to the left (beginning of the destination range is outside the source range) while `ranges::move_backward` is appropriate when moving to the right (end of the destination range is outside the source range).

## Possible implementation

eq fun|1=
struct move_backward_fn
{
template<std::bidirectional_iterator I1, std::sentinel_for<I1> S1,
std::bidirectional_iterator I2>
requires std::indirectly_movable<I1, I2>
constexpr ranges::move_backward_result<I1, I2>
operator()(I1 first, S1 last, I2 d_last) const
{
auto i {last};
for (; i != first; *--d_last = ranges::iter_move(--i))
{}
return {std::move(last), std::move(d_last)};
}
template<ranges::bidirectional_range R, std::bidirectional_iterator I>
requires std::indirectly_movable<ranges::iterator_t<R>, I>
constexpr ranges::move_backward_result<ranges::borrowed_iterator_t<R>, I>
operator()(R&& r, I d_last) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(d_last));
}
};
inline constexpr move_backward_fn move_backward {};

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

using Vec = std::vector<std::string>;

void print(std::string_view rem, Vec const& vec)
{
    std::cout << rem << "[" << vec.size() << "]: ";
    for (const std::string& s : vec)
        std::cout << (s.size() ? s : std::string{"·"}) << ' ';
    std::cout << '\n';
}

int main()
{
    Vec a{"▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"};
    Vec b(a.size());

    print("Before move:\n" "a", a);
    print("b", b);

    std::ranges::move_backward(a, b.end());

    print("\n" "Move a >> b:\n" "a", a);
    print("b", b);

    std::ranges::move_backward(b.begin(), b.end(), a.end());
    print("\n" "Move b >> a:\n" "a", a);
    print("b", b);

    std::ranges::move_backward(a.begin(), a.begin()+3, a.end());
    print("\n" "Overlapping move a[0, 3) >> a[5, 8):\n" "a", a);
}
```


**Output:**
```
Before move:
a[8]: ▁ ▂ ▃ ▄ ▅ ▆ ▇ █
b[8]: · · · · · · · ·

Move a >> b:
a[8]: · · · · · · · ·
b[8]: ▁ ▂ ▃ ▄ ▅ ▆ ▇ █

Move b >> a:
a[8]: ▁ ▂ ▃ ▄ ▅ ▆ ▇ █
b[8]: · · · · · · · ·

Overlapping move a[0, 3) >> a[5, 8):
a[8]: · · · ▄ ▅ ▁ ▂ ▃
```


## See also


| cpp/algorithm/ranges/dsc move | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy_backward | (see dedicated page) |
| cpp/algorithm/dsc move | (see dedicated page) |
| cpp/utility/dsc move | (see dedicated page) |

