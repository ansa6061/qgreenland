from qgreenland.config.datasets.esa_cci import esa_cci_ice_sheet_velocity_20191214_20200131 as dataset
from qgreenland.config.helpers.steps.compress_and_add_overviews import compress_and_add_overviews
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput


_esa_cci_velocity_params = {
    'esa_cci_velocity_magnitude': {
        'title': 'Land ice surface velocity 2019-2020 (250m)',
        'description': (
            """Magnitude of horizontal ice velocity in meters per day. Data is
            not masked to ice sheet boundary."""
        ),
        'variable': 'land_ice_surface_velocity_magnitude',
        'style': 'esa_cci_velocity',
    },
    'esa_cci_velocity_vertical': {
        'title': 'Land ice surface vertical velocity 2019-2020 (250m)',
        'description': (
            """Vertical ice velocity in meters per day. Data is not masked to
            ice sheet boundary."""
        ),
        'variable': 'land_ice_surface_vertical_velocity',
        'style': 'vertical_velocity',
    },
}


layers = [
    Layer(
        id=layer_id,
        title=params['title'],
        description=params['description'],
        tags=[],
        style=params['style'],
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets['only'],
        ),
        steps=[
            decompress_step(
                input_file='{input_dir}/greenland_iv_250m_s1_20191214_20200131_v1_3.zip',
                decompress_contents_mask=(
                    'greenland_iv_250m_s1_20191214_20200131_v1_3'
                    '/greenland_iv_250m_s1_20191214_20200131_v1_3.nc'
                ),
            ),
            *warp_and_cut(
                input_file=(
                    'NETCDF:{input_dir}/greenland_iv_250m_s1_20191214_20200131_v1_3/'
                    'greenland_iv_250m_s1_20191214_20200131_v1_3.nc'
                    f":{params['variable']}"
                ),
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
    for layer_id, params in _esa_cci_velocity_params.items()
]
