---
title: std::ranges::unique
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/unique
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::permutable I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_equivalence_relation<std::projected<I, Proj>>
C = ranges::equal_to >
constexpr ranges::subrange<I>
unique( I first, S last, C comp = {}, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< ranges::forward_range R, class Proj = std::identity,
std::indirect_equivalence_relation<std::projected<ranges::iterator_t<R>, Proj>>
C = ranges::equal_to >
requires std::permutable<ranges::iterator_t<R>>
constexpr ranges::borrowed_subrange_t<R>
unique( R&& r, C comp = {}, Proj proj = {} );
```

1. Eliminates all except the first element from every consecutive group of equivalent elements from the range [first, last) and returns a subrange [ret, last), where `ret` is a past-the-end iterator for the new end of the range.
@@ Two consecutive elements `*(i - 1)` and `*i` are considered equivalent if `1=std::invoke(comp, std::invoke(proj, *(i - 1)), std::invoke(proj, *i)) == true`, where `i` is an iterator in the range [first + 1, last).
2. Same as , but uses `r` as the range, as if using `ranges::begin(r)` as `first`, and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to process, sentinel=yes}})` - 
- `r` - the range of elements to process
- `comp` - the binary predicate to compare the projected elements
- `proj` - the projection to apply to the elements

## Return value

Returns }, where `ret` is a past-the-end iterator for the new end of the range.

## Complexity

For nonempty ranges, exactly `ranges::distance(first, last) - 1` applications of the corresponding predicate `comp` and no more that twice as many applications of any projection `proj`.

## Notes

Removing is done by shifting (by means of move assignment) the elements in the range in such a way that the elements that are not to be removed appear in the beginning of the range. Relative order of the elements that remain is preserved and the ''physical'' size of the container is unchanged. Iterators in [ret, last) (if any) are still dereferenceable, but the elements themselves have unspecified values (as per *MoveAssignable* post-condition).
A call to `ranges::unique` is sometimes followed by a call to a container’s `erase` member function, which erases the unspecified values and reduces the ''physical'' size of the container to match its new ''logical'' size. These two invocations together model the ''Erase–remove'' idiom.

## Possible implementation

eq fun|1=
struct unique_fn
{
template<std::permutable I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_equivalence_relation<std::projected<I, Proj>>
C = ranges::equal_to>
constexpr ranges::subrange<I>
operator()(I first, S last, C comp = {}, Proj proj = {}) const
{
first = ranges::adjacent_find(first, last, comp, proj);
if (first == last)
return {first, first};
auto i {first};
++first;
while (++first != last)
if (!std::invoke(comp, std::invoke(proj, *i), std::invoke(proj, *first)))
*++i = ranges::iter_move(first);
return {++i, first};
}
template<ranges::forward_range R, class Proj = std::identity,
std::indirect_equivalence_relation<std::projected<ranges::iterator_t<R>, Proj>>
C = ranges::equal_to>
requires std::permutable<ranges::iterator_t<R>>
constexpr ranges::borrowed_subrange_t<R>
operator()(R&& r, C comp = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r),
std::move(comp), std::move(proj));
}
};
inline constexpr unique_fn unique {};

## Example


### Example


**Output:**
```
1) 1 2 1 1 3 3 3 4 5 4
2) 1 2 1 3 4 5 4
3) 1 1 2 3 4 4 5
4) 1 2 3 4 5
5) (1,1) (-1,2) (-2,3) (2,4) (-3,5)
6) (1,1) (-2,3) (-3,5)
```


## See also


| cpp/algorithm/ranges/dsc unique_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc adjacent_find | (see dedicated page) |
| cpp/algorithm/ranges/dsc remove | (see dedicated page) |
| cpp/algorithm/dsc unique | (see dedicated page) |
| cpp/container/dsc unique|list | (see dedicated page) |
| cpp/container/dsc unique|forward_list | (see dedicated page) |

