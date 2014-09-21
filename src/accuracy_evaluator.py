#!/usr/bin/env python
# accuracy_evaluator 0.0.1
# Generated by dx-app-wizard.
#
# Basic execution pattern: Your app will run on a single machine from
# beginning to end.
#
# See https://wiki.dnanexus.com/Developer-Portal for documentation and
# tutorials on how to modify this file.
#
# DNAnexus Python Bindings (dxpy) documentation:
#   http://autodoc.dnanexus.com/bindings/python/current/

import os
import dxpy

@dxpy.entry_point('main')
def main(bam_file, vcf_file, qual_cutoff, depth_cutoff, bed_file=None):

    # The following line(s) initialize your data object inputs on the platform
    # into dxpy.DXDataObject instances that you can start using immediately.

    bam_file = dxpy.DXFile(bam_file)
    if bed_file is not None:
        bed_file = dxpy.DXFile(bed_file)
    vcf_file = dxpy.DXFile(vcf_file)

    # The following line(s) download your file inputs to the local file system
    # using variable names for the filenames.

    dxpy.download_dxfile(bam_file.get_id(), "bam_file")

    dxpy.download_dxfile(vcf_file.get_id(), "vcf_file")
    if bed_file is not None:
        dxpy.download_dxfile(bed_file.get_id(), "bed_file")

    # Fill in your application code here.

    # The following line(s) use the Python bindings to upload your file outputs
    # after you have created them on the local file system.  It assumes that you
    # have used the output field name for the filename for each output, but you
    # can change that behavior to suit your needs.

    sites_for_manual_review = dxpy.upload_local_file("sites_for_manual_review")

    # The following line fills in some basic dummy output and assumes
    # that you have created variables to represent your output with
    # the same name as your output fields.

    output = {}
    output["sites_for_manual_review"] = dxpy.dxlink(sites_for_manual_review)
    output["number_of_missed_sites"] = number_of_missed_sites
    output["found_sites"] = found_sites
    output["Sensitivity"] = Sensitivity
    output["specificity"] = specificity

    return output

dxpy.run()