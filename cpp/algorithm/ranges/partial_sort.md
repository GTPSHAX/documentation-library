---
title: std::ranges::partial_sort
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/partial_sort
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|num=1|1=
template< std::random_access_iterator I, std::sentinel_for<I> S,
class Comp = ranges::less, class Proj = std::identity >
requires std::sortable<I, Comp, Proj>
constexpr I
partial_sort( I first, I middle, S last, Comp comp = {}, Proj proj = {} );
dcl|since=c++20|num=2|1=
template< ranges::random_access_range R,
class Comp = ranges::less, class Proj = std::identity >
requires std::sortable<ranges::iterator_t<R>, Comp, Proj>
constexpr ranges::borrowed_iterator_t<R>
partial_sort( R&& r, ranges::iterator_t<R> middle, Comp comp = {},
Proj proj = {} );
```

1. Rearranges elements such that the range [first, middle) contains the sorted `middle - first` smallest elements in the range [first, last).
@@ The order of equal elements is ''not'' guaranteed to be preserved. The order of the remaining elements in the range [middle, last) is ''unspecified''.
@@ The elements are compared using the given binary comparison function `comp` and projected using `proj` function object.
2. Same as , but uses `r` as the range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to rearrange, sentinel=yes}})` - 
- `r` - the range of elements to rearrange
- `middle` - the range [first, middle) will be sorted
- `comp` - comparator to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

An iterator equal to `last`.

## Complexity

mathjax-or|\(\scriptsize \mathcal{O}(N\cdot\log{(M)})\)|𝓞(N&middot;log(M)) comparisons and twice as many projections, where  is `ranges::distance(first, last)`,  is `ranges::distance(first, middle)`.

## Possible implementation

eq fun|1=
struct partial_sort_fn
{
template<std::random_access_iterator I, std::sentinel_for<I> S,
class Comp = ranges::less, class Proj = std::identity>
requires std::sortable<I, Comp, Proj>
constexpr I
operator()(I first, I middle, S last, Comp comp = {}, Proj proj = {}) const
{
if (first == middle)
return ranges::next(first, last);
ranges::make_heap(first, middle, comp, proj);
auto it {middle};
for (; it != last; ++it)
{
if (std::invoke(comp, std::invoke(proj, *it), std::invoke(proj, *first)))
{
ranges::pop_heap(first, middle, comp, proj);
ranges::iter_swap(middle - 1, it);
ranges::push_heap(first, middle, comp, proj);
}
}
ranges::sort_heap(first, middle, comp, proj);
return it;
}
template<ranges::random_access_range R, class Comp = ranges::less,
class Proj = std::identity>
requires std::sortable<ranges::iterator_t<R>, Comp, Proj>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, ranges::iterator_t<R> middle, Comp comp = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), std::move(middle), ranges::end(r),
std::move(comp), std::move(proj));
}
};
inline constexpr partial_sort_fn partial_sort {};

## Example


### Example


**Output:**
```
x P y C z w P o
C P P y z x w o
^ ^ ^
3 a 1 b 4 1 c 5
c b a 1 3 1 4 5
^ ^ ^
```


## See also


| cpp/algorithm/ranges/dsc partial_sort_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc stable_sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc nth_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc make_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc pop_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc push_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc sort_heap | (see dedicated page) |
| cpp/algorithm/dsc partial_sort | (see dedicated page) |

