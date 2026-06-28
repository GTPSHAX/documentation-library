---
title: std::dextents
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/extents
---


```cpp
**Header:** `<`mdspan`>`
dcl|num=1|since=c++23|1=
template< class IndexType, std::size_t... Extents >
class extents;
dcl|num=2|since=c++23|1=
template< class IndexType, std::size_t Rank >
using dextents = /* see below */
dcl|num=3|since=c++26|1=
template< std::size_t Rank, class IndexType = std::size_t >
using dims = std::dextents<IndexType, Rank>;
```

1. Represents a multidimensional index space of rank equal to `sizeof...(Extents)`.
2. A convenient alias template for an all-dynamic `extents`. Let `d` denote `std::dynamic_extent`, each specialization of it `dextents<IndexType, Rank>` is equivalent to `extents<IndexType /*, d, d, ..., d*/>` (i.e.  is repeated a total of `Rank` times).
3. A convenient alias template for an all-dynamic `extents` with  as the default index type.
Each specialization of `extents` models  and is *TriviallyCopyable*.

## Template parameters


### Parameters

- `IndexType` - the type of each non-dynamic `Extents`. Shall be a signed or unsigned integer type. Otherwise, the program is ill-formed
- `Extents` - represents extent (size of an integer interval) for each rank index. Each element of it is either equal to  (in this case, it represents a ''dynamic extent'' and the extent size will be determined dynamically), or is representable as a value of type `IndexType` (then it represents a ''static extent'' and the extent size is just the value of it), or else the program is ill-formed
- `Rank` - denotes the rank of an all-dynamic `extents`

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member name** | Definition |


## Member functions


| cpp/container/mdspan/extents/dsc constructor | (see dedicated page) |

#### Observers

| cpp/container/mdspan/extents/dsc rank | (see dedicated page) |
| cpp/container/mdspan/extents/dsc rank_dynamic | (see dedicated page) |
| cpp/container/mdspan/extents/dsc static_extent | (see dedicated page) |
| cpp/container/mdspan/extents/dsc extent | (see dedicated page) |

#### Helpers

| cpp/container/mdspan/extents/dsc fwd-prod-of-extents | (see dedicated page) |
| cpp/container/mdspan/extents/dsc rev-prod-of-extents | (see dedicated page) |
| cpp/container/mdspan/extents/dsc index-cast | (see dedicated page) |
| cpp/container/mdspan/extents/dsc dynamic-index | (see dedicated page) |
| cpp/container/mdspan/extents/dsc dynamic-index-inv | (see dedicated page) |


## Non-member functions


| cpp/container/mdspan/extents/dsc operator{{== | (see dedicated page) |


## 


## Example

