---
title: std::rand
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/rand
---

ddcl|header=cstdlib|
int rand();
Returns a pseudo-random integral value from the range .
`std::srand()` seeds the pseudo-random number generator used by `rand()`.
If `rand()` is used before any calls to `std::srand()`, `rand()` behaves as if it was seeded with `std::srand(1)`.
Each time `rand()` is seeded with `std::srand()`, it must produce the same sequence of values on successive calls.
Other functions in the standard library may call `rand`. It is implementation-defined which functions do so.
It is implementation-defined whether `rand()` is thread-safe.

## Return value

Pseudo-random integral value between `0` and `RAND_MAX`.

## Notes

There are no guarantees as to the quality of the random sequence produced.
In the past, some implementations of `rand()` have had serious shortcomings in the randomness, distribution and period of the sequence produced (in one well-known example, the low-order bit simply alternated between `1` and `0` between calls).
`rand()` is not recommended for serious random-number generation needs. <sup>(since C++11)</sup> It is recommended to use C++11's random number generation facilities to replace `rand()`.

## Example


### Example

```cpp
#include <cstdlib>
#include <ctime>
#include <initializer_list>
#include <iostream>

unsigned bounded_rand(unsigned range)
{
    for (unsigned x, r;;)
        if (x = rand(), r = x % range, x - r <= -range)
            return r;
}

int main() 
{
    std::srand(std::time({})); // use current time as seed for random generator
    const int random_value = std::rand();
    std::cout << "Random value on [0, " << RAND_MAX << "]: " << random_value << '\n';

    for (const unsigned sides : {2, 4, 6, 8})
    {
        std::cout << "Roll " << sides << "-sided die 8 times: ";
        for (int n = 8; n; --n)
            std::cout << 1 + bounded_rand(sides) << ' ';

        std::cout << '\n';
    }
}
```


**Output:**
```
Random value on [0, 2147483647]: 948298199
Roll 2-sided die 8 times: 2 2 1 2 1 1 2 2 
Roll 4-sided die 8 times: 1 3 4 2 1 3 3 1 
Roll 6-sided die 8 times: 3 2 1 6 6 4 4 2 
Roll 8-sided die 8 times: 4 5 6 6 3 6 1 2
```


## See also


| cpp/numeric/random/dsc uniform_int_distribution | (see dedicated page) |
| cpp/numeric/random/dsc srand | (see dedicated page) |
| cpp/numeric/random/dsc RAND_MAX | (see dedicated page) |
| cpp/experimental/dsc randint | (see dedicated page) |

