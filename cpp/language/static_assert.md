---
title: static_assert declaration
type: Language
source: https://en.cppreference.com/w/cpp/language/static_assert
---


# tt|static_assert

Performs compile-time assertion checking.

## Syntax


**Syntax:**

- `sdsc|num=1|`
- `**`static_assert(`** *bool-constexpr* **`,`** *unevaluated-string* **`)`**`
- `|`
- `**`static_assert(`** *bool-constexpr* **`)`**`
- `|`
- `**`static_assert(`** *bool-constexpr* **`,`** *constant-expression* **`)`**`
Declares a static assertion. If the assertion fails, the program is ill-formed, and a diagnostic error message may be generated.
1. A static assertion with fixed error message.
2. A static assertion without error message.
3. A static assertion with user-generated error message.
@@ This syntax can only be matched if syntax  does not match.

## Explanation


### Parameters

- `{{spar` - bool-constexpr|rrev multi|rev1=
- a `contextually converted constant expression of type `bool``. Built-in conversions are not allowed, except for non-`narrowing` `integral conversions` to `bool`.
- |since2=c++23|rev2=an expression `contextually converted to `bool`` where the conversion is a `constant expression`
- `{{spar` - unevaluated-string|an `unevaluated string literal` that will appear as the error message
- `{{spar` - constant-expression|a `constant expression` `msg` satisfying all following conditions:
- * `msg.size()` is implicitly convertible to `std::size_t`.
- * `msg.data()` is implicitly convertible to `const char*`.
A `static_assert` declaration may appear at namespace and block `scope` (as a `block declaration`) and inside a class body (as a `member declaration`).
If *bool-constexpr* is well-formed and evaluates to `true`, or is evaluated in the context of a template definition and the template is uninstantiated, this declaration has no effect. Otherwise a compile-time error is issued, and the user-provided message, if any, is included in the diagnostic message.
The text of the user-provided message is determined as follows:
* If the message matches the syntactic requirements of *unevaluated-string*, the text of the message is the text of the *unevaluated-string*.
rrev|since=c++26|
* Otherwise, given the following values:
:* Let `msg` denote the value of *constant-expression*.
:* Let `len` denote the value of `msg.size()`, which must be a  of type `std::size_t`.
:* Let `ptr` denote the expression `msg.data()`, `implicitly converted` to `const char*`. `ptr` must be a .
: The text of the message is formed by the sequence of `len` `code units`, starting at `ptr`, of the `ordinary literal encoding`. For each integer `i` in [0, len), `ptr[i]` must be an .

## Notes

The standard does not require a compiler to print the verbatim text of , though compilers generally do so as much as possible.
rrev|until=c++26|
Since the error message has to be a string literal, it cannot contain dynamic information or even a `constant expression` that is not a string literal itself. In particular, it cannot contain the `name` of the `template type argument`.

## Keywords

`cpp/keyword/static_assert`

## Example


### Example

```cpp
#include <format>
#include <type_traits>

static_assert(03301 == 1729); // since C++17 the message string is optional

template<class T>
void swap(T& a, T& b) noexcept
{
    static_assert(std::is_copy_constructible_v<T>,
                  "Swap requires copying");
    static_assert(std::is_nothrow_copy_constructible_v<T> &&
                  std::is_nothrow_copy_assignable_v<T>,
                  "Swap requires nothrow copy/assign");
    auto c = b;
    b = a;
    a = c;
}

template<class T>
struct data_structure
{
    static_assert(std::is_default_constructible_v<T>,
                  "Data structure requires default-constructible elements");
};

template<class>
constexpr bool dependent_false = false; // workaround before CWG2518/P2593R1

template<class T>
struct bad_type
{
    static_assert(dependent_false<T>, "error on instantiation, workaround");
    static_assert(false, "error on instantiation"); // OK because of CWG2518/P2593R1
};

struct no_copy
{
    no_copy(const no_copy&) = delete;
    no_copy() = default;
};

struct no_default
{
    no_default() = delete;
};

#if __cpp_static_assert >= 202306L
// Not real C++ yet (std::format should be constexpr to work):
static_assert(sizeof(int) == 4, std::format("Expected 4, got {}", sizeof(int)));
#endif

int main()
{
    int a, b;
    swap(a, b);

    no_copy nc_a, nc_b;
    swap(nc_a, nc_b); // 1

    [[maybe_unused]] data_structure<int> ds_ok;
    [[maybe_unused]] data_structure<no_default> ds_error; // 2
}
```


**Output:**
```
1: error: static assertion failed: Swap requires copying
2: error: static assertion failed: Data structure requires default-constructible elements
3: error: static assertion failed: Expected 4, got 2
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-2039 | C++11 | only the expression before conversion is required to be constant | the conversion must also be<br>valid in a constant expression |


## References


## See also


| cpp/preprocessor/dsc error | (see dedicated page) |
| cpp/error/dsc assert | (see dedicated page) |
| cpp/language/dsc contract_assert | (see dedicated page) |
| cpp/types/dsc enable_if | (see dedicated page) |

