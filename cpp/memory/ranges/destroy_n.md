---
title: std::ranges::destroy_n
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/ranges/destroy_n
---


```cpp
**Header:** `<`memory`>`
dcl|num=1|since=c++20|
template< /*nothrow-input-iterator*/ I >
requires std::destructible<std::iter_value_t<I>>
constexpr I destroy_n( I first, std::iter_difference_t<I> count ) noexcept;
dcl|num=2|since=c++26|
template< /*execution-policy*/ Ep, /*nothrow-random-access-iterator*/ I >
requires std::destructible<std::iter_value_t<I>>
I destroy_n( Ep&& policy, I first, std::iter_difference_t<I> count );
```

For the definition of `/*execution-policy*/`, see this page; for the definition of other exposition-only concepts, see this page.
1. Destroys elements in the target range  as if by

```cpp
return std::ranges::destroy(std::counted_iterator(first, count),
                            std::default_sentinel).base();
```

2. Same as , but executed according to `policy`.

## Parameters


### Parameters

- `first` - the beginning of the range of elements to destroy
- `count` - the number of elements to destroy
- `policy` - execution policy

## Return value

As described above.

## Notes


## Possible implementation

eq fun|1=
struct destroy_n_fn
{
template</*nothrow-input-iterator*/ I>
requires std::destructible<std::iter_value_t<I>>
constexpr I operator()(I first, std::iter_difference_t<I> n) const noexcept
{
for (; n != 0; (void)++first, --n)
std::ranges::destroy_at(std::addressof(*first));
return first;
}
};
inline constexpr destroy_n_fn destroy_n{};

## Example


## See also


| cpp/memory/ranges/dsc destroy_at | (see dedicated page) |
| cpp/memory/ranges/dsc destroy | (see dedicated page) |
| cpp/memory/dsc destroy_n | (see dedicated page) |

