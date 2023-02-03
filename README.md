# Introduction 
The plugin developed is an QGIS extension for infas LT Geocoder. This plugin supports single, batch, and reverse geocoding of the addresses.

# Getting Started
Following steps are to be followed in order to setup the plugin:
1. Installation process
   1. Search for infas LT Geocoder from Plugins/Manage and Install Plugin in QGIS
   2. Click on infas LT Geocoder to load the plugin
2. Software dependencies
   1. QGIS 3.8 or higher
   2. Python 3.7 or higher, if any necessary library is not installed by default then install it from OSGeo4W Shell by typing following commands:
    1. -m pip install package-name or -m pip install --user package-name
    2. More information at https://landscapearchaeology.org/2018/installing-python-packages-in-qgis-3-for-windows/
    3. Following Python libraries- requests, pandas, math
3. Plugin information
This plugin provides three functionalities and steps to operate those are mentioned below:
   1. Single Geocoding- User needs to enter at least a city to run the plugin
   2. Batch Geocoding- User needs to provide a file containing multiple addresses
   3. Reverse Geocoding- User needs to provide lat and long co-ordinate with a valid license key 

Note- This plugin supports English and German language.

# Quick Contributing Guide
1. Fork and clone locally
2. Create a topic specific branch. Add some nice feature. Do not forget the tests ;-)
3. Send a Pull Request to spread the fun!

# Need more support or accurate results?
Just contact our support team at [vertrieb@infas-lt.de](mailto:vertrieb@infas-lt.de) or visit our website https://www.infas-lt.de/software/geocodierung/