from xdalgorithm.toolbox.reinvent.scoring.component_parameters import ComponentParameters
from xdalgorithm.toolbox.reinvent.scoring.score_components.physchem.base_physchem_component import BasePhysChemComponent
#from xdalgorithm.toolbox.scoring_component_library.descriptor_components import MolWeight as MW
from rdkit.Chem.Descriptors import MolWt

class MolWeight(BasePhysChemComponent):
    def __init__(self, parameters: ComponentParameters):
        super().__init__(parameters)

    def _calculate_phys_chem_property(self, mol):
        return MolWt(mol)

    def get_component_type(self):
        return "molecular_weight"
