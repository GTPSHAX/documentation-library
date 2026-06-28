---
title: Operator Precedence
type: Language
source: https://en.cppreference.com/w/cpp/language/operator_precedence
---


# C++ Operator Precedence

The following table lists the precedence and associativity of C++ operators. Operators are listed top to bottom, in descending precedence. `a`, `b` and `c` are operands.


| - |
| style="text-align: left" | Precedence |
| style="text-align: left" | Operator |
| style="text-align: left" | Description |
| style="text-align: left" | Associativity |
| - |
| 1 |
| c | a::b |
| rlp | identifiers#Qualified identifiers | Scope resolution |
| style="vertical-align: top" rowspan="6" | Left-to-right &#8594; |
| - style="border-top: 1px solid #aaa" |
| rowspan=5 | 2 |
| style="border-bottom-style: none" | c | a++c | a-- |
| style="border-bottom-style: none" | Suffix/postfix rlp | operator incdec | increment and decrement |
| - |
| style="border-bottom-style: none; border-top-style: none" | box | tt | ''type''c/core | (a)box | tt | ''type''c/core | {a} |
| style="border-bottom-style: none; border-top-style: none" | rlp | explicit cast | Functional cast |
| - |
| style="border-bottom-style: none; border-top-style: none" | c | a() |
| style="border-bottom-style: none; border-top-style: none" | rlp | operator other#Built-in function call operator | Function call |
| - |
| style="border-bottom-style: none; border-top-style: none" | c | a[] |
| style="border-bottom-style: none; border-top-style: none" | rlp | operator member access#Built-in subscript operator | Subscript |
| - |
| style="border-bottom-style: none; border-top-style: none" | c | a.bc | a->b |
| style="border-bottom-style: none; border-top-style: none" | rlp | operator member access#Built-in member access operators | Member access |
| - style="border-top: 1px solid #aaa" |
| rowspan=11 | 3 |
| style="border-bottom-style: none" | c | ++ac | --a |
| style="border-bottom-style: none" | Prefix rlp | operator incdec | increment and decrement |
| style="vertical-align: top" rowspan="11" | Right-to-left &#8592; |
| - |
| style="border-bottom-style: none; border-top-style: none" | c | +ac | -a |
| style="border-bottom-style: none; border-top-style: none" | Unary rlp | operator arithmetic#Unary arithmetic operators | plus and minus |
| - |
| style="border-bottom-style: none; border-top-style: none" | c | !ac | ~a |
| style="border-bottom-style: none; border-top-style: none" | rlp | operator logical | Logical NOT and rlp | operator arithmetic#Bitwise logic operators | bitwise NOT |
| - |
| style="border-bottom-style: none; border-top-style: none" | box | c/core | (tt | ''type''c/core | )a |
| style="border-bottom-style: none; border-top-style: none" | rlp | explicit cast | C-style cast |
| - |
| style="border-bottom-style: none; border-top-style: none" | c | *a |
| style="border-bottom-style: none; border-top-style: none" | rlp | operator member access#Built-in indirection operator | Indirection (dereference) |
| - |
| style="border-bottom-style: none; border-top-style: none" | c | &a |
| style="border-bottom-style: none; border-top-style: none" | rlp | operator member access#Built-in address-of operator | Address-of |
| - |
| style="border-bottom-style: none; border-top-style: none" | c | ^^a |
| style="border-bottom-style: none; border-top-style: none" | rlp | operator reflection | reflection operator <sup>(C++26)</sup> |
| - |
| style="border-bottom-style: none; border-top-style: none" | rlpt | sizeof |
| style="border-bottom-style: none; border-top-style: none" | rlp | sizeof | Size-of<ref>The operand of c/core | sizeof cannot be a C-style type cast: the expression c | sizeof (int) * p is unambiguously interpreted as c | (sizeof(int)) * p, but not c | sizeof((int)*p).</ref> |
| - |
| style="border-bottom-style: none; border-top-style: none" | ltt | cpp/keyword/co_await |
| style="border-bottom-style: none; border-top-style: none" | rlp | coroutines | await-expression |
| - |
| style="border-bottom-style: none; border-top-style: none" | rlpt | new&ndash;rlpt | new | new[] |
| style="border-bottom-style: none; border-top-style: none" | rlp | new | Dynamic memory allocation |
| - |
| style="border-top-style: none" | rlpt | delete&ndash;rlpt | delete | delete[] |
| style="border-top-style: none" | rlp | delete | Dynamic memory deallocation |
| - style="border-top: 1px solid #aaa" |
| 4 |
| c | a.*bc | a->*b |
| rlp | operator member access#Built-in pointer-to-member access operators | Pointer-to-member |
| style="vertical-align: top" rowspan="12" | Left-to-right &#8594; |
| - style="border-top: 1px solid #aaa" |
| 5 |
| c | a * bc | a / bc | a % b |
| rlp | operator arithmetic#Multiplicative operators | Multiplication, division, and remainder |
| - style="border-top: 1px solid #aaa" |
| 6 |
| c | a + bc | a - b |
| rlp | operator arithmetic#Additive operators | Addition and subtraction |
| - style="border-top: 1px solid #aaa" |
| 7 |
| c | a << bc | a >> b |
| Bitwise rlp | operator arithmetic#Bitwise shift operators | left shift and right shift |
| - style="border-top: 1px solid #aaa" |
| 8 |
| c | 1=a <=> b |
| [[cpp/language/operator comparison#Three-way comparison | Three-way comparison operator]] <sup>(C++20)</sup> |
| - style="border-top: 1px solid #aaa" |
| 9 |
| c | a < bc | 1=a <= bc | a > bc | 1=a >= b |
| For rlp | operator comparison | relational operators ttb | < and ttb | 1=<= and ttb | 1=> and ttb | 1=>= respectively |
| - style="border-top: 1px solid #aaa" |
| 10 |
| c | 1=a == bc | 1=a != b |
| For rlp | operator comparison | equality operators ttb | 1== and ttb | 1=!= respectively |
| - style="border-top: 1px solid #aaa" |
| 11 |
| c | a & b |
| rlp | operator arithmetic#Bitwise logic operators | Bitwise AND |
| - style="border-top: 1px solid #aaa" |
| 12 |
| c | a ^ b |
| rlp | operator arithmetic#Bitwise logic operators | Bitwise XOR (exclusive or) |
| - style="border-top: 1px solid #aaa" |
| 13 |
| c | a | b |
| rlp | operator arithmetic#Bitwise logic operators | Bitwise OR (inclusive or) |
| - style="border-top: 1px solid #aaa" |
| 14 |
| c | a && b |
| rlp | operator logical | Logical AND |
| - style="border-top: 1px solid #aaa" |
| 15 |
| c | a  b |
| rlp | operator logical | Logical OR |
| - style="border-top: 1px solid #aaa" |
| rowspan=8 | 16 |
| style="border-bottom-style: none" | c | a ? b : c |
| style="border-bottom-style: none" | rlp | operator other#Conditional operator | Ternary conditional<ref>The expression in the middle of the conditional operator (between ttb | ? and ttb | :) is parsed as if parenthesized: its precedence relative to ttb | ?: is ignored.</ref> |
| style="vertical-align: top" rowspan="8" | Right-to-left &#8592; |
| - |
| style="border-bottom-style: none; border-top-style: none" | rlpt | throw |
| style="border-bottom-style: none; border-top-style: none" | rlp | throw | throw operator |
| - |
| style="border-bottom-style: none; border-top-style: none" | ltt | cpp/keyword/co_yield |
| style="border-bottom-style: none; border-top-style: none" | rlp | coroutines | yield-expression |
| - |
| style="border-bottom-style: none; border-top-style: none" | c | 1=a = b |
| style="border-bottom-style: none; border-top-style: none" | rlp | operator assignment#Builtin direct assignment | Direct assignment (provided by default for C++ classes) |
| - |
| style="border-bottom-style: none; border-top-style: none" | c | 1=a += bc | 1=a -= b |
| style="border-bottom-style: none; border-top-style: none" | rlp | operator assignment#Builtin compound assignment | Compound assignment by sum and difference |
| - |
| style="border-bottom-style: none; border-top-style: none" | c | 1=a *= bc | 1=a /= bc | 1=a %= b |
| style="border-bottom-style: none; border-top-style: none" | rlp | operator assignment#Builtin compound assignment | Compound assignment by product, quotient, and remainder |
| - |
| style="border-bottom-style: none; border-top-style: none" | c | 1=a <<= bc | 1=a >>= b |
| style="border-bottom-style: none; border-top-style: none" | rlp | operator assignment#Builtin compound assignment | Compound assignment by bitwise left shift and right shift |
| - |
| style="border-top-style: none" | c | 1=a &= bc | 1=a ^= bc | 1=a |= b |
| style="border-top-style: none" | rlp | operator assignment#Builtin compound assignment | Compound assignment by bitwise AND, XOR, and OR |
| - style="border-top: 1px solid #aaa" |
| 17 |
| c | a, b |
| rlp | operator other#Built-in comma operator | Comma |
| Left-to-right &#8594; |

When parsing an expression, an operator which is listed on some row of the table above with a precedence will be bound tighter (as if by parentheses) to its arguments than any operator that is listed on a row further below it with a lower precedence. For example, the expressions `std::cout << a & b` and  `*p++` are parsed as `(std::cout << a) & b` and `*(p++)`, and not as `std::cout << (a & b)` or `(*p)++`.
Operators that have the same precedence are bound to their arguments in the direction of their associativity. For example, the expression `1=a = b = c` is parsed as `1=a = (b = c)`, and not as `1=(a = b) = c` because of right-to-left associativity of assignment, but `a + b - c` is parsed `(a + b) - c` and not `a + (b - c)` because of left-to-right associativity of addition and subtraction.
Associativity specification is redundant for unary operators and is only shown for completeness: unary prefix operators always associate right-to-left (`delete ++*p` is `delete(++(*p))`) and unary postfix operators always associate left-to-right (`a[1][2]++` is `((a[1])[2])++`). Note that the associativity is meaningful for member access operators, even though they are grouped with unary postfix operators: `a.b++` is parsed `(a.b)++` and not `a.(b++)`.
Operator precedence is unaffected by `operator overloading`. For example, `std::cout << a ? b : c;` parses as `(std::cout << a) ? b : c;` because the precedence of arithmetic left shift is higher than the conditional operator.

## Notes

Precedence and associativity are compile-time concepts and are independent from `order of evaluation`, which is a runtime concept.
The standard itself doesn't specify precedence levels. They are derived from the grammar.
`const_cast`, `static_cast`, `dynamic_cast`, `reinterpret_cast`, `typeid`, `sizeof...`, `noexcept` and `alignof` are not included since they are never ambiguous.
Some of the operators have `alternate spellings` (e.g., `and` for `&&`, `or` for `, `not` for `!`, etc.).
In C, the ternary conditional operator has higher precedence than assignment operators. Therefore, the expression `1=e = a < d ? a++ : a = d`, which is parsed in C++ as `1=e = ((a < d) ? (a++) : (a = d))`, will fail to compile in C due to grammatical or semantic constraints in C. See the corresponding C page for details.

## See also

