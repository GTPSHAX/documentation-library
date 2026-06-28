---
title: std::seed_seq::param
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/seed_seq/param
---


```cpp
dcl|since=c++11|1=
template< class OutputIt >
void param( OutputIt dest ) const;
```

Copies the stored seeds to the range beginning with `dest`. Equivalent to .
If values of type `result_type` are not writable to `dest`, the program is ill-formed.
If `OutputIt` does not satisfy the requirements of *OutputIterator*, the behavior is undefined.

## Parameters


### Parameters

- `dest` - the beginning iterator of the output range

## Exceptions

Only throws the exceptions thrown by the operations on `dest`.

## Example


### Example

```cpp
#include <iostream>
#include <iterator>
#include <random>

int main()
{
    std::seed_seq s1 = {-1, 0, 1};
    s1.param(std::ostream_iterator<int>(std::cout, " "));
}
```


**Output:**
```
-1 0 1
```


## Defect reports

