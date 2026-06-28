---
title: std::common_type
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/common_type
---

ddcl|header=type_traits|since=c++11|
template< class... T >
struct common_type;
Determines the common type among all types `T...`, that is a type all `T...` can be explicitly converted to. If such a type exists (as determined according to the rules below), the member `type` names that type. Otherwise, there is no member `type`.
* If `sizeof...(T)` is zero, there is no member `type`.
* If `sizeof...(T)` is one (i.e., `T...` contains only one type `T0`), the member `type` names the same type as `std::common_type<T0, T0>::type` if it exists; otherwise there is no member `type`.
* If `sizeof...(T)` is two (i.e., `T...` contains exactly two types `T1` and `T2`),
:* If applying `std::decay` to at least one of `T1` and `T2` produces a different type, the member `type` names the same type as `std::common_type<std::decay<T1>::type, std::decay<T2>::type>::type`, if it exists; if not, there is no member `type`;
:* Otherwise, if there is a user specialization for `std::common_type<T1, T2>`, that specialization is used;
:* Otherwise, if `std::decay<decltype(false ? std::declval<T1>() : std::declval<T2>())>::type` is a valid type, the member `type` denotes that type, see the conditional operator;
rrev|since=c++20|1=
:* Otherwise, if `std::decay<decltype(false ? std::declval<CR1>() : std::declval<CR2>())>::type` is a valid type, where `CR1` and `CR2` are `const std::remove_reference_t<T1>&` and `const std::remove_reference_t<T2>&` respectively, the member `type` denotes that type;
:* Otherwise, there is no member `type`.
* If `sizeof...(T)` is greater than two (i.e., `T...` consists of the types `T1, T2, R...`), then if `std::common_type<T1, T2>::type` exists, the member `type` denotes `std::common_type<typename std::common_type<T1, T2>::type, R...>::type` if such a type exists. In all other cases, there is no member `type`.

## Nested types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types


```cpp
dcl|since=c++14|1=
template< class... T >
using common_type_t = typename common_type<T...>::type;
```


## Specializations

Users may specialize `common_type` for types `T1` and `T2` if
* At least one of `T1` and `T2` depends on a user-defined type, and
* `std::decay` is an identity transformation for both `T1` and `T2`.
If such a specialization has a member named `type`, it must be a public and unambiguous member that names a cv-unqualified non-reference type to which both `T1` and `T2` are explicitly convertible. Additionally, `std::common_type<T1, T2>::type` and `std::common_type<T2, T1>::type` must denote the same type.
A program that adds `common_type` specializations in violation of these rules has undefined behavior.
Note that the behavior of a program that adds a specialization to any other template <sup>(since C++20)</sup> (except for `cpp/types/common_reference|std::basic_common_reference`) from `<type_traits>` is undefined.
The following specializations are already provided by the standard library:


| cpp/chrono/duration/dsc common_type | (see dedicated page) |
| cpp/chrono/time_point/dsc common_type | (see dedicated page) |
| cpp/utility/pair/dsc common_type | (see dedicated page) |
| cpp/utility/tuple/dsc common_type | (see dedicated page) |
| cpp/iterator/basic_const_iterator/dsc common_type | (see dedicated page) |


## Possible implementation

eq fun
|1=
// primary template (used for zero types)
template<class...>
struct common_type {};
// one type
template<class T>
struct common_type<T> : common_type<T, T> {};
namespace detail
{
template<class...>
using void_t = void;
template<class T1, class T2>
using conditional_result_t = decltype(false ? std::declval<T1>() : std::declval<T2>());
template<class, class, class = void>
struct decay_conditional_result {};
template<class T1, class T2>
struct decay_conditional_result<T1, T2, void_t<conditional_result_t<T1, T2>>>
: std::decay<conditional_result_t<T1, T2>> {};
template<class T1, class T2, class = void>
struct common_type_2_impl : decay_conditional_result<const T1&, const T2&> {};
// C++11 implementation:
// template<class, class, class = void>
// struct common_type_2_impl {};
template<class T1, class T2>
struct common_type_2_impl<T1, T2, void_t<conditional_result_t<T1, T2>>>
: decay_conditional_result<T1, T2> {};
}
// two types
template<class T1, class T2>
struct common_type<T1, T2>
: std::conditional<std::is_same<T1, typename std::decay<T1>::type>::value &&
std::is_same<T2, typename std::decay<T2>::type>::value,
detail::common_type_2_impl<T1, T2>,
common_type<typename std::decay<T1>::type,
typename std::decay<T2>::type>>::type {};
// 3+ types
namespace detail
{
template<class AlwaysVoid, class T1, class T2, class... R>
struct common_type_multi_impl {};
template<class T1, class T2, class...R>
struct common_type_multi_impl<void_t<typename common_type<T1, T2>::type>, T1, T2, R...>
: common_type<typename common_type<T1, T2>::type, R...> {};
}
template<class T1, class T2, class... R>
struct common_type<T1, T2, R...>
: detail::common_type_multi_impl<void, T1, T2, R...> {};

## Notes

For arithmetic types not subject to promotion, the common type may be viewed as the type of the (possibly mixed-mode) arithmetic expression such as `T0() + T1() + ... + Tn()`.

## Examples


### Example

```cpp
#include <iostream>
#include <type_traits>

template<class T>
struct Number { T n; };

template<class T, class U>
constexpr Number<std::common_type_t<T, U>>
    operator+(const Number<T>& lhs, const Number<U>& rhs)
{
    return {lhs.n + rhs.n};
}

void describe(const char* expr, const Number<int>& x)
{
    std::cout << expr << "  is  Number<int>{" << x.n << "}\n";
}

void describe(const char* expr, const Number<double>& x)
{
    std::cout << expr << "  is  Number<double>{" << x.n << "}\n";
}

int main()
{
    Number<int> i1 = {1}, i2 = {2};
    Number<double> d1 = {2.3}, d2 = {3.5};
    describe("i1 + i2", i1 + i2);
    describe("i1 + d2", i1 + d2);
    describe("d1 + i2", d1 + i2);
    describe("d1 + d2", d1 + d2);
}
```


**Output:**
```
i1 + i2  is  Number<int>{3}
i1 + d2  is  Number<double>{4.5}
d1 + i2  is  Number<double>{4.3}
d1 + d2  is  Number<double>{5.8}
```


## Defect reports


## See also


| cpp/concepts/dsc common_with | (see dedicated page) |

