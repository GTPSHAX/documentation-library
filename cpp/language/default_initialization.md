---
title: Default-initialization
type: Language
source: https://en.cppreference.com/w/cpp/language/default_initialization
---


# Default-initialization

This is the initialization performed when an object is constructed with no initializer.

## Syntax


**Syntax:**

- `**`;`**`
- `*T*`

## Explanation

Default-initialization is performed in three situations:
1. when a variable with automatic, static, or thread-local `storage duration` is declared with no initializer;
2. when an object with dynamic storage duration is created by a `new-expression` with no initializer;
3. when a base class or a non-static data member is not mentioned in a `constructor initializer list` and that constructor is called.
The effects of default-initialization are:
* if `T` is a (possibly cv-qualified) <sup>(until C++11)</sup> non-POD class type, the constructors are considered and subjected to `overload resolution` against the empty argument list. The constructor selected (which is one of the `default constructor`s) is called to provide the initial value for the new object;
* if `T` is an array type, every element of the array is default-initialized;
rrev|since=c++26|
* if `T` is `cpp/meta/info|std::meta::info`, the object is initialized to the null reflection value;
* otherwise, no initialization is performed (see notes).
rrev|until=c++11|
Only (possibly cv-qualified) non-POD class types (or arrays thereof) with automatic storage duration were considered to be default-initialized when no initializer is used. Scalars and POD types with dynamic storage duration were considered to be not initialized (since C++11, this situation was reclassified as a form of default-initialization).

## Default-initialization of a const object

If a program calls for the default-initialization of an object of a `const`-qualified type `T`, T must be a ''const-default-constructible'' type.
A type `T` is const-default-constructible if
rev|since=c++26|
* `T` is `cpp/meta/info|std::meta::info`.
rev|since=c++11|
* `T` is `std::nullptr_t`.
* Default-initialization of `T` would invoke a user-provided constructor of `T` <sup>(since C++11)</sup> (not inherited from a base class).
* `T` is a class type such that:
rrev multi|until1=c++11|rev1=
:* each direct non-static data member of `T` is of class type `X` (or array thereof), `X` is const-default-constructible, and
:* `T` has no direct `variant members`, and
:* each `potentially constructed` base class of `T` is const-default-constructible.
|rev2=
:* each direct non-variant non-static data member of `T` has a `default member initializer` or is of const-default-constructible type,
:* if `T` is a union with at least one non-static data member, exactly one `variant member` has a default member initializer,
:* if `T` is not a union, each anonymous union member is const-default-constructible, and
:* each `potentially constructed` base class of `T` is const-default-constructible.
* `T` is an array of const-default-initializable type.

## Indeterminate and erroneous values

rev|until=c++26|
When storage for an object with automatic or dynamic storage duration is obtained, the object has an ''indeterminate value''.
If no initialization is performed for an object, that object retains an indeterminate value until that value is replaced.
rev|since=c++26|
When storage for an object with automatic or dynamic storage duration is obtained, the bytes comprising the storage for the object have the following initial value:
* If the object has dynamic storage duration, or is the object associated with a variable or `function parameter` whose first declaration is marked with , the bytes have ''indeterminate values''.
* Otherwise, the bytes have ''erroneous values'', where each value is determined by the implementation independently of the state of the program.
If no initialization is performed for an object (including ), such a byte retains its initial value until that value is replaced.
* If any bit in the `value representation` has an indeterminate value, the object has an ''indeterminate value''.
* Otherwise, if any bit in the value representation has an erroneous value, the object has an ''erroneous value''.
If an evaluation produces an indeterminate value, the behavior is `undefined`.
rrev|since=c++26|
If an evaluation produces an erroneous value, the behavior is `erroneous`.

### Special cases

The following types are ''uninitialized-friendly'':
rrev|since=c++17|
*
* `unsigned char`
* `char`, if its underlying type is `unsigned char`
Given an indeterminate<sup>(since C++26)</sup>  or erroneous value `value`, the ''uninitialized result value'' of `value` is:
* An indeterminate value, if `value` is also an indeterminate value.
rrev|since=c++26|
* `value`, if `value` is an erroneous value.
If an evaluation produces an indeterminate<sup>(since C++26)</sup>  or erroneous value `value` of an uninitialized-friendly type, the behavior is well-defined if the evaluation is:
* the evaluation of one of the following expressions and operands:
:* The second or third operand of a `conditional expression`.
:* The right operand of a `comma expression`.
:* The operand of an `integral conversion`, `explicit cast` or `static_cast` to an uninitialized-friendly type.
:* A `discarded-value expression`.
: In this case, the result of the operation is the uninitialized result value of `value`.
* an evaluation of the right operand of a `simple assignment operator` whose left operand is an lvalue of an uninitialized-friendly type.
: In this case, the value of the object referred to by the left operand is replaced by the uninitialized result value of `value`.
* the evaluation of the initialization expression when initializing an object of an uninitialized-friendly type.
: In this case, that object is initialized to the uninitialized result value of `value`.
Converting an indeterminate value of an uninitialized-friendly type produces an indeterminate value.
rrev|since=c++26|
Converting an erroneous value of an uninitialized-friendly type produces an erroneous value, the result of the conversion is the value of the converted operand.

```cpp
// Case 1: Uninitialized objects with dynamic storage duration
// All C++ versions: indeterminate value + undefined behavior
int f(bool b)
{
    unsigned char* c = new unsigned char;
    unsigned char d = *c; // OK, “d” has an indeterminate value
    int e = d;            // undefined behavior
    return b ? d : 0;     // undefined behavior if “b” is true
}

// Case 2: Uninitialized objects with automatic storage duration
// until C++26: indeterminate value + undefined behavior
// since C++26: erroneous value + erroneous behavior
int g(bool b)
{
    unsigned char c;     // “c” has an indeterminate/erroneous value

    unsigned char d = c; // no undefined/erroneous behavior,
                         // but “d” has an indeterminate/erroneous value

    assert(c == d);      // holds, but both integral promotions have
                         // undefined/erroneous behavior

    int e = d;           // undefined/erroneous behavior
    return b ? d : 0;    // undefined/erroneous behavior if “b” is true
}

// Same as case 2
void h()
{
    int d1, d2;  // “d1” and “d2” have indeterminate/erroneous values
    int e1 = d1; // undefined/erroneous behavior
    int e2 = d1; // undefined/erroneous behavior

    assert(e1 == e2); // holds
    assert(e1 == d1); // holds, undefined/erroneous behavior
    assert(e2 == d1); // holds, undefined/erroneous behavior

    // no undefined/erroneous behavior,
    // but “d2” has an indeterminate/erroneous value
    std::memcpy(&d2, &d1, sizeof(int));

    assert(e1 == d2); // holds, undefined/erroneous behavior
    assert(e2 == d2); // holds, undefined/erroneous behavior
}
```


## Notes

References and const scalar objects cannot be default-initialized.

## Example


### Example

```cpp
#include <string>

struct T1 { int mem; };

struct T2
{
    int mem;
    T2() {} // “mem” is not in the initializer list
};

int n; // static non-class, a two-phase initialization is done:
       // 1) zero-initialization initializes n to zero
       // 2) default-initialization does nothing, leaving n being zero

int main()
{
    [[maybe_unused]]
    int n;            // non-class, the value is indeterminate
    std::string s;    // class, calls default constructor, the value is ""
    std::string a[2]; // array, default-initializes the elements, the value is {"", ""}
//  int& r;           // Error: a reference
//  const int n;      // Error: a const non-class
//  const T1 t1;      // Error: const class with implicit default constructor
    [[maybe_unused]]
    T1 t1;            // class, calls implicit default constructor
    const T2 t2;      // const class, calls the user-provided default constructor
                      // t2.mem is default-initialized
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-253 | C++98 | default-initialization of a const object could not<br>call an implicitly declared default constructor | allowed if all subobjects are initialized |
| cwg-616 | C++98 | lvalue to rvalue conversion of any<br>uninitialized object was always UB | indeterminate c/core |


## See also

* `converting constructor`
* `default constructor`
* `explicit`
* `initialization`
** `aggregate initialization`
** `constant initialization`
** `copy-initialization`
** `direct-initialization`
** `list-initialization`
** `reference initialization`
** `value-initialization`
** `zero-initialization`
* `new`
