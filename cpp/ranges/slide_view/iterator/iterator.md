---
title: std::ranges::slide_view::iterator<Const>::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/slide_view/iterator/iterator
---


```cpp
dcl|num=1|since=c++23|1=
/*iterator*/();
dcl|num=2|since=c++23|1=
constexpr /*iterator*/( /*iterator*/<!Const> i )
requires Const &&
std::convertible_to<ranges::iterator_t<V>, ranges::iterator_t<Base>>
|1=
private:
constexpr /*iterator*/( ranges::iterator_t<Base> current,
ranges::range_difference_t<Base> n )
requires (!/*slide-caches-first*/<Base>);
|1=
private:
constexpr /*iterator*/( ranges::iterator_t<Base> current,
ranges::iterator_t<Base> last_ele,
ranges::range_difference_t<Base> n )
requires /*slide-caches-first*/<Base>;
```

Construct an iterator.
1. Default constructor. Value-initializes the underlying data members:
*  with `ranges::iterator_t<Base>()`,
*  with `ranges::iterator_t<Base>()` (note that this member may not be present),
*  with `0`.
2. Conversion from `/*iterator*/<false>` to `/*iterator*/<true>`. Initializes the underlying data members:
*  with ,
*  with `i.n_`.
Note that `/*iterator*/<true>` can only be formed when  models `/*slide-caches-nothing*/`, in which case  is not present.
3. A private constructor which is used by `ranges::slide_view::begin` and `ranges::slide_view::end`. This constructor is not accessible to users. Initializes the underlying data members:
*  with `current`,
*  with `n`.
Note that this overload can only be present if  is not present.
4. A private constructor which is used by `ranges::slide_view::begin` and `ranges::slide_view::end`. This constructor is not accessible to users. Initializes the underlying data members:
*  with `current`,
*  with `last_ele` (note that this data member is present due to `/*slide-caches-first*/<Base>` requirement),
*  with `n`.

## Parameters


### Parameters

- `i` - an `/*iterator*/<false>`
- `current` - an iterator to current element of `slide_view`
- `last_ele` - an iterator to last element of `slide_view`
- `n` - the slide window width of `slide_view`

## Example

