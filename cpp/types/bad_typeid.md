---
title: std::bad_typeid
type: Utilities
source: https://en.cppreference.com/w/cpp/types/bad_typeid
---

ddcl|header=typeinfo|
class bad_typeid : public std::exception;
An exception of this type is thrown when a `cpp/language/typeid` operator is applied to a dereferenced null pointer value of a polymorphic type.

## Member functions


## Notes


## Example


### Example

```cpp
#include <iostream>
#include <typeinfo>

struct S // The type has to be polymorphic
{
    virtual void f();
};

int main()
{
    S* p = nullptr;
    try
    {
        std::cout << typeid(*p).name() << '\n';
    }
    catch (const std::bad_typeid& e)
    {
        std::cout << e.what() << '\n';
    }
}
```


**Output:**
```
Attempted a typeid of NULL pointer!
```

