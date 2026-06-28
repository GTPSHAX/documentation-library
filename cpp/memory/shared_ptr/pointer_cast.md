---
title: std::static_pointer_cast
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/shared_ptr/pointer_cast
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++11|constexpr=c++26|1=
template< class T, class U >
std::shared_ptr<T> static_pointer_cast( const std::shared_ptr<U>& r ) noexcept;
dcla|num=2|since=c++20|constexpr=c++26|1=
template< class T, class U >
std::shared_ptr<T> static_pointer_cast( std::shared_ptr<U>&& r ) noexcept;
dcla|num=3|since=c++11|constexpr=c++26|1=
template< class T, class U >
std::shared_ptr<T>
dynamic_pointer_cast( const std::shared_ptr<U>& r ) noexcept;
dcla|num=4|since=c++20|constexpr=c++26|1=
template< class T, class U >
std::shared_ptr<T> dynamic_pointer_cast( std::shared_ptr<U>&& r ) noexcept;
dcla|num=5|since=c++11|constexpr=c++26|1=
template< class T, class U >
std::shared_ptr<T> const_pointer_cast( const std::shared_ptr<U>& r ) noexcept;
dcla|num=6|since=c++20|constexpr=c++26|1=
template< class T, class U >
std::shared_ptr<T> const_pointer_cast( std::shared_ptr<U>&& r ) noexcept;
dcla|num=7|since=c++17|1=
template< class T, class U >
std::shared_ptr<T>
reinterpret_pointer_cast( const std::shared_ptr<U>& r ) noexcept;
dcl|num=8|since=c++20|1=
template< class T, class U >
std::shared_ptr<T> reinterpret_pointer_cast( std::shared_ptr<U>&& r ) noexcept;
```

Creates a new `std::shared_ptr` object whose stored pointer is obtained from `r`'s stored pointer using a cast expression.
* If `r` is empty, so is the new `shared_ptr` (but its stored pointer is not necessarily null).
* Otherwise, the new `shared_ptr` will share ownership with the initial value of `r`, except that it is empty if the `dynamic_cast` performed by `dynamic_pointer_cast` returns a null pointer.
@3,4@ Let `expr` be the expression `dynamic_cast<typename shared_ptr<T>::element_type*>(r.get())`:
* .
* .
:
@1,2@ `static_cast<T*>((U*)nullptr)`
@3,4@ `dynamic_cast<T*>((U*)nullptr)`
@5,6@ `const_cast<T*>((U*)nullptr)`
@7,8@ `reinterpret_cast<T*>((U*)nullptr)`

## Parameters


### Parameters

- `r` - the pointer to convert

## Return value

Let `Y` be `typename std::shared_ptr<T>::element_type`:
1. `shared_ptr<T>(r, static_cast<Y*>(r.get()))`
2. `shared_ptr<T>(std::move(r), static_cast<Y*>(r.get()))`
@3,4@ Let `p` be `dynamic_cast<Y*>(r.get())`:
:@3@ `p ? shared_ptr<T>(r, p) : shared_ptr<T>()`
:@4@ `p ? shared_ptr<T>(std::move(r), p) : shared_ptr<T>()`
5. `shared_ptr<T>(r, const_cast<Y*>(r.get()))`
6. `shared_ptr<T>(std::move(r), const_cast<Y*>(r.get()))`
7. `shared_ptr<T>(r, reinterpret_cast<Y*>(r.get()))`
8. `shared_ptr<T>(std::move(r), reinterpret_cast<Y*>(r.get()))`

## Notes

The expression `std::shared_ptr<T>(/* ***_cast */<T*>(r.get()))` might seem to have the same effect, but it will likely result in undefined behavior, attempting to delete the same object twice.
rrev|since=c++20|
After calling the rvalue overloads , `r` is empty and `r.get() , except that `r` is not modified for `dynamic_pointer_cast`  if the `dynamic_cast` fails.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

class Base
{
public:
    int a;
    virtual void f() const { std::cout << "I am base!\n"; }
    virtual ~Base() {}
};

class Derived : public Base
{
public:
    void f() const override { std::cout << "I am derived!\n"; }
    ~Derived() {}
};

int main()
{
    auto basePtr = std::make_shared<Base>();
    std::cout << "Base pointer says: ";
    basePtr->f();

    auto derivedPtr = std::make_shared<Derived>();
    std::cout << "Derived pointer says: ";
    derivedPtr->f();

    // static_pointer_cast to go up class hierarchy
    basePtr = std::static_pointer_cast<Base>(derivedPtr);
    std::cout << "Base pointer to derived says: ";
    basePtr->f();

    // dynamic_pointer_cast to go down/across class hierarchy
    auto downcastedPtr = std::dynamic_pointer_cast<Derived>(basePtr);
    if (downcastedPtr)
    {
        std::cout << "Downcasted pointer says: ";
        downcastedPtr->f();
    }

    // All pointers to derived share ownership
    std::cout << "Pointers to underlying derived: "
              << derivedPtr.use_count()
              << '\n';
}
```


**Output:**
```
Base pointer says: I am base!
Derived pointer says: I am derived!
Base pointer to derived says: I am derived!
Downcasted pointer says: I am derived!
Pointers to underlying derived: 3
```


## See also


| cpp/memory/shared_ptr/dsc constructor | (see dedicated page) |

