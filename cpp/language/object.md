---
title: Object
type: Language
source: https://en.cppreference.com/w/cpp/language/object
---


# Object

C++ programs create, destroy, refer to, access, and manipulate ''objects''.
An object, in C++, has
* size (can be determined with `sizeof`);
* alignment requirement (can be determined with `alignof`);
* `storage duration` (automatic, static, dynamic, thread-local);
* `lifetime` (bounded by storage duration or temporary);
* `type`;
* value (which may be indeterminate, e.g. for `default-initialized` non-class types);
* optionally, a `name`.
The following entities are not objects: value, reference, function, enumerator, type, non-static class member, template, class or function template specialization, namespace, parameter pack, and `this`.
A ''variable'' is an object or a reference that is not a non-static data member, that is introduced by a `declaration`.

## Object creation

Objects can be explicitly created by `definition`s, ``new` expressions`, ``throw` expressions`, changing the active member of a `union` and evaluating expressions that require `temporary objects`. The created object is uniquely defined in explicit object creation.
Objects of implicit-lifetime types can also be implicitly created by
* except during constant evaluation, operations that begin lifetime of an array of type `unsigned char`<sup>(since C++17)</sup>  or , in which case such objects are created in the array,
* call to following allocating functions, in which case such objects are created in the allocated storage:
:* `operator new` (except during constant evaluation)
:* `operator new[]` (except during constant evaluation)
:* `std::malloc`
:* `std::calloc`
:* `std::realloc`
rrev|since=c++17|
:* `std::aligned_alloc`
* call to following object representation copying functions, in which case such objects are created in the destination region of storage or the result:
:* `std::memcpy`
:* `std::memmove`
rrev|since=c++20|
:* `cpp/numeric/bit_cast|std::bit_cast`
rrev|since=c++23|
* call to following specific functions, in which case such objects are created in the specified region of storage:
:* `std::start_lifetime_as`
:* `std::start_lifetime_as_array`
Zero or more objects may be created in the same region of storage, as long as doing so would give the program defined behavior. If such creation is impossible, e.g. due to conflicting operations, the behavior of the program is undefined. If multiple such sets of implicitly created objects would give the program defined behavior, it is unspecified which such set of objects is created. In other words, implicitly created objects are not required to be uniquely defined.
After implicitly creating objects within a specified region of storage, some operations produce a pointer to a ''suitable created object''. The suitable created object has the same address as the region of storage. Likewise, the behavior is undefined if only if no such pointer value can give the program defined behavior, and it is unspecified which pointer value is produced if there are multiple values giving the program defined behavior.

```cpp
#include <cstdlib>

struct X { int a, b; };

X* MakeX()
{
    // One of possible defined behaviors:
    // the call to std::malloc implicitly creates an object of type X
    // and its subobjects a and b, and returns a pointer to that X object
    X* p = static_cast<X*>(std::malloc(sizeof(X)));
    p->a = 1;
    p->b = 2;
    return p;
}
```

Call to `std::allocator::allocate` or implicitly defined copy/move special member functions of `union` types can also create objects.

## Object representation and value representation

Some types and objects have ''object representations'' and ''value representations'', they are defined in the table below:


| Entity |
| Object representation |
| Value representation |
| - |
| a complete object type tt | T |
| the sequence of c | N c/core | unsigned char objects taken up by a non-rlp | bit field | bit-field complete object of type tt | T, where c | N is c | sizeof(T) |
| the set of bits in the object representation of tt | T that participate in representing a value of type tt | T |
| - |
| a non-bit-field complete object c | obj of type tt | T |
| the bytes of c | obj corresponding to the object representation of tt | T |
| the bits of c | obj corresponding to the value representation of tt | T |
| - |
| a bit-field object c | bf |
| the sequence of c | N bits taken up by c | bf, where c | N is the width of the bit-field |
| the set of bits in the object representation of c | bf that participate in representing the value of c | bf |

Bits in the object representation of a type or object that are not part of the value representation are ''padding bits''.
For *TriviallyCopyable* types, value representation is a part of the object representation, which means that copying the bytes occupied by the object in the storage is sufficient to produce another object with the same value (except if the object is a potentially-overlapping subobject, or the value is a ''trap representation'' of its type and loading it into the CPU raises a hardware exception, such as SNaN ("signalling not-a-number") floating-point values or NaT ("not-a-thing") integers).
Although most implementations do not allow trap representations, padding bits, or multiple representations for integer types, there are exceptions; for example a value of an integer type on Itanium [https://web.archive.org/web/20170830125905/https://blogs.msdn.microsoft.com/oldnewthing/20040119-00/?p=41003 may be a trap representation].
The reverse is not necessarily true: two objects of a *TriviallyCopyable* type with different object representations may represent the same value. For example, multiple floating-point bit patterns represent the same special value NaN. More commonly, padding bits may be introduced to satisfy `alignment requirements`, `bit-field` sizes, etc.

```cpp
#include <cassert>

struct S
{
    char c;  // 1 byte value
             // 3 bytes of padding bits (assuming alignof(float) == 4)
    float f; // 4 bytes value (assuming sizeof(float) == 4)

    bool operator==(const S& arg) const // value-based equality
    {
        return c == arg.c && f == arg.f;
    }
};

void f()
{
    assert(sizeof(S) == 8);
    S s1 = {'a', 3.14};
    S s2 = s1;
    reinterpret_cast<unsigned char*>(&s1)[2] = 'b'; // modify some padding bits
    assert(s1 == s2); // value did not change
}
```

For the objects of type `char`, `signed char`, `unsigned char`<sup>(since C++20)</sup> , `char8_t` (unless they are oversize `bit-fields`), every bit of the object representation is required to participate in the value representation and each possible bit pattern represents a distinct value (no padding bits, trap bits, or multiple representations allowed).

## Subobjects

An object can have ''subobjects''. These include
* member objects
* base class subobjects
* array elements
An object that is not a subobject of another object is called ''complete object''.
If a complete object, a member subobject, or an array element is of `class type`, its type is considered the ''most derived class'', to distinguish it from the class type of any base class subobject. An object of a most derived class type or of a non-class type is called a ''most derived object''.
For a class,
* its non-static `data members`,
* its non-virtual direct `base classes`, and,
* if the class is not `abstract`, its `virtual base classes`
are called its ''potentially constructed subobjects''.

## Size

A subobject is a ''potentially overlapping subobject'' if it is a base class subobject<sup>(since C++20)</sup>  or a non-static data member declared with the .
An object `obj` can only possibly have zero size if all following conditions are satisfied:
* `obj` is a potentially-overlapping subobject.
* `obj` is of a class type without virtual member functions and virtual base classes.
* `obj` does not have any subobject of nonzero size or unnamed `bit-fields` of nonzero length.
For an object `obj` satisfying all the conditions above:
* If `obj` is a base class subobject of a<sup>(since C++11)</sup>   class type with no non-static data members, it has zero size.
* Otherwise, it is implementation-defined under which circumstances where `obj` has zero size.
See `empty base optimization` for more details.
Any non-bit-field object with nonzero size must occupy one or more bytes of storage, including every byte that is occupied (in full or in part) by any of its subobjects. The storage occupied must be contiguous if the object is of trivially copyable<sup>(since C++11)</sup>  or standard-layout type.

## Address

Unless an object is a bit-field or a subobject of zero size, the ''address'' of that object is the address of the first  it occupies.
An object can contain other objects, in which case the contained objects are ''nested within'' the former object. An object `a` is nested within another object `b` if any of the following conditions is satisfied:
* `a` is a subobject of `b`.
* `b` `provides storage` for `a`.
* There exists an object `c` where `a` is nested within `c`, and `c` is nested within `b`.
An object is a ''potentially non-unique object'' if it is one of the following objects:
* A `string literal` object.
rrev|since=c++11|
* The `backing array` of an initializer list.
rrev|since=c++26|
* A template parameter object of array type (see `cpp/meta/reflect_constant_string|std::meta::reflect_constant_string` and `cpp/meta/reflect_constant_array|std::meta::reflect_constant_array`).
* A subobject of a potentially non-unique object.
For any two non-bit-field objects with overlapping `lifetime`s:
* If any of the following conditions is satisfied, they may have the same address:
:* One of them is nested within the other.
:* Any of them is a subobject of zero size, and their types are not `similar`.
:* They are both potentially non-unique objects.
* Otherwise, they always have distinct addresses and occupy disjoint bytes of storage.

```cpp
// character literals are always unique
static const char test1 = 'x';
static const char test2 = 'x';
const bool b = &test1 != &test2;      // always true

// the character 'x' accessed from “r”, “s” and “il”
// may have the same address (i.e., these objects may share storage)
static const char (&r) [] = "x";
static const char *s = "x";
static std::initializer_list<char> il = {'x'};
const bool b2 = r != il.begin();      // unspecified result
const bool b3 = r != s;               // unspecified result
const bool b4 = il.begin() != &test1; // always true
const bool b5 = r != &test1;          // always true
```


## Polymorphic objects

Objects of a class type that declares or inherits at least one virtual function are polymorphic objects. Within each polymorphic object, the implementation stores additional information (in every existing implementation, it is one pointer unless optimized out), which is used by `virtual function` calls and by the RTTI features (`dynamic_cast` and `typeid`) to determine, at run time, the type with which the object was created, regardless of the expression it is used in.
For non-polymorphic objects, the interpretation of the value is determined from the expression in which the object is used, and is decided at compile time.

### Example

```cpp
#include <iostream>
#include <typeinfo>

struct Base1
{
    // polymorphic type: declares a virtual member
    virtual ~Base1() {}
};

struct Derived1 : Base1
{
     // polymorphic type: inherits a virtual member
};

struct Base2
{
     // non-polymorphic type
};

struct Derived2 : Base2
{
     // non-polymorphic type
};

int main()
{
    Derived1 obj1; // object1 created with type Derived1
    Derived2 obj2; // object2 created with type Derived2

    Base1& b1 = obj1; // b1 refers to the object obj1
    Base2& b2 = obj2; // b2 refers to the object obj2

    std::cout << "Expression type of b1: " << typeid(decltype(b1)).name() << '\n'
              << "Expression type of b2: " << typeid(decltype(b2)).name() << '\n'
              << "Object type of b1: " << typeid(b1).name() << '\n'
              << "Object type of b2: " << typeid(b2).name() << '\n'
              << "Size of b1: " << sizeof b1 << '\n'
              << "Size of b2: " << sizeof b2 << '\n';
}
```


**Output:**
```
Expression type of b1: Base1
Expression type of b2: Base2
Object type of b1: Derived1
Object type of b2: Base2
Size of b1: 8
Size of b2: 1
```


## Strict aliasing

Accessing an object using an expression of a type other than the type with which it was created is undefined behavior in many cases, see `reinterpret_cast` for the list of exceptions and examples.

## Alignment

Every `object type` has the property called ''alignment requirement'', which is a nonnegative integer value (of type `std::size_t`, and always a power of two) representing the number of bytes between successive addresses at which objects of this type can be allocated.
rrev|since=c++11|
The alignment requirement of a type can be queried with `alignof` or `std::alignment_of`. The pointer alignment function `std::align` can be used to obtain a suitably-aligned pointer within some buffer. <sup>(until C++23)</sup> `std::aligned_storage` can be used to obtain suitably-aligned storage.
Each object type imposes its alignment requirement on every object of that type<sup>(since C++11)</sup> ; stricter alignment (with larger alignment requirement) can be requested using `alignas`. Attempting to create an object in storage that does not meet the alignment requirements of the object's type is undefined behavior.
In order to satisfy alignment requirements of all non-static members of a `class`, padding bits may be inserted after some of its members.

### Example


**Output:**
```
alignof(S) = 1
sizeof(S)  = 2
alignof(X) = 4
sizeof(X)  = 8
```

The weakest alignment (the smallest alignment requirement) is the alignment of `char`, `signed char`, and `unsigned char`, which equals `1`; the largest ''fundamental alignment'' of scalar type is implementation-defined<sup>(since C++11)</sup>  and equal to the alignment of `std::max_align_t`.
If a request for a specific extended alignment in a specific context is not supported by an implementation, the program is ill-formed.
rrev|since=c++11|
If a type's alignment is made stricter (larger) than `std::max_align_t`, it is known as a type with ''extended alignment'' requirement. A type whose alignment is extended or a class type whose non-static data member has extended alignment is an ''over-aligned type''.
*Allocator* types are required to handle over-aligned types correctly.
rrev|since=c++11|until=c++20|
It is implementation-defined if <sup>(until C++17)</sup> ``new` expressions and` `std::get_temporary_buffer` support over-aligned types.

## Notes

Objects in C++ have different meaning from objects in [Object-oriented programming|object-oriented programming (OOP)](https://en.wikipedia.org/wiki/Object-oriented programming|object-oriented programming (OOP)):


| Objects in C++ |
| Objects in OOP |
| - |
| can have any object type<br>(see lc | std::is_object) |
| must have a class type |
| - |
| no concept of “instance” |
| have the concept of “instance” (and there are mechanisms like tt | instanceof to detect “instance-of” relationship) |
| - |
| no concept of “interface” |
| have the concept of “interface” (and there are mechanisms like tt | instanceof to detect whether an interface is implemented) |
| - |
| polymorphism needs to be explicitly enabled via virtual members |
| polymorphism is always enabled |

In the defect report `P0593R6`, implicit object creation was considered happening when creating a byte array or invocating an allocation function (which is possibly user-defined and `constexpr`) during constant evaluation. However, such allowance caused indeterminism in constant evaluation which was undesired and uninplementable in some aspects. As a result, `P2747R2` disallowed such implicit object creation in constant evaluation. We intentedly treat such change as a defect report although the whole paper is not.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-633 | C++98 | variables could only be objects | they can also be references |
| cwg-734 | C++98 | it was unspecified whether variables defined<br>in the same scope that are guaranteed to have<br>the same value can have the same address | address is guaranteed to be<br>different if their lifetimes overlap,<br>regardless of their values |
| cwg-1189 | C++98 | two base class subobjects of the same<br>type could have the same address | they always have<br>distinct addresses |
| cwg-1861 | C++98 | for oversize bit-fields of narrow character<br>types, all bits of the object representation<br>still participated in the value representation | allows padding bits |
| cwg-2519 | C++98 | the definition of object representation did not address bit-fields | addresses bit-fields |
| cwg-2719 | C++98 | the behavior of creating an object<br>in misaligned storage was unclear | the behavior is<br>undefined in this case |
| cwg-2753 | C++11 | it was unclear whether a backing array of an<br>initializer list can share storage with a string literal | they can share storage |
| cwg-2795 | C++98 | when determining whether two objects with overlapping<br>lifetimes can have the same address, if any of them is a<br>subobject of zero size, they could have similar distinct types | only allows non-similar types |


## See also

