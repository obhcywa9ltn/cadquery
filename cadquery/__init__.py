"""
CadQuery - A parametric 3D CAD scripting framework.

CadQuery is an intuitive, easy-to-use Python module for building parametric
3D CAD models. It is inspired by OpenSCAD but uses Python instead of a
domain-specific language.

Example usage::

    import cadquery as cq

    # Create a simple box
    result = cq.Workplane("XY").box(1, 2, 3)

    # Export to STEP
    cq.exporters.export(result, "box.step")
"""

from .cq import (
    CQContext,
    CQObject,
    Workplane,
)
from .occ_impl.geom import (
    Vector,
    Matrix,
    Plane,
    Location,
)
from .occ_impl.shapes import (
    Shape,
    Vertex,
    Edge,
    Wire,
    Face,
    Shell,
    Solid,
    Compound,
)
from .occ_impl.assembly import (
    Assembly,
    Constraint,
)
from .selectors import (
    Selector,
    NearestToPointSelector,
    ParallelDirSelector,
    DirectionSelector,
    PerpendicularDirSelector,
    TypeSelector,
    DirectionMinMaxSelector,
    CenterNthSelector,
    RadiusNthSelector,
    LengthNthSelector,
    AreaNthSelector,
    StringSyntaxSelector,
)
from . import exporters
from . import importers

__version__ = "2.4.0"
__author__ = "CadQuery Contributors"
__license__ = "Apache 2.0"

__all__ = [
    # Core workplane
    "CQContext",
    "CQObject",
    "Workplane",
    # Geometry
    "Vector",
    "Matrix",
    "Plane",
    "Location",
    # Shapes
    "Shape",
    "Vertex",
    "Edge",
    "Wire",
    "Face",
    "Shell",
    "Solid",
    "Compound",
    # Assembly
    "Assembly",
    "Constraint",
    # Selectors
    "Selector",
    "NearestToPointSelector",
    "ParallelDirSelector",
    "DirectionSelector",
    "PerpendicularDirSelector",
    "TypeSelector",
    "DirectionMinMaxSelector",
    "CenterNthSelector",
    "RadiusNthSelector",
    "LengthNthSelector",
    "AreaNthSelector",
    "StringSyntaxSelector",
    # Submodules
    "exporters",
    "importers",
    # Version info
    "__version__",
]
