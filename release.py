import re
import zipfile
from collections import defaultdict
from pathlib import Path
# ======================================================================


PATTERNS_PROJECT = ('*.kicad_pro',  # Project
            '*.kicad_sch',  # Schema
            '*.kicad_pcb',  # Layout
            'README.md')    # Instructions

PATTERNS_LIBRARY = ('*.kicad_wks',
                    '*.kicad_sym',
                    'LICENSE.txt')

PATH_BASE = Path(__file__).parent

pattern_datasheet = re.compile(r'\(property "Datasheet" '
                               r'"\${KIPRJMOD}(?:\\{2}|/)'
                               r'Libraries(?:\\{2}|/)'
                               r'Datasheets(?:\\{2}|/)'
                               r'([^\n\t]*\.pdf)"\n')
pattern_footprint = re.compile(r'\(property "Footprint" "([^:\n]*):([^:\n]*)"\n')
pattern_3d_model = re.compile(r'\(model "\${KIPRJMOD}/Libraries/3D-models/([^/\n]*\.step)"\n')
# ======================================================================
def main() -> int:

    path_template = PATH_BASE / 'template'

    paths_zip = [next(path_template.glob(pattern)) for pattern in PATTERNS_PROJECT]

    path_libraries = path_template / 'Libraries'
    path_3d_model_dir = path_libraries / '3D-models'
    path_datasheet_dir = path_libraries / 'Datasheets'

    # Worksheet

    for pattern in PATTERNS_LIBRARY:
        paths_zip.append(next(path_libraries.glob(pattern)))

    # Datasheets

    schema_text = paths_zip[1].read_text()

    datasheet_names: set[str] = set()
    for datasheet in pattern_datasheet.findall(schema_text):
        # This returns duplicates for some reason
        if datasheet not in datasheet_names:
            datasheet_names.add(datasheet)
            paths_zip.append(path_datasheet_dir / datasheet)

    # 3D models

    footprints: defaultdict[str, set[str]] = defaultdict(set)

    for footprint_library, footprint_name in pattern_footprint.findall(schema_text):
        footprints[footprint_library].add(footprint_name)

    paths_3d_models = set()

    for footprint_library, footprint_names in footprints.items():
        if (path_footprint_library := (path_libraries
                                       / f'{footprint_library}.pretty')
            ).exists():
            for footprint_name in footprint_names:
                path_footprint = (path_footprint_library
                                  / f'{footprint_name}.kicad_mod')
                paths_zip.append(path_footprint)
                try:
                    footprint_text = path_footprint.read_text()
                except FileNotFoundError:
                    pass
                for match in pattern_3d_model.findall(footprint_text):
                    paths_3d_models.add(path_3d_model_dir / match)

    paths_zip.extend(paths_3d_models)

    with zipfile.ZipFile('.release.zip', 'w',
                         compression = zipfile.ZIP_DEFLATED) as file:
        for path in paths_zip:
            file.write(path, arcname = path.relative_to(path_template))

    return 0
# ----------------------------------------------------------------------
if __name__ == '__main__':
    raise SystemExit(main())
