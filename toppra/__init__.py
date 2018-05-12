"""
TOPP-RA
=======
Reachability-Analysis-based Time-Optimal Path Parametrization.

This package produces routines for creation and handling path constraints
using the algorithm `TOPP-RA`.
"""
# import constraint
# from .TOPP import *
from .interpolator import *
# from .constraints import *
from .utils import smooth_singularities, setup_logging
# from . import postprocess
# from .postprocess import compute_trajectory_gridpoints, compute_trajectory_uniform
from .planning_utils import retime_active_joints_kinematics
import constraint as constraint

setup_logging()
