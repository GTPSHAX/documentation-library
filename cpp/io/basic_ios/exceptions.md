---
title: std::basic_ios::exceptions
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/exceptions
---


```cpp
dcl|num=1|
std::ios_base::iostate exceptions() const;
dcl|num=2|
void exceptions( std::ios_base::iostate except );
```

Gets and sets the exception mask of the stream. The exception mask determines which error states trigger exceptions of type `failure`.
1. Returns the exception mask.
2. Sets the exception mask to `except`. If the stream has an error state covered by the exception mask when called, an exception is immediately triggered.

## Parameters


### Parameters

- `except` - exception mask

## Return value

1. The current exception mask.
2. (none)

## Notes


## Example


### Example

```cpp
#include <fstream>
#include <iostream>

int main() 
{
    int ivalue;
    try
    {
        std::ifstream in("in.txt");
        in.exceptions(std::ifstream::failbit); // may throw
        in >> ivalue; // may throw
    }
    catch (const std::ios_base::failure& fail)
    {
        // handle exception here
        std::cout << fail.what() << '\n';
    }
}
```


**Output:**
```
basic_ios::clear: iostream error
```

