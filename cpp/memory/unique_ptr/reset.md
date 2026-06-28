---
title: std::unique_ptr::reset
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/unique_ptr/reset
---


```cpp
dcla|num=1|constexpr=c++23|1=
void reset( pointer ptr = pointer() ) noexcept;
dcla|num=2|constexpr=c++23|1=
template< class U >
void reset( U ptr ) noexcept;
dcla|num=3|constexpr=c++23|1=
void reset( std::nullptr_t = nullptr ) noexcept;
```

Replaces the managed object.
@1,2@ Equivalent to c multi
|auto old_ptr  get();
|/* assigns “ptr” to the stored pointer */
|if (old_ptr)
|    get_deleter()(old_ptr);
.
@@ If `get_deleter()(old_ptr)` throws an exception, the behavior is undefined.
:@2@ :
* `pointer` is the same type as `element_type*`.
* `U` is a pointer type `V*` such that `V(*)[]` is convertible to `element_type(*)[]`.
3. Equivalent to `reset(pointer())`.

## Parameters


### Parameters

- `ptr` - pointer to a new object to manage

## Notes

To replace the managed object while supplying a new deleter as well, move assignment operator may be used.
A test for self-reset, i.e. whether `ptr` points to an object already managed by `*this`, is not performed, except where provided as a compiler extension or as a debugging assert. Note that code such as `p.reset(p.release())` does not involve self-reset, only code like `p.reset(p.get())` does.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

struct Foo // object to manage
{
    Foo() { std::cout << "Foo...\n"; }
    ~Foo() { std::cout << "~Foo...\n"; }
};

struct D // deleter
{
    void operator() (Foo* p)
    {
        std::cout << "Calling delete for Foo object... \n";
        delete p;
    }
};

int main()
{
    std::cout << "Creating new Foo...\n";
    std::unique_ptr<Foo, D> up(new Foo(), D()); // up owns the Foo pointer (deleter D)

    std::cout << "Replace owned Foo with a new Foo...\n";
    up.reset(new Foo());  // calls deleter for the old one

    std::cout << "Release and delete the owned Foo...\n";
    up.reset(nullptr);      
}
```


**Output:**
```
Creating new Foo...
Foo...
Replace owned Foo with a new Foo...
Foo...
Calling delete for Foo object...
~Foo...
Release and delete the owned Foo...
Calling delete for Foo object...
~Foo...
```


## Defect reports


## See also


| cpp/memory/unique_ptr/dsc release | (see dedicated page) |

