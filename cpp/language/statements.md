---
title: Statements
type: Language
source: https://en.cppreference.com/w/cpp/language/statements
---


# Statements

''Statements'' are fragments of the C++ program that are executed in sequence. The body of any function is a sequence of statements. For example:

```cpp
int main()
{
    int n = 1;                        // declaration statement
    n = n + 1;                        // expression statement
    std::cout << "n = " << n << '\n'; // expression statement
    return 0;                         // return statement
}
```

C++ includes the following types of statements:
*
*
*
*
*
rrev|since=c++26|
*
*
rrev|since=c++26|
*
*
* `try` blocks
rrev|since=tm_ts|
*

## Labeled statements

A labeled statement labels a statement for control flow purposes.

**Syntax:**

- `sdsc|`
- `*label statement*`

### Parameters

- `{{spar` - label|the label applied to the statement (defined below)
- `{{spar` - statement|the statement which the label applies to, it can be a labeled statement itself, allowing multiple labels

### Labels

*label* is defined as

**Syntax:**

- `sdsc|num=1|`
- `*attr* (optional) *identifier* **`:`**`
- `sdsc|num=2|`
- `*attr* (optional) **`case`** *constexpr* **`:`**`
- `sdsc|num=3|`
- `*attr* (optional) **`default:`**`
1. target for `goto` (identifier label);
2. `case` label in a `switch` statement;
3. `default` label in a `switch` statement.
Two identifier labels in a function must not have the same identifier. identifiers in labels are not found by `unqualified lookup`: a label can have the same name as any other entity in the program.
`case` labels and `default` labels must be enclosed by `switch` statements.
rev|since=c++11|
An `attribute` sequence *attr* may appear just at the beginning of the label (in which case it applies to the label), or just before any statement itself, in which case it applies to the entire statement.
rev|since=c++23|
Besides being added to a statement, labels can also be used anywhere in .
rev|since=c++26|
Identifier labels must not be enclosed by .

```cpp
void f()
{
    label1: 1 + 1; // a labeled statement
    label1: 1 - 1; // Error: cannot repeat label identifiers in the same function
    label2:        // label can appear at the end of a block standalone since C++23
}
```


### Control-flow-limited statements

The following statements are ''control-flow-limited statements'':
* The *compound-statement* of a ``try` block`.
* The *compound-statement* of a `handler`.
rev|since=c++17|
* All substatements of a `constexpr `if` statement`.
rev|since=c++23|
* All substatements of a `consteval `if` statement`.
For each control-flow-limited statement `S`:
* All `goto` target labels delcared in `S` can only be referred to by statements in `S`.
* Each `case` or `default` label appearing within `S` can only be associated with a ``switch` statement` within `S`.

## Expression statements

An expression statement is an expression followed by a semicolon.

**Syntax:**

- `sdsc|`
- `*attr* (optional) *expression* (optional) **`;`**`

### Parameters

- `{{spar` - attr|<sup>(C++11)</sup> optional sequence of any number of `attributes`
- `{{spar` - expression|an `expression`
Most statements in a typical C++ program are expression statements, such as assignments or function calls.
An expression statement without an expression is called a ''null statement''. It is often used to provide an empty body to a `for` or `while` loop. <sup>(until C++23)</sup> It can also be used to carry a label in the end of a compound statement.

## Compound statements

A compound statement or ''block'' groups a sequence of statements into a single statement.

**Syntax:**

- `sdsc|`
- `*attr* (optional) **`{`** *statement...* (optional) *label...* (optional)<sup>(C++23)</sup> }`
When one statement is expected, but multiple statements need to be executed in sequence (for example, in an `if` statement or a loop), a compound statement may be used:

```cpp
if (x > 5)          // start of if statement
{                   // start of block
    int n = 1;      // declaration statement
    std::cout << n; // expression statement
}                   // end of block, end of if statement
```

Each compound statement introduces its own block `scope`; variables declared inside a block are destroyed at the closing brace in reverse order:

```cpp
int main()
{ // start of outer block
    {                                // start of inner block
        std::ofstream f("test.txt"); // declaration statement
        f << "abc\n";                // expression statement
    }                                // end of inner block, f is flushed and closed
    std::ifstream f("test.txt"); // declaration statement
    std::string str;             // declaration statement
    f >> str;                    // expression statement
} // end of outer block, str is destroyed, f is closed
```

rrev|since=c++23|
A label at the end of a compound statement is treated as if it were followed by a null statement.

## Selection statements

A selection statement chooses between one of several control flows.

**Syntax:**

- `sdsc|num=1|`
- `*attr* (optional) **`if constexpr`** **`(`** *init-statement* (optional) *condition* **`)`** *statement*`
- `sdsc|num=2|`
- `*attr* (optional) **`if constexpr`** **`(`** *init-statement* (optional) *condition* **`)`** *statement*<br>**`else`** *statement*`
- `sdsc|num=3|`
- `*attr* (optional) **`switch (`** *init-statement* (optional) *condition* **`)`** *statement*`
- `|`
- `*attr* (optional) **`if !`** **`consteval`** *compound-statement*`
- `|`
- `*attr* (optional) **`if !`** **`consteval`** *compound-statement* **`else`** *statement*`
1. `if` statement;
2. `if` statement with an else clause;
3. `switch` statement;
4. `consteval if` statement;
5. `consteval if` statement with an else clause.

## Iteration statements

An iteration statement repeatedly executes some code.

**Syntax:**

- `sdsc|num=1|`
- `*attr* (optional) **`while (`** *condition* **`)`** *statement*`
- `sdsc|num=2|`
- `*attr* (optional) **`do`** *statement* **`while (`** *expression* **`)`** **`;`**`
- `sdsc|num=3|`
- `*attr* (optional) **`for (`** *init-statement condition* (optional) **`;`** *expression* (optional) **`)`** *statement*`
- `|`
- `*attr* (optional) **`for`**<br>**`(`** *init-statement* (optional)<sup>(C++20)</sup> *range-decl* **`:`** *range-init* **`)`** *statement*`
1. `while` loop;
2. `do-while` loop;
3. `for` loop;
4. `range for` loop.
rrev|since=c++26|

## Expansion statements

An expansion statement replaces some code with multiple copies.

**Syntax:**

- `sdsc|`
- `*attr* (optional) **`template for`**<br>**`(`** *init-statement* (optional) *expand-decl* **`:`** *expand-init* **`)`** *compound-statement*`
1. `template for` expansion.

## Jump statements

A jump statement unconditionally transfers control flow.

**Syntax:**

- `sdsc|num=1|`
- `*attr* (optional) **`break;`**`
- `sdsc|num=2|`
- `*attr* (optional) **`continue;`**`
- `sdsc|num=3|`
- `*attr* (optional) **`return`** *expression* (optional) **`;`**`
- `|`
- `*attr* (optional) **`return`** *braced-init-list* **`;`**`
- `sdsc|num=5|`
- `*attr* (optional) **`goto`** *identifier* **`;`**`
1. `break` statement;
2. `continue` statement;
3. `return` statement with an optional expression;
4. `return` statement using `list initialization`;
5. `goto` statement.
Note: for all jump statements, transfer out of a loop, out of a block, or back past an initialized variable with automatic storage duration involves the destruction of objects with automatic storage duration that are in scope at the point transferred from but not at the point transferred to. If multiple objects were initialized, the order of destruction is the opposite of the order of initialization.
rrev|since=c++26|

## Assertion statements

A `contract` assertion.

**Syntax:**

- `*attr* (optional) **`(`** *predicate* **`)`** **`;`**`
1. `contract_assert` statement.

## Declaration statements

A declaration statement introduces one or more identifiers into a block.

**Syntax:**

- `sdsc|num=1|`
- `*block-declaration*`
1. See `Declarations` and `Initialization` for details.

## `try` blocks

A `try` block catches exceptions thrown when executing other statements.

**Syntax:**

- `sdsc|num=1|`
- `*attr* (optional) **`try`** *compound-statement handler-sequence*`
1. See ``try` block` for details.
rrev|since=tm_ts|

## Atomic and synchronized blocks

An atomic and synchronized block provides `transactional memory`.

**Syntax:**

- `|`
- `**`synchronized`** *compound-statement*`
- `|`
- `**`atomic_noexcept`** *compound-statement*`
- `|`
- `**`atomic_cancel`** *compound-statement*`
- `|`
- `**`atomic_commit`** *compound-statement*`
1. `synchronized block`, executed in single total order with all synchronized blocks;
2. `atomic block` that aborts on exceptions;
3. `atomic block` that rolls back on exceptions;
4. `atomic block` that commits on exceptions.
===Substatements===
A ''substatement'' of a statement is one of the following:
* For a labeled statement, its statement.
* For a compound statement, any statement of its statement....
* For a selection statement, any of its statement<sup>(since C++23)</sup>  or compound-statement.
* For an iteration statement, its statement.
rrev|since=c++26|
* For an expansion statement, its compound-statement.
A statement `S1` ''encloses'' a statement `S2` if any of the following conditions is satisfied:
* `S2` is a substatement of `S1`
* `S1` is a selection statement<sup>(since C++26)</sup> , expansion statement or iteration statement, and `S2` is the *init-statement* of `S1`.
* `S1` is a ``try` block`, and `S2` is either its *compound-statement* or the *compound-statement* of any `handler` in its handler-seq.
* `S1` encloses a statement `S3` and `S3` encloses `S2`.
A statement `S1` is ''enclosed by'' a statement `S2` if `S2` encloses `S1`.

## See also

