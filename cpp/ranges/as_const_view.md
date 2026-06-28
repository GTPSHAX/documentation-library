---
title: std::ranges::views::as_const
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/as_const_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++23|1=
template< ranges::view V >
requires ranges::input_range<V>
class as_const_view
: public ranges::view_interface<as_const_view<V>>
dcl|num=2|since=c++23|1=
namespace views {
inline constexpr /* unspecified */ as_const = /* unspecified */;
}
dcl|since=c++23|1=
template< ranges::viewable_range R >
requires /* see below */
constexpr ranges::view auto as_const( R&& r );
```

1. A range adaptor that represents a view of underlying  that is also a . An `as_const_view` always has read-only elements (if not empty).
2. *RangeAdaptorObject*. Let `e` be a subexpression, let `T` be `decltype((e))`, and let `U` be `std::remove_cvref_t<T>`. Then the expression `views::as_const(e)` is expression-equivalent to:
* `views::all(e)`, if it is a well-formed expression and `views::all_t<T>` models ;
* otherwise, `std::span<const X, Extent>(e)` for some type `X` and some extent `Extent` if `U` denotes `std::span<X, Extent>`;
* otherwise, `ranges::ref_view(static_cast<const X&>(e.base()))` if `U` denotes `ranges::ref_view<X>` for some type `X` and `const X` models ;
* otherwise, `ranges::ref_view(static_cast<const U&>(e))` if `e` is an lvalue, `const U` models , and `U` does not model .
* otherwise, }.
`as_const_view` always models , and it models the , , , , , , and  when the underlying view `V` models respective concepts.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions

member|as_const_view|

```cpp
dcl|num=1|since=c++23|1=
as_const_view() requires std::default_initializable<V> = default;
dcl|num=2|since=c++23|
constexpr explicit as_const_view( V base );
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
constexpr auto begin() requires (!/*simple_view*/<V>);
dcl|num=2|since=c++23|
constexpr auto begin() const requires ranges::range<const V>;
```

Returns the constant iterator of the view. Equivalent to .
member|end|

```cpp
dcl|num=1|since=c++23|
constexpr auto end() requires (!/*simple_view*/<V>);
dcl|num=2|since=c++23|
constexpr auto end() const requires ranges::range<const V>;
```

Returns the constant sentinel of the view. Equivalent to .
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
as_const_view( R&& ) -> as_const_view<views::all_t<R>>;

## Helper templates

ddcl|since=c++23|1=
template< class T >
constexpr bool enable_borrowed_range<std::ranges::as_const_view<T>> =
ranges::enable_borrowed_range<T>;
This specialization of `ranges::enable_borrowed_range` makes `as_const_view` satisfy  when the underlying view satisfies it.

## Notes


## Example

assert(v1.back() == 5);
v1[0]++; // OK, can modify non-const element
auto v2 = x | std::views::drop(2) | std::views::as_const;
assert(v2.back() == 5);
// v2[0]++; // Compile-time error, cannot modify read-only element
}

## See also


| cpp/ranges/dsc as_rvalue_view | (see dedicated page) |
| cpp/ranges/dsc cbegin | (see dedicated page) |
| cpp/ranges/dsc cend | (see dedicated page) |
| cpp/utility/dsc as_const | (see dedicated page) |
| cpp/iterator/dsc basic_const_iterator | (see dedicated page) |

