# Erstellen von Installationspaketen

Einfach die Pipeline ausführen, dann wird ein neues Installationspaket in \\file.lt.lutumtappert.de\LTSoftware\Prerelease\QGis Erweiterungen\Infas LT Geocoder
erstellt. (TODO: Wird sich noch ändern!)

# Release bereitstellen

Wenn eine Version als Release bereitgestellt werden soll:
- Version im Plugin Quellcode prüfen
- Installationspaket Erstellen
- Im Unterordner Releases eine Datei nach Namensmuster ```infas-lt-geocoder-qgis-plugin-major-minor.zip``` erstellen, also z.B. ```infas-lt-geocoder-qgis-plugin-1-3.zip```.
- Per SFTP in den Server home66667588.1and1-data.host hochladen, im Server in den Ordner _/download.geomarketing.de/full_ laden (Zugangsdaten siehe Keepass, Ordner IONOS, FTP-Zugang 1&1 Server)
- Der Doanload ist dann über https://download.geomarketing.de/full/infas-lt-geocoder-qgis-plugin-major-minor.zip verfügbar.