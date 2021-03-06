from hasty.attribute import Attribute
from hasty.client import Client
from hasty.dataset import Dataset
from hasty.export_job import ExportJob
from hasty.image import Image
from hasty.inference import Detector, InstanceSegmentor, SemanticSegmentor
from hasty.label import Label
from hasty.label_class import LabelClass
from hasty.project import Project
import hasty.label_utils as label_utils


def int_or_str(value):
    try:
        return int(value)
    except ValueError:
        return value


__version__ = '0.2.1'
VERSION = tuple(map(int_or_str, __version__.split('.')))

__all__ = [
    'Attribute',
    'Client',
    'Dataset',
    'Detector',
    'ExportJob',
    'Image',
    'InstanceSegmentor',
    'Label',
    'LabelClass',
    'Project',
    'SemanticSegmentor',
    'label_utils'
]
