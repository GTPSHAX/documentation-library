---
title: std::ranges::uninitialized_default_construct_n
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/ranges/uninitialized_default_construct_n
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++20|constexpr=c++26|
template< /*nothrow-forward-iterator*/ I >
requires std::default_initializable<std::iter_value_t<I>>
I uninitialized_default_construct_n( I first,
std::iter_difference_t<I> count );
dcl|num=2|since=c++26|
template< /*execution-policy*/ Ep, /*nothrow-random-access-iterator*/ I >
requires std::default_initializable<std::iter_value_t<I>>
I uninitialized_default_construct_n( Ep&& policy, I first,
std::iter_difference_t<I> count );
```

For the definition of `/*execution-policy*/`, see this page; for the definition of other exposition-only concepts, see this page.
1. Constructs elements in the destination range  by default-initialization as if by
box|
`return ranges::uninitialized_default_construct(std::counted_iterator(first, count),`<br />
`std::default_sentinel).base();`
@@ If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.
2. Same as , but executed according to `policy`.

## Parameters


### Parameters

- `first` - the beginning of the range of elements to initialize
- `count` - the number of elements to construct
- `policy` - execution policy

## Return value

As described above.

## Exceptions

Any exception thrown on construction of the elements in the destination range.
2.

## Notes

An implementation may skip the objects construction (without changing the observable effect) if no non-trivial default constructor is called while default-initializing a `std::iter_value_t<I>` object, which can be detected by `std::is_trivially_default_constructible`.

## Possible implementation

eq fun|1=
struct uninitialized_default_construct_n_fn
{
template</*nothrow-forward-iterator*/ I>
requires std::default_initializable<std::iter_value_t<I>>
constexpr I operator()(I first, std::iter_difference_t<I> count) const
{
auto iter = std::counted_iterator(first, count);
return ranges::uninitialized_default_construct(iter, std::default_sentinel).base();
}
};
inline constexpr uninitialized_default_construct_n_fn uninitialized_default_construct_n{};

## Example


### Example

```cpp
#include <cstring>
#include <iostream>
#include <memory>
#include <string>

int main()
{
    struct S { std::string m{"█▓▒░ █▓▒░ "}; };

    constexpr int n{4};
    alignas(alignof(S)) char out[n * sizeof(S)];

    try
    {
        auto first{reinterpret_cast<S*>(out)};
        auto last = std::ranges::uninitialized_default_construct_n(first, n);

        auto count{1};
        for (auto it{first}; it != last; ++it)
            std::cout << count++ << ' ' << it->m << '\n';

        std::ranges::destroy(first, last);
    }
    catch (...)
    {
        std::cout << "Exception!\n";
    }

    // For scalar types, uninitialized_default_construct_n
    // generally does not zero-fill the given uninitialized memory area.
    constexpr int sample[]{1, 2, 3, 4, 5, 6};
    int v[]{1, 2, 3, 4, 5, 6};
    std::ranges::uninitialized_default_construct_n(std::begin(v), std::size(v));
    if (std::memcmp(v, sample, sizeof(v)) == 0)
    {
        // Maybe undefined behavior, pending CWG 1997:
        // for (const int i : v) { std::cout << i << ' '; }
        for (const int i : sample)
            std::cout << i << ' ';
    }
    else
        std::cout << "Unspecified!";
    std::cout << '\n';
}
```


**Output:**
```
1 █▓▒░ █▓▒░
2 █▓▒░ █▓▒░
3 █▓▒░ █▓▒░
4 █▓▒░ █▓▒░
1 2 3 4 5 6
```


## See also


| cpp/memory/ranges/dsc uninitialized_default_construct | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_value_construct | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_value_construct_n | (see dedicated page) |
| cpp/memory/dsc uninitialized_default_construct_n | (see dedicated page) |

