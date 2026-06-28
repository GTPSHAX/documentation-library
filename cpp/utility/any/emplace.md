---
title: std::any::emplace
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/any/emplace
---


```cpp
dcl|num=1|since=c++17|
template< class ValueType, class... Args >
std::decay_t<ValueType>& emplace( Args&&... args );
dcl|num=2|since=c++17|
template< class ValueType, class U, class... Args >
std::decay_t<ValueType>& emplace( std::initializer_list<U> il, Args&&... args );
```

Changes the contained object to one of type `std::decay_t<ValueType>` constructed from the arguments.
First destroys the current contained object (if any) by `reset|reset()`, then:
1. constructs an object of type `std::decay_t<ValueType>`, direct-non-list-initialized from `std::forward<Args>(args)...`, as the contained object.
* .
2. constructs an object of type `std::decay_t<ValueType>`, direct-non-list-initialized from `il, std::forward<Args>(args)...`, as the contained object.
* .

## Template parameters


### Parameters

- `ValueType` - contained value type

**Type requirements:**

- `std::decay_t<ValueType>`

## Return value

A reference to the new contained object.

## Exceptions

Throws any exception thrown by `T`'s constructor. If an exception is thrown, the previously contained object (if any) has been destroyed, and `*this` does not contain a value.

## Example


### Example

```cpp
#include <algorithm>
#include <any>
#include <iostream>
#include <string>
#include <vector>

class Star
{
    std::string name;
    int id;

public:
    Star(std::string name, int id) : name{name}, id{id}
    {
        std::cout << "Star::Star(string, int)\n";
    }

    void print() const
    {
        std::cout << "Star{\"" << name << "\" : " << id << "};\n";
    }
};

int main()
{
    std::any celestial;
    // (1) emplace(Args&&... args);
    celestial.emplace<Star>("Procyon", 2943);
    const auto* star = std::any_cast<Star>(&celestial);
    star->print();

    std::any av;
    // (2) emplace(std::initializer_list<U> il, Args&&... args);
    av.emplace<std::vector<char>>({'C', '+', '+', '1', '7'} /* no args */);
    std::cout << av.type().name() << '\n';
    const auto* va = std::any_cast<std::vector<char>>(&av);
    std::for_each(va->cbegin(), va->cend(), [](char const& c) { std::cout << c; });
    std::cout << '\n';
}
```


**Output:**
```
Star::Star(string, int)
Star{"Procyon" : 2943};
St6vectorIcSaIcEE
C++17
```


## See also


| cpp/utility/any/dsc constructor | (see dedicated page) |
| cpp/utility/any/dsc reset | (see dedicated page) |

