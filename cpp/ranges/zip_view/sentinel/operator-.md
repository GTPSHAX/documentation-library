---
title: operator-(ranges::zip_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_view/sentinel/operator-
---


# operator-small|(ranges::zip_view::''sentinel'')


```cpp
dcl|num=1|since=c++23|
template< bool OtherConst >
requires (std::sized_sentinel_for<
ranges::sentinel_t</*maybe-const*/<Const, Views>>,
ranges::iterator_t</*maybe-const*/<OtherConst, Views>>> && ...)
friend constexpr
std::common_type_t<ranges::range_difference_t</*maybe-const*/<OtherConst, Views>>...>
operator-( const iterator<OtherConst>& x, const sentinel& y );
dcl|num=2|since=c++23|
template< bool OtherConst >
requires (std::sized_sentinel_for<
ranges::sentinel_t</*maybe-const*/<Const, Views>>,
ranges::iterator_t</*maybe-const*/<OtherConst, Views>>> && ...)
friend constexpr
std::common_type_t<ranges::range_difference_t</*maybe-const*/<OtherConst, Views>>...>
operator-( const sentinel& y, const iterator<OtherConst>& x );
```

Computes the minimal distance between the underlying tuple of iterators of `x` and the underlying tuple of sentinels of `y`.

## Parameters


### Parameters

- `x` - an 
- `y` - a 

## Return value

Let  denote the underlying tuple of iterators of `x`, and  denote the underlying tuple of sentinels of `y`.
Let `''DIST''(x, y, i)` be a distance calculated by expression equivalent to `std::get<i>(x.current_) - std::get<i>(y.end_)` for some integer `i`.
1. the value with the smallest absolute value among `''DIST''(x, y, i)` of all `i` in range `0 ≤ i < sizeof...(Views)`
2. `1= -(x - y)`.

## Example


### Example

```cpp
#include <cassert>
#include <deque>
#include <list>
#include <ranges>
#include <vector>

int main()
{
    auto x = std::vector{1, 2, 3, 4};
    auto y = std::deque{'a', 'b', 'c'};
    auto z = {1.1, 2.2};
    auto w = std::list{1, 2, 3};

    auto p = std::views::zip(x, y, z);
    assert(p.begin() - p.end() == +2);
    assert(p.end() - p.begin() == -2);

    [[maybe_unused]]
    auto q = std::views::zip(x, y, w);

    // The following code fires a compile-time error because std::list::iterator
    // does not support operator- that is needed to calculate the distance:
    // auto e = q.begin() - q.end();
}
```

