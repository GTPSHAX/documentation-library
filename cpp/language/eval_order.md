---
title: Order of evaluation
type: Language
source: https://en.cppreference.com/w/cpp/language/eval_order
---


# Order of evaluation

Order of evaluation of any part of any expression, including order of evaluation of function arguments is ''unspecified'' (with some exceptions listed below). The compiler can evaluate operands and other subexpressions in any order, and may choose another order when the same expression is evaluated again.
There is no concept of left-to-right or right-to-left evaluation in C++. This is not to be confused with left-to-right and right-to-left associativity of operators: the expression `a() + b() + c()` is parsed as `(a() + b()) + c()` due to left-to-right associativity of `operator+`, but `c()` may be evaluated first, last, or between `a()` or `b()` at runtime:

### Example

```cpp
#include <cstdio>

int a() { return std::puts("a"); }
int b() { return std::puts("b"); }
int c() { return std::puts("c"); }

void z(int, int, int) {}

int main()
{
    z(a(), b(), c());       // all 6 permutations of output are allowed
    return a() + b() + c(); // all 6 permutations of output are allowed
}
```


**Output:**
```
b
c
a
c
a 
b
```


## "Sequenced before" rules <sup>(C++11)</sup>


### Evaluation of Expressions

Evaluation of each expression includes:
* ''Value computations'': calculation of the value that is returned by the expression. This may involve determination of the identity of the object (glvalue evaluation, e.g. if the expression returns a reference to some object) or reading the value previously assigned to an object (prvalue evaluation, e.g. if the expression returns a number, or some other value).
* Initiation of ''side effects'': access (read or write) to an object designated by a volatile glvalue, modification (writing) to an object, calling a library I/O function, or calling a function that does any of those operations.

### Ordering

''Sequenced before'' is an asymmetric, transitive, pair-wise relationship between evaluations `A` and `B` within the same thread.
* If `A` is sequenced before `B` (or, equivalently, `B` is ''sequenced after'' `A`), then evaluation of `A` will be complete before evaluation of `B` begins.
* If `A` is not sequenced before `B` and `B` is sequenced before `A`, then evaluation of `B` will be complete before evaluation of `A` begins.
* If `A` is not sequenced before `B` and `B` is not sequenced before `A`, then two possibilities exist:
** Evaluations of `A` and `B` are : they may be performed in any order and may overlap (within a single thread of execution, the compiler may interleave the CPU instructions that comprise `A` and `B`).
** Evaluations of `A` and `B` are : they may be performed in any order but may not overlap: either `A` will be complete before `B`, or `B` will be complete before `A`. The order may be the opposite the next time the same expression is evaluated.
Except where noted, evaluations of operands of individual operators and of subexpressions of individual expressions are unsequenced.
rrev|since=c++26|
During the evaluation of an expression as a `core constant expresison`, suboperands and subexpressions that are otherwise unsequenced or indeterminately sequenced are evaluated in lexical order.

### Rules

1. Each `full-expression` is sequenced before the next full-expression.
2. The value computations (but not the side effects) of the operands to any `operator` are sequenced before the value computation of the result of the operator (but not its side effects).
3. When calling a function `func` (whether or not the function is inline, and whether or not explicit function call syntax is used), each item in the following list is sequenced before the next item:
* every argument expression and the postfix expression designating `func`
rrev|since=c++26|
* every `precondition assertion` of `func`
* every expression or statement in the body of `func`
rrev|since=c++26|
* every `postcondition assertion` of `func`
4. The value computation of the built-in `post-increment and post-decrement` operators is sequenced before its side effect.
5. The side effect of the built-in `pre-increment and pre-decrement` operators is sequenced before its value computation (implicit rule due to definition as compound assignment).
6. The first (left) operand of the built-in `logical` AND operator `&&`, the built-in logical OR operator ` and the built-in `comma operator` `,` is sequenced before the second (right) operand.
7. The first operand in the  `?:` is sequenced before the second or third operand.
8. The side effect (modification of the left operand) of the built-in `assignment` operator and of all built-in `compound` assignment operators is sequenced after the value computation (but not the side effects) of both left and right operands, and is sequenced before the value computation of the assignment expression (that is, before returning the reference to the modified object).
9. In `list-initialization`, every value computation and side effect of a given initializer clause is sequenced before every value computation and side effect associated with any initializer clause that follows it in the brace-enclosed comma-separated list of initializers.
10. A function call that is not sequenced before or sequenced after another expression evaluation outside of the function (possibly another function call) is indeterminately sequenced with respect to that evaluation (the program must behave `as if` the CPU instructions that constitute a function call were not interleaved with instructions constituting evaluations of other expressions, including other function calls, even if the function was inlined).
<sup>(since C++17)</sup> The rule 10 has one exception: function calls made by a standard library algorithm executing under `cpp/algorithm/execution_policy_tag_t|std::execution::par_unseq` execution policy are unsequenced and may be arbitrarily interleaved with each other.
11. The call to the allocation function (`cpp/memory/new/operator new|operator new`) is <sup>(until C++17)</sup> indeterminately sequenced with respect to<sup>(since C++17)</sup> sequenced before the evaluation of the constructor arguments in a ``new` expression`.
12. When returning from a function, copy-initialization of the temporary that is the result of evaluating the function call is sequenced before the destruction of all temporaries at the end of the operand of the ``return` statement`, which, in turn, is sequenced before the destruction of local variables of the block enclosing the `return` statement.
rev|since=c++17|
13. In a function-call expression, the expression that names the function is sequenced before every argument expression and every default argument.
14. In a function call, value computations and side effects of the initialization of every  parameter are indeterminately sequenced with respect to value computations and side effects of any other parameter.
15. Every overloaded operator obeys the sequencing rules of the built-in operator it overloads when called using operator notation.
16. In a subscript expression `E1[E2]`, `E1` is sequenced before `E2`.
17. In a pointer-to-member expression `E1.*E2` or `E1->*E2`, `E1` is sequenced before `E2`.
18. In a shift operator expression `E1 << E2` and `E1 >> E2`, `E1` is sequenced before `E2`.
19. In every simple assignment expression `1=E1 = E2` and every compound assignment expression `1=E1 @= E2`, `E2` is sequenced before `E1`.
20. In `direct initialization` of non-aggregate class, every expression in a parenthesized initializer is evaluated as if for a function call (indeterminately-sequenced).
rev|since=c++20|
21. In `direct initialization` of aggregate, the initialization of every aggregate element is sequenced before the initialization of the next element.

### Undefined behavior

The behavior is `undefined` in the following cases:
1. A side effect on a  is unsequenced relative to another side effect on the same memory location:

```cpp
i = ++i + 2;       // well-defined
i = i++ + 2;       // undefined behavior until C++17
f(i = -2, i = -2); // undefined behavior until C++17
f(++i, ++i);       // undefined behavior until C++17, unspecified after C++17
i = ++i + i++;     // undefined behavior
```

2. A side effect on a memory location is unsequenced relative to a value computation using the value of any object in the same memory location:

```cpp
cout << i << i++; // undefined behavior until C++17
a[i] = i++;       // undefined behavior until C++17
n = ++i + i;      // undefined behavior
```

3. Starting or ending the `lifetime` of an object in a memory location is unsequenced relative to any of the following operations:
* a side effect on the same memory location
* a value computation using the value of any object in the same memory location
* starting or ending the lifetime of an object occupying storage that overlaps with the memory location

```cpp
union U { int x, y; } u;
(u.x = 1, 0) + (u.y = 2, 0); // undefined behavior
```


## Sequence point rules <sup>(until C++11)</sup>


### Pre-C++11 Definitions

Evaluation of an expression might produce side effects, which are: accessing an object designated by a volatile lvalue, modifying an object, calling a library I/O function, or calling a function that does any of those operations.
A ''sequence point'' is a point in the execution sequence where all side effects from the previous evaluations in the sequence are complete, and no side effects of the subsequent evaluations started.

### Pre-C++11 Rules

1. There is a sequence point at the end of each `full-expression` (typically, at the semicolon).
2. When calling a function (whether or not the function is inline and whether or not function call syntax was used), there is a sequence point after the evaluation of all function arguments (if any) which takes place before execution of any expressions or statements in the function body.
3. When returning from a function, there is a sequence point after the copy-initialization of the result of the function call, and before the destruction of all temporary objects at the end of *expression* in the ``return` statement` (if any).
4. There is a sequence point after the copying of a returned value of a function and before the execution of any expressions outside the function.
5. Once the execution of a function begins, no expressions from the calling function are evaluated until execution of the called function has completed (functions cannot be interleaved).
6. In the evaluation of each of the following four expressions, using the built-in (non-overloaded) operators, there is a sequence point after the evaluation of the expression `a`.

```cpp
a && b
a {{!!
```

a ? b : c
a , b

### Pre-C++11 Undefined behavior

The behavior is `undefined` in the following cases:
1. Between the previous and next sequence point, the value of any object in a memory location is modified more than once by the evaluation of an expression:

```cpp
i = ++i + i++;     // undefined behavior
i = i++ + 1;       // undefined behavior
i = ++i + 1;       // undefined behavior
++ ++i;            // undefined behavior
f(++i, ++i);       // undefined behavior
f(i = -1, i = -1); // undefined behavior
```

2. Between the previous and next sequence point, for an object whose value is modified by the evaluation of an expression, its prior value is accessed in a way other than to determine the value to be stored:

```cpp
cout << i << i++; // undefined behavior
a[i] = i++;       // undefined behavior
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1885 | C++11 | sequencing of the destruction of automatic<br>variables on function return was not explicit | sequencing rules added |
| cwg-1949 | C++11 | “sequenced after” was used but not defined in the C++ standard | defined as the inverse<br>of “sequenced before” |
| cwg-1953 | C++11 | side effects and value computations involving a memory<br>location could be unsequenced relative to starting or ending<br>the lifetime of an object in the same memory location | the behavior is<br>undefined in this case |
| cwg-2146 | C++98 | the cases involving undefined behaviors did not consider bit-fields | considered |


## References


## See also

* `Operator precedence` which defines how expressions are built from their source code representation.
