---
title: std::span::span
type: Containers
source: https://en.cppreference.com/w/cpp/container/span/span
---


```cpp
dcla|num=1|since=c++20|
constexpr span() noexcept;
dcla|num=2|since=c++20|1=
template< class It >
explicit(extent != std::dynamic_extent)
constexpr span( It first, size_type count );
dcla|num=3|since=c++20|1=
template< class It, class End >
explicit(extent != std::dynamic_extent)
constexpr span( It first, End last );
dcla|num=4|since=c++20|
template< std::size_t N >
constexpr span( std::type_identity_t<element_type> (&arr)[N] ) noexcept;
dcla|num=5|since=c++20|
template< class U, std::size_t N >
constexpr span( std::array<U, N>& arr ) noexcept;
dcla|num=6|since=c++20|
template< class U, std::size_t N >
constexpr span( const std::array<U, N>& arr ) noexcept;
dcla|num=7|since=c++20|1=
template< class R >
explicit(extent != std::dynamic_extent)
constexpr span( R&& r );
dcla|num=8|since=c++20|1=
template< class U, std::size_t N >
explicit(extent != std::dynamic_extent && N == std::dynamic_extent)
constexpr span( const std::span<U, N>& source ) noexcept;
dcla|num=9|since=c++20|1=
constexpr span( const span& other ) noexcept = default;
```

Constructs a `span`.

## Parameters


### Parameters

- `first` - iterator to the first element of the sequence
- `count` - number of elements in the sequence
- `last` - iterator past the last element of the sequence or another sentinel
- `arr` - array to construct a view for
- `r` - range to construct a view for
- `source` - another `span` to convert from
- `other` - another `span` to copy from

## Effects


| Overload |
| rlpf | data after construction |
| rlpf | size after construction |
| - |
| vl | 1 |
| c | nullptr |
| c | 0 |
| - |
| vl | 2 |
| rowspan=2 | c | std::to_address(first) |
| c | count |
| - |
| vl | 3 |
| c | last - first |
| - |
| vl | 4 |
| rowspan=3 | c | std::data(arr) |
| rowspan=3 | c | N |
| - |
| vl | 5 |
| - |
| vl | 6 |
| - |
| vl | 7 |
| c | ranges::data(r) |
| c | ranges::size(r) |
| - |
| vl | 8 |
| c | source.data() |
| c | source.size() |
| - |
| vl | 9 |
| c | other.data() |
| c | other.size() |


## Constraints and supplement information


### Size requirements

If `extent` is not `std::dynamic_extent` and the size of the source range is different from `extent`, the `span` object cannot be constructed.
:
1. `1=extent == std::dynamic_extent
@4-6@ `1=extent == std::dynamic_extent
9. `1=extent == std::dynamic_extent
2. `1=extent == std::dynamic_extent
3. `1=extent == std::dynamic_extent
7. `1=extent == std::dynamic_extent
8. `1=extent == std::dynamic_extent

### Conversion requirements

If `element_type` is different from the element type of the source range, and the latter cannot be converted to the former by , the `span` object cannot be constructed.
, where `U` is defined as follows:
@2,3@ `std::remove_reference_t<std::iter_reference_t<It>>`
@4-6@ `std::remove_pointer_t<decltype(std::data(arr))>`
7. `std::remove_reference_t<ranges::range_reference_t<R>>`
8. `U`

### Concept requirements

If any template argument does not model certain concept(s), the `span` object cannot be constructed.
. If it does not meet the semantic requirements of any corresponding concept, the behavior is undefined:


| Overload |
| Template<br>parameter |
| Concept |
| Remark |
| - |
| vl | 2 |
| tt | It |
| lconcept | contiguous_iterator |
|  |
| - |
| rowspan=2 | vl | 3 |
| tt | It |
| lconcept | contiguous_iterator |
|  |
| - |
| tt | End |
| lconcept | sized_sentinel_for | tt | sized_sentinel_for<It> |
|  |
| - |
| rowspan=3 | vl | 7 |
| rowspan=3 | tt | R |
| lconcept | contiguous_range |
|  |
| - |
| lconcept | sized_range |
|  |
| - |
| lconcept | borrowed_range |
| only required if c | std::is_const_v<element_type> is c | false |


### Other constraints

2. .
3. .
@@ .
7. :
* `std::remove_cvref_t<R>` is not a specialization of `std::span` or `std::array`.
* `std::is_array_v<std::remove_cvref_t<R>>` is `false`.

## Exceptions

2. Throws nothing.
3. Throws what and when `last - first` throws.
7. Throws what and when `std::ranges::size(r)` and `std::ranges::data(r)` throw.

## Example


### Example

```cpp
#include <array>
#include <iostream>
#include <span>
#include <vector>

void print_span(std::span<const int> s)
{
    for (int n : s)
        std::cout << n << ' ';
    std::cout << '\n';
}

int main()
{
    int c[]{1, 2, 3};
    print_span(c); // constructs from array

    std::array a{4, 5, 6};
    print_span(a); // constructs from std::array

    std::vector v{7, 8, 9};
    print_span(v); // constructs from std::vector

    // workaround for construction from a initializer list
    print_span({<!---->{0, 1, 2}<!---->}); // also constructs from array
}
```


**Output:**
```
1 2 3 
4 5 6
7 8 9
0 1 2
```


## See also


| cpp/container/dsc data|span | (see dedicated page) |
| cpp/container/dsc size|span | (see dedicated page) |
| cpp/container/span/dsc operator{{= | (see dedicated page) |
| cpp/iterator/dsc size | (see dedicated page) |
| cpp/iterator/dsc data | (see dedicated page) |

