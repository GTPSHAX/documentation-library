---
title: std::aligned_storage
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/aligned_storage
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|deprecated=c++23|1=
template< std::size_t Len, std::size_t Align = /* default-alignment */ >
struct aligned_storage;
```

Provides the nested type ''`type`'', which satisfies *TrivialType* and *StandardLayoutType* and suitable for use as uninitialized storage for any object whose size is at most `Len` and whose alignment requirement is a divisor of `Align`.
The default value of `Align` is the most stringent (the largest) alignment requirement for any object whose size is at most `Len`. If the default value is not used, `Align` must be the value of `alignof(T)` for some type `T`, or the behavior is undefined.
The behavior is undefined if `1=Len == 0`.
It is implementation-defined whether any extended alignment is supported.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types


```cpp
dcl|since=c++14|deprecated=c++23|1=
template< std::size_t Len, std::size_t Align = /* default-alignment */ >
using aligned_storage_t = typename aligned_storage<Len, Align>::type;
```


## Notes

The type defined by `std::aligned_storage<>::type` can be used to create uninitialized memory blocks suitable to hold the objects of given type, optionally aligned stricter than their natural alignment requirement, for example on a cache or page boundary.
As with any other uninitialized storage, the objects are created using placement new and destroyed with explicit destructor calls.

## Possible implementation

Except for default argument, aligned_storage is expressible in terms of alignas:
eq fun
|1=
template<std::size_t Len, std::size_t Align = /* default alignment not implemented */>
struct aligned_storage
{
struct type
{
alignas(Align) unsigned char data[Len];
};
};

## Example


### Example

```cpp
#include <cstddef>
#include <iostream>
#include <new>
#include <string>
#include <type_traits>

template<class T, std::size_t N>
class static_vector
{
    // Properly aligned uninitialized storage for N T's
    std::aligned_storage_t<sizeof(T), alignof(T)> data[N];
    std::size_t m_size = 0;

public:
    // Create an object in aligned storage
    template<typename ...Args> void emplace_back(Args&&... args)
    {
        if (m_size >= N) // Possible error handling
            throw std::bad_alloc{};

        // Construct value in memory of aligned storage using inplace operator new
        ::new(&data[m_size]) T(std::forward<Args>(args)...);
        ++m_size;
    }

    // Access an object in aligned storage
    const T& operator[](std::size_t pos) const
    {
        // Note: std::launder is needed after the change of object model in P0137R1
        return *std::launder(reinterpret_cast<const T*>(&data[pos]));
    }

    // Destroy objects from aligned storage
    ~static_vector()
    {
        for (std::size_t pos = 0; pos < m_size; ++pos)
            // Note: std::launder is needed after the change of object model in P0137R1
            std::destroy_at(std::launder(reinterpret_cast<T*>(&data[pos])));
    }
};

int main()
{
    static_vector<std::string, 10> v1;
    v1.emplace_back(5, '*');
    v1.emplace_back(10, '*');
    std::cout << v1[0] << '\n' << v1[1] << '\n';
}
```


**Output:**
```
*****
**********
```


## See also


| cpp/language/dsc alignas | (see dedicated page) |
| cpp/types/dsc alignment_of | (see dedicated page) |
| cpp/memory/c/dsc aligned_alloc | (see dedicated page) |
| cpp/types/dsc aligned_union | (see dedicated page) |
| cpp/types/dsc max_align_t | (see dedicated page) |
| cpp/utility/dsc launder | (see dedicated page) |

