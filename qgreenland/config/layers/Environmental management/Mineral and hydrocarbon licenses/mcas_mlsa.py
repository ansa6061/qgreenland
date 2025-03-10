from qgreenland.config.datasets.mineral_and_hydrocarbon_licenses import (
    mineral_and_hydrocarbon_licenses as dataset,
)
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import Layer, LayerInput


layer_params = {
    'mcas_mlsa_public_all': {
        'title': 'Public licenses',
        'description': (
            """Mining licenses granted by the government of Greenland."""
        ),
        'asset_id': 'mcas_mlsa_public_all',
    },
    'mcas_mlsa_public_historic': {
        'title': 'Historic public licenses',
        'description': (
            """Historic mining licenses granted by the government of Greenland."""
        ),
        'asset_id': 'mcas_mlsa_public_historic',
    },
}

layers = [
    Layer(
        id=key,
        title=params['title'],
        description=params['description'],
        tags=[],
        style='mcas_mlsa_licenses',
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets[params['asset_id']],
        ),
        steps=[
            *compressed_vector(
                input_file='{input_dir}/*.zip',
                output_file='{output_dir}/final.gpkg',
            ),
        ],
    ) for key, params in layer_params.items()
]
