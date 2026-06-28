---
title: std::allocator_traits::construct
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator_traits/construct
---


```cpp
**Header:** `<`memory`>`
dcla|since=c++11|constexpr=c++20|
template< class T, class... Args >
static void construct( Alloc& a, T* p, Args&&... args );
```

If possible, constructs an object of type `T` in allocated uninitialized storage pointed to by `p`, by calling
`a.construct(p, std::forward<Args>(args)...)`.
If the above is not possible (e.g. `Alloc` does not have the member function `construct()`), then calls
rrev multi
|until1=c++20|rev1=`::new (static_cast<void*>(p)) T(std::forward<Args>(args)...)`
|rev2=`std::construct_at(p, std::forward<Args>(args)...)`

## Parameters


### Parameters

- `a` - allocator to use for construction
- `p` - pointer to the uninitialized storage on which a `T` object will be constructed
- `args...` - the constructor arguments to pass to `a.construct()` or to <sup>(until C++20)</sup> placement-new<sup>(since C++20)</sup> `std::construct_at()`

## Notes

This function is used by the standard library containers when inserting, copying, or moving elements.
rrev|since=c++11|1=
Because this function provides the automatic fall back to , the member function `construct()` is an optional *Allocator* requirement.

## Example


### Example

```cpp
#include <memory>

struct foo
{
    virtual int bar() { return 0; }
    virtual ~foo() {}
};

int main()
{
    std::allocator<foo> al;
    using traits = std::allocator_traits<decltype(al)>;
    foo* p = traits::allocate(al, 1);
    traits::construct(al, p);
<!--Confirmation required:
    // Undefined behavior, object pointed to by p is still formally of uninitialized
    // type. This may result in faulty devirtualization during optimization.
    // p->bar();

    // Necessary devirtualization barrier after calling constructor.
    p = std::launder(p);
-->
    p->bar();
<!--
    // Need for devirtualization barrier also applies to destructor.
-->
    traits::destroy(al, p);
    traits::deallocate(al, p, 1);
}
```


## See also


| cpp/memory/new/dsc operator_new | (see dedicated page) |
| cpp/memory/allocator/dsc construct | (see dedicated page) |
| cpp/memory/dsc construct_at | (see dedicated page) |

