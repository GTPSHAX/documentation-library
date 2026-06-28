---
title: operators (ranges::zip_transform_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_transform_view/iterator/operator_arith2
---


# operator+,-small|(ranges::zip_transform_view::''iterator'')


```cpp
dcl|num=1|since=c++23|1=
friend constexpr /*iterator*/ operator+( const /*iterator*/& i, difference_type n )
requires ranges::random_access_range<Base>;
dcl|num=2|since=c++23|1=
friend constexpr /*iterator*/ operator+( difference_type n, const /*iterator*/& i )
requires ranges::random_access_range<Base>;
dcl|num=3|since=c++23|1=
friend constexpr /*iterator*/ operator-( const /*iterator*/& i, difference_type n )
requires ranges::random_access_range<Base>;
dcl|num=4|since=c++23|1=
friend constexpr difference_type operator-( const /*iterator*/& i,
const /*iterator*/& j )
requires std::sized_sentinel_for</*ziperator*/<Const>, /*ziperator*/<Const>>;
```

Let  denote the underlying iterator.
@1,2@ Returns the iterator `i` incremented by `n`. Equivalent to: `1=return /*iterator*/(*i.parent_, i.inner_ + n);`.
3. Returns the iterator `i` decremented by `n`. Equivalent to: `1=return /*iterator*/(*i.parent_, i.inner_ - n);`.
4. Calculates the ''distance'' between `i` and `j`. Equivalent to `return i.inner_ - j.inner_;`.

## Parameters


### Parameters

- `i, j` - the iterators
- `n` - position relative to current location

## Return value

@1,2@ }
3. }
4. `i.inner_ - j.inner_`

## Example


## See also


| cpp/ranges/adaptor/iterator/dsc operator arith|zip_transform_view | (see dedicated page) |

