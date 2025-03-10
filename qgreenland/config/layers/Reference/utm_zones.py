from qgreenland.config.datasets.utm_zones import utm_zones as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import Layer, LayerInput


utm_zones = Layer(
    id='utm_zones',
    title='Universal Transverse Mercator (UTM) zones',
    description=(
        """Polygons representing Universal Transverse Mercator (UTM) zones."""
    ),
    tags=[],
    style='utm_zones',
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *compressed_vector(
            ogr2ogr_args=(
                '-where', '"\"ZONE\" != 0"',
            ),
            input_file='{input_dir}/utmzone.zip',
            output_file='{output_dir}/utm_zones.gpkg',
            # TODO: Use SQL to generate the label currently set in the style:
            #       `concat(ZONE, ROW_)`
            # ?
        ),
    ],
)
