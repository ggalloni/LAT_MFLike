from .mflike import MFLike
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("mflike")
except PackageNotFoundError:
    # package is not installed
    pass
