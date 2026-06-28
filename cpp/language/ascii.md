---
title: ASCII Chart
type: Language
source: https://en.cppreference.com/w/cpp/language/ascii
---


# ASCII Chart

The following chart contains all 128 ASCII decimal '''(dec)''', octal '''(oct)''', hexadecimal '''(hex)''' and character '''(ch)''' codes.

## Example


### Example

```cpp
#include <iostream>

int main()
{
    std::cout << "Printable ASCII [32..126]:\n";
    for (char c{' '}; c <= '~'; ++c)
        std::cout << c << ((c + 1) % 32 ? ' ' : '\n');
    std::cout << '\n';
}
```


**Output:**
```
Printable ASCII [32..126]:
  ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ?
@ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _
` a b c d e f g h i j k l m n o p q r s t u v w x y z { {{!
```


## See also

