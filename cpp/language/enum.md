---
title: Enumeration declaration
type: Language
source: https://en.cppreference.com/w/cpp/language/enum
---


# Enumeration declaration

An ''enumeration'' is a distinct type whose value is restricted to a range of values (see below for details), which may include several explicitly named constants ("''enumerators''").
The values of the constants are values of an integral type known as the ''underlying type'' of the enumeration. An enumeration has the same `size`, `value representation`, and `alignment requirements` as its underlying type. Furthermore, each value of an enumeration has the same representation as the corresponding value of the underlying type.
An enumeration is (re)declared using the following syntax:

**Syntax:**

- `sdsc|num=1|1=`
- `*enum-key* *attr* (optional) *enum-head-name* (optional) *enum-base* (optional)<br>**`{`** *enumerator-list* (optional) }`
- `sdsc|num=2|1=`
- `*enum-key* *attr* (optional) *enum-head-name* (optional) *enum-base* (optional)<br>**`{`** *enumerator-list* }`
- `|1=`
- `*enum-key* *attr* (optional) *enum-head-name* *enum-base* (optional) **`;`**`
1. *enum-specifier*, which appears in *decl-specifier-seq* of the `declaration` syntax: defines the enumeration type and its enumerators.
2. A trailing comma can follow the *enumerator-list*.
3. Opaque enum declaration: defines the enumeration type but not its enumerators: after this declaration, the type is a complete type and its size is known.

### Parameters

- `{{spar` - enum-key|
- rrev multi|rev1=**`enum`**
- |since2=c++11|rev2=one of **`enum`**, **`enum class`**, or **`enum struct`**
- `{{spar` - attr|<sup>(C++11)</sup> optional sequence of any number of `attributes`
- `{{spar` - enum-head-name|
- rrev multi|rev1=the name of the enumeration that's being declared, it can be omitted.
- `nested-name-specifier}}: sequence of names and scope-resolution operators {{tt` - ::, ending with scope-resolution operator. It can only be omitted in unscoped non-opaque enumeration declarations.<br>
- `nested-name-specifier}} may only appear if the enumeration name is present and this declaration is a redeclaration. For opaque enumeration declarations, {{spar` - nested-name-specifier can only appear before the name of the enumeration in `explicit specialization declarations`.<br>
- `nested-name-specifier}} is present, the ''enum-specifier'' cannot refer to an enumeration  merely inherited or introduced by a {{rlp` - using declaration|`using` declaration, and the ''enum-specifier'' can only appear in a namespace enclosing the previous declaration. In such cases, *nested-name-specifier* cannot begin with a `decltype` specifier.
- `{{spar` - enum-base|<sup>(C++11)</sup> colon (**`:`**), followed by a *type-specifier-seq* that names an integral type (if it is cv-qualified, qualifications are ignored) that will serve as the fixed underlying type for this enumeration type
- `{{spar` - enumerator-list|comma-separated list of enumerator definitions, each of which is either simply a unique *identifier*, which becomes the name of the enumerator, or a unique identifier with a constant expression: *identifier* **` *constant-expression*. <sup>(since C++17)</sup> In either case, the *identifier can be directly followed by an optional `attribute specifier sequence`.*
There are two distinct kinds of enumerations: ''unscoped enumeration'' (declared with the *enum-key* **`enum`**) and ''scoped enumeration'' (declared with the *enum-key* **`enum class`** or **`enum struct`**).

## Unscoped enumerations


**Syntax:**

- `sdsc|num=1|1=`
- `**`enum`** *name* (optional) **`{`** *enumerator* **`=`** *constant-expression* **`,`** *enumerator* **` *constant-expression* **`,`** ... }`
- `|1=`
- `**`enum`** *name* (optional) **`:`** *type* **`{`** *enumerator* **`=`** *constant-expression* **`,`** *enumerator* **`=`** *constant-expression* **`,`** ... }`
- `|1=`
- `**`enum`** *name* **`:`** *type* **`;`**`
1. Declares an unscoped enumeration type whose underlying type is not fixed (in this case, the underlying type is an implementation-defined integral type that can represent all enumerator values; this type is not larger than `int` unless the value of an enumerator cannot fit in an `int` or `unsigned int`. If the *enumerator-list* is empty, the underlying type is as if the enumeration had a single enumerator with value `0`. If no integral type can represent all the enumerator values, the enumeration is ill-formed).
2. Declares an unscoped enumeration type whose underlying type is fixed.
3. Opaque enum declaration for an unscoped enumeration must specify the name and the underlying type.
Each *enumerator* becomes a named constant of the enumeration's type (that is, *name*), visible in the enclosing scope, and can be used whenever constants are required.

```cpp
enum Color { red, green, blue };
Color r = red;

switch(r)
{
    case red  : std::cout << "red\n";   break;
    case green: std::cout << "green\n"; break;
    case blue : std::cout << "blue\n";  break;
}
```

Each enumerator is associated with a value of the underlying type. When **`=`** are provided in an *enumerator-list*, the values of enumerators are defined by those associated *constant-expression*s. If the first enumerator does not have **`=`**, the associated value is zero. For any other enumerator whose definition does not have an **`=`**, the associated value is the value of the previous enumerator plus one.

```cpp
enum Foo { a, b, c = 10, d, e = 1, f, g = f + c };
//a = 0, b = 1, c = 10, d = 11, e = 1, f = 2, g = 12
```

The *name* of an unscoped enumeration may be omitted: such declaration only introduces the enumerators into the enclosing scope:
}
When an unscoped enumeration is a class member, its enumerators may be accessed using class member access operators **`.`** and **`->`**:

```cpp
struct X
{
    enum direction { left = 'l', right = 'r' };
};
X x;
X* p = &x;

int a = X::direction::left; // allowed only in C++11 and later
int b = X::left;
int c = x.left;
int d = p->left;
```

rrev|since=c++11|
In the `declaration specifiers` of a `member declaration`, the sequence
:**`enum`** *enum-head-name* **`:`**
is always parsed as a part of enumeration declaration:

```cpp
struct S
{
    enum E1 : int {};
    enum E1 : int {}; // error: redeclaration of enumeration,
                      // NOT parsed as a zero-length bit-field of type enum E1
};

enum E2 { e1 };

void f()
{
    false ? new enum E2 : int(); // OK: 'int' is NOT parsed as the underlying type
}
```


### Enumeration name for linkage purposes

An unnamed enumeration that does not have a  and that has an enumerator is denoted, for `linkage purposes`, by its underlying type and its first enumerator; such an enumeration is said to have an enumerator as a ''name for linkage purposes''.

## Scoped enumerations

rrev|since=c++11|

**Syntax:**

- `sdsc|num=1|1=`
- `**`enum struct *name* **`{`** *enumerator* **`=`** *constant-expression* **`,`** *enumerator* **`=`** *constant-expression* **`,`** ... }`
- `sdsc|num=2|1=`
- `**`enum struct *name* **`:`** *type* **`{`** *enumerator* **`=`** *constant-expression* **`,`** *enumerator* **`=`** *constant-expression* **`,`** ... }`
- `sdsc|num=3|1=`
- `**`enum struct *name* **`;`**`
- `sdsc|num=4|1=`
- `**`enum struct *name* **`:`** *type* **`;`**`
1. declares a scoped enumeration type whose underlying type is `int` (the keywords `class` and `struct` are exactly equivalent)
2. declares a scoped enumeration type whose underlying type is *type*
3. opaque enum declaration for a scoped enumeration whose underlying type is `int`
4. opaque enum declaration for a scoped enumeration whose underlying type is *type*
Each *enumerator* becomes a named constant of the enumeration's type (that is, *name*), which is contained within the scope of the enumeration, and can be accessed using scope resolution operator. There are no implicit conversions from the values of a scoped enumerator to integral types, although `static_cast` may be used to obtain the numeric value of the enumerator.

### Example

```cpp
#include <iostream>

int main()
{
    enum class Color { red, green = 20, blue };
    Color r = Color::blue;

    switch(r)
    {
        case Color::red  : std::cout << "red\n";   break;
        case Color::green: std::cout << "green\n"; break;
        case Color::blue : std::cout << "blue\n";  break;
    }

    // int n = r; // error: no implicit conversion from scoped enum to int
    int n = static_cast<int>(r); // OK, n = 21
    std::cout << n << '\n'; // prints 21
}
```

rrev|since=c++17|
An enumeration can be initialized from an integer without a cast, using `list initialization`, if all of the following are true:
* The initialization is direct-list-initialization.
* The initializer list has only a single element.
* The enumeration is either scoped or unscoped with underlying type fixed.
* The conversion is non-narrowing.
This makes it possible to introduce new integer types (e.g. `SafeInt`) that enjoy the same existing calling conventions as their underlying integer types, even on ABIs that penalize passing/returning structures by value.

```cpp
enum byte : unsigned char {}; // byte is a new integer type; see also std::byte (C++17)
byte b{42};        // OK as of C++17 (direct-list-initialization)
byte c = {42};     // error
byte d = byte{42}; // OK as of C++17; same value as b
byte e{-1};        // error

struct A { byte b; };
A a1 = {<!---->{42}<!---->};     // error (copy-list-initialization of a constructor parameter)
A a2 = {byte{42}<!---->}; // OK as of C++17

void f(byte);
f({42}); // error (copy-list-initialization of a function parameter)

enum class Handle : std::uint32_t { Invalid = 0 };
Handle h{42}; // OK as of C++17
```

rrev|since=c++20|

## `using enum` declaration


**Syntax:**

- `|`
- `**`using enum`** *using-enum-declarator* **`;`**`

### Parameters

- `{{spar` - declarator|a (possibly qualified) `identifier` or `simple template identifier`<sup>(since C++26)</sup>  or a `splice type specifier` that designates an enumeration type
*declarator* must name a non-`dependent` enumeration type. The enumeration declarations are found by type-only ordinary `qualified` or `unqualified` lookup, depending on whether *declarator* is qualified.

```cpp
enum E { x };

void f()
{
    int E;
    using enum E; // OK
}

using F = E;
using enum F; // OK

template<class T>
using EE = T;

void g()
{
    using enum EE<E>; // OK
}
```

A `using enum` declaration introduces the enumerator names of the named enumeration as if by a ``using` declaration` for each enumerator. When in class scope, a `using enum` declaration adds the enumerators of the named enumeration as members to the scope, making them accessible for member lookup.

```cpp
enum class fruit { orange, apple };

struct S
{
    using enum fruit; // OK: introduces orange and apple into S
};

void f()
{
    S s;
    s.orange;  // OK: names fruit::orange
    S::orange; // OK: names fruit::orange
}
```

Two `using enum` declarations that introduce two enumerators of the same name conflict.

```cpp
enum class fruit { orange, apple };
enum class color { red, orange };

void f()
{
    using enum fruit;    // OK
    // using enum color; // error: color::orange and fruit::orange conflict
}
```


## Notes

Values of unscoped enumeration type can be `promoted` or `converted` to integral types:

```cpp
enum color { red, yellow, green = 20, blue };
color col = red;
int n = blue; // n == 21
```

Values of integer, floating-point, and enumeration types can be converted to any enumeration type by using `static_cast`. Note that the value after such conversion may not necessarily equal any of the named enumerators defined for the enumeration:

```cpp
enum access_t { read = 1, write = 2, exec = 4 }; // enumerators: 1, 2, 4 range: 0..7
access_t rwe = static_cast<access_t>(7);
assert((rwe & read) && (rwe & write) && (rwe & exec));

access_t x = static_cast<access_t>(8.0); // undefined behavior since CWG 1766
access_t y = static_cast<access_t>(8);   // undefined behavior since CWG 1766

enum foo { a = 0, b = UINT_MAX }; // range: [0, UINT_MAX]
foo x = foo(-1); // undefined behavior since CWG 1766,
                 // even if foo's underlying type is unsigned int
```


## Keywords

`cpp/keyword/enum`,
`cpp/keyword/struct`,
`cpp/keyword/class`,
`cpp/keyword/using`

## Example


### Example

```cpp
#include <cstdint>
#include <iostream>

// enum that takes 16 bits
enum smallenum: std::int16_t
{
    a,
    b,
    c
};

// color may be red (value 0), yellow (value 1), green (value 20), or blue (value 21)
enum color
{
    red,
    yellow,
    green = 20,
    blue
};

// altitude may be altitude::high or altitude::low
enum class altitude: char
{
    high = 'h',
    low = 'l', // trailing comma only allowed after CWG 518
}; 

// the constant d is 0, the constant e is 1, the constant f is 3
enum
{
    d,
    e,
    f = e + 2
};

// enumeration types (both scoped and unscoped) can have overloaded operators
std::ostream& operator<<(std::ostream& os, color c)
{
    switch(c)
    {
        case red   : os << "red";    break;
        case yellow: os << "yellow"; break;
        case green : os << "green";  break;
        case blue  : os << "blue";   break;
        default    : os.setstate(std::ios_base::failbit);
    }
    return os;
}

std::ostream& operator<<(std::ostream& os, altitude al)
{
    return os << static_cast<char>(al);
}

// The scoped enum (C++11) can be partially emulated in earlier C++ revisions:

enum struct E11 { x, y }; // since C++11

struct E98 { enum { x, y }; }; // OK in pre-C++11

namespace N98 { enum { x, y }; } // OK in pre-C++11

struct S98 { static const int x = 0, y = 1; }; // OK in pre-C++11

void emu()
{
    std::cout << (static_cast<int>(E11::y) + E98::y + N98::y + S98::y) << '\n'; // 4
}

namespace cxx20
{
    enum class long_long_long_name { x, y };

    void using_enum_demo()
    {
        std::cout << "C++20 `using enum`: __cpp_using_enum == ";
        switch (auto rnd = []{return long_long_long_name::x;}; rnd())
        {
#if defined(__cpp_using_enum)
            using enum long_long_long_name;
            case x: std::cout << __cpp_using_enum << "; x\n"; break;
            case y: std::cout << __cpp_using_enum << "; y\n"; break;
#else
            case long_long_long_name::x: std::cout << "?; x\n"; break;
            case long_long_long_name::y: std::cout << "?; y\n"; break;
#endif
        }
    }
}

int main()
{
    color col = red;
    altitude a;
    a = altitude::low;

    std::cout << "col = " << col << '\n'
              << "a = "   << a   << '\n'
              << "f = "   << f   << '\n';

    cxx20::using_enum_demo();
}
```


**Output:**
```
col = red
a = l
f = 3
C++20 `using enum`: __cpp_using_enum == 201907; x
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-377 | C++98 | the behavior was unspecified when no integral<br>type can represent all the enumerator values | the enumeration is ill-<br>formed in this case |
| cwg-518 | C++98 | a trailing comma was not allowed after the enumerator list | allowed |
| cwg-1514 | C++11 | a redefinition of enumeration with fixed underlying type<br>could be parsed as a bit-field in a class member declaration | always parsed as a redefinition |
| cwg-1638 | C++11 | grammar of opaque enumeration declaration<br>prohibited use for template specializations | nested-name-specifier<br>permitted |
| cwg-1766 | C++98 | casting an out-of-range value to an enumeration<br>without fixed underlying type had an unspecified result | the behavior is undefined |
| cwg-2156 | C++11 | enum definitions could define<br>enumeration types by using-declarations | prohibited |
| cwg-2530 | C++98 | an enumerator list could contain multiple<br>enumerators with the same identifier | prohibited |
| cwg-2590 | C++98 | the size, value representation and alignment requirements<br>of an enumeration did not depend on its underlying type | all of them are identical to<br>those of the underlying type |


## References


## See also


| cpp/types/dsc is_enum | (see dedicated page) |
| cpp/types/dsc is_scoped_enum | (see dedicated page) |
| cpp/types/dsc underlying_type | (see dedicated page) |
| cpp/utility/dsc to_underlying | (see dedicated page) |

