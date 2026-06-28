---
title: dynamic_cast conversion
type: Language
source: https://en.cppreference.com/w/cpp/language/dynamic_cast
---


# tt|dynamic_cast

Safely converts pointers and references to classes up, down, and sideways along the inheritance hierarchy.

## Syntax


**Syntax:**

- `*target-type* **`>(`** *expression* **`)`**`

### Parameters

- `{{spar` - target-type|pointer to complete class type, reference to complete class type, or pointer to (optionally cv-qualified) `void`
- `{{spar` - expression|<sup>(until C++11)</sup> lvalue<sup>(since C++11)</sup> glvalue of a complete class type if *target-type* is a reference, prvalue of a pointer to complete class type if *target-type* is a pointer

## Explanation

For the convenience of description, “*expression* or the result is a reference to `T`” means that “it is a glvalue of type `T`”<sup>(since C++11)</sup> , which follows the convention of `decltype`.
Only the following conversions can be done with `dynamic_cast`, except when such conversions would `cast away constness` (or volatility).
1. If the type of *expression* is exactly *target-type* or a less cv-qualified version of *target-type*, the result is the value of *expression* with type *target-type*. In other words, `dynamic_cast` can be used to '''add constness'''. An implicit conversion and `static_cast` can perform this conversion as well.
2. If *target-type* is “pointer to (possibly cv-qualified) `Base`” and the type of *expression* is “pointer to (possibly cv-qualified) `Derived`” such that `Base` is a base class of `Derived`, the result is
* a null pointer value if *expression* is a null pointer value, or
* a pointer to the unique `Base` `subobject` of the `Derived` object pointed to by *expression* otherwise. In other words, `dynamic_cast` can be used to '''upcast''' pointers, from derived to base. An implicit conversion and `static_cast` can perform this conversion as well.
3. If *target-type* is “reference to (possibly cv-qualified) `Base`” and the type of *expression* is “(possibly cv-qualified) `Derived`” such that `Base` is a base class of `Derived`, the result is the unique `Base` subobject of the `Derived` object referred to by *expression*. In other words, `dynamic_cast` can be used to '''upcast''' references, from derived to base. An implicit conversion and `static_cast` can perform this conversion as well.
4. If *expression* is a null pointer value of a `polymorphic type`, the result is the null pointer value of *target-type*.
5. Otherwise, *expression* must be a pointer or reference to an object of `polymorphic type` within its `lifetime` or within its period of construction or destruction whose type is `similar` to the type of *expression* (otherwise the behavior is undefined)
:@a@ If *target-type* is a pointer to (possibly cv-qualified) `void`, the result is a pointer to the `most derived object` pointed to by *expression*.
:@b@ Otherwise a runtime check is applied to see if the object pointed/referred to by *expression* can be converted to the type `Target`, pointed or referred to by *target-type*:
::@i@ If, in the most derived object pointed/referred to by *expression*, *expression* points/refers to a public base class subobject of a `Target` object, and if only one object of type `Target` is derived from the subobject pointed/referred to by *expression*, the result points/refers to that `Target` object. In other words, `dynamic_cast` can be used to '''downcast''' pointers/references, from base to derived.
::@ii@ Otherwise, if *expression* points/refers to a public base class subobject of the most derived object, and the type of the most derived object has an unambiguous and public base class of type `Target`, the result points/refers to the `Target` subobject of the most derived object. In other words, `dynamic_cast` can be used to '''crosscast''' (or side-cast)  pointers/references, between two types derived from the same base.
::@iii@ Otherwise, the runtime check fails.
* If *target-type* is a pointer type, the result is the null pointer value of *target-type*.
* If *target-type* is a reference type, an exception of a type that would match a `handler` of type `std::bad_cast` is thrown.
When `dynamic_cast` is used in a constructor or a destructor (directly or indirectly), and *expression* refers to the object that's currently under construction/destruction, the object is considered to be the most derived object. If *target-type* is not a pointer or reference to the constructor's/destructor's own class or one of its bases, the behavior is undefined.
Similar to other cast expressions, the result is:
rev|until=c++11|
* an lvalue if *target-type* is a reference type
* an rvalue if *target-type* is a pointer type
rev|since=c++11|
* an lvalue if *target-type* is an lvalue reference type (*expression* must be an lvalue)
* an xvalue if *target-type* is an rvalue reference type (*expression* <sup>(until C++17)</sup> may be lvalue or rvalue<sup>(since C++17)</sup> must be a glvalue (prvalues are `materialized)` of a complete class type)
* a prvalue if *target-type* is a pointer type

## Notes

A downcast can also be performed with `static_cast`, which avoids the cost of the runtime check, but it is only safe if the program can guarantee (through some other logic) that the object pointed to by *expression* is definitely `Derived`.
Some forms of `dynamic_cast` rely on [Run-time type information|run-time type identification](https://en.wikipedia.org/wiki/Run-time type information|run-time type identification) (RTTI), that is, information about each polymorphic class in the compiled program. Compilers typically have options to disable the inclusion of this information.

## Keywords

`cpp/keyword/dynamic_cast`

## Example


### Example

```cpp
#include <iostream>

struct V
{
    virtual void f() {} // must be polymorphic to use runtime-checked dynamic_cast
};

struct A : virtual V {};

struct B : virtual V
{
    B(V* v, A* a)
    {
        // casts during construction (see the call in the constructor of D below)
        dynamic_cast<B*>(v); // well-defined: v of type V*, V base of B, results in B*
        dynamic_cast<B*>(a); // undefined behavior: a has type A*, A not a base of B
    }
};

struct D : A, B
{
    D() : B(static_cast<A*>(this), this) {}
};

struct Base
{
    virtual ~Base() {}
};

struct Derived : Base
{
    virtual void name() {}
};

int main()
{
    D d; // the most derived object
    A& a = d; // upcast, dynamic_cast may be used, but unnecessary

    [[maybe_unused]]
    D& new_d = dynamic_cast<D&>(a); // downcast
    [[maybe_unused]]
    B& new_b = dynamic_cast<B&>(a); // sidecast

    Base* b1 = new Base;
    if (Derived* d = dynamic_cast<Derived*>(b1); d != nullptr)
    {
        std::cout << "downcast from b1 to d successful\n";
        d->name(); // safe to call
    }

    Base* b2 = new Derived;
    if (Derived* d = dynamic_cast<Derived*>(b2); d != nullptr)
    {
        std::cout << "downcast from b2 to d successful\n";
        d->name(); // safe to call
    }

    delete b1;
    delete b2;
}
```


**Output:**
```
downcast from b2 to d successful
```


## Defect reports


## References


## See also

* `const_cast`
* `static_cast`
* `reinterpret_cast`
* `explicit cast`
* `implicit conversions`
