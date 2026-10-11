# TurboMOVES: Experimental Inputs and Data Availability

This repository provides the input files and run configurations for the different experimental designs evaluated in the **TurboMOVES paper**. The files are organized by experimental case to support transparency, inspection, and reproduction of the study's experiments.

## Experimental cases

Each folder contains the configuration files for its corresponding experimental case. The descriptions below summarize the settings in the uploaded files; refer to the paper for the experimental rationale and analysis.

| Case | Folder | Configuration and available files |
| --- | --- | --- |
| A | [CaseA](CaseA/) | County inventory configurations for eight New York counties, with a separate run specification and import configuration for each county. |
| C | [Case C](Case%20C/) | Default-domain inventory configuration covering eight New York counties. Includes a run specification and import configuration. |
| D | [CaseD](CaseD/) | Project inventory configurations for Bronx County, with build and no-build scenarios for hours 1–24. Includes run specifications, import configurations, two input workbooks, and a batch manifest. |
| E | [CaseE](CaseE/) | Project emission-rate configurations for Bronx County, with build and no-build scenarios for hours 1–24. Includes run specifications, import configurations, two input workbooks, and a batch manifest. |
| F | [Case F](Case%20F/) | Default-domain emission-rate configuration covering eight New York counties. Includes a run specification and import configuration. |

## File guide

- **`.mrs`** — MOVES run specifications defining the model settings and selected scenarios.
- **`*_Import.xml`** — Import configurations defining input database settings and, where applicable, references to input tables or workbooks.
- **`.xlsx`** — Project input workbooks supplied for Cases D and E.
- **`*_batch_manifest.csv`** — Lists the scenario, hour, run specification, import configuration, and input/output database names for Cases D and E.

The run specifications identify **MOVES 5.0.0**. Before running an experiment, check the file paths and database settings against your local environment, including any `@DIR@` placeholders in the import files.

## Data availability

The experimental input files and run configurations shared with the TurboMOVES paper are available in this repository:

**https://github.com/caferavci/uTECH-Turbo-MOVES**

Case A's import configurations reference county-specific `*_2023_MOVES_inputs.xlsx` workbooks that are not included in the current repository. These workbooks are required to execute the associated imports. The two project input workbooks for each of Cases D and E are included in their respective folders.

## License

See [LICENSE](LICENSE) for the repository's license terms.
