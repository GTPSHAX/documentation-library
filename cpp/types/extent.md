---
title: std::extent
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/extent
---

ddcl|header=type_traits|since=c++11|1=
template< class T, unsigned N = 0 >
struct extent;
If `T` is an array type, provides the member constant `value` equal to the number of elements along the  dimension of the array, if `N` is in [0, std::rank<T>::value). For any other type, or if `T` is an array of unknown bound along its first dimension and `N` is `0`, `value` is `0`.

## Helper variable template

ddcl|since=c++17|1=
template< class T, unsigned N = 0 >
constexpr std::size_t extent_v = extent<T, N>::value;

## Possible implementation

eq fun
|1=
template<class T, unsigned N = 0>
struct extent : std::integral_constant<std::size_t, 0> {};
template<class T>
struct extent<T[], 0> : std::integral_constant<std::size_t, 0> {};
template<class T, unsigned N>
struct extent<T[], N> : std::extent<T, N - 1> {};
template<class T, std::size_t I>
struct extent<T[I], 0> : std::integral_constant<std::size_t, I> {};
template<class T, std::size_t I, unsigned N>
struct extent<T[I], N> : std::extent<T, N - 1> {};

## Example


### Example

```cpp
#include <type_traits>

static_assert(
    std::extent_v<int[3]> == 3 && // default dimension is 0
    std::extent_v<int[3], 0> == 3 && // the same as above
    std::extent_v<int[3][4], 0> == 3 &&
    std::extent_v<int[3][4], 1> == 4 &&
    std::extent_v<int[3][4], 2> == 0 &&
    std::extent_v<int[]> == 0
);

int main()
{
    const auto ext = std::extent<int['*']>{};
    static_assert(ext == 42); // with implicit conversion to std::size_t

    const int ints[]{1, 2, 3, 4};
    static_assert(std::extent_v<decltype(ints)> == 4); // array size

    [[maybe_unused]] int ary[][3] = {<!---->{1, 2, 3}<!---->};

    // ary[0] is of type reference to 'int[3]', so, the extent
    // cannot be calculated correctly and it returns 0
    static_assert(std::is_same_v<decltype(ary[0]), int(&)[3]>);
    static_assert(std::extent_v<decltype(ary[0])> == 0);

    // removing reference gives correct extent value 3
    static_assert(std::extent_v<std::remove_cvref_t<decltype(ary[0])>> == 3);
}
```


## See also


| cpp/types/dsc is_array | (see dedicated page) |
| cpp/types/dsc rank | (see dedicated page) |
| cpp/types/dsc remove_extent | (see dedicated page) |
| cpp/types/dsc remove_all_extents | (see dedicated page) |
| cpp/container/mdspan/dsc extents | (see dedicated page) |

