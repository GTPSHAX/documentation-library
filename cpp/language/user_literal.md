---
title: User-defined literals
type: Language
source: https://en.cppreference.com/w/cpp/language/user_literal
---


# User-defined literals mark since c++11

Allows integer, floating-point, character, and string literals to produce objects of user-defined type by defining a user-defined suffix.

## Syntax

A user-defined literal is an expression of any of the following forms

**Syntax:**

- `*ud-suffix*`
- `*ud-suffix*`
- `*ud-suffix*`
- `*ud-suffix*`
- `*exponent-part* (optional) *ud-suffix*`
- `*exponent-part* *ud-suffix*`
- `*ud-suffix*`
- `*ud-suffix*`
@1-4@ user-defined integer literals, such as `12_km`
@5-6@ user-defined floating-point literals, such as `0.5_Pa`
7. user-defined character literal, such as `'c'_X`
8. user-defined string literal, such as `"abd"_L` or `u"xyz"_M`

### Parameters

- `{{spar` - decimal-literal|same as in `integer literal`, a non-zero decimal digit followed by zero or more decimal digits
- `{{spar` - octal-literal|same as in `integer literal`, a zero followed by zero or more octal digits
- `{{spar` - hex-literal|same as in `integer literal`, `0x` or `0X` followed by one or more hexadecimal digits
- `{{spar` - binary-literal|same as in `integer literal`, `0b` or `0B` followed by one or more binary digits
- `{{spar` - digit-sequence|same as in `floating literal`, a sequence of decimal digits
- `{{spar` - fractional-constant|same as in `floating literal`, either a *digit-sequence* followed by a dot (`123.`) or an optional *digit-sequence* followed by a dot and another *digit-sequence* (`1.0` or `.12`)
- `{{spar` - exponent-part|same as in `floating literal`, the letter `e` or the letter `E` followed by optional sign, followed by *digit-sequence*
- `{{spar` - character-literal|same as in `character literal`
- `{{spar` - string-literal|same as in `string literal`, including raw string literals
- `{{spar` - ud-suffix|an identifier, introduced by a ''literal operator'' or a ''literal operator template'' declaration (see below)
rrev|since=c++14|
In the `integer` and `floating-point` digit sequences, optional separators **`'`** are allowed between any two digits.
If a token matches a user-defined literal syntax and a regular literal syntax, it is assumed to be a regular literal (that is, it's impossible to overload `LL` in `123LL`).
When the compiler encounters a user-defined literal with *ud-suffix* `X`, it performs `unqualified name lookup`, looking for a function with the name `operator""X`. If the lookup does not find a declaration, the program is ill-formed. Otherwise,
1. For user-defined integer literals,
:@a@ if the overload set includes a literal operator with the parameter type `unsigned long long`, the user-defined literal expression is treated as a function call , where *n* is the literal without *ud-suffix*;
:@b@ otherwise, the overload set must include either, but not both, a raw literal operator or a numeric literal operator template. If the overload set includes a raw literal operator, the user-defined literal expression is treated as a function call ;
:@c@ otherwise, if the overload set includes a numeric literal operator template, the user-defined literal expression is treated as a function call , where *c1*..*ck* are the individual characters of *n* and all of them are from the `basic character set`.
2. For user-defined floating-point literals,
:@a@ If the overload set includes a literal operator with the parameter type `long double`, the user-defined literal expression is treated as a function call , where *f* is the literal without *ud-suffix*;
:@b@ otherwise, the overload set must include either, but not both, a raw literal operator or a numeric literal operator template. If the overload set includes a raw literal operator, the user-defined literal expression is treated as a function call ;
:@c@ otherwise, if the overload set includes a numeric literal operator template, the user-defined literal expression is treated as a function call , where *c1*..*ck* are the individual characters of *f* and all of them are from the `basic character set`.
3. For user-defined string literals, let `str` be the literal without *ud-suffix*:
rrev|since=c++20|1=
:@a@ If the overload set includes a string literal operator template with a non-type template parameter for which `str` is a well-formed template argument, then the user-defined literal expression is treated as a function call `operator ""X<str>()`;
:@b@ otherwise, the user-defined literal expression is treated as a function call `operator ""X (str, len)`, where `len` is the length of the string literal, excluding the terminating null character.
4. For user-defined character literals, the user-defined literal expression is treated as a function call `operator ""X(ch)`, where `ch` is the literal without *ud-suffix*.

```cpp
long double operator ""_w(long double);
std::string operator ""_w(const char16_t*, size_t);
unsigned    operator ""_w(const char*);

int main()
{
    1.2_w;    // calls operator ""_w(1.2L)
    u"one"_w; // calls operator ""_w(u"one", 3)
    12_w;     // calls operator ""_w("12")
    "two"_w;  // error: no applicable literal operator
}
```

When string literal concatenation takes place in `translation phase 6`, user-defined string literals are concatenated as well, and their *ud-suffix*es are ignored for the purpose of concatenation, except that only one suffix may appear on all concatenated literals:

```cpp
int main()
{
    L"A" "B" "C"_x;  // OK: same as L"ABC"_x
    "P"_x "Q" "R"_y; // error: two different ud-suffixes (_x and _y)
}
```


## Literal operators

The function called by a user-defined literal is known as ''literal operator'' (or, if it's a template, ''literal operator template''). It is declared just like any other `function` or `function template` at namespace scope (it may also be a friend function, an explicit instantiation or specialization of a function template, or introduced by a using-declaration), except for the following restrictions:
The name of this function can have one of the two forms:

**Syntax:**

- `*identifier*|num=1|notes=`
- `*user-defined-string-literal*|num=2`

### Parameters

- `{{spar` - identifier|the `identifier` to use as the *ud-suffix* for the user-defined literals that will call this function
- `{{spar` - user-defined-string-literal|the character sequence **`""`** followed, without a space, by the character sequence that becomes the *ud-suffix*
1. Declares a literal operator.
2. Declares a literal operator. This syntax makes it possible to use language keywords and reserved identifiers as *ud-suffix*es, for example, `operator ""if` from the header .
*ud-suffix* must begin with the underscore **`_`**: the suffixes that do not begin with the underscore are reserved for the literal operators provided by the standard library. It cannot contain double underscores **`__`** as well: such suffixes are also reserved.
If the literal operator is a template, it must have an empty parameter list and can have only one template parameter, which must be a non-type template parameter pack with element type `char` (in which case it is known as a ''numeric literal operator template''):

```cpp
template<char...>
double operator ""_x();
```

rrev|since=c++20|1=
or a non-type template parameter of class type (in which case it is known as a ''string literal operator template''):

```cpp
struct A { constexpr A(const char*); };

template<A a>
A operator ""_a();
```

Only the following parameter lists are allowed on literal operators:

**Syntax:**

- ``const char*` **`)`**`
- ``unsigned long long int` **`)`**`
- ``long double` **`)`**`
- ``char` **`)`**`
- ``wchar_t` **`)`**`
- ``char8_t` **`)`**|notes=<sup>(C++20)</sup>`
- ``char16_t` **`)`**`
- ``char32_t` **`)`**`
- ``const char*`**`,`** `std::size_t` **`)`**`
- ``const wchar_t*`**`,`** `std::size_t` **`)`**`
- ``const char8_t*`**`,`** `std::size_t` **`)`**|notes=<sup>(C++20)</sup>`
- ``const char16_t*`**`,`** `std::size_t` **`)`**`
- ``const char32_t*`**`,`** `std::size_t` **`)`**`
1. Literal operators with this parameter list are the ''raw literal operators'', used as fallbacks for integer and floating-point user-defined literals (see above)
2. Literal operators with these parameter lists are the first-choice literal operator for user-defined integer literals
3. Literal operators with these parameter lists are the first-choice literal operator for user-defined floating-point literals
@4-8@ Literal operators with these parameter lists are called by user-defined character literals
@9-13@ Literal operators with these parameter lists are called by user-defined string literals
`Default arguments` are not allowed.
C `language linkage` is not allowed.
Other than the restrictions above, literal operators and literal operator templates are normal functions (and function templates), they can be declared inline or constexpr, they may have internal or external linkage, they can be called explicitly, their addresses can be taken, etc.

### Example

```cpp
#include <string>

void        operator ""_km(long double); // OK, will be called for 1.0_km
void        operator "" _km(long double); // same as above, deprecated
std::string operator ""_i18n(const char*, std::size_t); // OK

template<char...>
double operator ""_pi(); // OK
float  operator ""_e(const char*); // OK

// error: suffix must begin with underscore
float operator ""Z(const char*);

// error: all names that begin with underscore followed by uppercase
// letter are reserved (NOTE: a space between "" and _).
double operator"" _Z(long double);

// OK. NOTE: no space between "" and _.
double operator""_Z(long double);

// OK: literal operators can be overloaded
double operator ""_Z(const char* args);

int main() {}
```


## Notes

Since the introduction of user-defined literals, the code that uses format macro constants for fixed-width integer types with no space after the preceding string literal became invalid: `std::printf("%"PRId64"\n",INT64_MIN);` has to be replaced by `std::printf("%" PRId64"\n",INT64_MIN);`.
Due to `maximal munch`, user-defined integer and floating point literals ending in <sup>(since C++17)</sup> `p`, `P`, `e` and `E`, when followed by the operators `+` or `-`, must be separated from the operator with whitespace or parentheses in the source:

```cpp
long double operator""_E(long double);
long double operator""_a(long double);
int operator""_p(unsigned long long);

auto x = 1.0_E+2.0;   // error
auto y = 1.0_a+2.0;   // OK
auto z = 1.0_E +2.0;  // OK
auto q = (1.0_E)+2.0; // OK
auto w = 1_p+2;       // error
auto u = 1_p +2;      // OK
```

Same applies to dot operator following an integer or floating-point user-defined literal:

```cpp
#include <chrono>

using namespace std::literals;

auto a = 4s.count();   // Error
auto b = 4s .count();  // OK
auto c = (4s).count(); // OK
```

Otherwise, a single invalid preprocessing number token (e.g., `1.0_E+2.0` or `4s.count`) is formed, which causes compilation to fail.

## Keywords

`cpp/keyword/operator`

## Examples


### Example

```cpp
#include <algorithm>
#include <cstddef>
#include <iostream>
#include <numbers>
#include <string>

// used as conversion from degrees (input param) to radians (returned output)
constexpr long double operator""_deg_to_rad(long double deg)
{
    long double radians = deg * std::numbers::pi_v<long double> / 180;
    return radians;
}

// used with custom type
struct mytype
{
    unsigned long long m;
};

constexpr mytype operator""_mytype(unsigned long long n)
{
    return mytype{n};
}

// used for side-effects
void operator""_print(const char* str)
{
    std::cout << str << '\n';
}

#if __cpp_nontype_template_args < 201911

std::string operator""_x2 (const char* str, std::size_t)
{
    return std::string{str} + str;
}

#else // C++20 string literal operator template

template<std::size_t N>
struct DoubleString
{
    char p[N + N - 1]{};

    constexpr DoubleString(char const(&pp)[N])
    {
        std::ranges::copy(pp, p);
        std::ranges::copy(pp, p + N - 1);
    }
};

template<DoubleString A>
constexpr auto operator""_x2()
{
    return A.p;
}

#endif // C++20

int main()
{
    double x_rad = 90.0_deg_to_rad;
    std::cout << std::fixed << x_rad << '\n';

    mytype y = 123_mytype;
    std::cout << y.m << '\n';

    0x123ABC_print;
    std::cout << "abc"_x2 << '\n';
}
```


**Output:**
```
1.570796
123
0x123ABC
abcabc
```


## Standard library

The following literal operators are defined in the standard library:


| std::literals::complex_literals|inline=true | |
| cpp/numeric/dsc operator""i | (see dedicated page) |
| std::literals::chrono_literals|inline=true | |
| cpp/chrono/dsc operator""h | (see dedicated page) |
| cpp/chrono/dsc operator""min | (see dedicated page) |
| cpp/chrono/dsc operator""s | (see dedicated page) |
| cpp/chrono/dsc operator""ms | (see dedicated page) |
| cpp/chrono/dsc operator""us | (see dedicated page) |
| cpp/chrono/dsc operator""ns | (see dedicated page) |
| cpp/chrono/dsc operator""y | (see dedicated page) |
| cpp/chrono/dsc operator""d | (see dedicated page) |
| std::literals::string_literals|inline=true | |
| cpp/string/basic_string/dsc operator""s | (see dedicated page) |
| std::literals::string_view_literals|inline=true | |
| cpp/string/basic_string_view/dsc operator""sv | (see dedicated page) |


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1479 | C++11 | literal operators could have default arguments | prohibited |

