---
title: std::pair
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/pair
---

ddcl|header=utility|
template<
class T1,
class T2
> struct pair;
`std::pair` is a class template that provides a way to store two heterogeneous objects as a single unit. A pair is a specific case of a `std::tuple` with two elements.
If neither `T1` nor `T2` is a possibly cv-qualified class type with non-trivial destructor, or array thereof, the destructor of `pair` is trivial.

## Template parameters


### Parameters

- `T1, T2` - the types of the elements that the pair stores.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member objects


| Item | Description |
|------|-------------|
| **Member name** | Type |


## Member functions


| cpp/utility/pair/dsc constructor | (see dedicated page) |
| cpp/utility/pair/dsc operator{{= | (see dedicated page) |
| cpp/utility/pair/dsc swap | (see dedicated page) |


## Non-member functions


| cpp/utility/pair/dsc make_pair | (see dedicated page) |
| cpp/utility/pair/dsc operator_cmp | (see dedicated page) |
| cpp/utility/pair/dsc swap2 | (see dedicated page) |
| cpp/utility/pair/dsc get | (see dedicated page) |


## Helper classes


| cpp/utility/pair/dsc tuple_size | (see dedicated page) |
| cpp/utility/pair/dsc tuple_element | (see dedicated page) |
| cpp/utility/pair/dsc basic_common_reference | (see dedicated page) |
| cpp/utility/pair/dsc common_type | (see dedicated page) |
| cpp/utility/format/dsc tuple_formatter|pair | (see dedicated page) |


## Helper specializations

ddcl|since=c++23|1=
template< class T, class U >
constexpr bool enable_nonlocking_formatter_optimization<std::pair<T, U>> =
enable_nonlocking_formatter_optimization<T> &&
enable_nonlocking_formatter_optimization<U>;
This specialization of  enables efficient implementation of  and  for printing a `pair` object when both `T` and `U` enable it.

## <sup>(C++17)</sup>


## Defect reports


## See also


| cpp/utility/dsc tuple | (see dedicated page) |
| cpp/utility/tuple/dsc tie | (see dedicated page) |

