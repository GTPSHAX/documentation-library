---
title: std::generator::~generator
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/generator/~generator
---

ddcl|since=c++23|1=
~generator();
Destructs the generator object.
Given `''coroutine_''` as the underlying coroutine object, equivalent to:

```cpp
if (coroutine_)
    coroutine_.destroy();
```

Note, that destroying the root generator effectively destroys the entire stack of yielded generators, because the ownership of recursively yielded generators is held in awaitable objects in the coroutine frame of the yielding generator.

## Complexity


## Example

