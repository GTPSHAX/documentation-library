---
title: The this pointer
type: Language
source: https://en.cppreference.com/w/cpp/language/this
---


# The tt|this


## Syntax


**Syntax:**

The expression `this` is a  `expression` whose value is the address of the  (object on which the implicit object member function is being called). It can appear in the following contexts:
1. Within the body of any `implicit object member function`, including `member initializer list`<sup>(since C++11)</sup> , and `lambda expression body`.
2. Within the `declaration` of any implicit object member function anywhere after the (optional) cv-qualifier sequence, including the `exception specification`<sup>(since C++11)</sup>  and the trailing return type.
rrev|since=c++11|
3. Within `default member initializer`.
4. Within `capture list` of a lambda expression.

## Explanation

`this` can only associate with the innermost enclosing class of its appearance, even if the appearance is invalid in the context:

```cpp
class Outer
{
    int a[sizeof(*this)];            // Error: not inside a member function
    unsigned int sz = sizeof(*this); // OK: in default member initializer

    void f()
    {
        int b[sizeof(*this)];     // OK

        struct Inner
        {
            int c[sizeof(*this)]; // Error: not inside a member function of Inner
                                  // “this” is not associated with Outer
                                  // even if it is inside a member function of Outer
        };
    }
};
```

The type of `this` in a member function of class `X` is `X*` (pointer to X). If the member function is `declared with a cv-qualifier sequence` ''cv'', the type of `this` is `''cv'' X*` (pointer to identically cv-qualified X). Since constructors and destructors cannot be declared with cv-qualifiers, the type of `this` in them is always `X*`, even when constructing or destroying a const object.
In class templates, `this` is a `dependent expression`, and explicit `this->` may be used to force another expression to become dependent.

```cpp
template<typename T>
struct B
{
    int var;
};

template<typename T>
struct D : B<T>
{
    D()
    {
        // var = 1;    // Error: “var” was not declared in this scope
        this->var = 1; // OK
    }
};
```

`During construction` of an object, if the value of the object or any of its subobjects is accessed through a glvalue that is not obtained, directly or indirectly, from the constructor's `this` pointer, the value of the object or subobject thus obtained is unspecified. In other words, the this pointer cannot be aliased in a constructor:

```cpp
extern struct D d;

struct D
{
    D(int a) : a(a), b(d.a) {} // b(a) or b(this->a) would be correct
    int a, b;
};

D d = D(1); // because b(d.a) did not obtain a through this, d.b is now unspecified
```

It is possible to execute `delete this;`, if the program can guarantee that the object was allocated by `new`, however, this renders every pointer to the deallocated object invalid, including the `this` pointer itself: after `delete this;` returns, such member function cannot refer to a member of a class (since this involves an implicit dereference of `this`) and no other member function may be called.
This can be used in the member function of the reference-counting pointer <sup>(since C++11)</sup> (for example, `std::shared_ptr`) responsible for decrementing the reference count, when the last reference to the managed object goes out of scope.

```cpp
<!-- libreoffice i18nlangtag/source/languagetag/simple-langtag.cxx -->
class ref
{
    // ...
    void incRef() { ++mnRef; }
    void decRef() { if (--mnRef == 0) delete this; }
};
```


## Keywords

`cpp/keyword/this`

## Example

source
|
|code=
class T
{
int x;
void foo()
{
x = 6;       // same as this->x = 6;
this->x = 5; // explicit use of this->
}
void foo() const
{
//  x = 7; // Error: *this is constant
}
void foo(int x) // parameter x shadows the member with the same name
{
this->x = x; // unqualified x refers to the parameter
// “this->” is required for disambiguation
}
int y;
T(int x) : x(x),      // uses parameter x to initialize member x
y(this->x) // uses member x to initialize member y
{}
T& operator=(const T& b)
{
x = b.x;
return *this; // many overloaded operators return *this
}
};

## Defect reports

