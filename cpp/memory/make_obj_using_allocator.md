---
title: std::make_obj_using_allocator
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/make_obj_using_allocator
---


```cpp
**Header:** `<`memory`>`
dcl|since=c++20|
template< class T, class Alloc, class... Args >
constexpr T make_obj_using_allocator( const Alloc& alloc, Args&&... args );
```

Creates an object of the given type `T` by means of `uses-allocator construction`.
Equivalent to

```cpp
return std::make_from_tuple<T>(
    std::uses_allocator_construction_args<T>(alloc, std::forward<Args>(args)...)
);
```


## Parameters


### Parameters

- `alloc` - the allocator to use
- `args` - the arguments to pass to T's constructor

## Return value

The newly-created object of type `T`.

## Exceptions

May throw any exception thrown by the constructor of `T`, typically including `std::bad_alloc`.

## Example

