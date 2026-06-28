---
title: Increment/decrement operators
type: Language
source: https://en.cppreference.com/w/cpp/language/operator_incdec
---


# Increment/decrement operators

Increment/decrement operators increment or decrement the value of the object.


| - |
| rowspan="2" | Operator name |
| rowspan="2" | Syntax |
| rowspan="2" | rlp | operators | Over&#8203;load&#8203;able |
| colspan="2" | Prototype examples (for c/core | class T) |
| - |
| Inside class definition |
| Outside class definition |
| - |
| pre-increment |
| tt | ++a |
|  |
| c | T& T::operator++(); |
| c | T& operator++(T& a); |
| - |
| pre-decrement |
| tt | --a |
|  |
| c | T& T::operator--(); |
| c | T& operator--(T& a); |
| - |
| post-increment |
| tt | a++ |
|  |
| c | T T::operator++(int); |
| c | T operator++(T& a, int); |
| - |
| post-decrement |
| tt | a-- |
|  |
| c | T T::operator--(int); |
| c | T operator--(T& a, int); |
| - |
| colspan="5" |  |


## Prefix operators

The prefix increment and decrement expressions have the form

**Syntax:**

- `*expression*`
- `*expression*`
- `@1@ prefix increment (pre-increment)`
- `@2@ prefix decrement (pre-decrement)`
- `====Built-in prefix operators====`
- `@1@ The expression `++x` is equivalent to `1=x += 1`, with the following exceptions:`
- `rev|until=c++17|`
- `* If the type of *expression* is (possibly volatile-qualified) `bool`, *expression* is set to `true`. Such a increment is deprecated.`
- `rev|since=c++17|`
- `* If the type of *expression* is (possibly cv-qualified) `bool`, the program is ill-formed.`
- `rev|since=c++20|`
- `* If the type of *expression* is volatile-qualified, the increment is deprecated.`
- `@2@ The expression `--x` is equivalent to `1=x -= 1`, with the following exceptions:`
- `* If the type of *expression* is (possibly cv-qualified) `bool`, the program is ill-formed.`
- `rrev|since=c++20|`
- `* If the type of *expression* is volatile-qualified, the decrement is deprecated.`
- `====Overloads====`
- `In `overload resolution against user-defined operators`, for every optionally volatile-qualified arithmetic type `A` other than `bool`, and for every optionally volatile-qualified pointer `P` to optionally cv-qualified object type, the following function signatures participate in overload resolution:`

```cpp
<sup>(until C++17)</sup>
```

- `===Postfix operators===`
- `The postfix increment and decrement expressions have the form`

**Syntax:**

- `**`++`**`
- `**`--`**`
1. postfix increment (post-increment)
2. postfix decrement (post-decrement)

### Built-in postfix operators

The result of postfix increment or decrement is the value obtained by applying the  to *expression* (before modification). The type of the result is the cv-unqualified version of the type of *expression*.
If *expression* is not a modifiable lvalue of an arithmetic type<sup>(since C++17)</sup>  other than (possibly cv-qualified) `bool`, or a pointer to a complete object type, the program is ill-formed.
rrev|since=c++20|
If the type of *expression* is volatile-qualified, the increment or decrement is deprecated.
1. The value of *expression* is modified as if it were the operand of the prefix `++` operator.
2. The value of *expression* is modified as if it were the operand of the prefix `--` operator.
The value computation of a postfix increment or decrement is `sequenced before` the modification of *expression*. With respect to an indeterminately-sequenced function call, the operation of a postfix increment or decrement is a single evaluation.

### Overloads

In `overload resolution against user-defined operators`, for every optionally volatile-qualified arithmetic type `A` other than `bool`, and for every optionally volatile-qualified pointer `P` to optionally cv-qualified object type, the following function signatures participate in overload resolution:

```cpp
<sup>(until C++17)</sup>
```


### Example


### Example

```cpp
#include <iostream>

int main()
{
    int n1 = 1;
    int n2 = ++n1;
    int n3 = ++ ++n1;
    int n4 = n1++;
//  int n5 = n1++ ++;   // error
//  int n6 = n1 + ++n1; // undefined behavior
    std::cout << "n1 = " << n1 << '\n'
              << "n2 = " << n2 << '\n'
              << "n3 = " << n3 << '\n'
              << "n4 = " << n4 << '\n';
}
```


**Output:**
```
n1 = 5
n2 = 2
n3 = 4
n4 = 4
```


## Notes

Because of the side-effects involved, built-in increment and decrement operators must be used with care to avoid undefined behavior due to violations of `sequencing rules`.
Because a temporary copy of the object is constructed during post-increment and post-decrement, pre-increment or pre-decrement operators are usually more efficient in contexts where the returned value is not used.

## Standard library

Increment and decrement operators are overloaded for many standard library types. In particular, every *Iterator* overloads `operator++` and every *BidirectionalIterator* overloads `operator--`, even if those operators are no-ops for the particular iterator.


#### overloads for arithmetic types

| cpp/atomic/atomic/dsc operator arith | (see dedicated page) |
| cpp/chrono/duration/dsc operator arith2 | (see dedicated page) |

#### overloads for iterator types

| cpp/memory/raw_storage_iterator/dsc operator arith | (see dedicated page) |
| cpp/iterator/adaptor/dsc operator arith|reverse_iterator | (see dedicated page) |
| cpp/iterator/adaptor/dsc operator arith|move_iterator | (see dedicated page) |
| cpp/iterator/inserter/dsc operator arith|front_insert_iterator | (see dedicated page) |
| cpp/iterator/inserter/dsc operator arith|back_insert_iterator | (see dedicated page) |
| cpp/iterator/inserter/dsc operator arith|insert_iterator | (see dedicated page) |
| cpp/iterator/istream_iterator/dsc operator arith | (see dedicated page) |
| cpp/iterator/ostream_iterator/dsc operator arith | (see dedicated page) |
| cpp/iterator/istreambuf_iterator/dsc operator arith | (see dedicated page) |
| cpp/iterator/ostreambuf_iterator/dsc operator arith | (see dedicated page) |
| cpp/regex/regex_iterator/dsc operator arith | (see dedicated page) |
| cpp/regex/regex_token_iterator/dsc operator arith | (see dedicated page) |


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-2901 | C++98 | lvalue-to-rvalue conversions were not applied<br>for built-in post-increment and post-decrement | applied |


## See also

`Operator precedence`
`Operator overloading`
