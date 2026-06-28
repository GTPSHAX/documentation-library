---
title: std::ranges::sized_range
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/sized_range
---


```cpp
**Header:** `<`ranges`>`
dcl rev multi|num=1|since1=c++20|until1=c++26|dcl1=
template< class T >
concept sized_range = ranges::range<T> &&
requires(T& t) {
ranges::size(t);
};
|dcl2=
template< class T >
concept sized_range = ranges::approximately_sized_range<T> &&
requires(T& t) {
ranges::size(t);
};
dcl|num=2|since=c++20|1=
template< class >
constexpr bool disable_sized_range = false;
```

1. The `sized_range` concept specifies the requirements of a <sup>(until C++26)</sup> <sup>(since C++26)</sup> `approximately_sized_range` type that knows its size in constant time with the `size` function.
2. The `disable_sized_range` exists to allow use of range types that provide a `size` function (either as a member or as a non-member) but do not in fact model `sized_range`. Users may specialize `disable_sized_range` for cv-unqualified program-defined types. Such specializations shall be usable in s and have type `const bool`.

## Semantic requirements

1. Given an lvalue `t` of type `std::remove_reference_t<T>`, `T` models `sized_range` only if
* `ranges::size(t)`
:* has amortized constant-time complexity,
:* does not alter the value of `t` in a manner observable to equality-preserving expressions, and
:* is equal to `ranges::distance(ranges::begin(t), ranges::end(t))`, and
* if `ranges::iterator_t<T>` models , `ranges::size(t)` is well-defined regardless of the evaluation of `ranges::begin(t)` (in other words, a single-pass sized range may support a call to size only before the first call to begin, but a forward range must support size at all times).

## Notes

`disable_sized_range` cannot be used to opt-out a range whose iterator and sentinel satisfy ; `std::disable_sized_sentinel_for` must be used instead.
`disable_sized_range` cannot be specialized for array types or reference types.

## Example


### Example

```cpp
#include <forward_list>
#include <list>
#include <ranges>

static_assert
(
    std::ranges::sized_range<std::list<int>> and
    not std::ranges::sized_range<std::forward_list<int>>
);

int main() {}
```


## See also


| cpp/ranges/dsc random_access_range | (see dedicated page) |
| cpp/ranges/dsc contiguous_range | (see dedicated page) |

