"""MultiQC submodule to parse output from Glimpse concordance analysis"""


import logging

from multiqc.base_module import BaseMultiqcModule, ModuleNoSamplesFound

# Import the GLIMPSE submodules
from .err_spl import ErrSplReportMixin
from .err_grp import ErrGrpReportMixin

# Initialise the logger
log = logging.getLogger(__name__)


class MultiqcModule(BaseMultiqcModule, ErrSplReportMixin, ErrGrpReportMixin):
    """Glimpse has a number of different commands and outputs.
    This MultiQC module supports some but not all."""

    def __init__(self):
        # Initialise the parent object
        super(MultiqcModule, self).__init__(
            name="GLIMPSE",
            anchor="glimpse",
            target="GLIMPSE",
            href="https://odelaneau.github.io/GLIMPSE/",
            info="Set of tools for low-coverage whole genome sequencing imputation",
            doi="10.1101/2022.11.28.518213 ",
        )

        # Set up class objects to hold parsed data
        self.general_stats_headers = dict()
        self.general_stats_data = dict()

        # Call submodule functions
        n_reports_found = 1

        # Call submodule functions
        n_reports_found += self.parse_glimpse_err_spl()
        n_reports_found += self.parse_glimpse_err_grp()

        # Exit if we didn't find anything
        if n_reports_found == 0:
            raise ModuleNoSamplesFound

        # Add to the General Stats table (has to be called once per MultiQC module)
        self.general_stats_addcols(self.general_stats_data, self.general_stats_headers)