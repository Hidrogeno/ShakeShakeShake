# ShakeShakeShake
Playing around with earthquake data from SSN

SSNMX.csv is a file obtained from the Mexican [Servicio Sismológico Nacional](http://www2.ssn.unam.mx:8080/catalogo/), taking into account all earthquakes with a magnitude >= 5.0 since January 1st 1900. It has been trimmed for easier handling.

noGUI reads the SSNMX.csv file and generates graphs for the following things:

- Number of earthquakes by month.
- Average magnitude of earthquakes by month.
- Number of earthquakes that happened on a given month by year.

You can set a threshold to the minimum intensity to consider by changing the mMin value.