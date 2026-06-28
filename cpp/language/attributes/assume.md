---
title: attribute: assume
type: Language
source: https://en.cppreference.com/w/cpp/language/attributes/assume
---

Specifies that the given expression is assumed to always evaluate to `true` at a given point in order to allow compiler optimizations based on the information given.

## Syntax


**Syntax:**

- `sdsc|`
- `**``[[`assume`(``** *expression* **``)]]``**`

### Parameters

- `{{spar` - expression|any expression (except unparenthesized comma expressions)

## Explanation

`assume` an only be applied to a null statement, as in `assume(x > 0);`. This statement is called an ''assumption''.
*expression* is contextually converted to `bool`, but it is not evaluated (it is still potentially evaluated).
* If the converted *expression* would evaluate to `true` at the point where the assumption appears, the assumption has no effect.
* Otherwise, evaluation of the assumption has runtime-undefined behavior.

## Notes

Since assumptions cause runtime-undefined behavior if they do not hold, they should be used sparingly.
One correct way to use them is to follow assertions with assumptions:
source
|code=
assert(x > 0);     // trigger an assertion when NDEBUG is not defined and x > 0 is false
assume(x > 0); // provide optimization opportunities when NDEBUG is defined

## Example

source
|code=
#include <cmath>
void f(int& x, int y)
{
void g(int);
void h();
assume(x > 0); // Compiler may assume x is positive
g(x / 2); // More efficient code possibly generated
x = 3;
int z = x;
assume((h(), x == z)); // Compiler may assume x would have the same value after
// calling h
// The assumption does not cause a call to h
h();
g(x); // Compiler may replace this with g(3);
h();
g(x); // Compiler may NOT replace this with g(3);
// An assumption applies only at the point where it appears
z = std::abs(y);
assume((g(z), true)); // Compiler may assume g(z) will return
g(z); // Due to above and below assumptions, compiler may replace this with g(10);
assume(y == -10); // Undefined behavior if y != -10 at this point
assume((x - 1) * 3 == 12);
g(x); // Compiler may replace this with g(5);
}

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-2924 | C++23 | violating an assumption would result in undefined behavior | results in runtime-undefined behavior |


## References


## See also


| cpp/utility/dsc unreachable | (see dedicated page) |
| cpp/language/dsc contract_assert | (see dedicated page) |


## External links

