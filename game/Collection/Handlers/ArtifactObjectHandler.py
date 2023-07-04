# game packages
# entity packages
from Entity.Stats.StarRating import StarRating
from Entity.Artifact.Artifact import Artifact

# content packages
from Content.ContentManager import ContentManager

# collection packages
from .BuffArrayHandler import BuffArrayHandler
from .ExperienceObjectHandler import ExperienceObjectHandler

# vars
content = ContentManager()

class ArtifactObjectHandler:
    """
    Makes a Handler of a BuffArray

    parameters

    artifact_object: Object
        the artifact info
    """

    artifact_object = None

    def __init__(self, artifact_object):
        self.artifact_object = artifact_object

    def create_artifact(self):
        experience = ExperienceObjectHandler(self.artifact_object["experience"]).create_experience()
        experience.limit = self.artifact_object["star rating"] * 4
        attributes = []
        for buff in self.artifact_object["stats"]["attributes"]:
            attributes.append(BuffArrayHandler(buff["buff"]).create_buff())

        artifact = Artifact(
            name=self.artifact_object["name"],
            star_rating=StarRating(self.artifact_object["star rating"]),
            family=self.artifact_object["family"],
            main_attribute=BuffArrayHandler(self.artifact_object["stats"]["main attribute"]).create_buff(),
            attributes=attributes,
            experience=experience
        )

        artifact_check_result = content.check_artifact(artifact)
        if artifact_check_result is not None:
            artifact = artifact_check_result()

        return artifact
