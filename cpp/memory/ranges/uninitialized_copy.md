---
title: std::ranges::uninitialized_copy_result
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/ranges/uninitialized_copy
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++20|constexpr=c++26|
template< std::input_iterator I, std::sentinel_for<I> S1,
/*nothrow-forward-iterator*/ O, /*nothrow-sentinel-for*/<O> S2 >
requires std::constructible_from<std::iter_value_t<O>,
std::iter_reference_t<I>>
uninitialized_copy_result<I, O>
uninitialized_copy( I ifirst, S1 ilast, O ofirst, S2 olast );
dcla|num=2|since=c++20|constexpr=c++26|
template< ranges::input_range IR, /*nothrow-forward-range*/ OR >
requires std::constructible_from<ranges::range_value_t<OR>,
ranges::range_reference_t<IR>>
uninitialized_copy_result<ranges::borrowed_iterator_t<IR>,
ranges::borrowed_iterator_t<OR>>
uninitialized_copy( IR&& in_range, OR&& out_range );
dcl|num=3|since=c++26|
template< /*execution-policy*/ Ep,
std::random_access_iterator I, std::sized_sentinel_for<I> S1,
/*nothrow-random-access-iterator*/ O,
/*nothrow-sized-sentinel-for*/<O> S2 >
requires std::constructible_from<std::iter_value_t<O>,
std::iter_reference_t<I>>
uninitialized_copy_result<I, O>
uninitialized_copy( Ep&& policy, I ifirst, S1 ilast, O ofirst, S2 olast );
dcl|num=4|since=c++26|
template< /*execution-policy*/ Ep, /*sized-random-access-range*/ IR,
/*nothrow-sized-random-access-range*/ OR >
requires std::constructible_from<ranges::range_value_t<OR>,
ranges::range_reference_t<IR>>
uninitialized_copy_result<ranges::borrowed_iterator_t<IR>,
ranges::borrowed_iterator_t<OR>>
uninitialized_copy( Ep&& policy, IR&& in_range, OR&& out_range );
dcl|num=5|since=c++20|1=
template< class I, class O >
using uninitialized_copy_result = ranges::in_out_result<I, O>;
```

For the definition of `/*execution-policy*/`, see this page; for the definition of `/*sized-random-access-range*/`, see this page; for the definition of other exposition-only concepts, see this page.
1. Constructs elements in the destination range [ofirst, olast) from elements in the source range [ifirst, ilast) as if by
box|
`1=for (; ifirst != ilast && ofirst != olast; ++ofirst, (void)++ifirst)`<br />
`::new (``(*ofirst)) std::remove_reference_t<std::iter_reference_t<O>>(*ifirst);`<br />
}
@@ If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.
@@ .
2. Same as , but uses `in_range` as the source range and `out_range` as the destination range.
@3,4@ Same as , but executed according to `policy`.

## Parameters


### Parameters

- `[ifirst, ilast)` - 
- `in_range` - the  of elements to copy from
- `[ofirst, olast)` - 
- `out_range` - the destination 
- `policy` - execution policy

## Return value

As described above.

## Exceptions

Any exception thrown on construction of the elements in the destination range.
@3,4@

## Notes

An implementation may improve the efficiency of `ranges::uninitialized_copy` if the value type of the output range is *TrivialType*.

## Possible implementation

eq fun|1=
struct uninitialized_copy_fn
{
template<std::input_iterator I, std::sentinel_for<I> S1,
/*nothrow-forward-iterator*/ O, /*nothrow-sentinel-for*/<O> S2>
requires std::constructible_from<std::iter_value_t<O>, std::iter_reference_t<I>>
constexpr ranges::uninitialized_copy_result<I, O>
operator()(I ifirst, S1 ilast, O ofirst, S2 olast) const
{
O current{ofirst};
try
{
for (; !(ifirst == ilast or current == olast); ++ifirst, ++current)
ranges::construct_at(std::addressof(*current), *ifirst);
return {std::move(ifirst), std::move(current)};
}
catch (...) // rollback: destroy constructed elements
{
for (; ofirst != current; ++ofirst)
ranges::destroy_at(std::addressof(*ofirst));
throw;
}
}
template<ranges::input_range IR, /*nothrow-forward-range*/ OR>
requires std::constructible_from<ranges::range_value_t<OR>,
ranges::range_reference_t<IR>>
constexpr ranges::uninitialized_copy_result<ranges::borrowed_iterator_t<IR>,
ranges::borrowed_iterator_t<OR>>
operator()(IR&& in_range, OR&& out_range) const
{
return (*this)(ranges::begin(in_range), ranges::end(in_range),
ranges::begin(out_range),
ranges::next(ranges::begin(out_range), ranges::end(out_range)));
}
template<ranges::forward_range IR, /*nothrow-forward-range*/ OR>
requires std::constructible_from<ranges::range_value_t<OR>,
ranges::range_reference_t<IR>>
constexpr ranges::uninitialized_copy_result<ranges::borrowed_iterator_t<IR>,
ranges::borrowed_iterator_t<OR>>
operator()(IR&& in_range, OR&& out_range) const
{
return (*this)(ranges::begin(in_range),
ranges::next(ranges::begin(in_range), ranges::end(in_range)),
ranges::begin(out_range),
ranges::next(ranges::begin(out_range), ranges::end(out_range)));
}
};
inline constexpr uninitialized_copy_fn uninitialized_copy{};

## Example


### Example

```cpp
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <memory>
#include <string>

int main()
{
    const char* v[]{"This", "is", "an", "example"};

    if (const auto sz{std::size(v)};
        void* pbuf = std::aligned_alloc(alignof(std::string), sizeof(std::string) * sz))
    {
        try
        {
            auto first{static_cast<std::string*>(pbuf)};
            auto last{first + sz};
            std::ranges::uninitialized_copy(std::begin(v), std::end(v), first, last);

            std::cout << "{";
            for (auto it{first}; it != last; ++it)
                std::cout << (it == first ? "" : ", ") << std::quoted(*it);
            std::cout << "};\n";

            std::ranges::destroy(first, last);
        }
        catch (...)
        {
            std::cout << "uninitialized_copy exception\n";
        }
        std::free(pbuf);
    }
}
```


**Output:**
```
{"This", "is", "an", "example"};
```


## See also


| cpp/memory/ranges/dsc uninitialized_copy_n | (see dedicated page) |
| cpp/memory/dsc uninitialized_copy | (see dedicated page) |

