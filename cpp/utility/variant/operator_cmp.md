---
title: operators (std::variant)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/operator_cmp
---


# 1=operator==, !=, <, <=, >, >=, <=>small|(std::variant)


```cpp
**Header:** `<`variant`>`
dcl|num=1|since=c++17|1=
template< class... Types >
constexpr bool operator==( const std::variant<Types...>& lhs,
const std::variant<Types...>& rhs );
dcl|num=2|since=c++17|1=
template< class... Types >
constexpr bool operator!=( const std::variant<Types...>& lhs,
const std::variant<Types...>& rhs );
dcl|num=3|since=c++17|
template< class... Types >
constexpr bool operator<( const std::variant<Types...>& lhs,
const std::variant<Types...>& rhs );
dcl|num=4|since=c++17|
template< class... Types >
constexpr bool operator>( const std::variant<Types...>& lhs,
const std::variant<Types...>& rhs );
dcl|num=5|since=c++17|1=
template< class... Types >
constexpr bool operator<=( const std::variant<Types...>& lhs,
const std::variant<Types...>& rhs );
dcl|num=6|since=c++17|1=
template< class... Types >
constexpr bool operator>=( const std::variant<Types...>& lhs,
const std::variant<Types...>& rhs );
dcl|num=7|since=c++20|1=
template< class... Types >
constexpr std::common_comparison_category_t
<std::compare_three_way_result_t<Types>...>
operator<=>( const std::variant<Types...>& lhs,
const std::variant<Types...>& rhs );
dcla|num=8|expos=yes|
template< std::size_t I, class... Types >
constexpr const std::variant_alternative_t<I, std::variant<Types...>>&
GET( const variant<Types...>& v );
```

Performs comparison operations on `std::variant` objects.
@1-7@ Compares two `std::variant` objects `lhs` and `rhs`. The contained values are compared (using the corresponding operator of `T`) only if both `lhs` and `rhs` contain values corresponding to the same index. Otherwise,
* `lhs` is considered ''equal to'' `rhs` if, and only if, both `lhs` and `rhs` do not contain a value.
* `lhs` is considered ''less than'' `rhs` if, and only if, either `rhs` contains a value and `lhs` does not, or `lhs.index()` is less than `rhs.index()`.
:@1-6@ Let `@` denote the corresponding comparison operator, for each of these functions:
rev|until=c++26|
If, for some values of `I`, the corresponding expression  is ill-formed or its result is not convertible to `bool`, the program is ill-formed.
rev|since=c++26|
.
8. The exposition-only function template  behaves like `std::get, except that `std::bad_variant_access` is never thrown.
@@ If `I < sizeof...(Types)` is `false`, the program is ill-formed.
@@ If `1=I == v.index()` is `false`, the behavior is undefined.

## Parameters


### Parameters

- `lhs,rhs` - variants to compare

## Return value


| rowspan=2 | Operator |
| colspan=2 | Both operands contains a value<br>normal | small | (let c | I be c | lhs.index() and c | J be c | rhs.index()) |
| rowspan=2 | c | lhs or c | rhs is valueless<br>normal | small | (let c | lhs_empty be c | lhs.valueless_by_exception() and c | rhs_empty be c | rhs.valueless_by_exception()) |
| - |
| c | I and c | J are equal |
| c | I and c | J are unequal |
| - |
| co | 1=== |
| box | tti | GETc/core | 1=<I>(lhs) ==tti | GETc/core | <I>(rhs) |
| c | false |
| c | lhs_empty && rhs_empty |
| - |
| co | 1=!= |
| box | tti | GETc/core | 1=<I>(lhs) !=tti | GETc/core | <I>(rhs) |
| c | true |
| c | 1=lhs_empty != rhs_empty |
| - |
| co | < |
| box | tti | GETc/core | <I>(lhs) <tti | GETc/core | <I>(rhs) |
| c | lhs.index() < rhs.index() |
| c | lhs_empty && !rhs_empty |
| - |
| co | > |
| box | tti | GETc/core | <I>(lhs) >tti | GETc/core | <I>(rhs) |
| c | lhs.index() > rhs.index() |
| c | !lhs_empty && rhs_empty |
| - |
| co | 1=<= |
| box | tti | GETc/core | 1=<I>(lhs) <=tti | GETc/core | <I>(rhs) |
| c | lhs.index() < rhs.index() |
| c | lhs_empty |
| - |
| co | 1=>= |
| box | tti | GETc/core | 1=<I>(lhs) >=tti | GETc/core | <I>(rhs) |
| c | lhs.index() > rhs.index() |
| c | rhs_empty |
| - |
| co | 1=<=> |
| box | tti | GETc/core | 1=<I>(lhs) <=>tti | GETc/core | <I>(rhs) |
| c | 1=lhs.index() <=> rhs.index() |
| see below |

For `1=operator<=>`:
* If only `lhs` is valueless, returns `cpp/utility/compare/strong_ordering|std::strong_ordering::less`.
* If only `rhs` is valueless, returns `cpp/utility/compare/strong_ordering|std::strong_ordering::greater`.
* If both `lhs` and `rhs` are valueless, returns `cpp/utility/compare/strong_ordering|std::strong_ordering::equal`.

## Notes


## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <variant>

int main()
{
    std::cout << std::boolalpha;
    std::string cmp;
    bool result;

    auto print2 = [&cmp, &result](const auto& lhs, const auto& rhs)
    {
        std::cout << lhs << ' ' << cmp << ' ' << rhs << " : " << result << '\n';
    };

    std::variant<int, std::string> v1, v2;

    std::cout << "operator==\n";
    {
        cmp = "==";

        // by default v1 = 0, v2 = 0;
        result = v1 == v2; // true
        std::visit(print2, v1, v2);

        v1 = v2 = 1;
        result = v1 == v2; // true
        std::visit(print2, v1, v2);

        v2 = 2;
        result = v1 == v2; // false
        std::visit(print2, v1, v2);

        v1 = "A";
        result = v1 == v2; // false: v1.index == 1, v2.index == 0
        std::visit(print2, v1, v2);

        v2 = "B";
        result = v1 == v2; // false
        std::visit(print2, v1, v2);

        v2 = "A";
        result = v1 == v2; // true
        std::visit(print2, v1, v2);
    }

    std::cout << "operator<\n";
    {
        cmp = "<";

        v1 = v2 = 1;
        result = v1 < v2; // false
        std::visit(print2, v1, v2);

        v2 = 2;
        result = v1 < v2; // true
        std::visit(print2, v1, v2);

        v1 = 3;
        result = v1 < v2; // false
        std::visit(print2, v1, v2);

        v1 = "A"; v2 = 1;
        result = v1 < v2; // false: v1.index == 1, v2.index == 0
        std::visit(print2, v1, v2);

        v1 = 1; v2 = "A";
        result = v1 < v2; // true: v1.index == 0, v2.index == 1
        std::visit(print2, v1, v2);

        v1 = v2 = "A";
        result = v1 < v2; // false
        std::visit(print2, v1, v2);

        v2 = "B";
        result = v1 < v2; // true
        std::visit(print2, v1, v2);

        v1 = "C";
        result = v1 < v2; // false
        std::visit(print2, v1, v2);
    }

    {
        std::variant<int, std::string> v1;
        std::variant<std::string, int> v2;
    //  v1 == v2; // Compilation error: no known conversion
    }

    // TODO: C++20 three-way comparison operator <=> for variants
}
```


**Output:**
```
operator==
0 == 0 : true
1 == 1 : true
1 == 2 : false
A == 2 : false
A == B : false
A == A : true
operator<
1 < 1 : false
1 < 2 : true
3 < 2 : false
A < 1 : false
1 < A : true
A < A : false
A < B : true
C < B : false
```


## See also


| cpp/utility/optional/dsc operator cmp | (see dedicated page) |

