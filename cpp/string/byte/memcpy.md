---
title: std::memcpy
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/memcpy
---

ddcl|header=cstring|
void* memcpy( void* dest, const void* src, std::size_t count );
Performs the following operations in order:
#Implicitly creates objects at `dest`.
# Copies `count` characters (as if of type `unsigned char`) from the object pointed to by `src` into the object pointed to by `dest`.
If any of the following conditions is satisfied, the behavior is undefined:
* `dest` or `src` is a null pointer or invalid pointer.
* Copying takes place between objects that overlap.

## Parameters


### Parameters

- `dest` - pointer to the memory location to copy to
- `src` - pointer to the memory location to copy from
- `count` - number of bytes to copy

## Return value

If there is a suitable created object, returns a pointer to it; otherwise returns `dest`.

## Notes

`std::memcpy` is meant to be the fastest library routine for memory-to-memory copy. It is usually more efficient than `std::strcpy`, which must scan the data it copies or `std::memmove`, which must take precautions to handle overlapping inputs.
Several C++ compilers transform suitable memory-copying loops to `std::memcpy` calls.
Where  prohibits examining the same memory as values of two different types, `std::memcpy` may be used to convert the values.

## Example


### Example

```cpp
#include <cstdint>
#include <cstring>
#include <iostream>

int main()
{
    // simple usage
    char source[] = "once upon a daydream...", dest[4];
    std::memcpy(dest, source, sizeof dest);
    std::cout << "dest[4] = {";
    for (int n{}; char c : dest)
        std::cout << (n++ ? ", " : "") << '\'' << c << "'";
    std::cout << "};\n";

    // reinterpreting
    double d = 0.1;
//  std::int64_t n = *reinterpret_cast<std::int64_t*>(&d); // aliasing violation
    std::int64_t n;
    std::memcpy(&n, &d, sizeof d); // OK

    std::cout << std::hexfloat << d << " is " << std::hex << n
              << " as a std::int64_t\n" << std::dec;

    // object creation in destination buffer
    struct S
    {
        int x{42};
        void print() const { std::cout << '{' << x << "}\n"; }
    } s;
    alignas(S) char buf[sizeof(S)];
    S* ps = new (buf) S; // placement new
    std::memcpy(ps, &s, sizeof s);
    ps->print();
}
```


**Output:**
```
dest[4] = {'o', 'n', 'c', 'e'};
0x1.999999999999ap-4 is 3fb999999999999a as a std::int64_t
{42}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-4064 | C++98 | it was unclear whether the returned pointer points to a suitable created object | made clear |


## See also


| cpp/string/byte/dsc memmove | (see dedicated page) |
| cpp/string/byte/dsc memset | (see dedicated page) |
| cpp/string/wide/dsc wmemcpy | (see dedicated page) |
| cpp/string/basic_string/dsc copy | (see dedicated page) |
| cpp/algorithm/dsc copy | (see dedicated page) |
| cpp/algorithm/dsc copy_backward | (see dedicated page) |
| cpp/types/dsc is_trivially_copyable | (see dedicated page) |

