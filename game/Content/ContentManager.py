# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.StarRating import StarRating

# content packages
from .ArtifactContentManager import ArtifactContentManager
from .LocationContentManager import LocationContentManager
from .CharacterContentManager import CharacterContentManager

# collection packages
from Collection.Dictionary import Dictionary

# graphics packages
from Graphics.Text.Text import Text

class ContentManager:
    characters = None
    weapons = None
    families = None
    locations = None

    def __init__(self):
        artifact_content_manager = ArtifactContentManager()
        artifact_content_manager.load_content()
        location_content_manager = LocationContentManager()
        location_content_manager.load_content()
        character_content_manager = CharacterContentManager()
        character_content_manager.load_content()
        self.families = artifact_content_manager.get_families()
        self.locations = location_content_manager.get_locations()
        self.characters = character_content_manager.get_characters()

    def check_character(self, name: str, description: str):
        for content_character in self.characters:
            if name == content_character.name:
                if description == content_character.description:
                    return content_character

        return None

    def check_artifact(self, artifact: Artifact):
        for content_family in self.families:
            if artifact.family == content_family.name:
                for a_family_artifact in content_family.artifacts:
                    if artifact.name == a_family_artifact.name:
                        return a_family_artifact

        return None

    def display_artifact_families(self):
        families = []
        family_content = []
        for family in self.families:
            families.append(family.name)
            artifact_list = []
            for artifact in family.artifacts:
                artifact_list.append(f"{artifact(StarRating(1)).name}")

            family_content.append(artifact_list)

        Dictionary(families, family_content).read()