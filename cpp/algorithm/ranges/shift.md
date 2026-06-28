---
title: std::ranges::shift_left
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/shift
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++23|1=
template< std::permutable I, std::sentinel_for<I> S >
constexpr ranges::subrange<I>
shift_left( I first, S last, std::iter_difference_t<I> n );
dcl|num=2|since=c++23|1=
template< ranges::forward_range R >
requires std::permutable<ranges::iterator_t<R>>
constexpr ranges::borrowed_subrange_t<R>
shift_left( R&& r, ranges::range_difference_t<R> n );
dcl|num=3|since=c++23|1=
template< std::permutable I, std::sentinel_for<I> S >
constexpr ranges::subrange<I>
shift_right( I first, S last, std::iter_difference_t<I> n );
dcl|num=4|since=c++23|1=
template< ranges::forward_range R >
requires std::permutable<ranges::iterator_t<R>>
constexpr ranges::borrowed_subrange_t<R>
shift_right( R&& r, ranges::range_difference_t<R> n );
```

Shifts the elements in the range [first, last) or `r` by `n` positions. The behavior is undefined if [first, last) is not a valid range.
1. Shifts the elements towards the beginning of the range:
* If `1=n == 0 , there are no effects.
* If `1=n < 0`, the behavior is undefined.
* Otherwise, for every integer `i` in [0, last - first - n), moves the element originally at position `first + n + i` to position `first + i`. The moves are performed in increasing order of `i` starting from `0`.
3. Shifts the elements towards the end of the range:
* If `1=n == 0 , there are no effects.
* If `1=n < 0`, the behavior is undefined.
* Otherwise, for every integer `i` in [0, last - first - n), moves the element originally at position `first + i` to position `first + n + i`. If `I` models , then the moves are performed in decreasing order of `i` starting from `last - first - n - 1`.
@2,4@ Same as  or  respectively, but uses `r` as the range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.
Elements that are in the original range but not the new range are left in a valid but unspecified state.

## Parameters


### Parameters

- `[3=to shift, sentinel=yes}})` - 
- `r` - the range of elements to shift
- `n` - the number of positions to shift

## Return value

@1,2@ }, where `''NEW_LAST''` is the end of the resulting range and equivalent to:
* `first + (last - first - n)`, if `n` is less than `last - first`;
* `first` otherwise.
@3,4@ }, where `''NEW_FIRST''` is the beginning of the resulting range and equivalent to:
* `first + n`, if `n` is less than `last - first`;
* `last` otherwise.

## Complexity

@1,2@ At most `ranges::distance(first, last) - n` assignments.
@3,4@ At most `ranges::distance(first, last) - n` assignment or swaps.

## Notes

`ranges::shift_left` / `ranges::shift_right` has better efficiency on common implementations if `I` models  or (better) .

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <type_traits>
#include <vector>

struct S
{
    int value{0};
    bool specified_state{true};

    S(int v = 0) : value{v} {}
    S(S const& rhs) = default;
    S(S&& rhs) { *this = std::move(rhs); }
    S& operator=(S const& rhs) = default;
    S& operator=(S&& rhs)
    {
        if (this != &rhs)
        {
            value = rhs.value;
            specified_state = rhs.specified_state;
            rhs.specified_state = false;
        }
        return *this;
    }
};

template<typename T>
std::ostream& operator<<(std::ostream& os, std::vector<T> const& v)
{
    for (const auto& s : v)
    {
        if constexpr (std::is_same_v<T, S>)
            s.specified_state ? os << s.value << ' ' : os << ". ";
        else if constexpr (std::is_same_v<T, std::string>)
            os << (s.empty() ? "." : s) << ' ';
        else
            os << s << ' ';
    }
    return os;
}

int main()
{
    std::cout << std::left;

    std::vector<S> a{1, 2, 3, 4, 5, 6, 7};
    std::vector<int> b{1, 2, 3, 4, 5, 6, 7};
    std::vector<std::string> c{"α", "β", "γ", "δ", "ε", "ζ", "η"};

    std::cout << "vector<S> \tvector<int> \tvector<string>\n";
    std::cout << a << "  " << b << "  " << c << '\n';

    std::ranges::shift_left(a, 3);
    std::ranges::shift_left(b, 3);
    std::ranges::shift_left(c, 3);
    std::cout << a << "  " << b << "  " << c << '\n';

    std::ranges::shift_right(a, 2);
    std::ranges::shift_right(b, 2);
    std::ranges::shift_right(c, 2);
    std::cout << a << "  " << b << "  " << c << '\n';

    std::ranges::shift_left(a, 8); // has no effect: n >= last - first
    std::ranges::shift_left(b, 8); // ditto
    std::ranges::shift_left(c, 8); // ditto
    std::cout << a << "  " << b << "  " << c << '\n';

//  std::ranges::shift_left(a, -3); // UB
}
```


**Output:**
```
vector<S>       vector<int>     vector<string>
1 2 3 4 5 6 7   1 2 3 4 5 6 7   α β γ δ ε ζ η
4 5 6 7 . . .   4 5 6 7 5 6 7   δ ε ζ η . . .
. . 4 5 6 7 .   4 5 4 5 6 7 5   . . δ ε ζ η .
. . 4 5 6 7 .   4 5 4 5 6 7 5   . . δ ε ζ η .
```


## See also


| cpp/algorithm/ranges/dsc move | (see dedicated page) |
| cpp/algorithm/ranges/dsc move_backward | (see dedicated page) |
| cpp/algorithm/ranges/dsc rotate | (see dedicated page) |
| cpp/algorithm/dsc shift | (see dedicated page) |

