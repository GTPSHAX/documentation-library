---
title: std::expected::swap
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/swap
---


```cpp
dcl|num=1|since=c++23|
constexpr void swap( expected& other ) noexcept(/* see below */);
dcl|num=2|since=c++23|
constexpr void swap( expected& other ) noexcept(/* see below */);
```

Swaps the contents with those of `other`.
1. The contained values are swapped as follows:


| rowspan=2 | Value of<br>rlpf | operator bool | has_value |
| colspan=2 | Value of c | other.has_value() |
| - |
| style="font-weight: normal;" | c | true |
| style="font-weight: normal;" | c | false |
| - |
| style="text-align: center;" | c | true |
| box | c/core | using std::swap;<br>c/core | swap(rlpi | /#Data members | valc/core | , rhs.tti | valc/core | ); |
| see below |
| - |
| style="text-align: center;" | c | false |
| c | other.swap(*this); |
| box | c/core | using std::swap;<br>c/core | swap(rlpi | /#Data members | unexc/core | , rhs.tti | unexc/core | ); |

@@ If  is `true` and `other.has_value()` is `false`, equivalent to:
box|
`// Case 1: the move constructions of unexpected values are non-throwing:`<br>
`// “other.unex” will be restored if the construction of “other.val” fails`<br>
`if constexpr (std::is_nothrow_move_constructible_v<E>)`<br>
`{`<br>
`E temp(std::move(other.``));`<br>
`std::destroy_at(std::addressof(other.``));`<br>
`try`<br>
`{`<br>
`std::construct_at(std::addressof(other.``), std::move(``)); // may throw`<br>
`std::destroy_at(std::addressof(``));`<br>
`std::construct_at(std::addressof(``), std::move(temp));`<br>
}<br>
`catch(...)`<br>
`{`<br>
`std::construct_at(std::addressof(other.``), std::move(temp));`<br>
`throw;`<br>
}<br>
}<br>
`// Case 2: the move constructions of expected values are non-throwing:`<br>
`// “this->val” will be restored if the construction of “this->unex” fails`<br>
`else`<br>
`{`<br>
`T temp(std::move(``));`<br>
`std::destroy_at(std::addressof(``));`<br>
`try`<br>
`{`<br>
`std::construct_at(std::addressof(``), std::move(other.``)); // may throw`<br>
`std::destroy_at(std::addressof(other.``));`<br>
`std::construct_at(std::addressof(other.``), std::move(temp));`<br>
}<br>
`catch(...)`<br>
`{`<br>
`std::construct_at(std::addressof(``), std::move(temp));`<br>
`throw;`<br>
}<br>
}<br>
`1== false;`<br>
`rhs.``1== true;`
@@ :
* `std::is_swappable_v<T>`
* `std::is_swappable_v<E>`
* `std::is_move_constructible_v<T> && std::is_move_constructible_v<E>`
* `std::is_nothrow_move_constructible_v<T>
2. The unexpected values are swapped as follows:


| rowspan=2 | Value of<br>rlpf | operator bool | has_value |
| colspan=2 | Value of c | other.has_value() |
| - |
| style="font-weight: normal;" | c | true |
| style="font-weight: normal;" | c | false |
| - |
| style="text-align: center;" | c | true |
| box | c/core | using std::swap;<br>c/core | swap(rlpi | /#Data members | valc/core | , rhs.tti | valc/core | ); |
| box | c/core | std::construct_at(std::addressof(tti | unexc/core | ),<br>nbspt | 18c/core | std::move(rhs.tti | unexc/core | ));<br>c/core | std::destroy_at(std::addressof(rhs.tti | unexc/core | ));<br>tti | has_valc/core | 1== false;<br>c/core | rhs.tti | has_valc/core | 1== true; |
| - |
| style="text-align: center;" | c | false |
| c | other.swap(*this); |
| box | c/core | using std::swap;<br>c/core | swap(rlpi | /#Data members | unexc/core | , rhs.tti | unexc/core | ); |

@@ .

## Parameters


### Parameters

- `other` - the `expected` object to exchange the contents with

## Exceptions

1. noexcept|
std::is_nothrow_move_constructible_v<T> && std::is_nothrow_swappable_v<T> &&
std::is_nothrow_move_constructible_v<E> && std::is_nothrow_swappable_v<E>
2. noexcept|
std::is_nothrow_move_constructible_v<E> && std::is_nothrow_swappable_v<E>

## Example


### Example

```cpp
#include <expected>
#include <iostream>
#include <string>

using Ex = std::expected<std::string, int>;

void show(const Ex& ex1, const Ex& ex2)
{
    for (int i{}; i < 2; ++i)
    {
        std::cout << (i ? "ex2" : "ex1");
        if (const Ex& ex = (i ? ex2 : ex1); ex.has_value())
            std::cout << ".has_value() = " << *ex << '\n';
        else
            std::cout << ".error() = " << ex.error() << '\n';
    }
}

int main()
{
    Ex ex1("\N{CAT FACE}");
    Ex ex2{"\N{GREEN HEART}"};
    show(ex1, ex2);
    ex1.swap(ex2);
    std::cout << "ex1.swap(ex2);\n";
    show(ex1, ex2);
    std::cout << '\n';

    ex2 = std::unexpected(13);
    show(ex1, ex2);
    std::cout << "ex1.swap(ex2);\n";
    ex1.swap(ex2);
    show(ex1, ex2);
    std::cout << '\n';

    ex2 = std::unexpected(19937);
    show(ex1, ex2);
    std::cout << "ex1.swap(ex2);\n";
    ex1.swap(ex2);
    show(ex1, ex2);
}
```


**Output:**
```
ex1.has_value() = 🐱
ex2.has_value() = 💚
ex1.swap(ex2);
ex1.has_value() = 💚
ex2.has_value() = 🐱

ex1.has_value() = 💚
ex2.error() = 13
ex1.swap(ex2);
ex1.error() = 13
ex2.has_value() = 💚

ex1.error() = 13
ex2.error() = 19937
ex1.swap(ex2);
ex1.error() = 19937
ex2.error() = 13
```


## See also


| cpp/utility/expected/dsc swap2 | (see dedicated page) |

