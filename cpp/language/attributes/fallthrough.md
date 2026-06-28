---
title: attribute: fallthrough
type: Language
source: https://en.cppreference.com/w/cpp/language/attributes/fallthrough
---

Indicates that the fall through from the previous case label is intentional and should not be diagnosed by a compiler that warns on fallthrough.

## Syntax


**Syntax:**

- `sdsc|1=`
- `**``fallthrough``**`

## Explanation

May only be applied to a null statement to create a ''fallthrough statement'' (`fallthrough;`).
A fallthrough statement may only be used in a switch statement, where the next statement to be executed is a statement with a case or default label for that switch statement. If the fallthrough statement is inside a loop, the next (labeled) statement must be part of the same iteration of that loop.

## Example


### Example

```cpp
void f(int n)
{
    void g(), h(), i();

    switch (n)
    {
        case 1:
        case 2:
            g();
            [[fallthrough]];
        case 3: // no warning on fallthrough
            h();
        case 4: // compiler may warn on fallthrough
            if (n < 3)
            {
                i();
                [[fallthrough]]; // OK
            }
            else
            {
                return;
            }
        case 5:
            while (false)
            {
                [[fallthrough]]; // ill-formed: next statement is not
                                 //             part of the same iteration
            }
        case 6:
            [[fallthrough]]; // ill-formed, no subsequent case or default label
    }
}
```


## Defect reports


## References


## See also

