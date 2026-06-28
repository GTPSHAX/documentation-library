---
title: Usual arithmetic conversions
type: Language
source: https://en.cppreference.com/w/cpp/language/usual_arithmetic_conversions
---


# Usual arithmetic conversions

Many binary operators that expect operands of `arithmetic` or `enumeration` type cause conversions and yield result types in a similar way. The purpose is to yield a common type, which is also the type of the result. This pattern is called the ''usual arithmetic conversions''.

## Definition

Usual arithmetic conversions are defined as follows:

### Stage 1

Applies  to both operands, the resulting prvalues are used in place of the original operands for the remaining process.

### Stage 2

rrev|since=c++11|
* If either operand is of `scoped enumeration type`, no conversions are performed; if the other operand does not have the same type, the expression is ill-formed.
* Otherwise, proceed to the next stage.

### Stage 3

rrev|since=c++26|
* If either operand is of `enumeration type`, and the other operand is of a different enumeration type or a floating-point type, the expression is ill-formed.
* Otherwise, proceed to the next stage.

### Stage 4

* If either operand is of `floating-point type`, the following rules are applied:
:* If both operands have the same type, no further conversion will be performed.
:* Otherwise, if one of the operands is of a non-floating-point type, that operand is converted to the type of the other operand.
:* Otherwise, if the s of the types of the operands are <sup>(since C++23)</sup> ordered but not equal, then the operand of the type with the lesser floating-point conversion rank is converted to the type of the other operand.
rrev|since=c++23|
:* Otherwise, if the floating-point conversion ranks of the types of the operands are equal, then the operand with the lesser  is converted to the type of the other operand.
:* Otherwise, the expression is ill-formed.
* Otherwise, both operands are of integer types, proceed to the next stage.

### Stage 5

Both operands are converted to a common type `C`. Given the types `T1` and `T2` as the promoted type (`under the rules of integral promotions`) of the operands, the following rules are applied to determine `C`:
* If `T1` and `T2` are the same type, `C` is that type.
* Otherwise, if `T1` and `T2` are both signed integer types or both unsigned integer types, `C` is the type of greater integer conversion rank.
* Otherwise, one type between `T1` and `T2` is an signed integer type `S`, the other type is an unsigned integer type `U`. Apply the following rules:
:* If the integer conversion rank of `U` is greater than or equal to the integer conversion rank of `S`, `C` is `U`.
:* Otherwise, if `S` can represent all of the values of `U`, `C` is `S`.
:* Otherwise, `C` is the unsigned integer type corresponding to `S`.
rrev|since=c++20|until=c++26|
If one operand is of enumeration type and the other operand is of a different enumeration type or a floating-point type, this behavior is deprecated.

## Integer conversion rank

Every `integer type` has an ''integer conversion rank'' defined as follows:
* No two signed integer types other than `char` and `signed char` (if `char` is signed) have the same rank, even if they have the same representation.
* The rank of a signed integer type is greater than the rank of any signed integer type with a smaller width.
* The ranks of the following integer types decrease in order:
rrev|since=c++11|
:* `long long`
:* `long`
:* `int`
:* `short`
:* `signed char`
* The rank of any unsigned integer type equals the rank of the corresponding signed integer type.
rrev|since=c++11|
* The rank of any standard integer type is greater than the rank of any extended integer type with the same width.
* The rank of `bool` is less than the rank of all standard integer types.
* The ranks of encoding character types (`char` <sup>(since C++20)</sup> , `char8_t`<sup>(since C++11)</sup> , `char16_t`, `char32_t`, and `wchar_t`) equal the ranks of their `underlying types`, which means:
:* The rank of `char` equals the rank of `signed char` and `unsigned char`.
rev|since=c++20|
:* The rank of `char8_t` equals the rank of `unsigned char`.
rev|since=c++11|
:* The rank of `char16_t` equals the rank of `std::uint_least16_t`.
:* The rank of `char32_t` equals the rank of `std::uint_least32_t`.
:* The rank of `wchar_t` equals the rank of its implementation-defined underlying type.
rrev|since=c++11|
* The rank of any extended signed integer type relative to another extended signed integer type with the same width is implementation-defined, but still subject to the other rules for determining the integer conversion rank.
* For all integer types `T1`, `T2`, and `T3`, if `T1` has greater rank than `T2` and `T2` has greater rank than `T3`, then `T1` has greater rank than `T3`.
The integer conversion rank is also used in the definition of .

## Floating-point conversion rank and subrank


### Floating-point conversion rank

Every `floating-point type` has a ''floating-point conversion rank'' defined as follows:
* The ranks of the standard floating-point types decrease in order:
** `long double`
** `double`
** `float`
rrev|since=c++23|
* The rank of a floating-point type `T` is greater than the rank of any floating-point type whose set of values is a proper subset of the set of values of `T`.
* Two extended floating-point types with the same set of values have equal ranks.
* An extended floating-point type with the same set of values as exactly one cv-unqualified standard floating-point type has a rank equal to the rank of that standard floating-point type.
* An extended floating-point type with the same set of values as more than one cv-unqualified standard floating-point type has a rank equal to the rank of `double`.
rrev|since=c++23|

### Floating-point conversion subrank

Floating-point types that have equal floating-point conversion ranks are ordered by ''floating-point conversion subrank''. The subrank forms a total order among types with equal ranks.
The types `std::float16_t`, `std::float32_t`, `std::float64_t`, and `std::float128_t` (fixed width floating-point types) have a greater conversion subrank than any standard floating-point type with equal conversion rank. Otherwise, the conversion subrank order is implementation-defined.

### Usage

The floating-point conversion rank and subrank are also used to
* determine whether a conversion between different floating-point types `can be implicit` or is a `narrowing conversion`,
* `distinguish the conversion sequences` in overload resolution,
rrev|since=c++23|
* determine the actual type extracted by  for the extraction of an extended floating-point type using `cpp/io/basic_istream/operator gtgt|std::basic_istream::operator>>`,
* determinte the actual type inserted by  for the insertion of an extended floating-point type using `cpp/io/basic_ostream/operator ltlt|std::basic_ostream::operator<<`,
* determine whether `std::complex`'s converting constructor is explicit, or
* determine the common floating-point type if the arguments of different floating-point types are passed to common or special math functions.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1642 | C++98 | usual arithmetic conversions might involve lvalues | applies lvalue-to-rvalue conversions first |
| cwg-2892 | C++98 | when both operands are of the same<br>floating-point type, the meaning of “no<br>further conversion is needed” was unclear | changed to “no further<br>conversion will be performed” |

