---
title: std::ranges::partition_copy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/partition_copy
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|num=1|1=
template< std::input_iterator I, std::sentinel_for<I> S,
std::weakly_incrementable O1, std::weakly_incrementable O2,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
requires std::indirectly_copyable<I, O1> &&
std::indirectly_copyable<I, O2>
constexpr partition_copy_result<I, O1, O2>
partition_copy( I first, S last, O1 out_true, O2 out_false,
Pred pred, Proj proj = {} );
dcl|since=c++20|num=2|1=
template< ranges::input_range R,
std::weakly_incrementable O1, std::weakly_incrementable O2,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<iterator_t<R>, Proj>> Pred >
requires std::indirectly_copyable<ranges::iterator_t<R>, O1> &&
std::indirectly_copyable<ranges::iterator_t<R>, O2>
constexpr partition_copy_result<ranges::borrowed_iterator_t<R>, O1, O2>
partition_copy( R&& r, O1 out_true, O2 out_false,
Pred pred, Proj proj = {} );
dcl|num=3|since=c++20|1=
template< class I, class O1, class O2 >
using partition_copy_result = ranges::in_out_out_result<I, O1, O2>;
```

1. Copies the elements from the input range [first, last) to two different output ranges depending on the value returned by the predicate `pred`. The elements that satisfy the predicate `pred` after projection by `proj` are copied to the range beginning at `out_true`. The rest of the elements are copied to the range beginning at `out_false`. The behavior is undefined if the input range overlaps either of the output ranges.
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first`, and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to copy from, range=source)` - 
- `r` - the source range of elements to copy from
- `out_true` - the beginning of the output range for the elements that satisfy `pred`
- `out_false` - the beginning of the output range for the elements that do not satisfy `pred`
- `pred` - predicate to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

}, where `o1` and `o2` are the ends of the output ranges respectively, after the copying is complete.

## Complexity

Exactly `ranges::distance(first, last)` applications of the corresponding predicate `comp` and any projection `proj`.

## Possible implementation

eq fun|1=
struct partition_copy_fn
{
template<std::input_iterator I, std::sentinel_for<I> S,
std::weakly_incrementable O1, std::weakly_incrementable O2,
class Proj = std::identity, std::indirect_unary_predicate<
std::projected<I, Proj>> Pred>
requires std::indirectly_copyable<I, O1> && std::indirectly_copyable<I, O2>
constexpr ranges::partition_copy_result<I, O1, O2>
operator()(I first, S last, O1 out_true, O2 out_false,
Pred pred, Proj proj = {}) const
{
for (; first != last; ++first)
if (!!std::invoke(pred, std::invoke(proj, *first)))
*out_true = *first, ++out_true;
else
*out_false = *first, ++out_false;
return {std::move(first), std::move(out_true), std::move(out_false)};
}
template<ranges::input_range R,
std::weakly_incrementable O1, std::weakly_incrementable O2,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<iterator_t<R>, Proj>> Pred>
requires std::indirectly_copyable<ranges::iterator_t<R>, O1> &&
std::indirectly_copyable<ranges::iterator_t<R>, O2>
constexpr ranges::partition_copy_result<ranges::borrowed_iterator_t<R>, O1, O2>
operator()(R&& r, O1 out_true, O2 out_false, Pred pred, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(out_true),
std::move(out_false), std::move(pred), std::move(proj));
}
};
inline constexpr partition_copy_fn partition_copy {};

## Example


### Example


**Output:**
```
in = N 3 U M 1 B 4 E 1 5 R 9
o1 = N U M B E R
o2 = 3 1 4 1 5 9
```


## See also


| cpp/algorithm/ranges/dsc partition | (see dedicated page) |
| cpp/algorithm/ranges/dsc stable_partition | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc remove_copy | (see dedicated page) |
| cpp/algorithm/dsc partition_copy | (see dedicated page) |

