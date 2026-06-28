---
title: static_cast conversion
type: Language
source: https://en.cppreference.com/w/cpp/language/static_cast
---


# tt|static_cast

Converts between types using a combination of implicit and user-defined conversions.

## Syntax


**Syntax:**

- `target-type**`>(`**expression**`)`**`
Returns a value of type *target-type*.

## Explanation

Only the following conversions can be done with `static_cast`, except when such conversions would `cast away constness` (or volatility).
1. If *expression* is an lvalue of type “''cv1'' `Base`” and *target-type* is “reference to ''cv2'' `Derived`”, the result refers to the object of type `Derived` enclosing *expression* if all following conditions are satisfied:
* `Derived` is a complete class type.
* `Base` is a base class of `Derived`.
* ''cv1'' is not a greater cv-qualification than ''cv2''.
@@ If any of the following conditions is satisfied, the program is ill-formed:
* `Base` is a `virtual base class` of `Derived`.
* `Base` is a base class of a virtual base class of `Derived`.
* No valid `standard conversion` from “pointer to `Derived`” to “pointer to `Base`” exists.
@@ If *expression* is actually not a base class subobject of an object of type `Derived`, the behavior is undefined.

```cpp
struct B {};
struct D : B { B b; };

D d;
B& br1 = d;
B& br2 = d.b;

static_cast<D&>(br1); // OK, lvalue denoting the original “d” object
static_cast<D&>(br2); // UB: the “b” subobject is not a base class subobject
```

rrev|since=c++11|
2. If *target-type* is “rvalue reference to `Derived`” and *expression* is an xvalue of type “(possibly cv-qualified) `Base`” such that `Base` is a base class of `Derived`, the result and constraints of such a conversion are the same as those of the “`Base` lvalue to `Derived` reference” conversion.
3. If *target-type* is an rvalue reference type and the referenced type is `reference-compatible` with the type of *expression*, `static_cast` converts the value of <sup>(until C++17)</sup> glvalue, class prvalue, or array prvalue<sup>(since C++17)</sup> any lvalue *expression* to xvalue referring to the same object as the expression, or to its base class subobject (depending on *target-type*).
@@ If *target-type* is an inaccessible or ambiguous base of the type of *expression*, the program is ill-formed.
@@ If *expression* is a `bit-field` lvalue, it is first converted to prvalue of the underlying type.
4. If *target-type* is the (possibly cv-qualified) `void`, the conversion has no result. In this case, *expression* is a `discarded-value expression`.
5. Otherwise, *expression* can be explicitly converted to *target-type* if
rev|until=c++17|
the declaration  is well-formed for some invented temporary variable `temp`.
The effect of such an explicit conversion is the same as performing the declaration and initialization and then using `temp` as the result of the conversion. The expression is used as <sup>(until C++11)</sup> an lvalue<sup>(since C++11)</sup> a glvalue if and only if the initialization uses it as <sup>(until C++11)</sup> an lvalue<sup>(since C++11)</sup> a glvalue.
rev|since=c++17|
any of the following conditions is satisfied:
* There is an implicit conversion sequence from *expression* to *target-type*.
* The `overload resolution` for a `direct-initialization` of an object or reference of type *target-type* from *expression* would find at least one viable function.
rrev|since=c++20|
* *target-type* is an `aggregate type` having a first element `x` and there is an implicit conversion sequence from *expression* to the type of `x`.
The explicit conversion is defined as follows:
* If *target-type* is a reference type, the effect is the same as performing the declaration and initialization  for some invented temporary variable `temp` and then using `temp` as the result of the conversion.
* Otherwise, the result object is direct-initialized from expression.
6. Otherwise, if the conversion from *expression* to *target-type* is an inverse of a standard conversion sequence, and the conversion sequence does not contain any of the following conversions, the conversion can be performed by `static_cast`:
*
*
*
* `null pointer conversion`
* `null member pointer conversion`
* `boolean conversion`
rrev|since=c++17|
* `function pointer conversion`
@@ If a program uses `static_cast` to perform the inverse of an ill-formed standard conversion sequence, it is ill-formed.
7. Otherwise, lvalue-to-rvalue, array-to-pointer, and function-to-pointer conversions are applied to *expression*. After these conversions, only the following conversions can be performed by `static_cast`:
rrev|since=c++11|
:@a@ A value of `scoped enumeration` type can be converted to an integer or floating-point type.
rev|until=c++20|
* If *target-type* is (possibly cv-qualified) `bool`, the result is `false` if the original value of *expression* is zero and `true` for all other values.
* If *target-type* is an integral type other than (possibly cv-qualified) `bool`, the value is unchanged if the original value of *expression* can be represented by *target-type*. Otherwise, the resulting value is unspecified.
rev|since=c++20|
* If *target-type* is an integral type, the result is the same as that of converting to the enumeration’s underlying type and then to *target-type*.
* If *target-type* is a floating-point type, the result is the same as that of converting from the original value to *target-type*.
:@b@ A value of integer or enumeration type can be converted to any complete enumeration type.
* If *target-type* has a fixed underlying type, *expression* is first converted to that type by  or `integral conversion`, if necessary, and then to *target-type*.
*  If *target-type* does not have a fixed underlying type, the value of *expression* is unchanged if the original value is `within the range of the enumeration values`, otherwise the behavior is undefined.
:@c@ A value of a floating-point type can also be converted to any complete enumeration type. The result is the same as `converting` the original value of *expression* first to the underlying type of *target-type*, and then to *target-type* itself.
rrev|since=c++23|
:@d@ A prvalue of floating-point type can be explicitly converted to any other floating-point type.
* If the source value of *expression* can be represented exactly in *target-type*, it does not change.
* Otherwise, if the source value of *expression* is between two representable values of *target-type*, the result of the conversion is an implementation-defined choice of either of those values.
* Otherwise, the behavior is undefined.
:@e@ <sup>(until C++11)</sup> An rvalue<sup>(since C++11)</sup> A prvalue of type “pointer to ''cv1'' `Base`” can be explicitly converted to the type “pointer to ''cv2'' `Derived`” if all following conditions are satisfied:
* `Derived` is a complete class type.
* `Base` is a base class of `Derived`.
* ''cv1'' is not a greater cv-qualification than ''cv2''.
:@@ If *expression* is a `null pointer value`, the result is a null pointer value of type *target-type*. Otherwise, the result is a pointer to the object of type `Derived` enclosing the object of type `Base` pointed to by *expression*.
:@@ If any of the following conditions is satisfied, the program is ill-formed:
* `Base` is a `virtual base class` of `Derived`.
* `Base` is a base class of a virtual base class of `Derived`.
* No valid standard conversion from “pointer to `Derived`” to “pointer to `Base`” exists.
:@@ If *expression* is not a null pointer value and does not actually point to a base class subobject of an object of type `Derived`, the behavior is undefined.
:@f@ <sup>(until C++11)</sup> An rvalue<sup>(since C++11)</sup> A prvalue of type “pointer to member of `Derived` of type ''cv1'' `T`” can be explicitly converted to the type “pointer to member of `Base` of type ''cv2'' `T`” if all following conditions are satisfied:
* `Derived` is a complete class type.
* `Base` is a base class of `Derived`.
* ''cv1'' is not a greater cv-qualification than ''cv2''.
:@@ If *expression* is a null member pointer value, the result is a null member pointer value of type *target-type*. Otherwise, the result is a pointer to the original (possibly indirect) member of class `Base`.
:@@ If no valid standard conversion from “pointer to member of `Base` of type `T`” to “pointer to member of `Derived` of type `T`” exists, the program is ill-formed.
:@@ If *expression* is not a null member pointer value and the member it denotes is not a (possibly indirect) member of class `Base`, the behavior is undefined.
:@g@ <sup>(until C++11)</sup> An rvalue<sup>(since C++11)</sup> A prvalue of type “pointer to ''cv1'' `void`” can be explicitly converted to the type “pointer to ''cv2'' `T`” if `T` is an object type and ''cv1'' is not a greater cv-qualification than ''cv2''.
rev|until=c++17|
* If *expression* is a null pointer value, the result is a null pointer value of type *target-type*.
* If the *expression* `represents the address` `A` of a  in memory and `A` satisfies the  requirement of `T`, then the resulting pointer value also represents `A`.
* The result of any other such pointer conversion is unspecified.
* If *expression* the result of a prior conversion from an object of type “pointer to ''cv3'' `T`”, the result has the original value.
rev|since=c++17|
* If *expression* `represents the address` `A` of a  in memory but `A` does not satisfy the  requirement of `T`, then the resulting pointer value is unspecified.
* Otherwise, if *expression* points to an object `a`, and there is an object `b` of type `T` (ignoring cv-qualification) that is pointer-interconvertible (see below) with `a`, the result is a pointer to `b`.
* Otherwise, the pointer value is unchanged by the conversion.

## Pointer-interconvertible objects

Two objects `a` and `b` are ''pointer-interconvertible'' if:
* they are the same object, or
* one is a union object and the other is a non-static data member of that object, or
* one is a  class object and the other is the first non-static data member of that object or any base class subobject of that object, or
* there exists an object `c` such that `a` and `c` are pointer-interconvertible, and `c` and `b` are pointer-interconvertible.

```cpp
union U { int a; double b; } u;
void* x = &u;                        // x's value is “pointer to u”
double* y = static_cast<double*>(x); // y's value is “pointer to u.b”
char* z = static_cast<char*>(x);     // z's value is “pointer to u”
```


## Notes

Base-to-derived conversions (''downcasts'') using `static_cast` make no runtime checks to ensure that the  of the pointed/referred object is `Derived`, and may only be used safely if this precondition is guaranteed by other means, such as when implementing [Curiously recurring template pattern#Static polymorphism|static polymorphism](https://en.wikipedia.org/wiki/Curiously recurring template pattern#Static polymorphism|static polymorphism). Safe downcast may be done with `dynamic_cast`.
`static_cast` may also be used to disambiguate function overloads by performing a function-to-pointer conversion to specific type, as in

```cpp
std::for_each(files.begin(), files.end(),
              static_cast<std::ostream&(*)(std::ostream&)>(std::flush));
```


## Keywords

`cpp/keyword/static_cast`

## Example


### Example

```cpp
#include <iostream>
#include <vector>

struct B
{
    int m = 42;
    const char* hello() const
    {
        return "Hello world, this is B!\n";
    }
};

struct D : B
{
    const char* hello() const
    {
        return "Hello world, this is D!\n";
    }
};

enum class E { ONE = 1, TWO, THREE };
enum EU { ONE = 1, TWO, THREE };

int main()
{
    // 1. static downcast
    D d;
    B& br = d; // upcast via implicit conversion
    std::cout << "1) " << br.hello();
    D& another_d = static_cast<D&>(br); // downcast
    std::cout << "1) " << another_d.hello();

    // 3. lvalue to xvalue
    std::vector<int> v0{1, 2, 3};
    std::vector<int> v2 = static_cast<std::vector<int>&&>(v0);
    std::cout << "3) after move, v0.size() = " << v0.size() << '\n';

    // 4. discarded-value expression
    static_cast<void>(v2.size());

    // 5. initializing conversion
    int n = static_cast<int>(3.14);
    std::cout << "5) n = " << n << '\n';
    std::vector<int> v = static_cast<std::vector<int>>(10);
    std::cout << "5) v.size() = " << v.size() << '\n';

    // 6. inverse of implicit conversion
    void* nv = &n;
    int* ni = static_cast<int*>(nv);
    std::cout << "6) *ni = " << *ni << '\n';

    // 7a. scoped enum to int
    E e = E::TWO;
    int two = static_cast<int>(e);
    std::cout << "7a) " << two << '\n';

    // 7b. int to enum, enum to another enum
    E e2 = static_cast<E>(two);
    [[maybe_unused]]
    EU eu = static_cast<EU>(e2);

    // 7f. pointer to member upcast
    int D::*pm = &D::m;
    std::cout << "7f) " << br.*static_cast<int B::*>(pm) << '\n';

    // 7g. void* to any object pointer
    void* voidp = &e;
    [[maybe_unused]]
    std::vector<int>* p = static_cast<std::vector<int>*>(voidp);
}
```


**Output:**
```
1) Hello world, this is B!
1) Hello world, this is D!
3) after move, v0.size() = 0
5) n = 3
5) v.size() = 10
6) *ni = 3
7a) 2
7f) 42
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-427 | C++98 | downcast might be ambiguous with direct-initialization | selects downcast in this case |
| cwg-1094 | C++98 | the conversion from floating-point values<br>to enumeration values was unspecified | specified |
| cwg-1320 | C++11 | the conversion from scoped enumeration<br>values to bool was unspecified | specified |
| cwg-1447 | C++11 | the conversion from bit-fields to rvalue references<br>was unspecified (cannot bind references to bit-fields) | specified |
| cwg-2224 | C++98 | the conversion from a member of base class type to<br>its complete object of derived class type was valid | the behavior is<br>undefined in this case |
| cwg-2254 | C++11 | a standard-layout class object with no data members<br>was pointer-interconvertible to its first base class | it is pointer-interconvertible<br>to any of its base classes |
| cwg-2284 | C++11 | a non-standard-layout union object and a non-static data<br>member of that object were not pointer-interconvertible | they are |
| cwg-2310 | C++98 | for base-to-derived pointer conversions and<br>derived-to-base pointer-to-member conversions,<br>the derived class type could be incomplete | must be complete |
| cwg-2499 | C++11 | a standard-layout class might have a non-pointer-interconvertible<br>base class, even though all base subobjects have the same address | it does not have |
| cwg-2718 | C++98 | for base-to-derived reference conversions,<br>the derived class type could be incomplete | must be complete |


## References


## See also

* `const_cast`
* `dynamic_cast`
* `reinterpret_cast`
* `explicit cast`
* `implicit conversions`
