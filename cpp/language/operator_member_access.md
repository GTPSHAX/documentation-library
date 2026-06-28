---
title: Member access operators
type: Language
source: https://en.cppreference.com/w/cpp/language/operator_member_access
---


# Member access operators

Accesses a member of its operand.


| - |
| rowspan="2" | nbsp | 2Operatornamenbsp | 2 |
| rowspan="2" | nbsp | 10Syntaxnbsp | 10 |
| rowspan="2" | rlp | operators | Over<wbr>load<wbr>able |
| colspan="2" | Prototype examples (for c/core | class T) |
| - |
| Inside class definition |
| Outside class definition |
| - |
| rowspan=2 | subscript |
| c | a[b] |
| rowspan=2 |
| c | R& T::operator[](S b); |
| rowspan=2 |
| - |
| c | a[...] <sup>(C++23)</sup> |
| c | R& T::operator[](...); |
| - |
| indirection |
| c | *a |
|  |
| c | 1=R& T::operator*(); |
| c | 1=R& operator*(T a); |
| - |
| address-of |
| c | &a |
|  |
| c | R* T::operator&(); |
| c | R* operator&(T a); |
| - |
| member of object |
| c | a.b |
|  |
|  |
|  |
| - |
| member of pointer |
| c | 1=a->b |
|  |
| c | R* T::operator->(); |
|  |
| - |
| pointer to member of object |
| c | a.*b |
|  |
|  |
|  |
| - |
| pointer to member of pointer |
| c | 1=a->*b |
|  |
| c | R& T::operator->*(S b); |
| c | R& operator->*(T a, S b); |
| - |
| colspan="5" |  |


## Explanation

Built-in ''subscript'' operator provides access to an object pointed-to by the `pointer` or `array` operand.
Built-in ''indirection'' operator provides access to an object or function pointed-to by the pointer operand.
Built-in ''address-of'' operator creates a pointer pointing to the object or function operand.
''Member of object'' and ''pointer to member of object'' operators provide access to a data member or member function of the object operand.
Built-in ''member of pointer'' and ''pointer to member of pointer'' operators provide access to a data member or member function of the class pointed-to by the pointer operand.

### Built-in subscript operator

The subscript operator expressions have the form

**Syntax:**

- `**`[`**expr2**`]`**`
- `**`[{`**expr`, ...`ttb|}]|notes=<sup>(C++11)</sup>`
- `**`[`**expr2`,` expr`, ...`**`]`**|notes=<sup>(C++23)</sup>`
1. For the built-in operator, one of the expressions (either *expr1* or *expr2*) must be a glvalue of type “array of `T`” or a prvalue of type “pointer to `T`”, while the other expression (*expr2* or *expr1*, respectively) must be a prvalue of unscoped enumeration or integral type. The result of this expression has the type `T`. <sup>(since C++23)</sup> *expr2 cannot be an unparenthesized `comma expression`.*
2. The form with brace-enclosed list inside the square brackets is only used to call an overloaded `operator[]`.
3. The form with comma-separated expression list inside the square brackets is only used to call an overloaded `operator[]`.
The built-in subscript expression `E1[E2]` is exactly identical to the expression `*(E1 + E2)` except for its value category (see below) <sup>(since C++17)</sup>  and `evaluation order`: the pointer operand (which may be a result of array-to-pointer conversion, and which must point to an element of some array or one past the end) is adjusted to point to another element of the same array, following the rules of `pointer arithmetic`, and is then dereferenced.
When applied to an array, the subscript expression is an `lvalue`<sup>(since C++11)</sup>  if the array is an lvalue, and an `xvalue if it isn't`.
When applied to a pointer, the subscript expression is always an lvalue.
The type `T` is not allowed to be an `incomplete type`, even if the size or internal structure of `T` is never used, as in `&x[0]`.
rrev multi
|since1=c++20|rev1=
Using an unparenthesized `comma expression` as second (right) argument of a subscript operator is deprecated.
For example, `a[b, c]` is deprecated and `a[(b, c)]` is not.
|since2=c++23|rev2=
An unparenthesized `comma expression` cannot be second (right) argument of a subscript operator. For example, `a[b, c]` is either ill-formed or equivalent to `a.operator[](b, c)`.
Parentheses are needed to for using a comma expression as the subscript, e.g., `a[(b, c)]`.
In `overload resolution against user-defined operators`, for every object type `T` (possibly cv-qualified), the following function signature participates in overload resolution:

```cpp
```


### Example

```cpp
#include <iostream>
#include <map>
#include <string>

int main()
{
    int a[4] = {1, 2, 3, 4};
    int* p = &a[2];
    std::cout << p[1] << p[-1] << 1[p] << (-1)[p] << '\n';

    std::map<std::pair<int, int>, std::string> m;
    m[{1, 2}] = "abc"; // uses the [{...}] version
}
```


**Output:**
```
4242
```


### Built-in indirection operator

The indirection operator expressions have the form

**Syntax:**

- `*expr*`
The operand of the built-in indirection operator must be pointer to object or a pointer to function, and the result is the lvalue referring to the object or function to which *expr* points. If *expr* does not actually points to an object or function, the behavior is undefined (except for the case specified by `typeid`).
A pointer to (possibly `cv`-qualified) `void` cannot be dereferenced. Pointers to other incomplete types can be dereferenced, but the resulting lvalue can only be used in contexts that allow an lvalue of incomplete type, e.g. when initializing a reference.
In `overload resolution against user-defined operators`, for every type `T` that is either object type (possibly cv-qualified) or function type (not const- or ref-qualified), the following function signature participates in overload resolution:

```cpp
```


### Example

```cpp
#include <iostream>

int f() { return 42; }

int main()
{
    int n = 1;
    int* pn = &n;

    int& r = *pn; // lvalue can be bound to a reference
    int m = *pn;  // indirection + lvalue-to-rvalue conversion

    int (*fp)() = &f;
    int (&fr)() = *fp; // function lvalue can be bound to a reference

    [](...){}(r, m, fr); // removes possible "unused variable" warnings
}
```


### Built-in address-of operator

The address-of operator expressions have the form

**Syntax:**

- `*expr*`
- `class**`::`***member*`
- `|**`&`***splice-specifier*`
1. If the operand is an lvalue expression of some object or function type `T`, `operator&` creates and returns a prvalue of type `T*`, with the same cv qualification, that is pointing to the object or function designated by the operand. If the operand has incomplete type, the pointer can be formed, but if that incomplete type happens to be a class that defines its own `operator&`, it is unspecified whether the built-in or the overload is used. For the operands of type with user-defined `operator&`, `std::addressof` may be used to obtain the true pointer.
Note that, unlike C99 and later C versions, there's no special case for the unary operator `&` applied to the result of the unary operator `*`.
rrev|since=c++23|
If *expr* names an `explicit object member function`, *expr* must be a `qualified identifier`. Applying `&` to an unqualified identifier naming an explicit object member function is ill-formed.
2. If the operand is a qualified name of a non-static or `variant` member<sup>(since C++23)</sup>  other than an `explicit object member function`, e.g. `&C::member`, the result is a prvalue `pointer to member function` or `pointer to data member` of type `T` in class `C`. Note that neither `&member` nor `C::member` nor even `&(C::member)` may be used to initialize a pointer to member.
3. If the operand is a `splice specifier`, the result is a pointer to member if it designates a non-static member; otherwise the result is an object pointer or function pointer to the designated object or function. The expression is invalid if an unparenthesized splice specifier designates a member of anonymous union. Note that `&([:r:])` is never a pointer to member.
If the operand designates an overloaded function or function template, the address may be taken only if the overload can be resolved due to context. See `Address of an overloaded function` for details.
In `overload resolution against user-defined operators`, this operator does not introduce any additional function signatures: built-in address-of operator does not apply if there exists an overloaded `operator&` that is a `viable function`.

### Example

```cpp
void f(int) {}
void f(double) {}

struct A { int i; };
struct B { void f(); };

int main()
{
    int n = 1;
    int* pn = &n;    // pointer
    int* pn2 = &*pn; // pn2 == pn

    int A::* mp = &A::i;      // pointer to data member
    void (B::*mpf)() = &B::f; // pointer to member function

    void (*pf)(int) = &f; // overload resolution due to initialization context
//  auto pf2 = &f; // error: ambiguous overloaded function type
    auto pf2 = static_cast<void (*)(int)>(&f); // overload resolution due to cast
}
```


### Built-in member access operators

The member access operator expressions have the form

**Syntax:**

- `**`.`** **`template`** *id-expr*`
- `**`->`** **`template`** *id-expr*`
- `|*expr* **`.`** *splice-specifier*`
- `|*expr* **`->`** *splice-specifier*`
1. The *expr* must be an expression of `complete` class type `T`, unless *id-expr* names a pseudo-destructor (see below).
@@ If *id-expr* names a `static member` or `enumerator`, *expr* is a `discarded-value expression`.
2. The *expr* must be an expression of pointer to complete class type `T*`, unless *id-expr* names a pseudo-destructor (see below).
*id-expr* is a name of (formally, an `identifier expression` that names) a member of `T` or of an unambiguous and accessible base class `B` of `T` (e.g. `E1.E2` or `E1->E2`), optionally `qualified` (e.g. `E1.B::E2` or `E1->B::E2`), optionally using ``template` disambiguator` (e.g. `E1.template E2` or `E1->template E2`).
rrev|since=c++26|
*splice-specifier* is a `splice expression` that designates a member of `T` or of an unambiguous and accessible base class `B` of `T`, or a direct base class relationship (i.e. an element of `std::meta::bases_of(^^T, ctx)`).
If a user-defined `operator->` is called, `operator->` is called again on the resulting value, recursively, until an `operator->` is reached that returns a plain pointer. After that, built-in semantics are applied to that pointer.
The expression `E1->E2` is exactly equivalent to `(*E1).E2` for built-in types; that is why the following rules address only `E1.E2`.
In the expression `E1.E2`:
1. If `E2` is a `static data member`:
* If `E2` is of reference type `T&` <sup>(since C++11)</sup> or `T&&`, the result is an lvalue of type `T` designating the object or function to which the reference is bound.
* Otherwise, given the type of `E2` as `T`, the result is an lvalue of type `T` designating that static data member.
@@ Essentially, `E1` is evaluated and discarded in both cases.
2. If `E2` is a `non-static data member`:
* If `E2` is of reference type `T&` <sup>(since C++11)</sup> or `T&&`, the result is an lvalue of type `T` designating the object or function to which the corresponding reference member of `E1` is bound.
* Otherwise, if `E1` is an lvalue, the result is an lvalue designating that non-static data member of `E1`.
* Otherwise (if `E1` is an <sup>(until C++17)</sup> rvalue<sup>(since C++17)</sup> xvalue (which may be `materialized from prvalue)`), the result is an <sup>(until C++11)</sup> rvalue<sup>(since C++11)</sup> xvalue designating that non-static data member of `E1`.
@@ If `E2` is not a `mutable` member, the `cv-qualification` of the result is the union of the cv-qualifications of `E1` and `E2`, otherwise (if `E2` is a mutable member), it is the union of the volatile-qualifications of `E1` and `E2`.
3. If `E2` is an overload set (of one or more `static member functions` and `non-static member functions`), `E1.E2` must be the (possibly-parenthesized) left-hand operand of a `member function call operator`, and `function overload resolution` is used to select the function to which `E2` refers, after that:
* If `E2` is a `static member function`, the result is an lvalue designating that static member function. Essentially, `E1` is evaluated and discarded in this case.
* Otherwise (`E2` is a `non-static member function`), the result is a prvalue designating that non-static member function of `E1`.
4. If `E2` is a member enumerator, given the type of `E2` as `T`, the result is <sup>(until C++11)</sup> an rvalue<sup>(since C++11)</sup> a prvalue of type `T` whose value is the value of the enumerator.
5. If `E2` is a `nested type`, the program is ill-formed.
rrev|since=c++26|
6. If `E2` designates a direct base class relationship, the result designates the said direct base class subobject of `E1`.

```cpp
struct B { int b; };
struct C : B { int get() const { return b; } };
struct D : B, C {};
constexpr int f() {
    D d = {1, {}<!---->};

    constexpr auto ctx = std::meta::access_context::current();

    // b unambiguously refers to the direct base class of type B,
    // not the indirect base class of type B
    B& b = d.[: std::meta::bases_of(^^D, ctx)[0] :];
    b.b += 10;
    return 10 * b.b + d.get();
}

static_assert(f() == 110);
```

7. If `E1` has a *ScalarType* and `E2` is a **`~`** followed by the `type name` or `decltype specifier` designating the same type (minus cv-qualifications), optionally `qualified`, the result is a special kind of prvalue that can only be used as the left-hand operand of a function call operator, and for no other purpose.
@@ The resulting function call expression is called ''pseudo-destructor call''. It takes no arguments, returns `void`, evaluates `E1`, and ends the lifetime of its result object. This is the only case where the left-hand operand of operator `.` has non-class type. Allowing pseudo-destructor call makes it possible to write code without having to know if a destructor exists for a given type.
`operator.` cannot be overloaded, and for `operator->`, in `overload resolution against user-defined operators`, the built-in operator does not introduce any additional function signatures: built-in `operator->` does not apply if there exists an overloaded `operator->` that is a `viable function`.

### Example

```cpp
#include <cassert>
#include <iostream>
#include <memory>

struct P
{
    template<typename T>
    static T* ptr() { return new T; }
};

template<typename T>
struct A
{
    A(int n): n(n) {}

    int n;
    static int sn;

    int f() { return 10 + n; }
    static int sf() { return 4; }

    class B {};
    enum E {RED = 1, BLUE = 2};

    void g()
    {
        typedef int U;

        // keyword template needed for a dependent template member
        int* p = T().template ptr<U>();
        p->~U(); // U is int, calls int's pseudo destructor
        delete p;
    }
};

template<>
int A<P>::sn = 2;

struct UPtrWrapper
{
    std::unique_ptr<std::string> uPtr;
    std::unique_ptr<std::string>& operator->() { return uPtr; }
};

int main()
{
    A<P> a(1);
    std::cout << a.n << ' '
              << a.sn << ' '   // A::sn also works
              << a.f() << ' ' 
              << a.sf() << ' ' // A::sf() also works
//            << &a.f << ' '   // error: ill-formed if a.f is not the
                               // left-hand operand of operator()
//            << a.B << ' '    // error: nested type not allowed
              << a.RED << ' '; // enumerator

    UPtrWrapper uPtrWrap{std::make_unique<std::string>("wrapped")};
    assert(uPtrWrap->data() == uPtrWrap.operator->().operator->()->data());
}
```


**Output:**
```
1 2 11 4 1
```

If `E2` is a non-static member <sup>(since C++26)</sup> or direct base class relationship and the result of `E1` is an object whose type is not `similar` to the type of `E1`, the behavior is undefined:

```cpp
struct A { int i; };
struct B { int j; };
struct D : A, B {};

void f()
{
    D d;
    static_cast<B&>(d).j;      // OK, object expression designates the B subobject of d
    reinterpret_cast<B&>(d).j; // undefined behavior
}
```


### Built-in pointer-to-member access operators

The member access operator expressions through pointers to members have the form

**Syntax:**

- `**`.*`***rhs*`
- `**`->*`***rhs*`
1. *lhs* must be an expression of class type `T`.
2. *lhs* must be an expression of type pointer to class type `T*`.
*rhs* must be an rvalue of type pointer to member (`data` or `function`) of `T` or pointer to member of an unambiguous and accessible base class `B` of `T`.
The expression `E1->*E2` is exactly equivalent to `(*E1).*E2` for built-in types; that is why the following rules address only `E1.*E2`.
In the expression `E1.*E2`:
1. if `E2` is a pointer to data member,
* if `E1` is an lvalue, the result is an lvalue designating that data member,
* otherwise (if `E1` is an <sup>(until C++17)</sup> rvalue<sup>(since C++17)</sup> xvalue (which may be `materialized from prvalue)`), the result is an <sup>(until C++11)</sup> rvalue<sup>(since C++11)</sup> xvalue designating that data member;
2. if `E2` is a pointer to member function, the result is a special kind of prvalue designating that member function that can only be used as the left-hand operand of a member function call operator, and for no other purpose;
3. cv-qualification rules are the same as for member of object operator, with one additional rule: a pointer to member that refers to a mutable member cannot be used to modify that member in a const object;
4. if `E2` is a null pointer-to-member value, the behavior is undefined;
5. if the result `E1` is an object such that its type is not `similar` to the type of `E1`, or its `most derived object` does not contain the member to which `E2` refers, the behavior is undefined;
6. if `E1` is an rvalue and `E2` points to a member function with ref-qualifier **`&`**, the program is ill-formed <sup>(since C++20)</sup> unless the member function has the cv-qualifier `const` but not `volatile`;
rrev|since=c++11|
7. if `E1` is an lvalue and `E2` points to a member function with ref-qualifier **`&&`**, the program is ill-formed.
In `overload resolution against user-defined operators`, for every combination of types `D`, `B`, `R`, where class type `B` is either the same class as `D` or an unambiguous and accessible base class of `D`, and `R` is either an object or function type, the following function signature participates in overload resolution:

```cpp
```

where both operands may be cv-qualified, in which case the return type's cv-qualification is the union of the cv-qualification of the operands.

### Example

```cpp
#include <iostream>

struct S
{
    S(int n) : mi(n) {}
    mutable int mi;
    int f(int n) { return mi + n; }
};

struct D : public S
{
    D(int n) : S(n) {}
};

int main()
{
    int S::* pmi = &S::mi;
    int (S::* pf)(int) = &S::f;

    const S s(7);
//  s.*pmi = 10; // error: cannot modify through mutable
    std::cout << s.*pmi << '\n';

    D d(7); // base pointers work with derived object
    D* pd = &d;
    std::cout << (d.*pf)(7) << ' '
              << (pd->*pf)(8) << '\n';
}
```


**Output:**
```
7
14 15
```


## Standard library

Subscript operator is overloaded by many standard container classes:


| cpp/utility/bitset/dsc operator at | (see dedicated page) |
| cpp/memory/unique_ptr/dsc operator at | (see dedicated page) |
| cpp/string/basic_string/dsc operator at | (see dedicated page) |
| cpp/container/dsc operator at|array | (see dedicated page) |
| cpp/container/dsc operator at|deque | (see dedicated page) |
| cpp/container/dsc operator at|vector | (see dedicated page) |
| cpp/container/dsc operator at|map | (see dedicated page) |
| cpp/container/dsc operator at|unordered_map | (see dedicated page) |
| cpp/iterator/reverse_iterator/dsc operator at | (see dedicated page) |
| cpp/iterator/adaptor/dsc operator at|move_iterator | (see dedicated page) |
| cpp/numeric/valarray/dsc operator at | (see dedicated page) |
| cpp/regex/match_results/dsc operator at | (see dedicated page) |

The indirection and member operators are overloaded by many iterators and smart pointer classes:


| cpp/memory/unique_ptr/dsc operator* | (see dedicated page) |
| cpp/memory/shared_ptr/dsc operator* | (see dedicated page) |
| cpp/memory/auto_ptr/dsc operator* | (see dedicated page) |
| cpp/memory/raw_storage_iterator/dsc operator* | (see dedicated page) |
| cpp/iterator/reverse_iterator/dsc operator* | (see dedicated page) |
| cpp/iterator/inserter/dsc operator*|back_insert_iterator | (see dedicated page) |
| cpp/iterator/inserter/dsc operator*|front_insert_iterator | (see dedicated page) |
| cpp/iterator/inserter/dsc operator*|insert_iterator | (see dedicated page) |
| cpp/iterator/adaptor/dsc operator*|move_iterator | (see dedicated page) |
| cpp/iterator/istream_iterator/dsc operator* | (see dedicated page) |
| cpp/iterator/ostream_iterator/dsc operator* | (see dedicated page) |
| cpp/iterator/istreambuf_iterator/dsc operator* | (see dedicated page) |
| cpp/iterator/ostreambuf_iterator/dsc operator* | (see dedicated page) |
| cpp/regex/regex_iterator/dsc operator* | (see dedicated page) |
| cpp/regex/regex_token_iterator/dsc operator* | (see dedicated page) |

No standard library classes overload `operator&`. The best known example of overloaded `operator&` is the Microsoft COM class [https://msdn.microsoft.com/en-us/library/31k6d0k7(v=vs.100).aspx `CComPtr`], although it can also appear in EDSLs such as [https://www.boost.org/doc/libs/release/libs/spirit/doc/html/spirit/qi/reference/operator/and_predicate.html boost.spirit].
No standard library classes overload `operator->*`. It was suggested that it could be part of [https://www.aristeia.com/Papers/DDJ_Oct_1999.pdf smart pointer interface], and in fact is used in that capacity by actors in [https://www.boost.org/doc/libs/release/libs/phoenix/doc/html/phoenix/modules/operator.html#phoenix.modules.operator.member_pointer_operator boost.phoenix], but is more common in EDSLs such as [https://github.com/schlangster/cpp.react/blob/master/include/react/Signal.h#L557 cpp.react].

## Notes


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1213 | C++11 | subscripting an array rvalue resulted in  lvalue | reclassified as xvalue |


## See also

`Operator precedence`
`Operator overloading`
