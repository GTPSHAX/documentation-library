---
title: std::is_execution_policy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/is_execution_policy
---

ddcl|header = execution|since=c++17|1=
template< class T >
struct is_execution_policy;
Checks whether `T` is a standard or implementation-defined execution policy type.
Provides the member constant `value` which is equal to `true`, if `T` is a standard execution policy type, or an implementation-defined execution policy type. Otherwise, `value` is equal to `false`.

## Template parameters


### Parameters

- `T` - a type to check

## Helper template

ddcl|header = execution|since=c++17|1=
template< class T >
constexpr bool is_execution_policy_v = std::is_execution_policy<T>::value;

### Example

```cpp
#include <execution>

static_assert(std::is_execution_policy_v<std::execution::unsequenced_policy>);
static_assert(!std::is_execution_policy_v<int>);

int main() {}
```


## See also


| cpp/algorithm/dsc execution_policy_tag_t | (see dedicated page) |
| cpp/algorithm/dsc execution_policy_tag | (see dedicated page) |

