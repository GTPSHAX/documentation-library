---
title: Concepts library
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts
---


# Concepts library mark since c++20

The concepts library provides definitions of fundamental library concepts that can be used to perform compile-time validation of template arguments and perform function dispatch based on properties of types. These concepts provide a foundation for equational reasoning in programs.
Most concepts in the standard library impose both syntactic and semantic requirements. It is said that a standard concept is ''satisfied'' if its syntactic requirements are met, and is ''modeled'' if it is satisfied and its semantic requirements (if any) are also met.
In general, only the syntactic requirements can be checked by the compiler. If the validity or meaning of a program depends whether a sequence of template arguments models a concept, and the concept is satisfied but not modeled, or if a semantic requirement is not met at the point of use, the program is ill-formed, no diagnostic required.

## Equality preservation

An expression is ''equality-preserving'' if it results in equal outputs given equal inputs, where
* the inputs consist of its operands (not neccessarily making the expression semantically valid), and
* the outputs consist of its result and all modifications to the operands by the expression, if any
where, for convenience of wording, its "operands" refer to its largest sub-expressions that consist of an id-expression or invocations of `cpp/utility/move|std::move`, `std::forward`, and `std::declval`.
The cv-qualification and value category of each operand is determined by assuming that each template type parameter in its type denotes a cv-unqualified complete non-array object type.
Every expression required to be equality preserving is further required to be stable, that is, two evaluations of it with the same input objects must have equal outputs without any explicit intervening modification of those input objects.
Unless noted otherwise, every expression used in a `requires` expression of the  is required to be equality preserving, and the evaluation of the expression may modify only its non-constant operands. Operands that are constant must not be modified.
In the standard library, the following concepts are allowed to have non equality-preserving `requires` expressions:
*
*
*
*
*

## Implicit expression variations

A `requires` expression that uses an expression that is non-modifying for some constant lvalue operand also implicitly requires additional variations of that expression that accept a non-constant lvalue or (possibly constant) rvalue for the given operand unless such an expression variation is explicitly required with differing semantics.
These ''implicit expression variations'' must meet the same semantic requirements of the declared expression. The extent to which an implementation validates the syntax of the variations is unspecified.

```cpp
template<class T>
concept C = requires(T a, T b, const T c, const T d)
{
    c == d;           // expression #1: does not modify the operands
    a = std::move(b); // expression #2: modifies both operands
    a = c;            // expression #3: modifies the left operand `a`
};

// Expression #1 implicitly requires additional expression variations that
// meet the requirements for c == d (including non-modification),
// as if the following expressions had been declared as well:

// ------ const == const ------- ------ const == non-const ---
//                                         c  ==           b;
//            c == std::move(d);           c  == std::move(b);
// std::move(c) ==           d;  std::move(c) ==           b;
// std::move(c) == std::move(d); std::move(c) == std::move(b);

// -- non-const == const ------- -- non-const == non-const ---
//           a  ==           d;            a  ==           b;
//           a  == std::move(d);           a  == std::move(b);
// std::move(a) ==           d;  std::move(a) ==           b;
// std::move(a) == std::move(d); std::move(a) == std::move(b);

// Expression #3 implicitly requires additional expression variations that
// meet the requirements for a = c
// (including non-modification of the second operand),
// as if the expressions a = b (non-constant lvalue variation)
// and a = std::move(c) (const rvalue variation) had been declared.

// Note: Since expression #2 already requires the non-constant rvalue variation
// (a == std::move(b)) explicitly, expression #3 does not implicitly require it anymore.

// The type T meets the explicitly stated syntactic requirements of
// concept C above, but does not meet the additional implicit requirements
// (i.e., T satisfies but does not model C):
// a program requires C<T> is ill-formed (no diagnostic required).
struct T
{
    bool operator==(const T&) const { return true; }
    bool operator==(T&) = delete;
};
```


## Standard library concepts


| std | |

#### Core language concepts

| concepts | |
| cpp/concepts/dsc same_as | (see dedicated page) |
| cpp/concepts/dsc derived_from | (see dedicated page) |
| cpp/concepts/dsc convertible_to | (see dedicated page) |
| cpp/concepts/dsc common_reference_with | (see dedicated page) |
| cpp/concepts/dsc common_with | (see dedicated page) |
| cpp/concepts/dsc integral | (see dedicated page) |
| cpp/concepts/dsc signed_integral | (see dedicated page) |
| cpp/concepts/dsc unsigned_integral | (see dedicated page) |
| cpp/concepts/dsc floating_point | (see dedicated page) |
| cpp/concepts/dsc assignable_from | (see dedicated page) |
| cpp/concepts/dsc swappable | (see dedicated page) |
| cpp/concepts/dsc destructible | (see dedicated page) |
| cpp/concepts/dsc constructible_from | (see dedicated page) |
| cpp/concepts/dsc default_initializable | (see dedicated page) |
| cpp/concepts/dsc move_constructible | (see dedicated page) |
| cpp/concepts/dsc copy_constructible | (see dedicated page) |

#### Comparison concepts

| concepts | |
| cpp/concepts/dsc boolean-testable | (see dedicated page) |
| cpp/concepts/dsc equality_comparable | (see dedicated page) |
| cpp/concepts/dsc totally_ordered | (see dedicated page) |
| compare | |
| cpp/utility/compare/dsc three_way_comparable | (see dedicated page) |

#### Object concepts

| concepts | |
| cpp/concepts/dsc movable | (see dedicated page) |
| cpp/concepts/dsc copyable | (see dedicated page) |
| cpp/concepts/dsc semiregular | (see dedicated page) |
| cpp/concepts/dsc regular | (see dedicated page) |

#### Callable concepts

| concepts | |
| cpp/concepts/dsc invocable | (see dedicated page) |
| cpp/concepts/dsc predicate | (see dedicated page) |
| cpp/concepts/dsc relation | (see dedicated page) |
| cpp/concepts/dsc equivalence_relation | (see dedicated page) |
| cpp/concepts/dsc strict_weak_order | (see dedicated page) |

Additional concepts can be found in the iterators library, the algorithms library, and the ranges library.

## See also

* Named Requirements
