---
title: std::pop_heap
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/pop_heap
---


```cpp
**Header:** `<`algorithm`>`
|
template< class RandomIt >
void pop_heap( RandomIt first, RandomIt last );
|
template< class RandomIt, class Compare >
void pop_heap( RandomIt first, RandomIt last, Compare comp );
```

Swaps the value in the position `first` and the value in the position `last - 1` and makes the subrange [first, last - 1) into a heap. This has the effect of removing the first element from the `heap` [first, last).
1. [first, last) is a heap with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
2. [first, last) is a heap with respect to `comp`.
If any of the following conditions is satisfied, the behavior is undefined:
* [first, last) is empty.
* [first, last) is not a heap with respect to the corresponding comparator.
rev|until=c++11|
* The type of `*first` is not *Swappable*.
rev|since=c++11|
* `RandomIt` is not *ValueSwappable*.
* The type of `*first` is not *MoveConstructible*.
* The type of `*first` is not *MoveAssignable*.

## Parameters


### Parameters

- `[3=to modify (extract root item), range=non-empty binary heap}})` - 

**Type requirements:**

- `RandomIt`
- `Compare`

## Complexity

Given  as `std::distance(first, last)`:
1. At most  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
2. At most  applications of the comparison function `comp`.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <string_view>
#include <type_traits>
#include <vector>

void println(std::string_view rem, const auto& v)
{
    std::cout << rem;
    if constexpr (std::is_scalar_v<std::decay_t<decltype(v)>>)
        std::cout << v;
    else
        for (int e : v)
            std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    std::vector<int> v{3, 1, 4, 1, 5, 9};

    std::make_heap(v.begin(), v.end());
    println("after make_heap: ", v);

    std::pop_heap(v.begin(), v.end()); // moves the largest to the end
    println("after pop_heap:  ", v);

    int largest = v.back();
    println("largest element: ", largest);

    v.pop_back(); // actually removes the largest element
    println("after pop_back:  ", v);
}
```


**Output:**
```
after make_heap: 9 5 4 1 1 3
after pop_heap:  5 3 4 1 1 9
largest element: 9
after pop_back:  5 3 4 1 1
```


## Defect reports


## See also


| cpp/algorithm/dsc push_heap | (see dedicated page) |
| cpp/algorithm/dsc is_heap | (see dedicated page) |
| cpp/algorithm/dsc is_heap_until | (see dedicated page) |
| cpp/algorithm/dsc make_heap | (see dedicated page) |
| cpp/algorithm/dsc sort_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc pop_heap | (see dedicated page) |

