---
title: std::qsort
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/qsort
---


```cpp
**Header:** `<`cstdlib`>`
dcl|num=1|
void qsort( void *ptr, std::size_t count,
std::size_t size, /* c-compare-pred */* comp );
void qsort( void *ptr, std::size_t count,
std::size_t size, /* compare-pred */* comp );
|1=
extern "C" using /* c-compare-pred */ = int(const void*, const void*);
extern "C++" using /* compare-pred */ = int(const void*, const void*);
```

Sorts the given array pointed to by `ptr` in ascending order. The array contains `count` elements of `size` bytes. Function pointed to by `comp` is used for object comparison.
If `comp` indicates two elements as equivalent, their order is unspecified.
If the type of the elements of the array is not a <sup>(until C++11)</sup> *PODType*<sup>(since C++11)</sup> *TriviallyCopyable type*, the behavior is undefined.

## Parameters


### Parameters

- `ptr` - pointer to the array to sort
- `count` - number of elements in the array
- `size` - size of each element in the array in bytes

## Return value

(none)

## Notes

Despite the name, C++, C, and POSIX standards do not require this function to be implemented using [Quicksort](https://en.wikipedia.org/wiki/Quicksort) or make any complexity or stability guarantees.
The two overloads provided by the C++ standard library are distinct because the types of the parameter `comp` are distinct ( is part of its type).

## Example


### Example

```cpp
#include <array>
#include <climits>
#include <compare>
#include <cstdlib>
#include <iostream>

int main()
{
    std::array a{-2, 99, 0, -743, INT_MAX, 2, INT_MIN, 4};

    std::qsort
    (
        a.data(),
        a.size(),
        sizeof(decltype(a)::value_type),
        [](const void* x, const void* y)
        {
            const int arg1 = *static_cast<const int*>(x);
            const int arg2 = *static_cast<const int*>(y);
            const auto cmp = arg1 <=> arg2;
            if (cmp < 0)
                return -1;
            if (cmp > 0)
                return 1;
            return 0;
        }
    );

    for (int ai : a)
        std::cout << ai << ' ';
    std::cout << '\n';
}
```


**Output:**
```
-2147483648 -743 -2 0 2 4 99 2147483647
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-405 | C++98 | the elements of the array could have any type | limited to named req |


## See also


| cpp/algorithm/dsc bsearch | (see dedicated page) |
| cpp/algorithm/dsc sort | (see dedicated page) |
| cpp/types/dsc is_trivial | (see dedicated page) |

