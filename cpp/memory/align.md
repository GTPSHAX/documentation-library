---
title: std::align
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/align
---

ddcl|since=c++11|header=memory|
void* align( std::size_t alignment,
std::size_t size,
void*& ptr,
std::size_t& space );
Given a pointer `ptr` to a buffer of size `space`, returns a pointer aligned by the specified `alignment` for `size` number of bytes and decreases `space` argument by the number of bytes used for alignment. The first aligned address is returned.
The function modifies the pointer only if it would be possible to fit the wanted number of bytes aligned by the given alignment into the buffer. If the buffer is too small, the function does nothing and returns `nullptr`.
The behavior is undefined if `alignment` is not a power of two.

## Parameters


### Parameters

- `alignment` - the desired alignment
- `size` - the size of the storage to be aligned
- `ptr` - pointer to contiguous storage (a buffer) of at least `space` bytes
- `space` - the size of the buffer in which to operate

## Return value

The adjusted value of `ptr`, or null pointer value if the space provided is too small.

## Example


### Example

```cpp
#include <iostream>
#include <memory>
#include <new>

template<std::size_t N>
struct MyAllocator
{
    std::byte data[N];
    std::size_t sz{N};
    void* p{data};

    MyAllocator() = default;

    // Note: only well-defined for implicit-lifetime types
    template<typename T>
    T* implicit_aligned_alloc(std::size_t a = alignof(T))
    {
        if (std::align(a, sizeof(T), p, sz))
        {
            T* result = std::launder(reinterpret_cast<T*>(p));
            p = static_cast<std::byte*>(p) + sizeof(T);
            sz -= sizeof(T);
            return result;
        }
        return nullptr;
    }
};

int main()
{
    MyAllocator<64> a;
    std::cout << "allocated a.data at " << (void*)a.data
              << " (" << sizeof a.data << " bytes)\n";

    // Allocate a char
    if (char* p = a.implicit_aligned_alloc<char>())
    {
        *p = 'a';
        std::cout << "allocated a char at " << (void*)p << '\n';
    }

    // Allocate an int
    if (int* p = a.implicit_aligned_alloc<int>())
    {
        *p = 1;
        std::cout << "allocated an int at " << (void*)p << '\n';
    }

    // Allocate an int, aligned at a 32-byte boundary
    if (int* p = a.implicit_aligned_alloc<int>(32))
    {
        *p = 2;
        std::cout << "allocated an int at " << (void*)p << " (32-byte alignment)\n";
    }
}
```


**Output:**
```
allocated a.data at 0x7ffc654e8530 (64 bytes)
allocated a char at 0x7ffc654e8530
allocated an int at 0x7ffc654e8534
allocated an int at 0x7ffc654e8540 (32-byte alignment)
```


## Defect reports


## See also


| cpp/language/dsc alignof | (see dedicated page) |
| cpp/language/dsc alignas | (see dedicated page) |
| cpp/types/dsc aligned_storage | (see dedicated page) |
| cpp/memory/dsc assume_aligned | (see dedicated page) |

