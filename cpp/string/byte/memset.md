---
title: std::memset
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/memset
---


```cpp
**Header:** `<`cstring`>`
dcl|num=1|
void* memset( void* dest, int ch, std::size_t count );
dcl|num=2|since=c++26|
void* memset_explicit( void* dest, int ch, std::size_t count );
```

Copies the value `static_cast<unsigned char>(ch)` into each of the first `count` characters of the object pointed to by `dest`.
rrev|since=c++26|
Invoking `memset_explicit` always results in a memory store (i.e. never elided), regardless of optimizations.
:
* The object is a potentially-overlapping subobject.
* The object is not *TriviallyCopyable*.
* `count` is greater than the size of the object.

## Parameters


### Parameters

- `dest` - pointer to the object to fill
- `ch` - fill byte
- `count` - number of bytes to fill

## Return value

`dest`

## Notes

`std::memset` may be optimized away (under the as-if rules) if the object modified by this function is not accessed again for the rest of its lifetime (e.g., [https://gcc.gnu.org/bugzilla/show_bug.cgi?id=8537 gcc bug 8537]). For that reason, this function cannot be used to scrub memory (e.g., to fill an array that stored a password with zeroes).
This optimization is prohibited for `std::memset_explicit`: they are guaranteed to perform the memory write. Before C++26,  can be used with volatile pointers.
Third-party solutions for that include FreeBSD [https://www.freebsd.org/cgi/man.cgi?query=explicit_bzero `explicit_bzero`] or Microsoft [https://learn.microsoft.com/en-us/previous-versions/windows/desktop/legacy/aa366877 `SecureZeroMemory`].

## Example


### Example

```cpp
#include <bitset>
#include <climits>
#include <cstring>
#include <iostream>

int main()
{
    int a[4];
    using bits = std::bitset<sizeof(int) * CHAR_BIT>;
    std::memset(a, 0b1111'0000'0011, sizeof a);
    for (int ai : a)
        std::cout << bits(ai) << '\n';
}
```


**Output:**
```
00000011000000110000001100000011
00000011000000110000001100000011
00000011000000110000001100000011
00000011000000110000001100000011
```


## See also


| cpp/string/byte/dsc memcpy | (see dedicated page) |
| cpp/string/byte/dsc memmove | (see dedicated page) |
| cpp/string/wide/dsc wmemset | (see dedicated page) |
| cpp/algorithm/dsc fill | (see dedicated page) |
| cpp/algorithm/dsc fill_n | (see dedicated page) |
| cpp/types/dsc is_trivially_copyable | (see dedicated page) |

