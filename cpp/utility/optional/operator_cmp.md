---
title: operators (std::optional)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/optional/operator_cmp
---


# 1=operator==, !=, <, <=, >, >=, <=>small|(std::optional)


```cpp
**Header:** `<`optional`>`
dcl|num=1|since=c++17|1=
template< class T, class U >
constexpr bool operator==( const optional<T>& lhs, const optional<U>& rhs );
dcl|num=2|since=c++17|1=
template< class T, class U >
constexpr bool operator!=( const optional<T>& lhs, const optional<U>& rhs );
dcl|num=3|since=c++17|1=
template< class T, class U >
constexpr bool operator<( const optional<T>& lhs, const optional<U>& rhs );
dcl|num=4|since=c++17|1=
template< class T, class U >
constexpr bool operator<=( const optional<T>& lhs, const optional<U>& rhs );
dcl|num=5|since=c++17|1=
template< class T, class U >
constexpr bool operator>( const optional<T>& lhs, const optional<U>& rhs );
dcl|num=6|since=c++17|1=
template< class T, class U >
constexpr bool operator>=( const optional<T>& lhs, const optional<U>& rhs );
dcl|num=7|since=c++20|1=
template< class T, std::three_way_comparable_with<T> U >
constexpr std::compare_three_way_result_t<T, U>
operator<=>( const optional<T>& lhs, const optional<U>& rhs );
dcl|num=8|since=c++17|1=
template< class T >
constexpr bool operator==( const optional<T>& opt, std::nullopt_t ) noexcept;
dcl|num=9|since=c++17|until=c++20|1=
template< class T >
constexpr bool operator==( std::nullopt_t, const optional<T>& opt ) noexcept;
dcl|num=10|since=c++17|until=c++20|1=
template< class T >
constexpr bool operator!=( const optional<T>& opt, std::nullopt_t ) noexcept;
dcl|num=11|since=c++17|until=c++20|1=
template< class T >
constexpr bool operator!=( std::nullopt_t, const optional<T>& opt ) noexcept;
dcl|num=12|since=c++17|until=c++20|1=
template< class T >
constexpr bool operator<( const optional<T>& opt, std::nullopt_t ) noexcept;
dcl|num=13|since=c++17|until=c++20|1=
template< class T >
constexpr bool operator<( std::nullopt_t, const optional<T>& opt ) noexcept;
dcl|num=14|since=c++17|until=c++20|1=
template< class T >
constexpr bool operator<=( const optional<T>& opt, std::nullopt_t ) noexcept;
dcl|num=15|since=c++17|until=c++20|1=
template< class T >
constexpr bool operator<=( std::nullopt_t, const optional<T>& opt ) noexcept;
dcl|num=16|since=c++17|until=c++20|1=
template< class T >
constexpr bool operator>( const optional<T>& opt, std::nullopt_t ) noexcept;
dcl|num=17|since=c++17|until=c++20|1=
template< class T >
constexpr bool operator>( std::nullopt_t, const optional<T>& opt ) noexcept;
dcl|num=18|since=c++17|until=c++20|1=
template< class T >
constexpr bool operator>=( const optional<T>& opt, std::nullopt_t ) noexcept;
dcl|num=19|since=c++17|until=c++20|1=
template< class T >
constexpr bool operator>=( std::nullopt_t, const optional<T>& opt ) noexcept;
dcl|num=20|since=c++20|1=
template< class T >
constexpr std::strong_ordering
operator<=>( const optional<T>& opt, std::nullopt_t ) noexcept;
dcl|num=21|since=c++17|1=
template< class T, class U >
constexpr bool operator==( const optional<T>& opt, const U& value );
<!-- Exchanging the template parameters T/U is intentional for
even-numbered overloads in order to simplify the constraints -->
dcl|num=22|since=c++17|1=
template< class U, class T >
constexpr bool operator==( const U& value, const optional<T>& opt );
dcl|num=23|since=c++17|1=
template< class T, class U >
constexpr bool operator!=( const optional<T>& opt, const U& value );
dcl|num=24|since=c++17|1=
template< class U, class T >
constexpr bool operator!=( const U& value, const optional<T>& opt );
dcl|num=25|since=c++17|1=
template< class T, class U >
constexpr bool operator<( const optional<T>& opt, const U& value );
dcl|num=26|since=c++17|1=
template< class U, class T >
constexpr bool operator<( const U& value, const optional<T>& opt );
dcl|num=27|since=c++17|1=
template< class T, class U >
constexpr bool operator<=( const optional<T>& opt, const U& value );
dcl|num=28|since=c++17|1=
template< class U, class T >
constexpr bool operator<=( const U& value, const optional<T>& opt );
dcl|num=29|since=c++17|1=
template< class T, class U >
constexpr bool operator>( const optional<T>& opt, const U& value );
dcl|num=30|since=c++17|1=
template< class U, class T >
constexpr bool operator>( const U& value, const optional<T>& opt );
dcl|num=31|since=c++17|1=
template< class T, class U >
constexpr bool operator>=( const optional<T>& opt, const U& value );
dcl|num=32|since=c++17|1=
template< class U, class T >
constexpr bool operator>=( const U& value, const optional<T>& opt );
dcl|num=33|since=c++20|1=
template< class T, std::three_way_comparable_with<T> U >
constexpr std::compare_three_way_result_t<T, U>
operator<=>( const optional<T>& opt, const U& value );
```

Performs comparison operations on `optional` objects.
@1-7@ Compares two `optional` objects, `lhs` and `rhs`. The contained values are compared (using the corresponding operator of `T`) only if both `lhs` and `rhs` contain values. Otherwise,
* `lhs` is considered ''equal to'' `rhs` if, and only if, both `lhs` and `rhs` do not contain a value.
* `lhs` is considered ''less than'' `rhs` if, and only if, `rhs` contains a value and `lhs` does not.
:@1-6@ Let `@` denote the corresponding comparison operator, for each of these functions:
rev|until=c++26|
If the corresponding expression `*lhs @ *rhs` is ill-formed or its result is not convertible to `bool`, the program is ill-formed.
rev|since=c++26|
.
@8-20@ Compares `opt` with a `nullopt`. Equivalent to  when comparing to an `optional` that does not contain a value.
rrev|since=c++20|
@21-33@ Compares `opt` with a `value`. The values are compared (using the corresponding operator of `T`) only if `opt` contains a value. Otherwise, `opt` is considered ''less than'' `value`.
:@21-32@ Let `@` denote the corresponding comparison operator, for each of these functions:
rev|until=c++26|
If the corresponding expression `*opt @ value` or `value @ *opt` (depending on the positions of the operands) is ill-formed or its result is not convertible to `bool`, the program is ill-formed.
rev|since=c++26|
:
* `U` is not a specialization of `std::optional`.
* The corresponding expression `*opt @ value` or `value @ *opt` (depending on the positions of the operands) is well-formed and its result is convertible to `bool`.

## Parameters


### Parameters

- `lhs, rhs, opt` - an `optional` object to compare
- `value` - value to compare to the contained value

## Return value

1.
2.
3. `!rhs ? false : (!lhs ? true : *lhs < *rhs)`
4. `1=!lhs ? true : (!rhs ? false : *lhs <= *rhs)`
5. `!lhs ? false : (!rhs ? true : *lhs > *rhs)`
6. `1=!rhs ? true : (!lhs ? false : *lhs >= *rhs)`
7. `1=lhs && rhs ? *lhs <=> *rhs : lhs.has_value() <=> rhs.has_value()`
@8,9@ `!opt`
@10,11@ `opt.has_value()`
12. `false`
13. `opt.has_value()`
14. `!opt`
15. `true`
16. `opt.has_value()`
17. `false`
18. `true`
19. `!opt`
20. `1=opt.has_value() <=> false`
21. `1=opt.has_value() ? *opt == value : false`
22. `1=opt.has_value() ? value == *opt : false`
23. `1=opt.has_value() ? *opt != value : true`
24. `1=opt.has_value() ? value != *opt : true`
25. `1=opt.has_value() ? *opt < value  : true`
26. `1=opt.has_value() ? value < *opt  : false`
27. `1=opt.has_value() ? *opt <= value : true`
28. `1=opt.has_value() ? value <= *opt : false`
29. `1=opt.has_value() ? *opt > value  : false`
30. `1=opt.has_value() ? value > *opt  : true`
31. `1=opt.has_value() ? *opt >= value : false`
32. `1=opt.has_value() ? value >= *opt : true`
33. `1=opt.has_value() ? *opt <=> value : std::strong_ordering::less`

## Exceptions

@1-7@
@21-33@ Throws when and what the comparison throws.

## Notes


## Defect reports

