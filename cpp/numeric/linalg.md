---
title: Basic linear algebra algorithms
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/linalg
---


# Basic linear algebra algorithms mark since c++26

Basic linear algebra algorithms are based on the dense Basic Linear Algebra Subroutines ([Basic Linear Algebra Subprograms|BLAS](https://en.wikipedia.org/wiki/Basic Linear Algebra Subprograms|BLAS)) which corresponds to a subset of the [http://www.netlib.org/blas/blast-forum/blas-report.pdf BLAS Standard]. These algorithms that access the elements of arrays view those elements through `std::mdspan` representing vector or matrix.
The BLAS algorithms are categorized into three sets of operations called ''levels'', which generally correspond to the degree of the polynomial in the complexities of algorithms:
* [Basic Linear Algebra Subprograms#Level 1|BLAS 1](https://en.wikipedia.org/wiki/Basic Linear Algebra Subprograms#Level 1|BLAS 1): All algorithms with `std::mdspan` parameters perform a count of `std::mdspan` array accesses and arithmetic operations that are ''linear'' in the maximum product of extents of any `std::mdspan` parameter. These algorithms contain ''vector'' operations such as dot products, norms, and vector addition.
* [Basic Linear Algebra Subprograms#Level 2|BLAS 2](https://en.wikipedia.org/wiki/Basic Linear Algebra Subprograms#Level 2|BLAS 2): All algorithms have general complexity in ''quadratic'' time. These algorithms contain ''matrix-vector'' operations such as matrix-vector multiplications and a solver of the triangular linear system.
* [Basic Linear Algebra Subprograms#Level 3|BLAS 3](https://en.wikipedia.org/wiki/Basic Linear Algebra Subprograms#Level 3|BLAS 3): All algorithms have general complexity in ''cubic'' time. These algorithms contain ''matrix-matrix'' operations such as matrix-matrix multiplications and a solver of the multiple triangular linear systems.


| linalg | |
| std::linalg | |
| cpp/numeric/linalg/dsc scaled_accessor | (see dedicated page) |
| cpp/numeric/linalg/dsc conjugated_accessor | (see dedicated page) |
| cpp/numeric/linalg/dsc layout_transpose | (see dedicated page) |
| cpp/numeric/linalg/dsc scaled | (see dedicated page) |
| cpp/numeric/linalg/dsc conjugated | (see dedicated page) |
| cpp/numeric/linalg/dsc transposed | (see dedicated page) |
| cpp/numeric/linalg/dsc conjugate_transposed | (see dedicated page) |
| linalg | |
| std::linalg | |
| cpp/numeric/linalg/dsc setup_givens_rotation | (see dedicated page) |
| cpp/numeric/linalg/dsc apply_givens_rotation | (see dedicated page) |
| cpp/numeric/linalg/dsc swap_elements | (see dedicated page) |
| cpp/numeric/linalg/dsc scale | (see dedicated page) |
| cpp/numeric/linalg/dsc copy | (see dedicated page) |
| cpp/numeric/linalg/dsc add | (see dedicated page) |
| cpp/numeric/linalg/dsc dot | (see dedicated page) |
| cpp/numeric/linalg/dsc dotc | (see dedicated page) |
| cpp/numeric/linalg/dsc vector_sum_of_squares | (see dedicated page) |
| cpp/numeric/linalg/dsc vector_two_norm | (see dedicated page) |
| cpp/numeric/linalg/dsc vector_abs_sum | (see dedicated page) |
| cpp/numeric/linalg/dsc vector_idx_abs_max | (see dedicated page) |
| cpp/numeric/linalg/dsc matrix_frob_norm | (see dedicated page) |
| cpp/numeric/linalg/dsc matrix_one_norm | (see dedicated page) |
| cpp/numeric/linalg/dsc matrix_inf_norm | (see dedicated page) |
| linalg | |
| std::linalg | |
| cpp/numeric/linalg/dsc matrix_vector_product | (see dedicated page) |
| cpp/numeric/linalg/dsc symmetric_matrix_vector_product | (see dedicated page) |
| cpp/numeric/linalg/dsc hermitian_matrix_vector_product | (see dedicated page) |
| cpp/numeric/linalg/dsc triangular_matrix_vector_product | (see dedicated page) |
| cpp/numeric/linalg/dsc triangular_matrix_vector_solve | (see dedicated page) |
| cpp/numeric/linalg/dsc matrix_rank_1_update | (see dedicated page) |
| cpp/numeric/linalg/dsc matrix_rank_1_update_c | (see dedicated page) |
| cpp/numeric/linalg/dsc symmetric_matrix_rank_1_update | (see dedicated page) |
| cpp/numeric/linalg/dsc hermitian_matrix_rank_1_update | (see dedicated page) |
| cpp/numeric/linalg/dsc symmetric_matrix_rank_2_update | (see dedicated page) |
| cpp/numeric/linalg/dsc hermitian_matrix_rank_2_update | (see dedicated page) |
| linalg | |
| std::linalg | |
| cpp/numeric/linalg/dsc matrix_product | (see dedicated page) |
| cpp/numeric/linalg/dsc symmetric_matrix_product | (see dedicated page) |
| cpp/numeric/linalg/dsc hermitian_matrix_product | (see dedicated page) |
| cpp/numeric/linalg/dsc triangular_matrix_product | (see dedicated page) |
| cpp/numeric/linalg/dsc symmetric_matrix_rank_k_update | (see dedicated page) |
| cpp/numeric/linalg/dsc hermitian_matrix_rank_k_update | (see dedicated page) |
| cpp/numeric/linalg/dsc symmetric_matrix_rank_2k_update | (see dedicated page) |
| cpp/numeric/linalg/dsc hermitian_matrix_rank_2k_update | (see dedicated page) |
| cpp/numeric/linalg/dsc triangular_matrix_matrix_solve | (see dedicated page) |
| linalg | |
| std::linalg | |
| cpp/numeric/linalg/dsc_storage_order_tags | (see dedicated page) |
| cpp/numeric/linalg/dsc_triangle_tags | (see dedicated page) |
| cpp/numeric/linalg/dsc_diagonal_tags | (see dedicated page) |
| cpp/numeric/linalg/dsc layout_blas_packed | (see dedicated page) |


## Notes


## Example


### Example

```cpp
#include <cassert>
#include <cstddef>
#include <execution>
#include <linalg>
#include <mdspan>
#include <numeric>
#include <vector>

int main()
{
    std::vector<double> x_vec(42);
    std::ranges::iota(x_vec, 0.0);

    std::mdspan x(x_vec.data(), x_vec.size());

    // x[i] *= 2.0, executed sequentially
    std::linalg::scale(2.0, x);

    // x[i] *= 3.0, executed in parallel
    std::linalg::scale(std::execution::par_unseq, 3.0, x);

    for (std::size_t i{}; i != x.size(); ++i)
        assert(x[i] == 6.0 * static_cast<double>(i));
}
```


## External links

