---
title: Logical operators
type: Language
source: https://en.cppreference.com/w/cpp/language/operator_logical
---


# Logical operators

Returns the result of a boolean operation.


| - |
| rowspan="2" | Operator name |
| rowspan="2" | Syntax |
| rowspan="2" | rlp | operators | Over&#8203;load&#8203;able |
| colspan="2" | Prototype examples (for c | class T) |
| - |
| Inside class definition |
| Outside class definition |
| - |
| negation |
| c | not a |
|  |
| c | bool T::operator!() const; |
| c | bool operator!(const T &a); |
| - |
| AND |
| c | a and b |
|  |
| c | bool T::operator&&(const T2 &b) const; |
| c | bool operator&&(const T &a, const T2 &b); |
| - |
| inclusive OR |
| c | a or b |
|  |
| c | bool T::operator(const T2 &b) const; |
| c | bool operator(const T &a, const T2 &b); |
| - |
| colspan="5" |  |


## Explanation

The logic operator expressions have the form

**Syntax:**

- `*rhs*`
- `**`&&`** *rhs*`
- `**`<nowiki>||</nowiki>`** *rhs*`
1. Logical NOT
2. Logical AND
3. Logical inclusive OR
If the operand is not `bool`, it is converted to `bool` using `contextual conversion to bool`: it is only well-formed if the declaration `bool t(arg)` is well-formed, for some invented temporary `t`.
The result is a `bool` prvalue.
For the built-in logical NOT operator, the result is `true` if the operand is `false`. Otherwise, the result is `false`.
For the built-in logical AND operator, the result is `true` if both operands are `true`. Otherwise, the result is `false`. This operator is [Short-circuit_evaluation|short-circuiting](https://en.wikipedia.org/wiki/Short-circuit_evaluation|short-circuiting): if the first operand is `false`, the second operand is not evaluated.
For the built-in logical OR operator, the result is `true` if either the first or the second operand (or both) is `true`. This operator is short-circuiting: if the first operand is `true`, the second operand is not evaluated.
Note that `bitwise logic operators` do not perform short-circuiting.

## Results


| c | a |
| c | true |
| c | false |
| - |
| c | !a |
| c | false |
| c | true |


| colspan=2 rowspan=2 | c | and |
| colspan=2 | c | a |
| - |
| c | true |
| c | false |
| - |
| rowspan=2 | c | b |
| c | true |
| c | true |
| c | false |
| - |
| c | false |
| c | false |
| c | false |


| colspan=2 rowspan=2 | c | or |
| colspan=2 | c | a |
| - |
| c | true |
| c | false |
| - |
| rowspan=2 | c | b |
| c | true |
| c | true<!--true | true--> |
| c | true<!--true | false--> |
| - |
| c | false |
| c | true<!--false | true--> |
| c | false<!--false | false--> |

In `overload resolution against user-defined operators`, the following built-in function signatures participate in overload resolution:

```cpp
(bool, bool)
```


## Example


### Example

```cpp
#include <iostream>
#include <sstream>
#include <string>

int main()
{
    int n = 2;
    int* p = &n;
    // pointers are convertible to bool
    if (    p && *p == 2  // "*p" is safe to use after "p &&"
        {{!!
```

std::cout << "true\n";
// streams are also convertible to bool
std::stringstream cin;
cin << "3...\n" << "2...\n" << "1...\n" << "quit";
std::cout << "Enter 'quit' to quit.\n";
for (std::string line;    std::cout << "> "
&& std::getline(cin, line)
&& line != "quit";)
std::cout << line << '\n';
}
|output=
true
Enter 'quit' to quit.
> 3...
> 2...
> 1...
>

## Standard library

Because the short-circuiting properties of `operator&&` and `operator do not apply to overloads, and because types with boolean semantics are uncommon, only two standard library classes overload these operators:


| cpp/numeric/valarray/operator_arith3|title=operator&&<br>operator<nowiki>||</nowiki>|applies binary operators to each element of two valarrays, or a valarray and a value | |
| cpp/io/basic_ios/dsc operator! | (see dedicated page) |


## See also

`Operator precedence`
`Operator overloading`
