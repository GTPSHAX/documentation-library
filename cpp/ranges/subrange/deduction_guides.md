---
title: deduction guides for std::ranges::subrange
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/subrange/deduction_guides
---


# deduction guides for tt|std::ranges::subrange


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|
template< std::input_or_output_iterator I, std::sentinel_for<I> S >
subrange(I, S) -> subrange<I, S>;
dcl|num=2|since=c++20|
template< std::input_or_output_iterator I, std::sentinel_for<I> S >
subrange(I, S, /*make-unsigned-like-t*/<std::iter_difference_t<I>>) ->
subrange<I, S, ranges::subrange_kind::sized>;
dcl|num=3|since=c++20|
template< ranges::borrowed_range<R> >
subrange(R&&) ->
subrange<ranges::iterator_t<R>, ranges::sentinel_t<R>,
(ranges::sized_range<R>
std::sized_sentinel_for<ranges::sentinel_t<R>,
ranges::iterator_t<R>>) ?
ranges::subrange_kind::sized : ranges::subrange_kind::unsized>;
dcl|num=4|since=c++20|
template< ranges::borrowed_range<R> >
subrange(R&&, /*make-unsigned-like-t*/<ranges::range_difference_t<R>>) ->
subrange<ranges::iterator_t<R>, ranges::sentinel_t<R>,
ranges::subrange_kind::sized>;
```

These deduction guides are provided for `std::ranges::subrange`.
1. Deduces the template arguments from the type of iterator and sentinel. The `subrange` is sized if `std::sized_sentinel_for<S, I>` is satisfied, as determined by the default template argument.
2. Deduces the template arguments from the type of iterator and sentinel, while the size of range is specified. The `subrange` is always sized.
3. Deduces the template arguments from the type of range. The `subrange` is sized if the size can be obtained from the range or its iterator and sentinel.
4. Deduces the template arguments from the type of range, while the size of range is specified. The `subrange` is always sized.
For the definition of `/* make-unsigned-like-t */`, see .

## Notes

While constructing the `subrange` object,
* for , the behavior is undefined if the iterator-sentinel pair does not denote a valid range,
* for , the behavior is undefined if the given size is not equal to the size of the range.

## Example

