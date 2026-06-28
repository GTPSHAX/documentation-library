---
title: The rule of three/five/zero
type: Language
source: https://en.cppreference.com/w/cpp/language/rule_of_three
---


# The rule of three/five/zero


## Rule of three

If a class requires a user-defined `destructor`, a user-defined `copy constructor`, or a user-defined `copy assignment operator`, it almost certainly requires all three.
Because C++ copies and copy-assigns objects of user-defined types in various situations (passing/returning by value, manipulating a container, etc), these special member functions will be called, if accessible, and if they are not user-defined, they are implicitly-defined by the compiler.
The implicitly-defined special member functions should not be used if the class manages a resource whose handle is an object of non-class type (raw pointer, POSIX file descriptor, etc), whose destructor does nothing and copy constructor/assignment operator performs a "shallow copy" (copies the value of the handle, without duplicating the underlying resource).

### Example

```cpp
#include <cstddef>
#include <cstring>
#include <iostream>
#include <utility>

class rule_of_three
{
    char* cstring; // raw pointer used as a handle to a
                   // dynamically-allocated memory block

public:
    explicit rule_of_three(const char* s = "") : cstring(nullptr)
    {   
        if (s)
        {   
            cstring = new char[std::strlen(s) + 1]; // allocate
            std::strcpy(cstring, s); // populate
        }
    }

    ~rule_of_three() // I. destructor
    {
        delete[] cstring; // deallocate
    }

    rule_of_three(const rule_of_three& other) // II. copy constructor
        : rule_of_three(other.cstring) {}

    rule_of_three& operator=(const rule_of_three& other) // III. copy assignment
    {
        // implemented through copy-and-swap for brevity
        // note that this prevents potential storage reuse
        rule_of_three temp(other);
        std::swap(cstring, temp.cstring);
        return *this;
    }

    const char* c_str() const // accessor
    {
        return cstring;
    }
};

int main()
{
    rule_of_three o1{"abc"};
    std::cout << o1.c_str() << ' ';
    auto o2{o1}; // II. uses copy constructor
    std::cout << o2.c_str() << ' ';
    rule_of_three o3("def");
    std::cout << o3.c_str() << ' ';
    o3 = o2; // III. uses copy assignment
    std::cout << o3.c_str() << '\n';
}   // I. all destructors are called here
```


**Output:**
```
abc abc def abc
```

Classes that manage non-copyable resources through copyable handles may have to <sup>(until C++11)</sup> declare copy assignment and copy constructor `private` and not provide their definitions<sup>(since C++11)</sup> define copy assignment and copy constructor as `1== delete`. This is another application of the rule of three: deleting one and leaving the other to be implicitly-defined typically incorrect.

## Rule of five

Because the presence of a user-defined (include `1== default` or `1== delete` declared) destructor, copy-constructor, or copy-assignment operator prevents implicit definition of the `move constructor` and the `move assignment operator`, any class for which move semantics are desirable, has to declare all five special member functions:

```cpp
class rule_of_five
{
    char* cstring; // raw pointer used as a handle to a
                   // dynamically-allocated memory block
public:
    explicit rule_of_five(const char* s = "") : cstring(nullptr)
    { 
        if (s)
        {
            cstring = new char[std::strlen(s) + 1]; // allocate
            std::strcpy(cstring, s); // populate 
        } 
    }

    ~rule_of_five()
    {
        delete[] cstring; // deallocate
    }

    rule_of_five(const rule_of_five& other) // copy constructor
        : rule_of_five(other.cstring) {}

    rule_of_five(rule_of_five&& other) noexcept // move constructor
        : cstring(std::exchange(other.cstring, nullptr)) {}

    rule_of_five& operator=(const rule_of_five& other) // copy assignment
    {
        // implemented as move-assignment from a temporary copy for brevity
        // note that this prevents potential storage reuse
        return *this = rule_of_five(other);
    }

    rule_of_five& operator=(rule_of_five&& other) noexcept // move assignment
    {
        std::swap(cstring, other.cstring);
        return *this;
    }

// alternatively, replace both assignment operators with copy-and-swap
// implementation, which also fails to reuse storage in copy-assignment.
//  rule_of_five& operator=(rule_of_five other) noexcept
//  {
//      std::swap(cstring, other.cstring);
//      return *this;
//  }
};
```

Unlike Rule of Three, failing to provide move constructor and move assignment is usually not an error, but a missed optimization opportunity.

## Rule of zero

Classes that have custom destructors, copy/move constructors or copy/move assignment operators should deal exclusively with ownership (which follows from the Single Responsibility Principle). Other classes should not have custom destructors, copy/move constructors or copy/move assignment operators.
This rule also appears in the C++ Core Guidelines as [https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rc-zero C.20: If you can avoid defining default operations, do].

```cpp
class rule_of_zero
{
    std::string cppstring;
public:
    rule_of_zero(const std::string& arg) : cppstring(arg) {}
};
```

When a base class is intended for polymorphic use, its destructor may have to be declared `public` and `virtual`. This blocks implicit moves (and deprecates implicit copies), and so the special member functions have to be defined as `1== default`.

```cpp
class base_of_five_defaults
{
public:
    base_of_five_defaults(const base_of_five_defaults&) = default;
    base_of_five_defaults(base_of_five_defaults&&) = default;
    base_of_five_defaults& operator=(const base_of_five_defaults&) = default;
    base_of_five_defaults& operator=(base_of_five_defaults&&) = default;
    virtual ~base_of_five_defaults() = default;
};
```

However, this makes the class prone to slicing, which is why polymorphic classes often define copy as `1== delete` (see [https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c67-a-polymorphic-class-should-suppress-public-copymove C.67: A polymorphic class should suppress public copy/move] in C++ Core Guidelines), which leads to the following generic wording for the Rule of Five:
:[https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c21-if-you-define-or-delete-any-copy-move-or-destructor-function-define-or-delete-them-all C.21: If you define or =delete any copy, move, or destructor function, define or =delete them all.]

## External links

