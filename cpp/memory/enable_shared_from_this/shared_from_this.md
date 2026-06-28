---
title: std::enable_shared_from_this::shared_from_this
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/enable_shared_from_this/shared_from_this
---


```cpp
dcla|num=1|since=c++11|constexpr=c++26|
std::shared_ptr<T> shared_from_this();
dcla|num=2|since=c++11|constexpr=c++26|
std::shared_ptr<const T> shared_from_this() const;
```

Returns a `std::shared_ptr` that shares ownership of `*this` with all existing `std::shared_ptr` that refer to `*this`.

## Return value


## Exceptions

If `shared_from_this` is called on an object that is not previously shared by `std::shared_ptr`, `std::bad_weak_ptr` is thrown by the `std::shared_ptr` constructor.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

struct Foo : public std::enable_shared_from_this<Foo>
{
    Foo() { std::cout << "Foo::Foo\n"; }
    ~Foo() { std::cout << "Foo::~Foo\n"; } 
    std::shared_ptr<Foo> getFoo() { return shared_from_this(); }
};

int main()
{
    Foo *f = new Foo;
    std::shared_ptr<Foo> pf1;

    {
        std::shared_ptr<Foo> pf2(f);
        pf1 = pf2->getFoo(); // shares ownership of object with pf2
    }

    std::cout << "pf2 is gone\n";   
}
```


**Output:**
```
Foo::Foo
pf2 is gone
Foo::~Foo
```


## See also


| cpp/memory/dsc shared_ptr | (see dedicated page) |

