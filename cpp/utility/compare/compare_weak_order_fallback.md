---
title: std::compare_weak_order_fallback
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/compare/compare_weak_order_fallback
---


```cpp
**Header:** `<`compare`>`
dcl|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */
compare_weak_order_fallback = /* unspecified */;
}
dcl|since=c++20|1=
template< class T, class U >
requires /* see below */
constexpr std::weak_ordering
compare_weak_order_fallback( T&& t, U&& u ) noexcept(/* see below */);
```

Performs three-way comparison on subexpressions `t` and `u` and produces a result of type , even if the operator `1=<=>` is unavailable.
If `std::decay_t<T>` and `std::decay_t<U>` are the same type, `std::compare_weak_order_fallback(t, u)` is expression-equivalent to:
* `std::weak_order(t, u)`, if it is a well-formed expression; otherwise,
* c multi
|1=t == u ? std::weak_ordering::equivalent :
|2=t <  u ? std::weak_ordering::less :
|3=         std::weak_ordering::greater
, if the expressions `1=t == u` and `t < u` are both well-formed and each of `1=decltype(t == u)` and `decltype(t < u)` models , except that `t` and `u` are evaluated only once.
In all other cases, `std::compare_weak_order_fallback(t, u)` is ill-formed, which can result in substitution failure when it appears in the immediate context of a template instantiation.

## Example


### Example

```cpp
#include <compare>
#include <iostream>

// does not support <=>
struct Rational_1
{
    int num;
    int den; // > 0
};

inline constexpr bool operator<(Rational_1 lhs, Rational_1 rhs)
{
    return lhs.num * rhs.den < rhs.num * lhs.den;
}

inline constexpr bool operator==(Rational_1 lhs, Rational_1 rhs)
{
    return lhs.num * rhs.den == rhs.num * lhs.den;
}

// supports <=>
struct Rational_2
{
    int num;
    int den; // > 0
};

inline constexpr std::weak_ordering operator<=>(Rational_2 lhs, Rational_2 rhs)
{
    return lhs.num * rhs.den <=> rhs.num * lhs.den;
}

inline constexpr bool operator==(Rational_2 lhs, Rational_2 rhs)
{
    return lhs <=> rhs == 0;
}

void print(int id, std::weak_ordering value)
{
    std::cout << id << ") ";
    if (value == 0)
        std::cout << "equal\n";
    else if (value < 0)
        std::cout << "less\n";
    else
        std::cout << "greater\n";
}

int main()
{
    Rational_1 a{1, 2}, b{3, 4};
//  print(0, a <=> b); // does not work
    print(1, std::compare_weak_order_fallback(a, b)); // works, defaults to < and ==

    Rational_2 c{6, 5}, d{8, 7};
    print(2, c <=> d); // works
    print(3, std::compare_weak_order_fallback(c, d)); // works

    Rational_2 e{2, 3}, f{4, 6};
    print(4, e <=> f); // works
    print(5, std::compare_weak_order_fallback(e, f)); // works
}
```


**Output:**
```
1) less
2) greater
3) greater
4) equal
5) equal
```


## Defect reports


## See also


| cpp/utility/compare/dsc weak_order | (see dedicated page) |

