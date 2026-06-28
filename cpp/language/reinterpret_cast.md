---
title: reinterpret_cast conversion
type: Language
source: https://en.cppreference.com/w/cpp/language/reinterpret_cast
---


# tt|reinterpret_cast

Converts between types by reinterpreting the underlying bit pattern.

## Syntax


**Syntax:**

- `*target-type* **`>(`** *expression* **`)`**`
Returns a value of type *target-type*.

## Explanation

Unlike `static_cast`, but like `const_cast`, the `reinterpret_cast` expression does not compile to any CPU instructions (except when converting between integers and pointers, or between pointers on obscure architectures where pointer representation depends on its type). It is primarily a compile-time directive which instructs the compiler to treat *expression* as if it had the type *target-type*.
Only the following conversions can be done with `reinterpret_cast`, except when such conversions would `cast away constness` (or volatility).
1. An expression of integral, enumeration, pointer, or pointer-to-member type can be converted to its own type. The resulting value is the same as the value of *expression*.
2. A pointer can be converted to any integral type large enough to hold all values of its type (e.g. to `std::uintptr_t`).
3. A value of any integral or enumeration type can be converted to a pointer type. A pointer converted to an integer of sufficient size and back to the same pointer type is guaranteed to have its original value, otherwise the resulting pointer cannot be dereferenced safely (the round-trip conversion in the opposite direction is not guaranteed; the same pointer may have multiple integer representations) The null pointer constant `NULL` or integer zero is not guaranteed to yield the null pointer value of the target type; `static_cast` or `implicit conversion` should be used for this purpose.
rrev|since=c++11|
4. Any value of type `std::nullptr_t`, including `nullptr` can be converted to any integral type as if it were `(void*)0`, but no value, not even `nullptr` can be converted to `std::nullptr_t`: `static_cast` should be used for that purpose.
5. Any object pointer type `T1*` can be converted to another object pointer type `''cv'' T2*`. This is exactly equivalent to  (which implies that if `T2`'s alignment requirement is not stricter than `T1`'s, the value of the pointer does not change and conversion of the resulting pointer back to its original type yields the original value). In any case, the resulting pointer may only be dereferenced safely if the dereferenced value is type-accessible.
6. An <sup>(until C++11)</sup> `lvalue`<sup>(since C++11)</sup> `glvalue` expression of type `T1` can be converted to reference to another type `T2`. The result is that of `*reinterpret_cast<T2*>(p)`, where `p` is a pointer of type “pointer to `T1`” to the object or function designated by *expression*. No temporary is <sup>(since C++17)</sup> materialized or created, no copy is made, no constructors or conversion functions are called. The resulting reference can only be accessed safely if it is type-accessible.
7. Any pointer to function can be converted to a pointer to a different function type. The result is unspecified, but converting such pointer back to pointer to the original function type yields the pointer to the original function. The resulting pointer can only be called safely if its function type is call-compatible with the original function type.
8. On some implementations (in particular, on any POSIX compatible system as required by [https://pubs.opengroup.org/onlinepubs/9699919799/functions/dlsym.html `dlsym`]), a function pointer can be converted to `void*` or any other object pointer, or vice versa. If the implementation supports conversion in both directions, conversion to the original type yields the original value, otherwise the resulting pointer cannot be dereferenced or called safely.
9. The null pointer value of any pointer type can be converted to any other pointer type, resulting in the null pointer value of that type. Note that the null pointer constant `nullptr` or any other value of type `std::nullptr_t` cannot be converted to a pointer with `reinterpret_cast`: implicit conversion or `static_cast` should be used for this purpose.
10. A pointer to member function can be converted to pointer to a different member function of a different type. Conversion back to the original type yields the original value, otherwise the resulting pointer cannot be used safely.
11. A pointer to member object of some class `T1` can be converted to a pointer to another member object of another class `T2`. If `T2`'s alignment is not stricter than `T1`'s, conversion back to the original type `T1` yields the original value, otherwise the resulting pointer cannot be used safely.

## Type aliasing


### Type accessibility

If a type `T_ref` is `similar` to any of the following types, an object of  `T_obj` is ''type-accessible'' through a <sup>(until C++11)</sup> lvalue<sup>(since C++11)</sup> glvalue of type `T_ref`:
* `char`, `unsigned char`<sup>(since C++17)</sup>  or `std::byte`: this permits examination of the  `object representation` of any object as an array of bytes.
* `T_obj`
* the signed or unsigned type corresponding to `T_obj`
If a program attempts to read or modify the stored value of an object through a <sup>(until C++11)</sup> lvalue<sup>(since C++11)</sup> glvalue through which it is not type-accessible, the behavior is undefined.
This rule enables type-based alias analysis, in which a compiler assumes that the value read through a glvalue of one type is not modified by a write to a glvalue of a different type (subject to the exceptions noted above).
Note that many C++ compilers relax this rule, as a non-standard language extension, to allow wrong-type access through the inactive member of a `union` (such access is not undefined in C).

### Call compatibility

If any of the following conditions is satisfied, a type `T_call` is ''call-compatible'' with a function type `T_func`:
* `T_call` is the same type as `T_func`.
rrev|since=c++17|
* `T_func*` can be converted to `T_call*` via a `function pointer conversion`.
If a function is called through an expression whose  is not call-compatible with the type of the called function’s definition, the behavior is undefined.

## Notes

Assuming that alignment requirements are met, a `reinterpret_cast` does not change the `value of a pointer` outside of a few limited cases dealing with `''pointer-interconvertible''` objects:

```cpp
struct S1 { int a; } s1;
struct S2 { int a; private: int b; } s2; // not standard-layout
union U { int a; double b; } u = {0};
int arr[2];

int* p1 = reinterpret_cast<int*>(&s1); // value of p1 is "pointer to s1.a" because
                                       // s1.a and s1 are pointer-interconvertible

int* p2 = reinterpret_cast<int*>(&s2); // value of p2 is unchanged by reinterpret_cast
                                       // and is "pointer to s2". 

int* p3 = reinterpret_cast<int*>(&u);  // value of p3 is "pointer to u.a":
                                       // u.a and u are pointer-interconvertible

double* p4 = reinterpret_cast<double*>(p3); // value of p4 is "pointer to u.b": u.a and
                                            // u.b are pointer-interconvertible because
                                            // both are pointer-interconvertible with u

int* p5 = reinterpret_cast<int*>(&arr); // value of p5 is unchanged by reinterpret_cast
                                        // and is "pointer to arr"
```

Performing a class member access that designates a non-static data member or a non-static member function on a glvalue that does not actually designate an object of the appropriate type - such as one obtained through a `reinterpret_cast` - results in undefined behavior:

```cpp
struct S { int x; };
struct T { int x; int f(); };
struct S1 : S {};    // standard-layout
struct ST : S, T {}; // not standard-layout

S s = {};
auto p = reinterpret_cast<T*>(&s); // value of p is "pointer to s"
auto i = p->x; // class member access expression is undefined behavior;
               // s is not a T object
p->x = 1; // undefined behavior
p->f();   // undefined behavior

S1 s1 = {};
auto p1 = reinterpret_cast<S*>(&s1); // value of p1 is "pointer to the S subobject of s1"
auto i = p1->x; // OK
p1->x = 1;      // OK

ST st = {};
auto p2 = reinterpret_cast<S*>(&st); // value of p2 is "pointer to st"
auto i = p2->x; // undefined behavior
p2->x = 1;      // undefined behavior
```

Many compilers issue "strict aliasing" warnings in such cases, even though technically such constructs run afoul of something other than the paragraph commonly known as the "strict aliasing rule".
The purpose of strict aliasing and related rules is to enable type-based alias analysis, which would be decimated if a program can validly create a situation where two pointers to unrelated types (e.g., an `int*` and a `float*`) could simultaneously exist and both can be used to load or store the same memory (see [https://web.archive.org/web/20201128194944/http://www.open-std.org/pipermail/ub/2016-February/000565.html this email on SG12 reflector]). Thus, any technique that is seemingly capable of creating such a situation necessarily invokes undefined behavior.
When it is needed to interpret the bytes of an object as a value of a different type, `std::memcpy` <sup>(since C++20)</sup> or `cpp/numeric/bit_cast|std::bit_cast` can be used:

```cpp
double d = 0.1;
std::int64_t n;
static_assert(sizeof n == sizeof d);
// n = *reinterpret_cast<std::int64_t*>(&d); // Undefined behavior
std::memcpy(&n, &d, sizeof d);               // OK
n = std::bit_cast<std::int64_t>(d);          // also OK
```

rrev|since=c++11|
If the implementation provides `std::intptr_t` and/or `std::uintptr_t`, then a cast from a pointer to an object type or ''cv'' `void` to these types is always well-defined. However, this is not guaranteed for a function pointer.
In C, aggregate copy and assignment access the aggregate object as a whole. But in C++ such actions are always performed through a member function call, which accesses the individual subobjects rather than the entire object (or, in the case of unions, copies the object representation, i.e., via `unsigned char`).

## Keywords

`cpp/keyword/reinterpret_cast`

## Example


### Example

```cpp
#include <cassert>
#include <cstdint>
#include <iostream>

int f() { return 42; }

int main()
{
    int i = 7;

    // pointer to integer and back
    std::uintptr_t v1 = reinterpret_cast<std::uintptr_t>(&i); // static_cast is an error
    std::cout << "The value of &i is " << std::showbase << std::hex << v1 << '\n';
    int* p1 = reinterpret_cast<int*>(v1);
    assert(p1 == &i);

    // pointer to function to another and back
    void(*fp1)() = reinterpret_cast<void(*)()>(f);
    // fp1(); undefined behavior
    int(*fp2)() = reinterpret_cast<int(*)()>(fp1);
    std::cout << std::dec << fp2() << '\n'; // safe

    // type aliasing through pointer
    char* p2 = reinterpret_cast<char*>(&i);
    std::cout << (p2[0] == '\x7' ? "This system is little-endian\n"
                                 : "This system is big-endian\n");

    // type aliasing through reference
    reinterpret_cast<unsigned int&>(i) = 42;
    std::cout << i << '\n';

    [[maybe_unused]] const int &const_iref = i;
    // int &iref = reinterpret_cast<int&>(
    //     const_iref); // compiler error - can't get rid of const
    // Must use const_cast instead: int &iref = const_cast<int&>(const_iref);
}
```


**Output:**
```
The value of &i is 0x7fff352c3580
42
This system is little-endian
42
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-195 | C++98 | conversion between function pointers<br>and object pointers not allowed | made conditionally-supported |
| cwg-658 | C++98 | the result of pointer conversions was unspecified<br>(except for conversions back to the original type) | specification provided for pointers<br>whose pointed-to types satisfy<br>the alignment requirements |


## References


## See also


| cpp/language/dsc const_cast | (see dedicated page) |
| cpp/language/dsc static_cast | (see dedicated page) |
| cpp/language/dsc dynamic_cast | (see dedicated page) |
| cpp/language/dsc explicit_cast | (see dedicated page) |
| cpp/language/dsc implicit_cast | (see dedicated page) |
| cpp/numeric/dsc bit_cast | (see dedicated page) |

