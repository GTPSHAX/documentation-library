---
title: std::shared_ptr::reset
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/shared_ptr/reset
---


```cpp
dcla|num=1|since=c++11|constexpr=c++26|
void reset() noexcept;
dcla|num=2|since=c++11|constexpr=c++26|
template< class Y >
void reset( Y* ptr );
dcla|num=3|since=c++11|constexpr=c++26|
template< class Y, class Deleter >
void reset( Y* ptr, Deleter d );
dcla|num=4|since=c++11|constexpr=c++26|
template< class Y, class Deleter, class Alloc >
void reset( Y* ptr, Deleter d, Alloc alloc );
```

Replaces the managed object with an object pointed to by `ptr`. Optional deleter `d` can be supplied, which is later used to destroy the new object when no `shared_ptr` objects own it.
If `*this` already owns an object and it is the last `shared_ptr` owning it, the object is destroyed through the owned deleter.
1. Releases the ownership of the managed object (if any). After the call, `*this` manages no object.
@@ Equivalent to `shared_ptr<T>().swap(*this);`.
@2-4@ Replaces the managed object with an object pointed to by `ptr`.
:@2@ Uses the `delete` expression as the deleter.
:@@ Equivalent to `shared_ptr<T>(ptr).swap(*this);`.
:@3@ Uses the specified deleter `d` as the deleter.
:@@ Equivalent to `shared_ptr<T>(ptr, d).swap(*this);`.
:@4@ Same as , but additionally uses a copy of `alloc` for allocation of data for internal use.
:@@ Equivalent to `shared_ptr<T>(ptr, d, alloc).swap(*this);`.

## Parameters


### Parameters

- `ptr` - pointer to an object to acquire ownership of
- `d` - deleter to store for deletion of the object
- `alloc` - allocator to use for internal allocations

## Notes

Proper `delete` expression corresponding to the supplied type is always selected, this is the reason why the function is implemented as template using a separate parameter `Y`.
In order for the internally invoked `shared_ptr` constructor to have well-defined behavior, the same conditions also need to be satisfied. For example, if the object pointed to by `ptr` is already owned by another `shared_ptr`, invoking the function generally results in undefined behavior.

## Exceptions

2. `std::bad_alloc` if required additional memory could not be obtained. May throw implementation-defined exception for other errors. `delete ptr` is evaluated if an exception occurs.
@3,4@ `std::bad_alloc` if required additional memory could not be obtained. May throw implementation-defined exception for other errors. `d(ptr)` is evaluated if an exception occurs.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

struct Foo
{
    Foo(int n = 0) noexcept : bar(n)
    {
        std::cout << "Foo::Foo(), bar = " << bar << " @ " << this << '\n';
    }
    ~Foo()
    {
        std::cout << "Foo::~Foo(), bar = " << bar << " @ " << this << '\n';
    }
    int getBar() const noexcept { return bar; }
private:
    int bar;
};

int main()
{
    std::cout << "1) unique ownership\n";
    {
        std::shared_ptr<Foo> sptr = std::make_shared<Foo>(100);

        std::cout << "Foo::bar = " << sptr->getBar() << ", use_count() = "
                  << sptr.use_count() << '\n';

        // Reset the shared_ptr without handing it a fresh instance of Foo.
        // The old instance will be destroyed after this call.
        std::cout << "call sptr.reset()...\n";
        sptr.reset(); // calls Foo's destructor here
        std::cout << "After reset(): use_count() = " << sptr.use_count()
                  << ", sptr = " << sptr << '\n';
    }   // No call to Foo's destructor, it was done earlier in reset().

    std::cout << "\n2) unique ownership\n";
    {
        std::shared_ptr<Foo> sptr = std::make_shared<Foo>(200);

        std::cout << "Foo::bar = " << sptr->getBar() << ", use_count() = "
                  << sptr.use_count() << '\n';

        // Reset the shared_ptr, hand it a fresh instance of Foo.
        // The old instance will be destroyed after this call.
        std::cout << "call sptr.reset()...\n";
        sptr.reset(new Foo{222});
        std::cout << "After reset(): use_count() = " << sptr.use_count()
                  << ", sptr = " << sptr << "\nLeaving the scope...\n";
    }   // Calls Foo's destructor.

    std::cout << "\n3) multiple ownership\n";
    {
        std::shared_ptr<Foo> sptr1 = std::make_shared<Foo>(300);
        std::shared_ptr<Foo> sptr2 = sptr1;
        std::shared_ptr<Foo> sptr3 = sptr2;

        std::cout << "Foo::bar = " << sptr1->getBar() << ", use_count() = "
                  << sptr1.use_count() << '\n';

        // Reset the shared_ptr sptr1, hand it a fresh instance of Foo.
        // The old instance will stay shared between sptr2 and sptr3.
        std::cout << "call sptr1.reset()...\n";
        sptr1.reset(new Foo{333});

        std::cout << "After reset():\n"
                  << "sptr1.use_count() = " << sptr1.use_count()
                  << ", sptr1 @ " << sptr1 << '\n'
                  << "sptr2.use_count() = " << sptr2.use_count()
                  << ", sptr2 @ " << sptr2 << '\n'
                  << "sptr3.use_count() = " << sptr3.use_count()
                  << ", sptr3 @ " << sptr3 << '\n'
                  << "Leaving the scope...\n";
    }   // Calls two destructors of: 1) Foo owned by sptr1,
        // 2) Foo shared between sptr2/sptr3.
}
```


**Output:**
```
1) unique ownership
Foo::Foo(), bar = 100 @ 0x23c5040
Foo::bar = 100, use_count() = 1
call sptr.reset()...
Foo::~Foo(), bar = 100 @ 0x23c5040
After reset(): use_count() = 0, sptr = 0

2) unique ownership
Foo::Foo(), bar = 200 @ 0x23c5040
Foo::bar = 200, use_count() = 1
call sptr.reset()...
Foo::Foo(), bar = 222 @ 0x23c5050
Foo::~Foo(), bar = 200 @ 0x23c5040
After reset(): use_count() = 1, sptr = 0x23c5050
Leaving the scope...
Foo::~Foo(), bar = 222 @ 0x23c5050

3) multiple ownership
Foo::Foo(), bar = 300 @ 0x23c5080
Foo::bar = 300, use_count() = 3
call sptr1.reset()...
Foo::Foo(), bar = 333 @ 0x23c5050
After reset():
sptr1.use_count() = 1, sptr1 @ 0x23c5050
sptr2.use_count() = 2, sptr2 @ 0x23c5080
sptr3.use_count() = 2, sptr3 @ 0x23c5080
Leaving the scope...
Foo::~Foo(), bar = 300 @ 0x23c5080
Foo::~Foo(), bar = 333 @ 0x23c5050
```


## See also


| cpp/memory/shared_ptr/dsc constructor | (see dedicated page) |

