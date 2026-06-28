---
title: std::ranges::view_interface::empty
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/view_interface/empty
---


```cpp
dcl|num=1|since=c++20|1=
constexpr bool empty()
requires ranges::sized_range<D>  ranges::forward_range<D>;
dcl|num=2|since=c++20|1=
constexpr bool empty() const
requires ranges::sized_range<const D>  ranges::forward_range<const D>;
```

The default implementation of `empty()` member function checks whether the object of the derived type's size is `0` (if valid), or whether the beginning iterator and the sentinel compare equal.
1. Let `derived` be a reference bound to `static_cast<D&>(*this)`. Equivalent to `1=return ranges::size(derived) == 0;` if `D` satisfies . Otherwise, equivalent to `1=return ranges::begin(derived) == ranges::end(derived);`.
2. Same as , except that `derived` is `static_cast<const D&>(*this)`.

## Return value

`true` if the size of the object of the derived type is `0` (if `D` satisfies `std::ranges::sized_range`), or its beginning iterator and the sentinel compare equal, `false` otherwise.

## Notes

Following derived types may use the default implementation of `empty`:
* `cpp/ranges/common_view|std::ranges::common_view`
* `cpp/ranges/drop_view|std::ranges::drop_view`
* `cpp/ranges/drop_while_view|std::ranges::drop_while_view`
* `cpp/ranges/elements_view|std::ranges::elements_view`
* `cpp/ranges/filter_view|std::ranges::filter_view`
* `cpp/ranges/join_view|std::ranges::join_view`
* `cpp/ranges/lazy_split_view|std::ranges::lazy_split_view`
* `cpp/ranges/reverse_view|std::ranges::reverse_view`
* `cpp/ranges/single_view|std::ranges::single_view`
* `cpp/ranges/split_view|std::ranges::split_view`
* `cpp/ranges/take_view|std::ranges::take_view`
* `cpp/ranges/take_while_view|std::ranges::take_while_view`
* `cpp/ranges/transform_view|std::ranges::transform_view`
rrev|since=c++23|
* `cpp/ranges/adjacent_transform_view|std::ranges::adjacent_transform_view`
* `cpp/ranges/adjacent_view|std::ranges::adjacent_view`
* `cpp/ranges/as_const_view|std::ranges::as_const_view`
* `cpp/ranges/as_rvalue_view|std::ranges::as_rvalue_view`
* `cpp/ranges/cartesian_product_view|std::ranges::cartesian_product_view`
* `cpp/ranges/chunk_view|std::ranges::chunk_view`
* `cpp/ranges/chunk_by_view|std::ranges::chunk_by_view`
* `cpp/ranges/join_with_view|std::ranges::join_with_view`
* `cpp/ranges/repeat_view|std::ranges::repeat_view`
* `cpp/ranges/slide_view|std::ranges::slide_view`
* `cpp/ranges/stride_view|std::ranges::stride_view`
* `cpp/ranges/zip_view|std::ranges::zip_view`
* `cpp/ranges/zip_transform_view|std::ranges::zip_transform_view`
rrev|since=c++26|
* `cpp/ranges/as_input_view|std::ranges::as_input_view`
* `cpp/ranges/cache_latest_view|std::ranges::cache_latest_view`
* `cpp/ranges/concat_view|std::ranges::concat_view`
Although `ranges::basic_istream_view|std::ranges::basic_istream_view` inherits from `ranges::view_interface|std::ranges::view_interface` and does not declare the `empty()` member function, it cannot use the default implementation, because it never satisfies neither `std::ranges::sized_range` nor `std::ranges::forward_range`.

## Example

static_assert(!(a | std::views::take(5)).empty());
static_assert((a | std::views::drop(5)).empty());
static_assert(!(a | std::views::drop(3)).empty());
static_assert(std::views::iota(0,0).empty());
static_assert(!std::views::iota(0).empty());
}

## Defect reports


## See also


| cpp/iterator/dsc empty | (see dedicated page) |
| cpp/ranges/dsc empty | (see dedicated page) |

