---
title: std::realloc
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/c/realloc
---

ddcl|header=cstdlib|
void* realloc( void* ptr, std::size_t new_size );
Reallocates the given area of memory (implicitly creating objects in the destination area). It must be previously allocated by `std::malloc`, `std::calloc` or `std::realloc` and not yet freed with `std::free`, otherwise, the results are undefined.
The reallocation is done by either:
@a@ expanding or contracting the existing area pointed to by `ptr`, if possible. The contents of the area remain unchanged up to the lesser of the new and old sizes. If the area is expanded, the contents of the new part of the array are undefined.
@b@ allocating a new memory block of size `new_size` bytes, copying memory area with size equal the lesser of the new and the old sizes, and freeing the old block.
If there is not enough memory, the old memory block is not freed and null pointer is returned.
If `ptr` is a null pointer, the behavior is the same as calling `std::malloc(new_size)`.
rev|until=c++26|
If `ptr` is not null and `new_size` is zero, the behavior is implementation defined: null pointer may be returned (in which case the old memory block may or may not be freed) or some non-null pointer may be returned that may not be used to access storage. <sup>(since C++20)</sup> Such usage is deprecated (via
rev|since=c++26|
If `ptr` is not null and `new_size` is zero, the behavior is erroneous and the effects are implementation-defined.

## Parameters


### Parameters

- `ptr` - pointer to the memory area to be reallocated
- `new_size` - new size of the array

## Return value

On success, returns a pointer to the beginning of newly allocated memory. To avoid a memory leak, the returned pointer must be deallocated with `std::free` or `std::realloc`. The original pointer `ptr` is invalidated and any access to it is undefined behavior (even if reallocation was in-place).
On failure, returns a null pointer. The original pointer `ptr` remains valid and may need to be deallocated with `std::free`.

## Notes

Because reallocation may involve bytewise copying (regardless of whether it expands or contracts the area), it is necessary (but not sufficient) for those objects to be of *TriviallyCopyable* type.
Some non-standard libraries define a type trait "BitwiseMovable" or "Relocatable", which describes a type that does not have:
* external references (e.g. nodes of a list or a tree that holds reference to another element), and
* internal references (e.g. member pointer which might hold the address of another member).
Objects of such type can be accessed after their storage is reallocated even if their copy constructors are not trivial.

## Example


### Example

```cpp
#include <cassert>
#include <cstdlib>
#include <new>

class MallocDynamicBuffer
{
    char* p;
public:
    explicit MallocDynamicBuffer(std::size_t initial = 0) : p(nullptr)
    {
        resize(initial);
    }

    ~MallocDynamicBuffer() { std::free(p); }

    void resize(std::size_t newSize)
    {
        if (newSize == 0) // this check is not strictly needed,
        {
            std::free(p); // but zero-size realloc is deprecated in C
            p = nullptr;
        }
        else
        {
            if (void* mem = std::realloc(p, newSize))
                p = static_cast<char*>(mem);
            else
                throw std::bad_alloc();
        }
    }

    char& operator[](size_t n) { return p[n]; }
    char operator[](size_t n) const { return p[n]; }
};

int main()
{
    MallocDynamicBuffer buf1(1024);
    buf1[5] = 'f';
    buf1.resize(10); // shrink
    assert(buf1[5] == 'f');
    buf1.resize(1024); // grow
    assert(buf1[5] == 'f');
}
```


## See also

