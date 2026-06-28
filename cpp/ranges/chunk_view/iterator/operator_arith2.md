---
title: operators (ranges::chunk_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/iterator/operator_arith2
---


# operator+,-small|(ranges::chunk_view::''iterator'')


```cpp
dcl|num=1|since=c++23|
friend constexpr /*iterator*/ operator+( const /*iterator*/& i,
difference_type pos )
requires ranges::random_access_range<Base>;
dcl|num=2|since=c++23|
friend constexpr /*iterator*/ operator+( difference_type pos,
const /*iterator*/& i )
requires ranges::random_access_range<Base>;
dcl|num=3|since=c++23|
friend constexpr /*iterator*/ operator-( const /*iterator*/& i,
difference_type pos )
requires ranges::random_access_range<Base>;
dcl|num=4|since=c++23|
friend constexpr difference_type operator-( const /*iterator*/& i,
const /*iterator*/& j )
requires std::sized_sentinel_for<ranges::iterator_t<Base>,
ranges::iterator_t<Base>>;
dcl|num=5|since=c++23|
friend constexpr difference_type operator-( std::default_sentinel_t,
const /*iterator*/& i )
requires std::sized_sentinel_for<ranges::sentinel_t<Base>,
ranges::iterator_t<Base>>;
dcl|num=6|since=c++23|
friend constexpr difference_type operator-( const /*iterator*/& i,
std::default_sentinel_t )
requires std::sized_sentinel_for<ranges::sentinel_t<Base>,
ranges::iterator_t<Base>>;
```

Performs `iterator` arithmetic or calculates the distance.
Let , , , and  be the underlying `data members`.
Equivalent to:
@1,2@ `1=auto r = i; r += pos; return r;`.
3. `1=auto r = i; r -= pos; return r;`.
4. `1=return (i.current_ - j.current_ + i.missing_ - j.missing_) / i.n_;`.
5. `1=return /*div-ceil*/(i.end_ - i.current_, i.n_);`.
6. `1=return -(y - x);`.

## Parameters


### Parameters

- `i, j` - the iterators
- `pos` - the position relative to current location

## Return value

@1,2@ An incremented iterator.
3. A decremented iterator.
4. A distance (in number of elements, i.e. chunks) between given iterators.
@5,6@ A distance (in number of elements) between given iterator and sentinel.

## Example

