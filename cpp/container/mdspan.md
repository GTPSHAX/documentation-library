---
title: std::mdspan
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan
---

ddcl|header=mdspan|since=c++23|1=
template<
class T,
class Extents,
class LayoutPolicy = std::layout_right,
class AccessorPolicy = std::default_accessor<T>
> class mdspan;
`std::mdspan` is a multidimensional array view that maps a multidimensional index to an element of the array. The mapping and element access policies are configurable, and the underlying array need not be contiguous or even exist in memory at all.
Each specialization `MDS` of `mdspan` models  and satisfies:
:* `std::is_nothrow_move_constructible_v<MDS>` is `true`,
:* `std::is_nothrow_move_assignable_v<MDS>` is `true`, and
:* `std::is_nothrow_swappable_v<MDS>` is `true`.
A specialization of `mdspan` is a *TriviallyCopyable* type if its `accessor_type`, `mapping_type` and `data_handle_type` are *TriviallyCopyable* types.

## Template parameters


### Parameters

- `T` - element type; a complete object type that is neither an abstract class type nor an array type.
- `Extents` - specifies number of dimensions, their sizes, and which are known at compile time. Must be a specialization of `std::extents`.
- `LayoutPolicy` - specifies how to convert multidimensional index to underlying 1D index (column-major 3D array, symmetric triangular 2D matrix, etc). Must satisfy the requirements of *LayoutMappingPolicy*.
- `AccessorPolicy` - specifies how to convert underlying 1D index to a reference to T. Must satisfy the constraint that `std::is_same_v<T, typename AccessorPolicy​::​element_type>` is `true`. Must satisfy the requirements of *AccessorPolicy*.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/container/mdspan/dsc constructor | (see dedicated page) |
| cpp/container/mdspan/dsc operator{{= | (see dedicated page) |

#### Element access

| cpp/container/mdspan/dsc operator_at | (see dedicated page) |

#### Observers

| cpp/container/mdspan/dsc rank | (see dedicated page) |
| cpp/container/mdspan/dsc rank_dynamic | (see dedicated page) |
| cpp/container/mdspan/dsc static_extent | (see dedicated page) |
| cpp/container/mdspan/dsc extent | (see dedicated page) |
| cpp/container/mdspan/dsc size | (see dedicated page) |
| cpp/container/mdspan/dsc empty | (see dedicated page) |
| cpp/container/mdspan/dsc stride | (see dedicated page) |
| cpp/container/mdspan/dsc extents_mfun | (see dedicated page) |
| cpp/container/mdspan/dsc data_handle | (see dedicated page) |
| cpp/container/mdspan/dsc mapping | (see dedicated page) |
| cpp/container/mdspan/dsc accessor | (see dedicated page) |
| cpp/container/mdspan/dsc is_unique | (see dedicated page) |
| cpp/container/mdspan/dsc is_exhaustive | (see dedicated page) |
| cpp/container/mdspan/dsc is_strided | (see dedicated page) |
| cpp/container/mdspan/dsc is_always_unique | (see dedicated page) |
| cpp/container/mdspan/dsc is_always_exhaustive | (see dedicated page) |
| cpp/container/mdspan/dsc is_always_strided | (see dedicated page) |


## Non-member functions


| cpp/container/mdspan/dsc swap | (see dedicated page) |

#### Subviews

| cpp/container/mdspan/dsc submdspan | (see dedicated page) |
| cpp/container/mdspan/dsc submdspan_extents | (see dedicated page) |


## Helper types and templates


| cpp/container/mdspan/dsc extents | (see dedicated page) |
| cpp/container/mdspan/dsc dextents | (see dedicated page) |
| cpp/container/mdspan/dsc default_accessor | (see dedicated page) |
| cpp/container/mdspan/dsc aligned_accessor | (see dedicated page) |

#### Layout mapping policies

| cpp/container/mdspan/dsc layout_left | (see dedicated page) |
| cpp/container/mdspan/dsc layout_right | (see dedicated page) |
| cpp/container/mdspan/dsc layout_stride | (see dedicated page) |
| cpp/container/mdspan/dsc layout_left_padded | (see dedicated page) |
| cpp/container/mdspan/dsc layout_right_padded | (see dedicated page) |

#### Subviews helpers

| cpp/container/mdspan/dsc full_extent | (see dedicated page) |
| cpp/container/mdspan/dsc strided_slice | (see dedicated page) |
| cpp/container/mdspan/dsc submdspan_mapping_result | (see dedicated page) |


## 


## Notes


## Example


### Example

```cpp
#include <cstddef>
#include <mdspan>
#include <print>
#include <vector>

int main()
{
    std::vector v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};

    // View data as contiguous memory representing 2 rows of 6 ints each
    auto ms2 = std::mdspan(v.data(), 2, 6);
    // View the same data as a 3D array 2 x 3 x 2
    auto ms3 = std::mdspan(v.data(), 2, 3, 2);

    // Write data using 2D view
    for (std::size_t i = 0; i != ms2.extent(0); i++)
        for (std::size_t j = 0; j != ms2.extent(1); j++)
            ms2[i, j] = i * 1000 + j;

    // Read back using 3D view
    for (std::size_t i = 0; i != ms3.extent(0); i++)
    {
        std::println("slice @ i = {}", i);
        for (std::size_t j = 0; j != ms3.extent(1); j++)
        {
            for (std::size_t k = 0; k != ms3.extent(2); k++)
                std::print("{} ", ms3[i, j, k]);
            std::println("");
        }
    }
}
```


**Output:**
```
slice @ i = 0
0 1
2 3
4 5
slice @ i = 1
1000 1001
1002 1003
1004 1005
```


## See also


| cpp/container/dsc span | (see dedicated page) |
| cpp/numeric/dsc valarray | (see dedicated page) |

