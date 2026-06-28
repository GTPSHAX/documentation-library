---
title: std::ranges::is_partitioned
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/is_partitioned
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::input_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
constexpr bool
is_partitioned( I first, S last, Pred pred, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< ranges::input_range R, class Proj = std::identity,
std::indirect_unary_predicate<
std::projected<ranges::iterator_t<R>, Proj>> Pred >
constexpr bool
is_partitioned( R&& r, Pred pred, Proj proj = {} );
```

1. Returns `true` if all elements in the range [first, last) that satisfy the predicate `pred` after projection appear before all elements that don't. Also returns `true` if [first, last) is empty.
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to examine, sentinel=yes}})` - 
- `r` - the range of elements to examine
- `pred` - predicate to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

`true` if the range [first, last) is empty or is partitioned by `pred`, `false` otherwise.

## Complexity

At most `ranges::distance(first, last)` applications of `pred` and `proj`.

## Possible implementation

eq fun|1=
struct is_partitioned_fn
{
template<std::input_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred>
constexpr bool operator()(I first, S last, Pred pred, Proj proj = {}) const
{
for (; first != last; ++first)
if (!std::invoke(pred, std::invoke(proj, *first)))
break;
for (; first != last; ++first)
if (std::invoke(pred, std::invoke(proj, *first)))
return false;
return true;
}
template<ranges::input_range R, class Proj = std::identity,
std::indirect_unary_predicate<std::projected<ranges::iterator_t<R>, Proj>> Pred>
constexpr bool operator()(R&& r, Pred pred, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::ref(pred), std::ref(proj));
}
};
inline constexpr auto is_partitioned = is_partitioned_fn();

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <numeric>
#include <utility>

int main()
{
    std::array<int, 9> v;

    auto print = [&v](bool o)
    {
        for (int x : v)
            std::cout << x << ' ';
        std::cout << (o ? "=> " : "=> not ") << "partitioned\n";
    };

    auto is_even = [](int i) { return i % 2 == 0; };

    std::iota(v.begin(), v.end(), 1); // or std::ranges::iota(v, 1);
    print(std::ranges::is_partitioned(v, is_even));

    std::ranges::partition(v, is_even);
    print(std::ranges::is_partitioned(std::as_const(v), is_even));

    std::ranges::reverse(v);
    print(std::ranges::is_partitioned(v.cbegin(), v.cend(), is_even));
    print(std::ranges::is_partitioned(v.crbegin(), v.crend(), is_even));
}
```


**Output:**
```
1 2 3 4 5 6 7 8 9 => not partitioned
2 4 6 8 5 3 7 1 9 => partitioned
9 1 7 3 5 8 6 4 2 => not partitioned
9 1 7 3 5 8 6 4 2 => partitioned
```


## See also


| cpp/algorithm/ranges/dsc partition | (see dedicated page) |
| cpp/algorithm/ranges/dsc partition_point | (see dedicated page) |
| cpp/algorithm/dsc is_partitioned | (see dedicated page) |

