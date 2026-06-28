---
title: std::make_heap
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/make_heap
---


```cpp
**Header:** `<`algorithm`>`
|
template< class RandomIt >
void make_heap( RandomIt first, RandomIt last );
|
template< class RandomIt, class Compare >
void make_heap( RandomIt first, RandomIt last, Compare comp );
```

Constructs a `heap` in the range [first, last).
1. The constructed heap is with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
2. The constructed heap is with respect to `comp`.
If any of the following conditions is satisfied, the behavior is undefined:
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
#include <functional>
#include <iostream>
#include <string_view>
#include <vector>

void print(std::string_view text, const std::vector<int>& v = {})
{
    std::cout << text << ": ";
    for (const auto& e : v)
        std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    print("Max heap");

    std::vector<int> v{3, 2, 4, 1, 5, 9};
    print("initially, v", v);

    std::make_heap(v.begin(), v.end());
    print("after make_heap, v", v);

    std::pop_heap(v.begin(), v.end());
    print("after pop_heap, v", v);

    auto top = v.back();
    v.pop_back();
    print("former top element", {top});
    print("after removing the former top element, v", v);

    print("\nMin heap");

    std::vector<int> v1{3, 2, 4, 1, 5, 9};
    print("initially, v1", v1);

    std::make_heap(v1.begin(), v1.end(), std::greater<>{});
    print("after make_heap, v1", v1);

    std::pop_heap(v1.begin(), v1.end(), std::greater<>{});
    print("after pop_heap, v1", v1);

    auto top1 = v1.back();
    v1.pop_back();
    print("former top element", {top1});
    print("after removing the former top element, v1", v1);
}
```


**Output:**
```
Max heap:
initially, v: 3 2 4 1 5 9
after make_heap, v: 9 5 4 1 2 3
after pop_heap, v: 5 3 4 1 2 9
former top element: 9
after removing the former top element, v: 5 3 4 1 2

Min heap:
initially, v1: 3 2 4 1 5 9
after make_heap, v1: 1 2 4 3 5 9
after pop_heap, v1: 2 3 4 9 5 1
former top element: 1
after removing the former top element, v1: 2 3 4 9 5
```


## Defect reports


## See also


| cpp/algorithm/dsc is_heap | (see dedicated page) |
| cpp/algorithm/dsc is_heap_until | (see dedicated page) |
| cpp/algorithm/dsc push_heap | (see dedicated page) |
| cpp/algorithm/dsc pop_heap | (see dedicated page) |
| cpp/algorithm/dsc sort_heap | (see dedicated page) |
| cpp/container/dsc priority_queue | (see dedicated page) |
| cpp/algorithm/ranges/dsc make_heap | (see dedicated page) |

