---
title: std::enable_shared_from_this::enable_shared_from_this
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/enable_shared_from_this/enable_shared_from_this
---


```cpp
dcl|num=1|since=c++11|
constexpr enable_shared_from_this() noexcept;
dcla|num=2|since=c++11|constexpr=c++26|
enable_shared_from_this( const enable_shared_from_this& other ) noexcept;
```

Constructs a new `enable_shared_from_this` object.  is value-initialized.

## Parameters


### Parameters

- `other` - an `enable_shared_from_this` to copy

## Notes

There is no move constructor: moving from an object derived from `enable_shared_from_this` does not transfer its shared identity.

## Example


### Example

```cpp
#include <memory>

struct Foo : public std::enable_shared_from_this<Foo>
{
    Foo() {} // implicitly calls enable_shared_from_this constructor
    std::shared_ptr<Foo> getFoo() { return shared_from_this(); }
};

int main()
{
    std::shared_ptr<Foo> pf1(new Foo);
    auto pf2 = pf1->getFoo(); // shares ownership of object with pf1
}
```


## See also


| cpp/memory/dsc shared_ptr | (see dedicated page) |

