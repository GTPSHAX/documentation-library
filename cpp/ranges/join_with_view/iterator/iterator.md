---
title: std::ranges::join_with_view::iterator<Const>::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_with_view/iterator/iterator
---


```cpp
dcl|num=1|since=c++23|1=
/*iterator*/() = default;
dcl|num=2|since=c++23|
constexpr /*iterator*/( /*iterator*/<!Const> i )
requires Const &&
std::convertible_to<ranges::iterator_t<V>, /*OuterIter*/> &&
std::convertible_to<ranges::iterator_t</*InnerRng*/>,
/*InnerIter*/> &&
std::convertible_to<ranges::iterator_t<Pattern>, /*PatternIter*/>;
dcla|num=3|since=c++23|expos=yes|
constexpr /*iterator*/( /*Parent*/& parent, /*OuterIter*/ outer )
requires std::forward_range</*Base*/>;
dcla|num=4|since=c++23|expos=yes|
constexpr explicit /*iterator*/( /*Parent*/ parent )
requires (!std::forward_range</*Base*/>);
```

Construct an iterator. Overloads  are called by  and  of `ranges::join_with_view`.


| rowspan=2 | Overload |
| colspan=3 | rlps | /#Data members |
| - |
| style="font-weight: normal;" | tti | parent_ |
| style="font-weight: normal;" | tti | outer_it_ |
| style="font-weight: normal;" | tti | inner_it_ |
| - |
| v | 1 |
| initialized with c | nullptr |
| [[cpp/language/value initialization | value-initialized]]<br>small | (only if rlpsi | /#Base models lconcept | forward_range) |
| rowspan=4 | [[cpp/language/default initialization | default-initialized]] |
| - |
| v | 2 |
| initialized with box | c/core | i.rlpsi | /#parent_ |
| initialized with box | c/core | std::move(i.rlpsi | /#outer_it_<br>small | (only if rlpsi | /#Base models lconcept | forward_range) |
| - |
| v | 3 |
| rowspan=2 | initialized with<br>c | std::addressof(parent) |
| initialized with c | std::move(outer) |
| - |
| v | 4 |
|  |

2. After initializing the data members, equivalent to box|
`if (i.``1=.index() == 0)`<br>
`.template emplace<0>(std::get<0>(std::move(i.``)));`<br>
`else`<br>
`.template emplace<1>(std::get<1>(std::move(i.``)));`
.
@3,4@ After initializing the data members, adjust the `outer iterator` as if the `inner iterator` was incremented by .

## Parameters


### Parameters

- `i` - a mutable iterator
- `parent` - a `std::ranges::join_with_view` object
- `outer` - an iterator into the underlying range of `parent`

## Example

