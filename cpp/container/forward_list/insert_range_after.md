---
title: std::forward_list::insert_range_after
type: Containers
source: https://en.cppreference.com/w/cpp/container/forward_list/insert_range_after
---

ddcl|since=c++23|
template< container-compatible-range<T> R >
iterator insert_range_after( const_iterator pos, R&& rg );
Inserts, in non-reversing order, the copies of elements in `rg` before `pos`. Each iterator in the range `rg` is dereferenced exactly once.
`pos` must be any dereferenceable iterator in the range  or the  iterator (thus,  is not a valid argument for `pos`).
No iterators or references become invalidated.
The behavior is undefined if `rg` overlaps with the container.

## Parameters


### Parameters

- `pos` - an iterator after which the content will be inserted
- `rg` - a , that is, an  whose elements are convertible to `T`

**Type requirements:**


## Return value

An `iterator` that points at the copy of the last element inserted into `forward_list` or at `pos` if `rg` is empty.

## Complexity

Linear in size of `rg`.

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <forward_list>
#include <iterator>
#include <vector>

int main()
{
    auto container = std::forward_list{1, 2, 3, 4};
    auto pos = std::next(container.cbegin());
    assert(*pos == 2);
    const auto rg = std::vector{-1, -2, -3};

#ifdef __cpp_lib_containers_ranges
    container.insert_range_after(pos, rg);
#else
    container.insert_after(pos, rg.cbegin(), rg.cend());
#endif

    assert(std::ranges::equal(container, std::vector{1, 2, -1, -2, -3, 3, 4}));
}
```


## See also

