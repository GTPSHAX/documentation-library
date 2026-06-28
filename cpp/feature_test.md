---
title: Feature testing
type: Feature testing
source: https://en.cppreference.com/w/cpp/feature_test
---


# Feature testing mark since c++20

The standard defines a set of preprocessor macros corresponding to C++ language and library features introduced in C++11 or later. They are intended as a simple and portable way to detect the presence of said features.

## Attributes


**Syntax:**

- `*attribute-token* **`)`**`
Checks for the support of an attribute named by *attribute-token* (after macro expansion).
For each standard attribute, it is implementation-defined whether `__has_cpp_attribute` expands to the value given in the table below (which is the year and month in which the attribute was added to the working draft) or `0`. It will expand to given value in the table if and only if the standard attribute causes the implementation to behave as recommended (issuing diagnostic messages, affecting class layout, etc.).
The presence of vendor-specific attributes is determined by a non-zero value.
`__has_cpp_attribute` can be expanded in the expression of `cpp/preprocessor/conditional|#if` and `cpp/preprocessor/conditional|#elif`.
It is treated as a defined macro by `cpp/preprocessor/conditional|#ifdef`, `cpp/preprocessor/conditional|#ifndef`<sup>(since C++23)</sup> , `cpp/preprocessor/conditional|#elifdef`, `cpp/preprocessor/conditional|#elifndef` and `cpp/preprocessor/conditional|defined` but cannot be used anywhere else.


| -#vardefine:counter | 0 |
| spar | attribute-token |
| Attribute |
| <abbr title="The year/month in which this feature was adopted. The hyperlink under each value opens a compiler support page with an entry for that feature.">Value</abbr> |
| <abbr title="Standard in which the attribute is introduced">Std</abbr> |
| Paper(s) |
| assume |
| attr | assume |
| 202207L | link=23#assume |
| 23 |
| P1774R8 |
| carries_dependency |
| attr | carries_dependency |
| 200809L | link=11#carries_dependency |
| 11 | until=26 |
| N2556 N2643 P3475R2 |
| deprecated |
| attr | deprecated |
| 201309L | link=14#deprecated |
| 14 |
| N3760 |
| fallthrough |
| attr | fallthrough |
| 201603L | link=17#fallthrough |
| 17 |
| P0188R1 |
| indeterminate |
| attr | indeterminate |
| 202403L | link=26#indeterminate |
| 26 |
| P2795R5 |
| likely |
| attr | likely |
| 201803L | link=20#likely |
| 20 |
| P0479R5 |
| maybe_unused |
| attr | maybe_unused |
| 201603L | link=17#maybe_unused |
| 17 |
| P0212R1 |
| no_unique_address |
| attr | no_unique_address |
| 201803L | link=20#no_unique_address |
| 20 |
| P0840R2 |
| nodiscard | ftm_span="2" |
| attr | nodiscard |
| 201603L | link=17#nodiscard |
| 17 |
| P0189R1 |
|  |
| attr | nodiscard with reason |
| 201907L | link=20#nodiscard |
| 20 |
| P1301R4 |
| noreturn |
| attr | noreturn |
| 200809L | link=11#noreturn |
| 11 |
| N2761 |
| unlikely |
| attr | likely | unlikely |
| 201803L | link=20#likely |
| 20 |
| P0479R5 |
| - |
| colspan="5" | Total number of attributes: |


## Language features

The following macros can be used to detect whether a language feature is implemented by the current implementation. They are predefined in every translation unit.
Each macro expands to an integer literal corresponding to the year and month when the corresponding feature has been included in the working draft. When a feature changes significantly, the macro will be updated accordingly.

## Library features

The following macros can be used to detect whether a standard library feature is implemented by the current implementation. Unlike the language feature test macros, they are not predefined. Instead, they are provided by the header .
For each library feature test macro, it is also provided by the headers that provide the relevant standard library components. See library feature test macros for a complete list of headers providing these macros.
Each macro expands to an integer literal corresponding to the year and month when the corresponding feature has been included in the working draft. When a feature changes significantly, the macro will be updated accordingly.

## Example


### Normal usage


### Compiler Features Dump


## Defect reports


## See also


## External links

