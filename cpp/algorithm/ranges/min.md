---
title: std::ranges::min
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/min
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< class T, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<const T*, Proj>> Comp = ranges::less >
constexpr const T&
min( const T& a, const T& b, Comp comp = {}, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< std::copyable T, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<const T*, Proj>> Comp = ranges::less >
constexpr T
min( std::initializer_list<T> r, Comp comp = {}, Proj proj = {} );
dcl|num=3|since=c++20|1=
template< ranges::input_range R, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<ranges::iterator_t<R>, Proj>> Comp = ranges::less >
requires std::indirectly_copyable_storable<ranges::iterator_t<R>,
ranges::range_value_t<R>*>
constexpr ranges::range_value_t<R>
min( R&& r, Comp comp = {}, Proj proj = {} );
```

Returns the smaller of the given projected elements.
1. Returns the smaller of `a` and `b`.
2. Returns the first smallest element in the initializer list `r`.
3. Returns the first smallest value in the range `r`.

## Parameters


### Parameters

- `a, b` - the values to compare
- `r` - the range of values to compare
- `comp` - comparison to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

1. The smaller of `a` and `b`, according to the projection. If they are equivalent, returns `a`.
@2,3@ The smallest element in `r`, according to the projection. If several values are equivalent to the smallest, returns the leftmost one. If the range is empty (as determined by `ranges::distance(r)`), the behavior is undefined.

## Complexity

1. Exactly one comparison.
@2,3@ Exactly `ranges::distance(r) - 1` comparisons.

## Possible implementation

eq fun
|1=
struct min_fn
{
template<class T, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<const T*, Proj>> Comp = ranges::less>
constexpr
const T& operator()(const T& a, const T& b, Comp comp = {}, Proj proj = {}) const
{
return std::invoke(comp, std::invoke(proj, b), std::invoke(proj, a)) ? b : a;
}
template<std::copyable T, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<const T*, Proj>> Comp = ranges::less>
constexpr
T operator()(std::initializer_list<T> r, Comp comp = {}, Proj proj = {}) const
{
return *ranges::min_element(r, std::ref(comp), std::ref(proj));
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
static_cast<V>(*ranges::min_element(r, std::ref(comp), std::ref(proj)));
else
{
auto i = ranges::begin(r);
auto s = ranges::end(r);
V m(*i);
while (++i != s)
if (std::invoke(comp, std::invoke(proj, *i), std::invoke(proj, m)))
m = *i;
return m;
}
}
};
inline constexpr min_fn min;

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <string>

int main()
{
    namespace ranges = std::ranges;
    using namespace std::string_view_literals;

    std::cout << "smaller of 1 and 9999: " << ranges::min(1, 9999) << '\n'
              << "smaller of 'a', and 'b': '" << ranges::min('a', 'b') << "'\n"
              << "shortest of \"foo\", \"bar\", and \"hello\": \""
              << ranges::min({"foo"sv, "bar"sv, "hello"sv}, {},
                             &std::string_view::size) << "\"\n";
}
```


**Output:**
```
smaller of 1 and 9999: 1
smaller of 'a', and 'b': 'a'
shortest of "foo", "bar", and "hello": "foo"
```


## See also


| cpp/algorithm/ranges/dsc max | (see dedicated page) |
| cpp/algorithm/ranges/dsc minmax | (see dedicated page) |
| cpp/algorithm/ranges/dsc min_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc clamp | (see dedicated page) |
| cpp/algorithm/dsc min | (see dedicated page) |

