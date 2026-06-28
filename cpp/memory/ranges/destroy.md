---
title: std::ranges::destroy
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/ranges/destroy
---


```cpp
**Header:** `<`memory`>`
dcl|num=1|since=c++20|
template< /*nothrow-input-iterator*/ I, /*nothrow-sentinel-for*/<I> S >
requires std::destructible<std::iter_value_t<I>>
constexpr I destroy( I first, S last ) noexcept;
dcl|num=2|since=c++20|
template< /*nothrow-input-range*/ R >
requires std::destructible<ranges::range_value_t<R>>
constexpr ranges::borrowed_iterator_t<R> destroy( R&& r ) noexcept;
dcl|num=3|since=c++26|
template< /*execution-policy*/ Ep, /*nothrow-random-access-iterator*/ I,
/*nothrow-sized-sentinel-for*/<I> S >
requires std::destructible<std::iter_value_t<I>>
I destroy( Ep&& policy, I first, S last );
dcl|num=4|since=c++26|
template< /*execution-policy*/ Ep, /*nothrow-sized-random-access-range*/ R >
requires std::destructible<ranges::range_value_t<R>>
ranges::borrowed_iterator_t<R> destroy( Ep&& policy, R&& r );
```

For the definition of `/*execution-policy*/`, see this page; for the definition of other exposition-only concepts, see this page.
1. Destroys elements in the target range [first, last) as if by

```cpp
for (; first != last; ++first)
    std::ranges::destroy_at(std::addressof(*first));
return first;
```

2. Same as , but uses `r` as the target range.
@3,4@ Same as , but executed according to `policy`.

## Parameters


### Parameters

- `[3=to destroy, sentinel=yes}})` - 
- `r` - the  to destroy
- `policy` - execution policy

## Return value

As described above.

## Exceptions

@3,4@

## Notes


## Possible implementation

eq fun|1=
struct destroy_fn
{
template</*nothrow-input-iterator*/ I, /*nothrow-sentinel-for*/<I> S>
requires std::destructible<std::iter_value_t<I>>
constexpr I operator()(I first, S last) const noexcept
{
for (; first != last; ++first)
ranges::destroy_at(std::addressof(*first));
return first;
}
template</*nothrow-input-range*/ R>
requires std::destructible<ranges::range_value_t<R>>
constexpr ranges::borrowed_iterator_t<R> operator()(R&& r) const noexcept
{
return (*this)(ranges::begin(r), ranges::end(r));
}
template</*nothrow-forward-range*/ R>
requires std::destructible<ranges::range_value_t<R>>
constexpr ranges::borrowed_iterator_t<R> operator()(R&& r) const noexcept
{
return (*this)(ranges::begin(r),
ranges::next(ranges::begin(r), ranges::end(r)));
}
};
inline constexpr destroy_fn destroy{};

## Example


## See also


| cpp/memory/ranges/dsc destroy_n | (see dedicated page) |
| cpp/memory/ranges/dsc destroy_at | (see dedicated page) |
| cpp/memory/dsc destroy | (see dedicated page) |

