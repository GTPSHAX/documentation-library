---
title: std::ranges::uninitialized_value_construct
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/ranges/uninitialized_value_construct
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++20|constexpr=c++26|
template< /*nothrow-forward-iterator*/ I, /*nothrow-sentinel-for*/<I> S >
requires std::default_initializable<std::iter_value_t<I>>
I uninitialized_value_construct( I first, S last );
dcla|num=2|since=c++20|constexpr=c++26|
template< /*nothrow-forward-range*/ R >
requires std::default_initializable<ranges::range_value_t<R>>
ranges::borrowed_iterator_t<R>
uninitialized_value_construct( R&& r );
dcl|num=3|since=c++26|
template< /*execution-policy*/ Ep, /*nothrow-random-access-iterator*/ I,
/*nothrow-sized-sentinel-for*/<I> S >
requires std::default_initializable<std::iter_value_t<I>>
I uninitialized_value_construct( Ep&& policy, I first, S last );
dcl|num=4|since=c++26|
template< /*execution-policy*/ Ep, /*nothrow-sized-random-access-range*/ R >
requires std::default_initializable<ranges::range_value_t<R>>
ranges::borrowed_iterator_t<R>
uninitialized_value_construct( Ep&& policy, R&& r );
```

For the definition of `/*execution-policy*/`, see this page; for the definition of other exposition-only concepts, see this page.
1. Constructs elements in the destination range [first, last) by value-initialization as if by
box|
`1=for (; first != last; ++first)`<br />
`::new (``(*first))`<br />
`std::remove_reference_t<std::iter_reference_t<I>>();`<br />
`return first;`
@@ If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.
2. Same as , but uses `r` as the destination range.
@3,4@ Same as , but executed according to `policy`.

## Parameters


### Parameters

- `[3=to value-initialize, sentinel=yes}})` - 
- `r` - the  of the elements to value-initialize
- `policy` - execution policy

## Return value

As described above.

## Exceptions

Any exception thrown on construction of the elements in the destination range.
@3,4@

## Notes

An implementation may improve the efficiency of the `ranges::uninitialized_value_construct` (by using e.g. ) if the value type of the range is a *CopyAssignable* *TrivialType*.

## Possible implementation

eq fun|1=
struct uninitialized_value_construct_fn
{
template</*nothrow-forward-iterator*/ I, /*nothrow-sentinel-for*/<I> S>
requires std::value_initializable<std::iter_value_t<I>>
constexpr I operator()(I first, S last) const
{
using value_type = std::remove_reference_t<std::iter_reference_t<I>>;
if constexpr (std::is_trivially_default_constructible_v<value_type>)
return ranges::fill(first, last, ValueType());
I rollback{first};
try
{
for (; !(first == last); ++first)
::new (static_cast<void*>(std::addressof(*first))) value_type();
return first;
}
catch (...) // rollback: destroy constructed elements
{
for (; rollback != first; ++rollback)
ranges::destroy_at(std::addressof(*rollback));
throw;
}
}
template</*nothrow-forward-range*/ R>
requires std::default_initializable<ranges::range_value_t<R>>
constexpr ranges::borrowed_iterator_t<R> operator()(R&& r) const
{
return (*this)(ranges::begin(r),
ranges::next(ranges::begin(r), ranges::end(r)));
}
};
inline constexpr uninitialized_value_construct_fn uninitialized_value_construct{};

## Example


### Example

```cpp
#include <iostream>
#include <memory>
#include <string>

int main()
{
    struct S { std::string m{"▄▀▄▀▄▀▄▀"}; };

    constexpr int n{4};
    alignas(alignof(S)) char out[n * sizeof(S)];

    try
    {
        auto first{reinterpret_cast<S*>(out)};
        auto last{first + n};

        std::ranges::uninitialized_value_construct(first, last);

        auto count{1};
        for (auto it{first}; it != last; ++it)
            std::cout << count++ << ' ' << it->m << '\n';

        std::ranges::destroy(first, last);
    }
    catch (...)
    {
        std::cout << "Exception!\n";
    }

    // For scalar types, uninitialized_value_construct
    // zero-fills the given uninitialized memory area.
    int v[]{0, 1, 2, 3};
    std::cout << ' ';
    for (const int i : v)
        std::cout << ' ' << static_cast<char>(i + 'A');
    std::cout << "\n ";
    std::ranges::uninitialized_value_construct(std::begin(v), std::end(v));
    for (const int i : v)
        std::cout << ' ' << static_cast<char>(i + 'A');
    std::cout << '\n';
}
```


**Output:**
```
1 ▄▀▄▀▄▀▄▀
2 ▄▀▄▀▄▀▄▀
3 ▄▀▄▀▄▀▄▀
4 ▄▀▄▀▄▀▄▀
  A B C D
  A A A A
```


## See also


| cpp/memory/ranges/dsc uninitialized_value_construct_n | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_default_construct | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_default_construct_n | (see dedicated page) |
| cpp/memory/dsc uninitialized_value_construct | (see dedicated page) |

