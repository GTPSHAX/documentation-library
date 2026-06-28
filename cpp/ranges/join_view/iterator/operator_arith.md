---
title: std::ranges::join_view::iterator<Const>::operators
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view/iterator/operator_arith
---


```cpp
dcl|num=1|since=c++20|
constexpr /*iterator*/& operator++();
dcl|num=2|since=c++20|
constexpr void operator++( int );
dcl|num=3|since=c++20|
constexpr /*iterator*/ operator++( int )
requires /*ref-is-glvalue*/ && ranges::forward_range<Base> &&
ranges::forward_range<ranges::range_reference_t<Base>>;
dcl|num=4|since=c++20|
constexpr iterator& operator--()
requires /*ref-is-glvalue*/ && ranges::bidirectional_range<Base> &&
ranges::bidirectional_range<ranges::range_reference_t<Base>> &&
ranges::common_range<ranges::range_reference_t<Base>>;
dcl|num=5|since=c++20|
constexpr /*iterator*/ operator--( int )
requires /*ref-is-glvalue*/ && ranges::bidirectional_range<Base> &&
ranges::bidirectional_range<ranges::range_reference_t<Base>> &&
ranges::common_range<ranges::range_reference_t<Base>>;
```

Increments or decrements the underlying iterator.
Let  and  be the underlying iterators, and  be the pointer to parent `ranges::join_view`, the constant `/*ref-is-glvalue*/` be `std::is_reference_v<ranges::range_reference_t<Base>>`.
1. Let `/*inner-range*/` be:
* `*outer_`, if `1=/*ref-is-glvalue*/ == true`;
* `*parent_->inner_` otherwise.
Equivalent to:

```cpp
auto&& inner_rng = /*inner-range*/;
if (++inner_ == ranges::end(inner_rng))
{
    ++outer_;
    satisfy();
}
return *this;
```

2. Equivalent to: `1=++*this`.
3. Equivalent to:

```cpp
auto tmp = *this;
++*this;
return tmp;
```

4. Equivalent to:

```cpp
if (outer_ == ranges::end(parent_->base_))
    inner_ = ranges::end(*--outer_);
while (inner_ == ranges::begin(*outer_))
    inner_ = ranges::end(*--outer_);
--inner_;
return *this;
```


```cpp
auto tmp = *this;
--*this;
return tmp;
```


## Parameters

(none)

## Return value

@1,4@ `*this`
2. (none)
@3,5@ a copy of `*this` that was made before the change.
