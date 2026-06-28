---
title: std::allocator::deallocate
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator/deallocate
---

ddcl|notes=<sup>(constexpr C++20)</sup>|
void deallocate( T* p, std::size_t n );
Deallocates the storage referenced by the pointer `p`, which must be a pointer obtained by an earlier call to `allocate()`<sup>(since C++23)</sup>  or `allocate_at_least()`.
The argument `n` must be equal to the first argument of the call to `allocate()` that originally produced `p`<sup>(since C++23)</sup> , or in the range closed range|m|count if `p` is obtained from a call to `allocate_at_least(m)` which returned }; otherwise, the behavior is undefined.
Calls `::operator delete(void*)` <sup>(since C++17)</sup> or `::operator delete(void*, std::align_val_t)`, but it is unspecified when and how it is called.
rrev|since=c++20|
In evaluation of a constant expression, this function must deallocate storage allocated within the evaluation of the same expression.

## Parameters


### Parameters

- `p` - pointer obtained from `allocate()`<sup>(since C++23)</sup>  or `allocate_at_least()`
- `n` - number of objects earlier passed to `allocate()`<sup>(since C++23)</sup> , or a number between requested and actually allocated number of objects via `allocate_at_least() (may be equal to either bound)`

## Return value

(none)

## Example


### Example


**Output:**
```
#1 S::S(42);
#2  S::S(43);
#3   S::S(44);
#4    S::S(45);
#1 S::id();
#2  S::id();
#3   S::id();
#4    S::id();
#1 S::~S();
#2  S::~S();
#3   S::~S();
#4    S::~S();
```


## See also


| cpp/memory/allocator/dsc allocate | (see dedicated page) |
| cpp/memory/allocator/dsc allocate_at_least | (see dedicated page) |
| cpp/memory/allocator_traits/dsc deallocate | (see dedicated page) |

