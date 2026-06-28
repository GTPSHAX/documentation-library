---
title: std::ranges::views::reverse
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/reverse_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< ranges::view V >
requires ranges::bidirectional_range<V>
class reverse_view
: public ranges::view_interface<reverse_view<V>>
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr /* unspecified */ reverse = /* unspecified */;
}
dcl|since=c++20|1=
template< ranges::viewable_range R >
requires /* see below */
constexpr ranges::view auto reverse( R&& r );
```

1. A range adaptor that represents a view of underlying  with reversed order.
2. *RangeAdaptorObject*. The expression `views::reverse(e)` is expression-equivalent to one of the following expressions, except that `e` is evaluated only once:
* `e.base()`, if the type of `e` is a (possibly cv-qualified) specialization of `reverse_view`;
* otherwise, if the type of `e` is (possibly cv-qualified) `ranges::subrange<std::reverse_iterator<I>, std::reverse_iterator<I>, K>` for some iterator type `I` and value `K` of type `ranges::subrange_kind`:
:* `ranges::subrange<I, I, K>(e.end().base(), e.begin().base(), e.size())`, if `K` is `ranges::subrange_kind::sized`;
:* otherwise `ranges::subrange<I, I, K>(e.end().base(), e.begin().base())`;
* otherwise }.
In other words, `views::reverse` unwraps reversed views if possible.
A `reverse_view` always models  and , and it models , , or  if the underlying view type `V` models the corresponding concept.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |
| dsc expos mem obj|cached_end_|id=cached_end|private=yes | |
| |maybe=(present only if `V` does not satisfy ) | |
| |spec=`<ranges::iterator_t<V>>` | |
| |an object that caches the result of calls to | |


## Member functions

member|reverse_view|

```cpp
dcl|num=1|since=c++20|1=
reverse_view() requires std::default_initializable<V> = default;
dcl|num=2|since=c++20|
constexpr reverse_view( V r );
```

1. Value-initializes  via its default member initializer (`1== V()`).
2. Initializes  with `std::move(r)`.

## Parameters


### Parameters

- `r` - range to reverse
member|base|

```cpp
dcl|num=1|since=c++20|
constexpr V base() const& requires std::copy_constructible<V>;
dcl|num=2|since=c++20|
constexpr V base() &&;
```

Returns the underlying view.
1. Copy-constructs the result from the underlying view. Equivalent to .
2. Move-constructs the result from the underlying view. Equivalent to .
member|begin|

```cpp
dcl|num=1|since=c++20|
constexpr std::reverse_iterator<ranges::iterator_t<V>> begin();
dcl|num=2|since=c++20|
constexpr std::reverse_iterator<ranges::iterator_t<V>> begin()
requires ranges::common_range<V>;
dcl|num=3|since=c++20|
constexpr auto begin() const requires ranges::common_range<const V>;
```

1. Returns .
@@ In order to provide the amortized constant time complexity required by the  concept, this function caches the result within the cache object for use on subsequent calls.
@2,3@ Equivalent to .
member|end|

```cpp
dcl|num=1|since=c++20|
constexpr std::reverse_iterator<ranges::iterator_t<V>> end();
dcl|num=2|since=c++20|
constexpr auto end() const requires ranges::common_range<const V>;
```

Equivalent to .
member|size|

```cpp
dcl|num=1|since=c++20|
constexpr auto size() requires ranges::sized_range<V>;
dcl|num=2|since=c++20|
constexpr auto size() const requires ranges::sized_range<const V>;
```

Returns the size of the view if the view is bounded. Equivalent to .
member|reserve_hint|

```cpp
dcl|num=1|since=c++26|
constexpr auto reserve_hint()
requires ranges::approximately_sized_range<V>;
dcl|num=2|since=c++26|
constexpr auto reserve_hint() const
requires ranges::approximately_sized_range<const V>;
```

Returns .

## Deduction guides

ddcl|since=c++20|
template< class R >
reverse_view( R&& ) -> reverse_view<views::all_t<R>>;

## Helper templates

ddcl|since=c++20|1=
template< class T >
constexpr bool enable_borrowed_range<std::ranges::reverse_view<T>> =
ranges::enable_borrowed_range<T>;
This specialization of `cpp/ranges/borrowed_range|std::ranges::enable_borrowed_range` makes `reverse_view` satisfy  when the underlying view satisfies it.

## Notes


## Example


### Example

```cpp
#include <iostream>
#include <ranges>

int main()
{
    static constexpr auto il = {3, 1, 4, 1, 5, 9};

    std::ranges::reverse_view rv{il};
    for (int i : rv)
        std::cout << i << ' ';
    std::cout << '\n';

    for (int i : il {{!
```

std::cout << i << ' ';
std::cout << '\n';
// operator[] is inherited from std::view_interface
for (auto i{0U}; i != rv.size(); ++i)
std::cout << rv[i] << ' ';
std::cout << '\n';
}
|output=
9 5 1 4 1 3
9 5 1 4 1 3
9 5 1 4 1 3

## Defect reports


## See also


| cpp/iterator/dsc reverse_iterator | (see dedicated page) |
| cpp/algorithm/ranges/dsc reverse | (see dedicated page) |
| cpp/algorithm/ranges/dsc reverse_copy | (see dedicated page) |

