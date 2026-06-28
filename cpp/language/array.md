---
title: Array declaration
type: Language
source: https://en.cppreference.com/w/cpp/language/array
---


# Array declaration

Declares an object of array type.

## Syntax

An array declaration is any simple declaration whose `declarator` has the form

**Syntax:**

- `sdsc|1=`
- `*noptr-declarator* **`[`***expr* (optional)**`]`** *attr* (optional)`

### Parameters

- `{{spar` - noptr-declarator|any valid *declarator*, but if it begins with `*`, `&`, or `&&`, it has to be surrounded by parentheses (otherwise the whole declarator is treated as a `pointer declarator` or `reference declarator`).
- `{{spar` - expr|<sup>(until C++14)</sup> an `integral constant expression`<sup>(since C++14)</sup> a `converted constant expression of type `std::size_t``, which evaluates to a value greater than zero
- `{{spar` - attr|<sup>(C++11)</sup> list of `attributes`
A declaration of the form `T a[N];`, declares `a` as an array `object` that consists of `N` contiguously allocated objects of type `T`. The elements of an array are numbered `0`, …, `N - 1`, and may be accessed with the `subscript operator []`, as in `a[0]`, …, `a[N - 1]`.
Arrays can be constructed from any `fundamental type` (except `void`), `pointer`s, `pointers to members`, `classes`, `enumerations`, or from other arrays of known bound (in which case the array is said to be multi-dimensional). In other words, only object types except for array types of unknown bound can be element types of array types. Array types of incomplete element type are also incomplete types.
rrev|since=c++11|
The <sup>(since C++20)</sup> possibly `constrained` `auto` specifier can be used as array element type in the declaration of a pointer or reference to array, which deduces the element type from the initializer<sup>(since C++14)</sup>  or the function argument, e.g. `1=auto (*p)[42] = &a;` is valid if `a` is an lvalue of type `int[42]`.
There are no arrays of references or arrays of functions.
Applying `cv-qualifiers` to an array type (through typedef or template type manipulation) applies the qualifiers to the element type, but any array type whose elements are of cv-qualified type is considered to have the same cv-qualification.

```cpp
// a and b have the same const-qualified type "array of 5 const char"

typedef const char CC;
CC a[5] = {};

typedef char CA[5];
const CA b = {};
```

When used with `new[]-expression`, the size of an array may be zero; such an array has no elements:

```cpp
int* p = new int[0]; // accessing p[0] or *p is undefined
delete[] p; // cleanup still required
```


### Assignment

Objects of array type cannot be modified as a whole: even though they are `lvalues` (e.g. an address of array can be taken), they cannot appear on the left hand side of an assignment operator:

```cpp
int a[3] = {1, 2, 3}, b[3] = {4, 5, 6};
int (*p)[3] = &a; // okay: address of a can be taken
a = b;            // error: a is an array

struct { int c[3]; } s1, s2 = {3, 4, 5};
s1 = s2; // okay: implicitly-defined copy assignment operator
         // can assign data members of array type
```


### Array-to-pointer decay

There is an `implicit conversion` from lvalues and rvalues of array type to rvalues of pointer type: it constructs a pointer to the first element of an array. This conversion is used whenever arrays appear in context where arrays are not expected, but pointers are:

### Multidimensional arrays

When the element type of an array is another array, it is said that the array is multidimensional:

```cpp
// array of 2 arrays of 3 int each
int a[2][3] = {{1, 2, 3},  // can be viewed as a 2 × 3 matrix
               {4, 5, 6
```

Note that when array-to-pointer decay is applied, a multidimensional array is converted to a pointer to its first element (e.g., a pointer to its first row or to its first plane): array-to-pointer decay is applied only once.

```cpp
int a[2];            // array of 2 int
int* p1 = a;         // a decays to a pointer to the first element of a

int b[2][3];         // array of 2 arrays of 3 int
// int** p2 = b;     // error: b does not decay to int**
int (*p2)[3] = b;    // b decays to a pointer to the first 3-element row of b

int c[2][3][4];      // array of 2 arrays of 3 arrays of 4 int
// int*** p3 = c;    // error: c does not decay to int***
int (*p3)[3][4] = c; // c decays to a pointer to the first 3 × 4-element plane of c
```


### Arrays of unknown bound

If *expr* is omitted in the declaration of an array, the type declared is "array of unknown bound of T", which is a kind of `incomplete type`, except when used in a declaration with an `aggregate initializer`:

```cpp
extern int x[];      // the type of x is "array of unknown bound of int"
int a[] = {1, 2, 3}; // the type of a is "array of 3 int"
```

Because array elements cannot be arrays of unknown bound, multidimensional arrays cannot have unknown bound in a dimension other than the first:

```cpp
extern int a[][2]; // okay: array of unknown bound of arrays of 2 int
extern int b[2][]; // error: array has incomplete element type
```

If there is a preceding declaration of the entity in the same scope in which the bound was specified, an omitted array bound is taken to be the same as in that earlier declaration, and similarly for the definition of a static data member of a class:

```cpp
extern int x[10];
struct S
{
    static int y[10];
};

int x[];               // OK: bound is 10
int S::y[];            // OK: bound is 10

void f()
{
    extern int x[];
    int i = sizeof(x); // error: incomplete object type
}
```

References and pointers to arrays of unknown bound can be formed, <sup>(until C++20)</sup> but cannot<sup>(since C++20)</sup> and can be initialized or assigned from arrays and pointers to arrays of known bound. Note that in the C programming language, pointers to arrays of unknown bound are compatible with pointers to arrays of known bound and are thus convertible and assignable in both directions.

```cpp
extern int a1[];

int (&r1)[] = a1;  // okay
int (*p1)[] = &a1; // okay
int (*q)[2] = &a1; // error (but okay in C)

int a2[] = {1, 2, 3};
int (&r2)[] = a2;  // okay (since C++20)
int (*p2)[] = &a2; // okay (since C++20)
```

Pointers to arrays of unknown bound cannot participate in `pointer arithmetic` and cannot be used on the left of the `subscript operator`, but can be dereferenced.

### Array rvalues

Although arrays cannot be returned from functions by value and cannot be targets of most cast expressions, array `prvalues` may be formed by using a type alias to construct an array temporary using `brace-initialized functional cast`.
rrev|since=c++17|
Like class prvalues, array prvalues convert to xvalues by `temporary materialization` when evaluated.
Array `xvalues` may be formed directly by accessing an array member of a class rvalue or by using `std::move` or another cast or function call that returns an rvalue reference.
}
|output=
24
24
24
24
24

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-393 | C++98 | a pointer or reference to an array of unknown<br>bound could not be a function parameter | allowed |
| cwg-619 | C++98 | when omitted, the bound of an array could<br>not be inferred from a previous declaration | inference allowed |
| cwg-2099 | C++98 | the bound of an array static data member could<br>not be omitted even if an initializer is provided | omission allowed |


## See also

