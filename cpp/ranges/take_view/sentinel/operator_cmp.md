---
title: operator==(std::ranges::take_view::sentinel<Const>)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/take_view/sentinel/operator_cmp
---


# 1= operator==small|(std::ranges::take_view::''sentinel''<Const>)


```cpp
dcl|num=1|since=c++20|1=
friend constexpr bool
operator==( const std::counted_iterator<ranges::iterator_t<Base>>& y,
const /*sentinel*/& x );
dcl|num=2|since=c++20|1=
template< bool OtherC = !Const >
requires std::sentinel_for<ranges::sentinel_t<Base>,
ranges::iterator_t</*add-const-if*/<OtherC, V>>>
friend constexpr bool
operator==( const std::counted_iterator<
ranges::iterator_t</*add-const-if*/<OtherC, V>>>& y,
const /*sentinel*/& x );
```

Compares a `take_view::/*sentinel*/` with a `std::counted_iterator` (typically obtained from a call to `cpp/ranges/take_view/begin|take_view::begin`).
Returns `true` if `y` points past the N element (where N is the number passed to the constructor of `take_view`), or if end of underlying view is reached.
The exposition-only alias template `/*add-const-if*/` is defined as<br>
c multi
|template<bool C, class T>
|using /*add-const-if*/  std::conditional_t<C, const T, T>;
.

## Parameters


### Parameters

- `y` - `std::counted_iterator` to compare
- `x` - sentinel to compare

## Return value

`1= y.count() == 0 , where  denotes the underlying sentinel.

## Example


## Defect reports

