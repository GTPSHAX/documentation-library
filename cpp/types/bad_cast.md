---
title: std::bad_cast
type: Utilities
source: https://en.cppreference.com/w/cpp/types/bad_cast
---

ddcl|header=typeinfo|
class bad_cast : public std::exception;
An exception of this type is thrown when a `cpp/language/dynamic_cast` to a reference type fails the run-time check (e.g. because the types are not related by inheritance), and also from `std::use_facet` if the requested facet does not exist in the locale.

## Member functions


## Notes


## Example


### Example

```cpp
#include <iostream>
#include <typeinfo>

struct Foo { virtual ~Foo() {} };
struct Bar { virtual ~Bar() { std::cout << "~Bar\n"; } };
struct Pub : Bar { ~Pub() override { std::cout << "~Pub\n"; } };

int main()
{
    Pub pub;
    try
    {
        [[maybe_unused]]
        Bar& r1 = dynamic_cast<Bar&>(pub); // OK, upcast

        [[maybe_unused]]
        Foo& r2 = dynamic_cast<Foo&>(pub); // throws
    }
    catch (const std::bad_cast& e)
    {
        std::cout << "e.what(): " << e.what() << '\n';
    }
}
```


**Output:**
```
e.what(): std::bad_cast
~Pub
~Bar
```

