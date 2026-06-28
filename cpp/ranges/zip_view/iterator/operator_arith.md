---
title: std::ranges::zip_view::iterator<Const>::operators
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_view/iterator/operator_arith
---


```cpp
dcl|num=1|since=c++23|
constexpr /*iterator*/& operator++();
dcl|num=2|since=c++23|
constexpr void operator++( int );
dcl|num=3|since=c++23|
constexpr /*iterator*/ operator++( int )
requires /*all-forward*/<Const, Views...>;
dcl|num=4|since=c++23|
constexpr /*iterator*/& operator--()
requires /*all-bidirectional*/<Const, Views...>;
dcl|num=5|since=c++23|
constexpr /*iterator*/ operator--( int )
requires /*all-bidirectional*/<Const, Views...>;
dcl|num=6|since=c++23|1=
constexpr /*iterator*/& operator+=( difference_type n )
requires /*all-random-access*/<Const, Views...>;
dcl|num=7|since=c++23|1=
constexpr /*iterator*/& operator-=( difference_type n )
requires /*all-random-access*/<Const, Views...>;
```

Increments or decrements each of the underlying  iterators in the underlying tuple-like object .
1. Equivalent to
}
2. Equivalent to `1=++*this;`
3. Equivalent to `1=auto tmp = *this; ++*this; return tmp;`
4. Equivalent to
}
5. Equivalent to `1=auto tmp = *this; --*this; return tmp;`
6. Equivalent to
}
7. Equivalent to
}

## Parameters


### Parameters

- `n` - position relative to current location

## Return value

@1,4,6,7@ `*this`
2. (none)
@3,5@ a copy of `*this` that was made before the change

## Example

