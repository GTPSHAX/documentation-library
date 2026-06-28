---
title: std::ranges::construct_at
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/ranges/construct_at
---


```cpp
**Header:** `<`memory`>`
dcl|since=c++20|
template< class T, class... Args >
constexpr T* construct_at( T* location, Args&&... args );
```

Creates a `T` object initialized with the arguments in `args` at given address `location`.
Equivalent to box|
`if constexpr (std::is_array_v<T>)`<br>
`return ::new (``(*location)) T[1]();`<br>
`else`<br>
`return ::new (``(*location)) T(std::forward<Args>(args)...);`
<sup>(until C++26)</sup> , except that `construct_at` may be used in evaluation of .
When `construct_at` is called in the evaluation of some constant expression `expr`, `location` must point to either a storage obtained by `std::allocator<T>::allocate` or an object whose lifetime began within the evaluation of `expr`.
:
* `std::is_unbounded_array_v<T>` is `false`.
* `::new(std::declval<void*>()) T(std::declval<Args>()...)` is well-formed when treated as an unevaluated operand.
If `std::is_array_v<T>` is `true` and `sizeof...(Args)` is nonzero, the program is ill-formed.

## Parameters


### Parameters

- `location` - pointer to the uninitialized storage on which a `T` object will be constructed
- `args...` - arguments used for initialization

## Return value

`location`

## Notes

`std::ranges::construct_at` behaves exactly same as `std::construct_at`, except that it is invisible to argument-dependent lookup.

## Example


### Example


**Output:**
```
S::S();
S { x=42; y=2.71828; z=3.1415; };
S::~S();
```


## Defect reports


## See also


| cpp/memory/ranges/dsc destroy_at | (see dedicated page) |
| cpp/memory/dsc construct_at | (see dedicated page) |

