---
title: std::ranges::borrowed_subrange_t
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/borrowed_iterator_t
---


```cpp
**Header:** `<`ranges`>`
dcla|num = 1|since = c++20|1 =
template< ranges::range R >
using borrowed_iterator_t = /* see below */;
dcla|num = 2|since = c++20|1 =
template< ranges::range R >
using borrowed_subrange_t = /* see below */;
```

1. `std::ranges::iterator_t<R>` if `R` models , `std::ranges::dangling` otherwise.
2. `std::ranges::subrange<std::ranges::iterator_t<R>>` if `R` models , `std::ranges::dangling` otherwise.
These two alias templates are used by some constrained algorithms to avoid returning potentially dangling iterators or views.

## Possible implementation

eq impl
|title1=borrowed_iterator_t|ver1=1|1=
template< std::ranges::range R >
using borrowed_iterator_t = std::conditional_t<std::ranges::borrowed_range<R>,
std::ranges::iterator_t<R>, std::ranges::dangling>;
|title2=borrowed_subrange_t|ver2=2|2=
template< std::ranges::range R >
using borrowed_subrange_t = std::conditional_t<std::ranges::borrowed_range<R>,
std::ranges::subrange<std::ranges::iterator_t<R>>, std::ranges::dangling>;

## See also


| cpp/ranges/dsc dangling | (see dedicated page) |

