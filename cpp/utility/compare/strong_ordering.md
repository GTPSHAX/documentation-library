---
title: std::strong_ordering
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/compare/strong_ordering
---

ddcl|since=c++20|header=compare|1=
class strong_ordering;
The class type `std::strong_ordering` is the result type of a  that:
* Admits all six relational operators (`1===`, `1=!=`, `<`, `1=<=`, `>`, `1=>=`).
* [Connected relation|Does not allow incomparable values](https://en.wikipedia.org/wiki/Connected relation|Does not allow incomparable values): exactly one of `a < b`, `1=a == b`, or `a > b` must be `true`.

## Constants

The type `std::strong_ordering` has four valid values, implemented as const static data members of its type:


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Conversions

`std::strong_ordering` is the strongest of the three comparison categories: it is not implicitly-convertible from any other category and is implicitly-convertible to the other two.
member|operator partial_ordering|2=
ddcl|1=
constexpr operator partial_ordering() const noexcept;

## Return value

`std::partial_ordering::less` if `v` is `less`,
`std::partial_ordering::greater` if `v` is `greater`,
`std::partial_ordering::equivalent` if `v` is `equal` or `equivalent`.
member|operator weak_ordering|2=
ddcl|1=
constexpr operator weak_ordering() const noexcept;

## Return value

`std::weak_ordering::less` if `v` is `less`,
`std::weak_ordering::greater` if `v` is `greater`,
`std::weak_ordering::equivalent` if `v` is `equal` or `equivalent`.

## Comparisons

Comparison operators are defined between values of this type and literal `0`. This supports the expressions `1=a <=> b == 0` or `1=a <=> b < 0` that can be used to convert the result of a three-way comparison operator to a boolean relationship; see  `cpp/utility/compare/named comparison functions|std::is_eq`, `cpp/utility/compare/named comparison functions|std::is_lt`, etc.
The behavior of a program that attempts to compare a `strong_ordering` with anything other than the integer literal `0` is undefined.


| cpp/utility/compare/strong_ordering|inlinemem=true|title=operator | |

member|1=operator==|2=

```cpp
dcl|num=1|1=
friend constexpr bool
operator==( strong_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool
operator==( strong_ordering v, strong_ordering w ) noexcept = default;
```


## Parameters


### Parameters

- `v, w` - `std::strong_ordering` values to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `equivalent` or `equal`, `false` if `v` is `less` or `greater`
2. `true` if both parameters hold the same value, `false` otherwise. Note that `equal` is the same as `equivalent`.
member|1=operator<|2=

```cpp
dcl|num=1|1=
friend constexpr bool operator<( strong_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool operator<( /*unspecified*/ u, strong_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::strong_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `less`, and `false` if `v` is `greater`,  `equivalent`, or `equal`
2. `true` if `v` is `greater`, and `false` if `v` is `less`,  `equivalent`, or `equal`
member|1=operator<=|2=

```cpp
dcl|num=1|1=
friend constexpr bool operator<=( strong_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool operator<=( /*unspecified*/ u, strong_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::strong_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `less`, `equivalent`, or `equal`, and `false` if `v` is `greater`
2. `true` if `v` is `greater`, `equivalent`, or `equal`, and `false` if `v` is `less`
member|1=operator>|2=

```cpp
dcl|num=1|1=
friend constexpr bool operator>( strong_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool operator>( /*unspecified*/ u, strong_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::strong_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `greater`, and `false` if `v` is `less`, `equivalent`, or `equal`
2. `true` if `v` is `less`, and `false` if `v` is `greater`, `equivalent`, or `equal`
member|1=operator>=|2=

```cpp
dcl|num=1|1=
friend constexpr bool operator>=( strong_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool operator>=( /*unspecified*/ u, strong_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::strong_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `greater`, `equivalent`, or `equal`, and `false` if `v` is `less`
2. `true` if `v` is `less`, `equivalent`, or `equal`, and `false` if `v` is `greater`
member|1=operator<=>|2=

```cpp
dcl|num=1|1=
friend constexpr strong_ordering
operator<=>( strong_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr strong_ordering
operator<=>( /*unspecified*/ u, strong_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::strong_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `v`.
2. `greater` if `v` is `less`, `less` if `v` is `greater`, otherwise `v`.

## Example


### Example

```cpp
#include <compare>
#include <iostream>

struct Point
{
    int x{}, y{};

    friend constexpr std::strong_ordering operator<=>(Point lhs, Point rhs)
    {
        if (lhs.x < rhs.x or (lhs.x == rhs.x and lhs.y < rhs.y))
            return std::strong_ordering::less;
        if (lhs.x > rhs.x or (lhs.x == rhs.x and lhs.y > rhs.y))
            return std::strong_ordering::greater;
        return std::strong_ordering::equivalent;
    }

    friend std::ostream& operator<<(std::ostream& os, Point s)
    {
        return os << '(' << s.x << ',' << s.y << ')';
    }
};

void print_three_way_comparison(const auto& p, const auto& q)
{
    const auto cmp{p <=> q};
    std::cout << p
              << (cmp < 0 ? " <  " : cmp > 0 ? " >  " : " == " ) // compares with 0
              << q << '\n';
}

void print_two_way_comparison(const auto& p, const auto& q)
{
    std::cout << p
              << (p < q ? " <  " : p > q ? " >  " : " == ") // compares p and q
              << q << '\n';
}

int main()
{
    const Point p1{0, 1}, p2{0, 1}, p3{0, 2};

    print_three_way_comparison(p1, p2);
    print_two_way_comparison(p1, p2);

    print_three_way_comparison(p2, p3);
    print_two_way_comparison(p2, p3);

    print_three_way_comparison(p3, p2);
    print_two_way_comparison(p3, p2);
}
```


**Output:**
```
(0,1) == (0,1)
(0,1) == (0,1)
(0,1) <  (0,2)
(0,1) <  (0,2)
(0,2) >  (0,1)
(0,2) >  (0,1)
```


## See also


| cpp/utility/compare/dsc weak_ordering | (see dedicated page) |
| cpp/utility/compare/dsc partial_ordering | (see dedicated page) |

