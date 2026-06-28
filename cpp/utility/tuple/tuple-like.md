---
title: tuple-like
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple/tuple-like
---


# ''tuple-like'', ''pair-like''


```cpp
dcla|since=c++23|num=1|expos=yes|anchor=no|1=
template< class T >
concept tuple-like = /* see below */;
dcla|since=c++23|num=2|expos=yes|anchor=no|1=
template< class T >
concept pair-like =
tuple-like<T> && std::tuple_size_v<std::remove_cvref_t<T>> == 2;
```

1. A type `T` models and satisfies the concept  if `std::remove_cvref_t<T>` is a specialization of
* `std::array`,
<sup>(since C++26)</sup> * `std::complex`,
* `std::pair`,
* `std::tuple`, or
* `std::ranges::subrange`.
2.  objects are  objects with exactly 2 elements.

## Notes

types implement the ''tuple protocol'', i.e., such types can be used with ,  and .
Elements of  types can be bound with structured binding.

## See also

and  are used in the following standard library components:


| cpp/utility/tuple/dsc constructor | (see dedicated page) |
| cpp/utility/tuple/dsc operator{{= | (see dedicated page) |
| cpp/utility/tuple/dsc operator cmp | (see dedicated page) |
| cpp/utility/tuple/dsc basic common reference | (see dedicated page) |
| cpp/utility/tuple/dsc common type | (see dedicated page) |
| cpp/utility/tuple/dsc tuple_cat | (see dedicated page) |
| cpp/utility/dsc apply | (see dedicated page) |
| cpp/utility/dsc make_from_tuple | (see dedicated page) |
| cpp/utility/pair/dsc constructor | (see dedicated page) |
| cpp/utility/pair/dsc operator{{= | (see dedicated page) |
| cpp/ranges/subrange/dsc operator PairLike | (see dedicated page) |
| cpp/ranges/dsc elements_view | (see dedicated page) |

