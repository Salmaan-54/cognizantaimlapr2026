"""Base store class for healthcare entities."""

from conf.logger_conf import setup_logger


class BaseStore:
    """Generic base store for healthcare entities with common CRUD operations."""

    def __init__(self, entity_name: str):
        self.entities = []
        self.entity_name = entity_name
        self.logger = setup_logger(f"{entity_name}Store.log")

    def add_entity(self, entity):
        """Add an entity to the store."""
        self.logger.info(f"Adding {self.entity_name}: {entity}")
        self.entities.append(entity)

    def get_entity_by_id(self, entity_id: int):
        """Get entity by ID. Raises exception if not found."""
        self.logger.info(f"Getting {self.entity_name} by id: {entity_id}")
        for entity in self.entities:
            if hasattr(entity, 'id') and entity.id == entity_id:
                return entity
        raise ValueError(f"{self.entity_name} with id {entity_id} not found")

    def get_all_entities(self):
        """Get all entities in the store."""
        self.logger.info(f"Getting all {self.entity_name}s")
        return self.entities

    def delete_entity(self, entity_id: int) -> bool:
        """Delete an entity by ID."""
        self.logger.info(f"Deleting {self.entity_name} with id: {entity_id}")
        entity = self.get_entity_by_id(entity_id)
        if entity:
            self.entities.remove(entity)
            return True
        return False
