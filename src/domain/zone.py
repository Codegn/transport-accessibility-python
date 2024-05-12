from dataclasses import dataclass

@dataclass(frozen=True)
class Zone:
    id: int
    name: str = ''
