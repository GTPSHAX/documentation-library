---
title: std::scoped_allocator_adaptor::destroy
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/scoped_allocator_adaptor/destroy
---


```cpp
**Header:** `<`scoped_allocator`>`
dcl|since=c++11|
template< class T >
void destroy( T* p );
```

Uses the outer allocator to call the destructor of the object pointed to by `p`, by calling
`std::allocator_traits<OUTERMOST>::destroy(OUTERMOST(*this), p)`
where OUTERMOST is the type that would be returned by calling `this->outer_allocator()`, and then calling the `outer_allocator()` member function recursively on the result of this call until reaching the type that has no such member function.

## Parameters


### Parameters

- `p` - pointer to the object that is going to be destroyed

## Return value

(none)

## See also


| cpp/memory/allocator_traits/dsc destroy | (see dedicated page) |
| cpp/memory/allocator/dsc destroy | (see dedicated page) |

