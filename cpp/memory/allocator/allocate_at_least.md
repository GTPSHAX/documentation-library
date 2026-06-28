---
title: std::allocator::allocate_at_least
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator/allocate_at_least
---

ddcl|since=c++23|
constexpr std::allocation_result<T*, std::size_t>
allocate_at_least( std::size_t n );
Allocates `count * sizeof(T)` bytes of uninitialized storage, where `count` is an unspecified integer value not less than `n`, by calling `::operator new` (possibly with an additional `std::align_val_t` argument), but it is unspecified when and how this function is called.
Then, this function creates an array of type `T[count]` in the storage and starts its lifetime, but does not start lifetime of any of its elements.
In order to use this function in a constant expression, the allocated storage must be deallocated within the evaluation of the same expression.
Use of this function is ill-formed if `T` is an incomplete type.

## Parameters


### Parameters

- `n` - the lower bound of number of objects to allocate storage for

## Return value

}, where `p` points to the first element of an array of `count` objects of type `T` whose elements have not been constructed yet.

## Exceptions

Throws `std::bad_array_new_length` if `std::numeric_limits<std::size_t>::max() / sizeof(T) < n`, or `std::bad_alloc` if allocation fails.

## Notes

`allocate_at_least` is mainly provided for contiguous containers, e.g. `std::vector` and `std::basic_string`, in order to reduce reallocation by making their capacity match the actually allocated size when possible.
The "unspecified when and how" wording makes it possible to combine or optimize away heap allocations made by the standard library containers, even though such optimizations are disallowed for direct calls to `::operator new`. For example, this is implemented by libc++ ([https://github.com/llvm-mirror/libcxx/blob/master@%7B2017-02-09%7D/include/memory#L1766-L1772] and [https://github.com/llvm-mirror/libcxx/blob/master@%7B2017-02-09%7D/include/new#L211-L217]).
After calling  and before construction of elements, pointer arithmetic of `T*` is well-defined within the allocated array, but the behavior is undefined if elements are accessed.

## Example


### Example

```cpp
#include <memory>
#include <print>

int main()
{
    const std::size_t count{69};
    std::allocator<int> alloc;
    std::allocation_result res{alloc.allocate_at_least(count)};
    std::print("count: {}\n"
               "res.ptr: {}\n"
               "res.count: {}\n", count, res.ptr, res.count);

    /* construct, use, then destroy elements */

    alloc.deallocate(res.ptr, res.count);
}
```


**Output:**
```
count: 69
res.ptr: 0x555a486a0960
res.count: 96
```


## See also


| cpp/memory/dsc allocation_result | (see dedicated page) |
| cpp/memory/allocator_traits/dsc allocate_at_least | (see dedicated page) |

