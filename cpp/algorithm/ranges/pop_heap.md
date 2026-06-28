---
title: std::ranges::pop_heap
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/pop_heap
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::random_access_iterator I, std::sentinel_for<I> S,
class Comp = ranges::less, class Proj = std::identity >
requires std::sortable<I, Comp, Proj>
constexpr I pop_heap( I first, S last, Comp comp = {}, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< ranges::random_access_range R,
class Comp = ranges::less, class Proj = std::identity >
requires std::sortable<ranges::iterator_t<R>, Comp, Proj>
constexpr ranges::borrowed_iterator_t<R>
pop_heap( R&& r, Comp comp = {}, Proj proj = {} );
```

Swaps the first element and the last element of the specified heap with respect to `comp` and `proj` and makes the subrange excluding the first position into a heap with respect to `comp` and `proj`. This has the effect of removing the first element from the specified heap.
1. The specified heap is [first, last).
2. The specified heap is `r`.

## Parameters


### Parameters

- `[3=to modify, sentinel=yes}})` - 
- `r` - the  of elements to modify
- `comp` - comparator to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

1. `last`
2. `ranges::end(r)`

## Complexity

At most } applications of `comp` and } applications of `proj`, where  is:
1. `ranges::distance(first, last)`
2. `ranges::distance(r)`

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <iterator>
#include <string_view>

template<class I = int*>
void print(std::string_view rem, I first = {}, I last = {},
           std::string_view term = "\n")
{
    for (std::cout << rem; first != last; ++first)
        std::cout << *first << ' ';
    std::cout << term;
}

int main()
{
    std::array v{3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
    print("initially, v: ", v.cbegin(), v.cend());

    std::ranges::make_heap(v);
    print("make_heap, v: ", v.cbegin(), v.cend());

    print("convert heap into sorted array:");
    for (auto n {std::ssize(v)}; n >= 0; --n)
    {
        std::ranges::pop_heap(v.begin(), v.begin() + n);
        print("[ ", v.cbegin(), v.cbegin() + n, "]  ");
        print("[ ", v.cbegin() + n, v.cend(), "]\n");
    }
}
```


**Output:**
```
initially, v: 3 1 4 1 5 9 2 6 5 3
make_heap, v: 9 6 4 5 5 3 2 1 1 3
convert heap into sorted array:
[ 6 5 4 3 5 3 2 1 1 9 ]  [ ]
[ 5 5 4 3 1 3 2 1 6 ]  [ 9 ]
[ 5 3 4 1 1 3 2 5 ]  [ 6 9 ]
[ 4 3 3 1 1 2 5 ]  [ 5 6 9 ]
[ 3 2 3 1 1 4 ]  [ 5 5 6 9 ]
[ 3 2 1 1 3 ]  [ 4 5 5 6 9 ]
[ 2 1 1 3 ]  [ 3 4 5 5 6 9 ]
[ 1 1 2 ]  [ 3 3 4 5 5 6 9 ]
[ 1 1 ]  [ 2 3 3 4 5 5 6 9 ]
[ 1 ]  [ 1 2 3 3 4 5 5 6 9 ]
[ ]  [ 1 1 2 3 3 4 5 5 6 9 ]
```


## See also


| cpp/algorithm/ranges/dsc push_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc is_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc is_heap_until | (see dedicated page) |
| cpp/algorithm/ranges/dsc make_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc sort_heap | (see dedicated page) |
| cpp/algorithm/dsc pop_heap | (see dedicated page) |

