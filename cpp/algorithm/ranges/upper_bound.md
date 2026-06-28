---
title: std::ranges::upper_bound
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/upper_bound
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|anchor=Version_1|since1=c++20|until1=c++26
|dcl1=
template< std::forward_iterator I, std::sentinel_for<I> S,
class T, class Proj = std::identity,
std::indirect_strict_weak_order
<const T*, std::projected<I, Proj>> Comp = ranges::less >
constexpr I upper_bound( I first, S last, const T& value,
Comp comp = {}, Proj proj = {} );
|dcl2=
template< std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
class T = std::projected_value_t<I, Proj>,
std::indirect_strict_weak_order
<const T*, std::projected<I, Proj>> Comp = ranges::less >
constexpr I upper_bound( I first, S last, const T& value,
Comp comp = {}, Proj proj = {} );
dcl rev multi|num=2|since1=c++20|until1=c++26
|dcl1=
template< ranges::forward_range R,
class T, class Proj = std::identity,
std::indirect_strict_weak_order
<const T*, std::projected<ranges::iterator_t<R>,
Proj>> Comp = ranges::less >
constexpr ranges::borrowed_iterator_t<R>
upper_bound( R&& r, const T& value, Comp comp = {}, Proj proj = {} );
|dcl2=
template< ranges::forward_range R,
class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj>,
std::indirect_strict_weak_order
<const T*, std::projected<ranges::iterator_t<R>,
Proj>> Comp = ranges::less >
constexpr ranges::borrowed_iterator_t<R>
upper_bound( R&& r, const T& value, Comp comp = {}, Proj proj = {} );
```

1. Returns an iterator pointing to the first element in the range [first, last) that is ''greater'' than `value`, or `last` if no such element is found.
The range [first, last) must be partitioned with respect to the expression or `!comp(value, element)`, i.e., all elements for which the expression is `true` must precede all elements for which the expression is `false`. A fully-sorted range meets this criterion.
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to examine, range=partially-ordered)` - 
- `r` - the partially-ordered range to examine
- `value` - value to compare the elements to
- `pred` - predicate to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

Iterator pointing to the first element that is ''greater'' than `value`, or `last` if no such element is found.

## Complexity

The number of comparisons and applications of the projection performed are logarithmic in the distance between `first` and `last` (at most $log comparisons and applications of the projection). However, for an iterator that does not model , the number of iterator increments is linear.

## Possible implementation

eq fun|1=
struct upper_bound_fn
{
template<std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity, class T = std::projected_value_t<I, Proj>,
std::indirect_strict_weak_order
<const T*, std::projected<I, Proj>> Comp = ranges::less>
constexpr I operator()(I first, S last, const T& value,
Comp comp = {}, Proj proj = {}) const
{
I it;
std::iter_difference_t<I> count, step;
count = ranges::distance(first, last);
while (count > 0)
{
it = first;
step = count / 2;
ranges::advance(it, step, last);
if (!comp(value, std::invoke(proj, *it)))
{
first = ++it;
count -= step + 1;
}
else
count = step;
}
return first;
}
template<ranges::forward_range R, class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj>,
std::indirect_strict_weak_order
<const T*, std::projected<ranges::iterator_t<R>,
Proj>> Comp = ranges::less>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, const T& value, Comp comp = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), value,
std::ref(comp), std::ref(proj));
}
};
inline constexpr upper_bound_fn upper_bound;

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <complex>
#include <iostream>
#include <iterator>
#include <vector>

int main()
{
    namespace ranges = std::ranges;

    std::vector<int> data{1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6};

    {
        auto lower = ranges::lower_bound(data.begin(), data.end(), 4);
        auto upper = ranges::upper_bound(data.begin(), data.end(), 4);

        ranges::copy(lower, upper, std::ostream_iterator<int>(std::cout, " "));
        std::cout << '\n';
    }
    {
        auto lower = ranges::lower_bound(data, 3);
        auto upper = ranges::upper_bound(data, 3);

        ranges::copy(lower, upper, std::ostream_iterator<int>(std::cout, " "));
        std::cout << '\n';
    }

    using CD = std::complex<double>;
    std::vector<CD> nums{<!---->{1, 0}, {2, 2}, {2, 1}, {3, 0}, {3, 1}<!---->};
    auto cmpz = [](CD x, CD y) { return x.real() < y.real(); };
    #ifdef __cpp_lib_algorithm_default_value_type
        auto it = ranges::upper_bound(nums, {2, 0}, cmpz);
    #else
        auto it = ranges::upper_bound(nums, CD{2, 0}, cmpz);
    #endif
    assert((*it == CD{3, 0}));
}
```


**Output:**
```
4 4 4 
3 3 3 3
```


## See also


| cpp/algorithm/ranges/dsc equal_range | (see dedicated page) |
| cpp/algorithm/ranges/dsc lower_bound | (see dedicated page) |
| cpp/algorithm/ranges/dsc partition | (see dedicated page) |
| cpp/algorithm/dsc upper_bound | (see dedicated page) |

