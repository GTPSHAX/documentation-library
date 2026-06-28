---
title: std::ranges::uninitialized_fill_n
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/ranges/uninitialized_fill_n
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++20|constexpr=c++26|
template< /*nothrow-forward-iterator*/ I, class T >
requires std::constructible_from<std::iter_value_t<I>, const T&>
I uninitialized_fill_n( I first, std::iter_difference_t<I> count,
const T& value );
dcl|num=2|since=c++26|1=
template< /*execution-policy*/ Ep, /*nothrow-random-access-iterator*/ I,
class T = std::iter_value_t<I> >
requires std::constructible_from<std::iter_value_t<I>, const T&>
I uninitialized_fill_n( Ep&& exec, I first, std::iter_difference_t<I> count,
const T& value );
```

For the definition of `/*execution-policy*/`, see this page; for the definition of other exposition-only concepts, see this page.
1. Constructs elements in the destination range  with the given value `value` as if by
box|
`return ranges::uninitialized_fill(std::counted_iterator(first, count),`<br />
`std::default_sentinel, value).base();`
@@ If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.
2. Same as , but executed according to `policy`.

## Parameters


### Parameters

- `first` - the beginning of the range of the elements to initialize
- `count` - number of elements to construct
- `value` - the value to construct the elements with
- `policy` - execution policy

## Return value

As described above.

## Exceptions

Any exception thrown on construction of the elements in the destination range.
2.

## Notes

An implementation may improve the efficiency of the `ranges::uninitialized_fill_n` (by using e.g. ) if the value type of the output range is *TrivialType*.

## Possible implementation

eq fun|1=
struct uninitialized_fill_n_fn
{
template</*nothrow-forward-range*/ I, class T>
requires std::constructible_from<std::iter_value_t<I>, const T&>
constexpr I operator()(I first, std::iter_difference_t<I> count,
const T& value) const
{
I rollback{first};
try
{
for (; count-- > 0; ++first)
ranges::construct_at(std::addressof(*first), value);
return first;
}
catch (...) // rollback: destroy constructed elements
{
for (; rollback != first; ++rollback)
ranges::destroy_at(std::addressof(*rollback));
throw;
}
}
};
inline constexpr uninitialized_fill_n_fn uninitialized_fill_n{};

## Example


### Example


**Output:**
```
cppreference
cppreference
cppreference
```


## See also


| cpp/memory/ranges/dsc uninitialized_fill | (see dedicated page) |
| cpp/memory/dsc uninitialized_fill_n | (see dedicated page) |

