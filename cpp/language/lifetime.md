---
title: Lifetime
type: Language
source: https://en.cppreference.com/w/cpp/language/lifetime
---


# Lifetime

Every `object` and `reference` has a ''lifetime'', which is a runtime property: for any object or reference, there is a point of execution of a program when its lifetime begins, and there is a moment when it ends.
The lifetime of an object begins when:
* storage with the proper alignment and size for its type is obtained, and
* its initialization (if any) is complete (including `default initialization` via no constructor or ), except that
:* if the object is a `union member` or subobject thereof, its lifetime only begins if that union member is the initialized member in the union, or it is made active,
:* if the object is nested in a union object, its lifetime may begin if the containing union object is assigned or constructed by a trivial special member function,
:* an array object's lifetime may also begin if it is allocated by `std::allocator::allocate`.
Some operations `implicitly create objects` of implicit-lifetime types in given region of storage and start their lifetime. If a subobject of an implicitly created object is not of an implicit-lifetime type, its lifetime does not begin implicitly.
The lifetime of an object ends when:
* if it is of a non-class type, the object is destroyed (maybe via a pseudo-destructor call), or
* if it is of a class type, the `destructor` call starts, or
* the storage which the object occupies is released, or is reused by an object that is not nested within it.
Lifetime of an object is equal to or is nested within the lifetime of its storage, see `storage duration`.
The lifetime of a `reference` begins when its initialization is complete and ends as if it were a scalar object.
Note: the lifetime of the referred object may end before the end of the lifetime of the reference, which makes  possible.
Lifetimes of non-static data members and base subobjects begin and end following `class initialization order`.

## Temporary object lifetime

Temporary objects are created <sup>(since C++17)</sup> when a prvalue is `materialized so that it can be used as a glvalue, which occurs` in the following situations:
* `binding a reference to a prvalue`
rrev|since=c++11|
* `initializing` an object of type `std::initializer_list<T>` from a `brace-enclosed initializer list`
rev|until=c++17|
* returning a prvalue from a function
* `conversion` that creates a prvalue (`including` `T(a, b, c)` and })
rrev|since=c++11|
* `lambda expression`
* `copy-initialization` that requires conversion of the initializer,
* `reference-initialization|binding a reference` to a different but convertible type or to a bitfield.
rev|since=c++17|
* when performing `member access` on a class prvalue
* when performing an `array-to-pointer` conversion or `subscripting` on an array prvalue
* for unevaluated operands in `sizeof` and `typeid`
* when a prvalue appears as a `discarded-value expression`
The materialization of a temporary object is generally delayed as long as possible in order to avoid creating unnecessary temporary object: see `copy elision`.
rrev|since=c++17|
When an object of type `T` is passed to or returned from a `potentially-evaluated` function call, if `T` is one of the following types, implementations are permitted to create temporary objects to hold the function parameter or result object:
rrev|since=c++26|
* a
* a class type satisfying all following conditions:
** `T` has at least one eligible `copy` or `move` constructor.
** Each eligible copy/move constructor of `T` is trivial.
** The `destructor` of `T` is either trivial or deleted.
rev|until=c++26|
The temporary object is constructed from the function argument or return value, respectively, and the function’s parameter or return object is initialized as if by using the eligible trivial constructor to copy the temporary (even if that constructor is inaccessible or would not be selected by overload resolution to perform a copy or move of the object).
rev|since=c++26|
The temporary objects are created as follows:
* The first such temporary object is constructed from the function argument or return value, respectively.
* Each successive temporary object is initialized from the previous one as if by `direct-initialization` if `T` is a scalar type, otherwise by using an eligible trivial constructor.
* The function parameter or return object is initialized from the final temporary as if by direct initialization if `T` is a scalar type, otherwise by using an eligible trivial constructor.
In all cases, the eligible constructor is used even if that constructor is inaccessible or would not be selected by overload resolution to perform a copy or move of the object.
This latitude is granted to allow objects to be passed to or returned from functions in registers.
All temporary objects are destroyed as the last step in evaluating the `full-expression` that (lexically) contains the point where they were created, and if multiple temporary objects were created, they are destroyed in the order opposite to the order of creation. This is true even if that evaluation ends in throwing an exception.
There are the following exceptions from that:
* The lifetime of a temporary object may be extended by binding to a reference, see `reference initialization` for details.
* The lifetime of a temporary object created when evaluating the default arguments of a default or copy constructor used to initialize or copy an element of an array ends before the next element of the array begins initialization.
rev|since=c++17|
* The lifetime of a temporary object created in a `structured binding` declaration (introduced by the initializer for a variable with unique name) is extended to the end of the structured binding declaration.
rev|since=c++23|
* The lifetime of a temporary object created in the *range-initializer* of a `range-`for`` statement that would otherwise be destroyed at the end of the *range-initializer* is extended to the end of the loop body.

## Storage reuse

A program is not required to call the destructor of an object to end its lifetime if the object is `trivially-destructible` (be careful that the correct behavior of the program may depend on the destructor). However, if a program ends the lifetime of a non-trivially destructible object that is a variable explicitly, it must ensure that a new object of the same type is constructed in-place (e.g. via placement `new`) before the destructor may be called implicitly, i.e. due to scope exit or exception for automatic objects<sup>(since C++11)</sup> , due to thread exit for thread-local objects, or due to program exit for static objects; otherwise the behavior is undefined.

```cpp
class T {}; // trivial

struct B
{
    ~B() {} // non-trivial
};

void x()
{
    long long n; // automatic, trivial
    new (&n) double(3.14); // reuse with a different type okay
} // okay

void h()
{
    B b; // automatic non-trivially destructible
    b.~B(); // end lifetime (not required, since no side-effects)
    new (&b) T; // wrong type: okay until the destructor is called
} // destructor is called: undefined behavior
```

It is undefined behavior to reuse storage that is or was occupied by a const complete object of static<sup>(since C++11)</sup> , thread-local, or automatic storage duration because such objects may be stored in read-only memory:

```cpp
struct B
{
    B(); // non-trivial
    ~B(); // non-trivial
};
const B b; // const static

void h()
{
    b.~B(); // end the lifetime of b
    new (const_cast<B*>(&b)) const B; // undefined behavior: attempted reuse of a const
}
```

When evaluating a ``new` expression`, storage is considered reused after it is returned from the allocation function, but before the evaluation of the *initializer* of the new expression:

```cpp
struct S
{
    int m;
};

void f()
{
    S x{1};
    new(&x) S(x.m); // undefined behavior: the storage is reused
}
```

If a new object is created at the address that was occupied by another object, then all pointers, references, and the name of the original object will automatically refer to the new object and, once the lifetime of the new object begins, can be used to manipulate the new object, but only if the original object is transparently replaceable by the new object.
If all following conditions are satisfied, object `x` is ''transparently replaceable'' by object `y`:
* The storage for `y` exactly overlays the storage location which `x` occupied.
* `y` is of the same type as `x` (ignoring the top-level cv-qualifiers).
* `x` is not a complete const object.
* Neither `x` nor `y` is a base class subobject<sup>(since C++20)</sup> , or a member subobject declared with .
* One of the following conditions is satisfied:
:* `x` and `y` are both complete objects.
:* `x` and `y` are direct subobjects of objects `ox` and `oy` respectively, and `ox` is transparently replaceable by `oy`.

```cpp
struct C
{
    int i;
    void f();
    const C& operator=(const C&);
};

const C& C::operator=(const C& other)
{
    if (this != &other)
    {
        this->~C();          // lifetime of *this ends
        new (this) C(other); // new object of type C created
        f();                 // well-defined
    }
    return *this;
}

C c1;
C c2;
c1 = c2; // well-defined
c1.f();  // well-defined; c1 refers to a new object of type C
```

rrev|since=c++17|
If the conditions listed above are not met, a valid pointer to the new object may still be obtained by applying the pointer optimization barrier `std::launder`:

```cpp
struct A
{ 
    virtual int transmogrify();
};

struct B : A
{
    int transmogrify() override { ::new(this) A; return 2; }
};

inline int A::transmogrify() { ::new(this) B; return 1; }

void test()
{
    A i;
    int n = i.transmogrify();
    // int m = i.transmogrify(); // undefined behavior:
    // the new A object is a base subobject, while the old one is a complete object
    int m = std::launder(&i)->transmogrify(); // OK
    assert(m + n == 3);
}
```

Similarly, if an object is created in the storage of a class member or array element, the created object is only a subobject (member or element) of the original object's containing object if:
* the lifetime of the containing object has begun and not ended
* the storage for the new object exactly overlays the storage of the original object
* the new object is of the same type as the original object (ignoring cv-qualification).
rrev|since=c++17|
Otherwise, the name of the original subobject cannot be used to access the new object without `std::launder`:

### Providing storage

As a special case, objects can be created in arrays of `unsigned char`<sup>(since C++17)</sup>  or  (in which case it is said that the array ''provides storage'' for the object) if
* the lifetime of the array has begun and not ended
* the storage for the new object fits entirely within the array
* there is no array object that satisfies these constraints nested within the array.
If that portion of the array previously provided storage for another object, the lifetime of that object ends because its storage was reused, however the lifetime of the array itself does not end (its storage is not considered to have been reused).

```cpp
template<typename... T>
struct AlignedUnion
{
    alignas(T...) unsigned char data[max(sizeof(T)...)];
};

int f()
{
    AlignedUnion<int, char> au;
    int *p = new (au.data) int;     // OK, au.data provides storage
    char *c = new (au.data) char(); // OK, ends lifetime of *p
    char *d = new (au.data + 1) char();
    return *c + *d; // OK
}
```


## Access outside of lifetime

Before the lifetime of an object has started but after the storage which the object will occupy has been allocated or, after the lifetime of an object has ended and before the storage which the object occupied is reused or released, the behaviors of the following uses of the glvalue expression that identifies that object are undefined, unless the object is being constructed or destructed (separate set of rules applies):
# Lvalue to rvalue conversion (e.g. function call to a function that takes a value).
# Access to a non-static data member or a call to a non-static member function.
# Binding a reference to a virtual base class subobject.
# `dynamic_cast` or `typeid` expressions.
The above rules apply to pointers as well (binding a reference to virtual base is replaced by implicit conversion to a pointer to virtual base), with two additional rules:
# `static_cast` of a pointer to storage without an object is only allowed when casting to (possibly cv-qualified) `void*`.
# Pointers to storage without an object that were cast to possibly cv-qualified `void*` can only be `static_cast` to pointers to possibly cv-qualified `char`, or possibly cv-qualified `unsigned char`<sup>(since C++17)</sup> , or possibly cv-qualified `cpp/types/byte|std::byte`.
During construction and destruction it is generally allowed to call non-static member functions, access non-static data members, and use `typeid` and `dynamic_cast`. However, because the lifetime either has not begun yet (during construction) or has already ended (during destruction), only specific operations are allowed. For one restriction, see `virtual function calls during construction and destruction`.

## Notes

Until the resolution of , the end of lifetime rules are different between non-class objects (end of storage duration) and class objects (reverse order of construction):

```cpp
struct A
{
    int* p;
    ~A() { std::cout << *p; } // undefined behavior since CWG2256: n does not outlive a
                              // well-defined until CWG2256: prints 123
};

void f()
{
    A a;
    int n = 123; // if n did not outlive a, this could have been optimized out (dead store)
    a.p = &n;
}
```

Until the resolution of [https://wg21.link/p1971r0#RU007 RU007], a non-static member of a const-qualified type or a reference type prevents its containing object from being transparently replaceable, which makes `std::vector` and `std::deque` hard to implement:

```cpp
struct X { const int n; };
union U { X x; float f; };

void tong()
{
    U u = { {1} };
    u.f = 5.f;                          // OK: creates new subobject of 'u'
    X *p = new (&u.x) X {2};            // OK: creates new subobject of 'u'
    assert(p->n == 2);                  // OK
    assert(u.x.n == 2);                 // undefined until RU007:
                                        // 'u.x' does not name the new subobject
    assert(*std::launder(&u.x.n) == 2); // OK even until RU007
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-119 | C++98 | an object of a class type with a non-trivial constructor can<br>only start its lifetime when the constructor call has completed | lifetime also started<br>for other initializations |
| cwg-201 | C++98 | lifetime of a temporary object in a default argument<br>of a default constructor was required to end<br>when the initialization of the array completes | lifetime ends before<br>initializing the next<br>element (also resolves<br>cwg |
| cwg-2012 | C++98 | lifetime of references was specified to match storage duration,<br>requiring that extern references are alive before their initializers run | lifetime begins<br>at initialization |
| cwg-2256 | C++98 | lifetime of trivially destructible objects were inconsistent with other objects | made consistent |
| cwg-2470 | C++98 | more than one arrays could provide storage for the same object | only one provides |
| cwg-2523 | C++98 | if a destructor is not invoked because of reusing storage and the<br>program depends on its side effects, the behavior was undefined | the behavior is well-<br>defined in this case |
| cwg-2854 | C++98 | exception objects were temporary objects | they are not<br>temporary objects |
| cwg-2867 | C++17 | the lifetime of temporary objects created in<br>structured binding declarations were not extended | extended to the end<br>of the declaration |


## References


## See also

