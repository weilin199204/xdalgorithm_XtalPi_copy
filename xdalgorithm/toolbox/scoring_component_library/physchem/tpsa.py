from rdkit.Chem.Descriptors import TPSA
from xdalgorithm.toolbox.reinvent.scoring.component_parameters import ComponentParameters
from xdalgorithm.toolbox.reinvent.scoring.score_components.physchem.base_physchem_component import BasePhysChemComponent


class PSA(BasePhysChemComponent):
    def __init__(self, parameters: ComponentParameters):
        super().__init__(parameters)

    def _calculate_phys_chem_property(self, mol):
        return TPSA(mol)

    def get_component_type(self):
        return "tpsa"
