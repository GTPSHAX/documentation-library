---
title: std::ranges::enumerate_view::iterator<Const>::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/enumerate_view/iterator/iterator
---


```cpp
dcl|num=1|since=c++23|1=
/*iterator*/()
requires std::default_initializable<ranges::iterator_t<Base>> = default;
dcl|num=2|since=c++23|1=
constexpr /*iterator*/( /*iterator*/<!Const> i )
requires Const &&
std::convertible_to<ranges::iterator_t<V>, ranges::iterator_t<Base>>;
|1=
private:
constexpr explicit /*iterator*/( ranges::iterator_t<Base> current,
difference_type pos);
```

Construct an iterator.
1. Default constructor. Value-initializes the underlying iterator  with `ranges::iterator_t<Base>()` and
the underlying index  with `0`.
2. Conversion from `/*iterator*/<false>` to `/*iterator*/<true>`. Initializes  with  and  with .
3. A private constructor which is used by `cpp/ranges/enumerate_view/begin|enumerate_view::begin` and `cpp/ranges/enumerate_view/end|enumerate_view::end`. This constructor is not accessible to users. Initializes  with `std::move(current)` and  with `pos`.

## Parameters


### Parameters

- `i` - an `/*iterator*/<false>`

## Example

