"""Physics functions for phonons in 1D atomic chains (reduced units)."""

import numpy as np


def monatomic_dispersion(k, C=1.0, m=1.0, a=1.0):
    """Phonon frequency omega(k) of a 1D monatomic chain.

    Uses omega = 2 * sqrt(C/m) * |sin(k*a/2)|.

    Parameters
    ----------
    k : float or np.ndarray
        Wavevector (usually in the first Brillouin zone, -pi/a <= k <= pi/a).
    C : float
        Spring constant between neighbouring atoms.
    m : float
        Atomic mass.
    a : float
        Lattice constant (distance between atoms).

    Returns
    -------
    float or np.ndarray
        Angular frequency omega, same shape as k.
    """
    return 2 * np.sqrt(C / m) * np.abs(np.sin(k * a / 2))
