"""Extractor package. Importing it registers all site extractors."""

from .base import Extractor, get_extractor, register  # noqa: F401
from . import developers  # noqa: F401  (registers DevelopersExtractor)
from . import support  # noqa: F401  (registers SupportExtractor)
