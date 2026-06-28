---
title: keyword: and
type: Keywords
source: https://en.cppreference.com/w/cpp/keyword/and
---


## Usage

* alternative operators: as an alternative for `&&`

## Example


### Example

```cpp
int main()
{
    static_assert((false and false) == false);
    static_assert((false and true)  == false);
    static_assert((true  and false) == false);
    static_assert((true  and true)  == true);
}
```


## See also

