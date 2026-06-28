---
title: std::ranges::max
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/max
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< class T, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<const T*, Proj>> Comp = ranges::less >
constexpr const T&
max( const T& a, const T& b, Comp comp = {}, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< std::copyable T, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<const T*, Proj>> Comp = ranges::less >
constexpr T
max( std::initializer_list<T> r, Comp comp = {}, Proj proj = {} );
dcl|num=3|since=c++20|1=
template< ranges::input_range R, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<ranges::iterator_t<R>, Proj>> Comp = ranges::less >
requires std::indirectly_copyable_storable<ranges::iterator_t<R>,
ranges::range_value_t<R>*>
constexpr ranges::range_value_t<R>
max( R&& r, Comp comp = {}, Proj proj = {} );
```

Returns the greater of the given projected values.
1. Returns the greater of `a` and `b`.
2. Returns the first greatest value in the initializer list `r`.
3. Returns the first greatest value in the range `r`.

## Parameters


### Parameters

- `a, b` - the values to compare
- `r` - the range of values to compare
- `comp` - comparison to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

1. The greater of `a` and `b`, according to their respective projected values. If they are equivalent, returns `a`.
@2,3@ The greatest value in `r`, according to the projection. If several values are equivalent to the greatest, returns the leftmost one. If the range is empty (as determined by `ranges::distance(r)`), the behavior is undefined.

## Complexity

1. Exactly one comparison.
@2,3@ Exactly `ranges::distance(r) - 1` comparisons.

## Possible implementation

eq fun
|1=
struct max_fn
{
template<class T, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<const T*, Proj>> Comp = ranges::less>
constexpr
const T& operator()(const T& a, const T& b, Comp comp = {}, Proj proj = {}) const
{
return std::invoke(comp, std::invoke(proj, a), std::invoke(proj, b)) ? b : a;
}
template<std::copyable T, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<const T*, Proj>> Comp = ranges::less>
constexpr
T operator()(std::initializer_list<T> r, Comp comp = {}, Proj proj = {}) const
{
return *ranges::max_element(r, std::ref(comp), std::ref(proj));
}
template<ranges::input_range R, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<ranges::iterator_t<R>, Proj>> Comp = ranges::less>
requires std::indirectly_copyable_storable<ranges::iterator_t<R>,
ranges::range_value_t<R>*>
constexpr
ranges::range_value_t<R> operator()(R&& r, Comp comp = {}, Proj proj = {}) const
{
using V = ranges::range_value_t<R>;
if constexpr (ranges::forward_range<R>)
return
static_cast<V>(*ranges::max_element(r, std::ref(comp), std::ref(proj)));
else
{
auto i = ranges::begin(r);
auto s = ranges::end(r);
V m(*i);
while (++i != s)
if (std::invoke(comp, std::invoke(proj, m), std::invoke(proj, *i)))
m = *i;
return m;
}
}
};
inline constexpr max_fn max;

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <string>

static_assert(std::ranges::max({0B10, 0X10, 010, 10}) == 16); // overload (2)

int main()
{
    namespace ranges = std::ranges;
    using namespace std::string_view_literals;

    std::cout << "larger of 1 and 9999: " << ranges::max(1, 9999) << '\n'
              << "larger of 'a', and 'b': '" << ranges::max('a', 'b') << "'\n"
              << "longest of \"foo\", \"bar\", and \"hello\": \""
              << ranges::max({"foo"sv, "bar"sv, "hello"sv}, {},
                             &std::string_view::size) << "\"\n";
}
```


**Output:**
```
larger of 1 and 9999: 9999
larger of 'a', and 'b': 'b'
longest of "foo", "bar", and "hello": "hello"
```


## See also


| cpp/algorithm/ranges/dsc min | (see dedicated page) |
| cpp/algorithm/ranges/dsc minmax | (see dedicated page) |
| cpp/algorithm/ranges/dsc max_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc clamp | (see dedicated page) |
| cpp/algorithm/dsc max | (see dedicated page) |

