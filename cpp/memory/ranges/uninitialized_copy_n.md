---
title: std::ranges::uninitialized_copy_n_result
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/ranges/uninitialized_copy_n
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++20|constexpr=c++26|
template< std::input_iterator I,
/*nothrow-input-iterator*/ O, /*nothrow-sentinel-for*/<O> S >
requires std::constructible_from<std::iter_value_t<O>,
std::iter_reference_t<I>>
uninitialized_copy_n_result<I, O>
uninitialized_copy_n( I ifirst, std::iter_difference_t<I> count,
O ofirst, S olast );
dcl|num=2|since=c++26|
template< /*execution-policy*/ Ep, std::random_access_iterator I,
/*nothrow-random-access-iterator*/ O,
/*nothrow-sized-sentinel-for*/<O> S>
requires std::constructible_from<std::iter_value_t<O>,
std::iter_reference_t<I>>
uninitialized_copy_n_result<I, O>
uninitialized_copy_n( Ep&& policy,
I ifirst, std::iter_difference_t<I> count,
O ofirst, S olast );
dcl|num=3|since=c++20|1=
template< class I, class O >
using uninitialized_copy_n_result = ranges::in_out_result<I, O>;
```

For the definition of `/*execution-policy*/`, see this page; for the definition of other exposition-only concepts, see this page.
1. Constructs elements in the destination range [ofirst, olast) from elements in the source range  as if by
box|
`1=auto ret = ranges::uninitialized_copy(std::counted_iterator(std::move(ifirst), count),`<br />
`std::default_sentinel, ofirst, olast);`<br />
}
@@ If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.
@@ .
2. Same as , but executed according to `policy`.

## Parameters


### Parameters

- `ifirst` - the beginning of the range of elements to copy from
- `count` - the number of elements to copy
- `[ofirst, olast)` - 
- `policy` - execution policy

## Return value

As described above.

## Exceptions

Any exception thrown on construction of the elements in the destination range.
2.

## Notes

An implementation may improve the efficiency of `ranges::uninitialized_copy_n` (by using e.g. ) if the value type of the output range is *TrivialType*.

## Possible implementation

eq fun|1=
struct uninitialized_copy_n_fn
{
template<std::input_iterator I,
/*nothrow-input-iterator*/ O, /*nothrow-sentinel-for*/<O> S>
requires std::constructible_from<std::iter_value_t<O>, std::iter_reference_t<I>>
constexpr ranges::uninitialized_copy_n_result<I, O>
operator()(I ifirst, std::iter_difference_t<I> count, O ofirst, S olast) const
{
auto iter = std::counted_iterator(std::move(ifirst), count);
auto ret = ranges::uninitialized_copy(iter, std::default_sentinel, ofirst, olast);
return {std::move(ret.in).base(), ret.out};
}
};
inline constexpr uninitialized_copy_n_fn uninitialized_copy_n{};

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <memory>
#include <string>

int main()
{
    const char* stars[]{"Procyon", "Spica", "Pollux", "Deneb", "Polaris"};

    constexpr int n{4};
    alignas(alignof(std::string)) char out[n * sizeof(std::string)];

    try
    {
        auto first{reinterpret_cast<std::string*>(out)};
        auto last{first + n};
        auto ret{std::ranges::uninitialized_copy_n(std::begin(stars), n, first, last)};

        std::cout << '{';
        for (auto it{first}; it != ret.out; ++it)
            std::cout << (it == first ? "" : ", ") << std::quoted(*it);
        std::cout << "};\n";

        std::ranges::destroy(first, last);
    }
    catch (...)
    {
        std::cout << "uninitialized_copy_n exception\n";
    }
}
```


**Output:**
```
{"Procyon", "Spica", "Pollux", "Deneb"};
```


## See also


| cpp/memory/ranges/dsc uninitialized_copy | (see dedicated page) |
| cpp/memory/dsc uninitialized_copy_n | (see dedicated page) |

