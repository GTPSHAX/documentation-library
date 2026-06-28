---
title: Other operators
type: Language
source: https://en.cppreference.com/w/cpp/language/operator_other
---


# Other operators


| - |
| rowspan="2" | Operator<br>name |
| rowspan="2" style="min-width: 70px;" | Syntax |
| rowspan="2" | rlp | operators | Over&#8203;load&#8203;able |
| colspan="2" | Prototype examples (for c/core | class T) |
| - |
| Inside class definition |
| Outside class definition |
| - |
| function call |
| tt | a(a1, a2) |
|  |
| c | R T::operator()(Arg1 &a1, Arg2 &a2, ...); |
|  |
| - |
| comma |
| tt | a, b |
|  |
| c | T2& T::operator,(T2 &b); |
| c | T2& operator,(const T &a, T2 &b); |
| - |
| conditional operator |
| tt | a ? b : c |
|  |
|  |
|  |

The ''function call'' operator provides function semantics for any object.
The ''conditional operator'' (colloquially referred to as ''ternary conditional'') checks the boolean value of the first expression and,  depending on the resulting value, evaluates and returns either the second or the third expression.

## Built-in function call operator

Function call expressions have the following form:

**Syntax:**

- `**`(`***arg1***`,`** *arg2***`,`** *arg3***`,`**...**`)`**`

### Parameters

- `{{spar` - function|an expression function type or function pointer type
- `{{spar` - arg1**`,`** *arg2***`,`** *arg3***`,`**...|a possibly empty list of arbitrary expressions<sup>(since C++11)</sup>  or `brace-enclosed initializer lists`, except the comma operator is not allowed at the top level to avoid ambiguity
For a call to a non-member function or to a `static member function`, *function* can be an lvalue that refers to a function (in which case the  is suppressed), or a prvalue of function pointer type.
The function (or member) name specified by *function* can be overloaded, `overload resolution` rules used to decide which overload is to be called.
If *function* specifies a member function, it may be virtual, in which case the final overrider of that function will be called, using dynamic dispatch at runtime.
Each function parameter is initialized with its corresponding argument after `implicit conversion` if necessary.
* If there is no corresponding argument, the corresponding `default argument` is used, and if there is none, the program is ill-formed.
* If the call is made to a member function, then the `this` pointer to current object is converted as if by explicit cast to the `this` pointer expected by the function.
* The initialization and destruction of each parameter occurs in the context of the `full-expression` where the function call appears, which means, for example, that if a constructor or destructor of a parameter throws an exception, the `function `try` blocks` of the called function are not considered.
If the function is a variadic function, `default argument promotions` are applied to all arguments matched by the ellipsis parameter.
It is implementation-defined whether a parameter is destroyed when the function in which it is defined exits or at the end of the enclosing full-expression. Parameters are always destroyed in the reverse order of their construction.
The return type of a function call expression is the return type of the chosen function, decided using static binding (ignoring the `virtual` keyword), even if the overriding function that is actually called returns a different type. This allows the overriding functions to return pointers or references to classes that are derived from the return type returned by the base function, i.e. C++ supports [Covariant return type|covariant return types](https://en.wikipedia.org/wiki/Covariant return type|covariant return types). If *function* specifies a destructor, the return type is `void`.
rrev|since=c++17|
When an object of class type `X` is passed to or returned from a function, if each copy constructor, move constructor, and destructor of `X` is either trivial or deleted, and `X` has at least one non-deleted copy or move constructor, implementations are permitted to create a temporary object to hold the function parameter or result object.
The temporary object is constructed from the function argument or return value, respectively, and the function's parameter or return object is initialized as if by using the non-deleted trivial constructor to copy the temporary (even if that constructor is inaccessible or would not be selected by overload resolution to perform a copy or move of the object).
This allows objects of small class types, such as `std::complex` or `std::span`, to be passed to or returned from functions in registers.
The value category of a function call expression is lvalue if the function returns an lvalue reference or an rvalue reference to function, is an xvalue if the function returns an rvalue reference to object, and is a prvalue otherwise. If the function call expression is a prvalue of object type, it must have `complete type`<sup>(since C++11)</sup>  except when used as the operand of `built-in comma operator]] that is the operand of `decltype`)`.
rrev|since=c++26|
When the called function exits normally, all  of the function are `evaluated in sequence`. If the implementation introduces any `temporary objects` to hold the result value, for the evaluation `E` of each postcondition assertion:
* `E` is `indeterminately sequenced` with respect to the initialization of any of those temporaries or the result object.
* `E` is `sequenced before` the destruction of any function parameter.
Function call expression is similar in syntax to value initialization `T()`, to `function-style cast` expression `T(A1)`, and to direct initialization of a temporary `T(A1, A2, A3, ...)`, where `T` is the name of a type.

### Example

```cpp
#include <cstdio>

struct S
{
    int f1(double d)
    {
        return printf("%f \n", d); // variable argument function call
    }

    int f2()
    {
        return f1(7); // member function call, same as this->f1()
                      // integer argument converted to double
    }
};

void f()
{
    puts("function called"); // function call
}

int main()
{
    f();    // function call
    S s;
    s.f2(); // member function call
}
```


**Output:**
```
function called
7.000000
```


## Built-in comma operator

Comma expressions have the following form:

**Syntax:**

- `**`,`** *E2*`
In a comma expression `E1, E2`, the expression `E1` is evaluated, its result is `discarded` (although if it has class type, it won't be destroyed `until the end of the containing full expression`), and its side effects are completed before evaluation of the expression `E2` begins <sup>(until C++17)</sup> (note that a user-defined `operator,` cannot guarantee sequencing).
The type, value, and value category of the result of the comma expression are exactly the type, value, and value category of the second operand, `E2`. If `E2` is a temporary <sup>(since C++17)</sup> expression, the result of the expression is that temporary <sup>(since C++17)</sup> expression. If `E2` is a bit-field, the result is a bit-field.
The comma in various comma-separated lists, such as function argument lists (`f(a, b, c)`) and initializer lists }, is not the comma operator. If the comma operator needs to be used in such contexts, it has to be parenthesized: `f(a, (n++, n + b), c)`.
rrev multi
|since1=c++20|rev1=
Using an unparenthesized comma expression as second (right) argument of a `subscript operator` is deprecated.
For example, `a[b, c]` is deprecated and `a[(b, c)]` is not.
|since2=c++23|rev2=
An unparenthesized comma expression cannot be second (right) argument of a `subscript operator`. For example, `a[b, c]` is either ill-formed or equivalent to `a.operator[](b, c)`.
Parentheses are needed when using a comma expression as the subscript, e.g., `a[(b, c)]`.

### Example

```cpp
#include <iostream>

int main()
{
    // comma is often used to execute more than one expression
    // where the language grammar allows only one expression:

    // * in the third component of the for loop
    for (int i = 0, j = 10; i <= j; ++i, --j)
    //            ^list separator      ^comma operator
        std::cout << "i = " << i << " j = " << j << '\n';

    // * in a return statement
    // return log("an error!"), -1;

    // * in an initializer expression
    // MyClass(const Arg& arg)
    // : member{ throws_if_bad(arg), arg }

    // etc.

    // comma operators can be chained; the result of the last
    // (rightmost) expression is the result of the whole chain:
    int n = 1;
    int m = (++n, std::cout << "n = " << n << '\n', ++n, 2 * n);

    // m is now 6
    std::cout << "m = " << (++m, m) << '\n';
}
```


**Output:**
```
i = 0 j = 10
i = 1 j = 9
i = 2 j = 8
i = 3 j = 7
i = 4 j = 6
i = 5 j = 5
n = 2
m = 7
```


## Conditional operator

The conditional operator expressions have the form

**Syntax:**

- `**`?`** *E2* **`:`** *E3*`
*E1* is evaluated and `contextually converted` to `bool`, if the result is `true`, the result of the conditional expression is the value of E2; otherwise the result of the conditional expression is the value of E3.
The type and value category of the conditional expression `E1 ? E2 : E3` are determined as follows:

### Stage 1

If both `E2` and `E3` are of type `void`, the result is <sup>(until C++11)</sup> an rvalue<sup>(since C++11)</sup> a prvalue of type `void`.
If exactly one of `E2` and `E3` is of type `void`:
* If that operand of type `void` is be a (possibly parenthesized) ``throw` expression`, the result has the type and the value category of the other operand. If the other operand is a `bit-field`, the result is also a bit-field.
* Otherwise, the program is ill-formed.
If neither of `E2` and `E3` is of type `void`, proceed to the next stage.

```cpp
2 + 2 == 4 ? throw 123 : throw 456; // the result is of type “void”

2 + 2 != 4 ? "OK" : throw "error";  // the result is of type “const char[3]”
                                    // even if an exception is always thrown
```


### Stage 2

If `E2` or `E3` are <sup>(until C++11)</sup> lvalue bit-fields<sup>(since C++11)</sup> glvalue bit-fields of the same value category and of types ''cv1'' `T` and ''cv2'' `T`, respectively, the operands are considered to be of type ''cv'' `T` for the remaining process, where ''cv'' is the union of ''cv1'' and ''cv2''.
If `E2` and `E3` have different types, and any of the following conditions is satisfied, proceed to stage 3:
* At least one of `E2` and `E3` is a (possibly cv-qualified) class type.
* Both of `E2` and `E3` are <sup>(until C++11)</sup> lvalues of the same type<sup>(since C++11)</sup> glvalues of the same value category and the same type except for cv-qualification.
Otherwise, proceed to stage 4.

### Stage 3

Attempts are made to form an `implicit conversion sequence`<ref>`Member access`<sup>(since C++11)</sup> , whether a conversion function is deleted and whether an operand is a bit-field are ignored.</ref> from an operand expression `X` of type `TX` to a ''target type'' related to the type `TY` of the operand expression `Y` as follows:
* If `Y` is an lvalue, the target type is `TY&`, but an implicit conversion sequence can only be formed if the reference would `bind directly` to <sup>(until C++11)</sup> an lvalue<sup>(since C++11)</sup> a glvalue.
rrev|since=c++11|
* If `Y` is an xvalue, the target type is `TY&&`, but an implicit conversion sequence can only be formed if the reference would bind directly.
* If `Y` is <sup>(until C++11)</sup> an rvalue<sup>(since C++11)</sup> a prvalue or if none of the conversion sequences above can be formed, and at least one of `TX` and `TY` is a (possibly cv-qualified) class type:
** If `TX` and `TY` are the same class type (ignoring cv-qualification):
*** If `TY` is at least as cv-qualified as `TX`, the target type is `TY`.
*** Otherwise, no conversion sequence is formed.
** Otherwise, if `TY` is a base class of `TX`, the target type is `TY` with the cv-qualifiers of `TX`.
** Otherwise, the target type is the type of `Z`, where `Z` is the value of `Y` after applying the lvalue-to-rvalue, array-to-pointer, and function-to-pointer `standard conversions`.
* Otherwise, no conversion sequence is formed.
Using this process, it is determined whether an implicit conversion sequence can be formed from `E2` to the target type determined for the `E3`, and vice versa.
* If no conversion sequence can be formed, proceed to the next stage.
* If exactly one conversion sequence can be formed:
** If the conversion sequence is ambiguous, the program is ill-formed.
** Otherwise, that conversion is applied to the chosen operand and the converted operand is used in place of the original operand for the remaining process, and proceed to the next stage.
* If both sequences can be formed, the program is ill-formed.

```cpp
struct A {};

struct B : A {};

using T = const B;

A a = true ? A() : T(); // Y = A(), TY = A, X = T(), TX = const B, Target = const A
```


### Stage 4

rev|until=c++11|
If `E2` and `E3` are lvalues of the same type, then the result is an lvalue of that type, and is a bit-field if at least one of `E2` and `E3` is a bit-field.
rev|since=c++11|
If `E2` and `E3` are glvalues of the same type and the same value category, then the result has the same type and value category, and is a bit-field if at least one of `E2` and `E3` is a bit-field.
Otherwise, the result is <sup>(until C++11)</sup> an rvalue<sup>(since C++11)</sup> a prvalue.
* If `E2` and `E3` do not have the same type, and either has (possibly cv-qualified) class type, proceed to stage 5.
* Otherwise, proceed to stage 6.

### Stage 5

`Overload resolution` is performed using the built-in candidates to attempt to convert the operands to built-in types:
* If the overload resolution fails, the program is ill-formed.
* Otherwise, the selected conversions are applied and the converted operands are used in place of the original operands for the remaining process. Proceed to the next stage.

### Stage 6

The array-to-pointer and function-to-pointer conversions are applied to (possibly-converted) `E2` and `E3`. After those conversions, at least one of the following conditions must hold, otherwise the program is ill-formed:
* `E2` and `E3` have the same type. In this case, the result is of that type and the result is `copy-initialized` using the selected operand.
* Both `E2` and `E3` have arithmetic or enumeration type. In this case, `usual arithmetic conversions` are applied to bring them to their common type, and the result is of that type.
* At least one of `E2` and `E3` is a pointer. In this case, lvalue-to-rvalue, pointer<sup>(since C++17)</sup> , function pointer and qualification conversions are applied to bring them to their , and the result is of that type.
* At least one of `E2` and `E3` is a pointer to member. In this case, lvalue-to-rvalue, pointer-to-member<sup>(since C++17)</sup> , function pointer and qualification conversions are applied to bring them to their , and the result is of that type.
rrev|since=c++11|
* Both `E2` and `E3` are null pointer constants, and at least one of which is of type `std::nullptr_t`. In this case, the result is of type `std::nullptr_t`.

```cpp
int* intPtr;

using Mixed = decltype(true ? nullptr : intPtr);

static_assert(std::is_same_v<Mixed, int*>); // nullptr becoming int*

struct A
{
    int* m_ptr;
} a;

int* A::* memPtr = &A::m_ptr; // memPtr is a pointer to member m_ptr of A

// memPtr makes nullptr as type of pointer to member m_ptr of A
static_assert(std::is_same_v<decltype(false ? memPtr : nullptr), int*A::*>);

// a.*memPtr is now just pointer to int and nullptr also becomes pointer to int
static_assert(std::is_same_v<decltype(false ? a.*memPtr : nullptr), int*>);
```

rrev|since=c++11|
The result type of a conditional operator is also accessible as the binary type trait `std::common_type`.

### Overloads

For every pair of promoted arithmetic types `L` and `R` and for every type `P`, where `P` is a pointer, pointer-to-member, or scoped enumeration type, the following function signatures participate in overload resolution:

```cpp
```

where LR is the result of `usual arithmetic conversions` performed on `L` and `R`.
The operator “`?:`” cannot be overloaded, these function signatures only exist for the purpose of overload resolution.

### Example

```cpp
#include <iostream>
#include <string>

struct Node
{
    Node* next;
    int data;

    // deep-copying copy constructor
    Node(const Node& other)
        : next(other.next ? new Node(*other.next) : NULL)
        , data(other.data)
    {}

    Node(int d) : next(NULL), data(d) {}

    ~Node() { delete next; }
};

int main()
{   
    // simple rvalue example
    int n = 1 > 2 ? 10 : 11;  // 1 > 2 is false, so n = 11

    // simple lvalue example
    int m = 10; 
    (n == m ? n : m) = 7; // n == m is false, so m = 7

    //output the result
    std::cout << "n = " << n << "\nm = " << m;
}
```


**Output:**
```
n = 11
m = 7
```


## Standard library

Many classes in the standard library overload `operator()` to be used as function objects.


| cpp/memory/default_delete/dsc operator() | (see dedicated page) |
| cpp/utility/functional/plus/dsc operator() | (see dedicated page) |
| cpp/utility/functional/minus/dsc operator() | (see dedicated page) |
| cpp/utility/functional/multiplies/dsc operator() | (see dedicated page) |
| cpp/utility/functional/divides/dsc operator() | (see dedicated page) |
| cpp/utility/functional/modulus/dsc operator() | (see dedicated page) |
| cpp/utility/functional/negate/dsc operator() | (see dedicated page) |
| cpp/utility/functional/equal_to/dsc operator() | (see dedicated page) |
| cpp/utility/functional/not_equal_to/dsc operator() | (see dedicated page) |
| cpp/utility/functional/greater/dsc operator() | (see dedicated page) |
| cpp/utility/functional/less/dsc operator() | (see dedicated page) |
| cpp/utility/functional/greater_equal/dsc operator() | (see dedicated page) |
| cpp/utility/functional/less_equal/dsc operator() | (see dedicated page) |
| cpp/utility/functional/logical_and/dsc operator() | (see dedicated page) |
| cpp/utility/functional/logical_or/dsc operator() | (see dedicated page) |
| cpp/utility/functional/logical_not/dsc operator() | (see dedicated page) |
| cpp/utility/functional/bit_and/dsc operator() | (see dedicated page) |
| cpp/utility/functional/bit_or/dsc operator() | (see dedicated page) |
| cpp/utility/functional/bit_xor/dsc operator() | (see dedicated page) |
| cpp/utility/functional/unary_negate/dsc operator() | (see dedicated page) |
| cpp/utility/functional/binary_negate/dsc operator() | (see dedicated page) |
| cpp/utility/functional/reference_wrapper/dsc operator() | (see dedicated page) |
| cpp/utility/functional/function/dsc operator() | (see dedicated page) |
| cpp/utility/functional/move_only_function/dsc operator() | (see dedicated page) |
| cpp/utility/functional/copyable_function/dsc operator() | (see dedicated page) |
| cpp/coroutine/coroutine_handle/dsc operator() | (see dedicated page) |
| cpp/locale/locale/dsc operator() | (see dedicated page) |
| cpp/container/value_compare/dsc operator()|map | (see dedicated page) |
| cpp/container/value_compare/dsc operator()|multimap | (see dedicated page) |
| cpp/thread/packaged_task/dsc operator() | (see dedicated page) |
| cpp/numeric/random/engine/dsc operator()|linear_congruential_engine | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator()|uniform_int_distribution | (see dedicated page) |

The comma operator is not overloaded by any class in the standard library. The boost library uses `operator,` in [https://www.boost.org/doc/libs/release/libs/assign/doc/index.html#intro boost.assign], [https://www.boost.org/doc/libs/release/libs/spirit/doc/html/index.html boost.spirit], and other libraries. The database access library [https://soci.sourceforge.net/doc.html SOCI] also overloads `operator,`.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-446 | C++98 | it was unspecified whether a temporary is created for an<br>lvalue-to-rvalue conversion on the conditional operator | always creates a temporary if<br>the operator returns a class rvalue |
| cwg-462 | C++98 | if the second operand of a comma operator is a temporary,<br>it was unspecified whether its lifetime will be extended when<br>the result of the comma expression is bound to a reference | the result of the comma expression<br>is the temporary in this case<br>(hence its lifetime is extended) |
| cwg-587 | C++98 | when the second and third operands of a conditional<br>operator are lvalues of the same type except for<br>cv-qualification, the result was an lvalue if these<br>operands have class types or an rvalue otherwise | the result is always<br>an lvalue in this case |
| cwg-1029 | C++98 | the type of a destructor call was unspecified | specified as c/core |
| cwg-1895 | C++98<br>C++11 | unclear if deleted (C++11) or inaccessible (C++98)<br>conversion function prevents conversion in<br>conditional expressions, and conversions from base<br>class to derived class prvalue were not considered | handled like<br>overload resolution |
| cwg-1932 | C++98 | same-type bit-fields were missing in conditional expressions | handled by underlying types |
| cwg-2226 | C++11 | when determining the target type of the other<br>operand of a conditional operator, reference could<br>not bind to an xvalue if that operand is an lvalue | allowed |
| cwg-2321 | C++98 | when determining the target type of the other operand<br>of a conditional operator, a derived class type could<br>not be converted to a less cv-qualified base class type | allowed to convert to the base<br>class type with the cv-qualification<br>from the derived class operand |
| cwg-2715 | C++98 | the initialization and destruction of each<br>parameter would occur within the context of<br>the calling function, which might not exist | occurs within the context of<br>the enclosing full-expression |
| cwg-2850 | C++98 | the destruction order of parameters was unclear | made clear |
| cwg-2906 | C++98 | lvalue-to-rvalue conversions were unconditionally applied<br>in the rvalue result case for the conditional operator | only applied in some cases |


## See also

`Operator precedence`<br>
`Operator overloading`
