from qgreenland.config.datasets.velocity_mosaic import velocity_mosaic as dataset
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep


_masked_velocity_mosaic_params = {
    'velocity_mosaic': {
        'title': 'Ice sheet velocity (120m)',
        'description': 'Magnitude of velocity in meters per year.',
        'variable': 'v',
        'style': 'ice_sheet_velocity',
    },
    'velocity_mosaic_error': {
        'title': 'Velocity error (120m)',
        'description': 'Magnitude of velocity error in meters per year.',
        'variable': 'v_err',
        'style': 'ice_sheet_velocity_error',
    },
}

masked_velocity_mosaic_layers = [
    Layer(
        id=layer_id,
        title=params['title'],
        description=params['description'],
        in_package=False,
        tags=[],
        style=params['style'],
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets['only'],
        ),
        steps=[
            CommandStep(
                args=[
                    'gdal_calc.py',
                    '--calc="A*B"',
                    '--outfile={output_dir}/' + f'masked_{layer_id}.tif',
                    '-A', 'NETCDF:{input_dir}/GRE_G0120_0000.nc:v',
                    '-B', 'NETCDF:{input_dir}/GRE_G0120_0000.nc:ice',
                ],
            ),
            *warp_and_cut(
                input_file='{input_dir}/' + f'masked_{layer_id}.tif',
                output_file='{output_dir}/' + f'{layer_id}.tif',
                cut_file=project.boundaries['data'].filepath,
            ),
            *compress_and_add_overviews(
                input_file='{input_dir}/' + f'{layer_id}.tif',
                output_file='{output_dir}/' + f'{layer_id}.tif',
                dtype_is_float=True,
            ),
        ],
    )
    for layer_id, params in _masked_velocity_mosaic_params.items()
]


velocity_mosaic_ice_mask = Layer(
    id='velocity_mosaic_ice_mask',
    title='Ice mask (120m)',
    description=(
        """Ice mask used for ITS_LIVE velocity mosiac."""
    ),
    in_package=False,
    tags=[],
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *warp_and_cut(
            input_file='NETCDF:{input_dir}/GRE_G0120_0000.nc:ice',
            output_file='{output_dir}/velocity_mosaic_ice_mask.tif',
            cut_file=project.boundaries['data'].filepath,
        ),
        *compress_and_add_overviews(
            input_file='{input_dir}/velocity_mosaic_ice_mask.tif',
            output_file='{output_dir}/velocity_mosaic_ice_mask.tif',
            dtype_is_float=False,
        ),
    ],
)
