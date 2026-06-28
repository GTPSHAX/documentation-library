---
title: std::integer_sequence
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/utility/integer_sequence
---

ddcl|since=c++14|header=utility|feature=__cpp_lib_integer_sequence|1=
template< class T, T... Ints >
struct integer_sequence;
The class template `std::integer_sequence` represents a compile-time sequence of integers. When used as an argument to a , the  `Ints` can be deduced and used in pack expansion.

## Template parameters


### Parameters

- `T` - an integer type to use for the elements of the sequence
- `...Ints` - a non-type parameter pack representing the sequence

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions

member|size|2=
ddcl|1=
static constexpr std::size_t size() noexcept;
Returns the number of elements in `Ints`. Equivalent to `sizeof...(Ints)`.

## Return value

The number of elements in `Ints`.

## Helper templates

A helper alias template `std::index_sequence` is defined for the common case where `T` is `std::size_t`:
ddcl|1=
template< std::size_t... Ints >
using index_sequence = std::integer_sequence<std::size_t, Ints...>;
Helper alias templates `std::make_integer_sequence` and `std::make_index_sequence` are defined to simplify creation of `std::integer_sequence` and `std::index_sequence` types, respectively, with `0`, `1`, `2`, `...`, `N - 1` as `Ints`:

```cpp
dcl|1=
template< class T, T N >
using make_integer_sequence = std::integer_sequence<T, /* a sequence 0, 1, 2, ..., N-1 */>;
dcl|1=
template< std::size_t N >
using make_index_sequence = std::make_integer_sequence<std::size_t, N>;
```

The program is ill-formed if `N` is negative. If `N` is zero, the indicated type is `integer_sequence<T>`.
A helper alias template `std::index_sequence_for` is defined to convert any type parameter pack into an index sequence of the same length:
ddcl|1=
template< class... T >
using index_sequence_for = std::make_index_sequence<sizeof...(T)>;

## Notes


## Possible implementation

eq impl
|title1=make_integer_sequence|1=
namespace detail {
template<class T, T I, T N, T... integers>
struct make_integer_sequence_helper
{
using type = typename make_integer_sequence_helper<T, I + 1, N, integers..., I>::type;
};
template<class T, T N, T... integers>
struct make_integer_sequence_helper<T, N, N, integers...>
{
using type = std::integer_sequence<T, integers...>;
};
}
template<class T, T N>
using make_integer_sequence = typename detail::make_integer_sequence_helper<T, 0, N>::type;

## Example


### Example

```cpp
#include <array>
#include <cstddef>
#include <iostream>
#include <tuple>
#include <utility>

namespace details {
template <typename Array, std::size_t... I>
constexpr auto array_to_tuple_impl(const Array& a, std::index_sequence<I...>)
{
    return std::make_tuple(a[I]...);
}

template <class Ch, class Tr, class Tuple, std::size_t... Is>
void print_tuple_impl(std::basic_ostream<Ch, Tr>& os,
                      const Tuple& t,
                      std::index_sequence<Is...>)
{
    ((os << (Is ? ", " : "") << std::get<Is>(t)), ...);
}
}

template <typename T, T... ints>
void print_sequence(int id, std::integer_sequence<T, ints...> int_seq)
{
    std::cout << id << ") The sequence of size " << int_seq.size() << ": ";
    ((std::cout << ints << ' '), ...);
    std::cout << '\n';
}

template <typename T, std::size_t N, typename Indx = std::make_index_sequence<N>>
constexpr auto array_to_tuple(const std::array<T, N>& a)
{
    return details::array_to_tuple_impl(a, Indx{});
}

template <class Ch, class Tr, class... Args>
auto& operator<<(std::basic_ostream<Ch, Tr>& os, const std::tuple<Args...>& t)
{
    os << '(';
    details::print_tuple_impl(os, t, std::index_sequence_for<Args...>{});
    return os << ')';
}

int main()
{
    print_sequence(1, std::integer_sequence<unsigned, 9, 2, 5, 1, 9, 1, 6>{});
    print_sequence(2, std::make_integer_sequence<int, 12>{});
    print_sequence(3, std::make_index_sequence<10>{});
    print_sequence(4, std::index_sequence_for<std::ios, float, signed>{});

    constexpr std::array<int, 4> array{1, 2, 3, 4};

    auto tuple1 = array_to_tuple(array);
    static_assert(std::is_same_v<decltype(tuple1),
                                 std::tuple<int, int, int, int>>, "");
    std::cout << "5) tuple1: " << tuple1 << '\n';

    constexpr auto tuple2 = array_to_tuple<int, 4,
        std::integer_sequence<std::size_t, 1, 0, 3, 2>>(array);
    std::cout << "6) tuple2: " << tuple2 << '\n';
}
```


**Output:**
```
1) The sequence of size 7: 9 2 5 1 9 1 6 
2) The sequence of size 12: 0 1 2 3 4 5 6 7 8 9 10 11 
3) The sequence of size 10: 0 1 2 3 4 5 6 7 8 9 
4) The sequence of size 3: 0 1 2 
5) tuple1: (1, 2, 3, 4)
6) tuple2: (2, 1, 4, 3)
```


## See also


| cpp/container/array/dsc to_array | (see dedicated page) |
| cpp/types/dsc integral_constant | (see dedicated page) |

