---
title: Low level memory management
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/new
---


# Low level memory management

The new-expression is the only way to create an object or an array of objects with dynamic storage duration, that is, with lifetime not restricted to the scope in which it is created. A new-expression obtains storage by calling an allocation function. A delete-expression destroys a most derived object or an array created by a new-expression and calls the deallocation function. The default allocation and deallocation functions, along with related functions, types, and objects, are declared in the header .


| new | |

#### Functions

| cpp/memory/new/dsc operator_new | (see dedicated page) |
| cpp/memory/new/dsc operator_delete | (see dedicated page) |
| cpp/memory/new/dsc get_new_handler | (see dedicated page) |
| cpp/memory/new/dsc set_new_handler | (see dedicated page) |

#### Classes

| cpp/memory/new/dsc bad_alloc | (see dedicated page) |
| cpp/memory/new/dsc bad_array_new_length | (see dedicated page) |
| cpp/memory/new/dsc align_val_t | (see dedicated page) |

#### Types

| cpp/memory/new/dsc new_handler | (see dedicated page) |

#### Objects

| cpp/memory/new/dsc nothrow | (see dedicated page) |
| cpp/memory/new/dsc destroying_delete | (see dedicated page) |

#### Object access

| cpp/utility/dsc launder | (see dedicated page) |

