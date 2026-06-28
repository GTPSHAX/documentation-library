---
title: std::memmove
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/memmove
---

ddcl|header=cstring|
void* memmove( void* dest, const void* src, std::size_t count );
Performs the following operations in order:
#Implicitly creates objects at `dest`.
# Copies `count` characters (as if of type `unsigned char`, the same below) from the object pointed to by `src` into a temporary array `arr` of `count` characters, where `arr` does not overlap the objects pointed to by `dest` and `src`.
# Copies `count` characters from `arr` into the object pointed to by `dest`.
If `dest` or `src` is a null pointer or invalid pointer, the behavior is undefined.

## Parameters


### Parameters

- `dest` - pointer to the memory location to copy to
- `src` - pointer to the memory location to copy from
- `count` - number of bytes to copy

## Return value

If there is a suitable created object, returns a pointer to it; otherwise returns `dest`.

## Notes

Despite the specification says a temporary buffer is used, actual implementations of this function do not incur the overhead of double copying or extra memory. For small `count`, it may load up and write out registers; for larger blocks, a common approach (glibc and bsd libc) is to copy bytes forwards from the beginning of the buffer if the destination starts before the source, and backwards from the end otherwise, with a fall back to `std::memcpy` when there is no overlap at all.
Where  prohibits examining the same memory as values of two different types, `std::memmove` may be used to convert the values.

## Example


### Example

```cpp
#include <cstring>
#include <iostream>

int main()
{
    char str[] = "1234567890";
    std::cout << str << '\n';
    std::memmove(str + 4, str + 3, 3); // copies from [4, 5, 6] to [5, 6, 7]
    std::cout << str << '\n';
}
```


**Output:**
```
1234567890
1234456890
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-4064 | C++98 | it was unclear whether the returned pointer points to a suitable created object | made clear |


## See also


| cpp/string/byte/dsc memcpy | (see dedicated page) |
| cpp/string/byte/dsc memset | (see dedicated page) |
| cpp/string/wide/dsc wmemmove | (see dedicated page) |
| cpp/algorithm/dsc copy | (see dedicated page) |
| cpp/algorithm/dsc copy_backward | (see dedicated page) |
| cpp/types/dsc is_trivially_copyable | (see dedicated page) |

