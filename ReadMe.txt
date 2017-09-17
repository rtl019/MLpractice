HW-6 readMe file
Team: kshaikh_mislam
Kazim Hyder Nizam Shaikh
Muhaimin Islam

IMPORTANT THING: For our easiness, we renamed the SacramentoRealEstateTransactions.csv to real.csv
and SacramentoCimeJanuary2006.csv to C.csv. Please rename your files before you start grading. Some functions
that we have typed ((especially the filter and report function) have file names or column names already specified in it and doesn't ask the user to input
the filename so please be careful. All fucntions would work perfectly if you keep this thing in consideration.

The homework pdf didn't ask us to make a wrapper so we did not make it. We have told how to run each module
below so have a look:

1) RealestateData.py module

In this module we wrote our own designed LatlongToPixel function and used that to convert latitude and longitude 
values that we got from each row in the csv file. We defined several colors for different conditions as instructed
and plotted circles on the map accordingly. In the Map function we inserted the respective filename and columnname
'price' and it returned the map with plots. We took a screen shot which is attached.

2)HW6_Data.py

In this module we created a map of crimes from the data in the csv that we had. We saw a pattern in the ucr_ncic_code
and on the basis of that pattern we created the conditions required for the color assignment. The conditions can
be reviewed in the function Crime(fileName,columnName).In this function we inserted the respective filename and
columnname
'ucr_ncic_code' and it returned the map with plots. We took a screen shot which is attached.

3)HW6_Filter.py

In this module we returned a list of 

The latitude, longitude, and distance specified in the report
• The number of residences sold within the distance from the given latitude and longitude
• The minimum, mean, median, and maximum selling prices
• The mean number of bedrooms and mean number of bathrooms
• The number and types of crimes reported within that distance of that location

by extracting the data from the csv file.

In this module module we made another function named report() this function writes the specified above topics
in a given textfile. this function takes 4 parameters they are latitude,longitude,distance and the report 
outputfile. The grader shoudl write the name of the file in the Outname parameter and then the output report
would be written and saved in that file. He should also mention the required longitude and latitude
and the distance. A text file containing a command line and the report for a selected location is attached.

4) ExtraCredit.py
We imported the modules we needed for this module. Please run the module and then enter Extracredit()
in the Python Shell to get started. A map would pop up and follow the instructions in the text
written on the map. Click one point and click another in the required distance and then check
your Python Shell to see th list of the filtered data. The output gives latitude of the first click,
longitude, distance number of residences sold within that distance, min, max, mean, median of the
seling prices, mean of bed and mean of bath and number and type of crimes in the specified order.
