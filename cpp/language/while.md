---
title: while loop
type: Language
source: https://en.cppreference.com/w/cpp/language/while
---


# tt|while

Conditionally executes a statement repeatedly.

## Syntax


**Syntax:**

- `**`while (`** *condition* **`)`** *statement*`

### Parameters

- `{{spar` - attr|<sup>(C++11)</sup> any number of `attributes`
- `{{spar` - condition|a condition
- `{{spar` - statement|a `statement` (typically a compound statement)

## Explanation

A `while` statement is equivalent to

**Syntax:**

- `sdsc|`
- ``/* label */` **`:`**<br>`
- `**`{`**<br>`
- `:**`if (`** *condition* **`)`**<br>`
- `:**`{`**<br>`
- `::*statement*<br>`
- `::**`goto`** `/* label */` **`;`**<br>`
- `:}<br>`
- `}`
If *condition* is a declaration, the variable it declares is destroyed and created with each iteration of the loop.
If the loop needs to be terminated within *statement*, a ``break` statement` can be used as terminating statement.
If the current iteration needs to be terminated within *statement*, a ``continue` statement` can be used as shortcut.

## Notes

Regardless of whether *statement* is a compound statement, it always introduces a `block scope`. Variables declared in it are only visible in the loop body, in other words,

```cpp
while (--x >= 0)
    int i;
// i goes out of scope
```

is the same as

```cpp
while (--x >= 0)
{
    int i;
} // i goes out of scope
```


## Keywords

`cpp/keyword/while`

## Example


### Example

```cpp
#include <iostream>

int main()
{
    // while loop with a single statement
    int i = 0;
    while (i < 10)
         i++;
    std::cout << i << '\n';

    // while loop with a compound statement
    int j = 2;
    while (j < 9)
    {
        std::cout << j << ' ';
        j += 2;
    }
    std::cout << '\n';

    // while loop with a declaration condition
    char cstr[] = "Hello";
    int k = 0;
    while (char c = cstr[k++])
        std::cout << c;
    std::cout << '\n';
}
```


**Output:**
```
10
2 4 6 8
Hello
```


## See also

