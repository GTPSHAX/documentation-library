---
title: std::type_index
type: Utilities
source: https://en.cppreference.com/w/cpp/types/type_index
---


```cpp
**Header:** `<`typeindex`>`
dcl|since=c++11|
class type_index;
```

The `type_index` class is a wrapper class around a `std::type_info` object, that can be used as index in associative and unordered associative containers. The relationship with `type_info` object is maintained through a pointer, therefore `type_index` is *CopyConstructible* and *CopyAssignable*.

## Member functions


| cpp/types/type_index/dsc constructor | (see dedicated page) |
| cpp/types/type_index/dsc operator_cmp | (see dedicated page) |
| cpp/types/type_index/dsc hash_code | (see dedicated page) |
| cpp/types/type_index/dsc name | (see dedicated page) |


## Helper classes


| cpp/types/type_index/dsc hash | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <memory>
#include <string>
#include <typeindex>
#include <typeinfo>
#include <unordered_map>

struct A
{
    virtual ~A() {}
};

struct B : A {};
struct C : A {};

int main()
{
    std::unordered_map<std::type_index, std::string> type_names;

    type_names[std::type_index(typeid(int))] = "int";
    type_names[std::type_index(typeid(double))] = "double";
    type_names[std::type_index(typeid(A))] = "A";
    type_names[std::type_index(typeid(B))] = "B";
    type_names[std::type_index(typeid(C))] = "C";

    int i;
    double d;
    A a;

    // note that we're storing pointer to type A
    std::unique_ptr<A> b(new B);
    std::unique_ptr<A> c(new C);

    std::cout << "i is " << type_names[std::type_index(typeid(i))] << '\n';
    std::cout << "d is " << type_names[std::type_index(typeid(d))] << '\n';
    std::cout << "a is " << type_names[std::type_index(typeid(a))] << '\n';
    std::cout << "*b is " << type_names[std::type_index(typeid(*b))] << '\n';
    std::cout << "*c is " << type_names[std::type_index(typeid(*c))] << '\n';
}
```


**Output:**
```
i is int
d is double
a is A
*b is B
*c is C
```


## See also


| cpp/types/dsc type_info | (see dedicated page) |

