---
title: if statement
type: Language
source: https://en.cppreference.com/w/cpp/language/if
---


# tt|if

Conditionally executes another statement.
Used where code needs to be executed based on a condition<sup>(since C++23)</sup> , or whether the `if` statement is evaluated in a manifestly constant-evaluated context.

## Syntax


**Syntax:**

- `sdsc|num=1|`
- `*attr* (optional) **`if`** **`constexpr`**<br>**`(`** *init-statement* (optional) *condition* **`)`** *statement-true*`
- `sdsc|num=2|`
- `*attr* (optional) **`if`** **`constexpr`**<br>**`(`** *init-statement* (optional) *condition* **`)`** *statement-true* **`else`** *statement-false*`
- `|`
- `*attr* (optional) **`if`** **`!`** **`consteval`** *compound-statement*`
- `|`
- `*attr* (optional) **`if`** **`!`** **`consteval`** *compound-statement* **`else`** *statement*`
1. `if` statement without an `else` branch
2. `if` statement with an `else` branch
3. consteval if statement without an `else` branch
4. consteval if statement with an `else` branch

### Parameters

- `{{spar` - attr|<sup>(C++11)</sup> any number of `attributes`
- `{{ttb` - constexpr|<sup>(C++17)</sup> if present, the statement becomes a constexpr if statement
- `{{spar` - init-statement|<sup>(C++17)</sup> either
- * an `expression statement` (which may be a null statement `;`)
- * a  `simple declaration`, typically a declaration of a variable with initializer, but it may declare arbitrary many variables or be a `structured binding` declaration
- rrev|since=c++23|
- * an `alias declaration`
- `{{spar` - condition|a condition
- `{{spar` - statement-true|the `statement` to be executed if *condition* yields `true`
- `{{spar` - statement-false|the statement to be executed if *condition* yields `false`
- `{{spar` - compound-statement|the `compound statement` to be executed if the `if` statement is evaluated in a `manifestly constant-evaluated context` (or is not evaluated in such a context if `!` is preceding `consteval`)
- `{{spar` - statement|the statement (must be a compound statement, see `below`) to be executed if the `if` statement is not evaluated in a manifestly constant-evaluated context (or is evaluated in such a context if `!` is preceding `consteval`)

## Branch selection

If the *condition* yields `true`, *statement-true* is executed.
If the `else` part of the `if` statement is present and *condition* yields `false`, *statement-false* is executed.
If the `else` part of the `if` statement is present and *statement-true* is also an `if` statement, then that inner `if` statement must contain an `else` part as well (in other words, in nested `if` statements, the `else` is associated with the closest `if` that does not yet have an associated `else`).

### Example


**Output:**
```
2 is not greater than 2
2 > 1 and 1 <= 2
df()
```

rrev|since=c++17|

## `if` statements with initializer

If *init-statement* is used, the `if` statement is equivalent to

**Syntax:**

- `sdsc|`
- `**`{`**<br>`
- `:*init-statement*<br>`
- `:*attr* (optional) **`if`** **`constexpr`** **`(`** *condition* **`)`**<br>`
- `::*statement-true*<br>`
- `}`
or

**Syntax:**

- `sdsc|`
- `**`{`**<br>`
- `:*init-statement*<br>`
- `:*attr* (optional) **`if`** **`constexpr`** **`(`** *condition* **`)`**<br>`
- `::*statement-true*<br>`
- `:**`else`**`
- `::*statement-false*<br>`
- `}`
Except that names declared by the *init-statement* (if *init-statement* is a declaration) and names declared by *condition* (if *condition* is a declaration) are in the same scope, which is also the scope of both statements.

```cpp
std::map<int, std::string> m;
std::mutex mx;
extern bool shared_flag; // guarded by mx

int demo()
{
    if (auto it = m.find(10); it != m.end())
        return it->second.size();

    if (char buf[10]; std::fgets(buf, 10, stdin))
        m[0] += buf;

    if (std::lock_guard lock(mx); shared_flag)
    {
        unsafe_ping();
        shared_flag = false;
    }

    if (int s; int count = ReadBytesWithSignal(&s))
    {
        publish(count);
        raise(s);
    }

    if (const auto keywords = {"if", "for", "while"};
        std::ranges::any_of(keywords, [&tok](const char* kw) { return tok == kw; }))
    {
        std::cerr << "Token must not be a keyword\n";
    }
}
```

rrev|since=c++17|

## Constexpr if

The statement that begins with `if constexpr` is known as the ''constexpr if statement''. All substatements of a constexpr if statement are .
In a constexpr if statement, *condition* must be <sup>(until C++23)</sup> a `contextually converted constant expression of type `bool``<sup>(since C++23)</sup> an expression `contextually converted to `bool`, where the conversion is a `constant expression``.
If *condition* yields `true`, then *statement-false* is discarded (if present), otherwise, *statement-true* is discarded.
The `return` statements in a discarded statement do not participate in function return type deduction:

```cpp
template<typename T>
auto get_value(T t)
{
    if constexpr (std::is_pointer_v<T>)
        return *t; // deduces return type to int for T = int*
    else
        return t;  // deduces return type to int for T = int
}
```

The discarded statement can `ODR-use` a variable that is not defined:

```cpp
extern int x; // no definition of x required

int f()
{
    if constexpr (true)
        return 0;
    else if (x)
        return x;
    else
        return -x;
}
```

Outside a template, a discarded statement is fully checked. `if constexpr` is not a substitute for the `cpp/preprocessor/conditional|#if` preprocessing directive:

```cpp
void f()
{
    if constexpr(false)
    {
        int i = 0;
        int *p = i; // Error even though in discarded statement
    }
}
```

If a constexpr if statement appears inside a , and if *condition* is not `value-dependent` after instantiation, the discarded statement is not instantiated when the enclosing template is instantiated.

```cpp
template<typename T, typename ... Rest>
void g(T&& p, Rest&& ...rs)
{
    // ... handle p
    if constexpr (sizeof...(rs) > 0)
        g(rs...); // never instantiated with an empty argument list
}
```

The condition remains value-dependent after instantiation is a nested template:

```cpp
template<class T>
void g()
{
    auto lm = [=](auto p)
    {
        if constexpr (sizeof(T) == 1 && sizeof p == 1)
        {
            // this condition remains value-dependent after instantiation of g<T>,
            // which affects implicit lambda captures
            // this compound statement may be discarded only after
            // instantiation of the lambda body
        }
    };
}
```

The discarded statement cannot be ill-formed for every possible specialization:

```cpp
template<typename T>
void f()
{
    if constexpr (std::is_arithmetic_v<T>)
        // ...
    else {
        using invalid_array = int[-1]; // ill-formed: invalid for every T
        static_assert(false, "Must be arithmetic"); // ill-formed before CWG2518
    }
}
```

The common workaround before the implementation of  for such a catch-all statement is a type-dependent expression that is always `false`:

```cpp
template<typename>
constexpr bool dependent_false_v = false;

template<typename T>
void f()
{
    if constexpr (std::is_arithmetic_v<T>)
        // ...
    else {
        // workaround before CWG2518
        static_assert(dependent_false_v<T>, "Must be arithmetic");
    }
}
```

A `typedef declaration` <sup>(since C++23)</sup> or `alias declaration` can be used as the *init-statement* of a constexpr if statement to reduce the scope of the type alias.
rrev|since=c++23|

## Consteval if

The statement that begins with `if consteval` is known as the ''consteval if statement''. All substatements of a consteval if statement are .
*statement* must be a compound statement, and it will still be treated as a part of the consteval if statement even if it is not a compound statement (and thus results in a compilation error):
If a consteval if statement is evaluated in a `manifestly constant-evaluated context`, *compound-statement* is executed. Otherwise, *statement* is executed if it is present.
If the statement begins with `if !consteval`, the *compound-statement* and *statement* (if any) must both be compound statements. Such statements are not considered consteval if statements, but are equivalent to consteval if statements:
* } is equivalent to<br>
: c|if consteval {} else {/* stmt */}.
* c|if !consteval {/* stmt-1 */} else {/* stmt-2 */} is equivalent to<br>
: c|if consteval {/* stmt-2 */} else {/* stmt-1 */}.
*compound-statement* in a consteval if statement (or *statement* in the negative form) is in an `immediate function context`, in which a call to an immediate function needs not to be a constant expression.

### Example

```cpp
#include <cmath>
#include <cstdint>
#include <cstring>
#include <iostream>

constexpr bool is_constant_evaluated() noexcept
{
    if consteval { return true; } else { return false; }
}

constexpr bool is_runtime_evaluated() noexcept
{
    if not consteval { return true; } else { return false; }
}

consteval std::uint64_t ipow_ct(std::uint64_t base, std::uint8_t exp)
{
    if (!base) return base;
    std::uint64_t res{1};
    while (exp)
    {
        if (exp & 1) res *= base;
        exp /= 2;
        base *= base;
    }
    return res;
}

constexpr std::uint64_t ipow(std::uint64_t base, std::uint8_t exp)
{
    if consteval // use a compile-time friendly algorithm
    {
        return ipow_ct(base, exp);
    }
    else // use runtime evaluation
    {
        return std::pow(base, exp);
    }
}

int main(int, const char* argv[])
{
    static_assert(ipow(0, 10) == 0 && ipow(2, 10) == 1024);
    std::cout << ipow(std::strlen(argv[0]), 3) << '\n';
}
```


## Notes

If *statement-true* or *statement-false* is not a compound statement, it is treated as if it were:

```cpp
if (x)
    int i;
// i is no longer in scope
```

is the same as

```cpp
if (x)
{
    int i;
}
// i is no longer in scope
```

The scope of the name introduced by *condition*, if it is a declaration, is the combined scope of both statements' bodies:

```cpp
if (int x = f())
{
    int x; // error: redeclaration of x
}
else
{
    int x; // error: redeclaration of x
}
```

If *statement-true* is entered by `goto` or `longjmp`, *condition* is not evaluated and *statement-false* is not executed.
rrev|since=c++17|until=c++23|
Built-in conversions are not allowed in the *condition* of a constexpr if statement, except for non-`narrowing` `integral conversions` to `bool`.

## Keywords

`cpp/keyword/if`,
`cpp/keyword/else`,
`cpp/keyword/constexpr`,
`cpp/keyword/consteval`

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-631 | C++98 | the control flow was unspecified if the<br>first substatement is reached via a label | the condition is not evaluated and the second<br>substatement is not executed (same as in C) |


## See also


| cpp/types/dsc is_constant_evaluated | (see dedicated page) |

