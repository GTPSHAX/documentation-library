---
title: std::span
type: Containers
source: https://en.cppreference.com/w/cpp/container/span
---

ddcl|header=span|since=c++20|1=
template<
class T,
std::size_t Extent = std::dynamic_extent
> class span;
The class template `span` describes an object that can refer to a contiguous sequence of objects with the first element of the sequence at position zero. A `span` can either have a ''static'' extent, in which case the number of elements in the sequence is known at compile-time and encoded in the type, or a ''dynamic'' extent.
For a `span` `s`, pointers, iterators, and references to elements of `s` are invalidated when an operation invalidates a pointer in the range [s.data(), s.data() + s.size()).
rrev|since=c++23|
Every specialization of `std::span` is a *TriviallyCopyable* type.

## Template parameters


### Parameters

- `T` - element type; must be a complete object type that is not an abstract class type
- `Extent` - the number of elements in the sequence, or `std::dynamic_extent` if dynamic

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |

All requirements on the iterator types of a *Container* apply to the `iterator` type of `span` as well.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/container/span/dsc constructor | (see dedicated page) |
| cpp/container/span/dsc operator{{= | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|span | (see dedicated page) |
| cpp/container/dsc end|span | (see dedicated page) |
| cpp/container/dsc rbegin|span | (see dedicated page) |
| cpp/container/dsc rend|span | (see dedicated page) |

#### Element access

| cpp/container/dsc front|span | (see dedicated page) |
| cpp/container/dsc back|span | (see dedicated page) |
| cpp/container/dsc at|span | (see dedicated page) |
| cpp/container/dsc operator_at|span | (see dedicated page) |
| cpp/container/dsc data|span | (see dedicated page) |

#### Observers

| cpp/container/dsc size|span | (see dedicated page) |
| cpp/container/span/dsc size_bytes | (see dedicated page) |
| cpp/container/span/dsc empty | (see dedicated page) |

#### Subviews

| cpp/container/span/dsc first | (see dedicated page) |
| cpp/container/span/dsc last | (see dedicated page) |
| cpp/container/span/dsc subspan | (see dedicated page) |


## Non-member functions


| cpp/container/span/dsc as_bytes | (see dedicated page) |


## Helper constant


| cpp/container/span/dsc dynamic_extent | (see dedicated page) |


## Helper templates

ddcl|since=c++20|1=
template< class T, std::size_t Extent >
constexpr bool ranges::enable_borrowed_range<std::span<T, Extent>> = true;
This specialization of `ranges::enable_borrowed_range` makes `span` satisfy .
ddcl|since=c++20|1=
template< class T, std::size_t Extent >
constexpr bool ranges::enable_view<std::span<T, Extent>> = true;
This specialization of `ranges::enable_view` makes `span` satisfy .

## 


## Notes

Specializations of `std::span` are already trivially copyable types in all existing implementations, even before the formal requirement introduced in C++23.

## Example


### Example

```cpp
#include <algorithm>
#include <cstddef>
#include <iostream>
#include <span>

template<class T, std::size_t N>
[[nodiscard]]
constexpr auto slide(std::span<T, N> s, std::size_t offset, std::size_t width)
{
    return s.subspan(offset, offset + width <= s.size() ? width : 0U);
}

template<class T, std::size_t N, std::size_t M>
constexpr bool starts_with(std::span<T, N> data, std::span<T, M> prefix)
{
    return data.size() >= prefix.size()
        && std::equal(prefix.begin(), prefix.end(), data.begin());
}

template<class T, std::size_t N, std::size_t M>
constexpr bool ends_with(std::span<T, N> data, std::span<T, M> suffix)
{
    return data.size() >= suffix.size()
        && std::equal(data.end() - suffix.size(), data.end(),
                      suffix.end() - suffix.size());
}

template<class T, std::size_t N, std::size_t M>
constexpr bool contains(std::span<T, N> span, std::span<T, M> sub)
{
    return std::ranges::search(span, sub).begin() != span.end();
}

void println(const auto& seq)
{
    for (const auto& elem : seq)
        std::cout << elem << ' ';
    std::cout << '\n';
}

int main()
{
    constexpr int a[]{0, 1, 2, 3, 4, 5, 6, 7, 8};
    constexpr int b[]{8, 7, 6};
    constexpr static std::size_t width{6};

    for (std::size_t offset{}; ; ++offset)
        if (auto s = slide(std::span{a}, offset, width); !s.empty())
            println(s);
        else
            break;

    static_assert(""
        && starts_with(std::span{a}, std::span{a, 4})
        && starts_with(std::span{a + 1, 4}, std::span{a + 1, 3})
        && !starts_with(std::span{a}, std::span{b})
        && !starts_with(std::span{a, 8}, std::span{a + 1, 3})
        && ends_with(std::span{a}, std::span{a + 6, 3})
        && !ends_with(std::span{a}, std::span{a + 6, 2})
        && contains(std::span{a}, std::span{a + 1, 4})
        && !contains(std::span{a, 8}, std::span{a, 9})
    );
}
```


**Output:**
```
0 1 2 3 4 5
1 2 3 4 5 6
2 3 4 5 6 7
3 4 5 6 7 8
```


## Defect reports


## See also


| cpp/container/dsc mdspan | (see dedicated page) |
| cpp/ranges/dsc subrange | (see dedicated page) |
| cpp/utility/dsc initializer_list | (see dedicated page) |
| cpp/string/dsc basic_string_view | (see dedicated page) |

