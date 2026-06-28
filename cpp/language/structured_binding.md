---
title: Structured binding declaration
type: Language
source: https://en.cppreference.com/w/cpp/language/structured_binding
---


# Structured binding declaration mark since c++17

Binds the specified names to subobjects or elements of the initializer.
Like a reference, a structured binding is an alias to an existing object. Unlike a reference, a structured binding does not have to be of a reference type.

**Syntax:**

- `sdsc|`
- `*attr* (optional) *decl-specifier-seq* *ref-qualifier* (optional) **`[`** *sb-identifier-list* **`]`** initializer**`;`**`

### Parameters

- `{{spar` - attr|sequence of any number of `attributes`
- `{{spar` - decl-specifier-seq|sequence of the following specifiers (following the rules of ):
- rrev|since=c++26|
- * `constexpr`
- * `constinit`
- * `cpp/keyword/static`
- * `cpp/keyword/thread_local`
- * `cpp/keyword/const`
- * `cpp/keyword/volatile` <sup>(deprecated C++20)</sup>
- * `auto`
- `{{spar` - ref-qualifier|either **`&`** or **`&&`**
- `{{spar` - sb-identifier-list|list of comma-separated identifiers introduced by this declaration<sup>(since C++26)</sup> , each identifier may be followed by an `attribute specifier sequence`
- `{{spar` - initializer|an initializer (see below)
*initializer* may be one of the following:

**Syntax:**

- `sdsc|num=1|`
- `**`=`** *expression*`
- `sdsc|num=2|`
- `**`{`** *expression* }`
- `sdsc|num=3|`
- `**`(`** *expression* **`)`**`

### Parameters

- `{{spar` - expression|any expression (except unparenthesized `comma expressions`)
A structured binding declaration introduces all identifiers in the *sb-identifier-list* as names in the surrounding scope and binds them to subobjects or elements of the object denoted by *expression*. The bindings so introduced are called ''structured bindings''.
rrev|since=c++26|
One of the identifiers in the *sb-identifier-list* can be preceded by an ellipsis. Such an identifier introduces a ''structured binding pack''.
The identifier must declare a .
A structured binding is an identifier in the *sb-identifier-list*<sup>(since C++26)</sup>  that is not preceded by an ellipsis, or an element of a structured binding pack introduced in the same identifier list.

## Binding process

A structured binding declaration first introduces a uniquely-named variable (here denoted by `e`) to hold the value of the initializer, as follows:
* If *expression* has array type ''cv1'' `A` and no *ref-qualifier* is present, define `e` as , where *specifiers* is a sequence of the specifiers in *decl-specifier-seq* excluding `auto`.
: Then each element of `e` is initialized from the corresponding element of *expression* as specified by the form of *initializer*:
:* For initializer syntax , the elements are `copy-initialized`.
:* For initializer syntaxes , the elements are `direct-initialized`.
* Otherwise, define `e` as .
We use `E` to denote the type of the identifier expression `e` (i.e., `E` is the equivalent of `std::remove_reference_t<decltype((e))>`).
A ''structured binding size'' of `E` is the number of structured bindings that need to be introduced by the structured binding declaration.
rev|until=c++26|
The number of identifiers in *sb-identifier-list* must be equal to the structured binding size of `E`.
rev|since=c++26|
Given the number of identifiers in *sb-identifier-list* as `N` and the structured binding size of `E` as `S`:
* If there is no structured binding pack, `N` must be equal to `S`.
* Otherwise, the number of non-pack elements (i.e., `N - 1`) must be less than or equal to `S`, and the number of elements of the structured binding pack is `S - N + 1` (which can be zero).

```cpp
struct C { int x, y, z; };

template<class T>
void now_i_know_my() 
{
    auto [a, b, c] = C(); // OK: a, b, c refer to x, y, z, respectively
    auto [d, ...e] = C(); // OK: d refers to x; ...e refers to y and z
    auto [...f, g] = C(); // OK: ...f refers x and y; g refers to z
    auto [h, i, j, ...k] = C();    // OK: the pack k is empty
    auto [l, m, n, o, ...p] = C(); // error: structured binding size is too small
}
```

A structured binding declaration performs the binding in one of three possible ways, depending on `E`:
* Case 1: If `E` is an array type of known bound, then the names are bound to the array elements.
* Case 2: If `E` is a non-union class type and `std::tuple_size<E>` is a complete type with a member named `value` (regardless of the type or accessibility of such member), then the "tuple-like" binding protocol is used.
* Case 3: If `E` is a non-union class type but `std::tuple_size<E>` is not a complete type, then the names are bound to the accessible data members of `E`.
Each of the three cases is described in more detail below.
Each structured binding has a ''referenced type'', defined in the description below. This type is the type returned by `decltype` when applied to an unparenthesized structured binding.

### Case 1: binding an array

Each structured binding in the *sb-identifier-list* becomes the name of an lvalue that refers to the corresponding element of the array. The structured binding size of `E` is equal to the number of array elements.
The ''referenced type'' for each structured binding is the array element type. Note that if the array type `E` is cv-qualified, so is its element type.

```cpp
int a[2] = {1, 2};

auto [x, y] = a;    // creates e[2], copies a into e,
                    // then x refers to e[0], y refers to e[1]
auto& [xr, yr] = a; // xr refers to a[0], yr refers to a[1]
```


### Case 2: binding a type implementing the tuple operations

The expression `std::tuple_size<E>::value` must be a well-formed , and the structured binding size of `E` is equal to `std::tuple_size<E>::value`.
For each structured binding, a variable whose type is "reference to `std::tuple_element<I, E>::type`" is introduced: lvalue reference if its corresponding initializer is an lvalue, rvalue reference otherwise. The initializer for the `I`th variable is
* `e.get<I>()`, if lookup for the identifier `get` in the scope of `E` by class member access lookup finds at least one declaration that is a function template whose first template parameter is a non-type parameter
* Otherwise, `get<I>(e)`, where `get` is looked up by `argument-dependent lookup` only, ignoring non-ADL lookup.
In these initializer expressions, `e` is an lvalue if the type of the entity `e` is an lvalue reference (this only happens if the *ref-qualifier* is **`&`** or if it is **`&&`** and the initializer expression is an lvalue) and an xvalue otherwise (this effectively performs a kind of perfect forwarding), `I` is a `std::size_t` prvalue, and `<I>` is always interpreted as a template parameter list.
The variable has the same `storage duration` as `e`.
The structured binding then becomes the name of an lvalue that refers to the object bound to said variable.
The ''referenced type'' for the `I`th structured binding is `std::tuple_element<I, E>::type`.

```cpp
float x{};
char  y{};
int   z{};

std::tuple<float&, char&&, int> tpl(x, std::move(y), z);
const auto& [a, b, c] = tpl;
// using Tpl = const std::tuple<float&, char&&, int>;
// a names a structured binding that refers to x (initialized from get<0>(tpl))
// decltype(a) is std::tuple_element<0, Tpl>::type, i.e. float&
// b names a structured binding that refers to y (initialized from get<1>(tpl))
// decltype(b) is std::tuple_element<1, Tpl>::type, i.e. char&&
// c names a structured binding that refers to the third component of tpl, get<2>(tpl)
// decltype(c) is std::tuple_element<2, Tpl>::type, i.e. const int
```


### Case 3: binding to data members

Every non-static data member of `E` must be a direct member of `E` or the same base class of `E`, and must be well-formed in the context of the structured binding when named as `e.name`. `E` may not have an anonymous union member. The structured binding size of `E` is equal to the number of non-static data members.
Each structured binding in *sb-identifier-list* becomes the name of an lvalue that refers to the next member of `e` in declaration order (bit-fields are supported); the type of the lvalue is that of `e.mI`, where `mI` refers to the `I`th member.
The ''referenced type'' of the `I`th structured binding is the type of `e.mI` if it is not a reference type, or the declared type of `mI` otherwise.

```cpp
#include <iostream>

struct S
{
    mutable int x1 : 2;
    volatile double y1;
};

S f() { return S{1, 2.3}; }

int main()
{
    const auto [x, y] = f(); // x is an int lvalue identifying the 2-bit bit-field
                             // y is a const volatile double lvalue
    std::cout << x << ' ' << y << '\n';  // 1 2.3
    x = -2;   // OK
//  y = -2.;  // Error: y is const-qualified
    std::cout << x << ' ' << y << '\n';  // -2 2.3
}
|output=
1 2.3
-2 2.3
```


### Initialization order

Let `valI` be the object or reference named by the `I`th structured binding in sb-identifier-list:
* The initialization of `e` is `sequenced before` the initialization of any `valI`.
* The initialization of each `valI` is sequenced before the initialization of any `valJ` where `I` is less than `J`.

## Notes

rrev|since=c++20|
Structured bindings cannot be `constrained`:

```cpp
template<class T>
concept C = true;

C auto [x, y] = std::pair{1, 2}; // error: constrained
```

The lookup for member `get` ignores accessibility as usual and also ignores the exact type of the non-type template parameter. A private `template<char*> void get();` member will cause the member interpretation to be used, even though it is ill-formed.
The portion of the declaration preceding **`[`** applies to the hidden variable `e`, not to the introduced structured bindings:

```cpp
int a = 1, b = 2;
const auto& [x, y] = std::tie(a, b); // x and y are of type int&
auto [z, w] = std::tie(a, b);        // z and w are still of type int&
assert(&z == &a);                    // passes
```

The tuple-like interpretation is always used if `std::tuple_size<E>` is a complete type with a member named `value`, even if that would cause the program to be ill-formed:

```cpp
struct A { int x; };

namespace std
{
    template<>
    struct tuple_size<::A> { void value(); };
}

auto [x] = A{}; // error; the "data member" interpretation is not considered.
```

The usual rules for reference-binding to temporaries (including lifetime-extension) apply if a *ref-qualifier* is present and the *expression* is a prvalue. In those cases the hidden variable `e` is a reference that binds to the temporary variable `materialized` from the prvalue expression, extending its lifetime. As usual, the binding will fail if `e` is a non-const lvalue reference:

```cpp
int a = 1;

const auto& [x] = std::make_tuple(a); // OK, not dangling
auto&       [y] = std::make_tuple(a); // error, cannot bind auto& to rvalue std::tuple
auto&&      [z] = std::make_tuple(a); // also OK
```

`decltype(x)`, where `x` denotes a structured binding, names the ''referenced type'' of that structured binding. In the tuple-like case, this is the type returned by `std::tuple_element`, which may not be a reference even though a hidden reference is always introduced in this case. This effectively emulates the behavior of binding to a struct whose non-static data members have the types returned by `std::tuple_element`, with the referenceness of the binding itself being a mere implementation detail.

```cpp
std::tuple<int, int&> f();

auto [x, y] = f();       // decltype(x) is int
                         // decltype(y) is int&

const auto [z, w] = f(); // decltype(z) is const int
                         // decltype(w) is int&
```

rrev|until=c++20|
Structured bindings cannot be captured by `lambda expressions`:

```cpp
#include <cassert>

int main()
{
    struct S { int p{6}, q{7}; };
    const auto& [b, d] = S{};
    auto l = [b, d] { return b * d; }; // valid since C++20
    assert(l() == 42);
}
```

rrev|since=c++26|
A structured binding size is allowed to be `0` as long as the *sb-identifier-list* contains exactly one identifier that can only introduce an empty structured binding pack.

```cpp
auto return_empty() -> std::tuple<>;

template <class>
void test_empty()
{
    auto [] = return_empty(); // error
    auto [...args] = return_empty(); // OK, args is an empty pack
    auto [one, ...rest] = return_empty(); // error, structured binding size is too small
}
```


## Keywords

`cpp/keyword/auto`

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <set>
#include <string>

int main()
{
    std::set<std::string> myset{"hello"};

    for (int i{2}; i; --i)
    {
        if (auto [iter, success] = myset.insert("Hello"); success) 
            std::cout << "Insert is successful. The value is "
                      << std::quoted(*iter) << ".\n";
        else
            std::cout << "The value " << std::quoted(*iter)
                      << " already exists in the set.\n";
    }

    struct BitFields
    {
        // C++20: default member initializer for bit-fields
        int b : 4 {1}, d : 4 {2}, p : 4 {3}, q : 4 {4};
    };

    {
        const auto [b, d, p, q] = BitFields{};
        std::cout << b << ' ' << d << ' ' << p << ' ' << q << '\n';
    }

    {
        const auto [b, d, p, q] = []{ return BitFields{4, 3, 2, 1}; }();
        std::cout << b << ' ' << d << ' ' << p << ' ' << q << '\n';
    }

    {
        BitFields s;

        auto& [b, d, p, q] = s;
        std::cout << b << ' ' << d << ' ' << p << ' ' << q << '\n';

        b = 4, d = 3, p = 2, q = 1;
        std::cout << s.b << ' ' << s.d << ' ' << s.p << ' ' << s.q << '\n';
    }
}
```


**Output:**
```
Insert is successful. The value is "Hello".
The value "Hello" already exists in the set.
1 2 3 4
4 3 2 1
1 2 3 4
4 3 2 1
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-2313 | C++17 | in case 2, the structure binding variables could be redeclared | cannot be redeclared |
| cwg-2635 | C++20 | structured bindings could be constrained | prohibited |
| cwg-2867 | C++17 | the initialization order was unclear | made clear |


## References


## See also


| cpp/utility/tuple/dsc tie | (see dedicated page) |

