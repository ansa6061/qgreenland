from qgreenland.models.config.asset import OnlineAsset
from qgreenland.models.config.dataset import Dataset


image_mosaic = Dataset(
    id='image_mosaic',
    assets=[
        OnlineAsset(
            id='2019',
            provider='gdal',
            url=(
                '/vsicurl/http://its-live-data.jpl.nasa.gov.s3.amazonaws.com/'
                'rgb_mosaics/GRE2/Greenlandmedian_Aug_2019.vrt'
            ),
        ),
        OnlineAsset(
            id='2015',
            provider='gdal',
            url=(
                '/vsicurl/http://its-live-data.jpl.nasa.gov.s3.amazonaws.com/'
                'rgb_mosaics/GRE/GRE_L8_Aug_2015_on_S3.vrt'
            ),
        ),
    ],
    # TODO: Switch to class instantiation. Makes it easier to differentiate keys
    # from values in this big wall-of-string.
    metadata={
        'title': 'Sentinel-2 Imagery Mosaics',
        # Editability matters most, so we use """triple-quote strings""".
        'abstract': (
            """Abstract for reference publication: Each summer, surface melting
            of the margin of the Greenland Ice Sheet exposes a distinctive
            visible stratigraphy that is related to past variability in
            subaerial dust deposition across the accumulation zone and
            subsequent ice flow toward the margin. Here we map this surface
            stratigraphy along the northern margin of the ice sheet using
            mosaicked Sentinel-2 multispectral satellite imagery from the end of
            the 2019 melt season and finer-resolution WorldView-2/3 imagery for
            smaller regions of interest.  We trace three distinct transitions in
            apparent dust concentration and the top of a darker basal layer. The
            three dust transitions have been identified previously as
            representing late-Pleistocene climatic transitions, allowing us to
            develop a coarse margin chronostratigraphy for northern Greenland.
            Substantial folding of late-Pleistocene stratigraphy is observed but
            uncommon. The oldest conformal surface-exposed ice in northern
            Greenland is likely located adjacent to Warming Land and may be up
            to ~55 thousand years old. Basal ice is commonly exposed hundreds of
            metres from the ice margin and may indicate a widespread frozen
            basal thermal state. We conclude that the ice margin across northern
            Greenland offers multiple opportunities to recover paleoclimatically
            distinct ice relative to previously studied regions in southwestern
            Greenland.

            QGreenland displays 2015 and 2019 Sentinel-2 mosaics as online-only
            access layers."""
        ),
        'citation': {
            'text': (
                """MacGregor JA, Fahnestock MA, Colgan WT, Larsen NK, Kjeldsen
                KK, Welker JM (2020). The age of surface-exposed ice along the
                northern margin of the Greenland Ice Sheet. Journal of
                Glaciology 66(258), 667–684.

                https://doi.org/10.1017/jog.2020.62"""
            ),
            'url': 'https://doi.org/10.1017/jog.2020.62',
        },
    },
)
