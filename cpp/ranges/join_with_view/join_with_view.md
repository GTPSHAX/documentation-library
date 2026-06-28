---
title: std::ranges::join_with_view::join_with_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_with_view/join_with_view
---


```cpp
dcl|num=1|since=c++23|1=
join_with_view()
requires std::default_initializable<V> &&
std::default_initializable<Pattern> = default;
dcl|num=2|since=c++23|
constexpr explicit join_with_view( V base, Pattern pattern );
dcl|num=3|since=c++23|
template< ranges::input_range R >
requires std::constructible_from<V, views::all_t<R>> &&
std::constructible_from
<Pattern, ranges::single_view
<ranges::range_value_t</*InnerRng*/>>>
constexpr explicit join_with_view
( R&& r, ranges::range_value_t</*InnerRng*/> e );
```

Constructs a `join_with_view`, initializes the underlying view  and the stored pattern .


| rowspan=2 | Overload |
| colspan=2 | rlps | /#Data members |
| - |
| style="font-weight: normal;" | tti | base_ |
| style="font-weight: normal;" | tti | pattern_ |
| - |
| v | 1 |
| [[cpp/language/value initialization | value-initialized]] |
| [[cpp/language/value initialization | value-initialized]] |
| - |
| v | 2 |
| initialized with c | std::move(base) |
| initialized with c | std::move(pattern) |
| - |
| v | 3 |
| initialized with c | views::all(std::forward<R>(r)) |
| initialized with c | views::single(std::move(e)) |


## Parameters


### Parameters

- `base` - a view of ranges to be flattened
- `pattern` - view to be used as the delimiter
- `e` - element to be used as the delimiter

## Example

