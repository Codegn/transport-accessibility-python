from pathlib import Path

from src.domain.accessibility.entities.accessibility_by_zone import AccessibilityByZone
from src.domain.accessibility.repository.accessibility_repository import (
    AccessibilityRepository,
)


class SaveAccessibilityByZoneToFile:
    def __init__(self, accessibility_repository: AccessibilityRepository):
        self.accessibility_repository = accessibility_repository

    def save(self, accessibility_by_zone: AccessibilityByZone, output_path: Path):
        self.accessibility_repository.save_accessibility_by_zone_to_file(accessibility_by_zone, output_path)
