---
title: std::unique_ptr::get_deleter
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/unique_ptr/get_deleter
---


```cpp
|1=
Deleter& get_deleter() noexcept;
|1=
const Deleter& get_deleter() const noexcept;
```

Returns the deleter object which would be used for destruction of the managed object.

## Parameters

(none)

## Return value

The stored deleter object.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

struct Foo
{
    Foo() { std::cout << "Foo() 0x" << std::hex << (void*)this << '\n'; }
    ~Foo() { std::cout << "~Foo() 0x" << std::hex << (void*)this << '\n'; }
};

struct D
{
    int number;

    void bar()
    {
        std::cout << "call D::bar(), my number is: " << std::dec << number << '\n';
    }

    void operator()(Foo* p) const
    {
        std::cout << "call deleter for Foo object 0x" << std::hex << (void*)p << '\n';
        delete p;
    }
};

int main()
{
    std::cout << "main start\n";

    std::unique_ptr<Foo, D> up1(new Foo(), D(42));
    D& del1 = up1.get_deleter();
    del1.bar();

    std::unique_ptr<Foo, D> up2(new Foo(), D(43));
    D& del2 = up2.get_deleter();
    auto* released = up2.release();
    del2(released);

    std::cout << "main end\n";
}
```


**Output:**
```
main start
Foo() 0x0x90cc30
call D::bar(), my number is: 42
Foo() 0x0x90cc50
call deleter for Foo object 0x0x90cc50
~Foo() 0x0x90cc50
main end
call deleter for Foo object 0x0x90cc30
~Foo() 0x0x90cc30
```


## See also


| cpp/memory/shared_ptr/dsc get_deleter | (see dedicated page) |

