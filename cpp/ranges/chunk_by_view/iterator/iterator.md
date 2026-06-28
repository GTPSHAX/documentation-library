---
title: std::ranges::chunk_by_view::iterator::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_by_view/iterator/iterator
---


```cpp
dcl|num=1|since=c++23|1=
/*iterator*/() = default;
|1=
private:
constexpr /*iterator*/( chunk_by_view& parent,
ranges::iterator_t<V> current,
ranges::iterator_t<V> next );
```

Construct an iterator.
1. Default constructor. Value-initializes the underlying data-members as follows:
*  with `nullptr`,
*  with `ranges::iterator_t<V>()`,
*  with `ranges::iterator_t<V>()`.
2. A private constructor which is used by `chunk_by_view::begin` and `chunk_by_view::end`. This constructor is not accessible to users. Initializes:
*  with `std::addressof(parent)`,
*  with `current`,
*  with `next`.

## Parameters


### Parameters

- `parent` - a parent object
- `current, next` - iterators

## Example

