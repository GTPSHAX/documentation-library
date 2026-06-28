---
title: std::ranges::subrange::subrange
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/subrange/subrange
---


```cpp
dcl|num=1|since=c++20|1=
subrange() requires std::default_initializable<I> = default;
dcl|num=2|since=c++20|
constexpr subrange( /*convertible-to-non-slicing*/<I> auto i, S s )
requires (!/*StoreSize*/);
dcl|num=3|since=c++20|1=
constexpr subrange( /*convertible-to-non-slicing*/<I> auto i, S s,
/*make-unsigned-like-t*/<std::iter_difference_t<I>> n )
requires (K == ranges::subrange_kind::sized);
dcla|num=4|since=c++20|
template< /*different-from*/<subrange> R >
requires ranges::borrowed_range<R> &&
/*convertible-to-non-slicing*/<ranges::iterator_t<R>, I> &&
std::convertible_to<ranges::sentinel_t<R>, S>
constexpr subrange( R&& r )
requires (!/*StoreSize*/  ranges::sized_range<R>);
dcl|num=5|since=c++20|1=
template< ranges::borrowed_range R>
requires /*convertible-to-non-slicing*/<ranges::iterator_t<R>, I> &&
std::convertible_to<ranges::sentinel_t<R>, S>
constexpr subrange( R&& r,
/*make-unsigned-like-t*/<std::iter_difference_t<I>> n )
requires (K == ranges::subrange_kind::sized)
: subrange{ranges::begin(r), ranges::end(r), n} {}
```

Constructs a `subrange`.
For the definitions of `/*make-unsigned-like-t*/` and `/*different-from*/`, see  and  respectively.


| rowspan=2 | Overload |
| colspan=3 | rlps | /#Data members |
| - |
| style="font-weight: normal;" | tti | begin_ |
| style="font-weight: normal;" | tti | end_ |
| style="font-weight: normal;" | tti | size_<br>small | (only if box | rlpsi | /#StoreSize is c | true) |
| - |
| v | 1 |
| [[cpp/language/value initialization | value-initialized]] |
| [[cpp/language/value initialization | value-initialized]] |
| initialized with c | 0 |
| - |
| - |
| v | 2 |
| rowspan=2 | initialized with c | std::move(i) |
| rowspan=2 | initialized with c | s |
|  |
| - |
| v | 3 |
| initialized with c | n |
| - |
| v | 4 |
| rowspan=2 | initialized with c | std::move(ranges::begin(r)) |
| rowspan=2 | initialized with c | ranges::end(r) |
| initialized with <span style="text-align: left">box | c/core | static_cast<decltype(rlpsi | /#size_c/core | )><br>nbspt | 4c/core | (ranges::size(r))</span> |
| - |
| v | 5 |
| initialized with c | n |

2. If [i, s) is not a valid range, the behavior is undefined.
3. If any of the following conditions is satisfied, the behavior is undefined:
* [i, s) is not a valid range.
*  is `false`.

## Parameters


### Parameters

- `i` - iterator that denotes the beginning of the range
- `s` - sentinel that denotes the end of the range
- `r` - range
- `n` - size hint, must be equal to the size of the range

## Example

