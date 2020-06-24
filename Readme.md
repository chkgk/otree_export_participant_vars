# Exporting Participant Variables in oTree

This snippet demos how to export participant variables from oTree. It relies on functionality for custom data export first introduced in oTree 2.6 (beta). 

Basically, we simply create a custom data export function which takes the participant variables you want to export. Take a look at models.py in the "part_vars_export" app to see how it works. From oTree 2.6 (beta) onwards, custom exports defined this way appear as export links in the main "Data" tab.