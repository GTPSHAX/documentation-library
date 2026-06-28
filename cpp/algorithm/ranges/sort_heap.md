---
title: std::ranges::sort_heap
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/sort_heap
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::random_access_iterator I, std::sentinel_for<I> S,
class Comp = ranges::less, class Proj = std::identity >
requires std::sortable<I, Comp, Proj>
constexpr I sort_heap( I first, S last, Comp comp = {}, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< ranges::random_access_range R,
class Comp = ranges::less, class Proj = std::identity >
requires std::sortable<ranges::iterator_t<R>, Comp, Proj>
constexpr ranges::borrowed_iterator_t<R>
sort_heap( R&& r, Comp comp = {}, Proj proj = {} );
```

Sorts the elements in the specified range with respect to `comp` and `proj`, where the range originally represents a heap with respect to `comp` and `proj`. The sorted range no longer maintains the heap property.
1. The specified range is [first, last).
2. The specified range is `r`.
If the specified range is not a heap with respect to `comp` and `proj`, the behavior is undefined.

## Parameters


### Parameters

- `[3=to modify, sentinel=yes}})` - 
- `r` - the  of elements to modify
- `comp` - comparator to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

1. `last`
2. `ranges::end(r)`

## Complexity

At most  applications of `comp` and  applications of `proj`, where  is:
1. `ranges::distance(first, last)`
2. `ranges::distance(r)`

## Possible implementation

eq fun|1=
struct sort_heap_fn
{
template<std::random_access_iterator I, std::sentinel_for<I> S,
class Comp = ranges::less, class Proj = std::identity>
requires std::sortable<I, Comp, Proj>
constexpr I operator()(I first, S last, Comp comp = {}, Proj proj = {}) const
{
auto ret{ranges::next(first, last)};
for (auto last{ret}; first != last; --last)
ranges::pop_heap(first, last, comp, proj);
return ret;
}
template<ranges::random_access_range R,
class Comp = ranges::less, class Proj = std::identity>
requires std::sortable<ranges::iterator_t<R>, Comp, Proj>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, Comp comp = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(comp), std::move(proj));
}
};
inline constexpr sort_heap_fn sort_heap{};

## Example


### Example


**Output:**
```
original array:  3 1 4 1 5 9
after make_heap: 9 5 4 1 1 3
after sort_heap: 1 1 3 4 5 9
```


## See also


| cpp/algorithm/ranges/dsc is_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc is_heap_until | (see dedicated page) |
| cpp/algorithm/ranges/dsc make_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc pop_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc push_heap | (see dedicated page) |
| cpp/algorithm/dsc sort_heap | (see dedicated page) |

