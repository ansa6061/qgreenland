from qgreenland._typing import ResamplingMethod, StepArgs
from qgreenland.config.project import project
from qgreenland.models.config.step import CommandStep


def warp_and_cut(
    *,
    # TODO: think about how to require all step template functions to take
    # input_file, output_file.
    input_file,
    output_file,
    cut_file,
    resampling_method: ResamplingMethod = 'bilinear',
    reproject_args: StepArgs = (),
    cut_args: StepArgs = (),
) -> list[CommandStep]:
    reproject = CommandStep(
        args=[
            'gdalwarp',
            '-t_srs', project.crs,
            '-r', resampling_method,
            *reproject_args,
            input_file,
            '{output_dir}/warped.tif',
        ],
    )

    cut = CommandStep(
        args=[
            'gdalwarp',
            '-cutline',
            cut_file,
            '-crop_to_cutline',
            '-co', 'COMPRESS=DEFLATE',
            *cut_args,
            '{input_dir}/warped.tif',
            output_file,
        ],
    )

    return [reproject, cut]
