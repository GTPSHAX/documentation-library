---
title: const_cast conversion
type: Language
source: https://en.cppreference.com/w/cpp/language/const_cast
---


# tt|const_cast

Converts between types with different cv-qualification.

## Syntax


**Syntax:**

- `*target-type* **`>(`** *expression* **`)`**`
Returns a value of type *target-type*.

## Explanation

Only the following conversions can be done with `const_cast`:
1. For two `similar` object pointer or pointer to data member types `T1` and `T2`, a prvalue of type `T1` can be converted to `T2` if `T1` and `T2` differ only in cv-qualification (formally, if, considering the `qualification-decompositions` of both types, each `P1_i` is the same as `P2_i` for all `i`).
* If *expression* is a null pointer value, the result is also a null pointer value.
* If *expression* is a null member pointer value, the result is also a null member pointer value.
* If *expression* points to an object, the result points to the same object.
* If *expression* points past an object, the result points past the same object.
* If *expression* points to a data member, the result points to the same data member.
rrev|since=c++17|
Even if *expression* is a prvalue,  is not performed.
2. For two s `T1` and `T2`, if a pointer to `T1` can be explicitly converted to the type “pointer to `T2`” using `const_cast<T2*>`, then the following conversions can also be made:
* An lvalue of type `T1` can be explicitly converted to an lvalue of type `T2` using `const_cast<T2&>`.
rrev|since=c++11|
* A glvalue of type `T1` can be explicitly converted to an xvalue of type `T2` using `const_cast<T2&&>`.
* If `T1` is a class or array type, a prvalue of type `T1` can be explicitly converted to an xvalue of type `T2` using `const_cast<T2&&>`.
rev|until=c++17|
The result reference refers to the original object.
rev|since=c++17|
If *expression* is a glvalue, the result reference refers to the original object. Otherwise, the result reference refers to the `materialized temporary`.

## Casting away constness

For two different types `T1` and `T2`, a conversion from `T1` to `T2` ''casts away constness'' if there exists a `qualification-decomposition` of `T2` of the form “cv2_0 P2_0 cv2_1 P2_1 ... cv2_n−1 P2_n−1 cv2_n U2”, and there is no  that converts `T1` to “cv2_0 P1_0 cv2_1 P1_1 ... cv2_n−1 P1_n−1 cv2_n U1” (same cv-components, different P-components and U-components).
If a cast from a prvalue of type `T1*` to the type `T2*` casts away constness, casting from an expression of type `T1` to a reference to `T2` will also cast away constness.
Only `const_cast` may be used to cast away constness.
“Casting away constness” implies “casting away volatility”, as qualification conversions cannot cast away volatility as well.

## Notes

Pointers to functions and pointers to member functions are not subject to `const_cast`.
`const_cast` makes it possible to form a reference or pointer to non-const type that is actually referring to a `const object` or a reference or pointer to non-volatile type that is actually referring to a `volatile object`. Modifying a const object through a non-const access path and referring to a volatile object through a non-volatile  results in undefined behavior.

## Keywords

`cpp/keyword/const_cast`

## Example


### Example

```cpp
#include <iostream>

struct type
{
    int i;

    type(): i(3) {}

    void f(int v) const
    {
        // this->i = v;                 // compile error: this is a pointer to const
        const_cast<type*>(this)->i = v; // OK as long as the type object isn't const
    }
};

int main()
{
    int i = 3;                 // i is not declared const
    const int& rci = i;
    const_cast<int&>(rci) = 4; // OK: modifies i
    std::cout << "i = " << i << '\n';

    type t; // if this was const type t, then t.f(4) would be undefined behavior
    t.f(4);
    std::cout << "type::i = " << t.i << '\n';

    const int j = 3; // j is declared const
    [[maybe_unused]]
    int* pj = const_cast<int*>(&j);
    // *pj = 4;      // undefined behavior

    [[maybe_unused]]
    void (type::* pmf)(int) const = &type::f; // pointer to member function
    // const_cast<void(type::*)(int)>(pmf);   // compile error: const_cast does
                                              // not work on function pointers
}
```


**Output:**
```
i = 4
type::i = 4
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-2879 | C++17 | pointer pvalue operands were materialized | they are not materialized |


## References


## See also

* `static_cast`
* `dynamic_cast`
* `reinterpret_cast`
* `explicit cast`
* `implicit conversions`
