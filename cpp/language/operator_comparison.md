---
title: Comparison operators
type: Language
source: https://en.cppreference.com/w/cpp/language/operator_comparison
---


# Comparison operators

Compares the arguments.


| - |
| rowspan="2" | Operator name |
| rowspan="2" | Syntax |
| rowspan="2" | rlp | operators | Over<wbr>load<wbr>able |
| colspan="2" | Prototype examples (for c/core | class T) |
| - |
| Inside class definition |
| Outside class definition |
| - |
| Equal to |
| tt | 1=a == b |
|  |
| c | 1=bool T::operator==(const U& b) const; |
| c | 1=bool operator==(const T& a, const U& b); |
| - |
| Not equal to |
| tt | 1=a != b |
|  |
| c | 1=bool T::operator!=(const U& b) const; |
| c | 1=bool operator!=(const T& a, const U& b); |
| - |
| Less than |
| tt | 1=a < b |
|  |
| c | 1=bool T::operator<(const U& b) const; |
| c | 1=bool operator<(const T& a, const U& b); |
| - |
| Greater than |
| tt | 1=a > b |
|  |
| c | 1=bool T::operator>(const U& b) const; |
| c | 1=bool operator>(const T& a, const U& b); |
| - |
| Less than or equal to |
| tt | 1=a <= b |
|  |
| c | 1=bool T::operator<=(const U& b) const; |
| c | 1=bool operator<=(const T& a, const U& b); |
| - |
| Greater than or equal to |
| tt | 1=a >= b |
|  |
| c | 1=bool T::operator>=(const U& b) const; |
| c | 1=bool operator>=(const T& a, const U& b); |
| - |
| Three-way comparison |
| tt | 1=a<=>b |
|  |
| box | tti | Rc/core | 1=T::operator<=>(const U& b) const;<ref name="R">tti | R is the return type of tt | 1=operator<=> ([[#Three-way comparison | see below]])</ref> |
| box | tti | Rc/core | 1=operator<=>(const T& a, const U& b); |
| - |
| colspan="5" |  |


## Two-way comparison

The two-way comparison operator expressions have the form

#### Relational operators


**Syntax:**

- `**`<`** *rhs*`
- `**`>`** *rhs*`
- `**`<=`** *rhs*`
- `**`>=`** *rhs*`

#### Equality operators


**Syntax:**

- `**`==`** *rhs*`
- `**`!=`** *rhs*`
1. Returns `true` if *lhs* is less than *rhs*, `false` otherwise.
2. Returns `true` if *lhs* is greater than *rhs*, `false` otherwise.
3. Returns `true` if *lhs* is less than or equal to *rhs*, `false` otherwise.
4. Returns `true` if *lhs* is greater than or equal to *rhs*, `false` otherwise.
5. Returns `true` if *lhs* is equal to *rhs*, `false` otherwise.
6. Returns `true` if *lhs* is not equal to *rhs*, `false` otherwise.

### Built-in two-way comparison operators

For built-in two-way comparison operators, s<sup>(until C++26)</sup> ,  and s are applied to *lhs* and rhs.
rev|since=c++20|until=c++26|
The comparison is deprecated if both *lhs* and *rhs* have array type prior to the application of these conversions.
rev|since=c++26|
For built-in relational operators, if one of the operands is a pointer, the  is performed on the other operand.
For built-in equality operators, if one of the operands is a pointer or a `null pointer constant`, the array-to-pointer conversion is performed on the other operand.
For built-in two-way comparison operators, the result is a `bool` prvalue.

### Built-in arithmetic comparison

If the converted operands both have arithmetic or enumeration type (scoped or unscoped), `usual arithmetic conversions` are performed on both operands. The values are compared after conversions:

### Example

```cpp
#include <iostream>

int main()
{
    static_assert(sizeof(unsigned char) < sizeof(int),
                  "Cannot compare signed and smaller unsigned properly");
    int a = -1;
    int b = 1;
    unsigned int c = 1;
    unsigned char d = 1;

    std::cout << std::boolalpha
              << "Comparing two signed values:\n"
                 " -1 == 1 ? " << (a == b) << "\n"
                 " -1 <  1 ? " << (a <  b) << "\n"
                 " -1 >  1 ? " << (a >  b) << "\n"
                 "Comparing signed and unsigned:\n"
                 // may issue different-signedness warning:
                 " -1 == 1 ? " << (a == c) << "\n"
                 // may issue different-signedness warning:
                 " -1 <  1 ? " << (a <  c) << "\n"
                 // may issue different-signedness warning:
                 " -1 >  1 ? " << (a >  c) << "\n"
                 "Comparing signed and smaller unsigned:\n"
                 " -1 == 1 ? " << (a == d) << "\n"
                 " -1 <  1 ? " << (a <  d) << "\n"
                 " -1 >  1 ? " << (a >  d) << '\n';
}
```


**Output:**
```
Comparing two signed values:
 -1 == 1 ? false
 -1 <  1 ? true
 -1 >  1 ? false
Comparing signed and unsigned:
 -1 == 1 ? false
 -1 <  1 ? false
 -1 >  1 ? true
Comparing signed and smaller unsigned:
 -1 == 1 ? false
 -1 <  1 ? true
 -1 >  1 ? false
```


### Built-in pointer equality comparison

The converted operands of equality operators `1===` and `1=!=` can also have<sup>(since C++11)</sup>  the type `std::nullptr_t`, pointer type or pointer-to-member type.
Built-in pointer equality comparison has three possible results: equal, unequal and unspecified. The values yielded by equality operators for built-in pointer equality comparison is listed below:


| - |
| rowspan=2 | Comparison result<br>of c | p and c | q |
| colspan=2 | Value yielded by |
| - |
| c | 1=p == q |
| c | 1=p != q |
| - |
| equal |
| tt | true |
| tt | false |
| - |
| unequal |
| tt | false |
| tt | true |
| - |
| unspecified |
| colspan=2 | unspecified c/core | bool value |

If at least one of converted *lhs* and *rhs* is a pointer, <sup>(since C++17)</sup> ,  and  are performed on both converted operands to bring them to their . The two pointers of the composite pointer type are compared as follows:
* If one pointer `represents the address` of a complete object, and another pointer
:* represents the address past the end of a different complete non-array object, or
:* represents the address one past the last element of a different complete array object,
: the result of the comparison is unspecified.
* Otherwise, if the pointers are both null, both point to the same function, or both represent the same address (i.e., they point to or are past the end of the same object), they compare equal.
* Otherwise, the pointers compare unequal.
If at least one of converted *lhs* and *rhs* is a pointer to member, <sup>(since C++17)</sup> ,  and  are performed on both converted operands to bring them to their . The two pointers to members of the composite pointer type are compared as follows:
* If two pointers to members are both the null member pointer value, they compare equal.
* If only one of two pointers to members is the null member pointer value, they compare unequal.
* If either is a pointer to a `virtual member function`, the result is unspecified.
* If one refers to a member of class `C1` and the other refers to a member of a different class `C2`, where neither is a base class of the other, the result is unspecified.
* If both refer to (possibly different) members of the same `union`, they compare equal.
* Otherwise, two pointers to members compare equal if they would refer to the same member of the same `most derived object` or the same subobject if indirection with a hypothetical object of the associated class type were performed, otherwise they compare unequal.

```cpp
struct P {};
struct Q : P { int x; };
struct R : P { int x; };

int P::*bx = (int(P::*)) &Q::x;
int P::*cx = (int(P::*)) &R::x;

bool b1 = (bx == cx); // unspecified

struct B
{
    int f();
};
struct L : B {};
struct R : B {};
struct D : L, R {};

int (B::*pb)() = &B::f;
int (L::*pl)() = pb;
int (R::*pr)() = pb;
int (D::*pdl)() = pl;
int (D::*pdr)() = pr;

bool x = (pdl == pdr); // false
bool y = (pb == pl);   // true
```

rrev|since=c++11|
Two operands of type `std::nullptr_t` or one operand of type `std::nullptr_t` and the other a null pointer constant compare equal.

### Built-in pointer relational comparison

The converted operands of relational operators `>`, `<`, `1=>=` and `1=<=` can also have pointer type.
Built-in pointer relational comparison on unequal pointers `p` and `q` has three possible results: `p` is greater, `q` is greater and unspecified. The values yielded by relational operators for built-in pointer relational comparison is listed below:


| - |
| rowspan=2 | Comparison result<br>of c | p and c | q |
| colspan=4 | Value yielded by |
| - |
| c | p > q |
| c | p < q |
| c | 1=p >= q |
| c | 1=p <= q |
| - |
| equal |
| tt | false |
| tt | false |
| tt | true |
| tt | true |
| - |
| c | p is greater |
| tt | true |
| tt | false |
| tt | true |
| tt | false |
| - |
| c | q is greater |
| tt | false |
| tt | true |
| tt | false |
| tt | true |
| - |
| unspecified |
| colspan=4 | unspecified c/core | bool value |

If converted *lhs* and *rhs* are both pointers, <sup>(since C++17)</sup> ,  and  are performed on both converted operands to bring them to their . The two pointers of the composite pointer type are compared as follows:
* If the pointers compare equal or the equality comparison result is unspecified, the relational comparison result falls into the same category.
* Otherwise (the pointers compare unequal), if any of the pointers is not a pointer to object, the result is unspecified.
* Otherwise (both pointers point to objects), the result is defined in terms of a partial order consistent with the following rules:
:* Given two different elements `high` and `low` of an array such than `high` has higher subscript than `low`, if one pointer points to `high` (or a subobject of `high`) and the other pointer points to `low` (or a subobject of `low`), the former compares greater than the latter.
:* If one pointer points to an element `elem` (or to a subobject of `elem`) of an array, and the other pointer is past the end of the same array, the past-the-end pointer compares greater than the other pointer.
:* If one pointer points to a complete object, a base class subobject or a member subobject `obj` (or to a subobject of `obj`), and the other pointer is past the end of `obj`, the past-the-end pointer compares greater than the other pointer.
:* If the pointers point to different<sup>(since C++20)</sup>  `non-zero-sized` non-static data members<sup>(until C++23)</sup>  with the same `member access` of the same object of a non-union class type, or to subobjects of such members, recursively, the pointer to the later declared member compares greater than the other pointer.
:* Otherwise, the result is unspecified.

### Pointer total order

There exists an ''implementation-defined strict total order over pointers'' in each program. The strict total order is consistent with the partial order described above: unspecified results become implementation-defined, while other results stay the same.
Pointer comparison with the strict total order is applied in the following cases:
* Calling the `operator()` of the pointer type specializations of `std::less`, `std::greater`, `std::less_equal`, and `std::greater_equal`.
rev|since=c++14|
* Calling built-in operators comparing pointers from the `operator()` of specializations `cpp/utility/functional/less_void|std::less<void>`, `cpp/utility/functional/greater_void|std::greater<void>`, `cpp/utility/functional/less_equal_void|std::less_equal<void>`, and `cpp/utility/functional/greater_equal_void|std::greater_equal<void>`.
rev|since=c++20|
* Calling built-in `1=operator<=>` comparing pointers from the `operator()` of `std::compare_three_way`.
* Calling built-in `1=operator==` comparing pointers from the `operator()` of `cpp/utility/functional/ranges/equal_to|std::ranges::equal_to` and `cpp/utility/functional/ranges/not_equal_to|std::ranges::not_equal_to`.
* Calling built-in `operator<` comparing pointers from the `operator()` of `cpp/utility/functional/ranges/less|std::ranges::less`, `cpp/utility/functional/ranges/greater|std::ranges::greater`, `cpp/utility/functional/ranges/less_equal|std::ranges::less_equal`, and `cpp/utility/functional/ranges/greater_equal|std::ranges::greater_equal`.
rrev|since=c++26|

### Built-in reflection comparison

Two values of type `cpp/meta/info|std::meta::info` compare equal if they:
* are null reflection values;
* represent values that are `template-argument-equivalent`;
* represent the same object;
* represent the same entity;
* represent the same annotation;
* represent the same direct base class relationship; or
* represent equal data member descriptions.
Note that a reflection of type or namespace alias compare unequal to a reflection of the aliased type or namespace.

### Overloads

In `overload resolution against user-defined operators`, for every pair of promoted arithmetic types `L` and `R`, including enumeration types, the following function signatures participate in overload resolution:

```cpp
```

For every type `P` which is either pointer to object or pointer to function, the following function signatures participate in overload resolution:

```cpp
```

For every type `MP` that is a pointer to member object or pointer to member function<sup>(since C++11)</sup>  or `std::nullptr_t`<sup>(since C++26)</sup>  or `std::meta::info`, the following function signatures participate in overload resolution:

```cpp
```


### Example

```cpp
#include <iostream>

struct Foo
{
    int n1;
    int n2;
};

union Union
{
    int n;
    double d;
};

int main()
{
    std::cout << std::boolalpha;

    char a[4] = "abc";
    char* p1 = &a[1];
    char* p2 = &a[2];
    std::cout << "Pointers to array elements:\n"
              << "p1 == p2? " << (p1 == p2) << '\n'
              << "p1 <  p2? " << (p1 <  p2) << '\n';

    Foo f;
    int* p3 = &f.n1;
    int* p4 = &f.n2;
    std::cout << "Pointers to members of a class:\n"
              << "p3 == p4? " << (p3 == p4) << '\n'
              << "p3 <  p4? " << (p3 <  p4) << '\n';

    Union u;
    int* p5 = &u.n;
    double* p6 = &u.d;
    std::cout << "Pointers to members of a union:\n"
              << "p5 == (void*)p6? " << (p5 == (void*)p6) << '\n'
              << "p5 <  (void*)p6? " << (p5 <  (void*)p6) << '\n';
}
```


**Output:**
```
Pointers to array elements:
p1 == p2? false
p1 <  p2? true
Pointers to members of a class:
p3 == p4? false
p3 <  p4? true
Pointers to members of a union:
p5 == (void*)p6? true
p5 <  (void*)p6? false
```

rrev|since=c++20|

## Three-way comparison

The three-way comparison operator expressions have the form

**Syntax:**

- `**`<=>`** *b*`
The expression returns an object such that
* `1=(a <=> b) < 0` if `a < b`,
* `1=(a <=> b) > 0` if `a > b`,
* `1=(a <=> b) == 0` if `a` and `b` are equal/equivalent.
If one of the operands is of type `bool` and the other is not, the program is ill-formed.
If both operands have arithmetic types, or if one operand has unscoped enumeration type and the other has integral type, the usual arithmetic conversions are applied to the operands, and then
* If a narrowing conversion is required, other than from an integral type to a floating point type, the program is ill-formed.
* Otherwise, if the operands have integral type, the operator yields a prvalue of type :
:* `std::strong_ordering::equal` if both operands are arithmetically equal,
:* `std::strong_ordering::less` if the first operand is arithmetically less than the second,
:* `std::strong_ordering::greater` otherwise.
* Otherwise, the operands have floating-point type, and the operator yields a prvalue of type . The expression `1=a <=> b` yields
:* `std::partial_ordering::less` if `a` is less than `b`,
:* `std::partial_ordering::greater` if `a` is greater than `b`,
:* `std::partial_ordering::equivalent` if `a` is equivalent to `b` (`1=-0 <=> +0` is equivalent),
:* `std::partial_ordering::unordered` (`1=NaN <=> anything` is unordered).
If both operands have the same enumeration type `E`, the operator yields the result of converting the operands to the underlying type of E and applying `1=<=>` to the converted operands.
If at least one of the operands is a pointer to object or pointer to member, `array-to-pointer conversions`,  and  are applied to both operands to bring them to their .
For converted pointer operands `p` and `q`, `1=p <=> q` returns a prvalue of type `cpp/utility/compare/strong_ordering|std::strong_ordering`:
* `std::strong_ordering::equal` if they compare equal,
* `std::strong_ordering::less` if `q` compares greater than `p`,
* `std::strong_ordering::greater` if `p` compares greater than `q`,
* unspecified result if the two-way comparison result is unspecified.
Otherwise, the program is ill-formed.

### Overloads

In `overload resolution against user-defined operators`, for pointer or enumeration type `T`, the following function signature participates in overload resolution:

```cpp
```

Where `R` is the ordering category type defined above.

### Example

```cpp
#include <compare>
#include <iostream>

int main()
{
    double foo = -0.0;
    double bar = 0.0;

    auto res = foo <=> bar;

    if (res < 0)
        std::cout << "-0 is less than 0";
    else if (res > 0)
        std::cout << "-0 is greater than 0";
    else if (res == 0)
        std::cout << "-0 and 0 are equal";
    else
        std::cout << "-0 and 0 are unordered";
}
```


**Output:**
```
-0 and 0 are equal
```


## Notes

Because comparison operators group left-to-right, the expression `a < b < c` is parsed `(a < b) < c`, and not `a < (b < c)` or `(a < b) && (b < c)`.

### Example

```cpp
#include <iostream>

int main()
{
    int a = 3, b = 2, c = 1;

    std::cout << std::boolalpha
        << (a < b < c) << '\n' // true; maybe warning
        << ((a < b) < c) << '\n' // true
        << (a < (b < c)) << '\n' // false
        << ((a < b) && (b < c)) << '\n'; // false
}
```

A common requirement for `user-defined operator<` is [Strict weak ordering|strict weak ordering](https://en.wikipedia.org/wiki/Strict weak ordering|strict weak ordering). In particular, this is required by the standard algorithms and containers that work with *Compare* types: `std::sort`, `std::max_element`, `std::map`, etc.
The comparison result of pointers to different non-static data members of the same class implies that non-static data members<sup>(until C++23)</sup>  in each of the three `member access modes` are positioned in memory in order of declaration.
Although the results of comparing pointers of random origin (e.g. not all pointing to members of the same array) is unspecified, many implementations provide [Total order#Strict total order|strict total ordering](https://en.wikipedia.org/wiki/Total order#Strict total order|strict total ordering) of pointers, e.g. if they are implemented as addresses within continuous virtual address space. Those implementations that do not (e.g. where not all bits of the pointer are part of a memory address and have to be ignored for comparison, or an additional calculation is required or otherwise pointer and integer is not a 1 to 1 relationship), provide a specialization of `std::less` for pointers that has that guarantee. This makes it possible to use all pointers of random origin as keys in standard associative containers such as `std::set` or `std::map`.
For the types that are both *EqualityComparable* and *LessThanComparable*, the C++ standard library makes a distinction between ''equality'', which is the value of the expression `1=a == b` and ''equivalence'', which is the value of the expression `!(a < b) && !(b < a)`.
Comparison between pointers and null pointer constants was removed by the resolution of  included in :
Three-way comparison can be automatically generated for class types, see `default comparisons`.
If both of the operands are arrays, three-way comparison is ill-formed.

```cpp
unsigned int i = 1;
auto r = -1 < i;    // existing pitfall: returns ‘false’
auto r2 = -1 <=> i; // Error: narrowing conversion required
```


## Standard library

Comparison operators are overloaded for many classes in the standard library.


| cpp/types/type_info/dsc operator cmp | (see dedicated page) |
| cpp/error/error_code/dsc operator cmp | (see dedicated page) |
| cpp/error/error_condition/dsc operator cmp | (see dedicated page) |
| cpp/utility/pair/dsc operator cmp | (see dedicated page) |
| cpp/utility/tuple/dsc operator cmp | (see dedicated page) |
| cpp/utility/bitset/dsc operator cmp | (see dedicated page) |
| cpp/memory/allocator/dsc operator cmp | (see dedicated page) |
| cpp/memory/unique_ptr/dsc operator cmp | (see dedicated page) |
| cpp/memory/shared_ptr/dsc operator cmp | (see dedicated page) |
| cpp/utility/functional/function/dsc operator cmp | (see dedicated page) |
| cpp/chrono/duration/dsc operator cmp | (see dedicated page) |
| cpp/chrono/time_point/dsc operator cmp | (see dedicated page) |
| cpp/memory/scoped_allocator_adaptor/dsc operator cmp | (see dedicated page) |
| cpp/types/type_index/dsc operator cmp | (see dedicated page) |
| cpp/string/basic_string/dsc operator cmp | (see dedicated page) |
| cpp/locale/locale/dsc operator cmp | (see dedicated page) |
| cpp/container/dsc operator cmp|array | (see dedicated page) |
| cpp/container/dsc operator cmp|deque | (see dedicated page) |
| cpp/container/dsc operator cmp|forward_list | (see dedicated page) |
| cpp/container/dsc operator cmp|list | (see dedicated page) |
| cpp/container/dsc operator cmp|vector | (see dedicated page) |
| cpp/container/dsc operator cmp|map | (see dedicated page) |
| cpp/container/dsc operator cmp|multimap | (see dedicated page) |
| cpp/container/dsc operator cmp|set | (see dedicated page) |
| cpp/container/dsc operator cmp|multiset | (see dedicated page) |
| cpp/container/dsc operator cmp_unord|unordered_map | (see dedicated page) |
| cpp/container/dsc operator cmp_unord|unordered_multimap | (see dedicated page) |
| cpp/container/dsc operator cmp_unord|unordered_set | (see dedicated page) |
| cpp/container/dsc operator cmp_unord|unordered_multiset | (see dedicated page) |
| cpp/container/dsc operator cmp|queue | (see dedicated page) |
| cpp/container/dsc operator cmp|stack | (see dedicated page) |
| cpp/iterator/adaptor/dsc operator cmp|reverse_iterator | (see dedicated page) |
| cpp/iterator/adaptor/dsc operator cmp|move_iterator | (see dedicated page) |
| cpp/iterator/istream_iterator/dsc operator cmp | (see dedicated page) |
| cpp/iterator/istreambuf_iterator/dsc operator cmp | (see dedicated page) |
| cpp/numeric/complex/dsc operator cmp | (see dedicated page) |
| cpp/numeric/valarray/dsc operator cmp | (see dedicated page) |
| cpp/numeric/random/engine/dsc operator cmp|linear_congruential_engine | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator cmp|poisson_distribution | (see dedicated page) |
| cpp/regex/sub_match/dsc operator cmp | (see dedicated page) |
| cpp/regex/match_results/dsc operator cmp | (see dedicated page) |
| cpp/regex/regex_iterator/dsc operator cmp | (see dedicated page) |
| cpp/regex/regex_token_iterator/dsc operator cmp | (see dedicated page) |
| cpp/thread/thread/id/dsc operator cmp | (see dedicated page) |

The namespace `cpp/utility/rel_ops/operator cmp|std::rel_ops` provides generic operators `1=!=`, `>`, `1=<=`, and `1=>=`:


| utility | |
| std::rel_ops | |
| cpp/utility/rel_ops/dsc operator cmp | (see dedicated page) |


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1596 | C++98 | non-array objects were considered to belong to arrays with<br>one element only for the purpose of pointer arithmetic | the rule is also<br>applied to comparison |
| cwg-1598 | C++98 | two pointers to members of classes that are different and<br>neither is the base class of the other did not compare equal<br>even if the offsets of the pointed members can be the same | the result is<br>unspecified<br>in this case |
| cwg-1858 | C++98 | it was not clear whether two pointers to members<br>that refer to different members of the same union<br>compare equal as if they refer to the same member | they compare<br>equal in this case |
| cwg-2796 | C++17 | function pointer conversions were not performed on the converted<br>pointer operands during built-in pointer relational comparisons | performs these<br>conversions in this case |


## See also

* `Operator precedence`
* `Operator overloading`
* *Compare* (named requirements)
