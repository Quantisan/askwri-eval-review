---
doc_id: 2021_medindo-mp25-com-sensores-de-baixo-custo_6821
source_pdf: kp-docs/askwri-kps/2021_medindo-mp25-com-sensores-de-baixo-custo_6821.pdf
extraction_method: cache-plaintext
char_count: 56773
title: Medindo MP2,5 com Sensores de Baixo Custo
authors: Contreras, Seth; Dye, Tim; Marcelo, Audrei; Campos, Marco Siqueira; Albuquerque, Cristina; Tavares, Virginia; Jotz, Matheus
date_published: 2/8/2021
article_type: Practice Note
sub_tag: Transport decarbonization
wri_primary_office: WRI Brasil
wri_programs: Cities
language: Portuguese
url: "https://www.wribrasil.org.br/publicacoes/medindo-mp25-com-sensores-de-baixo-custo"
doi: "https://doi.org/10.46830/wripn.19.00035"
summary: "WRI Brasil evaluated AirBeam2 low-cost PM2.5 sensors during São Paulo's Car-Free Friday initiative (September–November 2018), deploying 30 sensors in fixed and mobile configurations across the city's historic center. Collocation against CETESB reference stations showed strong sensor-to-sensor correlation (R²>0.94) and acceptable reference agreement (R²≈0.9 for daily means). Fixed sensors revealed significantly lower PM2.5 differences between car-free and non-car-free zones on Car-Free Fridays, suggesting the initiative positively impacts local air quality. Mobile sensors generated pollution hotspot maps. Key recommendations include mandatory pre/post collocation, backup sensors, municipal partnerships for site access, and treating low-cost sensors as complementary—not replacement—monitoring tools."
---

# Medindo MP2,5 com Sensores de Baixo Custo

PRACTICE NOTE
Measuring PM2.5 with 
Low-Cost Sensors 
Practice notes provide rapid analysis of experiences related 
to a particular project. The analysis and recommendations 
are limited to the specific context presented in the note and 
should not be construed to apply more broadly.
WRIBRASIL.ORG.BR

wribrasil.org.br
2
Executive Summary ..................................................................................................................... 3
Introduction ...................................................................................................................................... 5
Logistical Procedures ................................................................................................................. 8
     Initial Checking Steps ........................................................................................................... 8
     Logistics of Fixed Sensor System .................................................................................. 8
     Logistics of Mobile Sensor System ............................................................................... 9
     Data Management ............................................................................................................... 10
     Contigency Planning: Sensor Backup Approach ................................................ 10
     Data Quality Assurance Procedures .......................................................................... 10
Methodology .................................................................................................................................. 10
     Collocation: Pre- and Postprocessing ........................................................................ 11
     Fixed Sensor System Study ............................................................................................ 14
     Mobile Sensor System Study ......................................................................................... 15
Results .............................................................................................................................................. 15
     Collocation ............................................................................................................................... 15
     Fixed Sensor System .......................................................................................................... 17
     Mobile Sensor System ....................................................................................................... 17
Lessons Learned ......................................................................................................................... 19
Conclusions .................................................................................................................................... 19
References ...................................................................................................................................... 21
Authors
Cristina Albuquerque, Matheus Bello Jotz, Virginia Bergamaschi Tavares, Seth Contreras, Tim Dye, 
Audrei Marcelo and Marco Siqueira Campos
Layout
Ana Porazzi
Cover Photo
Joana Oliveira/WRI Brasil
July 2021
Suggested Citation: Albuquerque, C., M.B. Jotz, V.B. Tavares, S. Contreras, T. Dye, A. 
Marcelo, and M.S. Campos. 2021. “Measuring PM 2.5 with Low-Cost Sensors”. Practice Note. 
Porto Alegre, Brazil: WRI Brasil. Available online at: https://doi.org/10.46830/wripn.19.00035
CONTENTS

PRACTICE NOTE   ▪  MEASURING PM 2.5  WITH LOW-COST SENSORS 
3
 ▪ In 2018, WRI evaluated the use of low-cost air quality 
sensors1 measuring particulate matter 2.5 (PM2.5) 
concentrations on some days of an urban intervention, 
São Paulo’s Car-Free Friday. The use of these sensors can 
enhance both the existing network of air quality monitors in 
cities as well as analysis of the impact of specific initiatives. 
This project seeks to help cities by sharing methodology 
used, lessons learned, key takeaways, and best practices.
 ▪ São Paulo’s Car-Free Friday initiative closes off streets in 
the historic center of the city on the last Friday of each 
month. WRI used low-cost air quality sensors—in both 
fixed and mobile modes—to measure PM 2.5 concentrations 
on some days of this initiative.
 ▪ Logistical preparations with a large number of measuring 
instruments are also provide valuable lessons learned from 
this project. This practice note discusses procedures to 
calibrate the instruments, to prepare a site to install a low-
cost sensor, and to maintain and manage the instruments.
 ▪ Data generated indicate that the initiative may be having a 
positive impact on local PM2.5 concentrations. Despite the 
small sample of days, the analysis revealed a significant 
statistical difference between the PM2.5 concentrations on 
Car-Free Fridays and those on regular Fridays. 
HIGHLIGHTS
EXECUTIVE SUMMARY
maintenance, and operation high costs of conventional 
monitoring stations do not allow most cities to have 
sufficient geographic coverage of monitoring stations 
spread across their airshed (ISS 2014; IEMA 2014). 
Although low-cost sensors are not yet as accurate 
as traditional monitoring stations, they do offer 
several advantages: they are portable, easier to use, 
and more can be deployed due to their lower cost. 
These instruments provide an opportunity to conduct 
special monitoring studies and should be tested as a 
complementary technology to the traditional monitoring 
stations, helping cities to increase monitoring 
capacity and public awareness about air quality.
ABOUT THIS PRACTICE NOTE
The objectives of this practice note are to evaluate 
low-cost sensors’ effectiveness, assessing methodology, 
lessons learned, key takeaways, and best practices 
for future studies with these instruments. A 
secondary objective is to evaluate the air quality 
impact of using low-cost sensors in an urban 
intervention (São Paulo’s Car-Free Friday).
AirBeam2, which measures PM 2.5, temperature, 
and relative humidity, was selected as the low-cost 
air quality instrument. The technology used by 
AirBeam2 makes it possible to transmit data in real 
time through the AirCasting platform. It can work in 
fixed or mobile modes. In the fixed mode, the sensors 
generate data every minute. In the mobile mode, 
AirBeam2 collects data every second, which generates 
a map of air pollution. Both fixed and mobile modes 
are used in this project. Car-Free Friday (CFF), an 
initiative that closes off streets in the historic center 
for all private cars and motorcycles on the last Friday 
of each month, was chosen as the scenario for the 
pilot project application with low-cost sensors.
Several logistical procedures were undertaken to 
ensure and control the quality of the measurement 
study. A total of 30 sensors were deployed for this 
project, with 21 used in the field study. Some of 
CONTEXT
Air pollution is the top environmental cause of 
disease in the world (Landrigan et al. 2018). This 
makes providing an air quality monitoring network 
increasingly important. While scientists have noted 
uncertainties associated with them, low-cost air quality 
sensors still provide valuable “policy-relevant and 
society-relevant information” (Gupta et al. 2018).
Currently, the air quality reference monitoring 
network in Brazil is poorly maintained. Acquisition,

wribrasil.org.br
4
the nonselected sensors were set aside because 
of operational difficulties and others due to lower 
correlation identified in the initial collocation.
METHODOLOGY AND RESULTS
The methodology of this project can be 
divided into three major components: 
 ▪ Collocation
 ▪ Fixed sensor study
 ▪ Mobile sensor study
Collocation is the process of comparing data collected 
from a sensor, whose performance is unknown or not 
well understood, with data collected by a reference 
instrument, whose performance is well established 
and trusted as a result of prior evaluation. Traditional 
monitoring stations can be used as reference 
instruments to evaluate the quality and accuracy of 
low-cost sensors. In São Paulo, monitoring stations 
are managed by the Environmental Company of the 
State of São Paulo (CETESB). In this study, one of 
CETESB’s reference-grade monitoring stations (in Dom 
Pedro II Park) was used to evaluate the performance 
of the low-cost air quality instruments deployed.
Data must be adjusted using regression equations 
generated from the collocation. During the study, a 
continuous collocation was performed with a sensor 
(called the golden sensor) located next to a reference 
monitoring station, as shown in Figure ES-1. The 
assessment with the monitoring station confirmed the 
reliability of the low-cost sensors, but it wasn’t used as 
an adjustment equation to relate other sensors to the 
reference instrument data. To guarantee the high quality 
of data collected and to adjust the measurements from 
the low-cost instruments, a collocation of all sensors 
was performed before and after the field measurements.
After the initial collocation, 13 sensors were deployed 
for a fixed sensor study (i.e., sensors were installed 
in a fixed location for measuring PM2.5 concentrations), 
11 outside public buildings in the central part of the 
city and 2 near the reference instrument. The 13 fixed 
sensors were divided between two zones (the Car-Free 
Zone [CFZ] and the Non-Car-Free Zone [NCFZ]) to 
Figure ES-1  |  Collocation Phases
Source: Authors.

PRACTICE NOTE   ▪  MEASURING PM 2.5  WITH LOW-COST SENSORS 
5
evaluate the impacts of the Car-Free Friday initiative. 
These sensors measured PM concentrations every day 
from September 28 to November 22, 2018 (September 
26 to November 23 considering collocations).
The hourly average PM2.5 concentration was calculated 
for each zone and a comparison was made between 
the measurements from the CFZ and the NCFZ. For 
each day, statistical tests were performed to check 
for percentage differences between zones, using 
the difference-in-differences method. Then paired 
t-tests were used to compare mean differences among 
days. Data from all Fridays measured during the 
study period (except holidays) were compared.
In addition to the fixed study, five sensors were 
deployed for a mobile sensor study (i.e., sensors 
connected to a smartphone). Study participants 
carried a mobile sensor and walked along different 
routes. Mobile PM2.5 measurements occurred on 
two Car-Free Fridays (September 28 and October 
26) and on three regular Fridays (October 5, October 
19, and November 9) at three different times (9 a.m. 
to 10 a.m., 12:3o p.m. to 1:30 p.m., and 4 p.m. to 5 
p.m.). The remaining sensors that were not used in 
both studies served as backup sensors for the study.
The collocation has shown that the measurements 
from the low-cost air quality sensors were well 
correlated with one another (R 2 > 0.94). When 
compared to the reference instrument, they also 
obtained a reasonable coefficient of determination 
(R2), with an R 2 for hourly means of approximately 
0.68, while for the daily means the R 2 was 
approximately 0.9. When combined with other 
information, the sensors demonstrated that they 
could give good indications of PM concentrations.
For the fixed sensor study, measurements have 
shown that, on all Fridays, the PM 2.5 concentration 
inside the CFZ was slightly higher than in the NCFZ. 
On Car-Free Fridays, the difference between the zones 
was smaller than on other Fridays. The results show 
a significant difference between Car-Free Fridays 
(CFFs) and Non-Car-Free Fridays (NCFFs) in all cases 
(each day compared to another), when eliminating 
outliers. These results suggest that the Car-Free Friday 
initiative may have an impact on PM2.5 concentration 
in that area. However, since the measurements were 
only taken on two Car-Free Fridays, more studies 
need to be done to statistically validate these results. 
For the mobile sensor study, data on five Fridays 
were collected, using five sensors on each of these days. 
This generated an abundance of data, which serves to 
verify the potential of data visualization insights for 
projects with low-cost sensors. Despite the limited 
number of days analyzed, having such visual analysis 
can show some interesting features (e.g., hotspots) 
worth further investigation and might help to better 
identify sources of pollution in different areas.
LESSONS LEARNED
This project demonstrates several lessons learned 
that are worth sharing for future deployments of 
low-cost sensors. Logistical issues and data analysis 
challenges when dealing with large numbers of 
sensors, the importance of collocation with a reference 
instrument to analyze the study’s accuracy, and the 
need to engage with city officials in implementing 
the project are some points highlighted.
INTRODUCTION
Air pollution is the world’s top environmental cause 
of disease. In 2015, diseases caused by pollution were 
responsible for an estimated 9 million premature 
deaths (Landrigan et al. 2018). According to the World 
Health Organization (WHO), more than 90 percent 
of the world’s population lives in areas with unsafe 
air quality levels, the majority of these people in 
developing countries (WHO 2016). This is a symptom 
of a larger development challenge, combined with a 
slow energy transition, a lack of political will, and 
governance structures that can be difficult to navigate. 
But awareness of the risks of air pollution is growing 
(WHO 2016), and the proliferation of low-cost sensors 
can help to increase it. While uncertainties have been 
raised by atmospheric scientists who question the 
performance, accuracy, and reliability of low-cost air 
quality sensors, these instruments still provide valuable

wribrasil.org.br
6
“policy-relevant and society-relevant information” 
(Gupta et al. 2018). In 2018, the World Meteorological 
Organization (WMO) released a comprehensive report 
recommending situations in which low-cost air quality 
instruments should be used. The WMO concluded that 
low-cost sensors are not yet a substitute for reference 
instruments but can be a useful complementary 
source of air quality information (WMO 2018). 
In its current state, the air quality reference monitoring 
network in Brazil is costly to properly operate and 
maintain. Management of air quality is a state-
level responsibility, but most Brazilian states do not 
have monitoring stations (ISS 2014; IEMA 2014). 
Due to the high up-front costs of acquisition, and 
of the maintenance and operation of conventional 
monitoring stations, most cities do not have sufficient 
geographic coverage of monitoring stations spread 
across their airshed (ISS 2014; IEMA 2014). With 
no reference network, it is difficult to apply special 
monitoring projects. While low-cost sensors are not 
yet accurate enough to replace reference-grade air 
quality instruments, they can be used to supplement 
the network in locations with fewer resources. 
These sensors provide an opportunity to conduct 
special monitoring studies. New low-cost sensors 
should be tested as a complementary technology to 
the traditional monitoring stations, with the aim 
of increasing cities’ monitoring and management 
capacity—in addition to increasing public awareness. 
The current use of low-cost sensors to measure air 
quality in cities is still experimental (Karagulian et 
al. 2019). Although low-cost sensors are not yet as 
accurate as traditional monitoring stations, they offer 
several advantages: they are portable, easier to use, 
and more can be deployed due to their lower cost. 
Gupta et al. (2018) used low-cost sensors and satellite 
observations to generate statistical models, obtaining 
reasonable “policy-relevant” results. Castell et al. 
(2017) found that low-cost sensors can be useful in 
providing socially relevant information on air quality. 
Many low-cost air quality sensors are available on 
the market. Besides measuring different pollutants, 
each model has unique functions and characteristics, 
and different performance in terms of accuracy 
and precision. Several factors were considered in 
selecting sensors: cost, pollutants measured, data 
communication methods, and vendor support. For 
this study particulate matter (PM) sensors were 
selected. Particulate matter includes small particles 
suspended in air, which those with a diameter of less 
than 10 micrometers can penetrate, enabling them 
to lodge inside the lungs. Particulate matter with a 
diameter of less than 2.5 micrometers (PM 2.5) is one 
of the most-studied pollutants and is associated with 
significant health risks (WHO 2016). Low-cost PM 2.5 
sensors have proved to be reasonably reliable and 
accurate (Magi et al. 2020; Feenstra et al. 2019). 
In parallel to the ground-up, citizen-science nature of 
low-cost air quality sensors, cities are implementing 
emission-reduction strategies to move from awareness 
to action. Many cities around the globe (Masiol et 
al. 2014) are taking actions to improve air quality 
and minimize the growing health impacts.
The objectives of this practice note are to evaluate 
low-cost sensors’ effectiveness, highlighting the 
methodology used, final lessons learned, key 
takeaways, and best practices for future studies using 
low-cost sensors, with the aim of helping cities be 
better prepared to do their own special projects. A 
secondary objective is to assess the air quality impact 
of using low-cost sensors in an urban intervention.
AirBeam2 was selected as the low-cost air quality 
instrument. AirBeam2 measures PM 2.5, temperature, 
and relative humidity. The AirBeam2 is an updated 
model of the original AirBeam, which at the time of 
this study had already been evaluated by a reputable 
institution and found to perform well (AQ-SPEC .2019). 
The instrument dimensions are given in Figure 1. 
Some of the key factors driving the selection were 
fixed and mobile modes of operation, multiple 
communication methods (Wi-Fi and cellular), ease of 
use, power from a battery or external power source, 
and an online platform for real-time viewing of data.
The technology used by AirBeam2 makes it possible 
to transmit data in real time through the AirCasting 
platform. It can work in fixed or mobile modes. In 
the fixed mode, the sensors generate data every 
minute. Figure 2 shows how to view data online. In

PRACTICE NOTE   ▪  MEASURING PM 2.5  WITH LOW-COST SENSORS 
7
Figure 1  |  AirBeam2 Dimensions
Source: Authors.
the mobile mode, the AirBeam2 must be connected 
to an Android smartphone via Bluetooth to properly 
geolocate and timestamp the measurements. In 
the mobile mode, AirBeam2 collects data every 
second, which generates a map of air pollution. Both 
fixed and mobile modes are used in this project.
In areas where traffic is shown to be one of the 
dominant sources of emissions (Karagulian et al. 2015), 
strategies such as low-emission zones (LEZs) and 
car rationing (e.g., even/odd license plate programs) 
are being implemented. In the case of São Paulo, one 
initiative undertaken by the city that began as a pilot 
but is now fully operational is the Car-Free Friday 
initiative. Car-Free Friday was chosen as the scenario 
for the pilot project application with low-cost sensors.
The Car-Free Friday initiative closes off streets in 
the historic center to all private cars and motorcycles 
on the last Friday of each month from 6 a.m. to 
6 p.m. Buses, taxis, bicycles, school buses and 
Figure 2  |  AirCasting Platform
Source: aircasting.habitatmap.org.

wribrasil.org.br
8
cars carrying the elderly or people with disability 
credentials may continue to circulate, as can 
drivers who are residents of the area. The streets 
highlighted in red in Figure 3 are those designated 
as “car-free” on the last Friday of each month.
Initially conceived as a pilot, São Paulo’s first Car-Free 
Friday took place on September 22, 2017, as a part of 
World Car-Free Day and Mobility Week. The popularity 
of the initiative with the public and the mayor led to its 
long-term institutionalization, and Car-Free Fridays 
have continued since September 2017. In October 2018, 
WRI surveyed more than 500 people about the Car-Free 
Friday initiative: 77 percent of respondents said they 
would like to increase the frequency of Car-Free Fridays 
and replicate the initiative in other areas of the city.
LOGISTICAL 
PROCEDURES
Several logistical procedures were undertaken to 
ensure and control the quality of the measurement 
study. The first step was to determine how many air 
quality sensors to use. Not having the right quantity 
of air quality instruments can make a measurement 
study much more challenging logistically. A total of 
30 sensors were deployed for this project, although 
not all of them were used in the field studies.
INITIAL CHECKING STEPS
Upon receiving new low-cost sensors, it was 
important to set up each one to make sure it 
worked, to confirm that no damage had occurred 
during shipping, and to draw up an inventory list 
to help management. The initial steps were to:
 ▪ create an inventory list;
 ▪ inspect each sensor for visible signs of damage;
 ▪ assign a code to and label each instrument;
 ▪ charge the battery for the time recommended by the 
manufacturer; and
 ▪ upgrade the firmware to its latest version.
Even these relatively simple steps can take a long 
time when several sensors are used. For example, 
a simple five-minute firmware update, applied to 
30 sensors, can take 2.5 hours to complete. As the 
number of sensors increases, such seemingly small 
tasks can lengthen a project’s schedule significantly.
LOGISTICS OF FIXED SENSOR SYSTEM
Siting any air quality measuring instrument can be 
challenging due to atmospheric conditions, local 
emissions, and logistical considerations, such as 
obtaining permission to access the site. For example, a 
smokestack or vent emissions could interfere with 
measurement of air quality conditions over a larger 
region like a neighborhood or city. Other factors like 
power and security can limit where sensors may be 
located. It takes time to find an appropriate site for any 
fixed sensor. 
Figure 3  |  Historic City Center of São Paulo and Car-Free Friday Roadways (Red)
Source: Authors.

PRACTICE NOTE   ▪  MEASURING PM 2.5  WITH LOW-COST SENSORS 
9
For this study, fixed sensors were installed on the 
exterior of windows of city government buildings. 
A partnership with the municipality helped with 
access. The installation of the physical sensors was 
quick (about one to two hours for each sensor), but 
getting access to the site took several weeks, requiring 
coordination with different actors and local visits to 
check whether and how the location could be used.
The low-cost air quality instruments were placed 
sufficiently far from nearby structures to prevent air 
flow restrictions. Sensors were placed in an outdoor 
location that assured air flow. The height chosen was 
between buildings’ second and third floors. Because 
they were at similar heights, the instruments could 
be better compared. This height proved suitable for 
locating all the sensors and more secure than on the 
ground floor, where they are more vulnerable to theft. 
Local emissions sources may affect the data collected at 
a site, so nearby sources that might bias the data were 
checked. All the sites chosen had guaranteed access and 
offered safety for personnel performing installation, 
routine visits, and maintenance. It was also important 
to make sure that power sources were available next 
to the windows where the sensors would be placed 
and that city employees knew not to turn them off. 
Figure.4 shows an example of fixed sensor installation.
The cellular network connection was sufficient and 
reliable in the region, avoiding the need to utilize a 
Wi-Fi connection. Communication systems in the area 
were tested before deploying the sensors.
After the sensors were turned on and configured, they 
were physically installed at their outdoor locations. 
Installers made sure the power cable was secure and 
would remain fixed in normal weather conditions, such 
as rain and wind. 
Once the sensors were installed, the network’s operation 
was monitored online to ensure that sensors were 
sending data correctly. In some instances, the sensors 
stopped sending data. Sometimes this could be fixed by 
restarting the instrument; in one instance the sensor 
had to be replaced.
LOGISTICS OF MOBILE SENSOR SYSTEM
When choosing mobile routes, it is important to 
ensure that the objective of the data collection is 
being satisfied. In this case, the objective was mostly 
to evaluate potential use for data visualization, and 
measurements inside and outside the area of study 
were taken. The choice of routes influenced the 
number of people required to walk with the sensors.
To ensure correct data collection with simultaneous 
mobile measurements at the same times and 
locations, participants who walked the routes were 
trained. Study participants were instructed to 
place the sensors at waist height. It was important 
to standardize how to use the sensors and how to 
name recording sessions, to teach participants how 
to connect sensors with cell phones, and to provide 
general tips (e.g., to avoid following people smoking). 
Figure 4  |  AirBeam Installed
Source: Seth Contreras/WRI.

wribrasil.org.br
10
DATA MANAGEMENT
Sites were named based on geographic landmarks that 
could be easily identified on a map. Their names included 
that of the building and the address. When there was 
more than one sensor on the same building, they faced 
different streets, so the street names were used.
The PM2.5 data collected from the low-cost sensors 
were sent automatically to the AirCasting.org website, 
where they could be plotted and displayed on a map in 
near real time. All data were stored on the AirCasting.
org server, and systematic downloads of data were 
done manually to maintain a backup database.
Traditional monitoring stations provide a reference for 
air quality concentrations and can be used to evaluate 
the quality and accuracy of low-cost sensors. In the São 
Paulo metropolitan area, 29 monitoring stations are 
managed by the Environmental Company of the State 
of São Paulo (CETESB), 17 of which perform PM2.5 
measurements (CETESB 2019). In this study, one of 
CETESB’s reference-grade monitoring stations (in Dom 
Pedro II Park) was used to evaluate the performance 
of the low-cost air quality instruments deployed.
Data from the CETESB reference instrument were 
necessary to address the study objectives of comparing 
the data from the low-cost instruments to the reference-
instrument measurements; reference data were 
available on the official CETESB website. Data delivered 
were processed on a periodic basis and backed up.
CONTINGENCY PLANNING: SENSOR 
BACKUP APPROACH
Some sensors may fail, sustain damage, or be stolen; 
therefore, backup sensors were available as 
replacements. Only one AirBeam2 was replaced during 
the two-month study, due to operational problems.    
Due to the project’s complexity, it was important to 
document this problem, to know which sensor had 
failed, where this sensor was located, and when it was 
replaced.
DATA QUALITY ASSURANCE PROCEDURES
Data validation is the process of determining the 
quality and validity of observations. Several procedures 
were needed to ensure that data were of sufficient 
quality for analysis. The quality assurance included 
developing a project plan (which guided the whole 
study), assessing sensors’ quality (the process of 
collocation is described in Section 3), monitoring 
data in real time, identifying problems and fixing 
them, and reviewing data for problems or outliers. 
During the study, the functioning of the sensors was 
checked constantly, both to verify that they were 
transmitting the data and to evaluate possible unreal 
measured data. When data do not flow normally 
for long periods, it is important to check the sensor 
where it was installed. At times, the sensors needed a 
reboot or, in one case, to be replaced with a backup.
METHODOLOGY
The methodology can be divided into three major 
components: collocation, fixed sensors, and mobile 
sensors. The study was designed and followed the 
guidance for air monitoring developed by the U.S. 
Environmental Protection Agency to ensure collection 
of high-quality data (U.S. EPA 2002). All measurements 
were made between September and November 2018. Box 
1 presents some general information about the study.
Box 1  |  Study Overview
Area: Historic city center of São Paulo
Pollutant: Particulate matter 2.5 (PM 2.5)
Measurements: Collocation, fixed sensor study, and 
mobile sensor study
Duration: September 26–November 23, 2018
Other data:  CETESB (Environmental Company of the State 
of São Paulo) monitoring station data
Outcomes sought:  Evaluation of low-cost sensors 
effectiveness

PRACTICE NOTE   ▪  MEASURING PM 2.5  WITH LOW-COST SENSORS 
11
COLLOCATION: PRE- AND 
POSTPROCESSING
A collocation is the process of comparing data collected 
from a sensor system with other sensor systems, or with 
data collected by a known reference instrument, for the 
purpose of evaluating their quality. Low-cost sensors 
in general cannot be directly calibrated, so the sensor 
data are adjusted using regression equations generated 
from the collocation studies. As shown in Figure 5, 
one initial (pre-data collection processing) and one 
final (post-data collection processing) collocation were 
done for all sensors. During the study, a continuous 
collocation was performed with a sensor (called the 
golden sensor) located next to a reference station. This 
golden sensor served as reference for other low-cost 
instruments, with their measurements being adjusted 
at the end of the study. The golden sensor was chosen 
among the instruments with best correlation with 
their peers in the pre-collocation. The reference station 
used was in Dom Pedro II Park, which has automatic 
measurement equipment using the beta radiation 
method. The monitoring station is operated by CETESB 
and is the closest to the area studied. This approach 
was important to compare how well sensors were 
measuring relative to each other and to the reference.
The collocation was conducted at the beginning and 
end of the study for at least 24 hours each time. The 
sensors were located as close as possible to each 
other to measure similar atmospheric conditions, yet 
with enough separation that they did not interfere 
with each other. To run this experiment, a secure 
and accessible two-square-meter area, with power 
connection available, was used for the 30 sensors.
For the collocations, Airbeam2’s communication 
methods of Wi-Fi and cellular were used to check 
both modes’ reliability. The tests showed that 
the communication method did not alter the 
concentration measurements or the amount of data.
After the initial collocation, 21 sensors were chosen 
for the Car-Free Friday study (18 for deployment 
and 3 as spares in case of theft or damage). Some 
of the nonselected sensors were set aside due to 
operational difficulties and others due to lower 
correlation identified in the initial collocation. 
Figure 5  |  Collocation Phases
Source: Authors.

wribrasil.org.br
12
Eleven sensors were installed on public buildings 
in the central part of the city. These sensors were 
used as fixed sensors. With the support of CETESB, 
another two sensors were installed near the Dom 
Pedro II Park air quality monitoring station (Figure .6) 
to provide continuous collocation with a reference 
instrument (one is the golden sensor, and the other is 
a backup in case of problems with the golden sensor). 
In total, 13 sensors were installed in the fixed mode.
In addition to the fixed sensors, five mobile sensors 
were used to measure PM2.5 on different routes. 
Study participants carried a sensor (Figure 7) and 
walked a specific route. Mobile measurements 
occurred on two Car-Free Fridays (September 
28 and October 26) and on three regular Fridays 
(October 5, October 19, and November 9).
The objective with collocations was to compare all 
sensor systems to ensure that an individual sensor 
system performed similarly to its peers. Initial and 
final collocations were used to determine how these 
Figure 6  |  AirBeams Installed at the Top of the Monitoring Station
Source: Virginia B. Tavares/WRI Brasil.
Figure 7  |  Study Participant Carrying a Sensor
Source: Virginia B. Tavares/WRI Brasil.

PRACTICE NOTE   ▪  MEASURING PM 2.5  WITH LOW-COST SENSORS 
13
sensors performed during the study period. If a sensor’s 
performance worsened compared to the others, this 
meant that there were problems with its operation 
that would require adjustments in the data collected. 
In this study, as there was no significant change 
between the sensors’ correlation in the initial and 
final collocations, a regular adjustment based on 
the golden sensor was applied to the results. This 
adjustment was the same during the entire study for 
each sensor. That made all sensors’ data internally 
consistent, which is necessary to compare data 
from different locations and times of the day.
For this specific intervention, the objective was 
to verify the difference between the areas, not to 
measure the absolute concentration itself. For that 
reason, the assessment with the monitoring station 
served to confirm the low-cost sensors’ reliability, but 
it wasn’t used as an adjustment2 equation to relate 
other sensors to the reference instrument data.
Linear regression equations were used to adjust 
the data. Measurement standardization allowed 
comparison of results with the golden sensor. Equation 
1 presents the format of the generated equations.
Sensor (calibrated) = Slope * Sensor value + Intercept (1)
Figures 8, 9, and 10 exemplify the data adjustment 
process using the golden sensor (not using real data 
collected in the project). The process begins with 
the development of a scatter plot that compares the 
pollutant concentrations measured by the golden 
sensor with the concentrations detected by each sensor, 
generating the equations for adjustment (Figure 8). 
From this equation, the data are adjusted. Figure 9 
shows an example of measurements before adjustment. 
Figure 10 illustrates data after measurement 
adequacy was checked by the regression equation.
Figure 8  |  Example of Scatter Plot to Generate 
Adjustment Equations
Source: Authors.
Figure 9  |  Example of Measurement Data Before 
Adjustment
Figure 10  |  Example of Measurement Data After 
Adjustment
Source: Authors.
Source: Authors.

wribrasil.org.br
14
Figure 11  |  Location of Fixed Sensors in São Paulo City Center
Source: Authors.
FIXED SENSOR SYSTEM STUDY
The locations of fixed sensors were chosen such that 
some sensors would be near the area with closed streets 
and some outside this area, where the impacts were not 
expected to be so direct. To verify differences in local 
PM2.5 concentrations, the sensors were divided into two 
distinct zones. The zone where the initiative takes place 
was called the Car-Free Zone (CFZ). Eight fixed sensors 
were located in the CFZ and appear in blue in Figure 11.
Sensors outside this area were placed in the comparison 
group, called the Non-Car-Free Zone (NCFZ). Five 
fixed sensors were installed in the NCFZ, including 
equipment located near the CETESB monitoring 
station, and appear in yellow in Figure 11.
Comparisons between zones were made during the 
same periods of time. Since different days do not 
have the same weather conditions, direct comparison 
of their PM concentration levels can lead to false 
conclusions. For example, a Friday not part of the 
initiative may have lower PM2.5 concentrations than a 
Car-Free Friday, but that does not mean that closing 
roads to cars increases pollution levels, since several 
external factors affect the pollutant concentration. 
In order to analyze both the reliability of the sensors 
and the PM concentrations in the study area, it was 
necessary to verify whether the amount of data was 
sufficient to draw conclusions about the validity of 
the averages used. Data may be lacking due to system 
problems that lead to measurements being taken at 
a slower rate than normal, or operational problems 
such as power outages. When sensors did not have 
enough data on a given analyzed Friday, these data 
were excluded from the analysis. Apart from that, 
for all sensors, outlier data were eliminated based on 
cutoffs generated by adjusting statistical distributions, 
using inverse cumulative probability for 0.99865.
All sensors in the same zone were considered as a 
network of sensors, gathering all their hourly data 
and then using an hourly average per zone. The 
averages of PM2.5 concentration were calculated 
by zone (CFZ and NCFZ), and then the zones were 
Car-Free Zone          Non-Car-Free Zone

PRACTICE NOTE   ▪  MEASURING PM 2.5  WITH LOW-COST SENSORS 
15
compared for each hour of the day. For each day, 
the percentage differences between zones were 
calculated, using the difference-in-differences method. 
Then statistical tests were performed to check the 
differences between each day and others. Data from 
all Fridays measured during the study period, except 
holidays, were compared, producing data for two 
Car-Free Fridays and three Non-Car-Free Fridays.
MOBILE SENSOR SYSTEM STUDY
Mobile sensors can be a useful way to collect data at 
many different locations. The AirBeam2 was paired 
with a mobile phone to get a GPS signal. For this mode 
of sampling, the sensor records one-second data, 
capturing the time and location of the measurements. 
Using mobile mode, an enormous quantity of data 
distributed on the city center’s streets was collected. The 
main goal with mobile data was to verify the potential 
of data visualization for on-the-ground interventions.
Five routes were designed to collect mobile 
measurements in both Car-Free and Non-Car-Free 
Zones. Each study participant would walk their 
route three hours per day: in the morning (between 
9 a.m. and 10 a.m.), in early afternoon (between 
12:30 p.m. and 1:30 p.m.), and in late afternoon 
(between 4 p.m. and 5 p.m.). The same routes 
were taken on two Car-Free Fridays (September 
28 and October 26) and on three regular Fridays 
(October 5, October 19, and November 9).
RESULTS
COLLOCATION
The first validation step of the project’s results was to 
verify the sensors’ reliability. This verification was 
essential to ensure that the analysis carried out would 
be valid and credible.
Correlation analysis showed that all sensors compared 
to the reference (or “golden”) sensor using hourly 
averages were well correlated (R² equal to or greater 
than 0.94). Sensor performance in pre- and               
post-collocation studies were similar, meaning that no 
further adjustments were needed to adapt the results 
presented.
The two sensors that were placed near the CETESB 
monitoring station in Dom Pedro II Park showed 
reasonably consistent results when compared to 
the reference instrument. Initially the sensors 
named AB1 and AB29 (golden sensor) were 
placed near the station. During the first week AB1 
stopped working. It was replaced with AB2 and 
no longer used in the study. AB29 was installed 
on September 27, while AB2 began operating on 
October 4. Both were removed on November 23.
The sensors ultimately showed a reasonable correlation 
with the reference instrument. For the hourly means 
the R² was approximately 0.68, while for the daily 
means the R² was approximately 0.9, as shown in 
Figures 12 and 13. These values demonstrate that the 
measurements performed by the sensors were reliable.

wribrasil.org.br
16
Figure 13  |  Scatter Plot of Average Daily Concentrations
Source: Authors.
Figure 12  |  Scatter Plot of Average Hourly Concentrations
Source: Authors.

PRACTICE NOTE   ▪  MEASURING PM 2.5  WITH LOW-COST SENSORS 
17
FIXED SENSOR SYSTEM
For the fixed sensor study, three sensors were 
eliminated due to technical problems. Two of these 
were the sensors located at the CETESB monitoring 
station: one had to be replaced since it stopped working 
(for unknown reasons) in the first days of the study; 
the other didn’t have enough daily data on one of the 
Fridays. The third one was located in the Car-Free 
Zone and also was discarded due to lack of data. Other 
sensors also had problems collecting data, such as 
reporting data less frequently or power outages and 
consequent complete loss of battery power, but that 
didn’t invalidate the averages obtained for those days.
In total, of the eight fixed sensors placed in the CFZ, 
seven were used for the data analysis. For the NCFZ, 
four of five sensors were used, including the golden 
sensor located next to the CETESB reference  
monitoring station. 
Measurements have shown that, on all Fridays, the 
PM2.5 concentration in the CFZ was slightly higher 
than in the NCFZ. The analysis was conducted from 
6 a.m. to 5:59 p.m., to match the times of the car-free 
initiative. Paired t-tests were used to compare mean 
differences between days. On Car-Free Fridays, the 
difference between the zones was smaller than on 
other Fridays. The results show a significant difference 
between Car-Free Fridays (CFFs) and Non-Car-Free 
Fridays (NCFFs) in all cases (each day compared to 
another), when eliminating outliers. This result suggests 
that the Car-Free Friday initiative might reduce PM 2.5 
concentration in that area. However, as measurements 
were taken on only two Car-Free Fridays, more studies 
are needed to statistically validate these results. Figure 
14 shows the percentage difference between the zones 
on each day, calculated as (CFZ or NCFZ)/CFZ. 
MOBILE SENSOR SYSTEM
For the mobile sensor study, data on five Fridays 
(two CFFs and three NCFFs) were collected, using 
five sensors on each of these days. Five participants 
walked routes in both Car-Free Zones and Non-
Car-Free Zones. This generated an abundance 
of data, demonstrating the potential of data 
visualization insights for this type of project.
Figure 15 shows raw data generated by sensors, 
before cleaning procedures, while Figure 16 shows 
daily averages organized per street segment, 
for a CFF and an NCFF, respectively. The scale 
was constructed using minimum and maximum 
concentration averages for the day. Color scaling helps 
to identify differences within and between regions 
and segments. Despite the limited number of days 
analyzed, having such visual analysis shows some 
interesting features worth deeper investigation:
 ▪ Relatively higher PM2.5 conditions outside the 
Car-Free Zone (left dots) on Car-Free Fridays may 
indicate more pollution from another source (per-
haps more traffic congestion). Detailed traffic counts 
could help confirm this observation.
 ▪ Persistently higher PM2.5 concentrations at a fixed 
spot occurred on all days and may indicate a very 
local “hot spot,” which could be investigated by 
looking for local sources of PM2.5 in that area.
This type of data visualization enables us to better 
identify sources of pollution in different areas.
Source: Authors.
Figure 14  |  Percentage Difference between Zones  
for Fixed Sensors

wribrasil.org.br
18
Source: Authors.
Source: Authors.
Figure 15  |  Mobile Data Generated in One CFF
Figure 16  |  Average Daily Concentrations per Street Segment

PRACTICE NOTE   ▪  MEASURING PM 2.5  WITH LOW-COST SENSORS 
19
LESSONS 
LEARNED
This project has produced several lessons learned that 
are worth sharing for future deployments of low-cost 
sensors:
 ▪ Pollutant analyzed for the type of urban 
intervention chosen: Other pollutants emitted 
more directly by vehicles impacted by CFF, such as 
CO or NOx, might have shown a greater impact on 
pollutant concentrations. In Brazil, it is more com-
mon for trucks and buses to use diesel, which emits 
more PM2.5. Cars and motorcycles (vehicles that 
have more traffic restrictions on CFFs) generally use 
other types of fuel that emit more of other pollut-
ants. These factors are important to analyze while 
planning the scope of project.
 ▪ Atmospheric conditions: It is important to 
consider expected weather patterns when planning 
such a study. For example, winter versus summer 
seasons, or windy conditions and months when 
heavy rainfall is common. Those changes might 
affect the evaluation of a given initiative, generating 
different results.
 ▪ Logistical issues: This study started with 30 
devices, which generated a large amount of data. It 
was important to maintain a good management and 
logging system to keep track of them and keep ev-
erything labeled and documented. Small procedures 
that require little effort for one or two devices can 
take much longer when many sensors are involved. 
Also, preparing a site to install a low-cost sensor took 
several weeks, so it was important to plan according-
ly and budget enough time in the project schedule.
 ▪ Data analysis: This short-term study produced 
a wealth of data with one-minute fixed values and 
one-second mobile values. Extracting and process-
ing this information required identifying software to 
extract the data from the air sensor web database, 
creating rules on how to average data to ensure 
completeness and representativeness, and perform-
ing statistical analysis for the assessment.
 ▪ Collocation with the reference instrument: 
Comparison of the sensor data with the CETESB 
monitoring station was very important to verify the 
instruments’ accuracy. The sensors were installed at 
the station for about two months, collecting enough 
data to enable a strong statistical analysis to eval-
uate them. It is especially important to collocate 
the sensors with a reliable reference instrument to 
analyze the study’s accuracy.
 ▪ Awareness building: By engaging with officials at 
city government, fixed sensors could be installed in 
government buildings for an extended period, and 
have access to power outlets. Moreover, government 
employees were genuinely interested in learning 
more about the sensors—how they worked, what they 
measured, and why the study was being conducted. 
This form of awareness-building can prove very valu-
able for moving the needle from awareness to action, 
and also reinforce for city agents the importance and 
the value of programs like Car-Free Friday.
CONCLUSIONS
The study generated valuable lessons learned that 
might help cities to design and better prepare studies 
using low-cost sensors. The low-cost instruments 
have shown a good correlation among them. When 
compared to a reference instrument, such as the 
CETESB monitoring station, the Airbeam2 instrument 
compared well and consistently with other studies. 
When combined with other information, the sensors 
can give good indications of PM concentrations. 
Sometimes the sensors collected incomplete data, 
which can present a challenge to more robust use, 
but they are a useful complement to traditional 
monitoring station networks. Because these devices 
are a new technology, we recommend more studies to 
validate low-cost sensors’ application and reliability.

wribrasil.org.br
20
The use of low-cost sensors could help to build public 
awareness and catalyze smarter cities. As their 
technology improves, more studies are conducted, 
and lessons learned are shared, the application of 
low-cost sensors could move, in the near future, 
from piloting to standard operations. Sustainable 
mobility initiatives, like Sao Paulo’s Car-Free 
Friday, could benefit from such a data evolution.
The deployment of low-cost sensors to analyze 
Car-Free Friday indicates that the initiative might 
have impacts on local PM concentration, despite its 
restricted geographic area. In the fixed sensor study, 
considering only the Fridays measured during the 
study, a significant statistical difference between the 
PM2.5 concentrations on Car-Free Fridays compared to 
Non-Car-Free Fridays was observed. However, due to 
small sampling (five days) it cannot be concluded that 
the initiative has effective impact on PM concentrations. 
The use of mobile data also demonstrated good 
potential for further analysis, helping to localize 
places that have higher PM concentrations.
Future studies to evaluate the intervention should use 
a greater sample of days to be able to offer statistical 
conclusions about the impacts of the initiative. Traffic 
behavior in São Paulo could also be analyzed to see 
if Friday patterns are similar to other weekdays, 
so more days can be used for this analysis. Finally, 
this specific initiative could be evaluated with other 
types of pollutants, since its effect on particulate 
matter must be lower considering that cars and 
motorcycles usually use gasoline in Brazil.
ENDNOTES
1. Sensors are not stand-alone devices (in order to measure, they must 
be incorporated into an instrument), and, depending on how an 
instrument is designed, the sensor may perform well or poorly. We 
use the terms low-cost air quality sensors and low-cost air quality 
instruments as synonyms, however, since the first is most used in the 
literature.
2. The adjustment is used as a calibration, but instead of calibrating the 
sensors before study, their measurements were adjusted afterward.

PRACTICE NOTE   ▪  MEASURING PM 2.5  WITH LOW-COST SENSORS 
21
AQ-SPEC (Air Quality Sensor Performance Evaluation Center). 2019. 
“AirBeam Evaluation Summary.” http://www.aqmd.gov/docs/default-
source/aq-spec/summary/pdf.pdf?sfvrsn=16. Accessed September 25.
Castell, N., F.R. Dauge, P . Schneider, M. Vogt, U. Lerner, B. Fishbain, D. Broday, 
and A. Bartonova. 2017. “Can Commercial Low-Cost Sensor Platforms 
Contribute to Air Quality Monitoring and Exposure Estimates?” Environment 
International 99 (February): 293–302.
CETESB (Companhia ambiental do Estado de São Paulo). 2020. Qualidade 
do ar no Estado de São Paulo 2019. São Paulo: CETESB.
Feenstra, B., V. Papapostolou, S. Hasheminassab, H. Zhang, H., B. 
Boghossian, D. Cocker, and A. Polidori. 2019. “Performance Evaluation 
of Twelve Low-Cost PM 2.5 Sensors at an Ambient Air Monitoring Site.” 
Atmospheric Environment 216 (November).
Gupta, P ., P . Doraiswamy, R. Levy, O. Pikelnaya, J. Maibach, B. Feenstra, 
A. Polidori, et al. 2018. “Impact of California Fires on Local and Regional 
Air Quality: The Role of a Low-Cost Sensor Network and Satellite 
Observations.” GeoHealth 2 (June): 172–81.
IEMA (Instituto Energia e Meio Ambiente). 2014. 1º Diagnóstico de rede de 
monitoramento da qualidade do ar no Brasil. São Paulo: IEMA.
ISS (Instituto Saúde e Sustentabilidade). 2014. Monitoramento da qualidade 
do ar no Brasil. São Paulo: ISS.
Karagulian, F., C.A. Belis, C.F.C. Dora, A.M. Prüss-Ustün, S. Bonjour, H. Adair-
Rohani, and M. Amann. 2015. “Contributions to Cities’ Ambient Particulate 
Matter (PM): A Systematic Review of Local Source Contributions at Global 
Level.” Atmospheric Environment 120 (November): 475–83.
Karagulian, F., M. Barbiere, A. Kotsev, L. Spinelle, M. Gerboles, F. Lagler, N. 
Redon, S. Crunaire, and A. Borowiak. 2019. “Review of the Performance of 
Low-Cost Sensors for Air Quality Monitoring.” Atmosphere  10 (August).
Landrigan, P .J., R. Fuller, N.J.R. Acosta, O. Adeyie, R. Arnold, 
N. Basu, A.B. Baldé, et al. 2018. “The Lancet Commission on 
Pollution and Health.” Lancet 391 (February): 462–512.
Magi, B. I., C. Cupini, J. Francis, M. Green, and C. Hauser. 2020. 
“Evaluation of PM2.5 Measured in an Urban Setting Using a Low-
Cost Optical Particle Counter and a Federal Equivalent Method 
Beta Attenuation Monitor.” Aerosol Science and Technology 54 
(May): 147–59.
Masiol, M., C. Agostinelli, G. Formenton, E. Tarabotti, and B. 
Pavoni. 2014. “Thirteen Years of Air Pollution Hourly Monitoring 
in a Large City: Potential Sources, Trends, Cycles and Effects 
of Car-Free Days.” Science of the Total Environment 494–95 
(October): 84–96.
U.S. EPA (United States Environmental Protection Agency). 2002. 
Guidance for Quality Assurance Project Plans. Washington, DC: 
U.S. EPA.
WHO (World Health Organization). 2016. Ambient Air Pollution: A 
Global Assessment of Exposure and Burden of Disease.  Geneva: 
WHO.
WMO (World Meteorological Organization). 2018. Low-Cost 
Sensors for the Measurement of Atmospheric Composition: 
Overview of Topic and Future Applications. Geneva: WMO.
REFERENCES

wribrasil.org.br
22
ACKNOWLEDGMENTS
WRI Brasil developed this practice note with the financial support of the 
Children’s Investment Fund Foundation (CIFF).
We express our gratitude to the Municipality of São Paulo for making the 
pilot’s execution feasible, largely in the form of support provided through 
the Mobility and Transport Secretariat. We also thank CETESB for allowing 
us to install the sensors at its monitoring station.
Our acknowledgments of those who contributed directly or indirectly to the 
implementation of this project: Luis Antônio Lindau, Eduardo Siqueira, Luiza 
de Oliveira Schmidt, Talita Esturba, Diogo Lemos, Francisco Pasqual, Joana 
Oliveira, Luisa Peixoto Guimarães, and Carolina Cominotti.
Thanks also to the internal and external reviewers: Marcelo Alonso, Beatriz 
Cardenas, Carolina Cominotti, Talita Esturba, Thiago Guimarães, Michael 
Heimbinder, Robin King, Tania Lopez, Ajay Singh Nagpure, Jessica Seddon, 
Su Song, and Rita Ynoue.
ABOUT WRI BRASIL
WRI Brasil is a research institute that transforms big ideas into actions 
to protect the environment and foster Brazil’s prosperity in an inclusive 
and sustainable fashion. It is focused on research and applications of 
sustainable solutions oriented towards climate, forests, and cities. WRI 
Brasil combines technical excellence with political articulation and works 
in close collaboration with governments, private companies, universities 
and civil society.
WRI Brasil is part of World Resources Institute (WRI), a global research 
organization whose work extends to over 50 countries. WRI encompasses 
the work of almost 1200 professionals in offices in Brazil, China, the United 
States, Mexico, India, Indonesia, Europe, Turkey and Africa.
ABOUT THE AUTHORS
Cristina Albuquerque  is the Urban Mobility Manager at WRI Brasil. 
Contact: cristina.albuquerque@wri.org
Matheus Bello Jotz  is a former Urban Mobility Analyst at WRI Brasil. 
Contact: matheusbellojotz@gmail.com
Virginia Bergamaschi Tavares is an Urban Mobility Analyst at WRI Brasil.  
Contact: virginia.tavares@wri.org
Seth Contreras is a former Air Quality Associate at WRI. 
Contact: seth.d.contreras@gmail.com
Tim Dye is a Low-Cost Sensors Specialist at TD Environmental Services LLC.  
Contact: tim@tdenviro.com
Audrei Marcelo is a Statistician at Siqueira Campos Associados. 
Contact: audrei@siqueiracampos.com
Marco Siqueira Campos  is a Statistician at Siqueira Campos Associados. 
Contact: marco@siqueiracampos.com
ABOUT CIFF
The Children’s Investment Fund Foundation (CIFF) is an independent 
philanthropic organization with offices in Addis Ababa, Beijing, London, 
Nairobi, and New Delhi. Established in 2002, CIFF works with a wide range 
of partners seeking to transform the lives of children and adolescents in 
developing countries. Areas of work include adolescent sexual health, ma -
ternal and child health, opportunities for girls and young women, tackling 
child slavery and exploitation, and supporting smart ways to slow down 
and stop climate change.

Maps are for illustrative purposes and do not imply the expression of any opinion on the part of WRI, concerning the legal status of any country or 
territory or concerning the delimitation of frontiers or boundaries.
Each World Resources Institute report represents a timely, scholarly treatment of a subject of public concern. WRI takes responsibility for choosing 
the study topics and guaranteeing its authors and researchers freedom of inquiry. It also solicits and responds to the guidance of advisory panels and 
expert reviewers. Unless otherwise stated, however, all the interpretation and findings set forth in WRI publications are those of the authors.
Copyright 2021 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License.  
To view a copy of the license, visit http://creativecommons.org/licenses/by/4.0/

SÃO PAULO
R. CLÁUDIO SOARES, 72 CJ. 1510
PINHEIROS, SÃO PAULO - SP
05422-030, BRASIL
+55 11 3032-1120
PORTO ALEGRE
AV. INDEPENDÊNCIA, 1299 CJ. 401
PORTO ALEGRE - RS
90035-077, BRASIL
+55 51 3312 6324
WRIBRASIL.ORG.BR
doi.org/10.46830/wripn.19.00035
