def raw_coefficients(degree: int, max_abs_coeff: int) -> list[tuple[int, ...]]:
    if degree == 0:
        return [(c,) for c in range(-max_abs_coeff, max_abs_coeff+1)]
    return [
        (c, *coeffs)
        for c in range(-max_abs_coeff, max_abs_coeff+1)
        for coeffs in raw_coefficients(degree-1, max_abs_coeff)
    ]

def coefficients(n: int) -> list[tuple[int, ...]]:
    raw = []
    for degree in range(1, n+1):
        raw.extend(raw_coefficients(degree, n))
    # remove zero-degree polys
    out = []
    for poly in raw:
        if any(c != 0 for c in poly[1:]):
            out.append(poly)
    return out

def polynomials(max_n: int) -> list[tuple[int, ...]]:
    polys = []
    for n in range(1, max_n+1):
        new_polys = coefficients(n)
        for poly in new_polys:
            if poly not in polys:
                polys.append(poly)
    return polys

for _poly in polynomials(3):
    print(_poly)