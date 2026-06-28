---
title: std::rank
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/rank
---

ddcl|header=type_traits|since=c++11|
template< class T >
struct rank;
If `T` is an array type, provides the member constant `value` equal to the number of dimensions of the array. For any other type, `value` is `0`.

## Helper variable template

ddcl|since=c++17|1=
template< class T >
constexpr std::size_t rank_v = rank<T>::value;

## Possible implementation

eq fun
|1=
template<class T>
struct rank : public std::integral_constant<std::size_t, 0> {};
template<class T>
struct rank<T[]> : public std::integral_constant<std::size_t, rank<T>::value + 1> {};
template<class T, std::size_t N>
struct rank<T[N]> : public std::integral_constant<std::size_t, rank<T>::value + 1> {};

## Example


### Example

```cpp
#include <type_traits>

static_assert(std::rank<int>{} == 0);
static_assert(std::rank<int[5]>{} == 1);
static_assert(std::rank<int[5][5]>{} == 2);
static_assert(std::rank<int[][5][5]>{} == 3);

int main()
{
    [[maybe_unused]] int ary[][3] = {<!---->{1, 2, 3}<!---->};

    // The rank of reference type, e.g., ary[0], that is int(&)[3], is 0:
    static_assert(std::rank_v<decltype(ary[0])> == 0);
    static_assert(std::is_same_v<decltype(ary[0]), int(&)[3]>);

    // The solution is to remove the reference type.
    static_assert(std::rank_v<std::remove_cvref_t<decltype(ary[0])>> == 1);
}
```


## See also


| cpp/types/dsc is_array | (see dedicated page) |
| cpp/types/dsc extent | (see dedicated page) |
| cpp/types/dsc remove_extent | (see dedicated page) |
| cpp/types/dsc remove_all_extents | (see dedicated page) |

