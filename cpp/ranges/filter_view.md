---
title: std::ranges::views::filter
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/filter_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< ranges::input_range V,
std::indirect_unary_predicate<ranges::iterator_t<V>> Pred >
requires ranges::view<V> && std::is_object_v<Pred>
class filter_view
: public ranges::view_interface<filter_view<V, Pred>>
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr /* unspecified */ filter = /* unspecified */;
}
dcl|since=c++20|1=
template< ranges::viewable_range R, class Pred >
requires /* see below */
constexpr ranges::view auto filter( R&& r, Pred&& pred );
dcl|since=c++20|1=
template< class Pred >
constexpr /* range adaptor closure */ filter( Pred&& pred );
```

1. A range adaptor that represents a  of an underlying sequence without the elements that fail to satisfy a predicate.
2. *RangeAdaptorObject*. The expression `views::filter(e, p)` is expression-equivalent to `filter_view(e, p)` for any suitable subexpressions `e` and `p`.
`filter_view` models the concepts , , , and  when the underlying  `V` models respective concepts.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions

member|filter_view|2=

```cpp
dcl|since=c++20|num=1|1=
filter_view() requires std::default_initializable<V> &&
std::default_initializable<Pred> = default;
dcl|since=c++20|num=2|
constexpr explicit filter_view( V base, Pred pred );
```

1. Value-initializes  via its default member initializer (`1== V()`) and default-initializes  (which value-initializes the contained `Pred`).
2. Initializes  with `std::move(base)` and initializes  with `std::move(pred)`.

## Parameters


### Parameters

- `base` - range to filter
- `pred` - predicate to filter out elements
member|base|2=

```cpp
dcl|since=c++20|num=1|
constexpr V base() const& requires std::copy_constructible<V>;
dcl|since=c++20|num=2|
constexpr V base() &&;
```

1. Equivalent to `return base_;`.
2. Equivalent to `return std::move(base_);`.
member|pred|2=
ddcl|since=c++20|1=
constexpr const Pred& pred() const;
Returns a reference to the contained `Pred` object. The behavior is undefined if  does not contain a value.
member|begin|2=
ddcl|notes=|
constexpr /*iterator*/ begin();
In order to provide the amortized constant time complexity required by the  concept, this function caches the result within the `filter_view` object for use on subsequent calls. Equivalent to

```cpp
if constexpr (!ranges::forward_range<V>)
    return /*iterator*/{*this, ranges::find_if(base_, std::ref(*pred_))};
else
{
    if (!begin_.has_value())
        begin_ = ranges::find_if(base_, std::ref(*pred_)); // caching
    return /*iterator*/{*this, begin_.value())};
}
```

The behavior is undefined if  does not contain a value.
member|end|2=
ddcl|since=c++20|1=
constexpr auto end();
Returns an iterator to the end. Equivalent to

```cpp
if constexpr (ranges::common_range<V>)
    return /*iterator*/{*this, ranges::end(base_)};
else
    return /*sentinel*/{*this};
```


## Deduction guides

ddcl|since=c++20|1=
template< class R, class Pred >
filter_view( R&&, Pred ) -> filter_view<views::all_t<R>, Pred>;

## Nested classes


## Example


### Example

```cpp
#include <iostream>
#include <ranges>

int main()
{
    auto even = [](int i) { return 0 == i % 2; };
    auto square = [](int i) { return i * i; };

    for (int i : std::views::iota(0, 6)
               {{!
```

| std::views::transform(square))
std::cout << i << ' ';
std::cout << '\n';
}
|output=
0 4 16

## Defect reports


## See also


| cpp/ranges/dsc take_while_view | (see dedicated page) |

