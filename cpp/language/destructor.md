---
title: Destructors
type: Language
source: https://en.cppreference.com/w/cpp/language/destructor
---


# Destructors

A destructor is a special `member function` that is called when the `lifetime of an object` ends. The purpose of the destructor is to free the resources that the object may have acquired during its lifetime.
rrev|since=c++20|
A destructor cannot be a `coroutine`.

## Syntax

<sup>(until C++20)</sup> Destructors<sup>(since C++20)</sup> Prospective destructors are declared using member `function declarators` of the following form:

**Syntax:**

- `**`(`** *parameter-list* (optional) **`)`** *except* (optional) *attr* (optional)`

### Parameters

- `{{spar` - class-name-with-tilde|an `identifier expression`,<sup>(since C++11)</sup>  possibly followed by a list of `attributes, and` possibly enclosed by a pair parentheses
- `{{spar` - parameter-list| (must be either empty or `void`)
- `{{spar` - except|
- `{{spar` - attr|<sup>(C++11)</sup> a list of `attributes`
The only specifiers allowed in the `declaration specifiers` of a<sup>(since C++20)</sup>  prospective destructor declaration are<sup>(since C++11)</sup> `constexpr,` `friend`, `inline` and `virtual` (in particular, no return type is allowed).
The identifier expression of *class-name-with-tilde* must have one of the following forms:
* In a member declaration that belongs to the  of a class or class template, but is not a `friend declaration`:
:* For classes, the identifier expression is `~` followed by the `injected-class-name` of the immediately-enclosing class.
:* For class templates, the identifier expression is `~` followed by <sup>(until C++20)</sup> a class name that names the <sup>(since C++20)</sup> the injected-class-name of the immediately-enclosing class template.
* Otherwise, the identifier expression is a qualified identifier whose terminal unqualified identifier is `~` followed by the injected-class name of the class nominated by the non-terminal parts of the qualified identifier.

## Explanation

The destructor is implicitly invoked whenever an object's `lifetime` ends, which includes
* program termination, for objects with static `storage duration`
rrev|since=c++11|
* thread exit, for objects with thread-local storage duration
* end of scope, for objects with automatic storage duration and for temporaries whose life was extended by binding to a reference
* ``delete` expression`, for objects with dynamic storage duration
* end of the full `expression`, for nameless temporaries
* , for objects with automatic storage duration when an exception escapes their block, uncaught.
The destructor can also be invoked explicitly.
rrev|since=c++20|

## Prospective destructor

A class may have one or more prospective destructors, one of which is selected as the destructor for the class.
In order to determine which prospective destructor is the destructor, at the end of the definition of the class, `overload resolution` is performed among prospective destructors declared in the class with an empty argument list. If the overload resolution fails, the program is ill-formed. Destructor selection does not `odr-use` the selected destructor, and the selected destructor may be deleted.
All prospective destructors are special member functions. If no user-declared prospective destructor is provided for class `T`, the compiler will always implicitly declare one, and the implicitly-declared prospective destructor is also the destructor for `T`.

### Example

```cpp
#include <cstdio>
#include <type_traits>

template<typename T>
struct A
{
    ~A() requires std::is_integral_v<T> { std::puts("~A, T is integral"); }
    ~A() requires std::is_pointer_v<T> { std::puts("~A, T is a pointer"); }
    ~A() { std::puts("~A, T is anything else"); }
};

int main()
{
    A<int> a;
    A<int*> b;
    A<float> c;
}
```


**Output:**
```
~A, T is anything else
~A, T is a pointer
~A, T is integral
```


## Potentially-invoked destructor

The destructor for class `T` is ''potentially invoked'' in the following situations:
* It is invoked explicitly or implicitly.
* A ``new` expression` creates an array of objects of type `T`.
* The result object of a ``return` statement` is of type `T`.
* An array is under `aggregate initialization`, and its element type is `T`.
* A class object is under aggregate initialization, and it has a member of type `T` where `T` is not an `anonymous union` type.
* A `potentially constructed subobject` is of type `T` in a<sup>(since C++11)</sup>  non-`delegating` constructor.
* An  of type `T` is constructed.
If a potentially-invoked destructor is<sup>(since C++11)</sup>  deleted or not accessible from the context of the invocation, the program is ill-formed.

## Implicitly-declared destructor

If no user-declared<sup>(since C++20)</sup>  prospective destructor is provided for a `class type`, the compiler will always declare a destructor as an `inline public` member of its class.
As with any implicitly-declared special member function, the exception specification of the implicitly-declared destructor is non-throwing unless <sup>(since C++17)</sup> the destructor of any potentially-constructed base or member is `potentially-throwing`<sup>(until C++17)</sup> implicit definition would directly invoke a function with a different exception specification. In practice, implicit destructors are `noexcept` unless the class is "poisoned" by a base or member whose destructor is `noexcept(false)`.

## Implicitly-defined destructor

If an implicitly-declared destructor is not deleted, it is implicitly defined (that is, a function body is generated and compiled) by the compiler when it is `odr-used`. This implicitly-defined destructor has an empty body.
rrev|since=c++20|
If this satisfies the requirements of a <sup>(until C++23)</sup> <sup>(since C++23)</sup> , the generated destructor is `constexpr`.
rrev|since=c++11|

## Deleted destructor

The implicitly-declared or explicitly-defaulted destructor for class `T` is defined as deleted if any of the following conditions is satisfied:
rev|until=c++26|
* `T` has a  of class type `M` (or possibly multi-dimensional array thereof) such that `M` has a destructor that
:* is deleted or inaccessible from the destructor of `T`, or
:* in the case of the subobject being a `variant member`, is non-trivial.
rev|since=c++26|
* `T` is not a union, and has a non-`variant`  of class type `M` (or possibly multidimensional array thereof) such that `M` has a destructor that is deleted or inaccessible from the destructor of `T`.
* `T` is a union, and any of the following conditions is satisfied:
:* The overload resolution to select a constructor to default-initialize an object of type `T` either fails or selects a constructor that is either deleted or non-trivial.
:* `T` has a variant member `V` of class type `M` (or possibly multidimensional array thereof) where `V` has a default initializer and `M` has a destructor that is non-trivial.
* The destructor is virtual and the lookup for the deallocation function results in
:* an ambiguity, or
:* a function that is deleted or inaccessible from the destructor.
rrev|since=c++20|
An explicitly-defaulted prospective destructor for `T` is defined as deleted if it is not the destructor for `T`.

## Trivial destructor

The destructor for class `T` is trivial if all following conditions are satisfied:
* The destructor is <sup>(until C++11)</sup> implicitly-declared<sup>(since C++11)</sup> not `user-provided`.
* The destructor is not virtual.
* All direct base classes have trivial destructors.
rev|until=c++26|
* Every non-static data member of class type (or array of class type) has a trivial destructor.
rev|since=c++26|
* Either `T` is a union, or every non-variant non-static data member of class type (or array of class type) has a trivial destructor.
A trivial destructor is a destructor that performs no action. Objects with trivial destructors don't require a `delete` expression and may be disposed of by simply deallocating their storage. All data types compatible with the C language (POD types) are trivially destructible.

## Destruction sequence

For both user-defined or implicitly-defined destructors, after executing the body of the destructor and destroying any automatic objects allocated within the body, the compiler calls the destructors for all non-static non-variant data members of the class, in reverse order of declaration, then it calls the destructors of all direct non-virtual base classes in `reverse order of construction` (which in turn call the destructors of their members and their base classes, etc), and then, if this object is of `most derived class`, it calls the destructors of all virtual bases.
Even when the destructor is called directly (e.g. `obj.~Foo();`), the `return` statement in `~Foo()` does not return control to the caller immediately: it calls all those member and base destructors first.

## Virtual destructors

Deleting an object through pointer to base invokes undefined behavior unless the destructor in the base class is `virtual`:

```cpp
class Base
{
public:
    virtual ~Base() {}
};

class Derived : public Base {};

Base* b = new Derived;
delete b; // safe
```

A common guideline is that a destructor for a base class must be [http://www.gotw.ca/publications/mill18.htm either public and virtual or protected and nonvirtual].

## Pure virtual destructors

A <sup>(since C++20)</sup> prospective destructor may be declared `pure virtual`, for example in a base class which needs to be made abstract, but has no other suitable functions that could be declared pure virtual. A pure virtual destructor must have a definition, since all base class destructors are always called when the derived class is destroyed:

```cpp
class AbstractBase
{
public:
    virtual ~AbstractBase() = 0;
};
AbstractBase::~AbstractBase() {}

class Derived : public AbstractBase {};

// AbstractBase obj; // compiler error
Derived obj;         // OK
```


## Exceptions

As any other function, a destructor may terminate by throwing an `exception` <sup>(since C++11)</sup> (this usually requires it to be explicitly declared `noexcept(false)`), however if this destructor happens to be called during , `std::terminate` is called instead.
Although `std::uncaught_exceptions` may sometimes be used to detect stack unwinding in progress, it is generally considered bad practice to allow any destructor to terminate by throwing an exception. This functionality is nevertheless used by some libraries, such as  [https://github.com/SOCI/soci SOCI] and [https://galeracluster.com/downloads/ Galera 3], which rely on the ability of the destructors of nameless temporaries to throw exceptions at the end of the full expression that constructs the temporary.
in Library fundamental TS v3 may have a potentially-throwing destructor, which throws an exception when the scope is exited normally and the exit function throws an exception.

## Notes

Calling a destructor directly for an ordinary object, such as a local variable, invokes undefined behavior when the destructor is called again, at the end of scope.
In generic contexts, the destructor call syntax can be used with an object of non-class type; this is known as pseudo-destructor call: see `member access operator`.

## Example


### Example

```cpp
#include <iostream>

struct A
{
    int i;

    A(int num) : i(num)
    {
        std::cout << "ctor a" << i << '\n';
    }

    (~A)() // but usually ~A()
    {
        std::cout << "dtor a" << i << '\n';
    }
};

A a0(0);

int main()
{
    A a1(1);
    A* p;

    { // nested scope
        A a2(2);
        p = new A(3);
    } // a2 out of scope

    delete p; // calls the destructor of a3
}
```


**Output:**
```
ctor a0
ctor a1
ctor a2
ctor a3
dtor a2
dtor a3
dtor a1
dtor a0
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-193 | C++98 | whether automatic objects in a destructor are<br>destroyed before or after the destruction of the<br>class's base and member subobjects was unspecified | they are destroyed<br>before destroying<br>those subobjects |
| cwg-1241 | C++98 | static members might be destroyed<br>right after destructor execution | only destroy non-<br>static members |
| cwg-1353 | C++98 | the conditions where implicitly-declared destructors are<br>undefined did not consider multi-dimensional array types | consider these types |
| cwg-1435 | C++98 | the meaning of “class name” in the<br>declarator syntax of destructor was unclear | changed the syntax to a specialized<br>function declarator syntax |
| cwg-2180 | C++98 | the destructor of a class that is not a most derived class<br>would call the destructors of its virtual direct base classes | it will not call those destructors |


## See also

* `copy elision`
* `new`
* `delete`
