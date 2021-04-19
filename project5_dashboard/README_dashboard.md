#Project 5: Dashboard - Berlin covid-19 data

<div style="text-align: justify">

The project was developed during the Spiced Academy Data Science Bootcamp using **PostgreSQL** and **AWS cloud services**. Data on the covid-19 pandemic in Berlin were extracted from the information provided by LAGeSo (Landesamt für Gesundheit und Soziales) and cover the period March 2020 to 13 April 2021.*
</div>

*<sub> [https://daten.berlin.de/datensaetze/covid-19-fälle-im-land-berlin-verteilung-nach-altersgruppen; https://daten.berlin.de/datensaetze/covid-19-berlin-verteilung-den-bezirken-gesamtübersicht; https://daten.berlin.de/datensaetze/covid-19-berlin-verteilung-den-bezirken; https://daten.berlin.de/datensaetze/covid-19-berlin-fallzahlen-und-indikatoren-gesamtübersicht; https://daten.berlin.de/datensaetze/covid-19-fälle-im-land-berlin-7tage-inzidenz-nach-altersgruppen-und-meldewochen]. </sub>
<br>

## Dashboard structure


![Dashboard opening](/Users/giudittaparolini/Documents/Bootcamp/vanilla-vectors-student-code/project5_dashboard/image1.png)

<div style="text-align: justify">
The dashboard is composed of six widgets: one introductory text box summarising the main data related to the development of the pandemics in Berlin (people infected with covid-19 so far, deaths, key stages of development) and four plots (incidence of the covid-19 cases over seven days, covid-19 incidence per age group, deaths due to covid-19 and occupancy of the intensive care units (ICU) in the local hospitals by covid patients, distribution of the covid cases per borough.
</div>
<br>

<div style="text-align: justify">
The dashboard has been created using the open source version of the software [metabase](https://www.metabase.com). AWS services were used for hosting in the cloud the postgreSQL database and the EC2 instance running metabase.
</div>
<br>

<div style="text-align: justify">
The data used in the dashboard cover the period from the beginning of the pandemics to 13th April 2021, when the data tables were downloaded. Potentially, the data could be updated daily by connecting to the APIs created by LAGESO. However, before entering them in the database they need proper cleaning (removing Umlaute not recognised by the UFT-8 codification, transforming the formats of numeric data, etc.)
</div>
<br>

## Dashboard content

<br>
* <a name="summary">Summary</a> <br>
* <a name="7daystot">Total Covid-19 incidence over seven days</a><br>
* <a name="7daysage">Covid-19 incidence per age group over seven days</a><br>
* <a name="deaths_icu">Covid-19 deaths and ICU occupancy</a><br>
* <a name="borough">Covid-19 cases per borough</a><br>

<br>


####[Summary](#summary)
<div style="text-align: justify">
Short text box with key data about the development of the pandemic in Berlin.
</div>

![Summary](/Users/giudittaparolini/Documents/Bootcamp/vanilla-vectors-student-code/project5_dashboard/image2.png)
<br>

####[Total Covid-19 incidence over seven days](#7daystot)
<div style="text-align: justify">
Opening plot, chosen as such because the Berlin public authorities use the incidence of covid-19 cases over seven days as a main criterion to take action.
</div>

![Total Covid-19 incidence over seven days](/Users/giudittaparolini/Documents/Bootcamp/vanilla-vectors-student-code/project5_dashboard/image3.png)
<br>

####[Covid-19 incidence per age group over seven days](#7daysage)
<div style="text-align: justify">
The plot provides an insight into how different age groups have been affected by covid-19. In order to plot in chronological order (from 2020 to 2021) the incidence data disaggregated per age group, it was necessary to regroup the time information casting year and week as VARCHAR and joining them to write a unique time information (see SQL query below).
</div>
![Covid-19 incidence per age group over seven days](/Users/giudittaparolini/Documents/Bootcamp/vanilla-vectors-student-code/project5_dashboard/image4.png)


![SQL query](/Users/giudittaparolini/Documents/Bootcamp/vanilla-vectors-student-code/project5_dashboard/image7.png)
<br>

####[Covid-19 deaths and ICU occupancy](#deaths_icu)
<div style="text-align: justify">
The plot displays the covid-19 deaths and ICU occupancy. Berlin public authorities considered also the ICU occupancy as a key factor in the development of the epidemics.
</div>
![Covid-19 deaths and ICU occupancy](/Users/giudittaparolini/Documents/Bootcamp/vanilla-vectors-student-code/project5_dashboard/image5.png)

<br>
####[Covid-19 cases per borough](#borough)
<div style="text-align: justify">
Distribution of the covid-19 cases according to the Berlin borough in which they were registered. Due to limitations in the metabase software, it was not possible to insert a map of the Berlin boroughs. A link to an open source is provided.
</div>
![Covid-19 cases per borough](/Users/giudittaparolini/Documents/Bootcamp/vanilla-vectors-student-code/project5_dashboard/image6.png)

## Dashboard as data stories
<div style="text-align: justify">
BY examining the dashboard, it becomes evident that the covid pandemics did not hit Berlin much for the first months (March 2020 to April 2020), but since October 2020, the situation has significantly deteriorated. A weekly incidence of covid cases superior to 200 has been recorded for many age groups and the pressure on the ICUs of the local hospitals has sensibly increased reaching critical levels at times. Quite significantly, the recorded deaths from March 2020 to September 2020 were slightly more than 200. By the end of December 2020, this number had reached quota 1271 and, by the end of February 2021, the covid deaths in town exceeded 2800.
</div>
