---
title: Attribute specifier sequence(since C++11)
type: Language
source: https://en.cppreference.com/w/cpp/language/attributes
---


# Attribute specifier sequence mark since c++11

Introduces implementation-defined attributes for types, objects, code, etc.

## Syntax


**Syntax:**

- `|1=`
- `**`[[`** *attribute-list* **`]]`**`
- `|1=`
- `**`[[`** **`using`** *attribute-namespace* **`:`** *attribute-list* **`]]`**`
where *attribute-list* is a comma-separated sequence of zero or more attributes (possibly ending with an ellipsis **`...`** indicating a `pack expansion`)

**Syntax:**

- `**`::`** *identifier*`
- `**`(`** *argument-list* (optional) **`)`**`
- `**`::`** *identifier* **`(`** *argument-list* (optional) **`)`**`
where *attribute-namespace* is an *identifier* and *argument-list* is a sequence of tokens where parentheses, brackets and braces are balanced (*balanced-token-seq*).
1. Simple attribute, such as `noreturn`.
2. Attribute with a namespace, such as `gnu::unused`.
3. Attribute with arguments, such as `deprecated("because")`.
4. Attribute with both a namespace and an argument list.
rrev|since=c++17|
If `using namespace:` appears in the beginning of an attribute list, no other attributes in the attribute list can specify a namespace: the namespace specified in a using applies to them all:

```cpp
[[using CC: opt(1), debug]] // same as [[CC::opt(1), CC::debug]]
[[using CC: CC::opt(1)]] // error: cannot combine using and scoped attribute
```

rrev|since=c++26|
If every item in the attribute specifier starts with `, the attribute specifier instead introduces `annotations`. Attributes (not starting with `) and annotations (starting with `) cannot be intermixed in an attribute specifier.

## Explanation

Attributes provide the unified standard syntax for implementation-defined language extensions, such as the GNU and IBM language extensions `__attribute__((...))`, Microsoft extension `__declspec()`, etc.
An attribute can be used almost everywhere in the C++ program, and can be applied to almost everything: to types, to variables, to functions, to names, to code blocks, to entire translation units, although each particular attribute is only valid where it is permitted by the implementation:  could be an attribute that can only be used with an `if`, and not with a class declaration.  could be an attribute that applies to a code block or to a `for` loop, but not to the type `int`, etc (note these two attributes are fictional examples, see below for the standard and some non-standard attributes).
In declarations, attributes may appear both before the whole declaration and directly after the name of the entity that is declared, in which case they are combined. In most other situations, attributes apply to the directly preceding entity.
The ``alignas` specifier` is a part of the attribute specifier sequence, although it has different syntax. It may appear where the `[<nowiki/>[...]]` attributes appear and may mix with them (provided it is used where `alignas` is permitted).
Two consecutive left square bracket tokens (`[[`) may only appear when introducing an attribute-specifier or inside an attribute argument.

```cpp
void f()
{
    int y[3];
    y[<!---->[] { return 0; }()] = 1;  // error
    int i [[cats::meow([[]])]]; // OK
}
```

Besides the standard attributes listed below, implementations may support arbitrary non-standard attributes with implementation-defined behavior. <sup>(since C++17)</sup> All attributes unknown to an implementation are ignored without causing an error.
rrev|since=c++20|
An attribute without *attribute-namespace* and an *attribute-namespace* whose name is either `std` or `std` followed by one or more digits is reserved for future standardization. That is, every non-standard attribute is in the *attribute-namespace* provided by the implementation, e.g. , , and .

## Standard attributes

The following attributes are defined by the C++ standard.
Standard attributes cannot be syntactically ignored: they cannot contain syntax errors, must be applied to the correct target, and entities in the arguments must be .
Standard attributes cannot be semantically ignored either: the behavior with all instances of a particular standard attribute removed would have been a conforming behavior for the original program with the attribute present.


| cpp/language/attributes/dsc noreturn | (see dedicated page) |
| cpp/language/attributes/dsc carries_dependency | (see dedicated page) |
| cpp/language/attributes/dsc deprecated | (see dedicated page) |
| cpp/language/attributes/dsc fallthrough | (see dedicated page) |
| cpp/language/attributes/dsc maybe_unused | (see dedicated page) |
| cpp/language/attributes/dsc nodiscard | (see dedicated page) |
| cpp/language/attributes/dsc likely | (see dedicated page) |
| cpp/language/attributes/dsc no_unique_address | (see dedicated page) |
| cpp/language/attributes/dsc assume | (see dedicated page) |
| cpp/language/attributes/dsc indeterminate | (see dedicated page) |
| cpp/language/attributes/dsc optimize_for_synchronized | (see dedicated page) |


## Notes

The presence of each individual attribute on a given platform can be checked with `__has_cpp_attribute` preprocessor macro.

## Example


### Example

```cpp
[[gnu::always_inline]] [[gnu::hot]] [[gnu::const]] [[nodiscard]]
inline int f(); // declare f with four attributes

[[gnu::always_inline, gnu::const, gnu::hot, nodiscard]]
int f(); // same as above, but uses a single attr specifier that contains four attributes

// C++17:
[[using gnu : const, always_inline, hot]] [[nodiscard]]
int f[[gnu::always_inline]](); // an attribute may appear in multiple specifiers

int f() { return 0; }

int main() {}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-2538 | C++11 | it was unclear whether standard attributes can be syntactically ignored | prohibited |
| cwg-2695 | C++11 | it was unclear whether standard attributes can be semantically ignored | prohibited |


## See also


## External links

