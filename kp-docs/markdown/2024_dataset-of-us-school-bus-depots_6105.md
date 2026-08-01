---
doc_id: 2024_dataset-of-us-school-bus-depots_6105
source_pdf: kp-docs/askwri-kps/2024_dataset-of-us-school-bus-depots_6105.pdf
extraction_method: cache-plaintext
char_count: 77492
title: Dataset of U.S. School Bus Depots
authors: Shao, Yang; Lazer, Leah; Taff, Gregory
date_published: 4/1/2024
article_type: Technical Note
sub_tag: Transport decarbonization
wri_primary_office: WRI US
wri_programs: Cities
language: English
url: "https://www.wri.org/research/dataset-us-school-bus-depots"
doi: "https://doi.org/10.46830/writn.22.00019"
summary: A novel dataset of 11,309 school bus depots across the contiguous U.S. was created using high-resolution aerial imagery from the National Agriculture Imagery Program, employing an object-based approach to detect clusters of school buses. The dataset reveals that over half of these depots are located within 350 meters of schools, highlighting potential air pollution hotspots. Accuracy assessments showed a 15.2% omission error rate compared to reference datasets, indicating reliable data quality. This dataset is crucial for analyzing environmental justice issues, guiding electrification efforts, and informing utility planning for future electricity demands from electric school buses.
---

# Dataset of U.S. School Bus Depots

TECHNICAL NOTE   |  Version 1.0  |  Month Year  |  1
CONTENTS
Abstract. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
Introduction and motivation. . . . . . . . . . . . . . .2
Methods and data ........................ 4
Results and discussion ................... 11
Challenges and limitations ............... 19
Conclusion ............................... 21
Endnote. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
References .............................. 23
Additional Sources Consulted. . . . . . . . . . . 25
Acknowledgments ...................... 26
About the authors. . . . . . . . . . . . . . . . . . . . . . . 26
Credit author statement. . . . . . . . . . . . . . . . . 26
About WRI .............................. 26
Technical notes document the research or analytical 
methodology underpinning a publication, interactive 
application, or tool.
Suggested Citation: Shao, Y., L. Lazer, and G. 
Taff. 2023. “Dataset of U.S. school bus depots.” 
Technical Note. Washington, DC: World Resources 
Institute. Available online at: doi.org/10.46830/
writn.22.00019.
TECHNICAL NOTE
Dataset of U.S. school bus depots
Authors: Yang Shao, Leah Lazer, and Gregory Taff
ABSTRACT
This technical note describes the methods used to create a first-of-its-kind 
dataset of school bus depot locations in the United States. There are nearly 
half a million school buses in the country, but almost no public information 
about where they are kept, even though school bus depots may create air 
pollution hotspots and may require grid infrastructure upgrades for future bus 
electrification.
We created this dataset using an object-based approach with remote sensing 
data. Our primary source of aerial imagery was the National Agriculture Imag-
ery Program (NAIP) dataset. We analyzed NAIP imagery to locate individual 
school buses based on their color and size, and then classified clusters of 
school buses as potential depots, which we then verified visually. The result-
ing dataset contains 11,309 depots across the 48 contiguous U.S. states and 
Washington, DC. Fifty-one percent (5,730 depots) are at schools, defined as 
being 350 meters or less from the nearest school.
We assessed the accuracy of the dataset by comparing it with independent 
reference datasets containing 506 depots, from the records of two school 
transportation companies. We found good agreement, with an omission error 
rate of 15.2 percent (77 depots). This dataset represents one of the only remote 
sensing projects to conduct object detection using sub-meter to one-meter 
resolution data for a continental-scale application.

2  |  
  
INTRODUCTION AND 
MOTIVATION
For nearly a century, the iconic yellow school bus has played a 
transformational role in making education accessible for millions 
of children who have no other way to get to school. With about 
half a million school buses nationwide driving a total of 2.71 
billion miles per year (SBFM 2023), school buses are among the 
most ubiquitous and visible vehicles in the United States, trans-
porting students in every state and every type of community. In 
2019–20, more than 20 million students rode the bus to school 
each day, out of a total of approximately 53.9 million students in 
kindergarten through 12th grade nationwide (NCES 2022a). 
More than 90 percent of the school buses today are diesel 
powered (APP n.d.). Diesel exhaust pollution has proven links 
to serious physical health issues and can lead to asthma, cancer, 
and other respiratory illnesses, as well as cognitive development 
impacts for children (Austin et al. 2019; Beatty and Shimshack 
2011). Communities that have been historically disadvantaged 
are more likely to suffer from vehicle-based air pollution due 
to racist lending, transit, housing, and zoning policies that have 
concentrated Black and Brown communities closer to highways 
and other pollution sources (ITDP 2021).  Due in part to their 
associated health and climate benefits, there has been a grow-
ing demand for the electrification of school buses (Lazer and 
Freehafer 2023) as well as a large increase in public funding for 
electric school buses (Levinson and Achury 2023). While the 
number of school buses in the United States is small compared 
with the total number of medium- and heavy-duty vehicles, 
electrifying school buses can make electrification more visible 
and offer learning opportunities for community members. 
Based on consultations with staff in the Electric School Bus Ini-
tiative at World Resources Institute (WRI), we learned that two 
groups are particularly exposed to exhaust from school buses. 
The first is the people on the buses, including students, driv-
ers, and aides. A growing body of literature explores how diesel 
exhaust from school buses impacts these people. The second 
group is people living near school bus depots since buses often 
run at depots for relatively long periods and frequently drive in 
and out of them. As of May 2023, we were not able to find any 
nationwide (or even state-level) dataset or map of school bus 
depot locations or any research exploring the characteristics of 
communities living near school bus depots or how those depots 
impact the surrounding communities. Such information may be 
accessible at the local-government or school-district level but 
has not been compiled in a centralized manner. People living 
along school bus routes are less exposed to pollution from school 
buses because there are relatively few school buses in the overall 
vehicle fleet and most school buses drive their routes only a 
couple times per day. Therefore, the primary objective of this 
research was to map the locations of school bus depots using 
high-resolution remote sensing data, creating a first-of-its-
kind dataset that pinpoints depots across the United States.
Moreover, despite the lack of data related specifically to school 
bus depots, a large body of environmental justice and public 
heath literature describes how undesirable or dangerous facili-
ties such as truck depots and polluting industrial plants are 
disproportionately located in or near communities of color, low-
income communities, or populations that have been otherwise 
marginalized or underserved, leading to health harms (Brown 
et al. 2003; Cook et al. 2021; Linden 2008). Research also 
describes the high levels of traffic-related air and noise pollution 
near many schools, which are often inequitably distributed and 
linked to health harm (Brunekreef et al. 1997; Li et al. 2009; 
Chakraborty and Aun 2023). 
Therefore, a primary use case for this dataset is to analyze the 
extent to which school bus depots are located in underserved 
areas, and create an evidence base that would better enable the 
work of community members, advocates, and other stakehold-
ers toward improving air quality, equity, and public health in 
underserved areas (Hsu et al. 2021). 
Other possible uses for this school bus depot dataset include 
electricity grid planning and resilience. The specific locations of 
school bus depots can assist utility companies in assessing future 
electricity demand from electric school buses, and help them 
plan for new charging stations (Huether 2021). It could also be 
useful to identify school bus depots that are at risk from climate 
and other hazards and may not be strong candidates for large 
investments in electric infrastructure, and conversely to identify 
depots that could serve as resilience hubs, making use of the 
electricity that can be stored and moved in electric school bus 
batteries or fed back into the grid.

TECHNICAL NOTE   |  Month Year  |  3
Dataset of U.S. school bus depots
Box 1  |  Definition of school bus depot
School bus depots (also called school bus yards, barns, garages, or 
lots) are typically parking lots that accommodate multiple buses. They 
can be owned and operated by a school, school district, or private 
fleet operator, and can be located on the grounds of a school or at a 
separate location. Some depots also provide facilities for maintenance. 
They serve as a workplace for fleet managers, drivers, and other staff. 
The locations of these school bus depots are crucial for bus route 
planning, which involves meeting various constraints such as travel 
time, school schedules, and bus capacity. a 
To create this dataset, we developed a working definition of what 
spatial arrangement of school buses constitutes a school bus depot, 
establishing the following four criteria that must be met to be con -
sidered one: 
1. Four buses within a moving window size of 80 meters (m) by 80 m 
are considered a school bus depot. 
2. If one facility contains multiple parking areas or clusters of buses, 
it is still considered one depot (see Figure B1-1).
3. Similarly, if buses are parked in two lots that are adjacent or 
directly across the street from each other, it is still considered one 
depot (see Figure B1-2).
4. If a facility contains four or more school buses but does not 
belong to an entity that provides school transportation services, 
it is not a school bus depot. This criterion led to the removal of 
auto repair shops, scrapyards, farms, and ski resorts, among other 
locations.
We used criterion 1 during the object detection and clustering phases 
(Steps 1–3 in the “Detailed methods” section), while we applied criteria 
2–4 during the visual interpretation process (Step 4 in the “Detailed 
methods” section). We based criteria 2 and 3 on the assumption that 
these nearby parking areas are likely owned or managed by the same 
school district or fleet operator, and that the intended use cases of the 
dataset would be better supported by considering them depots, since 
they would be considered one entity for use cases like electricity grid 
upgrades for vehicle electrification. While it is not possible to apply 
this operational definition with complete accuracy based on a visual 
inspection of aerial images, we drew on our knowledge of school 
transportation and land use patterns to decide and corroborated with 
street view or business information from Google Maps as needed.
FIGURE B1-1. EXAMPLE OF A SCHOOL PARKING LOT WITH TWO 
AREAS OF SCHOOL BUS PARKING (PURPLE DOTS), CONSIDERED 
ONE SCHOOL BUS DEPOT
Source: Esri 2023.  
FIGURE B1-2. EXAMPLE OF A SCHOOL BUS DEPOT WITH TWO 
PARKING AREAS DIRECTLY ACROSS THE STREET FROM EACH OTHER 
(PURPLE DOTS), CONSIDERED ONE SCHOOL BUS DEPOT
Source: Esri 2023.

4  |  
  
METHODS AND DATA
Other methods considered
Before arriving at the remote sensing methods described 
below, we first explored several alternatives. We initially tried 
to compile data from state agencies, such as state departments 
of education or transportation, which maintain inventories of 
school buses in many states. This approach was successful for 
compiling the Dataset of U.S. School Bus Fleets (Lazer et al. 
2023), but no state agencies that we contacted held information 
on school bus depots. We also considered gathering informa-
tion from school districts because they have information on the 
location of the depots that serve the district. However, there are 
over 13,000 school districts in the United States (in addition 
to hundreds or thousands of private fleet operators) and they 
do not have any standardized data request process or format of 
information on depot locations. It was not feasible to collect 
data from nearly 14,000 districts and operators individually. 
Another initial attempt involved web information retrieval. 
We tried using a web crawler (an internet bot that system-
atically browses the internet and gathers information about 
webpages) to extract school bus depot locations from school 
district websites, based on the National Center for Education 
Statistics (NCES) Common Core of Data, which includes the 
website URLs for many school districts (NCES 2020). How-
ever, due to the inconsistent formatting and labeling of school 
districts’ websites and any bus depot information, in addition 
to the infrequency with which they published this informa-
Box 1  |  Definition of school bus depot (Continued)
While most school bus depots are open-air parking lots, some have 
covered areas or fully enclosed structures (“enclosed depots”) (see 
Figure B1-3). These are also considered depots for the purposes 
of this dataset. Enclosed depots are most common in places with 
extreme temperatures or weather or in dense urban areas. Some 
enclosed depots were detected using our methods because they also 
had school buses parked outdoors, like in Figure B1-3, but we think 
most of the depots we missed are enclosed. See the “ Challenges and 
limitations” section for further discussion of potential omission errors.  
FIGURE B1-3. EXAMPLE OF AN ENCLOSED SCHOOL BUS DEPOT
Note: a. Park and Kim 2010.
Source: Esri 2023.
tion, this approach was not successful. Open-source maps like 
OpenStreetMap contained very little information on school 
bus depots. Google Maps contained better information (though 
still incomplete and occasionally incorrect), but scraping data 
from Google Maps is prohibited in their terms of service, 
and our request for an exception for nonprofit research pur-
poses was denied. 
Overview of methods
The general method we used to find school bus depots was to 
analyze very-high-resolution aerial images (0.6–1 m) to identify 
clusters of individual school buses. We were able to treat detect-
ing school buses as a typical object detection problem in optical 
remote sensing because of their particular spectral characteristics 
and dimensions: They are legally required to be painted “school 
bus yellow” (though some have white roofs) and are manufactured 
as just three main types (A, C, and D) with specific dimensions. 
(Type B buses are very infrequently used, constituting approxi-
mately 0.25 percent of the U.S. fleet [Lazer et al. 2023], and 
would be very difficult to distinguish from Type C using remote 
sensing). We labeled dense clusters of school buses as potential 
school bus depots (four or more school buses within a moving 
window size of 80 m by 80 m—a minimum of four buses was 
chosen to balance finding small depots and avoid flagging too 
many non-depot clusters of buses on roadways throughout the 
United States, for instance). At spatial resolutions of one meter or 
even finer, individual school buses and depots are visually dis-
tinguishable, which enabled visual verification of the depots (see

TECHNICAL NOTE   |  Month Year  |  5
Dataset of U.S. school bus depots
“Step 4. Visual interpretation”). We also investigated recognizing 
whole school bus depots as individual objects, but this approach 
was less successful due to the diverse parking lot surface materi-
als, such as asphalt, concrete, sand, or grass, and the wide range of 
depot sizes and layouts.
Various algorithms and approaches have been developed using 
very-high-resolution (less than five meter) remote sensing 
data to identify image objects such as roads, buildings, trees, 
and vehicles (Cheng and Han 2016). These methods can 
be categorized into four general groups: knowledge-based 
methods, object-based image analysis (OBIA) (which we 
use in this analysis), machine learning–based methods, and 
the less common template matching–based methods (which 
are not described here due to infrequent usage) (Cheng and 
Han 2016). Knowledge-based methods use geometric and 
contextual information to identify image objects intuitively. 
For example, the size, shape, and spatial relationships of image 
objects can be used to improve the accuracy of object labeling 
or classification (Shao et al. 2011). OBIA involves a two-step 
image analysis procedure consisting of image segmentation 
and object classification. The first step (image segmentation) 
divides an image into spatially adjoining and spectrally 
homogeneous regions (objects), sometimes referred to as 
segments. These segments are then used as analytical units in 
the following classification procedure, which we used to classify/
identify school buses among the homogeneous “segments.” The 
multiresolution segmentation algorithm within the eCognition 
Essentials software, which allows user-defined scale, shape, 
and compactness parameters, has been widely used for creating 
meaningful image objects to support object detection (Baker 
et al. 2013; Shao et al. 2021). More recently, machine learning 
algorithms, particularly deep neural networks (DNNs), have 
been increasingly employed to extract image features and objects 
(Ma et al. 2019). Examples of DNN applications include the 
detection of airplanes, cars, and urban villages (Zhong et al. 
2018; Ding et al. 2018; Li et al. 2017). The advantage of using 
DNNs is their ability to leverage the rich spatial and spectral 
information available in very-high-resolution data.
Most remote sensing–based object detection studies found in 
the authors’ literature review focus on algorithm development 
at a proof-of-concept level. They are primarily applied to small 
experimental sites using selected imagery due to data and 
computing constraints. However, our task of identifying all 
U.S. school buses required a national-scale mapping effort. This 
dataset represents one of the first attempts in remote sensing 
research to conduct object detection using sub-meter to one-
meter resolution data for a continental-scale application. The 
authors’ literature review yielded one study with a similar goal 
of identifying all industrial poultry operations in the contiguous 
United States using aerial imagery (Robinson et al. 2022); our 
study differs in that we were detecting smaller objects and used 
a multistage approach to increase accuracy. Given the very large 
quantity of aerial images to be processed, our methods balanced 
considerations such as data availability, algorithm performance 
and speed, data storage, and overall operational effectiveness. 
For instance, since there is no readily available training data for 
school bus detection, it was not feasible to develop large-scale 
deep neural networks. Traditional object-based image analysis 
or knowledge-based methods, combined with commonly used 
machine learning algorithms like random forest, are better 
suited for this research. However, the high volume of data and 
computational intensity still posed significant challenges. 
Data sources and description
The primary input data for our study were aerial imagery obtained 
from the National Agriculture Imagery Program (NAIP) (USDA 
2022). Since 2002, the U.S. Department of Agriculture’s Farm 
Service Agency has been acquiring high-resolution aerial imagery 
with a ground sample distance of one meter. To ensure up-to-date 
information for maintaining Common Land Unit boundaries 
and supporting agricultural applications, a three-year repeating 
cycle is employed starting from 2009. NAIP images from recent 
years have four spectral bands—red, green, blue (RGB) and 
near infrared—and spatial resolutions ranging from 0.6 to 1 m. 
NAIP is commonly used in the remote sensing community 
for high-resolution urban mapping, vegetation mapping, and 
object detection (Prasai et al. 2021; Shao et al. 2015). It is freely 
available for the 48 contiguous states of the United States and 
Washington, DC, through the Google Earth Engine (GEE) 
cloud computing platform (Gorelick et al. 2017). NAIP imagery 
excludes Alaska, Hawaii, and all U.S. territories, so they are also 
excluded from this dataset. 
We selected NAIP as our primary input data because it offered 
nationwide, high-resolution, recently updated coverage and 
was free. Additionally, one of the most compelling reasons was 
that, because NAIP is intended for agricultural purposes, the 
images were captured during the agricultural growing season, 
or leaf-on conditions, which in most places corresponds with 
summer, when school buses are rarely in use. Table 1 summa-
rizes the acquisition dates of NAIP images that formed part of 
depots included in this dataset. Approximately half the images 
were collected in June, July, and August. We could not find any 
published data on summertime school bus utilization rates, but 
consultations with experts and school bus operators indicate 
that 0–25 percent of buses are in use in the summer, depend-
ing on the region and owner. Compared with the school year, 
summer usage is more likely to consist of shorter trips that vary 
by day or week.

6  |  
  
Table 1  |   National Agriculture Imagery Program image 
acquisition years and months
YEAR PERCENTAGE OF IMAGES CAPTURED
2018 27.8%
2019 45.5%
2020 19%
2021 7.7%
MONTH PERCENTAGE OF IMAGES CAPTURED
April 0.6%
May 1.3%
June 7.1%
July 22.4%
August 20.8%
September 20.1%
October 14.1%
November 11.8%
December 1.8%
Source: Authors.
As an ancillary data source for our school bus depot mapping 
effort, we acquired Microsoft’s building footprints dataset 
for the United States (Microsoft 2023). This dataset consists 
of 129,591,852 computer-generated building footprints. We 
expected that some small buildings could have similar spectral 
and shape characteristics as school buses; the building footprints 
thus served as masks to remove false positives of buildings 
or portions of buildings that our initial algorithm mislabeled 
as school buses.
We also obtained the Sentinel-2 global land use and land cover 
(LULC) map at a 10-m resolution from Esri (Esri et al. 2023). 
This map was developed using a deep learning segmentation 
model based on Sentinel-2 data (Karra et al. 2021). We used the 
urban classes derived from this LULC map as additional ancil-
lary data, particularly for a subset of western states. In addition to 
the aforementioned datasets, we also acquired various geographic 
information system (GIS) layers, including state and county 
boundaries, as well as school locations, to support data manage-
ment and simple distance measures (i.e., from school bus depots 
to the nearest school). We also used Esri’s ArcGIS World Imagery 
base map (Esri 2023), which has one-meter or finer satellite and 
aerial imagery as an additional reference data source.
Detailed methods
We designed a four-step mapping method for identifying 
school bus depots:
Step 1. Identify possible buses: Image classification for 
identifying possible individual school buses
Step 2. Verify buses: Object-based image analysis to remove non-
bus objects (“false positives”)
Step 3. Identify possible depots: Spatial cluster analysis of image 
objects (buses) for identifying potential school bus depots
Step 4. Verify depots: Verification of school bus depots 
using visual interpretation of NAIP imagery and the Esri 
aerial base map 
The following sections contain detailed descriptions of each step.
Step 1. School bus detection using Google Earth 
Engine–based image classification 
We conducted NAIP image classification using the Google Earth 
Engine cloud computing platform. We used GEE as the starting 
point for initial image analysis, because downloading and process-
ing high-resolution (0.6–1 m) NAIP would present a significant 
challenge for local computation. GEE also has a rich set of 
machine learning algorithms to support various image analytical 
tasks (Gorelick et al. 2017). 
We designed a simple three-class image classification scheme 
to separate school buses, built-up areas, and vegetation cover. 
For each U.S. state, we first did a Google search with the key 
words “school bus depot.” Within the resultant depot locations, 
we selected 10–15 locations per state as our candidate areas for 
training data collection. We collected training data points for 
NAIP image classification by drawing small polygons on bus 
tops, built-up areas, and vegetation cover, respectively. The three-
class scheme is certainly non-exhaustive. However, other surface 
materials such as bare soil can be included in the built-up areas 
because of their spectral similarity. The most important part in 
this mapping procedure is to separate school buses from common 
parking lot materials such as asphalt and concrete. For certain 
school bus depots, the background surface material may be simply 
grass or sand (Figure 1). The unique spectral signals from school 
buses, including both “school bus yellow” or white (for the white 
school bus roofs), still provide sufficient separability against various 
ground surface materials.

TECHNICAL NOTE   |  Month Year  |  7
Dataset of U.S. school bus depots
Figure 1  |   Examples of school bus depots with various ground surface materials 
Source: Esri 2023.

8  |  
  
We employed a commonly used random forest algorithm to 
classify these three classes of interest (Belgiu and Drăguţ 2016). 
Training data were different for each U.S. state, and we imple-
mented GEE image classification state by state, independent of 
each other. Depending on data availability for different states, 
we used seamless NAIP mosaics from 2018 to 2021 as input for 
image classification. We note that NAIP images are acquired 
over a period of weeks (or even months) over the growing sea-
son. Variations in acquisition dates, viewing geometry, and plant 
phenology result in high within-class spectral variability for land 
cover types (Maxwell et al. 2017). It is thus important to check 
initial classification results and collect additional training data 
to improve classification performance, particularly focusing on 
separating school buses from the background surface materials 
of parking lots. 
Figures 2a and 2b show an example of an image classification 
result. Figure 2a includes unprocessed NAIP imagery with 
individual school buses that are clearly visible to the human 
eye. Figure 2b depicts the result of the image classification that 
highlighted possible school buses, with some buildings also 
classified as school buses. In this step, our intention was not to 
achieve a clean image classification of school buses. We delib-
erately erred on the side of being overly inclusive and allowed 
for a higher commission error rate because we could rely on 
subsequent image processing steps to reduce false positives, but 
would have no way of identifying school buses that were missed 
due to overly strict classification. Most false positives were other 
human-made structures that exhibited similar spectral signals 
to school buses (particularly school buses with white tops), 
including buildings with white roofs, storage units, trucks, and 
port containers. 
Figure 2  |   (2a) Unprocessed National Agriculture Imagery Program imagery, with school buses clearly discernable; 
(2b) An example of an image classification result showing possible school buses, with some buildings also 
highlighted
Source: Authors, based on National Agriculture Imagery Program imagery (USDA 2022).
Step 2. Object-based image analysis for 
improving bus mapping results
In Step 1 of image classification, we relied on spectral infor-
mation only to identify school buses and allowed a high 
commission error. In Step 2, we applied object-based analyses to 
identify and filter out objects that are clearly not buses. Object-
based image analysis has been commonly used in the remote 
sensing community, especially for high-resolution urban map-
ping (Shao et al. 2011, 2021). Object-based routines/functions 
within the GEE platform are at an earlier stage of development 
compared with other commercial software packages such as 
MATLAB. Therefore, we downloaded the three-class image 
classification results from GEE and conducted object-based 
analyses using MATLAB in Virginia Tech’s Advanced Research 
Computing environment. This was feasible in terms of local data 
storage because the dimensions of the images were significantly 
reduced—from four bands to one band with only three classes.
We first recoded the image classification results: pixels within 
potential school buses (code = 1), and pixels within built-up or 
vegetation cover (code = 0). We then processed the resultant 
binary image to generate image objects using the four-neighbor 
rule (i.e., delineating potential school bus objects based on 
contiguous pixels that share edges with other pixels that were 
coded as 1). Ideally, a school bus is represented as a single image 
object (see red objects in Figure 2b). Similarly, a small building, 
falsely classified as a school bus, may also be represented as an 
image object. For each image object, we computed several prop-
erties, including object size, major axis length, and perimeter/
area ratio. These object properties were found to be particularly 
useful for separating buses and non-bus objects. We selected 
2a. 2b.

TECHNICAL NOTE   |  Month Year  |  9
Dataset of U.S. school bus depots
Figure 3  |   Example of a school bus depot represented as 
a cluster of school bus image objects
 
Source: Authors, based on National Agriculture Imagery Program imagery (USDA 2022).
two states (Virginia and North Carolina) to examine resultant 
potential bus objects and their spatial properties; selecting just 
two states was sufficient because buses have the same character-
istics in all states. School bus objects typically have the following 
characteristics:
 ▪ Object size in the range of 20–80 pixels (1-m resolution)
 ▪ Major axis length in the range of 8–20 m
 ▪ Perimeter–area ratio larger than 1.15 
These empirical statistics allowed us to remove many non-bus 
image objects. For example, a large building may be falsely 
classified as a school bus in the initial image classification within 
GEE. However, the measurements of object size or major axis 
allowed us to label it as a “non-bus” image object. The range of 
each spatial index (the dimensions that an object could have and 
be considered a potential school bus) is relatively large because 
we did not want to remove potential bus objects that were 
merged from several individual buses, nor buses that may be 
partly obscured by tree cover. 
In addition, we used the U.S. building footprints dataset from 
Microsoft as a mask to further remove false positives. The 
Microsoft dataset contains 129,591,852 computer-generated 
building footprints. We applied a 2-m buffer for each build-
ing footprint before masking. This reduced impacts from 
spatial registration uncertainties (i.e., mismatch of building 
edges from different image sources). For the western United 
States, agricultural regions, deserts, and certain mountain 
areas showed a high rate of false positives. Therefore, in only 
the western states, we applied the 10-m global land use and 
land cover map (Esri et al. 2023) as another mask to remove 
areas labeled as crops, bare ground, and rangeland. For Utah, 
Arizona, and California, we examined locations of school bus 
depots and found that almost all of them are in the urban 
class of land use map.
Step 3. Spatial clustering of school buses, or 
“object density analysis” 
The next step was to identify clusters of buses. Figure 3 
shows an example of a school bus depot where we see 
approximately 60 school buses. However, sometimes images 
of potential school bus depots contain only a few buses. This 
could be because the depot houses only a few buses, other 
school buses from that depot are deployed at that time, it is 
a different type of facility (such as a repair shop or dealer), 
or those buses are parked at a school or other destination to 
pick up riders (and therefore it is not a depot). See “Chal-
lenges and limitations” for more detail on how we accounted 
for these issues. 
There was no clear-cut ideal threshold for how many school 
buses usually constitute a real depot. For this dataset, we 
chose a threshold of a minimum of four school buses within 
a moving window size of 80 m by 80 m to be flagged as 
polygons for subsequent visual verification (see Figure 4 and 
Box 1). This threshold was designed to be high enough that 
we would be unlikely to incorrectly identify school buses as a 
depot if they are driving, one behind another, on a road. We 
estimate that most depots contain well more than four buses, 
but the threshold was set low because it would be possible to 
raise the threshold later in the process before the publication 
of the dataset, but it would not be possible to lower it after 
Step 3 was completed.

10  |  
  
Figure 4  |   Possible school bus depots highlighted using 
spatial clustering or object density analysis
Source: Authors, based on National Agriculture Imagery Program imagery (USDA 2022). 
Step 4. Visual Interpretation
The object intensity analysis resulted in many locations as can-
didates for school bus depots. We relied on two image analysts 
to verify and filter out these false positives. For ease of visual 
interpretation, the spatial polygons with candidates of school 
bus depots were further grouped into 5 kilometer (km) by 5 km 
analytical units. 
Within each analytical unit, image analysts visually interpreted 
candidate locations using ArcGIS World Imagery and NAIP 
from GEE as references. World Imagery has one-meter or finer 
satellite and aerial imagery so it served as another useful refer-
ence for visual interpretation. For a large majority of candidate 
locations, we found agreement between NAIP imagery (GEE) 
and ArcGIS World Imagery—in other words, the images from 
those two sources looked very similar or identical in terms of 
school buses present, even though they were taken on different 
dates. There were rare cases where NAIP imagery showed school 
bus clusters while ArcGIS World Imagery showed an empty 
parking lot. We considered such locations to be valid school bus 
depots. If two parking lots with school buses were in very close 
proximity, such as being separated only by a small building or 
roadway, we assumed that they were part of the same depot, and 
identified them with one point and object identification (ID).
The rate of candidate depots that we found to be true depots 
by visual interpretation ranged from 3 percent to 20 percent for 
most states. For example, we interpreted a total of 421 analytical 
units (1,379 candidate depots) in Delaware and found 81 actual 
school bus depots. It was much more challenging for several 
states in the western United States, such as California, New 
Mexico, and Texas. Due to large geographical coverage and land 
cover characteristics, image analysts typically needed to evaluate 
several thousand analytical units for these states. In total, we 
spent about 500 hours on visual interpretation. Other structures 
and land uses that were included as candidate school bus depots 
included truck rental businesses and truck depots, transit bus 
garages or depots, auto repair businesses, boat storage facilities, 
storage units, certain single family residential areas, and agricul-
tural structures.
In the version of the dataset that resulted from the process 
describe above, there was an outstanding issue: multiple clusters 
of school buses within one depot were often incorrectly identi-
fied as multiple separate depots. Factors that contributed to 
this issue included our relatively low threshold—four or more 
buses—as the definition of a depot, as well as the inspection 
process that involved looking at relatively zoomed-in images of 
depot candidates without broader context. To mitigate this issue, 
we first determined which depot candidates were within 500 
meters of another depot candidate. We selected the threshold of 
500 meters based on the distribution of distances between depot 
candidates and the nearest school; there was a clear drop-off in 
frequency after 500 meters (see Figures 5a and 5b). We then 
conducted further visual inspection on the subset of depot 
candidates within 500 meters of a neighboring depot candidate. 
This resulted in the consolidation of approximately 750 depot 
candidates. We considered clusters of buses to be part of the 
same depot if they were in the same parking lot, were separate 
lots on the campus of the same institution (i.e., a large school 
that had two parking lots on opposite sides of their grounds), 
or were separate lots that were located directly across the street 
from each other without intervening land uses. In ambiguous 
cases, we consulted Google Maps to determine if the clusters or 
adjacent lots were owned by the same entity—if so, we consid -
ered them to be one depot.
We also noticed a larger than anticipated number of commission 
errors, most of which were auto repair businesses with four or 
more visible school buses. To mitigate this issue, we conducted a 
final round of visual inspection of all the remaining depot candi-
dates. We removed 679 depot candidates during that process.

TECHNICAL NOTE   |  Month Year  |  11
Dataset of U.S. school bus depots
After Step 4, we conducted an accuracy assessment by compar-
ing our dataset to an independent reference dataset of school 
bus depots shared by private school transportation companies 
(see “Accuracy assessment: Comparison with reference data-
set of school bus depots”). That accuracy assessment revealed 
83 additional depots that we had not detected using remote 
sensing. Those depots were added to the final dataset, with the 
permission of the companies. This resulted in the final published 
version of the dataset. Due to commercial sensitivities, these 83 
depots are not distinguishable from the others in the dataset. 
RESULTS AND DISCUSSION 
Data structure 
In the dataset, each depot is represented as a single point 
location that is somewhere inside the depot, but in most cases 
not the centroid. The data are available for download as a 
spreadsheet or shapefile. For each depot location, in addition to 
latitude and longitude, we included other attributes to enable 
analysis. The “Data Description and Sources” sheet in the dataset 
includes additional details about the fields and their sources. 
Future additions could include information such as the size 
of the depot or the number of buses observed. Here is the full 
list of fields:
 ▪ Feature ID
 ▪ State
 ▪ State abbreviation
 ▪ State FIPS (Federal Information Processing Series) Code
 ▪ County
 ▪ Locale
 ▪ POINT_X
 ▪ POINT_Y
 ▪ Distance to nearest school (meters)
 ▪ NCES School ID of nearest school
 ▪ Name of nearest school
 ▪ Name of school district
 ▪ LEAID (Local Education Agency Identification) of 
school district
 ▪ Electric utility
 ▪ Census tract ID
 ▪ Total population
 ▪ Percent people of color
 ▪ Percent low-income households
 ▪ PM2.5 concentration1 (micrograms per cubic meter; μg/m3) 
 ▪ Ozone concentration (parts per billion; ppb) 
 ▪ PM2.5 percentile
 ▪ Ozone percentile
School bus depots at schools
A surprising finding from the visual inspection process was that 
many school bus depots seemed to be located at schools. School 
bus depots at schools would have different implications than 
standalone depots, such as a higher exposure of students to the 
bus exhaust. They would also have more potential to integrate 
electric school bus charging with a school’s solar panels, or to use 
the bus batteries as power resources during electricity outages to 
enable the schools to serve as community resilience hubs. 
To enable this dataset to serve those use cases, we calculated 
the distance from each school bus depot to the nearest school, 
using the school location dataset from the National Center for 
Education Statistics (NCES 2022b). Figure 5a illustrates the 
frequency distribution of these distance measures, ranging from 
14 meters to 28,520 meters, with a median value of 337 meters. 
We classified the depots into two groups: at a school, defined as 
350 meters or less from the nearest school; and not at a school, 
defined as more than 350 meters from the nearest school. The 
350-meter threshold was set based on the median value, and the 
observation that after 350 meters, there is a drop-off in the total 
number of depots at a given distance. Based on this definition, 
approximately 51 percent of the school bus depots are at a 
school (5,730 depots). Figure 5a shows the frequency distribu-
tion of distance to a school for all school bus depots, and Figure 
5b shows a zoomed-in version where the x-axis extends to only 
1,500 meters to better illustrate the drop-off around 350 meters. 
We assume that if a school bus is domiciled on the grounds 
of a school, then it serves that school, but it may serve other 
schools too, and may be owned or operated by the school or by 
a private fleet operator. We did not conduct visual inspection 
or any further verification to determine whether depots in the 
vicinity group were located on the grounds of a school. Some 
depots in the vicinity group may happen to be 500 meters from 
a school, but not have any relationship to it, and some depots in 
the non-vicinity group may be on the grounds of schools with 
large campuses.

12  |  
  
Figure 5  |   (5a) Frequency distribution of distance (in meters) to school measurement for all school bus depots; (5b) 
Frequency distribution of distance (in meters) to the nearest school, for depots within 1,500 meters of a school
5a.
5b
.
Source: Authors .
0
50
40
30
20
10
Number of school bus depots
DISITANCE TO NEAREST SCHOOL (METERS)
0K
5K
10K
15K
20K
0
50
40
30
20
10
Number of school bus depots
DISITANCE TO NEAREST SCHOOL (METERS)
0
600
800
1,000
1,200
1,400

TECHNICAL NOTE   |  Month Year  |  13
Dataset of U.S. school bus depots
Distribution of school bus depots 
We identified a total of 11,309 school bus depots across the 48 
contiguous states of the United States and Washington, DC. 
Figure 6 maps these depots as individual points. A higher den-
sity of depots is observed in the eastern part of the United States 
and especially the Northeast, likely related to higher population 
density. The number of depots varies significantly across states, 
likely correlated with factors such as the state’s population and 
the percentage of students that ride school buses. To simplify the 
representation, Figure 7 displays the number of depots by state. 
The median number of depots per state is 218.
Figure 6  |  The distribution of school bus depots in the 48 contiguous U.S. states and Washington, DC
Source: Authors.
North Carolina stands out with a high number of 841 depots. 
However, approximately 85 percent of North Carolina’s detected 
depots are located at schools (often with small clusters of 
approximately four school buses), and the state ranks 13th in 
total number of school buses and 8th in number of school bus 
riders. In other words, the high number of depots seems to 
indicate a decentralization of school bus storage, rather than 
very high school bus usage.
Texas and New York had some of the highest numbers of 
depots, 697 and 618, respectively.

14  |  
  
Figure 7  |  The number of school bus depots identified by state
Source: Authors.
This tracks with their large populations, ranking second and 
fourth among all states. California, the most populous state, only 
has 394 depots—however, California has relatively low school 
bus ridership, at only 9 percent in 2017 (Mays 2022). The large 
variation in ridership among states may be due to differences 
in state-level school transportation requirements or funding, or 
differences in land use patterns or mode shares. The number of 
depots in California may also be an underestimate due to the 
limitations of the remote sensing–based approach. For example, 
school buses may be parked within garages or shelters, which 
the image analysts noted was more common in large cities of 
western states. 
Several states have relatively few school bus depots. For 
instance, South Dakota and Wyoming have only 29 depots each. 
These states have total populations of 895,376 and 578,803, 
respectively, with a high share of rural areas, and therefore 
relatively few school bus depots are expected.
Figures 8 and 9 visualize the state-level total residents per 
school bus depot and school bus riders per depot, respectively.
Table 2 presents state-level data on school bus depots, school 
bus riders, total population, and school buses, and includes 
state rankings.
4 841

TECHNICAL NOTE   |  Month Year  |  15
Dataset of U.S. school bus depots
Figure 8  |  Total residents per school bus depot, by state
Sources:  Authors and CB 2022.
Figure 9  |  School bus riders per depot, by state
Note: The values represented in this map are the number of students that ride the bus in each state divided by the number of school bus depots identified in each state.
Sources:  Authors and BTS 2017.
11,575 167,951
432 3878

16  |  
  
Table 2  |  School bus depots, school bus riders, total population, and school buses, by state
State
Number of 
school bus 
depots
Rank: Number 
of school bus 
depots
Number of 
school bus riders
Percent of 
students that 
ride the bus
School bus 
riders per school 
bus depot
Rank: School bus 
riders per depot
North Carolina 841 1 652,000 42% 775 43
Texas 697 2 1,389,000 28% 1,993 18
New York 618 3 1,290,000 44% 2,087 15
Pennsylvania 539 4 1,059,000 60% 1,965 19
Ohio 523 5 927,000 45% 1,772 22
Michigan 463 6 540,000 34% 1,166 37
Virginia 446 7 586,000 50% 1,314 27
Illinois 405 8 754,000 37% 1,862 21
California 394 9 546,000 9% 1,386 26
Missouri 326 10 422,000 61% 1,294 30
Georgia 322 11 847,000 50% 2,630 6
Alabama 319 12 249,000 36% 781 42
Indiana 316 13 439,000 50% 1,389 25
Florida 300 14 854,000 31% 2,847 4
New Jersey 272 15 546,000 38% 2,007 17
Mississippi 254 16 240,000 50% 945 41
Wisconsin 254 16 312,000 35% 1,228 33
Minnesota 252 17 529,000 55% 2,099 14
Oklahoma 238 18 110,000 17% 462 48
Arkansas 237 19 265,000 52% 1,118 38
Maryland 231 20 510,000 57% 2,208 10
Kentucky 223 21 473,000 65% 2,121 12
Washington 218 22 527,000 52% 2,406 8
Massachusetts 219 22 457,000 49% 2,087 16
Tennessee 218 23 280,000 27% 1,284 31
South Carolina 206 24 294,000 39% 1,427 24
Arizona 165 25 314,000 30% 1,903 20
Louisiana 165 25 413,000 54% 2,503 7
Connecticut 155 26 203,000 47% 1,310 28
Kansas 151 27 156,000 26% 1,033 39
Iowa 150 28 185,000 34% 1,233 32
Oregon 144 29 187,000 29% 1,299 29
Colorado 128 30 153,000 20% 1,195 35
Maine 112 31 136,000 48% 1,214 34
Idaho 95 32 210,000 48% 2,188 11

TECHNICAL NOTE   |  Month Year  |  17
Dataset of U.S. school bus depots
State Number of 
residents
Residents 
per depot
Rank: 
Residents 
per depot
Number 
of school 
buses
School 
buses 
per depot
Rank: 
School 
buses per 
depot
Number of 
depots at 
schools
Percent of 
depots at 
schools
Rank: 
Percent of 
depots at 
schools
North Carolina  10,698,973 12,722 47 12,975 15.4 46 715 85.0% 1
Texas  30,029,572 43,084 8 50,327 72.2 4 381 54.7% 19
New York  19,677,151 31,840 15 45,600 73.8 3 226 36.6% 37
Pennsylvania  12,972,008 24,067 24 30,835 57.2 14 111 20.6% 44
Ohio  11,756,058 22,478 29 14,522 27.8 38 283 54.1% 20
Michigan  10,034,113 21,672 30 16,844 36.4 31 265 57.2% 13
Virginia    8,683,619 19,470 37 12,572 28.2 37 300 67.3% 6
Illinois  12,582,032 31,067 17 25,337 62.6 10 183 45.2% 31
California  39,029,342 99,059 2 20,333 51.6 18 191 48.5% 28
Missouri    6,177,957 18,951 39 11,889 36.5 30 205 62.9% 11
Georgia  10,912,876 33,891 11 20,186 62.7 9 159 49.4% 26
Alabama    5,074,296 15,907 42 7,913 24.8 43 224 70.2% 5
Indiana    6,833,037 21,624 31 16,533 52.3 17 174 55.1% 17
Florida  22,244,823 74,149 4 18,164 60.5 13 153 51.0% 24
New Jersey    9,261,699 34,050 10 16,704 61.4 12 87 32.0% 38
State
Number of 
school bus 
depots
Rank: Number 
of school bus 
depots
Number of 
school bus riders
Percent of 
students that 
ride the bus
School bus 
riders per school 
bus depot
Rank: School bus 
riders per depot
New Mexico 88 33 38,000 19% 432 49
West Virginia 85 34 230,000 83% 2,706 5
Montana 71 35 49,000 33% 671 45
Delaware 70 36 67,000 63% 957 40
Nebraska 59 37 31,000 12% 525 46
Utah 53 38 191,000 24% 3,604 2
New Hampshire 51 39 160,000 66% 3,137 3
Vermont 48 40 23,000 28% 479 47
Rhode Island 43 41 76,000 51% 1,767 23
North Dakota 42 42 49,000 50% 1,167 36
Nevada 41 43 159,000 43% 3,878 1
Wyoming 29 44 22,000 23% 759 44
South Dakota 29 44 61,000 46% 2,103 13
District of Columbia 4 45 9,000 6% 2,250 9
Table 2  |  School bus depots, school bus riders, total population, and school buses, by state (Continued)

18  |  
  
State Number of 
residents
Residents 
per depot
Rank: 
Residents 
per depot
Number 
of school 
buses
School 
buses 
per depot
Rank: 
School 
buses per 
depot
Number of 
depots at 
schools
Percent of 
depots at 
schools
Rank: 
Percent of 
depots at 
schools
Mississippi 2,940,057 11,575 49 3,559 14.0 47 179 70.5% 4
Wisconsin    5,892,539   23,199 27 10,055 39.6 28 56 22.0% 42
Minnesota    5,7 17,184   22,687 28 17,014 67.5 7 67 26.6% 40
Oklahoma    4,019,800   16,890 41 562  2.4 49 153 64.3% 8
Arkansas    3,045,637   12,851 46 6,515 27.5 39 171 72.2% 3
Maryland    6,164,660   26,687 21  7,248 31.4 35 39 16.9% 45
Kentucky    4,512,310   20,235 34  9,488 42.5 23 141 63.2% 9
Washington    7,785,786   35,552 9   10,601 48.4 19 124 56.6% 14
Massachusetts    6,981,974   31,881 14  9,000 41.1 26 46 21.0% 43
Tennessee    7,051,339   32,346 13  9,233 42.4 24 98 45.0% 32
South Carolina    5,282,634   25,644 22  6,930 33.6 34 130 63.1% 10
Arizona    7,359,197   44,601 7  7,166 43.4 22 110 66.7% 7
Louisiana    4,590,241   27,820 19  6,841 41.5 25 81 49.1% 27
Connecticut    3,626,205   23,395 26  8,600 55.5 16 22 14.2% 47
Kansas    2,937,150   19,451 38  4,026 26.7 41 78 51.7% 22
Iowa    3,200,517   21,337 32  6,020 40.1 27 72 48.0% 29
Oregon    4,240,137   29,445 18  4,913 34.1 32 53 36.8% 36
Colorado    5,839,926   45,624 6 683  5.3 48 59 46.1% 30
Maine    1,385,340   12,369 48  2,815 25.1 42 43 38.4% 35
Idaho    1,939,033   20,198 35  2,996 31.2 36 53 55.2% 16
New Mexico    2,113,344   24,015 25  2,007 22.8 44 45 51.1% 23
West Virginia    1,775,156   20,884 33  2,900 34.1 33 34 40.0% 33
Montana    1,122,867   15,382 43  3,502 48.0 20 41 56.2% 15
Delaware    1,018,396   14,549 44  1,565 22.4 45 11 15.7% 46
Nebraska    1,967,923   33,355 12  5,706 96.7 2 31 52.5% 21
Utah    3,380,800   63,789 5  3,286 62.0 11 21 39.6% 34
New Hampshire    1,395,231   27,357 20  3,200 62.7 8 4 7.8% 49
Vermont 647,064   13,481 45  1,300 27.1 40 24 50.0% 25
Rhode Island    1,093,734   25,436 23  1,691 39.3 29 6 14.0% 48
North Dakota 779,261   18,554 40  2,351 56.0 15 23 54.8% 18
Nevada    3,177 ,772   77,507 3  2,903 70.8 5 32 78.0% 2
Wyoming 581,381   20,048 36 1,343 46.3 21 17 58.6% 12
South Dakota 909,824   31,373 16  2,000 69.0 6 8 27.6% 39
District of Columbia 671,803 167,951 1 683  170.8 1 1 25.0% 41
Table 2  |  School bus depots, school bus riders, total population, and school buses, by state (Continued)
Sources:  Authors; SBFM 2023; CB 2022; FHA 2017.

TECHNICAL NOTE   |  Month Year  |  19
Dataset of U.S. school bus depots
Accuracy assessment 
Before undertaking this analysis, we consulted school transpor-
tation experts from the School District Technical Assistance 
team of WRI’s Electric School Bus Initiative to roughly esti-
mate the number of depots that we expected to find across all 
U.S. states and territories. The team expected that most school 
districts would have one depot, some would have multiple, and 
some would have none, and that some additional depots would 
serve entities other than public school districts (such as Head 
Start programs), so we anticipated finding slightly more depots 
than school districts. Given the 13,000 “regular” school districts 
in the United States, we arrived at an estimate of roughly 16,000 
depots. Our dataset’s count of 11,309 depots is lower than the 
initial 16,000-depot approximation, but is within a reasonable 
margin of error, especially considering our analysis did not 
include Hawaii (which has about 725 school buses), Alaska 
(which has about 950 school buses), or any U.S. territories, and 
likely missed some enclosed depots.
Comparison with reference dataset of school 
bus depots
To assess the accuracy of our dataset, we compared the loca-
tions of school bus depots found through our remote sensing 
approach with an independent reference dataset of 506 known 
school bus depot locations from First Student and National 
Express, large school transportation companies that generously 
shared their depot locations to support this research. The First 
Student depots are distributed across 38 states, though most are 
clustered in the northeastern, midwestern, and western states. 
The 151 National Express depots are in 28 states. Together, 
the two datasets include depots in 41 states, offering a sample 
within the majority of states for the accuracy assessment. 
For each depot from the reference dataset that we had not 
detected using remote sensing, we visually examined both the 
NAIP imagery and Esri imagery to identify school bus clus-
ters within a 300–500-meter buffer. This generated a detailed 
comparison between remote sensing–derived school bus depots 
and the reference datasets (Table 3). 
State Number of 
residents
Residents 
per depot
Rank: 
Residents 
per depot
Number 
of school 
buses
School 
buses 
per depot
Rank: 
School 
buses per 
depot
Number of 
depots at 
schools
Percent of 
depots at 
schools
Rank: 
Percent of 
depots at 
schools
Mississippi 2,940,057 11,575 49 3,559 14.0 47 179 70.5% 4
Wisconsin    5,892,539   23,199 27 10,055 39.6 28 56 22.0% 42
Minnesota    5,7 17,184   22,687 28 17,014 67.5 7 67 26.6% 40
Oklahoma    4,019,800   16,890 41 562  2.4 49 153 64.3% 8
Arkansas    3,045,637   12,851 46 6,515 27.5 39 171 72.2% 3
Maryland    6,164,660   26,687 21  7,248 31.4 35 39 16.9% 45
Kentucky    4,512,310   20,235 34  9,488 42.5 23 141 63.2% 9
Washington    7,785,786   35,552 9   10,601 48.4 19 124 56.6% 14
Massachusetts    6,981,974   31,881 14  9,000 41.1 26 46 21.0% 43
Tennessee    7,051,339   32,346 13  9,233 42.4 24 98 45.0% 32
South Carolina    5,282,634   25,644 22  6,930 33.6 34 130 63.1% 10
Arizona    7,359,197   44,601 7  7,166 43.4 22 110 66.7% 7
Louisiana    4,590,241   27,820 19  6,841 41.5 25 81 49.1% 27
Connecticut    3,626,205   23,395 26  8,600 55.5 16 22 14.2% 47
Kansas    2,937,150   19,451 38  4,026 26.7 41 78 51.7% 22
Iowa    3,200,517   21,337 32  6,020 40.1 27 72 48.0% 29
Oregon    4,240,137   29,445 18  4,913 34.1 32 53 36.8% 36
Colorado    5,839,926   45,624 6 683  5.3 48 59 46.1% 30
Maine    1,385,340   12,369 48  2,815 25.1 42 43 38.4% 35
Idaho    1,939,033   20,198 35  2,996 31.2 36 53 55.2% 16
New Mexico    2,113,344   24,015 25  2,007 22.8 44 45 51.1% 23
West Virginia    1,775,156   20,884 33  2,900 34.1 33 34 40.0% 33
Montana    1,122,867   15,382 43  3,502 48.0 20 41 56.2% 15
Delaware    1,018,396   14,549 44  1,565 22.4 45 11 15.7% 46
Nebraska    1,967,923   33,355 12  5,706 96.7 2 31 52.5% 21
Utah    3,380,800   63,789 5  3,286 62.0 11 21 39.6% 34
New Hampshire    1,395,231   27,357 20  3,200 62.7 8 4 7.8% 49
Vermont 647,064   13,481 45  1,300 27.1 40 24 50.0% 25
Rhode Island    1,093,734   25,436 23  1,691 39.3 29 6 14.0% 48
North Dakota 779,261   18,554 40  2,351 56.0 15 23 54.8% 18
Nevada    3,177 ,772   77,507 3  2,903 70.8 5 32 78.0% 2
Wyoming 581,381   20,048 36 1,343 46.3 21 17 58.6% 12
South Dakota 909,824   31,373 16  2,000 69.0 6 8 27.6% 39
District of Columbia 671,803 167,951 1 683  170.8 1 1 25.0% 41
Out of the 506 depots in the reference datasets, our approach 
successfully detected 429 of them (84.8 percent). When con-
sidering the effectiveness of remote sensing for finding all U.S. 
school bus depots, the omission rate was 15.2 percent (i.e., we 
missed 15.2 percent of all depots in the reference datasets). In 
terms of the effectiveness of using remote sensing plus visual 
inspection, the omission rate was 7.7 percent (39 depots); in 
other words, this method missed 7.7 percent of the buses that 
it should have been able to detect. An examination of the 39 
depots categorized as “Missed, buses visible in NAIP”  revealed 
that contributing factors included confusion between buses 
and background surface materials of parking lots, buses located 
underneath trees and shade structures, and closely clustered 
buses that resulted in large image objects. These factors could 
not be easily resolved with the current image analysis approach. 
Our remote sensing approach used one set of NAIP imagery 
as input, but future work could incorporate multiple years of 
NAIP data to reduce omissions related to image acquisition 
dates and times.
Overall, we consider our omission rate to be acceptable for a 
national-scale mapping effort, and a large improvement over the 
current condition where there was no school bus depot dataset 
whatsoever. If our omission rate was extrapolated to the entire 
country, that would indicate an estimated 13,000 depots in the 
United States. 
We think that we have few commission errors because Step 
4 uses visual interpretation, which is conclusive in determin-
ing that the locations included in the dataset are parking lots 
with school buses.
CHALLENGES AND 
LIMITATIONS 
The main challenge in creating this dataset were the large 
data and computing needs. The study is data- and computing-
intensive because it uses one-meter NAIP imagery for the entire 
country. Although GEE provides the NAIP imagery archive 
and supports initial image classification, the state-by-state 
processing and data downloading are still time-consuming. For 
example, for the state of New York, it took more than 10 hours 
to download all classification results. Object-based analyses are 
handled locally at Virginia Tech’s Advanced Research Comput-
ing. A large majority of image processing steps are streamlined 
and parallel processing is employed, so these components require 
less human interaction. The most time-consuming component 
is the final step involving visual interpretation and verification 
of school bus depots. Because we did not want to apply overly

20  |  
  
Table 3  |  Results of accuracy assessment
CATEGORY
DEPOT IN 
REFERENCE 
DATASET?
DETECTED 
USING OUR 
REMOTE SENSING 
METHODS?
BUSES 
VISIBLE 
IN NAIP 
IMAGERY?
BUSES VISIBLE 
IN ESRI 
IMAGERY?
DESCRIPTION NUMBER OF 
DEPOTS PERCENTAGE
Detected Yes Yes  N/A  N/A These depots were identified using remote 
sensing. 429 84.8%
Missed, 
buses 
visible in 
NAIP
Yes No Yes  N/A
These depots were missed using remote 
sensing despite being visible in our main 
dataset of aerial imagery (NAIP). This 
indicates the shortcomings of our remote 
sensing algorithm.
39 7.7%
Missed, 
buses 
visible in 
Esri but not 
NAIP
Yes No No Yes
These depots were missed using remote 
sensing and were not visible in our 
main dataset of aerial imagery (NAIP), 
but supplementary imagery from Esri 
confirmed the presence of a depot at 
this location. This does not indicate a 
failure of the remote sensing algorithm, 
because there were no buses visible for 
it to detect in NAIP , but it does reflect 
the shortcomings of relying only on 
NAIP imagery since some images were 
captured when no buses were present.
19 3.8%
Missed, 
no buses 
visible
Yes No No No
Depots missed using remote sensing, 
and there were no buses visible in 
either dataset. This could reflect the 
shortcomings of using any remote sensing 
approach and imagery to detect bus 
depots compared with collecting data 
directly from districts or operators. It 
could also indicate error in the reference 
datasets; i.e., the depot was closed but the 
list of locations was not updated, or the 
location is only an office.
19 3.8%
Total 506 100%
Omission error 77 15.2%
Note: NAIP = National Agriculture Imagery Program; N/A = not applicable.
Source: Authors.

TECHNICAL NOTE   |  Month Year  |  21
Dataset of U.S. school bus depots
aggressive screening methods in the previous analytical proce-
dures, image analysts needed to assess many candidate depots 
for each state. For example, we visually examined approximately 
4,000 image clips or analytical units for a state with approxi-
mately 400 school bus depots. 
The two main limitations of the resulting dataset are possible 
omission errors and missing states and territories. Remote 
sensing methods are not well suited for identifying depots 
that are enclosed in a building, except in cases where multiple 
school buses are present in associated parking lots. We may 
also have missed depots where the buses were deployed at the 
time the image was captured, though empty parking lots in 
moderate-sized depots are likely less common. However, visual 
interpretation of various image sources, such as NAIP imagery 
from multiple mapping years and Esri aerial images, generally 
confirmed our identification of school bus depots, although 
the specific number and location of school buses sometimes 
varied. To reduce potential omission errors from the one-year, or 
“snapshot,” mapping, we could apply the same image analytical 
approach to NAIP imagery from different years and then com-
bine mapping results. Furthermore, future studies could explore 
the use of various deep neural networks for school bus depot 
detection. School buses that are painted entirely white might not 
have been identified using our methods; however, since they may 
be parked in depots with yellow school buses, the depot may still 
have been identified. Notably, our results, consisting of 11,309 
depots, can serve as a valuable training and validation dataset for 
other methods that could be used to improve accuracy.
The dataset encompasses school bus depots in the 48 contiguous 
U.S. states and Washington, DC. Alaska, Hawaii, and all U.S. 
territories were excluded because NAIP imagery is not available 
in those places. We expect that many depots in Alaska may be 
enclosed due to the cold weather, so they may not have been 
identified using remote sensing anyway. A source of commission 
error could be school parking lots where multiple school buses 
were parked briefly to pick up students, but that do not serve 
as a depot for the buses. We addressed this challenge by using 
images taken during the summer, setting a minimum threshold 
of four buses, and using visual inspection to distinguish depots 
from buses in use.
CONCLUSION 
By employing a combination of machine learning, object-based 
image analysis techniques, and visual verification, we success-
fully identified over 11,000 school bus depots across the 48 
contiguous U.S. states and Washington, DC. Our approach used 
high-resolution remote sensing imagery obtained from NAIP . 
Notably, this study represents the first continental-scale effort to 
detect small objects using sub-meter to one-meter high-resolu-
tion imagery. At the state level, we observed a strong correlation 
between the total number of school bus depots and both the 
total population and total number of school buses. A point-by-
point comparison with an independent reference dataset (n = 
506) also showed a good agreement between two datasets. An 
omission error of approximately 15 percent indicates a high 
detection rate and validates the reliability of our method. Our 
remote sensing analytical approach can be applied to similar 
tasks that require object detection using very-high-resolution 
remote sensing data. The availability of school bus depot 
locations will be beneficial to researchers, practitioners, and poli-
cymakers, enabling them to support various initiatives related to 
public health, environmental studies, and sustainability.

22  |  
  
ENDNOTE
1. PPM2.5 is defined as particulate matter of 2.5 
micrometers or less in diameter.

TECHNICAL NOTE   |  Month Year  |  23
Dataset of U.S. school bus depots
REFERENCES
APP (Atlas Public Policy). n.d. “Atlas EV Hub.” https://www.atlasevhub.
com/. Accessed October 24, 2022.
Austin, W., G. Heutel, and D. Kreisman. 2019. “School Bus Emissions, 
Student Health and Academic Performance.” Economics of Education 
Review 70 (June): 109–26. doi:10.1016/j.econedurev.2019.03.002.
Baker, B.A., T.A. Warner, J.F. Conley, and B.E. McNeil. 2013. “Does 
Spatial Resolution Matter? A Multi-scale Comparison of Object-Based 
and Pixel-Based Methods for Detecting Change Associated with 
Gas Well Drilling Operations.”  International Journal of Remote Sens -
ing 34  (5): 1633–51.
Beatty, T.K.M., and J.P. Shimshack. 2011. “School Buses, Diesel Emis -
sions, and Respiratory Health.” Journal of Health Economics  30 (5): 
987–99. doi:https://doi.org/10.1016/j.jhealeco.2011.05.017.
Belgiu, M., and L. Drăguţ. 2016. “Random Forest in Remote Sensing: 
A Review of Applications and Future Directions.” ISPRS Journal of 
Photogrammetry and Remote Sensing  114: 24–31.
Brown, P., B. Mayer, S. Zavestoski, T. Luebke, J. Mandelbaum, and S. 
McCormick. 2003. “The Health Politics of Asthma: Environmental 
Justice and Collective Illness Experience in the United States.” Social 
Science & Medicine  57 (3): 453–64.
Brunekreef, B., N.A. Janssen, J. de Hartog, H. Harssema, M. Knape, and 
P. van Vliet. 1997. “Air Pollution from Truck Traffic and Lung Function in 
Children Living near Motorways.”  Epidemiology 8  (3): 298–303.
BTS (U.S. Bureau of Transportation Statistics). 2017. “National House -
hold Travel Survey Daily Travel Quick Facts.” https://www.bts.gov/
statistical-products/surveys/national-household-travel-survey-daily-
travel-quick-facts .
CB (U.S. Census Bureau). 2022. “Population Estimates Program (PEP) 
Data.” https://www.census.gov/quickfacts/.
Chakraborty, J., and J.J. Aun. 2023. “Social Inequities in Exposure 
to Traffic-Related Air and Noise Pollution at Public Schools in 
Texas.”  International Journal of Environmental Research and Public 
Health 20  (7): 5308.
Cheng, G., and J. Han. 2016. “A Survey on Object Detection in Opti -
cal Remote Sensing Images.”  ISPRS Journal of Photogrammetry and 
Remote Sensing 117 : 11–28.
Cook, Q., K. Argenio, and S. Lovinsky-Desir. 2021. “The Impact of En -
vironmental Injustice and Social Determinants of Health on the Role 
of Air Pollution in Asthma and Allergic Disease in the United States.” 
The Journal of Allergy and Clinical Immunology  148 (5): 1089–1101.e5. 
doi:10.1016/j.jaci.2021.09.018.
Ding, P., Y. Zhang, W.-J. Deng, P. Jia, and A. Kuijper. 2018. “A Light 
and Faster Regional Convolutional Neural Network for Object 
Detection in Optical Remote Sensing Images.” ISPRS Journal of 
Photogrammetry and Remote Sensing  141 (July): 208–18. doi: 10.1016/j.
isprsjprs.2018.05.005 .
Esri. 2023. “World Imagery.” Map Service. Updated August 16. 
https://www.arcgis.com/home/item.html?id=10df2279f9684e4a
9f6a7f08febac2a9.
Esri, Impact Observatory, and Microsoft. 2023. “Sentinel-2 10-Meter 
Land Use/Land Cover. ”https://www.arcgis.com/home/item.html?id=
cfcb7609de5f478eb7 666240902d4d3d .
FHA (U.S. Department of Transportation, Federal Highway Ad -
ministration). 2017. “National Household Travel Survey.” https://
nhts.ornl.gov/.
Gorelick, N., M. Hancher, M. Dixon, S. Ilyushchenko, D. Thau, and R. 
Moore. 2017. “Google Earth Engine: Planetary-Scale Geospatial Analy -
sis for Everyone.”  Remote Sensing of Environment   202: 18–27.
Hsu, Y.-T., S. Yan, and P. Huang. 2021. “The Depot and Charging Facil -
ity Location Problem for Electrifying Urban Bus Services.” Transporta-
tion Research Part D: Transport and Environment  100: 103053.
Huether, P. 2021. Siting Electric Vehicle Supply Equipment (EVSE) with 
Equity in Mind. White Paper. Washington, DC: American Council for 
an Energy-Efficient Economy. www.aceee.org/Sites/Default/Files/
Pdfs/Siting_evse_with_equity_final_3-30-21.pdf.
ITDP (Institute for Transportation and Development Policy). 2021. 
“Highways and Zoning: Tools of Racist Policy.” Transport Matters  
(blog). March 10. https://www.itdp.org/2021/03/10/highways-and-
zoning-tools-of- racist-policy/.
Karra, K., C. Kontgis, Z. Statman-Weil, J.C. Mazzariello, M. Mathis, and 
S.P. Brumby. 2021. “Global Land Use/Land Cover with Sentinel 2 and 
Deep Learning.” In  2021 IEEE International Geoscience and Remote 
Sensing Symposium IGARSS , 4704–07. New York: IEEE.
Lazer, L., and L. Freehafer. 2023. “A Dataset of Electric School Bus 
Adoption in the United States.” Technical Note. Washington, DC: 
World Resources Institute. https://www.wri.org/research/technical-
note-dataset-electric-school-bus-adoption-united-states.

24  |  
  
Park, J., and B.I. Kim. 2010. “The School Bus Routing Problem: A Re -
view.”  European Journal of Operational Research   202 (2): 311–19.
Prasai, R., T.W. Schwertner, K. Mainali, H. Mathewson, H. Kafley, S. 
Thapa, D. Adhikari, et al. 2021. “Application of Google Earth Engine Py -
thon API and NAIP Imagery for Land Use and Land Cover Classifica -
tion: A Case Study in Florida, USA.”   Ecological Informatics   66: 101474.
Robinson, C., B. Chugg, B. Anderson, J.M.L. Ferres, and D.E. Ho. 2022. 
“Mapping Industrial Poultry Operations at Scale with Deep Learning 
and Aerial Imagery.” IEEE Journal of Selected Topics in Applied Earth 
Observations and Remote Sensing  15: 7458–71.
SBFM (School Bus Fleet Magazine ). 2023. “School Bus Fleet Fact 
Book 2023.” https://schoolbusfleet.mydigitalpublication.com/fact-
book-2023/page-14?pp=1.
Shao, Y., G.N. Taff, and S.J. Walsh. 2011. “Shadow Detection and 
Building-Height Estimation Using IKONOS Data.”   International Journal 
of Remote Sensing  32 (22): 6929–44.
Shao, Y., G.L. Li, E. Guenther, and J.B. Campbell. 2015. “Evaluation 
of Topographic Correction on Subpixel Impervious Cover Mapping 
with CBERS-2B Data.”  IEEE Geoscience and Remote Sensing Let -
ters  12 (8): 1675–79.
Shao, Y., A.J. Cooner, and S.J. Walsh. 2021. “Assessing Deep Convolu -
tional Neural Networks and Assisted Machine Perception for Urban 
Mapping.”  Remote Sensing 13  (8): 1523.
USDA (U.S. Department of Agriculture). 2022. “National Agriculture 
Imagery Program (NAIP).” Version 10.8.1. https://naip-usdaonline.
hub.arcgis.com/ .
Zhong, Y., X. Han, and L. Zhang. 2018. “Multi-class Geospatial Object 
Detection Based on a Position-Sensitive Balancing Framework for 
High Spatial Resolution Remote Sensing Imagery.” ISPRS Journal of 
Photogrammetry and Remote Sensing  138 (April): 281–94. doi: 10.1016/j.
isprsjprs.2018.02.014 .
Lazer, L., L. Freehafer, and J. Wang. 2023. “Dataset of U.S. School Bus 
Fleets.” Version 2. Washington, DC: World Resources Institute. https://
datasets.wri.org/dataset/sch ool_bus_fleets .
Levinson, M., and A. Achury. 2023. “Clearinghouse: Electric School 
Bus Funding and Financing Opportunities.” Electric School Bus 
Initiative. Washington, DC: World Resources Institute. https://electric -
schoolbusinitiative.org/clearinghouse-electric-school-bus-funding-
and-financing-opportunities.
Li, C., Q. Nguyen, P.H. Ryan, G.K. LeMasters, H. Spitz, M. Lobaugh, 
S. Glover, et al. 2009. “School Bus Pollution and Changes in the Air 
Quality at Schools: A Case Study.”  Journal of Environmental Monitor-
ing  11 (5): 1037–42.
Li, Y., X. Huang, and H. Liu. 2017. “Unsupervised Deep Feature 
Learning for Urban Village Detection from High-Resolution Remote 
Sensing Images.”  Photogrammetric Engineering & Remote Sens -
ing  83 (8): 567–79.
Linden, J. 2008. “At the Bus Depot: Can Administrative Complaints 
Help Stalled Environmental Justice Plaintiffs?” NYU Envtl. LJ  16: 170.
Ma, L., Y. Liu, X. Zhang, Y. Ye, G. Yin, and B.A. Johnson. 2019. “Deep 
Learning in Remote Sensing Applications: a Meta-Analysis and 
Review.”  ISPRS Journal of Photogrammetry and Remote Sens -
ing 152 : 166–77.
Maxwell, A.E., T.A. Warner, B.C. Vanderbilt, and C.A. Ramezan. 2017. 
“Land Cover Classification and Feature Extraction from National 
Agriculture Imagery Program (NAIP) Orthoimagery: A Review.” Photo-
grammetric Engineering & Remote Sensing  83 (11): 737–47.
Mays, M. 2022. “California Is Richer than Ever. Why Is It Last in the 
Nation for School Bus Access?” Los Angeles Times , June 22. Sec. 
California. https://www.latimes.com/california/story/2022-06-22/
theres-a-human-cost-to-this-california-ranks-lowest-in-nation-for-
school-bus-use .
Microsoft. 2023. “US Building Footprints.” https://github.com/Micro -
soft/USBuild ingFootprints . 
NCES (National Center for Education Statistics). 2020. “Common Core 
of Data (CCD).” https://nces.ed.gov /ccd/files.asp .
NCES. 2022a. “Annual Reports and Information.” Last updated 
May. https://nces.ed.gov/programs/coe/indicator/cgc/private-
school-enrollment .
NCES. 2022b. “School Locations & Geoassignments: Public Schools 
& School Districts.” https://nces.ed.gov/programs/edge/Geographic/
SchoolLocations.

TECHNICAL NOTE   |  Month Year  |  25
Dataset of U.S. school bus depots
ADDITIONAL SOURCES 
CONSULTED
Baatz, M. 2000. “Multiresolution Segmentation: An Optimization 
Approach for High Quality Multi-scale Image Segmentation.”   Ange-
wandte Geographische Informationsverarbeitung:  12–23.
Blaschke, T. 2010. “Object Based Image Analysis for Remote 
Sensing.”  ISPRS Journal of Photogrammetry and Remote Sens -
ing 65 (1): 2–16.
U.S. Environmental Protection Agency. 2023. “EJScreen.” https://
ejscreen.epa.gov/.
Homeland Infrastructure Foundation Level Database. 2023. “Elec -
tric Retail Service Territories.” https://hifld-geoplatform.opendata.
arcgis.com/datasets/geoplatform::electric-retail-service-territories-2/
explore?location=32.405550%2C-105 .636155%2C3.00 .
National Center for Education Statistics . 2020. “School District 
Boundaries.” https://nces.ed.gov/programs/edge/eographic/Dis -
trictBoundaries.
Trinder, J.C., and Y. Wang. 1998. “Automatic Road Extraction from 
Aerial Images.”  Digital Signal Processing 8 (4): 215–24.

Copyright 2023 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License.  
To view a copy of the license, visit http://creativecommons.org/licenses/by/4.0/
  
10 G Street, NE  |  Washington, DC 20002  |  WRI.ORG
ABOUT WRI 
World Resources Institute is a global research organization that 
turns big ideas into action at the nexus of environment, economic 
opportunity, and human well-being. 
Our challenge
Natural resources are at the foundation of economic opportunity and 
human well-being. But today, we are depleting Earth’s resources at 
rates that are not sustainable, endangering economies and people’s 
lives. People depend on clean water, fertile land, healthy forests, 
and a stable climate. Livable cities and clean energy are essential 
for a sustainable planet. We must address these urgent, global 
challenges this decade.
Our vision
We envision an equitable and prosperous planet driven by the wise 
management of natural resources. We aspire to create a world where 
the actions of government, business, and communities combine to 
eliminate poverty and sustain the natural environment for all people.
Our approach
COUNT IT
We start with data. We conduct independent research and draw on 
the latest technology to develop new insights and recommendations. 
Our rigorous analysis identifies risks, unveils opportunities, and 
informs smart strategies. We focus our efforts on influential 
and emerging economies where the future of sustainability 
will be determined.
CHANGE IT
We use our research to influence government policies, business 
strategies, and civil society action. We test projects with communities, 
companies, and government agencies to build a strong evidence 
base. Then, we work with partners to deliver change on the ground 
that alleviates poverty and strengthens society. We hold ourselves 
accountable to ensure our outcomes will be bold and enduring.
SCALE IT
We don’t think small. Once tested, we work with partners to adopt 
and expand our efforts regionally and globally. We engage with 
decision-makers to carry out our ideas and elevate our impact. We 
measure success through government and business actions that 
improve people’s lives and sustain a healthy environment.
ACKNOWLEDGMENTS
Thank you to the image analysts from Virginia Tech who helped verify 
the school bus depot locations. Thank you to our internal and external 
reviewers, Alex Kovac, Amy Todd, Ben Shapiro, Brian Zepka, Carlos 
Muñoz Pina, Carolina Chacon, Heng Wan, Jamie Dunckley, John 
Iiames, Sophie Young, and Thet Hein Tun. Thank you to First Student 
and National Express for sharing their school bus depot location data 
to help us assess the accuracy of this dataset. Thank you to Sarah 
DeLucia for editing and Julie Moretti for layout.
ABOUT THE AUTHORS
Yang Shao is an associate professor in the Department of 
Geography at Virginia Tech. His work focuses on remote sensing 
digital image processing, GIS, and statistical modeling, with a 
specialty in advanced image classification algorithms for land cover 
mapping.
Leah Lazer  is a research associate focused on sustainable, equitable 
transportation with the Ross Center for Sustainable Cities program 
and the New Urban Mobility Alliance at WRI.
Gregory Taff is director of research and data integrity at WRI and 
has a background in remote sensing and land use change. 
CREDIT AUTHOR STATEMENT
Yang Shao: Conceptualization, methodology, software, validation, 
formal analysis, investigation, resources, data curation, writing 
(original draft), writing (review and editing), supervision, project 
administration 
Leah Lazer:  Conceptualization, methodology, validation, data 
curation, formal analysis, writing (original draft), writing (review and 
editing), visualization, supervision, project administration
Gregory Taff: Conceptualization, methodology, writing (review and 
editing), supervision, project administration
