---
title: switch statement
type: Language
source: https://en.cppreference.com/w/cpp/language/switch
---


# tt|switch

Transfers control to one of several statements, depending on the value of a condition.

## Syntax


**Syntax:**

- `sdsc|`
- `*attr* (optional) **`switch`** **`(`** *init-statement* (optional) *condition* **`)`** *statement*`

### Parameters

- `{{spar` - attr|<sup>(C++11)</sup> any number of `attributes`
- `{{spar` - init-statement|<sup>(C++17)</sup> any of the following:
- * an `expression statement` (which may be a null statement `;`)
- * a , typically a declaration of a variable with initializer, but it may declare arbitrarily many variables or `structured binding`s
- rrev|since=c++23|
- * an `alias declaration`
- `{{spar` - condition|a condition
- `{{spar` - statement|a statement (typically a compound statement)

### Type

*condition* can only yield the following types:
* integral types
* enumeration types
* class types
If the yielded value is of a class type, it is contextually implicitly converted to an integral or enumeration type.
If the (possibly converted) type is subject to s , the yielded value is converted to the promoted type.

## Labels

Any statement within the `switch` statement can be labeled with one or more following labels:

**Syntax:**

- `sdsc|num=1|`
- `*attr* (optional) **`case`** *constant-expression* **`:`**`
- `sdsc|num=2|`
- `*attr* (optional) **`default:`**`

### Parameters

- `{{spar` - attr|<sup>(C++11)</sup> any number of `attributes`
- `{{spar` - constant-expression|a  of the adjusted type of the `switch` condition
A `case` or `default` label is associated with the innermost `switch` statement enclosing it.
If any of the following conditions is satisfied, the program is ill-formed:
* A `switch` statement is associated with multiple `case` labels whose constant-expressions have the same value after conversions.
* A `switch` statement is associated with multiple `default` labels.

## Control flow transfer

When the condition of a `switch` statement yields a (possibly converted) value:
* If one of the associated `case` label constants has the same value, control is passed to the statement labeled by the matched `case` label.
* Otherwise, if there is an associated `default` label, control is passed to the statement labeled by the `default` label.
* Otherwise, none of the statements in the `switch` statement will be executed.
`case` and `default` labels in themselves do not alter the flow of control. To exit from a `switch` statement from the middle, see ``break` statements`.
Compilers may issue warnings on fallthrough (reaching the next `case` or `default` label without a `break`)<sup>(since C++17)</sup>  unless the attribute .

```cpp
switch (1)
{
    case 1:
        std::cout << '1'; // prints "1",
    case 2:
        std::cout << '2'; // then prints "2"
}
```


```cpp
switch (1)
{
    case 1:
        std::cout << '1'; // prints "1"
        break;            // and exits the switch
    case 2:
        std::cout << '2';
        break;
}
```

rrev|since=c++17|

## `switch` statements with initializer

If *init-statement* is used, the switch statement is equivalent to

**Syntax:**

- `sdsc|`
- `**`{`**<br>`
- `:*init-statement*<br>`
- `:**`switch`** **`(`** *condition* **`)`** *statement*<br>`
- `}`
Except that names declared by the *init-statement* (if *init-statement* is a declaration) and names declared by *condition* (if *condition* is a declaration) are in the same scope, which is also the scope of *statement*.

## Notes

Because transfer of control is `not permitted to enter the scope` of a variable, if a declaration statement is encountered inside the *statement*, it has to be scoped in its own compound statement:

```cpp
switch (1)
{
    case 1:
        int x = 0; // initialization
        std::cout << x << '\n';
        break;
    default:
        // compilation error: jump to default:
        // would enter the scope of 'x' without initializing it
        std::cout << "default\n";
        break;
}
```


```cpp
switch (1)
{
    case 1:
        {
            int x = 0;
            std::cout << x << '\n';
            break;
        } // scope of 'x' ends here
    default:
        std::cout << "default\n"; // no error
        break;
}
```


## Keywords

`cpp/keyword/switch`,
`cpp/keyword/case`,
`cpp/keyword/default`

## Example


### Example

```cpp
#include <iostream>

int main()
{
    const int i = 2;
    switch (i)
    {
        case 1:
            std::cout << '1';
        case 2:              // execution starts at this case label
            std::cout << '2';
        case 3:
            std::cout << '3';
            [[fallthrough]]; // C++17 attribute to silent the warning on fallthrough
        case 5:
            std::cout << "45";
            break;           // execution of subsequent statements is terminated
        case 6:
            std::cout << '6';
    }

    std::cout << '\n';

    switch (i)
    {
        case 4:
            std::cout << 'a';
        default:
            std::cout << 'd'; // there are no applicable constant expressions 
                              // therefore default is executed
    }

    std::cout << '\n';

    switch (i)
    {
        case 4:
            std::cout << 'a'; // nothing is executed
    }

    // when enumerations are used in a switch statement, many compilers
    // issue warnings if one of the enumerators is not handled
    enum color { RED, GREEN, BLUE };
    switch (RED)
    {
        case RED:
            std::cout << "red\n";
            break;
        case GREEN:
            std::cout << "green\n";
            break;
        case BLUE:
            std::cout << "blue\n";
            break;
    }

    // the C++17 init-statement syntax can be helpful when there is
    // no implicit conversion to integral or enumeration type
    struct Device
    {
        enum State { SLEEP, READY, BAD };
        auto state() const { return m_state; }

        /* ... */

    private:
        State m_state{};
    };

    switch (auto dev = Device{}; dev.state())
    {
        case Device::SLEEP:
            /* ... */
            break;
        case Device::READY:
            /* ... */
            break;
        case Device::BAD:
            /* ... */
            break;
    }

    // pathological examples

    // the statement does not have to be a compound statement
    switch (0)
        std::cout << "this does nothing\n";

    // labels do not require a compound statement either
    switch (int n = 1)
        case 0:
        case 1:
            std::cout << n << '\n';
}
```


**Output:**
```
2345
d
red
1
```


## Defect reports


## See also


## External links

