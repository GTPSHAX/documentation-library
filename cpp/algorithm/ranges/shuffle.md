---
title: std::ranges::shuffle
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/shuffle
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::random_access_iterator I, std::sentinel_for<I> S, class Gen >
requires std::permutable<I> &&
std::uniform_random_bit_generator<std::remove_reference_t<Gen>>
I shuffle( I first, S last, Gen&& gen );
dcl|num=2|since=c++20|1=
template< ranges::random_access_range R, class Gen >
requires std::permutable<ranges::iterator_t<R>> &&
std::uniform_random_bit_generator<std::remove_reference_t<Gen>>
ranges::borrowed_iterator_t<R>
shuffle( R&& r, Gen&& gen );
```

1. Reorders the elements in the given range [first, last) such that each possible permutation of those elements has equal probability of appearance.
2. Same as , but uses `r` as the range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to shuffle randomly, sentinel=yes}})` - 
- `r` - the range of elements to shuffle randomly
- `gen` - the random number generator

## Return value

An iterator equal to `last`.

## Complexity

Exactly `(last - first) - 1` swaps.

## Possible implementation

eq fun|1=
struct shuffle_fn
{
template<std::random_access_iterator I, std::sentinel_for<I> S, class Gen>
requires std::permutable<I> &&
std::uniform_random_bit_generator<std::remove_reference_t<Gen>>
I operator()(I first, S last, Gen&& gen) const
{
using diff_t = std::iter_difference_t<I>;
using distr_t = std::uniform_int_distribution<diff_t>;
using param_t = typename distr_t::param_type;
distr_t D;
const auto n {last - first};
for (diff_t i {1}; i < n; ++i)
ranges::iter_swap(first + i, first + D(gen, param_t(0, i)));
return ranges::next(first, last);
}
template<ranges::random_access_range R, class Gen>
requires std::permutable<ranges::iterator_t<R>> &&
std::uniform_random_bit_generator<std::remove_reference_t<Gen>>
ranges::borrowed_iterator_t<R> operator()(R&& r, Gen&& gen) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::forward<Gen>(gen));
}
};
inline constexpr shuffle_fn shuffle {};

## Example


### Example


**Output:**
```
A B C D E F
F E A C D B
E C B F A D
B A E C F D
```


## See also


| cpp/algorithm/ranges/dsc next_permutation | (see dedicated page) |
| cpp/algorithm/ranges/dsc prev_permutation | (see dedicated page) |
| cpp/algorithm/dsc random_shuffle | (see dedicated page) |

