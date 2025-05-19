from abc import ABC, abstractmethod
from typing import Any, Dict, List


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, data: dict) -> None:
        pass

    @abstractmethod
    def get(self, product_id: int) -> Dict[Any, Any]:
        pass

    @abstractmethod
    def list(self) -> List[Any]:
        pass
