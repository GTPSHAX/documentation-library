---
title: for loop
type: Language
source: https://en.cppreference.com/w/cpp/language/for
---


# tt|for

Conditionally executes a statement repeatedly, where the statement does not need to manage the loop condition.

## Syntax


**Syntax:**

- `**`for (`** *init-statement* *condition* (optional) **`;`** *expression* (optional) **`)`** *statement*`

### Parameters

- `{{spar` - attr|<sup>(C++11)</sup> any number of `attributes`
- `{{spar` - init-statement|one of
- * an `expression statement` (which may be a null statement `;`)
- * a   (typically a declaration of a loop counter variable with initializer), it may declare arbitrary many variables<sup>(since C++17)</sup>  or `structured bindings`
- rrev|since=c++23|
- * an `alias declaration`
- `{{spar` - condition|a condition
- `{{spar` - expression|an `expression` (typically an expression that increments the loop counter)
- `{{spar` - statement|a `statement` (typically a compound statement)

## Explanation

A `for` statement equivalent to:

**Syntax:**

- `sdsc|`
- `**`{`**<br>`
- `:*init-statement*<br>`
- `:**`while (`** *condition* **`)`**<br>`
- `:**`{`**<br>`
- `::*statement*<br>`
- `::*expression* **`;`**<br>`
- `:}`
- `}`
Except that
* The scope of *init-statement* and the scope of *condition* are the same.
* The scope of *statement* and the scope of *expression* are disjoint and nested within the scope of *init-statement* and *condition*.
* Executing a ``continue` statement` in *statement* will evaluate *expression*.
* Empty *condition* is equivalent to `true`.
If the loop needs to be terminated within *statement*, a ``break` statement` can be used as terminating statement.
If the current iteration needs to be terminated within *statement*, a ``continue` statement` can be used as shortcut.

## Notes

As is the case with `while` loop, if *statement* is not a compound statement, the scope of variables declared in it is limited to the loop body as if it was a compound statement.

```cpp
for (;;)
    int n;
// n goes out of scope
```

While in C names declared in the scope of *init-statement* and *condition* can be shadowed in the scope of *statement*, it is forbidden in C++:

```cpp
for (int i = 0;;)
{
    long i = 1;   // valid C, invalid C++
    // ...
}
```


## Keywords

`cpp/keyword/for`

## Example


### Example

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::cout << "1) typical loop with a single statement as the body:\n";
    for (int i = 0; i < 10; ++i)
        std::cout << i << ' ';

    std::cout << "\n\n" "2) init-statement can declare multiple names, as\n"
                 "long as they can use the same decl-specifier-seq:\n";
    for (int i = 0, *p = &i; i < 9; i += 2)
        std::cout << i << ':' << *p << ' ';

    std::cout << "\n\n" "3) condition may be a declaration:\n";
    char cstr[] = "Hello";
    for (int n = 0; char c = cstr[n]; ++n)
        std::cout << c;

    std::cout << "\n\n" "4) init-statement can use the auto type specifier:\n";
    std::vector<int> v = {3, 1, 4, 1, 5, 9};
    for (auto iter = v.begin(); iter != v.end(); ++iter)
        std::cout << *iter << ' ';

    std::cout << "\n\n" "5) init-statement can be an expression:\n";
    int n = 0;
    for (std::cout << "Loop start\n";
         std::cout << "Loop test\n";
         std::cout << "Iteration " << ++n << '\n')
    {
        if (n > 1)
            break;
    }

    std::cout << "\n" "6) constructors and destructors of objects created\n"
                 "in the loop's body are called per each iteration:\n";
    struct S
    {
        S(int x, int y) { std::cout << "S::S(" << x << ", " << y << "); "; }
        ~S() { std::cout << "S::~S()\n"; }
    };
    for (int i{0}, j{5}; i < j; ++i, --j)
        S s{i, j};

    std::cout << "\n" "7) init-statement can use structured bindings:\n";
    long arr[]{1, 3, 7};
    for (auto [i, j, k] = arr; i + j < k; ++i)
        std::cout << i + j << ' ';
    std::cout << '\n';
}
```


**Output:**
```
1) typical loop with a single statement as the body:
0 1 2 3 4 5 6 7 8 9

2) init-statement can declare multiple names, as
long as they can use the same decl-specifier-seq:
0:0 2:2 4:4 6:6 8:8

3) condition may be a declaration:
Hello

4) init-statement can use the auto type specifier:
3 1 4 1 5 9

5) init-statement can be an expression:
Loop start
Loop test
Iteration 1
Loop test
Iteration 2
Loop test

6) constructors and destructors of objects created
in the loop's body are called per each iteration:
S::S(0, 5); S::~S()
S::S(1, 4); S::~S()
S::S(2, 3); S::~S()

7) init-statement can use structured bindings:
4 5 6
```


## See also


| cpp/language/dsc range-for | (see dedicated page) |

