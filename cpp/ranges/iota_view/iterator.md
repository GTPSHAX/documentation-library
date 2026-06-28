---
title: std::ranges::iota_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/iota_view/iterator
---


```cpp
dcla|num=1|anchor=no|expos=yes|
struct /*iterator*/;
dcla|num=2|anchor=iota-diff-t|expos=yes|1=
template< class I >
using /*iota-diff-t*/ = /* see below */;
dcla|num=3|anchor=decrementable|expos=yes|1=
template< class I >
concept /*decrementable*/ =
std::incrementable<I> && requires(I i)
{
{ --i } -> std::same_as<I&>;
{ i-- } -> std::same_as<I>;
};
dcla|num=4|anchor=advanceable|expos=yes|1=
template< class I >
concept /*advanceable*/ =
/*decrementable*/<I> && std::totally_ordered<I> &&
requires(I i, const I j, const /*iota-diff-t*/<I> n)
{
{ i += n } -> std::same_as<I&>;
{ i -= n } -> std::same_as<I&>;
I(j + n);
I(n + j);
I(j - n);
{ j - j } -> std::convertible_to</*iota-diff-t*/<I>>;
};
```

1. `ranges::iota_view<W, Bound>::` is the type of the iterators returned by  and  of `ranges::iota_view<W, Bound>`.
2. Calculates the difference type for both iterator types and integer-like types.
* If `I` is not an integral type, or if it is an integral type and `sizeof(std::iter_difference_t<I>)` is greater than `sizeof(I)`, then `/*iota-diff-t*/<I>` is `std::iter_difference_t<I>`.
* Otherwise, `/*iota-diff-t*/<I>` is a signed integer type of width greater than the width of `I` if such a type exists.
* Otherwise, `I` is one of the widest integral types, and `/*iota-diff-t*/<I>` is an unspecified signed-integer-like type of width not less than the width of `I`. It is unspecified whether `/*iota-diff-t*/<I>` models  in this case.
3. Specifies that a type is , and pre- and post- `operator--` for the type have common meaning.
4. Specifies that a type is both  and , and `1=operator+=`, `1=operator-=`, `operator+`, and `operator-` among the type and its different type have common meaning.
`/*iterator*/` models
*  if `W` models  ,
*  if `W` models  ,
*  if `W` models , and
*  otherwise.
However, it only satisfies *InputIterator* if `W` models , and does not satisfy *InputIterator* otherwise.

## Semantic requirements

3. Type `I` models  only if `I` satisfies  and all concepts it subsumes are modeled, and given equal objects `a` and `b` of type `I`:
* If `a` and `b` are in the domain of both pre- and post- `operator--` (i.e. they are decrementable), then the following are all `true`:
** `1=std::addressof(--a) == std::addressof(a)`,
** `1=bool(a-- == b)`,
** `1=bool(((void)a--, a) == --b)`,
** `1=bool(++(--a) == b)`.
* If `a` and `b` are in the domain of both pre- and post- `operator++` (i.e. they are incrementable), then `1=bool(--(++a) == b)` is `true`.
4. Let `D` denote `/*iota-diff-t*/<I>`. Type `I` models  only if `I` satisfies  and all concepts it subsumes are modeled, and given
* objects `a` and `b` of type `I` and
* value `n` of type `D`,
such that `b` is reachable from `a` after `n` applications of `++a`, all following conditions are satisfied:
* `1=(a += n)` is equal to `b`.
* `1=std::addressof(a += n)` is equal to `std::addressof(a)`.
* `I(a + n)` is equal to `1=(a += n)`.
* For any two positive values `x` and `y` of type `D`, if `I(a + D(x + y))` is well-defined, then `I(a + D(x + y))` is equal to `I(I(a + x) + y)`.
* `I(a + D(0))` is equal to `a`.
* If `I(a + D(n - 1))` is well-defined, then `I(a + n)` is equal to }.
* `1=(b += -n)` is equal to `a`.
* `1=(b -= n)` is equal to `a`.
* `1=std::addressof(b -= n)` is equal to `std::addressof(b)`.
* `I(b - n)` is equal to `1=(b -= n)`.
* `D(b - a)` is equal to `n`.
* `D(a - b)` is equal to `D(-n)`.
* `1=bool(a <= b)` is `true`.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


### Determining the iterator concept

`iterator_concept` is defined as follows:
* If `W` models , `iterator_concept` denotes `std::random_access_iterator_tag`.
* Otherwise, if `W` models , `iterator_concept` denotes `std::bidirectional_iterator_tag`.
* Otherwise, if `W` models , `iterator_concept` denotes `std::forward_iterator_tag`.
* Otherwise, `iterator_concept` denotes `std::input_iterator_tag`.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions

member|''iterator''|2=

```cpp
dcl|num=1|since=c++20|1=
/*iterator*/() requires std::default_initializable<W> = default;
dcl|num=2|since=c++20|
constexpr explicit /*iterator*/( W value );
```

1. Value initializes .
2. Initializes  with `value`.
member|operator*|2=
ddcl|since=c++20|
constexpr W operator*() const
noexcept(std::is_nothrow_copy_constructible_v<W>);
Returns .

## Example


### Example

```cpp
#include <cassert>
#include <ranges>

int main()
{
    auto it{std::views::iota(6, 9).begin()};
    const int& r = *it; // binds with temporary
    assert(*it == 6 and r == 6);
    ++it;
    assert(*it == 7 and r == 6);
}
```

member|operator++|2=

```cpp
dcl|num=1|since=c++20|
constexpr /*iterator*/& operator++();
dcl|num=2|since=c++20|
constexpr void operator++(int);
dcl|num=3|since=c++20|
constexpr /*iterator*/ operator++(int) requires std::incrementable<W>;
```

1. Equivalent to .
2. Equivalent to .
3. Equivalent to .

## Example


### Example

```cpp
#include <cassert>
#include <ranges>

int main()
{
    auto it{std::views::iota(8).begin()};
    assert(*it == 8);
    assert(*++it == 9);
    assert(*it++ == 9);
    assert(*it == 10);
}
```

member|operator--|2=

```cpp
dcl|num=1|since=c++20|
constexpr /*iterator*/& operator--() requires /*decrementable*/<W>;
dcl|num=2|since=c++20|
constexpr /*iterator*/operator--(int) requires /*decrementable*/<W>;
```

1. Equivalent to .
2. Equivalent to .

## Example


### Example

```cpp
#include <cassert>
#include <ranges>

int main()
{
    auto it{std::views::iota(8).begin()};
    assert(*it == 8);
    assert(*--it == 7);
    assert(*it-- == 7);
    assert(*it == 6);
}
```

member|1=operator+=|2=
ddcl|since=c++20|1=
constexpr /*iterator*/& operator+=( difference_type n )
requires /*advanceable*/<W>;
Updates  and returns `*this`:
* If `W` is an unsigned-integer-like type:
** If `n` is non-negative, performs .
** Otherwise, performs .
* Otherwise, performs .

## Example


### Example

```cpp
#include <cassert>
#include <ranges>

int main()
{
    auto it{std::views::iota(5).begin()};
    assert(*it == 5);
    assert(*(it += 3) == 8);
}
```

member|1=operator-=|2=
ddcl|since=c++20|1=
constexpr /*iterator*/& operator-=( difference_type n )
requires /*advanceable*/<W>;
Updates  and returns `*this`:
* If `W` is an unsigned-integer-like type:
** If `n` is non-negative, performs .
** Otherwise, performs .
* Otherwise, performs .

## Example


### Example

```cpp
#include <cassert>
#include <ranges>

int main()
{
    auto it{std::views::iota(6).begin()};
    assert(*it == 6);
    assert(*(it -= -3) == 9);
}
```

member|operator[]|2=
ddcl|since=c++20|
constexpr W operator[]( difference_type n ) const
requires /*advanceable*/<W>;
Returns .

## Example


### Example

```cpp
#include <cassert>
#include <ranges>

int main()
{
    auto it{std::views::iota(6).begin()};
    assert(*it == 6);
    assert(*(it + 3) == 9);
}
```


## Non-member functions

member|1=operator==, <, >, <=, >=, <=>|2=

```cpp
dcl|num=1|since=c++20|1=
friend constexpr bool operator==
( const /*iterator*/& x, const /*iterator*/& y )
requires std::equality_comparable<W>;
dcl|num=2|since=c++20|
friend constexpr bool operator<
( const /*iterator*/& x, const /*iterator*/& y )
requires std::totally_ordered<W>;
dcl|num=3|since=c++20|
friend constexpr bool operator>
( const /*iterator*/& x, const /*iterator*/& y )
requires std::totally_ordered<W>;
dcl|num=4|since=c++20|1=
friend constexpr bool operator<=
( const /*iterator*/& x, const /*iterator*/& y )
requires std::totally_ordered<W>;
dcl|num=5|since=c++20|1=
friend constexpr bool operator>=
( const /*iterator*/& x, const /*iterator*/& y )
requires std::totally_ordered<W>;
dcl|num=6|since=c++20|1=
friend constexpr bool operator<=>
( const /*iterator*/& x, const /*iterator*/& y )
requires std::totally_ordered<W> && std::three_way_comparable<W>;
```

1. Returns .
2. Returns .
3. Returns `y < x`.
4. Returns `!(y < x)`.
5. Returns `!(x < y)`.
6. Returns .
member|1=operator+|2=

```cpp
dcl|num=1|since=c++20|
friend constexpr /*iterator*/ operator+
( /*iterator*/ i, difference_type n )
requires /*advanceable*/<W>;
dcl|num=2|since=c++20|
friend constexpr /*iterator*/ operator+
( difference_type n, /*iterator*/ i )
requires /*advanceable*/<W>;
```

Equivalent to `1=i += n; return i;`.
member|1=operator-|2=

```cpp
dcl|num=1|since=c++20|
friend constexpr /*iterator*/ operator-
( /*iterator*/ i, difference_type n )
requires /*advanceable*/<W>;
dcl|num=2|since=c++20|
friend constexpr difference_type operator-
( const /*iterator*/& x, const /*iterator*/& y )
requires /*advanceable*/<W>;
```

1. Equivalent to `1=i -= n; return i;`.
2. Let `D` be `difference_type`:
* If `W` is an integer-like type:
** If `W` is signed-integer-like, returns .
** Otherwise, returns .
* Otherwise, returns .

## Defect reports

