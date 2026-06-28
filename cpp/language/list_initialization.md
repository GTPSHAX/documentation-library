---
title: List-initialization
type: Language
source: https://en.cppreference.com/w/cpp/language/list_initialization
---


# List-initialization mark since c++11

Initializes an object from a `brace-enclosed initializer list`.

## Syntax


### Direct-list-initialization


**Syntax:**

- `sdsc|num=1|`
- `*T object* **`{`** *arg1, arg2, ...* ttb|};`
- `rrev|since=c++20|`
- `*T object***`{.`***des1* **`=`** *arg1* **`, .`***des2* **`{`** *arg2* } *...* ttb|};`
- `sdsc|num=2|`
- `*T* **`{`** *arg1, arg2, ...* }`
- `rrev|since=c++20|`
- `*T* **`{.`***des1* **`=`** *arg1* **`, .`***des2* **`{`** *arg2* } *...* }`
- `sdsc|num=3|`
- `**`new`** *T* **`{`** *arg1, arg2, ...* }`
- `rrev|since=c++20|`
- `**`new`** *T* **`{.`***des1* **`=`** *arg1* **`, .`***des2* **`{`** *arg2* } *...* }`
- `sdsc|num=4|`
- `*Class* **`{`** *T member* **`{`** *arg1, arg2, ...* ttb|}; };`
- `rrev|since=c++20|`
- `*Class* **`{`** *T member* **`{.`***des1* **`=`** *arg1* **`, .`***des2* **`{`** *arg2* } *...* ttb|}; };`
- `sdsc|num=5|`
- `*Class***`::`***Class***`() :`** *member* **`{`** *arg1, arg2, ...* ttb|} {...`
- `rrev|since=c++20|`
- `*Class***`::`***Class***`() :`** *member* **`{.`***des1* **`=`** *arg1* **`, .`***des2* **`{`** *arg2* } *...*ttb|} {...`

### Copy-list-initialization


**Syntax:**

- `sdsc|num=6|`
- `*T object* **`= {`** *arg1, arg2, ...* ttb|};`
- `rrev|since=c++20|`
- `*T object* **`= {.`***des1* **`=`** *arg1* **`, .`***des2* **`{`** *arg2* } *...* ttb|};`
- `sdsc|num=7|`
- `*function* **`({`** *arg1, arg2, ...* ttb|})`
- `rrev|since=c++20|`
- `*function* **`({.`***des1* **`=`** *arg1* **`, .`***des2* **`{`** *arg2* } *...* ttb|})`
- `sdsc|num=8|`
- `**`return {`** *arg1, arg2, ...* ttb|};`
- `rrev|since=c++20|`
- `**`return `****`{.`***des1* **`=`** *arg1* **`, .`***des2* **`{`** *arg2* } *...* ttb|};`
- `sdsc|num=9|`
- `*object* **`[{`** *arg1, arg2, ...* ttb|}]`
- `rrev|since=c++20|`
- `*object* **`[{.`***des1* **`=`** *arg1* **`, .`***des2* **`{`** *arg2* } *...* ttb|}]`
- `sdsc|num=10|`
- `*object* **`= {`** *arg1, arg2, ...* }`
- `rrev|since=c++20|`
- `*object* **`= {.`***des1* **`=`** *arg1* **`, .`***des2* **`{`** *arg2* } *...* }`
- `sdsc|num=11|`
- `*U* **`({`** *arg1, arg2, ...* ttb|})`
- `rrev|since=c++20|`
- `*U* **`({.`***des1* **`=`** *arg1* **`, .`***des2* **`{`** *arg2* } *...* ttb|})`
- `sdsc|num=12|`
- `*Class* **`{`** *T member* **`= {`** *arg1, arg2, ...* ttb|}; };`
- `rrev|since=c++20|`
- `*Class* **`{`** *T member* **`= {.`***des1* **`=`** *arg1* **`, .`***des2* **`{`** *arg2* } *...* ttb|}; };`
List initialization is performed in the following situations:
* direct-list-initialization (both explicit and non-explicit constructors are considered)
1. initialization of a named variable with a brace-enclosed initializer list
2. initialization of an unnamed temporary with a brace-enclosed initializer list
3. initialization of an object with dynamic storage duration with a `new-expression`, where the initializer is a brace-enclosed initializer list
4. in a non-static `data member initializer` that does not use the equals sign
5. in a `member initializer list` of a constructor if a brace-enclosed initializer list is used
* copy-list-initialization (both explicit and non-explicit constructors are considered, but only non-explicit constructors may be called)
6. initialization of a named variable with a brace-enclosed initializer list after an equals sign
7. in a function call expression, with a brace-enclosed initializer list used as an argument and list-initialization initializes the function parameter
8. in a `return` statement with a brace-enclosed initializer list used as the return expression and list-initialization initializes the returned object
9. in a `subscript expression` with a user-defined `operator[]`, where list-initialization initializes the parameter of the overloaded operator
10. in an `assignment expression`, where list-initialization initializes the parameter of the overloaded operator
11. `functional cast expression` or other constructor invocations, where a brace-enclosed initializer list is used in place of a constructor argument. Copy-list-initialization initializes the constructor's parameter (note; the type `U` in this example is not the type that is being list-initialized; `U`'s constructor's parameter is)
12. in a non-static `data member initializer` that uses the equals sign

## Explanation

The effects of list-initialization of an object of type (possibly cv-qualified) `T` are:
rrev|since=c++20|
* If the brace-enclosed initializer list contains a `designated initializer list` and `T` is not a reference type, `T` must be an aggregate class. The ordered identifiers in the designators of the designated initializer list must form a subsequence of the ordered identifiers in the direct non-static data members of `T`. `Aggregate initialization` is performed.
* If `T` is an aggregate class and the brace-enclosed initializer list<sup>(since C++20)</sup> , which does not contain a designated initializer list, has a single initializer clause of the same or derived type (possibly cv-qualified), the object is initialized from that initializer clause (by `copy-initialization` for copy-list-initialization, or by `direct-initialization` for direct-list-initialization).
* Otherwise, if `T` is a character array and the brace-enclosed initializer list has a single initializer clause that is an appropriately-typed string literal, the array is  `initialized from the string literal as usual`.
* Otherwise, if `T` is an `aggregate type`, `aggregate initialization` is performed.
* Otherwise, if the brace-enclosed initializer list is empty and `T` is a class type with a default constructor, `value-initialization` is performed.
* Otherwise, if `T` is a specialization of `std::initializer_list`, the object is initialized as described below.
* Otherwise, if `T` is a class type, the constructors of `T` are considered, in two phases:
:* All constructors that take `std::initializer_list` as the only argument, or as the first argument if the remaining arguments have default values, are examined, and matched by `overload resolution` against a single argument of type `std::initializer_list`.
:* If the previous stage does not produce a match, all constructors of `T` participate in `overload resolution` against the set of arguments that consists of the initializer clauses of the brace-enclosed initializer list, with the restriction that only non-narrowing conversions are allowed. If this stage produces an explicit constructor as the best match for a copy-list-initialization, compilation fails (note, in simple copy-initialization, explicit constructors are not considered at all).
rrev|since=c++17|
* Otherwise, if `T` is an `enumeration type` that with fixed underlying type `U`, the brace-enclosed initializer list has only one initializer `v`, and all following conditions are satisfied, then the enumeration is initialized with the result of converting `v` to `U`:
** The initialization is direct-list-initialization.
** `v` is of scalar type.
** `v` is implicitly convertible to `U`.
** The conversion from `v` to `U` is non-narrowing.
* Otherwise (if `T` is not a class type), if the brace-enclosed initializer list has only one initializer clause and either `T` is not a reference type or is a reference type whose referenced type is same as or is a base class of the type of the initializer clause, `T` is `direct-initialized` (in direct-list-initialization) or `copy-initialized` (in copy-list-initialization), except that narrowing conversions are not allowed.
* Otherwise, if `T` is a reference type that is not compatible with the type of the initializer clause:
rev|until=c++17|
:* a prvalue temporary of the type referenced by `T` is copy-list-initialized, and the reference is bound to that temporary (this fails if the reference is a non-const lvalue reference).
rev|since=c++17|
:* a prvalue is generated. The prvalue initializes its result object by copy-list-initialization. The prvalue is then used to direct-initialize the reference (this fails if the reference is a non-const lvalue reference). The type of the temporary is the type referenced by `T`<sup>(since C++20)</sup> , unless `T` is “reference to array of unknown bound of `U`”, in which case the type of the temporary is the type of `x` in the declaration `U x[] H`, where `H` is the initializer list.
* Otherwise, if the brace-enclosed initializer list has no initializer clause, `T` is `value-initialized`.

## List-initializing `std::initializer_list`

An object of type `std::initializer_list<E>` is constructed from an initializer list as if the compiler generated<sup>(since C++17)</sup>  and `materialized` a `prvalue` of type “array of `N` `const E`”, where `N` is the number of initializer clauses in the initializer list; this is called the initializer list’s ''backing array''.
Each element of the backing array is `copy-initialized` with the corresponding initializer clause of the initializer list, and the `std::initializer_list<E>` object is constructed to refer to that array. A constructor or conversion function selected for the copy is required to be `accessible` in the context of the initializer list. If a narrowing conversion is required to initialize any of the elements, the program is ill-formed.
The backing array has the same lifetime as any other `temporary object`, except that initializing an `std::initializer_list` object from the backing array extends the lifetime of the array exactly like `binding a reference to a temporary`.

```cpp
void f(std::initializer_list<double> il);

void g(float x)
{
   f({1, x, 3});
}

void h()
{
   f({1, 2, 3});
}

struct A { mutable int i; };

void q(std::initializer_list<A>);

void r()
{
    q({A{1}, A{2}, A{3}<!---->});
}

// The initialization above will be implemented in a way roughly equivalent to below,
// assuming that the compiler can construct an initializer_list object with a pair of
// pointers, and with the understanding that `__b` does not outlive the call to `f`.

void g(float x)
{
    const double __a[3] = {double{1}, double{x}, double{3}<!---->}; // backing array
    f(std::initializer_list<double>(__a, __a + 3));
}

void h()
{
    static constexpr double __b[3] =
        {double{1}, double{2}, double{3}<!---->}; // backing array
    f(std::initializer_list<double>(__b, __b + 3));
}

void r()
{
    const A __c[3] = {A{1}, A{2}, A{3}<!---->}; // backing array
    q(std::initializer_list<A>(__c, __c + 3));
}
```

Whether all backing arrays are distinct (that is, are stored in `non-overlapping objects`) is unspecified:

```cpp
bool fun(std::initializer_list<int> il1, std::initializer_list<int> il2)
{
    return il2.begin() == il1.begin() + 1;
}

bool overlapping = fun({1, 2, 3}, {2, 3, 4}); // the result is unspecified:
                                              // the back arrays can share
                                              // storage within {1, 2, 3, 4}
```


## Narrowing conversions

List-initialization limits the allowed `implicit conversion`s by prohibiting the following:
* conversion from a floating-point type to an integer type
* conversion from a floating-point type `T` to another floating-point type whose  is neither greater than nor equal to that of `T`, except where the conversion result is a `constant expression` and one of the following conditions is satisfied:
** The converted value is finite, and the conversion does not overflow.
** The values before and after the conversion are not finite.
* conversion from an integer type to a floating-point type, except where the source is a constant expression whose value can be stored exactly in the target type
* conversion from integer or unscoped enumeration type to integer type that cannot represent all values of the original, except where
** the source is a `bit-field` whose width `w` is less than that of its type (or, for an `enumeration type`, its underlying type) and the target type can represent all the values of a hypothetical extended integer type with width `w` and with the same signedness as the original type, or
** the source is a constant expression whose value can be stored exactly in the target type
* conversion from a pointer type or pointer-to-member type to `bool`

## Notes

Every initializer clause is `sequenced before` any initializer clause that follows it in the brace-enclosed initializer list. This is in contrast with the arguments of a `function call expression`, which are <sup>(until C++17)</sup> `unsequenced`<sup>(since C++17)</sup> `indeterminately sequenced`.
A brace-enclosed initializer list is not an expression and therefore has no type, e.g. } is ill-formed. Having no type implies that template type deduction cannot deduce a type that matches a brace-enclosed initializer list, so given the declaration `template<class T> void f(T);` the expression } is ill-formed. However, the template parameter can otherwise be deduced, as is the case for }, where the iterator type is deduced by the first argument but also used in the second parameter position. A special exception is made for `type deduction using the keyword `auto``, which deduces any brace-enclosed initializer list as `std::initializer_list` in copy-list-initialization.
Also because a brace-enclosed initializer list has no type, `special rules for overload resolution` apply when it is used as an argument to an overloaded function call.
Aggregates copy/move initialize directly from brace-enclosed initializer list of a single initializer clause of the same type, but non-aggregates consider `std::initializer_list` constructors first:

```cpp
struct X {}; // aggregate

struct Q     // non-aggregate
{
    Q() = default;
    Q(Q const&) = default;
    Q(std::initializer_list<Q>) {}
};

int main()
{
    X x;
    X x2 = X{x}; // copy-constructor (not aggregate initialization)

    Q q;
    Q q2 = Q{q}; // initializer-list constructor (not copy constructor)
}
```

Some compilers (e.g., gcc 10) only consider conversion from a pointer or a pointer-to-member to `bool` narrowing in C++20 mode.

## Example


### Example

```cpp
#include <iostream>
#include <map>
#include <string>
#include <vector>

struct Foo
{
    std::vector<int> mem = {1, 2, 3}; // list-initialization of a non-static member
    std::vector<int> mem2;

    Foo() : mem2{-1, -2, -3} {} // list-initialization of a member in constructor
};

std::pair<std::string, std::string> f(std::pair<std::string, std::string> p)
{
    return {p.second, p.first}; // list-initialization in return statement
}

int main()
{
    int n0{};  // value-initialization (to zero)
    int n1{1}; // direct-list-initialization

    std::string s1{'a', 'b', 'c', 'd'}; // initializer-list constructor call
    std::string s2{s1, 2, 2};           // regular constructor call
    std::string s3{0x61, 'a'}; // initializer-list ctor is preferred to (int, char)

    int n2 = {1}; // copy-list-initialization
    double d = double{1.2}; // list-initialization of a prvalue, then copy-init
    auto s4 = std::string{"HelloWorld"}; // same as above, no temporary
                                         // created since C++17

    std::map<int, std::string> m = // nested list-initialization
    {
        {1, "a"},
        {2, {'a', 'b', 'c'}<!---->},
        {3, s1}
    };

    std::cout << f({"hello", "world"}).first // list-initialization in function call
              << '\n';

    const int (&ar)[2] = {1, 2}; // binds an lvalue reference to a temporary array
    int&& r1 = {1}; // binds an rvalue reference to a temporary int
//  int& r2 = {2}; // error: cannot bind rvalue to a non-const lvalue ref

//  int bad{1.0}; // error: narrowing conversion
    unsigned char uc1{10}; // okay
//  unsigned char uc2{-1}; // error: narrowing conversion

    Foo f;

    std::cout << n0 << ' ' << n1 << ' ' << n2 << '\n'
              << s1 << ' ' << s2 << ' ' << s3 << '\n';
    for (auto p : m)
        std::cout << p.first << ' ' << p.second << '\n';
    for (auto n : f.mem)
        std::cout << n << ' ';
    for (auto n : f.mem2)
        std::cout << n << ' ';
    std::cout << '\n';

    [](...){}(d, ar, r1, uc1); // has effect of [[maybe_unused]]
}
```


**Output:**
```
world
0 1 1
abcd cd aa
1 a
2 abc
3 abcd
1 2 3 -1 -2 -3
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1288 | C++11 | list-initializing a reference with a brace-enclosed initializer list of a<br>single initializer clause always bound the reference to a temporary | bind to that initializer<br>clause if valid |
| cwg-1290 | C++11 | the lifetime of the backing array was not correctly specified | specified same as other<br>temporary objects |
| cwg-1467 | C++11 | same-type initialization of aggregates and character<br>arrays was prohibited; initializer-list constructors had<br>priority over copy constructors for single-clause lists | same-type initialization<br>allowed; single-clause<br>lists initialize directly |
| cwg-1494 | C++11 | when list-initializing a reference with an initializer clause of an<br>incompatible type, it was unspecified whether the temporary<br>created is direct-list-initialized or copy-list-initialized | it depends on the<br>kind of initialization<br>for the reference |
| cwg-2252 | C++17 | enumerations could be list-initialized from non-scalar values | prohibited |
| cwg-2374 | C++17 | direct-list-initialization of an enum allowed too many source types | restricted |
| cwg-2627 | C++11 | a narrow bit-field of a larger integer type can be promoted to<br>a smaller integer type, but it was still a narrowing conversion | it is not a<br>narrowing conversion |
| cwg-2713 | C++20 | references to aggregate classes could not<br>be initialized by designated initializer lists | allowed |
| cwg-2830 | C++11 | list-initialization did not ignore the top-level cv-qualification | ignores |
| cwg-2864 | C++11 | floating-point conversions that overflow were not narrowing | they are narrowing |


## See also

* `constructor`
* `converting constructor`
* `copy assignment`
* `copy constructor`
* `copy elision`
* `default constructor`
* `explicit`
* `initialization`
** `aggregate initialization`
** `constant initialization`
** `copy initialization`
** `direct initialization`
** `reference initialization`
** `value initialization`
** `zero initialization`
* `move assignment`
* `move constructor`
* `new`
