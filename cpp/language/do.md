---
title: do-while loop
type: Language
source: https://en.cppreference.com/w/cpp/language/do
---


# tt|do

Conditionally executes a statement repeatedly (at least once).

## Syntax


**Syntax:**

- `**`do`** *statement* **`while (`** *expression* **`);`**`

### Parameters

- `{{spar` - attr|<sup>(C++11)</sup> any number of `attributes`
- `{{spar` - expression|an `expression`
- `{{spar` - statement|a `statement` (typically a compound statement)

## Explanation

When control reaches a `do` statement, its *statement* will be executed unconditionally.
Every time *statement* finishes its execution, *expression* will be evaluated and contextually converted to `bool`. If the result is `true`, *statement* will be executed again.
If the loop needs to be terminated within *statement*, a ``break` statement` can be used as terminating statement.
If the current iteration needs to be terminated within *statement*, a ``continue` statement` can be used as shortcut.

## Notes


## Keywords

`cpp/keyword/do`,
`cpp/keyword/while`

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <string>

int main()
{
    int j = 2;
    do // compound statement is the loop body
    {
        j += 2;
        std::cout << j << ' ';
    }
    while (j < 9);
    std::cout << '\n';

    // common situation where do-while loop is used
    std::string s = "aba";
    std::sort(s.begin(), s.end());

    do std::cout << s << '\n'; // expression statement is the loop body
    while (std::next_permutation(s.begin(), s.end()));
}
```


**Output:**
```
4 6 8 10
aab
aba
baa
```


## See also

