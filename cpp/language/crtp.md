---
title: Curiously Recurring Template Pattern
type: Language
source: https://en.cppreference.com/w/cpp/language/crtp
---


# Curiously Recurring Template Pattern

The [Curiously Recurring Template Pattern](https://en.wikipedia.org/wiki/Curiously Recurring Template Pattern) is an idiom in which a class `X` derives from a class template `Y`, taking a template parameter `Z`, where `Y` is instantiated with `1=Z = X`.  For example,

```cpp
template<class Z>
class Y {};

class X : public Y<X> {};
```


## Example


### Example

```cpp
#include <cstdio>

#ifndef __cpp_explicit_this_parameter // Traditional syntax

template <class Derived>
struct Base
{
    void name() { static_cast<Derived*>(this)->impl(); }
protected:
    Base() = default; // prohibits the creation of Base objects, which is UB
};
struct D1 : public Base<D1> { void impl() { std::puts("D1::impl()"); } };
struct D2 : public Base<D2> { void impl() { std::puts("D2::impl()"); } };

#else // C++23 deducing-this syntax

struct Base { void name(this auto&& self) { self.impl(); } };
struct D1 : public Base { void impl() { std::puts("D1::impl()"); } };
struct D2 : public Base { void impl() { std::puts("D2::impl()"); } };

#endif

int main()
{
    D1 d1; d1.name();
    D2 d2; d2.name();
}
```


**Output:**
```
D1::impl()
D2::impl()
```


## See also


| cpp/memory/dsc enable_shared_from_this | (see dedicated page) |
| cpp/ranges/dsc view_interface | (see dedicated page) |


## External links

elink|[https://www.fluentcpp.com/2017/05/12/curiously-recurring-template-pattern/ The Curiously Recurring Template Pattern (CRTP) - 1] &mdash; Fluent}
elink|[https://www.fluentcpp.com/2017/05/16/what-the-crtp-brings-to-code/ What the CRTP can bring to your code - 2] &mdash; Fluent}
elink|[https://www.fluentcpp.com/2017/05/19/crtp-helper/ An implementation helper for the CRTP - 3] &mdash; Fluent}
