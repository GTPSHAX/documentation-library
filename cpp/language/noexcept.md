---
title: noexcept operator
type: Language
source: https://en.cppreference.com/w/cpp/language/noexcept
---


# tt|noexcept

The `noexcept` operator performs a compile-time check that returns `true` if an expression is declared to not throw any exceptions.
It can be used within a function template's ``noexcept` specifier` to declare that the function will throw exceptions for some types but not others.

## Syntax


**Syntax:**

- `*expression* **`)`**`
Returns a  of type `bool`. The result is `true` if <sup>(until C++17)</sup> the set of `potential exceptions of the *expression` is empty*<sup>(since C++17)</sup> *expression is specified to be `non-throwing`*, and `false` otherwise.
*expression* is an `unevaluated operand`.
rrev|since=c++17|
If *expression* is a prvalue,  is applied.

## Notes

Even if `noexcept(expr)` is `true`, an evaluation of `expr` may still throw as the result of encountering undefined behavior.
rrev|since=c++17|
If *expression* is of a class type or (possibly multidimensional) array thereof, temporary materialization requires the destructor be non-deleted and accessible.

## Keywords

`cpp/keyword/noexcept`

## Example


### Example

```cpp
#include <iostream>
#include <utility>
#include <vector>

void may_throw();
void no_throw() noexcept;
auto lmay_throw = []{};
auto lno_throw = []() noexcept {};

class T
{
public:
    ~T(){} // dtor prevents move ctor
           // copy ctor is noexcept
};

class U
{
public:
    ~U(){} // dtor prevents move ctor
           // copy ctor is noexcept(false)
    std::vector<int> v;
};

class V
{
public:
    std::vector<int> v;
};

int main()
{
    T t;
    U u;
    V v;

    std::cout << std::boolalpha <<
        "may_throw() is noexcept(" << noexcept(may_throw()) << ")\n"
        "no_throw() is noexcept(" << noexcept(no_throw()) << ")\n"
        "lmay_throw() is noexcept(" << noexcept(lmay_throw()) << ")\n"
        "lno_throw() is noexcept(" << noexcept(lno_throw()) << ")\n"
        "~T() is noexcept(" << noexcept(std::declval<T>().~T()) << ")\n"
        // note: the following tests also require that ~T() is noexcept because
        // the expression within noexcept constructs and destroys a temporary
        "T(rvalue T) is noexcept(" << noexcept(T(std::declval<T>())) << ")\n"
        "T(lvalue T) is noexcept(" << noexcept(T(t)) << ")\n"
        "U(rvalue U) is noexcept(" << noexcept(U(std::declval<U>())) << ")\n"
        "U(lvalue U) is noexcept(" << noexcept(U(u)) << ")\n"
        "V(rvalue V) is noexcept(" << noexcept(V(std::declval<V>())) << ")\n"
        "V(lvalue V) is noexcept(" << noexcept(V(v)) << ")\n";
}
```


**Output:**
```
may_throw() is noexcept(false)
no_throw() is noexcept(true)
lmay_throw() is noexcept(false)
lno_throw() is noexcept(true)
~T() is noexcept(true)
T(rvalue T) is noexcept(true)
T(lvalue T) is noexcept(true)
U(rvalue U) is noexcept(false)
U(lvalue U) is noexcept(false)
V(rvalue V) is noexcept(true)
V(lvalue V) is noexcept(false)
```


## Defect reports


## See also


| cpp/language/dsc noexcept spec | (see dedicated page) |
| cpp/language/dsc except spec | (see dedicated page) |

