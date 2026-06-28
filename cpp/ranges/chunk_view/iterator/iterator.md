---
title: std::ranges::chunk_view::iterator<Const>::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/iterator/iterator
---


```cpp
dcl|num=1|since=c++23|1=
/*iterator*/() = default;
dcl|num=2|since=c++23|1=
constexpr /*iterator*/( /*iterator*/<!Const> i )
requires
Const and
std::convertible_to<ranges::iterator_t<V>, ranges::iterator_t<Base>> and
std::convertible_to<ranges::sentinel_t<V>, ranges::sentinel_t<Base>>;
|1=
private:
constexpr /*iterator*/( Parent* parent,
ranges::iterator_t<Base> current,
ranges::range_difference_t<Base> missing = 0 );
```

Construct an iterator.
1. Default constructor. Value-initializes the underlying `data members`:
*  with `ranges::iterator_t<Base>()`,
*  with `ranges::sentinel_t<Base>()`,
*  with `0`,
*  with `0`.
2. Conversion from `/*iterator*/<false>` to `/*iterator*/<true>`. Initializes the underlying `data members`:
*  with `std::move(i.current_)`,
*  with `std::move(i.end_)`,
*  with `i.n_`,
*  with `i.missing_`.
3. A private constructor which is used by `ranges::chunk_view::begin` and `ranges::chunk_view::end`. This constructor is not accessible to users. Initializes the underlying `data members`:
*  with `current`,
*  with `ranges::end(parent->base_)`,
*  with `parent->n_`,
*  with `missing`.

## Parameters


### Parameters

- `i` - an `/*iterator*/<false>`
- `parent` - a pointer to owning `chunk_view`
- `current` - an iterator to the begin of current chunk
- `missing` - a difference between expected () and actual size of current chunk

## Example

