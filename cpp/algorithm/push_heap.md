---
title: std::push_heap
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/push_heap
---


```cpp
**Header:** `<`algorithm`>`
|
template< class RandomIt >
void push_heap( RandomIt first, RandomIt last );
|
template< class RandomIt, class Compare >
void push_heap( RandomIt first, RandomIt last, Compare comp );
```

Inserts the element at the position `last - 1` into the `heap` [first, last - 1). The heap after the insertion will be [first, last).
1. The heap is with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
2. The heap is with respect to `comp`.
If any of the following conditions is satisfied, the behavior is undefined:
* [first, last - 1) is not a heap with respect to the corresponding comparator.
rev|until=c++11|
* The type of `*first` is not *Swappable*.
rev|since=c++11|
* `RandomIt` is not *ValueSwappable*.
* The type of `*first` is not *MoveConstructible*.
* The type of `*first` is not *MoveAssignable*.

## Parameters


### Parameters


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
#include <vector>

void println(std::string_view rem, const std::vector<int>& v)
{
    std::cout << rem;
    for (int e : v)
        std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    std::vector<int> v{3, 1, 4, 1, 5, 9};

    std::make_heap(v.begin(), v.end());
    println("after make_heap: ", v);

    v.push_back(6);
    println("after push_back: ", v);

    std::push_heap(v.begin(), v.end());
    println("after push_heap: ", v);
}
```


**Output:**
```
after make_heap: 9 5 4 1 1 3
after push_back: 9 5 4 1 1 3 6
after push_heap: 9 5 6 1 1 3 4
```


## Defect reports


## See also


| cpp/algorithm/dsc is_heap | (see dedicated page) |
| cpp/algorithm/dsc is_heap_until | (see dedicated page) |
| cpp/algorithm/dsc make_heap | (see dedicated page) |
| cpp/algorithm/dsc pop_heap | (see dedicated page) |
| cpp/algorithm/dsc sort_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc push_heap | (see dedicated page) |

