---
title: std::ranges::filter_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/filter_view/iterator
---

ddcla|since=c++20|expos=yes|
class /*iterator*/;
The return type of `cpp/ranges/filter_view|filter_view::begin`.
This is a  if `V` models , a  if `V` models , and  otherwise.
Modification of the element denoted by this iterator is permitted, but results in undefined behavior if the resulting value does not satisfy the filter's predicate.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| dsc|`iterator_concept`| | |
| * `std::bidirectional_iterator_tag`, if `V` models , | |
| * `std::forward_iterator_tag`, if `V` models , | |
| * `std::input_iterator_tag` otherwise. | |
| dsc|`iterator_category`<br>| | |
| Let `C` be the type `std::iterator_traits<ranges::iterator_t<V>>::iterator_category`. | |
| * `std::bidirectional_iterator_tag`, if `C` models `std::derived_from<std::bidirectional_iterator_tag>`, | |
| * `std::forward_iterator_tag`, if `C` models `std::derived_from<std::forward_iterator_tag>`, | |
| * `C` otherwise. | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions

member|''iterator''|2=

```cpp
dcl|since=c++20|num=1|1=
/*iterator*/()
requires std::default_initializable<ranges::iterator_t<V>> = default;
dcl|since=c++20|num=2|1=
constexpr /*iterator*/( filter_view& parent,
ranges::iterator_t<V> current );
```

1. Initializes  and  with their default member initializers, which are `1== ranges::iterator_t<V>()` and `1== nullptr` respectively.
2. Initializes  with `std::move(current)` and  with `std::addressof(parent)`.
member|base|2=

```cpp
dcl|since=c++20|num=1|1=
constexpr const ranges::iterator_t<V>& base() const & noexcept;
dcl|since=c++20|num=2|1=
constexpr ranges::iterator_t<V> base() &&;
```

1. Equivalent to `return current_;`.
2. Equivalent to `return std::move(current_);`.
member|operator*,->|2=

```cpp
dcl|since=c++20|num=1|1=
constexpr ranges::range_reference_t<V> operator*() const;
dcl|since=c++20|num=2|1=
constexpr ranges::iterator_t<V> operator->() const
requires /*has-arrow*/<ranges::iterator_t<V>> &&
std::copyable<ranges::iterator_t<V>>;
```

1. Equivalent to `return *current_;`.
2. Equivalent to `return current_;`.<br>
For a type `I`, `/*has-arrow*/<I>` is modeled or satisfied, if and only if `I` models or satisfies  respectively, and either `I` is a pointer type or `requires(I i){ i.operator->();`} is `true`.
member|operator++|2=

```cpp
dcl|since=c++20|num=1|1=
constexpr /*iterator*/& operator++();
dcl|since=c++20|num=2|1=
constexpr void operator++( int );
dcl|since=c++20|num=3|1=
constexpr /*iterator*/ operator++( int )
requires ranges::forward_range<V>;
```

1. Equivalent to<br>c multi
|current_  ranges::find_if(std::move(++current_), ranges::end(parent_->base_),
|                           std::ref(*parent_->pred_));
|return *this;
.
2. Equivalent to `++*this;`.
3. Equivalent to `1=auto tmp = *this; ++*this; return tmp;`.
member|operator--|2=

```cpp
dcl|since=c++20|num=1|1=
constexpr /*iterator*/& operator--()
requires ranges::bidirectional_range<V>;
dcl|since=c++20|num=2|1=
constexpr /*iterator*/ operator--( int )
requires ranges::bidirectional_range<V>;
```

1. Equivalent to<br>c multi
|do
|    --current_;
|while (!std::invoke(*parent_->pred_, *current_));
|return *this;
.
2. Equivalent to `1=auto tmp = *this; --*this; return tmp;`.

## Non-member functions

member|1= operator==|2=
ddcl|since=c++20|1=
friend constexpr bool operator==( const /*iterator*/& x, const /*iterator*/& y )
requires std::equality_comparable<ranges::iterator_t<V>>;
Equivalent to `1=return x.current_ == y.current_;`.
member|1= iter_move|2=
ddcl|since=c++20|1=
friend constexpr ranges::range_rvalue_reference_t<V>
iter_move( const /*iterator*/& i )
noexcept(noexcept(ranges::iter_move(i.current_)));
Equivalent to `1=return ranges::iter_move(i.current_);`.
member|1= iter_swap|2=
ddcl|since=c++20|1=
friend constexpr void iter_swap( const /*iterator*/& x, const /*iterator*/& y )
noexcept(noexcept(ranges::iter_swap(x.current_, y.current_)))
requires std::indirectly_swappable<ranges::iterator_t<V>>;
Equivalent to `1=ranges::iter_swap(x.current_, y.current_)`.

## Defect reports

