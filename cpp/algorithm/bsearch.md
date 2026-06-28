---
title: std::bsearch
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/bsearch
---


```cpp
**Header:** `<`cstdlib`>`
dcl|num=1|
void* bsearch( const void* key, const void* ptr, std::size_t count,
std::size_t size, /* c-compare-pred */* comp );
dcl|num=2|
void* bsearch( const void* key, const void* ptr, std::size_t count,
std::size_t size, /* compare-pred */* comp );
dcl|num=3|since=c++26|
void* bsearch( void* key, const void* ptr, std::size_t count,
std::size_t size, /* c-compare-pred */* comp );
dcl|num=4|since=c++26|
void* bsearch( void* key, const void* ptr, std::size_t count,
std::size_t size, /* compare-pred */* comp );
dcla|expos=yes|1=
extern "C" using /* c-compare-pred */ = int(const void*, const void*);
dcla|expos=yes|1=
extern "C++" using /* compare-pred */ = int(const void*, const void*);
```

Finds an element equal to element pointed to by `key` in an array pointed to by `ptr`. The array contains `count` elements of `size` bytes each and must be partitioned with respect to the object pointed to by `key`, that is, all the elements that compare less than must appear before all the elements that compare equal to, and those must appear before all the elements that compare greater than the key object. A fully sorted array satisfies these requirements. The elements are compared using function pointed to by `comp`.
.
If the array contains several elements that `comp` would indicate as equal to the element searched for, then it is unspecified which element the function will return as the result.

## Parameters


### Parameters

- `key` - pointer to the element to search for
- `ptr` - pointer to the array to examine
- `count` - number of element in the array
- `size` - size of each element in the array in bytes

## Return value

Pointer to the found element or null pointer if the element has not been found.

## Notes

Despite the name, neither C nor POSIX standards require this function to be implemented using binary search or make any complexity guarantees.
The two overloads provided by the C++ standard library are distinct because the types of the parameter `comp` are distinct ( is part of its type).

## Example


### Example

```cpp
#include <array>
#include <cstdlib>
#include <iostream>

template<typename T>
int compare(const void *a, const void *b)
{
    const auto &arg1 = *(static_cast<const T*>(a));
    const auto &arg2 = *(static_cast<const T*>(b));
    const auto cmp = arg1 <=> arg2;
    return cmp < 0 ? -1
        :  cmp > 0 ? +1
        :  0;
}

int main()
{
    std::array arr{1, 2, 3, 4, 5, 6, 7, 8};

    for (const int key : {4, 8, 9})
    {
        const int* p = static_cast<int*>(
            std::bsearch(&key,
                arr.data(),
                arr.size(),
                sizeof(decltype(arr)::value_type),
                compare<int>));

        std::cout << "value " << key;
        if (p)
            std::cout << " found at position " << (p - arr.data()) << '\n';
        else
            std::cout << " not found\n";
    }
}
```


**Output:**
```
value 4 found at position 3
value 8 found at position 7
value 9 not found
```


## See also


| cpp/algorithm/dsc qsort | (see dedicated page) |
| cpp/algorithm/dsc equal_range | (see dedicated page) |

