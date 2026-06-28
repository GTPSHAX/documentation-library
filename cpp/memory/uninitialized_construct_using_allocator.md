---
title: std::uninitialized_construct_using_allocator
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/uninitialized_construct_using_allocator
---

ddcl|header=memory|since=c++20|
template< class T, class Alloc, class... Args >
constexpr T* uninitialized_construct_using_allocator( T* p,
const Alloc& alloc,
Args&&... args );
Creates an object of the given type `T` by means of `uses-allocator construction` at the uninitialized memory location indicated by `p`.
Equivalent to

```cpp
return std::apply(
    [&]<class... Xs>(Xs&&...xs)
    {
        return std::construct_at(p, std::forward<Xs>(xs)...);
    },
    std::uses_allocator_construction_args<T>(alloc, std::forward<Args>(args)...));
```


## Parameters


### Parameters

- `p` - the memory location where the object will be placed
- `alloc` - the allocator to use
- `args` - the arguments to pass to T's constructor

## Return value

Pointer to the newly-created object of type `T`.

## Exceptions

May throw any exception thrown by the constructor of `T`, typically including `std::bad_alloc`.

## Example

