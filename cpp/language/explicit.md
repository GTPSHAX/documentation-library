---
title: explicit specifier
type: Language
source: https://en.cppreference.com/w/cpp/language/explicit
---


# tt|explicit


## Syntax


**Syntax:**

- `sdsc|num=1|`
- `**`explicit`**`
- `|`
- `**`explicit (`** *expression* **`)`**`

### Parameters

- `{{spar` - expression|`contextually converted constant expression of type `bool``
1. Specifies that a constructor <sup>(since C++11)</sup> or conversion function<sup>(since C++17)</sup> or `deduction guide` is explicit, that is, it cannot be used for `implicit conversion`s and `copy-initialization`.
rrev|since=c++20|
2. The `explicit` specifier may be used with a constant expression. The function is explicit if and only if that constant expression evaluates to `true`.
The explicit specifier may only appear within the *decl-specifier-seq* of the declaration of a constructor <sup>(since C++11)</sup> or conversion function within its class definition.

## Notes

A constructor <sup>(until C++11)</sup> with a single non-default parameter that is declared without the function specifier `explicit` is called a `converting constructor`.
Both constructors (other than `copy`/`move`) and user-defined conversion functions may be function templates; the meaning of `explicit` does not change.
rrev|since=c++20|1=
A **`(`** token that follows `explicit` is always parsed as part of the explicit specifier:

```cpp
struct S
{
    explicit (S)(const S&);    // error in C++20, OK in C++17
    explicit (operator int)(); // error in C++20, OK in C++17
};
```


## Keywords

`cpp/keyword/explicit`

## Example


## See also

* `converting constructor`
* `initialization`
* `copy initialization`
* `direct initialization`
