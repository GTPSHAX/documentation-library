---
title: std::weak_ptr::weak_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/weak_ptr/weak_ptr
---


```cpp
dcl|num=1|since=c++11|
constexpr weak_ptr() noexcept;
dcla|num=2|since=c++11|constexpr=c++26|
weak_ptr( const weak_ptr& r ) noexcept;
dcla|num=3|since=c++11|constexpr=c++26|
template< class Y >
weak_ptr( const weak_ptr<Y>& r ) noexcept;
dcla|num=4|since=c++11|constexpr=c++26|
template< class Y >
weak_ptr( const std::shared_ptr<Y>& r ) noexcept;
dcla|num=5|since=c++11|constexpr=c++26|
weak_ptr( weak_ptr&& r ) noexcept;
dcla|num=6|since=c++11|constexpr=c++26|
template< class Y >
weak_ptr( weak_ptr<Y>&& r ) noexcept;
```

Constructs new `weak_ptr` that potentially shares an object with `r`.
1. Default constructor. Constructs an empty `weak_ptr`.
@2-4@ Constructs a new `weak_ptr` which shares an object managed by `r`. If `r` manages no object, `*this` manages no object too.
:@3,4@ .
@5,6@ Move constructors. Moves a weak_ptr instance from `r` into `*this`. After this, `r` is empty and `1=r.use_count() == 0`.
:@6@ .

## Parameters


### Parameters

- `r` - a `std::shared_ptr` or `weak_ptr` that will be viewed by this `weak_ptr`

## Notes

Because the default constructor is `constexpr`, static `weak_ptr`s are initialized as part of static non-local initialization, before any dynamic non-local initialization begins. This makes it safe to use a `weak_ptr` in a constructor of any static object.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

struct Foo {};

int main()
{
    std::weak_ptr<Foo> w_ptr;

    {
        auto ptr = std::make_shared<Foo>();
        w_ptr = ptr;
        std::cout << "w_ptr.use_count() inside scope: " << w_ptr.use_count() << '\n';
    }

    std::cout << "w_ptr.use_count() out of scope: " << w_ptr.use_count() << '\n';
    std::cout << "w_ptr.expired() out of scope: "
              << std::boolalpha << w_ptr.expired() << '\n';
}
```


**Output:**
```
w_ptr.use_count() inside scope: 1
w_ptr.use_count() out of scope: 0
w_ptr.expired() out of scope: true
```


## Defect reports


## See also


| cpp/memory/weak_ptr/dsc operator{{= | (see dedicated page) |

