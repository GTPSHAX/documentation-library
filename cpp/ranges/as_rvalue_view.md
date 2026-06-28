---
title: std::ranges::views::as_rvalue
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/as_rvalue_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++23|1=
template< ranges::view V >
requires ranges::input_range<V>
class as_rvalue_view
: public ranges::view_interface<as_rvalue_view<V>>
dcl|num=2|since=c++23|1=
namespace views {
inline constexpr /* unspecified */ as_rvalue = /* unspecified */;
}
dcl|since=c++23|1=
template< ranges::viewable_range R >
requires /* see below */
constexpr ranges::view auto as_rvalue( R&& r );
```

1. A range adaptor that represents a view of underlying  whose elements are rvalues.
2. *RangeAdaptorObject*. Let `e` be a subexpression and let `T` be `decltype((e))`. Then the expression `views::as_rvalue(e)` is expression-equivalent to:
* `views::all(e)`, if it is a well-formed expression, `T` models , and `std::same_as<ranges::range_rvalue_reference_t<T>, ranges::range_reference_t<T>>` is `true`;
* } otherwise.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions

member|as_rvalue_view|

```cpp
dcl|num=1|since=c++23|1=
as_rvalue_view() requires std::default_initializable<V> = default;
dcl|num=2|since=c++23|
constexpr explicit as_rvalue_view( V base );
```

1. Value-initializes  via its default member initializer (`1== V()`).
2. Initializes  with `std::move(base)`.

## Parameters


### Parameters

- `base` - a view
member|base|

```cpp
dcl|num=1|since=c++23|
constexpr V base() const& requires std::copy_constructible<V>;
dcl|num=2|since=c++23|
constexpr V base() &&;
```

Returns the underlying view.
1. Copy-constructs the result from the underlying view. Equivalent to .
2. Move-constructs the result from the underlying view. Equivalent to .
member|begin|

```cpp
dcl|num=1|since=c++23|
constexpr auto begin() requires (!/*simple-view*/<V>);
dcl|num=2|since=c++23|
constexpr auto begin() const requires ranges::range<const V>;
```

Returns .
member|end|

```cpp
dcl|num=1|since=c++23|
constexpr auto end() requires (!/*simple-view*/<V>);
dcl|num=2|since=c++23|
constexpr auto end() const requires ranges::range<const V>;
```

Returns  if  `V` or  `const V` models .
Returns  otherwise.
member|size|

```cpp
dcl|num=1|since=c++23|
constexpr auto size() requires ranges::sized_range<V>;
dcl|num=2|since=c++23|
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

ddcl|since=c++23|
template< class R >
as_rvalue_view( R&& ) -> as_rvalue_view<views::all_t<R>>;

## Helper templates

ddcl|since=c++23|1=
template< class T >
constexpr bool enable_borrowed_range<std::ranges::as_rvalue_view<T>> =
ranges::enable_borrowed_range<T>;
This specialization of `ranges::enable_borrowed_range` makes `as_rvalue_view` satisfy  when the underlying view satisfies it.

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <ranges>
#include <string>
#include <vector>

int main()
{
    std::vector<std::string> words =
        {"Quick", "red", "\N{FOX FACE}", "jumped", "over", "a", "pterodactyl"};
    std::vector<std::string> new_words;

    std::ranges::copy(
        words {{!
```

std::back_inserter(new_words)); // move string from words into new_words
auto quoted = std::views::transform([](auto&& s) { return "“" + s + "”"; });
std::cout << "Old words: ";
for (auto&& word : words | std::views::as_rvalue | quoted)
std::cout << word << ' ';
std::cout << "\nNew words: ";
for (auto&& word : new_words | std::views::as_rvalue | quoted)
std::cout << word << ' ';
}
|p=true
|output=
Old words: “” “” “” “” “” “” “”
New words: “Quick” “red” “🦊” “jumped” “over” “a” “pterodactyl”

## Defect reports


## See also


| cpp/iterator/ranges/dsc iter_move | (see dedicated page) |
| cpp/iterator/dsc move_iterator | (see dedicated page) |
| cpp/iterator/dsc move_sentinel | (see dedicated page) |
| cpp/ranges/dsc as_const_view | (see dedicated page) |

