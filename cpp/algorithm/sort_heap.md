---
title: std::sort_heap
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/sort_heap
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class RandomIt >
void sort_heap( RandomIt first, RandomIt last );
dcla|num=2|notes=<sup>(constexpr C++20)</sup>|
template< class RandomIt, class Compare >
void sort_heap( RandomIt first, RandomIt last, Compare comp );
```

Converts the `heap` [first, last) into a sorted range. The heap property is no longer maintained.
1. The heap is with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}, and will be sorted with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
2. The heap is with respect to `comp`, and will be sorted with respect to `comp`.
If any of the following conditions is satisfied, the behavior is undefined:
* [first, last) is not a heap.
rev|until=c++11|
* The type of `*first` is not *Swappable*.
rev|since=c++11|
* `RandomIt` is not *ValueSwappable*.
* The type of `*first` is not *MoveConstructible*.
* The type of `*first` is not *MoveAssignable*.

## Parameters


### Parameters

- `[3=to make the sorted range, range=binary heap}})` - 

**Type requirements:**

- `RandomIt`
- `Compare`

## Complexity

Given  as `std::distance(first, last)`:
1. At most  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
2. At most  applications of the comparison function `comp`.

## Possible implementation

eq impl
|title1=sort_heap (1)|ver1=1|1=
template<class RandomIt>
void sort_heap(RandomIt first, RandomIt last)
{
while (first != last)
std::pop_heap(first, last--);
}
|title2=sort_heap (2)|ver2=2|2=
template<class RandomIt, class Compare>
void sort_heap(RandomIt first, RandomIt last, Compare comp)
{
while (first != last)
std::pop_heap(first, last--, comp);
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <string_view>
#include <vector>

void println(std::string_view fmt, const auto& v)
{
    for (std::cout << fmt; const auto &i : v)
        std::cout << i << ' ';
    std::cout << '\n';
}

int main()
{
    std::vector<int> v{3, 1, 4, 1, 5, 9};

    std::make_heap(v.begin(), v.end());
    println("after make_heap, v: ", v);

    std::sort_heap(v.begin(), v.end());
    println("after sort_heap, v: ", v);
}
```


**Output:**
```
after make_heap, v: 9 4 5 1 1 3
after sort_heap, v: 1 1 3 4 5 9
```


## Defect reports


## See also


| cpp/algorithm/dsc is_heap | (see dedicated page) |
| cpp/algorithm/dsc is_heap_until | (see dedicated page) |
| cpp/algorithm/dsc make_heap | (see dedicated page) |
| cpp/algorithm/dsc pop_heap | (see dedicated page) |
| cpp/algorithm/dsc push_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc sort_heap | (see dedicated page) |

