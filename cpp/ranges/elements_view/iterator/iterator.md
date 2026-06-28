---
title: std::ranges::elements_view::iterator<Const>::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/elements_view/iterator/iterator
---


```cpp
dcl | num=1 | since=c++20 | 1=
/*iterator*/() requires std::default_initializable<ranges::iterator_t<Base>>
= default;
dcl | num=2 | since=c++20 | 1=
constexpr explicit /*iterator*/( ranges::iterator_t<Base> current );
dcl | num=3 | since=c++20 | 1=
constexpr /*iterator*/( /*iterator*/<!Const> i ) requires Const &&
std::convertible_to<ranges::iterator_t<V>, ranges::iterator_t<Base>>;
```

Construct an iterator.
1. Value-initializes the underlying iterator `''current_''` via its default member initializer (`1== ranges::iterator_t<Base>()`).
2. Initializes the underlying iterator `''current_''` with `std::move(current)`.
3. Conversion from `/*iterator*/<false>` to `/*iterator*/<true>`. Initializes the underlying iterator `''current_''` with `std::move(i.current)`.

## Parameters


### Parameters


## Example

