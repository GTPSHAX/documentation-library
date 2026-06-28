---
title: std::ranges::uninitialized_fill
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/ranges/uninitialized_fill
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++20|constexpr=c++26|
template< /*nothrow-forward-iterator*/ I, /*nothrow-sentinel-for*/<I> S,
class T >
requires std::constructible_from<std::iter_value_t<I>, const T&>
I uninitialized_fill( I first, S last, const T& value );
dcla|num=2|since=c++20|constexpr=c++26|
template< /*nothrow-forward-range*/ R, class T >
requires std::constructible_from<ranges::range_value_t<R>, const T&>
ranges::borrowed_iterator_t<R> uninitialized_fill( R&& r,
const T& value );
dcl|num=3|since=c++26|1=
template< /*execution-policy*/ Ep, /*nothrow-random-access-iterator*/ I,
/*nothrow-sized-sentinel-for*/<I> S,
class T = std::iter_value_t<I> >
requires constructible_from<std::iter_value_t<I>, const T&>
I uninitialized_fill( Ep&& policy, I first, S last, const T& value );
dcl|num=4|since=c++26|1=
template< /*execution-policy*/ Ep, /*nothrow-sized-random-access-range*/ R,
class T = ranges::range_value_t<R> >
requires std::constructible_from<ranges::range_value_t<R>, const T&>
ranges::borrowed_iterator_t<R> uninitialized_fill( Ep&& policy, R&& r,
const T& value );
```

For the definition of `/*execution-policy*/`, see this page; for the definition of other exposition-only concepts, see this page.
1. Constructs elements in the destination range [first, last) with the given value `value` as if by
box|
`1=for (; first != last; ++first)`<br />
`::new (``(*first)) std::remove_reference_t<std::iter_reference_t<I>>(value);`<br />
`return first;`
@@ If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.
2. Same as , but uses `r` as the destination range.
@3,4@ Same as , but executed according to `policy`.

## Parameters


### Parameters

- `[3=to initialize, sentinel=yes}})` - 
- `r` - the  of the elements to initialize
- `value` - the value to construct the elements with
- `policy` - execution policy

## Return value

As described above.

## Exceptions

Any exception thrown on construction of the elements in the destination range.
@3,4@

## Notes

An implementation may improve the efficiency of the `ranges::uninitialized_fill` (by using e.g. ) if the value type of the output range is *TrivialType*.

## Possible implementation

eq fun|1=
struct uninitialized_fill_fn
{
template</*nothrow-forward-iterator*/ I, /*nothrow-sentinel-for*/<I> S, class T>
requires std::constructible_from<std::iter_value_t<I>, const T&>
constexpr I operator()(I first, S last, const T& value) const
{
I rollback{first};
try
{
for (; !(first == last); ++first)
ranges::construct_at(std::addressof(*first), value);
return first;
}
catch (...)
{
// rollback: destroy constructed elements
for (; rollback != first; ++rollback)
ranges::destroy_at(std::addressof(*rollback));
throw;
}
}
template</*nothrow-forward-range*/ R, class T>
requires std::constructible_from<ranges::range_value_t<R>, const T&>
constexpr ranges::borrowed_iterator_t<R> operator()(R&& r, const T& value) const
{
return (*this)(ranges::begin(r),
ranges::next(ranges::begin(r), ranges::end(r)), value);
}
};
inline constexpr uninitialized_fill_fn uninitialized_fill{};

## Example


### Example

```cpp
#include <iostream>
#include <memory>
#include <string>

int main()
{
    constexpr int n{4};
    alignas(alignof(std::string)) char out[n * sizeof(std::string)];

    try
    {
        auto first{reinterpret_cast<std::string*>(out)};
        auto last{first + n};
        std::ranges::uninitialized_fill(first, last, "▄▀▄▀▄▀▄▀");

        int count{1};
        for (auto it{first}; it != last; ++it)
            std::cout << count++ << ' ' << *it << '\n';

        std::ranges::destroy(first, last);
    }
    catch(...)
    {
        std::cout << "Exception!\n";
    }
}
```


**Output:**
```
1 ▄▀▄▀▄▀▄▀
2 ▄▀▄▀▄▀▄▀
3 ▄▀▄▀▄▀▄▀
4 ▄▀▄▀▄▀▄▀
```


## See also


| cpp/memory/ranges/dsc uninitialized_fill_n | (see dedicated page) |
| cpp/memory/dsc uninitialized_fill | (see dedicated page) |

