---
title: std::float_round_style
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/float_round_style
---

ddcl|header=limits|1=
enum float_round_style {
round_indeterminate       = -1,
round_toward_zero         = 0,
round_to_nearest          = 1,
round_toward_infinity     = 2,
round_toward_neg_infinity = 3
};
Enumeration constants of type `std::float_round_style` indicate the rounding style used by floating-point arithmetic whenever a result of an expression is stored in an object of a floating-point type.

## Enumeration constants


| Item | Description |
|------|-------------|
| **Enumerator** | Meaning |


## See also


| cpp/types/numeric_limits/dsc round_style | (see dedicated page) |
| cpp/numeric/fenv/dsc FE_round | (see dedicated page) |

