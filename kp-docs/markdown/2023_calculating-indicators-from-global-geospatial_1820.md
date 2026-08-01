---
doc_id: 2023_calculating-indicators-from-global-geospatial_1820
source_pdf: kp-docs/askwri-kps/2023_calculating-indicators-from-global-geospatial_1820.pdf
extraction_method: cache-plaintext
char_count: 148250
title: Calculating Indicators From Global Geospatial Data Sets for Benchmarking and Tracking Change in the Urban Environment
authors: Mackres, Eric; Shabou, Saif; Wong, Ted
date_published: 3/29/2023
article_type: Technical Note
sub_tag: Transport decarbonization
wri_primary_office: WRI Global
wri_programs: Cities
language: English
url: "https://www.wri.org/research/calculating-indicators-global-geospatial-datasets-urban-environment"
doi: "https://doi.org/10.46830/writn.22.00123"
summary: This technical note discusses methods for using these data in combination with locally meaningful jurisdictional boundaries to calculate local measurements of indicators on several themes—including access to urban amenities, air quality, biodiversity, flooding, climate change mitigation, heat, and land protection and restoration—relevant to urban decision-makers, researchers, and other stakeholders.
---

# Calculating Indicators From Global Geospatial Data Sets for Benchmarking and Tracking Change in the Urban Environment

TECHNICAL NOTE   |  Version 1.0  |  March 2023  |  1
CONTENTS
Abstract   .................................. 1
Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .2
General methods. . . . . . . . . . . . . . . . . . . . . . . . . .3
Indicator methods. . . . . . . . . . . . . . . . . . . . . . . . .5
General limitations ...................... 26
Further work . . . . . . . . . . . . . . . . . . . . . . . . . . . . .27
Endnotes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
References .............................. 29
Acknowledgments ...................... 35
About the authors. . . . . . . . . . . . . . . . . . . . . . . 35
Technical notes document the research or analytical 
methodology underpinning a publication, interactive 
application, or tool.
Suggested Citation: Mackres, E., S. Shabou, 
and T . Wong. 2023. “Calculating indicators from 
global geospatial data sets for benchmarking 
and tracking change in the urban environment.” 
Technical Note. Washington, DC: World Resources 
Institute. Available online at: doi.org/10.46830/
writn.22.00123.
TECHNICAL NOTE
Calculating indicators from global 
geospatial data sets for benchmarking and 
tracking change in the urban environment
Eric Mackres, Saif Shabou, and Theodore Wong
ABSTRACT 
Global data sets derived from remote sensing, urban sensors, crowdsourcing, 
or surveys can provide valuable insights on the current state of cities, how 
cities are changing, and opportunities to improve the urban environment. This 
technical note discusses methods for using these data in combination with 
locally meaningful jurisdictional boundaries to calculate local measurements 
of indicators on several themes—including access to urban amenities, air qual-
ity, biodiversity, flooding, climate change mitigation, heat, and land protection 
and restoration—relevant to urban decision-makers, researchers, and other 
stakeholders. These indicators were identified and prioritized in consulta-
tion with program staff and stakeholders from two global sustainable urban 
development initiatives: Cities4Forests and UrbanShift. Indicator calculations 
were also generated for cities of interest to these initiatives. These indicators 
can help urban policymakers and civil society assess differences within their 
cities; make comparisons with other cities; and measure themselves against 
national or global benchmarks, such as the Sustainable Development Goals, or 
against self-defined metrics. Geospatial analysis and zonal statistics methods 
are applied to existing published geospatial data sets and relevant administra-
tive, statistical, or physical city boundaries to calculate comparable indicators 
for any city or urban area. This methodology can be applied to any area of 
interest on Earth. Most indicators are based on open-source data, increasing 
the feasibility of repeating, replicating, and scaling the analyses at low mar-
ginal cost. Although the transferability and comparability of these methods are 
notable strengths of this approach, this note also discusses limitations of this 
approach for decision-making.

2  |  
  
INTRODUCTION
Global data sets derived from sources such as remote sensing, 
urban sensors, crowdsourcing, or surveys can provide valuable 
insights on the current state of cities, how cities are changing, 
differences among cities and among neighborhoods within 
cities, and opportunities for improvements to the urban environ-
ment (Prakash et al. 2020; Helmrich et al. 2021). However, these 
data are often inaccessible or not immediately relevant to urban 
stakeholders and decision-makers (Kalluri et al. 2003; Zerger 
and Smith 2003; Engel-Cox et al. 2004; Wellmann et al. 2020). 
Processing these data to produce indicators that provide local 
measurements of themes of interest to local stakeholders is a 
necessary, yet oftentimes missing, step to enable the supply of 
new data to meet the demand for locally relevant insights and 
responsive decision-making (Prakash et al. 2020; Wellmann et 
al. 2020). Additionally, these indicators can help urban policy-
makers and civil society assess differences within their cities; 
make comparisons with other cities; and measure themselves 
against national or global benchmarks, such as the Sustainable 
Development Goals (SDGs), or against self-defined metrics 
(Kuffer et al. 2018; Avtar et al. 2019; Kavvada et al. 2020; Wang 
et al. 2020; Giuliani et al. 2021; Song and Wu 2021). 
The past few years have seen the beginning of a revolution 
in remote sensing, crowdsourced data, cloud computing, and 
machine learning—technologies that are quickly generating new 
insights about Earth and its urban areas (Fritz et al. 2019; Kav-
vada et al. 2020; Niu and Silva 2020; Salcedo-Sanz et al. 2020; 
Ludwig et al. 2021). For the first time, researchers and citizen-
scientists have access to globally standardized, open-source, 
continually updated data sets and methods to help answer 
important questions about how we live and the impacts of our 
present and future activities, from the neighborhood scale to 
the continent scale. This also means that some information that 
had not been previously collected or made public through local 
methods (e.g., ground-based tree inventories) can be generated 
through alternative means, which are often cheaper and easier 
to implement over large areas (e.g., remote sensing–based tree 
cover mapping). Moreover, utilizing open-source data increases 
the feasibility of repeating, replicating, and scaling the analyses 
for additional cities or time frames at low marginal cost, which 
can be particularly helpful in data-scarce regions or on topics 
with limited local data available.
To help understand the status of development and sustain-
ability in cities and identify existing and potential challenges, 
this paper presents a consistent, replicable approach to calculate 
indicators on seven key themes: access to urban services and 
amenities (ACC), air quality (AQ), biodiversity (BIO), flooding 
(FLD), climate change mitigation (GHG), heat (HEA), and 
land protection and restoration (LND). Data to measure these 
indicators, as described in this document, are almost exclusively 
taken from global, open-source data sets. However, these meth-
ods can be customized by including equivalent local data sets. 
Indicators are calculated to assess the baselines and trends of 
change within each city on identified themes, providing infor-
mation to distinguish patterns within and between cities and 
helping to detect problems and define solutions (e.g., prioritiz-
ing neighborhoods with limited tree cover for a tree planting 
campaign). The methods are open source, so other researchers 
are also welcome to use the methods and scripts developed 
to process data and make calculations for other cities or with 
different input data. The results will be disseminated to local 
and national governments as well as to civil society stakeholders 
in the context of initiatives supported by WRI Ross Center for 
Sustainable Cities. 
So far, the indicators developed using this framework align with 
themes of interest to two city cohorts with which WRI Ross 
Center has been working. The two immediate pilot applica-
tions of the indicator methods described in this technical note 
are for cities participating in the Cities4Forests and Urban-
Shift initiatives.
 ▪ Cities4Forests1 supports city decision-makers in over 80 
cities in making commitments and taking action to preserve 
and expand tree cover within, near, and far away from 
their cities. Urban tree indicators can be used by forestry 
or other tree-focused staff in municipal governments to 
inform policies and programs related to forests and natural 
resource management. 
 ▪ UrbanShift2 supports city decision-makers across 23 cities 
on four continents to adopt integrated approaches to 
urban development, shaping zero-carbon, climate-resilient 
communities where both people and the planet can thrive. 
The initiative’s focus includes biodiversity, climate change, 
and land degradation, and we have developed indicators on 
these themes. We anticipate that city planning and other 
strategic sustainable urban investment-focused staff in 
municipal governments will use the indicators to inform 
policies, programs, and projects in UrbanShift cities. 
The themes prioritized and indicators calculated for the city 
cohorts convened by these initiatives were developed in con-
sultation with their staff and stakeholders. An iterative process 
involving meetings with and surveys of staff working directly

TECHNICAL NOTE   |  March 2023  |  3
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
with city stakeholders in 2022 (Cities4Forests account manag-
ers and UrbanShift regional coordinators) provided the main 
information used to identify the most important and relevant 
themes, define the indicators, and organize the presentation of 
the calculations for the cities. Indicator calculations and visual-
izations for these cities will be made publicly accessible through 
an online dashboard. 
We anticipate that these indicators, and others like them calcu-
lated using a similar framework, will be relevant to many other 
city cohorts and urban themes. Many indicators also align with 
global objectives, such as the urban targets of the SDGs (SDG 
11) (United Nations n.d.). We foresee additional uses of the 
indicators included in the technical note in other geographies 
and time frames and the development of supplemental indica-
tors on existing and new themes and using new data sources. 
Additionally, we expect to update the indicator calculation 
methodologies for these current city cohorts as new data cover-
ing additional years become available. 
Some cities may have more granular and detailed relevant data 
for measuring the themes of our indicators. However, even 
those cities can benefit from measurements that are standard-
ized globally, between cities, and over time; provide enhanced 
temporal resolution; and are available worldwide. Additionally, 
these indicators can provide a screening and prioritization tool. 
Global data will rarely, if ever, be more useful than local data 
for monitoring local dynamics, but such data sets can help 
users understand the main challenges faced locally and start 
conversations about addressing them. Even when the lower local 
accuracy levels of global data sets impede local usability, they can 
help generate the conversations needed to identify local con-
cerns and then identify better data. 
Other projects on various urban and nonurban topics have 
developed indicators using zonal statistics derived from global 
geospatial data sets (Bocher et al. 2018; Jing et al. 2019; 
Cochran et al. 2020; Kuffer et al. 2020; Sathyakumar et al. 2020; 
Boeing et al. 2022; Nicoletti et al. 2022). However, this publica-
tion presents the first method of this kind developed by WRI to 
include multiple urban themes and focus on the needs of specific 
city cohorts and their questions around urban change, opportu-
nities, and risks. 
GENERAL METHODS
To calculate the indicators, we use a general data management 
workflow that is consistently applied across all indicators. We 
also use methods to process specific data relevant to individual 
indicators. All indicators are assigned short name designa-
tions and are organized into themes, as shown in Figure 1. The 
definitions and methodologies for calculating the indicators in 
the seven themes below are described in detail in the following 
sections, which are organized and named by theme. 
 ▪ Access to urban services and amenities (ACC)
 ▪ Air quality (AQ)
 ▪ Biodiversity (BIO)
 ▪ Flooding (FLD)
 ▪ Climate change mitigation (GHG)
 ▪ Heat (HEA)
 ▪ Land protection and restoration (LND)
These themes and indicators are not intended to be exhaustive; 
rather, they are tailored to the needs of the specific initiatives 
for which they were originally developed. We anticipate add-
ing additional indicators under these themes and potentially 
adding additional themes as identified as important by cities or 
other stakeholders. All indicators are subject to limitations and 
uncertainty associated with their methods, as described specifi-
cally in each indicator section and generally in the “General 
limitations” section.
General data management workflow
Our general data workflow consists of three steps to process, 
standardize, calculate, and save data, as visualized in Figure 2.
 ▪ Step 1: Define boundaries. As our indicators consist of 
zonal statistics, which are statistical descriptive summaries of 
raster (or grid) data within vector (or polygon) boundaries, 
we must first define zones. We define zones based on locally 
relevant administrative boundaries. For each city, we define 
boundaries for two administrative levels: the overall area of 
interest (typically a municipality or a metropolitan area) and 
several subareas (typically multiple wards/districts within a 
municipality or multiple municipalities within a metropolitan 
area). The former represents the union into a single polygon 
of the multiple geographies of the latter. The source of these 
boundaries may be a polygon file or map received from the 
local government or obtained from a national statistical 
agency. If such a local data source is not easily accessed,

4  |  
  
Figure 1  |  Themes and indicators described in this document 
Source: WRI authors.
THEMES
INDICATORS
Access to 
urban services 
& amenities 
Air qualityB iodiversity Flooding Climate change 
mitigation Heat
Land 
protection and 
restoration
Recreational space 
per capita
Urban open space 
for public use
Proximity to public 
open space 
Proximity to 
tree cover 
Fine particulate 
matter exposure
High pollution 
days
Change in air 
pollutant 
emissions 
Natural areas
Change in number 
of arthropod 
species
Change in number 
of bird species
Change in number 
of vascular plant 
species 
Biodiversity in 
built-up areas 
(birds) 
Connectivity of 
natural lands
Exposure to 
coastal and river 
flooding
Vegetation cover 
in riparian zones
Vegetation cover 
in built areas
Impervious 
surfaces
Land near natural 
drainage
Extreme 
precipitation 
hazard
Vulnerability of 
steep slopes
Tree cover
Protection of Key 
Biodiversity Areas
Protected areas
Habitat types
 restored
Habitat areas 
restored 
Change in 
vegetation and 
water cover
Built-up Key 
Biodiversity Areas
Permeable areas
Land surface 
temperature
Built land without 
tree cover
Surface 
reflectivity 
Extreme heat 
hazard 
Climate change 
impact of trees
Greenhouse gas 
emissions
the boundaries may be obtained from a global database such 
as geoBoundaries (Runfola et al. 2020) or OpenStreetMap 
(OSM).3 Where multiple options are available, stakeholders 
are consulted when possible on the most appropriate 
boundaries to use. Even for indicators that use a time series 
of data and for regions where boundaries may have changed 
over time, we use only the most recent available boundaries 
for our calculations to hold the region of study constant. 
These boundaries for each area of interest are then saved as 
GeoJSON files with a standard naming schema. 
 ▪ Step 2: Extract citywide data layers. The defined boundary 
extents are used to extract the data for each city area of 
interest from global data sets relevant to calculating one or 
more indicator. These extracted data are saved with respect to 
defined schemas and are stored as GeoTIFF or GeoJSON 
files depending on the data type: raster or vector, respectively. 
Metadata for each data source and extracted subset are also 
stored as a JSON file. 
 ▪ Step 3: Calculate the final indicators. For each zone 
defined in Step 1, we run spatial statistic calculations on 
the data layers, as extracted in Step 2, in keeping with the 
methods for each specific indicator. For all indicators, we 
use weighted reduction calculations (using only the portions 
of pixels that fall within the area of interest) to calculate 
these zonal statistics, primarily using reduction functions 
from Google Earth Engine (GEE 2021). We then store 
the indicator value for each geographic zone in a table 
aggregated by indicator with respect to a common schema. 
Next, we produce a final aggregated table with all indicators 
for all zones relevant to a city cohort. This table can then be 
used for further statistical analysis, joined with a polygon 
file of boundaries to produce a map, or integrated into 
visualization software.

TECHNICAL NOTE   |  March 2023  |  5
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
Figure 2  |  General data management workflow 
Notes: The figure describes the steps applied to generate calculations for each city, data source, and indicator. Boundaries are used to extract a spatial subset layer from the source data 
set that is relevant to the city. This subset is stored, and its metadata is added to a data catalog. The indicator methods are applied to the spatial subset, and the calculation result for 
each boundary is appended to a table that stores the unique indicator results for each boundary.
Source: WRI authors.
INPUT COMPUTE
Global data
Cities boundaries
VISUALIZE
Extract layers 
based on cities’ 
boundaries
Store extracted
layers data
Compute 
indicators
Store computed
indicators
Catalog
Dashboard
Data catalog
Catalog layers
Scripts to implement these methods are saved in code reposito-
ries on GitHub.4 
Selection of relevant input data sets 
For several indicators, multiple potential source data sets could 
be used. To select the data sets for use in our indicators, we 
followed a few general principles. We typically chose the data 
set that met the greatest number of our criteria. In cases where 
there were trade-offs between multiple criteria, we prioritized 
the criteria that were most important to enable consistent and 
meaningful calculations of the specific indicator. The following 
criteria were used to evaluate data sets:
 ▪ Published in a peer-reviewed source
 ▪ Open-source license
 ▪ Globally consistent coverage
 ▪ Recency of data
 ▪ High spatial resolution
 ▪ High accuracy compared to peer data
 ▪ Broad temporal coverage (multiple years of data to enable 
time series comparisons)
 ▪ Likelihood of ongoing support for the source data initiative 
and future updates to the data set, enabling updates to the 
indicators and tracking over time
 ▪ Compatible spatial and temporal resolution with other data 
sets used for the indicator
INDICATOR METHODS
Access to urban services and 
amenities (ACC)
Cities exist because the physical proximity of many kinds of 
activities enables residents to more easily access opportunities 
and collaborate economically. But access to opportunities varies 
considerably within cities. These indicators measure the variation 
in physical access to services and amenities within cities.

6  |  
  
ACC-1: Recreational space per capita
DEFINITION
The hectares of recreational space (open space for public use) 
per 1,000 people.
IMPORTANCE
Parks, natural areas, and other open spaces provide city residents 
with important recreational, spiritual, cultural, and educational 
services. The use of open and green spaces has been shown to 
improve human physical and psychological health (Pietilä et al. 
2015; Litwiller et al. 2016).
METHODS
The recreational services indicator is calculated as
Data on recreational areas were taken from the crowdsourced 
data initiative OSM using the Geemap Python library (Geemap 
n.d.). The OSM tags used to retrieve polygons of these areas 
are park, nature_reserve, common, playground, pitch, and track 
in the leisure category and protected_area and national_park 
in the boundary category. Population data are 2020 estimates 
from WorldPop accessed through Google Earth Engine 
(WorldPop n.d.). 
LIMITATIONS
There is uncertainty in the population estimates, especially the 
distribution of population within enumeration areas. Analysis 
of these WorldPop data for Namibia have found large cell-level 
errors, particularly in areas of informal settlements (Thom-
son et al. 2022).
ACC-2: Urban open space for public use
DEFINITION
The percentage of built-up area that is open space for public use.
IMPORTANCE
The availability and area of public open space, such as 
parks, are key factors for assessing the quality of life for city 
residents. Open spaces provide ecosystem services, recreation 
opportunities, and habitat for wildlife. Indicators of open 
space are included in the SDGs (Indicator 11.7.1 [UN-
Habitat 2020]) and the Singapore Index on Cities’ Biodiversity 
(Chan et al. 2021).
total area of recreational space within the boundary
population within the boundary ÷ 1,000
METHODS
This indicator uses polygon data on categories of open space as 
retrieved from OSM in August 2022 using the Geemap Python 
library (Geemap n.d.). The OSM tags used to retrieve these 
areas are park, nature_reserve, common, playground, pitch, and 
track in the leisure category and protected_area and national_park 
in the boundary category. For this indicator, we focus on open 
space that is within urbanized areas of the city and therefore 
more easily accessible by a greater population. This is distinct 
from ACC-1, which considers all public open space within 
the jurisdictional boundary, including in nonurbanized areas. 
To constrain our analysis to urbanized or built areas of the city 
(areas where land is predominantly covered by urban infrastruc-
ture, such as buildings and streets, and where most people live 
and work), we use data on these areas as derived from the 2020 
European Space Agency (ESA) WorldCover data set’s “built-
up” class5 (ESA 2020a; Zanaga et al. 2021). Status as open space 
or non–open space for each 10-meter (m) pixel of built land is 
derived using the built-up class as a mask to constrain the analy-
sis to only urbanized areas. Finally, the count of masked pixels of 
open space divided by the count of all masked pixels is used to 
calculate the percentage of built area that is open space.
LIMITATIONS
Because of the relatively high (10 m) resolution of the World-
Cover data set and its definition of built-up areas, large- and 
medium-sized urban open spaces that are predominantly green 
areas will be excluded. As a result, this indicator best captures 
smaller open spaces, such as pocket parks; open spaces that are 
not predominantly green, such as plazas; and designated parks 
that are a mix of built-up and nonbuilt land, such as historic 
districts. This indicator is a candidate for future revision to use 
an alternative urbanized area mask based on a data set that 
provides a common, global definition of urbanized areas of cities 
that is less restrictive of green open spaces. From our assessment, 
a global data set meeting this description is not yet available. 
OSM is a crowdsourced data set with a diverse user commu-
nity, and its completeness, accuracy, and standards of use vary 
considerably. Accuracy within individual studied cities is not 
precisely known. Some regions lack data on some of their open 
spaces in OSM, but all cities we have analyzed so far have data 
on the sites of at least some open spaces. Additionally, use of 
the OSM taxonomic system of tags to categorize features is 
used differently by different local contributing communities. In 
selecting the tags used in our methods, we considered the most 
commonly used tags to designate open spaces available for pub-

TECHNICAL NOTE   |  March 2023  |  7
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
lic use (parks, athletic fields, etc.) but attempted to exclude tags 
used primarily for private, limited access or indeterminate open 
spaces. However, as the OSM tagging system is not designed 
to make this distinction, this may result in the exclusion of data 
on some open spaces that are available for public use as well as 
inclusion of some nonpublic open spaces for some cities. OSM 
is being constantly edited, potentially improving the relevant 
data for these cities, so our download of data from one point in 
time may become outdated. Finally, metadata for OSM features 
(parks, roads, etc.) include when the feature was added or edited 
in the map but typically do not provide information on when it 
was installed on the ground. This makes it difficult to measure 
changes to cities over time using OSM data. 
ACC-3: Proximity to public open space
DEFINITION
The percentage of the population within walking distance (400 
m) of public open space. 
IMPORTANCE
Beyond simply being present, open space must also be easy to 
access. Although accessibility has many elements, physical prox-
imity to open spaces is an important factor affecting who does 
or does not have access. The spatial distribution of open spaces 
across a city, their alignment with population locations, and their 
accessibility within walking distance (commonly defined at 400 
m, including in the Singapore Index [Chan et al. 2021]) are all 
critical factors for understanding how many city residents are 
well served by open space.
METHODS
This indicator makes use of gridded population at 100 m 
resolution from the WorldPop project as accessed on Google 
Earth Engine (University of Southampton n.d.). The open 
space polygons retrieved from OSM are buffered by 400 m to 
derive recreation catchment areas. The population within those 
recreation catchment areas is calculated and then converted to a 
percentage by dividing that value by the total population of the 
area of interest.
LIMITATIONS
The limitations of OSM data previously described are also rel-
evant to this indicator. Additionally, our approach for calculating 
access to open space relies on Euclidean distance for simplicity. 
However, this straight-line measurement is not an accurate 
characterization of how people travel within cities; it does not 
account for the orientation of streets or barriers to pedestrian 
travel. Because of this reality on the ground, in most cases real 
pedestrian travel of 400 m will enable access to a smaller area 
than our methods present.
ACC-4: Proximity to tree cover
DEFINITION
The percentage of the population with an average tree cover 
of greater than 10 percent within walking distance (400 m) 
of their homes.
IMPORTANCE
Proximity to tree cover is an important indicator of quality green 
space, whether the trees are in public or private space. Privately 
maintained trees also provide a variety of public benefits, includ-
ing improved air quality, heat mitigation, and shade. In addition 
to providing a range of ecosystem services, urban forests are 
increasingly recognized for their socioeconomic benefits (Kondo 
et al. 2017; Martinuzzi et al. 2018, 2021; Volin et al. 2020). 
This indicator considers all trees within walking distance (400 
m) for each resident of the city as a measure of the quality of 
green space that they interact with during an average day. It also 
distinguishes between populations with and without walkable 
access to an average tree cover greater than 10 percent, which is 
the threshold used by the Food and Agriculture Organization of 
the United Nations and in SDG 15.1.1 as part of the definition 
of forest (UN-Habitat 2022).
METHODS
This indicator uses 10 m resolution tree cover data for the year 
2020 from the Trees in Mosaic Landscapes data set 6 (Brandt 
et al. 2022), which gives tree extent within each 10 m pixel. It 
also applies the gridded population for 2020 at 100 m resolu-
tion from the WorldPop project as retrieved from Google Earth 
Engine. A neighborhood reduction method using a circular 
kernel of 400 m radius is applied to the tree cover layer to 
calculate the mean percentage tree cover within 400 m of each 
10 m pixel within the area of interest. This result is then used 
to mask the population layer to only include 100 m population 
pixels (or a portion thereof ) with an average of greater than 10 
percent tree cover within 400 m. The population of this 100 m 
masked population layer is calculated and then converted to a 
percentage by dividing that value by the total population of the 
area of interest.

8  |  
  
LIMITATIONS
The limitations previously described related to the use of 
Euclidean distance are also relevant to this indicator. 
The limitations of Brandt et al. (2022) mean that certain cities 
may have missing tree cover data due to a lack of cloud-free 
imagery for 2020 or a lack of valid Sentinel-1 radar imagery, 
which can happen at the borders of satellite orbits and is com-
mon in coastal cities. Cloud removal algorithms used to generate 
tree cover data sets often have a high quantity of false negatives 
in cities (pixels that look like buildings but are, in fact, clouds) 
because clouds and buildings share bright reflectance values. The 
persistence of cloudy images means that most tree cover data 
sets underestimate trees in cities because these false negative 
clouds hide trees in some of the pixels. Brandt et al. (2022) 
employ a more aggressive approach to cloud removal in cities, 
resulting in fewer false negatives but less available data. In this 
data set, trees are defined as woody vegetation with a height of 
more than 5 m, or woody vegetation with a height of more than 
3 m having a defined crown with at least a 5 m diameter. This 
data set properly excludes nontree crops that may be taller than 
3 or 5 m, such as tea, sugar, banana, and cacti, but currently it 
does not disambiguate plantation trees from nonplantation trees. 
At present, this data set is only available for 2020 and is limited 
to countries located within the tropics. In the tropics, the data 
set was found to have 97 percent user accuracy and 96 percent 
producer accuracy. Additional limitations and uncertainty 
related to the tree cover data set is described in the methods 
paper for Trees in Mosaic Landscapes (Brandt et al. 2022).
Air quality (AQ)
Air quality is a major factor in the physical health of urban 
residents. Cities both produce air pollution and are impacted 
by pollution. These indicators measure city contributions to air 
pollution and resident exposure to pollution. 
AQ-1: Air pollutant emissions and their costs
DEFINITION
The percentage change in annual air pollutant emissions from 
city areas (tonnes) and related social costs (in U.S. dollars), 
disaggregated by pollutant and sector, between 2000 and 2020.
IMPORTANCE
Human activity contributes to air pollution and climate change 
through greenhouse gas emissions from fuel combustion, 
industrial processes, and agriculture. This pollution imposes 
social costs through its negative impacts on human health and 
economic productivity. This indicator can help decision-makers 
and stakeholders identify the most important pollutants emitted 
locally, the activities responsible for the emissions, and, with 
multiple years of data, understand emissions trends over time.
METHODS
This indicator is based on the Global Anthropogenic Emissions 
data set of the Copernicus Atmosphere Monitoring Service 
(CAMS) and the Emissions of atmospheric Compounds and 
Compilation of Ancillary Data (ECCAD) (Granier et al. 
2019).7 The data set provides annual estimates of emissions from 
12 sectors of human activity, on a 0.1-degree (approximately 11 
kilometers [km]) spatial resolution. The estimates are based on 
simulations and historical data and are updated intermittently. 
The included sectors are agriculture (livestock); agriculture 
(soils); agriculture (waste burning); power generation; fugitive 
emissions; industry; combustion in residential, commercial, and 
other settings; ships; solvents; solid waste and wastewater; off-
road transportation; and on-road transportation.
We use Google Earth Engine to calculate the emissions from 
within our areas of interest (city administrative boundaries). We 
extract annual, sector-disaggregated emissions in tonnes per year 
for 2000 and 2020 for each of the health-related pollutant spe-
cies available in the data set: black carbon (BC), methane (CH4), 
carbon monoxide (CO), nitrogen oxides (NOx), sulfur dioxide 
(SO2), organic carbon (OC) compounds, ammonia (NH3), and 
non-methane volatile organic compounds (NMVOCs). Because 
of the coarse resolution of this data set, we only report values for 
the geographic area of the full city and not for each subcity area. 
To combine the emissions of multiple pollutant species to 
generate a meaningful summary value, we convert tonnes to U.S. 
dollars based on health-related social costs per tonne (Table 
1) as estimated by Shindell (2015) for all pollutant species 
except NMVOCs. For the social cost of NMVOCs, we used 
the median value for NMVOCs emitted below an elevation of 
100 m in van der Kamp (2017). Van der Kamp’s estimates are 
in 2015€, which we converted to 2015$ at €1 = US$1.11. To 
produce a summary number for the final indicator, we share the 
percentage change in social costs from 2000 to 2020. 
LIMITATIONS
The emissions data used for this indicator only account for 
direct emissions from activities within the boundaries of the city 
(Scope 1 type emissions). This data does not account for emis-
sions associated with electricity used in the city but generated 
elsewhere (Scope 2) or emissions produced elsewhere associated

TECHNICAL NOTE   |  March 2023  |  9
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
with products or services consumed in the city (Scope 3), such 
as air pollution from fires in formerly forested areas cleared to 
produce agricultural commodities consumed in cities, including 
beef and palm oil. Additionally, this analysis does not provide 
information on where the social cost of these emissions accrues. 
Because pollution travels and most costs are associated with 
pollution exposure, not emissions, many of the costs associated 
with pollution from the city may be experienced outside the 
city. The CAMS data set is modeled data based on an ensemble 
of multiple emissions models and is subject to the limitation of 
those models. The methods used to develop the CAMS emis-
sions data set are described in Granier et al. (2019).
AQ-2: High pollution days
DEFINITION
The annual number of days that air pollutants were above World 
Health Organization (WHO) air quality standards in 2020.
IMPORTANCE
Exposure to high concentrations of air pollutants increases the 
probability of developing serious health conditions, reduced lung 
function, increased susceptibility to respiratory infections, and 
aggravated asthma. Long-term exposure increases the probabil-
ity of developing chronic conditions such as stroke susceptibility, 
heart disease, and cancer (Kampa and Castanas 2008; Lee et 
al. 2018). This indicator can help public health officials deter-
mine which air pollutants are present at levels dangerous to 
human health and how many days each year the population is 
exposed to them.
METHODS
The data used for this indicator come from the CAMS Global 
Reanalysis EAC4 data set (Inness et al. 2019), which combines 
satellite monitoring of pollutant concentrations with atmo-
spheric modeling to estimate concentrations near the earth’s 
surface.8 The EAC4 data are provided at approximately 80 km 
spatial resolution. Because of the coarse resolution of this data 
set, we only report value for the geographic area of the full city 
and not for each subcity area.
We report the number of days each city was estimated in 2020 
to have a near-surface concentration of air pollutants that 
exceeds WHO’s standards for outdoor air pollutants (WHO 
2021). Table 2 outlines the pollutants and standards used. 
LIMITATIONS
The CAMS data has uncertainty related to the limitations of 
the atmospheric modeling methods used. Additionally, the 
low resolution of the data set does not allow for analysis of 
Table 1  |  Estimated social cost for major pollutant species
POLLUTANT SPECIES SOCIAL COST PER TONNE (US$)
Black carbon (BC) 62,000a
Methane (CH4) 740a
Carbon monoxide (CO) 250a
Carbon dioxide (CO2) 0a
Nitrogen oxides (NO x) 67,000a 
Sulfur dioxide (SO2) 33,000a 
Organic carbon (OC) 51,000a
Ammonia (NH3) 22,000a 
Non-methane volatile organic 
compounds (NMVOCs) 1,172b
Sources:   a. Nonclimate health-related costs estimated in Shindell (2015); b. Median cost 
across four German regions for emissions below 100 meters, as estimated in van der 
Kamp (2017).
Table 2  |  WHO standards for outdoor air pollutants 
POLLUTANT 
SPECIES
AVERAGING 
TIME (HOURS) a
WHO-RECOMMENDED AIR QUALITY 
GUIDELINE MAXIMUM LEVEL c
Nitrogen dioxide 
(NO2) 24 25 µg/m3 
Sulfur dioxide 
(SO2) 24 40 µg/m3 
Ozone (O3) 8b 100 µg/m3 
Carbon 
monoxide (CO) 24 4,000 µg/m3 
Fine particulate 
matter (PM2.5) 24 15 µg/m3 
Coarse 
particulate 
matter (PM10)
24 45 µg/m3 
Notes:  a. The World Health Organization provides additional guidelines for the 
same pollutants for other averaging times; b. Due to limitations with the Copernicus 
Atmosphere Monitoring Service data set, for the ozone calculations we used data for the 
nine-hour window of 6 AM–3 PM. In some parts of the world, the highest level of ozone 
is reached after 5 PM; c. Pollutant concentrations are given as micrograms per cubic 
meter (µg/m 3)
Source: WHO 2021.

10  |  
  
subcity geographic units and may introduce uncertainty to 
the city-scale calculations due to aggregated data from an area 
larger than the city.
AQ-3: Fine particulate matter exposure
DEFINITION
The annual mean fine particulate matter (PM2.5) concentra-
tion as a percentage of WHO’s air quality guideline for 
annual exposure.
IMPORTANCE
PM2.5 consists of very small particles that are smaller than 
2.5 micrometers (µm) in diameter. (For comparison, a typical 
human hair has a diameter of 50–70 µm.) PM2.5 is released from 
combustion (including fuel combustion in vehicles and power 
plants, the use of wood and other biomass for cooking and 
heating, as well as wildfires), degradation of vehicle tires during 
use, and some chemical processes that occur in the atmosphere. 
PM2.5 is a serious health concern because the small size allows 
PM2.5 particles to travel deep into human lungs, enter the blood-
stream, and cause direct damage to internal organs. Long-term 
exposure to PM2.5 leads to increased incidence of heart and lung 
diseases, cancers, and premature death (Feng et al. 2016; WHO 
2021). This indicator can help decision-makers determine how 
many city residents face long-term exposure to dangerous levels 
of PM2.5 and in which neighborhoods these residents live.
METHODS
This indicator uses the global surface PM2.5 V5.GL.02 data 
set from the Atmospheric Composition Analysis Group at 
Washington University (van Donkelaar et al. 2021).9 This data 
set combines models of atmospheric mixing and chemistry with 
analysis of imagery from the Moderate Resolution Imaging 
Spectroradiometer, Multi-angle Imaging SpectroRadiometer, 
and Sea-viewing Wide Field-of-view Sensor satellite instru-
ments from the National Aeronautics and Space Administration 
(NASA) to generate estimates of PM2.5 concentrations near the 
earth’s surface. The data are provided at a spatial resolution of 
0.01 degrees, or approximately 1.1 km. Our indicator is based on 
annual average concentrations for 2020.
We report each district’s 2020 average PM2.5 concentration as 
a percentage of WHO’s air quality guideline (recommended 
maximum level) for annual exposure: 5 µg per cubic meter (m3) 
(WHO 2021). The annual average is calculated spatially over the 
area of the district. For example, an average concentration of 15 
µg/m3 would be reported as 300 percent of the WHO standard. 
This indicator is based on the WHO annual average concentra-
tion recommendation for PM2.5, as distinct from the WHO 
24-hour average recommendation used in indicator AQ-2. 
LIMITATIONS
The PM2.5 data set has uncertainty related to the limitations of 
the atmospheric modeling methods that it uses. The concentra-
tion levels we report cannot be directly translated into health 
impacts. The health impacts of air pollution are not linearly 
related to pollutant concentrations, so although higher con-
centrations are worse for health, concentrations at, for example, 
300 percent of the WHO standard should not be interpreted as 
three times worse than concentrations at 100 percent. 
Biodiversity (BIO)
Cities are often thought of as detrimental to biodiversity—and 
they can have significant negative impacts related to habitat loss 
and resource extraction—but cities can also make choices that 
mitigate biodiversity loss and enhance habitat. 
Most of the indicator methods in this category are based on 
the indicator definitions used in the Singapore Index on Cities’ 
Biodiversity (Chan et al. 2021). The Singapore Index is a widely 
recognized assessment framework designed to help assess and 
track biodiversity and its protection within cities. The entire 
Singapore Index encompasses assessment of biodiversity, access 
to the societal benefits of biodiversity, and government struc-
tures and processes supporting biodiversity. It can be used to 
assess the status of local biodiversity and the conditions that 
support it as well as to identify priority areas for future urban 
biodiversity efforts.
The Singapore Index defines indicators and a scoring method, 
and cities are invited to adapt the indicators and definitions 
for their own purposes. It does not provide data for calculating 
indicator values, and data acquisition and processing can make 
it difficult for cities to use the Singapore Index. We provide 
data supporting a subset of the Singapore Index’s indicators 
that address biodiversity and access to benefits. Some of the 
biodiversity indicators do not measure biodiversity directly but 
rather conditions that support or harm biodiversity. We have 
defined and implemented our indicators to adhere as closely as 
possible to the definitions in the Singapore Index. Our approach 
prioritizes global, publicly available, and peer-reviewed data sets 
to develop indicators; however, cities often have access to local 
data that are of higher quality or are more specifically suited to 
local contexts and needs.

TECHNICAL NOTE   |  March 2023  |  11
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
BIO-1: Natural Areas
DEFINITION
The percentage of land that is within natural area land classes.
IMPORTANCE
Natural areas support biodiversity by providing habitat. They 
also provide human beings with ecosystem services. The portion 
of the total city area that is close to a natural state thus provides 
information about a city’s biodiversity and about the benefits 
provided by biodiversity.
METHODS
Natural ecosystems, as defined by the Singapore Index, are all 
areas that are natural and not highly disturbed or completely 
human-altered landscapes. Examples of natural ecosystems 
include forests, mangroves, freshwater swamps, natural grass-
lands, streams, and lakes. Parks, golf courses, cropland, and 
roadside plantings are not considered natural. This indicator is 
calculated as the percentage of natural area within the 
city boundary:
We calculated this indicator using the ESA WorldCover 10 m 
2020 V100 land-classification map (Zanaga et al. 2021). We 
included as natural area all land classified in this data set as 
trees, shrubland, grassland, herbaceous wetland, mangrove, or 
moss and lichen.
LIMITATIONS
 ▪ The 2020 WorldCover layer was assessed to have overall 
accuracy of 74.4 percent (Tsendbazar et al. 2021); this means 
it includes errors in land cover classification, and these errors 
are carried through to our characterization of natural and 
nonnatural lands. 
 ▪ The WorldCover data set has a spatial resolution of 10 m. 
For some wildlife species, patches smaller than 10 m might 
provide useful habitat. WorldCover and our implementation 
of this indicator could fail to account for these tiny patches.
 ▪ Some species have requirements with respect to habitat 
patch size, plant-community composition, level of vegetation 
homogeneity, and composition of nearby land. Our 
method accounts for none of these (or other) potentially 
important ecological details. Biodiversity planning that 
total area of natural, restored, and naturalized areas
area of city
x 100%
prioritizes particular species or that is informed by a locally 
implemented ecological assessment should contemplate 
augmenting our indicators with local ground truthing and 
habitat classifications defined by local species’ requirements.
BIO-2: Connectivity of natural lands
DEFINITION
Landscape coherence is a measure of the connectivity of patches 
of land that can serve as habitat for wild animals. Coher-
ence values range from zero to one, with larger coherence 
values indicating greater ease of animal movement between 
habitat patches.
IMPORTANCE
In general, contiguous habitat benefits biodiversity better than 
habitat that is subdivided by roads, buildings, and other built 
infrastructure (Forman and Godron 1991; Fahrig 2003). The 
connectivity of habitat patches mitigates the effects of habitat 
fragmentation by allowing wildlife to access more habitat 
without having to cross inhospitable terrain. The fragmentation 
of natural areas affects different species differently. For example, 
a road might not be a barrier for birds, but it can seriously frag-
ment a population of arboreal primates. Although consideration 
of dispersal ability and habitat requirements are important in the 
management of particular species, the Singapore Index adopts a 
generalist approach to quantifying connectivity based purely on 
patch geometry.
PLAIN-LANGUAGE CONCEPTUAL DEFINITIONS
Natural area is land that is hospitable to wild animals. Because 
animal species differ in their habitat requirements, the concept 
of natural area is necessarily nonspecific and is taken by the 
Singapore Index and by us to encompass natural, near-natural, 
and other lands that are relatively undisturbed by human activity.
Connected natural area patches are patches that are at most 
100 m separated from each other at their nearest points. Most 
animals can move from one habitat patch to another, crossing 
some distance of inhospitable land. Animal species differ in their 
movement behaviors and their tolerance of nonhabitat environ-
ments, so the Singapore Index uses a generally useful distance 
to define patch isolation. The 100 m threshold was chosen by a 
consensus of expert advisers to the development of the corre-
sponding indicator in the Singapore Index.

12  |  
  
The indicator is defined as coherence, which is a landscape 
measure of natural area connectivity. Coherence is the probabil-
ity that any two randomly selected points in a city’s natural areas 
will be located in the same contiguous natural area patch, or net-
work of connected patches. If the two random points represent 
the locations of two animals of the same species, the coherence 
models the probability that they encounter one another. Coher-
ence is the sum of the squared areas of each natural area patch, 
divided by the squared total natural area. (The areas of patches 
that are connected to each other are summed and treated as a 
single patch.) Maximum coherence would indicate a landscape 
in which all natural area exists as a single contiguous (or con-
nected) patch: coherence would be unity. A landscape in which 
natural area is subdivided into many isolated patches would have 
coherence between zero and unity.
METHODS
We calculated this indicator using the ESA WorldCover 10 m 
2020 V100 land-classification map (Zanaga et al. 2021). We 
included as natural area all land classified as trees, shrubland, 
grassland, herbaceous wetland, mangrove, or moss and lichen.
The indicator is the coherence
where Atotal is the total area of all natural areas; AG1 to AGn are 
the sizes of each group of connected patches of natural area that 
are distinct from each other; and n is the total number of groups 
of connected patches of natural area. AG1 to AGn to may consist 
of areas that are the sum of two or more smaller patches that are 
connected. In general, patches are considered to be connected if 
they are less than 100 m apart. This equation was derived from 
Deslauriers et al. (2018).
LIMITATIONS
 ▪ This indicator shares the limitations of BIO-1, which stem 
from unavoidable errors in land classification.
 ▪ This indicator does not currently address roadways as 
particular dangers to animals, despite the well-documented 
role vehicle collisions play in harming wildlife (Sugiarto 
2022). We would like to integrate roadway information into 
our implementation of future versions of this indicator.
 ▪ We consider two habitat patches to be connected if they are 
no more than 100 m apart. The 100 m threshold is taken 
from the definition of the corresponding indicator in the 
Singapore Index, but its appearance there does not suggest 
any universal applicability to all types of animal movement. 
 (       +       + ... +       )A 
2
G1 A 
2
G2 A 
2
GnCoherence =    1   
A 
2
total
Some flying animals are likely to tolerate greater distances, 
and some small animals (especially amphibians) cannot 
traverse 100 m of, say, pavement. Biodiversity planning 
that prioritizes particular animals for protection should 
contemplate implementing this indicator using a distance 
threshold that accounts for the particular movement behavior 
and physiological tolerances of the species of interest.
BIO-3: Biodiversity in built-up areas (birds)
DEFINITION
The percentage of bird species in all areas that were also 
observed in built-up areas.
IMPORTANCE
Cities often include large amounts of built-up and denuded 
land. These areas are not typically thought of as high-quality 
habitat, but they can support some species. This indicator reflects 
the ability of built-up areas to support biodiversity, using birds 
as an indicator group. Built-up areas include impermeable 
surfaces such as buildings, roads, and drainage channels as well 
as anthropogenic green spaces such as roof gardens, roadside 
plantings, golf courses, private gardens, cemeteries, lawns, 
and urban parks.
METHODS
The indicator is calculated as
To delineate built-up areas, we used the ESA WorldCover 2020 
classification of built-up land (Zanaga et al. 2021). For the 
number of bird species, we estimated the saturation levels of 
species-area curves as described for indicators BIO-4, BIO-
5, and BIO-6, using research-grade observations of birds in 
2016–21 in the crowdsourced iNaturalist database, accessed 
through the Global Biodiversity Information Facility (GBIF 
2022b). Calculations are made using only the observations that 
occurred on built-up land and using all observations within 
city boundaries. We report the built-up estimate divided by the 
all-city estimate. 
number of bird species observed in built-up areas
number of bird species observed in all areas of city

TECHNICAL NOTE   |  March 2023  |  13
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
LIMITATIONS 
This method shares the limitations of BIO-4, BIO-5, and BIO-
6, as well as the following:
 ▪ The WorldCover data set’s built-up classification is subject 
to error due both to automated data processing and to 
resolution issues.
 ▪ All estimates include unavoidable errors. This indicator is 
calculated from two estimates, and so the potential error is 
greater. When nearly the entire city or district is built up, the 
estimated species count on built-up land will be very similar 
to the citywide estimate, and the indicator value will be close 
to one. Occasionally, the calculated value is greater than one 
because of errors introduced by the methods used to produce 
the numerator, the denominator, or both. In these cases, 
because values greater than one are impossible, we report 
the value as one.
BIO-4–6: Change in number of vascular plant, 
bird, and arthropod species 
DEFINITION
The estimated change in the number of vascular plant, bird, and 
arthropod species, 2021–24.
IMPORTANCE
Direct measurement of biodiversity is important, but it would be 
impossible to directly assess the diversity and health of all wild 
populations in a city. We therefore provide species-richness data 
for the three indicator taxa chosen by the Singapore Index as 
proxies for overall biodiversity: vascular plants, birds, and arthro-
pods. The change in species richness for these major groups is 
likely to be directly associated with changes in general habitat 
quality and in overall biodiversity.
 ▪ Vascular plants are plants with vascular tissues, which 
conduct water, minerals, and the products of photosynthesis 
throughout the plant. In contrast to nonvascular plants 
(for example, mosses), vascular plants can grow tall and 
in locations with little moisture on the surface of the 
soil. Vascular plants include more than 90 percent of the 
earth’s vegetation.
 ▪ Birds are one of the most visible species groups in urban 
areas, and they are often considered as a key indicator of 
environmental quality. They are well studied by professional 
and amateur naturalists worldwide, are sensitive to 
environmental and habitat changes, and are comparatively 
easy to observe and count. The Singapore Index includes the 
change in the number of bird species over time.
 ▪ Arthropods include insects, spiders, crustaceans, and other 
animals with exoskeletons and jointed limbs. They are 
important actors in terrestrial ecosystems, driving critical 
processes such as pollination, food-web relations, and 
nutrient cycling. Many are highly sensitive to changes in 
their physical and ecological environments.
The Singapore Index recommends reporting the number of 
native species in each of these groups in regular time intervals. 
A local data collection process would typically involve partner-
ing with a local research institution to carry out a species survey. 
This survey would be repeated every few years; the indicator 
is the change in time from a baseline level to the current year. 
Here, we provide species counts estimated from crowdsourced 
species-occurrence data sets. Our method cannot substitute 
for on-the-ground species surveys. We intend it to provide 
rough estimates that can be used in the absence of more 
intensive efforts.
METHOD FOR ESTIMATING SPECIES NUMBER
Biologists often interpret species survey data by examining the 
number of species found as a function of effort, plotted as a 
species accumulation curve (SAC). The SAC plots the cumula-
tive number of species recorded as a function of sampling effort 
(i.e., number of individuals collected or cumulative number of 
samples). At the start of a species survey, the total number of 
species found typically grows quickly with every unit of effort. 
After some time, however, effort expended yields more and more 
species that have already been found earlier in the survey—and 
the total number of species grows more slowly per unit of effort. 
A plot of species number versus effort will come to a plateau, 
and this saturation level is a common estimator for the number 
of species in an area, as shown in Figure 3.
We estimated species richness by estimating the saturation level 
of SACs using individual crowdsourced observations as our 
effort unit. The estimated counts are the mean saturation levels 
of 100 SACs, each generated by randomizing the order of all 
research-grade iNaturalist observations of the Aves (birds), Tra-
cheophyta (vascular plants), and Arthropoda (arthropods) taxa 
(GBIF 2022a, 2022b, 2022c) in 2016–21. Only species observa-
tions with enough data to generate SACs are considered for 
estimating species richness. Although using just one year of 
observations might have allowed us to associate species count 
estimates with particular years, observation data in most cities 
were insufficient when we limited our method to single-year 
data. We thus combined data over six years to increase the 
number of cities for which we could report estimates.

14  |  
  
METHOD FOR ESTIMATING CHANGE IN SPECIES NUMBER
The Singapore Index Indicators 4–6 require calculation of 
changes in species number. At publication time, we have calcu-
lated only the baseline species numbers based on iNaturalist data 
for 2016–21. In a future year, likely 2025, we will estimate species 
numbers again and report change as an absolute change: 
We will use the curve-fitting method described above to esti-
mate countnew, but with more recent observation data. For each 
estimate in 2025, we will use the same number of observations 
as was used in the corresponding baseline estimate. For example, 
if the baseline arthropod count estimate for some location was 
based on 830 observations taken from 2016–21, then we will use 
830 observations to estimate the updated arthropod count. We 
will begin with the iNaturalist observations for the most recent 
full year, which will be 2024. If the number of observations is 
less than the number of observations needed, then we will look 
to 2023. For each year that we do not reach the target observa-
tion number, we will look to the previous year. In the year for 
which the observations become too many if we use the entire 
set of that year’s observations, we will instead use the number of 
change = countnew – countbaseline
observations needed, chosen randomly from that year’s observa-
tions. Because citizen-scientist contributions to iNaturalist have 
increased over time, we are hopeful that we will be able to match 
the observation numbers used for the baseline estimate with 
fewer than six years of observations.
LIMITATIONS 
We use the SAC curve-fitting approach because it is impossible 
to conduct an exhaustive survey of all species present even in the 
indicator taxa. However, our reliance on crowdsourced species 
observations introduces serious limitations.
 ▪ Citizen-scientist observations do not benefit from deliberate 
spatial sampling techniques. One consequence is that 
the observations that inform our calculations tend to be 
clustered in heavily populated areas and popular recreational 
sites. We are therefore likely to miss species that tend to 
avoid human activity. This probably biases our estimates 
toward undercounts.
 ▪ Our curve-fitting method includes a step that randomizes 
the sequence in which observations are incorporated into the 
SAC. Because of the randomization, calculating any of these 
indicators twice with the same data generally yields slightly 
different values. We try to minimize the randomization 
effects by averaging over 100 instances of the curve-fitting 
step, but we are unable to eliminate the effect entirely.
 ▪ In many cities and subcity areas, there are not enough 
citizen-scientist observations to estimate a plausible SAC. 
This can be true for any number of the indicator taxa. When 
there is insufficient data, we are unable to report a species 
count estimate.
 ▪ We are unable to distinguish between native and introduced 
species. Our estimates almost certainly include introduced 
species, and in this way our indicators differ from their 
counterparts in the Singapore Index. Introduced species can 
(but do not always) harm native populations and ecosystems, 
and so a large species count—if it does not exclude 
introduced species—should not be taken as an unambiguous 
signal of good ecological health.
Flooding (FLD)
Most cities are sited based on access to water or for use in 
agriculture, power, transportation, or other purposes. But 
proximity to water also exposes cities to risks of flooding, which 
are expected to increase in most of the world with a changing 
climate. These indicators measure city exposure to a variety of 
flooding-related risks. 
Figure 3  |  An example of a species accumulation curve (SAC)
Note: In a field species census, as more individuals are caught, the more unique species 
are identified. Because the addition of unique species grows more slowly at high 
capture number, it is possible to extrapolate the curve and estimate a saturation species 
number.
Source: WRI authors.
0
0
Number of individuals caught
Number of specie s
1,000
5
10
15
20
25
30
35
40
45
50
1002 00 300 400 5006 00 700 8009 00

TECHNICAL NOTE   |  March 2023  |  15
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
FLD-1: Exposure to coastal and riverine flooding
DEFINITION
The percentage of built land exposed to coastal or 
riverine flooding.
IMPORTANCE
Most cities are built near coasts or along rivers. These natural 
assets for economic development can also present a hazard 
when they cause flooding in built-up areas. The prevalence of 
these floods is increasing globally due to sea level rise, extreme 
precipitation, and snowmelt caused by climate change.
METHODS
We use projections from Aqueduct Floods (Ward et al. 2020), 
with a resolution of 30 arc seconds (approximately 1 km), 
retrieved through Google Earth Engine to characterize the 
coastal and riverine flood hazards for each city in 2050 in terms 
of meters of expected inundation depth for a given scenario.10 
The scenario variables we use are a 100-year return period 
(providing the expected depth of inundation from a once-
in-100-years flood event), the business-as-usual/pessimistic 
(Representative Concentration Pathway 8.5) climate scenario, 
high sea level rise, no subsidence, and the mean inundation 
depth from the results of all five riverine projection models that 
are available in Aqueduct Floods. We then compare locations 
of either projected coastal or riverine flooding to built-up areas 
in the city in 2020 as defined by the built-up class from the 
ESA’s WorldCover. For each city and city district, we calculate 
the number of built-up pixels and the number of built-up pixels 
projected to experience a flood inundation depth greater than 
zero under the described flooding scenario. Then we calculate 
the percentage of built-up pixels with flood exposure.
LIMITATIONS
The Aqueduct Floods data set with a 1 km resolution may be 
too coarse for some applications related to assessing flood risk to 
individual blocks and buildings. Additionally, because this indi-
cator considers 2020 built-up areas in comparison to projected 
2050 inundation, it may underestimate built area exposed to the 
hazard as a result of future land development. Note, however, 
that this is an indicator of flood hazard, and it does not consider 
how mitigation measures such as flood protection infrastructure 
(levees, etc.) may impact the risk of inundation from flooding 
under the scenario described. This indicator is limited in scope 
to riverine and coastal flooding hazards, which are modeled 
independently—combined effects from riverine and coastal 
floods are not included. It also does not describe hazards from 
flash pluvial flooding resulting from heavy precipitation events. 
FLD-2: Extreme precipitation hazard
DEFINITION
The expected extreme precipitation event hazard (expected 
maximum millimeters of precipitation in one day in 2050) and 
trend (percentage change between 2020 and 2050 in millimeters 
of precipitation on the most extreme day).
IMPORTANCE
Understanding the hazard presented by extreme precipitation 
and the likely future change of that hazard can inform the 
importance of planning for extreme precipitation events and 
investing in infrastructure, such as trees and other vegetation, 
that can help mitigate their impacts.
METHODS
This indicator is calculated as 
where xyear is the expected precipitation on the day of year 
with the most precipitation. The expected maximum daily 
precipitation is calculated from a probability distribution 
model using European Centre for Medium-Range Weather 
Forecasts atmospheric reanalysis (ERA5)11 historical precipita-
tion data (Hersbach et al. 2020) and NASA Earth Exchange 
Global Daily Downscaled Climate Projections (NEX-GDDP) 
ensemble climate projections12 (Thrasher et al. 2012). In our 
implementation, the indicator is processed for the 0.25-degree 
pixel containing the city centroid. Because of the coarse resolu-
tion of this data set, we only report value for the geographic area 
of the full city and not for each subcity area.
More detailed documentation of these methods is under devel-
opment, and we plan to publish it in a future technical note. 
LIMITATIONS
This indicator is based on estimates of precipitation magnitude 
probabilities as modeled by climate simulations. There are 
unavoidable errors from numerous sources, including climate 
stochasticity, scientific uncertainty regarding Earth system 
processes, and uncertainty in future greenhouse gas emissions 
trends. Notably, we use the expected value of a random variable 
to capture information about a probability distribution in a 
single number. It should not be interpreted as a prediction. 
x2050 – x2020
x2020
x 100

16  |  
  
The two years over which we calculate change might not 
be appropriate for local planning needs. This indicator only 
compares expected precipitation for two years; thus, it provides a 
conservative estimate of risk. The risk is likely higher if multiple 
adjacent years are considered because the greatest daily pre-
cipitation amount between a range of years (e.g., 2046–55) is 
likely higher than the greatest precipitation expected for just one 
year (e.g., 2050). 
Maximum daily precipitation also is not a direct predictor 
of flooding. It does not account for aggravating or moderat-
ing factors such as antecedent rainfall, the local geography 
of impervious surfaces or stormwater management systems, 
and topography.
FLD-3: Land near natural drainage
DEFINITION
The percentage of built land cover within 1 m height above the 
nearest drainage.
IMPORTANCE
Land near natural drainage (e.g., streams, rivers) is at risk for 
pluvial or flash flooding hazards. Development closer in eleva-
tion to natural drainage, especially near drainage for large land 
areas, is at greater risk. The risk for these types of floods can be 
difficult to predict, and beyond height above drainage, other 
factors—such as the amount of precipitation, soil type, extent 
of impervious surfaces, distance from natural drainage, and 
the presence and efficacy of built drainage systems—are also 
important influences.
METHODS
This indicator uses 30 m resolution data on height above drain-
age channels from the Global 30 m Height Above the Nearest 
Drainage data set13 (Donchyts et al. 2016) to estimate the land 
area 1 m or less above the nearest drainage for drains with a 
flow accumulation area of at least 1 km2. We then compare these 
areas to built-up areas in the city as defined by the built-up class 
from the ESA WorldCover for 2020. 14 For each city and city 
district, we calculate at 10 m scale the number of built-up pixels 
and the number of built-up pixels within 1 m of the nearest 
drainage. Then we calculate the percentage of built-up pixels 
that are 1 m or less above the nearest drainage.
LIMITATIONS
Although this indicator is an important factor related to flash 
flooding hazards, it does not include other important informa-
tion essential to assessing flash flood hazards (soil type, artificial 
drainage systems, etc.) comprehensively. The resulting spatial 
analysis should not be interpreted as a hazard map. Because 
it does not incorporate data on artificial drainage networks 
and the city’s conveyance and routing of water (sewers, drains, 
canals), this analysis does not provide a comprehensive pic-
ture of where water is going and where it is likely to stagnate 
during pluvial flooding; rather, it provides only an extremely 
rough approximation.
FLD-4: Impervious surfaces
DEFINITION
The percentage of built land that has impervious surfaces.
IMPORTANCE
Impervious surfaces (in urban areas, typically buildings, roads, 
and other pavement) prevent water from soaking into the 
ground on-site and contribute to decreased overall water 
infiltration and increased runoff and can increase the prevalence 
of localized flooding. This type of flooding also lowers the 
quality of receiving waters fed by surface water runoff, impact-
ing the biodiversity of aquatic and marine systems downstream. 
Building cities in ways that minimize impervious surfaces (with 
alternative construction materials or intentional greening) 
allows for greater natural water infiltration and can enable cities 
to “sponge” up excess water, decrease the risk of flooding, and 
recharge groundwater resources.
METHODS
We obtain the estimated extent of impervious areas in 2018 
from the Tsinghua annual maps of global artificial impervious 
area (Gong et al. 2020).15 This 30 m resolution data set defines 
a pixel with at least 50 percent estimated impervious surface as 
being impervious. We then compare these areas to built-up areas 
(human settlement areas) in the city as defined by the built-up 
class from the 2020 ESA WorldCover For each city and city 
district, we calculate the number of built-up pixels and the 
number of impervious built-up pixels at a 10 m scale. Then we 
calculate the percentage of built-up pixels that are impervious. 
This indicator is similar to LND-1, with two distinctions. This 
indicator considers only built-up land in the area of interest (not 
all land), and the numerator in the calculation is impermeable 
area (not permeable area).
LIMITATIONS
These calculations are based entirely on remotely sensed data, 
which are not assessed against local ground truth data. The two 
data sets compared are in different resolutions and assess differ-
ent years, which presents difficulties for precise comparison.

TECHNICAL NOTE   |  March 2023  |  17
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
FLD-5: Vegetation cover in built areas
DEFINITION
The percentage of built land cover without vegetation.
IMPORTANCE
Vegetation cover provides many benefits in urban areas. For 
flood mitigation, greater vegetation cover can increase water 
infiltration into the ground, reducing water stagnation and 
runoff on the surface. In turn, an absence of vegetation cover can 
increase the prevalence of localized flooding.
METHODS
To estimate vegetation cover, we used a 10 m annual greenest 
pixel mosaic of Sentinel-2 imagery (ESA 2015b) for 2020 to 
calculate the normalized difference vegetation index (NDVI) 
with a minimum threshold of 0.4, which is commonly used as 
the threshold for a moderate degree of vegetation (EOS Data 
Analytics 2019). This NDVI provides an estimate of the loca-
tion of all types of vegetation within the area of interest. This is 
distinct from tree cover data (Brandt et al. 2022) used in other 
indicators, which intentionally includes only trees. We then 
compare these areas to built-up areas in the city as defined by 
the built-up class from the 2020 ESA WorldCover. For each city 
and city district, we calculate at 10 m scale the number of built-
up pixels and the number of vegetated built-up pixels. Then we 
calculate the percentage of built-up pixels that are vegetated.
LIMITATIONS
These calculations are based fully on remotely sensed data, 
which are not assessed against local ground truth data. An 
annual mosaic is used to assess the greenest point in the year 
for each individual pixel; as a result, this assessment does not 
measure the state of vegetation at any one point in time but 
rather the maximum state of vegetation during the year. This 
estimates for each pixel a combination of the amount of vegeta-
tion and state of greenness at peak greenness. In most pixels, 
the amount of vegetation does not change (except for leaves), 
but using the peak greenness allows us to estimate how much 
vegetation exists. Temporal and seasonal changes in vegetation 
(for example, vegetation that sheds foliage or goes dormant sea-
sonally) are known to affect the ability of green space to deliver 
expected benefits such as stormwater mitigation. The benefits 
in areas with seasonal change will not be as high as those in 
evergreen ecosystems or where there is no seasonal change 
(Wilson et al. 2022).
FLD-6: Vegetation cover in riparian zones
DEFINITION
The percentage of riparian areas without vegetation 
or water cover.
IMPORTANCE
Riparian areas—the spatial interface between land and water, 
particularly rivers and streams—can serve as natural infrastruc-
ture for flood control. Whereas in many urban areas these areas 
have been developed, paved over, or channelized, the presence 
of vegetation cover in the riparian zone is a primary factor in 
determining its flood mitigation effectiveness; vegetation can 
slow down water flow as well as increase its absorption into land 
and its transpiration into the air (Croke et al. 2017). Riparian 
areas are also critical habitats that support biodiversity.
METHODS
This indicator uses data on elevation and drainage channels 
from the Global 30m Height Above the Nearest Drainage data 
set and on the location of water bodies from the Joint Research 
Centre ( JRC) Global Surface Water data set16 (Pekel et al. 2016) 
to estimate the location of lakes, rivers, and streams. To estimate 
riparian zones, we buffered these waterways by 144 m—the 
estimated size of riparian areas often needed to preserve signifi-
cant bird diversity (Lind et al. 2019)—and excluded the area of 
the water channel itself. To estimate vegetation and water cover, 
we used an annual greenest/bluest pixel mosaic of Sentinel-2 
imagery to calculate the NDVI and the normalized difference 
water index (NDWI) with minimum thresholds of 0.4 and 0.3, 
respectively (McFeeters 2013; EOS Data Analytics 2019). For 
the buffered riparian areas in each city or subcity unit, we calcu-
lated at 30 m scale the count of all riparian area pixels and the 
count of riparian area pixels with vegetation or water cover. Then 
we calculated the percentage of riparian area pixels without 
vegetation or water cover.
LIMITATIONS
These calculations are entirely based on remotely sensed data, 
which are not assessed against local ground truth data. In 
particular, the general definition of riparian zone used may 
not match the situation on the ground as characterized with 
additional local data, such as in the case of extreme topography 
adjacent to drainage channels.

18  |  
  
FLD-7: Vulnerability of steep slopes
DEFINITION
The percentage of steep hillside slopes without vegetation cover.
IMPORTANCE
Steep slopes are vulnerable to landslides, especially during 
incidence of extreme precipitation or flooding, where soil can 
become saturated with or washed away by water. Vegetation is 
critical for stabilizing slopes; roots hold soil in place, and plants 
absorb water from the soil. Steep slopes without vegetation 
cover are particularly vulnerable to erosion, which can under-
mine the entire slope’s stability and lead to landslides.
METHODS
To estimate slopes on land, we apply the Google Earth Engine 
slope algorithm (GEE 2022) to the global NASA NASADEM 
30 m digital elevation model (NASA JPL 2020). The slope layer 
is then masked to only include high slope areas of 10 degrees 
or greater—the threshold at which landslide susceptibility 
starts to grow quickly (Stanley and Kirschbaum 2017). Vegeta-
tion cover is estimated using Sentinel-2 imagery 17 to calculate 
greenest pixel NDVI with a minimum threshold of 0.4—the 
minimum NDVI value representative of significant vegetation 
cover (EOS Data Analytics 2019). For the high slope areas in 
each city or subcity unit, we calculated at 30 m scale the count 
of all high slope pixels and the count of high slope pixels with 
any 10 m Sentinel-2 subpixels not meeting the NDVI threshold 
for vegetation cover. Then we used these values to calculate the 
percentage of high slope pixels without vegetation cover.
LIMITATIONS
These calculations are entirely based on remotely sensed data, 
which are not assessed against local ground truth data. The 
digital elevation model is based on data collected in 2000, which 
may be outdated if significant changes have occurred in local 
slopes. Additionally, its relatively low resolution (30 horizontal 
m) may not capture important smaller slope details.
Climate change mitigation (GHG)
Cities are responsible for most human-produced greenhouse 
gas emissions, but cities are also efficient at using resources and 
can reduce emissions through innovations to mitigate climate 
change. These indicators consider how cities contribute to 
climate change, including by measuring the contribution of 
economic sectors, gases, and activities. 
GHG-1: Greenhouse gas emissions
DEFINITION
The change in annual greenhouse gas emissions (CO2 equivalent 
[CO2 e]) from city area, 2000–20 (percentage), disaggregated by 
pollutant and sector.
IMPORTANCE
Human activity contributes to air pollution and climate change 
through greenhouse gas emissions from fuel combustion, 
industrial processes, and agriculture. This indicator can help 
decision-makers and stakeholders identify the most important 
pollutants emitted locally, the activities responsible for the emis-
sions, and, with multiple years of data, emissions trends.
METHODS
Similar to indicator GRE-2.1, this indicator is based on 
the CAMS Global Anthropogenic Emissions data set (Granier 
et al. 2019). The data set provides estimates of emissions from 
12 sectors of human activity, on a 0.1-degree (approximately 
11 km) spatial resolution. The estimates are based on simula-
tions and historical data. The included sectors are agriculture 
(livestock); agriculture (soils); agriculture (waste burning); 
power generation; fugitive emissions; industry; combustion in 
residential, commercial, and other settings; ships; solvents; solid 
waste and wastewater; off-road transportation; and on-road 
transportation.
We used Google Earth Engine to calculate the emissions from 
within our areas of interest (city administrative boundaries). We 
extract annual, sector-disaggregated emissions in tonnes/year 
for 2000 and 2020 for each pollutant species. We also provide 
summaries of total emissions for 2000 and 2020. Because of the 
coarse resolution of this data set, we only report value for the 
geographic area of the full city and not for each subcity area. 
To have a shared unit of measurement for all species of emis-
sions, we convert tonnes to CO2 e based on the 20-year global 
warming potentials (EPA n.d.) as listed in Table 3. To produce a 
summary number for the final indicator, we share the percentage 
change in CO2 e from 2000 to 2020.
LIMITATIONS
The emissions data used for this indicator only account for 
direct emissions from activities within the boundaries of the city 
(Scope 1 type emissions). These data do not account for emis-
sions associated with electricity used in the city but generated 
elsewhere (Scope 2) or emissions produced elsewhere associated 
with products or services consumed in the city (Scope 3). The 
CAMS data set is modeled data based on an ensemble of mul-

TECHNICAL NOTE   |  March 2023  |  19
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
tiple emissions models and is subject to the limitation of those 
models. The methods used to develop the CAMS emissions data 
set are described in Granier et al. (2019).
GHG-2: Impact of trees on greenhouse gases
DEFINITION
The average annual greenhouse gas net flux from trees (2001–
21) per hectare (ha) of city area (megagrams [Mg] CO2e/ha).
IMPORTANCE
Trees are critical contributors to a balanced climate system. 
Whereas healthy, growing trees remove carbon from the 
atmosphere and sequester it, trees that are cut or die emit carbon 
(Gibbs et al. 2022). Cities can work to keep forests and trees 
healthy and invest in expanding tree cover locally, regionally, and 
globally to increase carbon removals and reduce their contribu-
tions to climate change (Pool et al. 2022; Wilson et al. 2022).
METHODS
This indicator is calculated from the Net Carbon Flux from 
Forests data set (Version 1.2.2) per Harris et al. (2021), as 
accessed on Google Earth Engine. 18 This 30 m resolution data 
layer provides an estimate of net carbon flux from trees (gross 
emissions minus gross removals) from 2001 through 2021 
inclusive in units of Mg CO2e/ha. To calculate the mean annual 
carbon flux for each area of interest, we first unmask the data 
set; then pixels where the data set shows no carbon flux are 
given a value of zero and are included in subsequent calculations. 
Next, we calculate the mean for the area and divide the result-
ing value by 21 to annualize the 21-year data set. The resulting 
value estimates the average carbon net flux per hectare from the 
area of interest during each year in the 21-year period. As we 
are interested in measuring city and area characteristics based on 
their full geographies, not just forest areas, net flux was normal-
ized using total area as the denominator. 
Negative numbers represent net greenhouse gas removals, and 
positive values indicate net emissions.
LIMITATIONS
The carbon flux model used for the calculations was designed for 
forests and is based on tree cover as detected by Landsat, which 
means it does not pick up or measure carbon flux from sparse 
tree cover. At 30 m resolution, Landsat and products developed 
from it do not pick up isolated trees. Additionally, the model 
is limited to pixels with tree canopy density greater than 30 
percent and trees of less than 5 m height in 2000 or subsequent 
tree cover gain, so low density or short tree cover is not included. 
Other limitations of the net flux data are described in Har-
ris et al. (2021).
This indicator does not measure the impacts of indirect land-use 
change or the greenhouse gas implications of land-use decisions 
outside its borders. For instance, if a city chooses to avoid devel-
Table 3  |  Global warming potential of major pollutant species
POLLUTANT SPECIES INCLUDED AS GHG GWP (20-YEAR CO 2 EQUIVALENT) GWP SOURCE
Black carbon (BC) Yes 460 Global values reported in IPCC AR5, Table 8.A.6
Methane (CH4) Yes 84 IPCC AR5, Table 8.A.1
Carbon monoxide (CO) Yes 7.65 Midpoints of global values reported in IPCC AR5, Table 8.A.4
Carbon dioxide (CO2) Yes 1 Definition of GWP
Nitrogen oxides (NO x) Yes 19 Global values reported in IPCC AR5, Table 8.A.3
Sulfur dioxide (SO2) No NA NA
Organic carbon (OC) Yes -240 Global values reported in IPCC AR5, Table 8.A.6
Ammonia (NH3) No NA NA
Non-methane volatile organic 
compounds (NMVOCs) Yes 14 Global values reported in IPCC AR5, Table 8.A.5
Notes: GHG = greenhouse gas; GWP = global warming potential; IPCC AR5= Fifth Assessment Report of the United Nations Intergovernmental Panel on Climate Change; NA =not 
applicable.
Source: Myhre et al. 2013.

20  |  
  
oping a green area within its borders, this may lead to exporting 
the development to nearby suburban areas, possibly resulting in 
the loss of a greater number of trees and increased transporta-
tion demand, both of which could increase net carbon emissions. 
When making decisions related to land use, cities should 
consider both the direct and indirect impacts of those decisions.
Heat (HEA)
Due to the urban heat island effect, cities and their residents 
are exposed to greater heat hazard than equivalent rural areas. 
Climate change is expected to further exacerbate this risk to cit-
ies. These indicators measure local heat hazard and the presence 
of heat-mitigating infrastructure. 
HEA-1: Extreme heat hazard
DEFINITION
The expected extreme heat event hazard (expected days above 
35°C in 2050) and trend (percentage change between 2020 and 
2050 in number of days exceeding a threshold of 35°C). 
IMPORTANCE
Understanding the hazard presented by extreme heat and the 
likely future change of that hazard can inform planning for an 
extreme heat event and investing in infrastructure that can help 
mitigate its impacts. The temperature at which heat is “extreme” 
depends on location and on the potential impacts at issue. 
METHODS
This indicator is calculated as
where xyear is the expected number of days in which the maxi-
mum near-surface air temperature is above 35°C in year. This 
value is calculated from a probability distribution modeled using 
ERA5 reanalysis historical temperature data (Hersbach et al. 
2020) and NEX-GDDP ensemble climate projections (Thrasher 
et al. 2012). In our implementation, the indicator is processed 
for the 0.25-degree pixel containing the city centroid. Because 
of the coarse resolution of this data set, we only report value 
for the geographic area of the full city and not for each subcity 
area. We chose the years 2020 and 2050 to span a large number 
of years while still remaining in the time horizon of interest to 
many target users. We chose 35°C as an extreme-heat threshold; 
in high humidity, 35°C is likely to be lethal for human beings 
(Asseng et al. 2021).
x2050 – x2020
x2020
x 100
More detailed documentation of these methods is under devel-
opment, and we plan to publish it in a future technical note. 
LIMITATIONS
This indicator is based on estimates of precipitation magnitude 
probabilities as modeled by climate simulations. There are 
unavoidable errors from numerous sources, including climate 
stochasticity, scientific uncertainty regarding Earth system 
processes, and uncertainty in future greenhouse gas emissions 
trends. Notably, we use the expected value of a random variable 
as a way to capture information about a probability distribution 
in a single number. It should not be interpreted as a prediction.
The 35°C threshold is not the only temperature that could be 
useful for calculating this indicator. For example, 30°C is estab-
lished as being associated with significant decreases in human 
health and productivity (Tuholske et al. 2021). Users imple-
menting this indicator would be wise to consult public health 
officials to identify a locally appropriate temperature threshold.
The 30°C and 35°C thresholds have both been studied as a 
wet-bulb globe temperature—that is, they are believed to be 
dangerous at high enough humidity that evaporation cannot 
cool a body below them. Due to lack of humidity variables in 
Coupled Model Intercomparison Project Phase 5 (CMIP5) 
data used in NEX-GDDP , our current implementation does not 
account for humidity and does not calculate a wet-bulb globe 
temperature, but future implementations will.
HEA-2: Land surface temperature
DEFINITION
The percentage of built land with a high land surface tempera-
ture (LST) during the hot season (greater than or equal to 3°C 
above mean for built land).
IMPORTANCE
LST is closely correlated with near-surface air temperature, 
which is how people experience heat. This metric can identify 
areas of the city exposed to above-average heat. Such areas 
may be good candidates for heat mitigation measures such as 
increased tree or vegetation cover or solar reflective surfaces.
METHODS
This indicator uses LST for each pixel in the area of interest 
calculated using the methods from Ermida et al. (2020) and 
Landsat imagery, at 30 m resolution, as retrieved from Google 
Earth Engine. Mean LST is calculated from a mosaic of cloud-
masked Landsat images from 2013 to 2022 selected from the 
month of the year that had the hottest day during this period

TECHNICAL NOTE   |  March 2023  |  21
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
as determined from the ERA5 daily aggregates (Hersbach et 
al. 2020). Average and pixel-wise LST is then retrieved for 
built land cover areas using the built-up class from the ESA 
WorldCover as a mask. Finally, areas that are 3°C or more above 
the area average are masked to calculate the percentage of built 
area with high LST .
LIMITATIONS
These calculations are based entirely on remotely sensed data, 
which are not assessed against local ground truth data. Notably, 
LST is not a direct measure of how people in cities experi-
ence heat, which is more closely related to near-surface air 
temperature and heat indices. Additionally, this indicator uses 
measurements from the times of day at which Landsat retrieves 
images, usually within a few hours of midday locally. As a result, 
this indicator does not measure heat in the evening or at night, 
which is important for understanding local heat impacts. Finally, 
because this indicator uses an image mosaic to remove cloud 
cover and provide an average for the hot season in the location, 
it does not reflect any one year, day, or heat event.
HEA-3: Surface reflectivity
DEFINITION
The percentage of built land with low surface reflectivity 
(below 0.2 albedo).
IMPORTANCE
This indicator can identify areas of the city with a high share 
of surfaces that retain excess heat. Surfaces with low solar 
reflectivity (albedo) absorb heat and transfer it to immediate 
surroundings. Areas with a high share of low albedo surfaces 
may be candidates for installing measures—such as trees or 
solar reflective roofs and pavements—that will reduce the heat 
retained on surfaces or otherwise cool the immediate area.
METHODS
This indicator uses pixel-wise albedo values derived from Sen-
tinel-2, at 10 m resolution, as retrieved from Google Earth 
Engine using the algorithms defined by Bonafoni and 
Sekertekin (2020). Annual mean albedo is calculated from 
cloud-free pixels from 2021. Values for built land cover areas 
only are derived using the built-up class from the 10 m resolu-
tion ESA WorldCover data set as a mask. Finally, pixels with 
albedo values below 0.2—a common threshold used for defining 
moderately reflective surfaces (Energy Star n.d.)—are masked to 
calculate the percentage of built area with low surface reflectivity.
LIMITATIONS
These calculations are based fully on remotely sensed data, 
which are subject to atmospheric interference and other chal-
lenges in data collection and are not assessed against local 
ground truth data. This indicator uses an image mosaic to 
remove cloud cover and provide an annual average; thus, it does 
not reflect the situation at any one point in time.
HEA-4: Built land without tree cover
DEFINITION
The percentage of built land without tree cover.
IMPORTANCE
This indicator can identify city areas without significant tree 
cover and therefore lacking in shade and evapotranspiration 
that can reduce local heat. Tree cover in built areas varies 
significantly across cities. Tree cover can provide a cooling effect, 
documented to be in the range of 3°C (Wang et al. 2018), in 
urban areas. Areas without tree cover are often exposed to a 
higher extreme heat hazard. Areas with low tree cover may be 
candidates for implementing heat mitigation measures—such as 
trees, other vegetation, or solar reflective roofs and pavements—
that will reduce the heat retained locally or otherwise cool the 
immediate area.
METHODS
This indicator uses 10 m resolution tree cover data for 2020 
from the Trees in Mosaic Landscapes data set (Brandt et 
al. 2022), which gives tree extent within each 10 m pixel, as 
retrieved from Google Earth Engine. The built-up class for 2020 
from ESA WorldCover is used to mask the tree cover layer. The 
number of built pixels with tree cover is counted, all built pixels 
are counted, and these two values are divided to calculate the 
percentage of built land with tree cover. This value for percent 
tree cover is then inverted to derive a value for the percentage of 
built-up land without tree cover.
LIMITATIONS
The limitations associated with data from Brandt et al. (2022), as 
described in ACC-4, also apply to this indicator. 
Land protection and restoration (LND)
Cities play an important role in protecting and restoring natural 
lands. These lands provide ecosystem services to cities, habitat 
to wildlife, and other benefits. These indicators classify and 
measure the characteristics of land within the city or track 
changes over time.

22  |  
  
LND-1: Permeable areas
DEFINITION
The percentage of land area that has a permeable 
(pervious) surface.
IMPORTANCE
Impervious areas are areas in which pavement or other surfaces 
prevent water from infiltrating the soil. As climate change in 
many places will change precipitation regimes, many cities with 
large areas of impervious surfaces will experience high peaks 
in water runoff, resulting stormwater flooding, and damage to 
infrastructure and natural areas. This type of flooding also low-
ers the quality of receiving waters fed by surface water runoff, 
impacting the water quality for the biodiversity of aquatic and 
marine systems downstream.
METHODS
This indicator is calculated by measuring the proportion of all 
permeable areas to total terrestrial area of city:
Permeable areas are taken from the Global Artificial Impervious 
Area (GAIA) impervious surface data set (Gong et al. 2020), 
which classifies land at a 30 m spatial resolution as permeable 
or impermeable to water based on vegetation dynamics, water 
content, and reflectance. Water bodies and undeveloped land are 
assumed to be permeable. This indicator is similar to FLD-4, 
with two distinctions: it considers all land in the area of interest 
(not just built-up land), and the numerator in the calculation is 
permeable area (not impermeable area). 
LIMITATIONS
These calculations are based entirely on remotely sensed data, 
which are not assessed against local ground truth data. Other 
variables that factor into permeability that are not detectable 
with remote sensing (such as soil type) are not considered in 
this analysis. 
total permeable area
total area of city
LND-2: Tree cover
DEFINITION
The percentage of land area that has tree cover.
IMPORTANCE
Trees provide numerous services to cities. They provide cooling, 
improve air quality, store carbon, reduce noise pollution, and 
regulate the water cycle. Trees also provide habitat for birds, 
insects, and mammals, and they generally improve local ecosys-
tem health (Wilson et al. 2022).
METHODS
This indicator uses 10 m resolution tree cover data for 2020 
from the Trees in Mosaic Landscapes data set (Brandt et al. 
2022) as retrieved from Google Earth Engine, which gives the 
percentage of tree cover for each 10 m pixel. The formula used 
is as follows: 
This indicator differs from indicator HEA-4 in three ways: it 
calculates the mean tree cover of all relevant pixels (rather than 
the percentage of pixels with any tree cover), it is calculated over 
the entire area of interest (not just built-up areas within it), and 
it counts the areas with tree cover (rather than those without).
LIMITATIONS
The limitations associated with data from Brandt et al. (2022), as 
described in ACC-4, also apply to this indicator. 
LND-3: Change in vegetation and water cover
DEFINITION
The net increase or decrease in area of vegetation and water 
cover between 2019 and 2022 as a percentage of the area with 
vegetation and water cover in 2019.
IMPORTANCE
Vegetation and water cover provide many ecosystem services to 
cities, including groundwater recharge, flood management, and 
temperature moderation. They also provide critical prerequisites 
to habitat for wildlife.
area with tree cover
total area of city

TECHNICAL NOTE   |  March 2023  |  23
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
METHODS
This indicator uses a trend line of the measurements of remote 
sensing spectral indices from 2019 to 2022 to estimate the 
change in the presence of vegetation and water at points 
within each city. We use 10 m Sentinel-2 data, as accessed 
on Google Earth Engine and cloud masked (ESA 2015a), to 
calculate spectral indices associated with vegetation (NDVI) 
and water (NDWI). We then create annual greenest/bluest pixel 
mosaics for each year. We calculate trend lines of greenness and 
blueness for each pixel over the four-year period, filter to pixels 
with trend lines that are significant to a P value of 0.05, and flag 
pixels with an average annual change (slope) of at least (+/-)0.1 
in its index value. Although some studies use much lower slope 
values to detect change (Forkel et al. 2013), we selected this 
comparatively high threshold slope value to restrict the results 
to obvious major changes related to likely changes in land use or 
environmental context (e.g., vegetation cleared for construction, 
a lake bed filled with water again after a major drought) rather 
than gradual changes (e.g., natural succession, crop rotation). We 
then mask these trend layers by layers that include all pixels that 
meet the threshold for vegetation (NDVI of at least 0.4) (EOS 
Data Analytics 2019) or water (NDWI of at least 0.3) in at least 
one study year so as to exclude pixels that are not likely to be 
vegetation or water in any year. Next, we separate these change 
layers into gain and loss layers (one with slope values greater 
than zero and another with values less than zero), combine the 
separate vegetation and water layers to produce one gain and 
one loss layer, and apply 30 m resolution reductions (using the 
mean trend line values of the 10 m pixels within a 30 m pixel) to 
count the number of pixels of loss and gain for either vegetation 
or water in each city and subcity area. We then subtract the loss 
pixels from the count of gain pixels to produce a net change in 
vegetation and water pixels. To normalize this value so it repre-
sents a percentage increase or decrease in vegetation and water 
area, we divide it by the total number of 30 m pixels that met 
the index value threshold for vegetation or water in 2019 for the 
same area of interest.
LIMITATIONS
This indicator measures both change in the area of vegetation/
water cover as well as change in the strength of the vegetation 
or water signal provided by the index. Most importantly, pixels 
classified as vegetation change include areas of gained (e.g., 
conversion from bare ground to green field) and lost vegetation 
(e.g., a forest converted to buildings) as well as changes to exist-
ing vegetation areas that have become observably greener (e.g., 
a meadow that is growing tree cover due to succession) or less 
green (e.g., an existing field that is now used to grow a differ-
ent crop). Not all vegetation or water provides equal benefits. 
These varying characteristics of green and blue features are not 
measured with this method. 
LND-4: Habitat areas restored
DEFINITION
The area of habitat land restored between 2000 and 2020 as a 
percentage of habitat land in 2000.
IMPORTANCE
Cities can directly improve biodiversity by converting poor habi-
tat or nonhabitat land to good habitat. Good habitat generally 
includes multispecies vegetation and enough structural complex-
ity to provide shade and cover from predators. The Singapore 
Index’s Indicator 7 calls on cities either to estimate the area of 
land restored to “good ecological functioning” or to enumerate 
the types of habitat restored. This indicator supports the area of 
land restored method.
METHODS
We are unable to discern habitat quality using global data, but 
we can provide data on changes in land classification from 
nonhabitat to habitat. We used the Landsat Analysis Ready 
Data (Potapov et al. 2022) from the Global Land Analysis and 
Discovery research group at the University of Maryland. 19 We 
defined habitat as aquatic or noncropland vegetated classes, and 
we compared classifications from 2000 and 2020. We defined 
new habitat as pixels that were classified as nonhabitat (urban, 
cropland, or bare) in 2000 but as habitat in 2020. For this 
indicator, we calculated
LIMITATIONS
This method differs somewhat from what is described in the 
Singapore Index’s Indicator 7. Our denominator is nonhabitat 
rather than degraded habitat. Our estimate probably underesti-
mates restoration as measured by this indicator.
area of habitat in 2020 – area of habitat in 2000
area of nonhabitat in 2000

24  |  
  
LND-5: Habitat types restored
DEFINITION
The number of habitat types restored between 2000 and 2020 as 
a percentage of all habitat types in the area.
IMPORTANCE
Cities can directly improve biodiversity by converting poor 
habitat or nonhabitat land to good habitat. Good habitat 
generally includes multispecies vegetation and enough structural 
complexity to provide shade and cover. The Singapore Index’s 
Indicator 7 calls on cities either to estimate the area of land 
restored to “good ecological functioning” or to enumerate the 
types of habitat restored. This indicator supports the habitat-
type enumeration method.
METHODS
This indicator is calculated by the formula
The Landsat Analysis Ready Data discerns six land cover classes 
that we include as types of habitat: short vegetation, forest, tall 
forest (taller than 20 m), wetland with short vegetation, wetland 
forest, and open water. (We treated the classes for bare ground, 
snow or ice, cropland, and built-up area as nonhabitat.) We 
calculate our indicator by identifying areas of new habitat, where 
habitat existed in 2020 but not in 2000; counting the number of 
habitat types (i.e., aquatic and vegetated land cover classes) in 
these areas of new habitat; and comparing this number to the 
total number of habitat types in the city in 2020. For example, 
consider a city that had four types of habitat in 2020. We look 
for all habitat areas in 2020 that were nonhabitat in the baseline 
year 2000 and consider these to be new habitat areas. If there are 
two habitat types in the new habitat areas, then the indicator 
is as follows:
LIMITATIONS
This indicator describes restoration as a fraction of the existing 
diversity of habitat types, not as the absolute diversity of restored 
habitat. It does not distinguish between a city that restores many 
number of habitat types restored
number of habitat types in city in baseline year
2 habitat types in new habitat
4 habitat types in city in 2020 x 100% = 50%
types of habitat and a city that simply has few habitat types. For 
example, in a city with six habitat types, restoration of six types 
of habitat will result in an indicator value of 100 percent. The 
indicator is also 100 percent if a city with just one habitat type 
restores just one habitat type. By scaling restored diversity by 
overall diversity, this indicator focuses narrowly on cities’ efforts 
to restore native diversity and not on the diversity itself.
Our method also differs from that in the Singapore Index: we 
use new habitat instead of habitat that has been improved from 
degraded to good ecological function. Cities that have access to 
local data specifically detailing the extent and status of habitat 
restoration projects would probably benefit from calculating the 
Singapore Index’s Indicator 7 using that data.
LND-6: Protected areas
DEFINITION
The percentage of land area that is designated as protected area.
IMPORTANCE
Protected or secured natural areas indicate a government’s 
legally formalized commitment to conserve biodiversity. 
Protected areas are lands (or waters) with legal restrictions on 
development or use and sometimes physical barriers to entry. 
Protected areas inside and near cities, including outside their 
jurisdictional boundaries, can provide multiple benefits to people 
living in cities in the form of human health and well-being and 
water security (Wilson et al. 2022). Importantly, they serve as 
havens for biodiversity and can be used to create ecological con-
nectivity and restore previously lost biodiversity in the cityscape. 
METHODS
This indicator uses the following formula:
Our data on protected areas come from the World Database 
on Protected Areas (WDPA), which is a collection of data on 
protected areas contributed by national governments (UNEP-
WCMC and IUCN n.d.).
area of protected or secured natural areas within city
total area of city

TECHNICAL NOTE   |  March 2023  |  25
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
LIMITATIONS
 ▪ This indicator measures only protected areas within city 
boundaries, excluding nearby protected areas. 
 ▪ The WDPA is based on information contributed by national 
governments. It might exclude areas whose protections do 
not fit criteria set by these governments.
 ▪ Intensive, biodiversity-harming activities can occur within 
formally protected areas. We do not assess specific legal 
protections; nor do we assess enforcement of protections.
LND-7: Protection of Key Biodiversity Areas
DEFINITION
The percentage of Key Biodiversity Area (KBA) land that is 
designated as protected area.
IMPORTANCE
KBAs are areas that have been identified by the KBA Partner-
ship as being important to global biodiversity, generally because 
they include either a globally important type of habitat or 
because they include habitat for a globally important species 
(BirdLife International 2022). Criteria for inclusion include 
the presence of threatened biodiversity, the presence of geo-
graphically restricted biodiversity, ecological integrity, critical 
biological processes, and irreplaceability. Cities can threaten or 
contribute to the global persistence of biodiversity through their 
development choices. Limiting development within KBAs or 
formally protecting land within KBAs can protect biodiversity 
in these areas.
In addition to the map of local KBAs, we provide two indicators 
related to these areas (LND-7 and LND-8). Neither indicator 
corresponds directly to an indicator in the Singapore Index.
METHODS
KBAs can often benefit from formal protection (KBA Partner-
ship 2017). In this indicator, we provide information on how 
much of a city’s KBA is currently under formal protection. This 
is the formula:
KBA data are provided by (BirdLife International 2022) for the 
KBA Partnership, and data on protected areas come from the 
WDPA (UNEP-WCMC and IUCN n.d.). 
area of KBA within city under formal protection
total area of KBA within city
LIMITATIONS
This indicator shares the limitations of LND-6 arising from 
limitations in the WDPA. Both the WDPA and the KBA data 
are periodically updated. Users who use values of this indicator 
calculated by WRI or others should note whether they were 
based on the most recent versions of the input data.
The terms of use provided by the KBA Partnership do not allow 
us to share the source KBA data, but all data can be requested 
from BirdLife International. Similarly, the United Nations 
Environment Programme World Conservation Monitoring 
Centre and the International Union for Conservation of Nature 
do not allow us to share the source data on protected areas, 
but all data are available on the WDPA website (https://www.
protectedplanet.net). 
LND-8: Built-up KBAs
DEFINITION
The percentage of KBA land that is built up. 
IMPORTANCE
Land expansion from cities and other settlements poses a major 
threat to biodiversity (McDonald et al. 2018). Habitat qual-
ity in built-up areas tends to be lower than in natural areas. 
Habitat quality in KBAs might therefore be improved by 
habitat restoration efforts that convert built-up areas to natural 
ecosystem types.
METHODS
We provide an indicator that describes how much of the KBA 
within the city is built up. The formula is as follows:
The data on built-up areas are from the 2020 ESA WorldCover. 
KBA data are provided by BirdLife International (2022) for the 
KBA Partnership. 
LIMITATIONS
The KBA data are periodically updated. Users who use values of 
this indicator calculated by WRI or others should note whether 
they were based on the most recent versions of the input data.
The terms of use provided by the KBA Partnership do not allow 
us to share the source data, but all data can be requested on its 
website (https://www.keybiodiversityareas.org).
built-up area within KBA within city
total area of KBA within city

26  |  
  
GENERAL LIMITATIONS
The indicators developed through these methods can provide 
numerous insights on variations within and between cities and 
changes over time. However, there are limitations to the value 
provided by these indicators, uncertainty regarding the result-
ing indicator values, and caveats to their meaning and potential 
applications that should be understood. In addition to the 
limitations specific to each indicator mentioned, there are also 
a few general limitations. We have addressed these concerns to 
the extent practical through how specific indicators are defined 
and presented, but these issues remain important for users of 
the indicators.
 ▪ Boundaries and aggregations. These methods primarily 
focus on providing a summary value of each area of 
interest for each indicator. Doing so helps to simplify a 
large amount of data, but it can also obscure nuance and 
important information. First, the areas of interest need to 
be meaningful. We use administrative areas because they 
are important boundaries of authority for decision-makers 
and are often used to aggregate other information. But 
different boundaries result in different indicator values. 
Other boundaries may be more relevant to a different set of 
stakeholders in the same city. Boundaries can change over 
time, making comparisons difficult. And for some topics, 
other kinds of boundaries may be more appropriate to 
generate meaningful insights (e.g., watershed boundaries 
for hydrology). Second, how boundaries are drawn and 
the characteristics of the areas within the boundaries can 
profoundly affect the results of data aggregations for the area 
of interest. As an example, if a park is equally split between 
two city wards, and they have similar vegetation coverage, 
the boundaries could obscure the significant vegetation 
differences within their respective residential areas due to 
averaging. If the park were classified as a separate area of 
interest, a vegetation cover indicator would more accurately 
characterize the differences between the two remaining 
residential areas. Third, the size of the areas of interest in 
comparison to the scale of the data sets used to calculate 
indicators can produce results that range from insightful to 
near meaningless. For example, assume a city has equally 
sized square districts of 1 km in each direction. A raster data 
set that is at a smaller scale would give useful information 
about the area within the district (but if it is much smaller in 
scale, such as 10 m, it may give too much information for an 
aggregate indicator to fully summarize, as we discuss further 
below). However, if the data set is of a larger scale, say 10 
km, aggregations at the smaller district scale result in the 
same value for many districts, which likely does not reflect 
the reality on the ground and does not give any meaningful 
information for comparison between the districts. 
 ▪ Data uncertainty and incompleteness. The data sources 
used to calculate the indicators themselves have significant 
limitations. The global-scale data sets from remote sensing 
or crowdsourcing used for our indicators are limited by what 
sensors can detect, their minimum mapping unit, and user 
contributions. They can give the impression of completeness 
while not being relevant at the scale of the desired analysis or 
can be missing important contextual details. We document 
limitations of specific data sets within the description of 
methods for each indicator. In contrast, local data pose 
their own problems, including being limited in scope, using 
local definitions that are often incompatible with data 
used elsewhere, introducing bias to an analysis, and often 
being difficult to access. The time required to collect and 
process local data makes it impossible to use local data for 
this project, which aims to calculate shared indicators for 
eventually hundreds of cities around the world. Ultimately, 
decisions about the most appropriate data for a local 
challenge need to be made by or with local stakeholders. 
For this reason, methods with flexible data input sources are 
critical. Our indicator methods can be adapted by our team 
or other researchers for use with similar alternative data sets, 
including from local sources, if a more appropriate one is 
developed or identified. 
 ▪ Comparability between indicators and data sets. The 
differences between data sets—such as their scale or dates 
of acquisition—can make it complex to use multiple data 
sets together. We intend for multiple indicators to be shared 
with stakeholders; however, indicators within the same 
thematic areas, and even indicators themselves, may draw 
on information from various data sets. Within individual 
indicators, we often use multiple data sets together (e.g., a 
primary data set and another data set to mask the data to 
focus on land cover types of interest) to develop an indicator 
statistic. The best data sets for required variables may be 
available for different years, meaning some changes during 
that time period are ignored or misrepresented. Or they may 
be of different scales, meaning that issues of aggregation 
(as discussed previously) or precision (e.g., more trees being 
detectable at a 10 m scale than a 30 m scale) can mean that 
the data sets show different information in the same place. 
 ▪ Spatial observational data are not enough. Our indicators 
almost exclusively identify the current physical states or 
changes to them in cities. This information can establish

TECHNICAL NOTE   |  March 2023  |  27
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
trends; benchmark areas against each other; and help 
identify opportunities, diagnose problems, and spatially 
target interventions. However, the indicators alone are 
likely not sufficient to identify actions and set targets. 
Domain expertise and local knowledge to identify options 
and planning processes to determine objectives are 
required. Importantly, these indicators do not measure or 
attribute influences on physical changes, such as policies or 
infrastructure investment, or their effectiveness. To track 
progress toward physical goals, observational data is essential. 
To understand which actions are working well and which are 
falling short, other data and methods are required. 
FURTHER WORK
These indicator methods and their uses can be further refined 
and enhanced. Options identified so far include the following:
 ▪ Develop a standard indicator workflow and shared database. 
Consolidating variations on our core workflow and indicator 
sets that have been developed for multiple projects would 
make it easier to quickly calculate any set of indicators for 
any set of areas of interest. 
 ▪ Package the indicator workflow solution into an 
open-source framework (R or Python package) that 
can be easily reused and/or updated by external/
internal contributors. 
 ▪ Offer guidance on developing new or revised indicators 
emphasizing designs that are fit for purpose and data set 
comparison and selection. 
 ▪ Develop additional indicators or adapt existing indicator 
methods into our calculation framework to allow for similar 
standard measurements on other urban themes relevant to 
city decision-makers or stakeholders. 
 ▪ Calculate indicators for additional cities and for other 
initiatives supporting cities on sustainable development. 
 ▪ Compare our indicator findings with socioeconomic data to 
explore relationships between indicators of urban equity and 
the presence of urban amenities/risk in multiple cities.
 ▪ Create a process for vetting and validating new global or 
local data layers as they become available to potentially 
integrate with and improve existing indicator methods.
 ▪ Compare computed indicators using global data with 
computations from available local data for validation 
and provide support to stakeholders for collecting local 
data as needed. 
 ▪ Calculate indicator time series for some areas of interest, 
where appropriate multiyear input data layers are available 
and where relevant to indicators. 
 ▪ Improve integration of user feedback and needs into 
indicator prioritization, design, and development.
 ▪ Connect more with potential users and stakeholders and 
define their profiles, statuses, data capacities, and needs. 
 ▪ Conduct user needs assessments to better understand 
how the proposed indicators may help our stakeholders 
in their decision-making processes and what additional 
indicators—or modifications of existing indicators—may 
be useful for users. 
 ▪ Map our indicators with potential city-level actions and 
how the proposed metrics may drive them. 
 ▪ Create focus groups or case studies of cities sharing 
feedback on the value and uses of the data and indicators.

28  |  
  
ENDNOTES
1. To learn about the Cities4Forests initiative, visit https://cities4for -
ests.com/. 
2. For information about the UrbanShift initiative, see https://www.
shiftcities.org/.
3. For more information about the OSM database, see https://www.
openstreetmap.org/.
4. Current methods are documented in two separate code reposi -
tories, one for each initiative with which the indicators are being 
piloted: Cities4Forests (https://github.com/wri/cities-cities4for -
ests-indicators) and UrbanShift (https://github.com/wri/cities-
urbanshift/tree/main/baseline-indicators). 
5. The “built-up” land cover class of WorldCover 2020 is defined as 
“land covered by buildings, roads and other man-made structures 
such as railroads. Buildings include both residential and industrial 
building. Urban green (parks, sport facilities) is not included in this 
class” (ESA 2020b).
6. For more information about the Trees in Mosaic Landscapes data 
set, see https://resourcewatch.org/data/explore/Trees-in-Mosaic-
Landscapes.
7. To learn more about the Global Anthropogenic Emissions data 
set, see https://eccad3.sedoo.fr/metadata/479; for CAMS, see 
https://atmosphere.copernicus.eu/; and for ECCAD, see https://
eccad.aeris-data.fr/. 
8. For more information about the CAMS Global Reanalysis EAC4 
data set, visit https://www.ecmwf.int/en/forecasts/dataset/cams-
global-reanalysis.
9. To learn more about the V5.GL.02 data set, see https://sites.wustl.
edu/acag/datasets/surface-pm2-5/#V5.GL.02, and for the Atmo -
spheric Composition Analysis Group, see https://sites.wustl.edu/
acag/.
10. For more information about the Aqueduct Floods database, visit 
https://www.wri.org/applications/aqueduct/floods.
11. Additional information about the ERA5 reanalysis can be found on 
the Google Earth Engine Data Catalog, https://developers.google.
com/earth-engine/datasets/catalog/ECMWF_ERA5_DAILY.
12. More information about the NEX-GDDP ensemble climate pro -
jections is available on the Google Earth Engine Data Catalog, 
https://developers.google.com/earth-engine/datasets/catalog/
NASA_NEX-GDDP.
13. For additional information about the Global 30 m Height Above 
the Nearest Drainage data set, see https://gee-community-cata -
log.org/projects/hand/.
14. For more information about the 2020 ESA WorldCover, visit 
https://developers.google.com/earth-engine/datasets/catalog/
ESA_WorldCover_v100.
15. For more information about the Tsinghua annual maps, see 
https://developers.google.com/earth-engine/datasets/catalog/
Tsinghua_FROM-GLC_GAIA_v10.
16. More information about the JRC Global Surface Water data set is 
available at https://developers.google.com/earth-engine/datas -
ets/catalog/JRC_GSW1_3_GlobalSurfaceWater.
17. For additional information about Sentinel-2 data, see https://
developers.google.com/earth-engine/datasets/catalog/COPERNI -
CUS_S2.
18. To access the Net Carbon Flux from Forests data set, visit https://
code.earthengine.google.com/?asset=projects/wri-datalab/gfw-
data-lake/net-flux-forest-extent-per-ha-v1-2-2-2001-2021/net-flux-
global-forest-extent-per-ha-2001-2021. 
19. To learn more about the Global Land Analysis and Discovery 
research group, visit https://glad.umd.edu/.

TECHNICAL NOTE   |  March 2023  |  29
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
REFERENCES
Asseng, S., D. Spänkuch, I.M. Hernandez-Ochoa, and J. Laporta. 2021. 
“The Upper Temperature Thresholds of Life.” Lancet Planetary Health  
5 (6): e378–85. https://doi.org/10.1016/S2542-5196(21)00079-6.
Avtar, R., R. Aggarwal, A. Kharrazi, P. Kumar, and T.A. Kurniawan. 2019. 
“Utilizing Geospatial Information to Implement SDGs and Monitor 
Their Progress.” Environmental Monitoring and Assessment  192 (De-
cember): 35. https://doi.org/10.1007/s10661-019-7996-9.
BirdLife International. 2022. (Database.) World Database of Key 
Biodiversity Areas .” Key Biodiversity Areas Partnership. https://www.
keybiodiversityareas.org/.
Bocher, E., G. Petit, J. Bernard, and S. Palominos. 2018. “A Geoprocess -
ing Framework to Compute Urban Indicators: The MApUCE Tools 
Chain.” Urban Climate 24 (June): 153–74. https://doi.org/10.1016/j.
uclim.2018.01.008.
Boeing, G., C. Higgs, S. Liu, B. Giles-Corti, J.F. Sallis, E. Cerin, M. Lowe, 
et al. 2022. “Using Open Data and Open-Source Software to De -
velop Spatial Indicators of Urban Design and Transport Features for 
Achieving Healthy and Sustainable Cities.” Lancet Global Health  10 (6): 
e907–18. https://doi.org/10.1016/S2214-109X(22)00072-9.
Bonafoni, S., and A. Sekertekin. 2020. “Albedo Retrieval from Senti -
nel-2 by New Narrow-to-Broadband Conversion Coefficients.” IEEE 
Geoscience and Remote Sensing Letters  17 (9): 1618–22. https://doi.
org/10.1109/LGRS.2020.2967085.
Brandt, J., J. Ertel, J. Spore, and F. Stolle. 2022. “The Extent of Trees 
in the Tropics.” Research Square, September 29. https://doi.
org/10.21203/rs.3.rs-2109093/v1.
Chan, L., O. Hillel, P. Werner, N. Holman, I. Coetzee, R. Galt, and T. 
Elmqvist. 2021. “Handbook on the Singapore Index on Cities’ Biodi -
versity (also Known as the City Biodiversity Index).” CBD Technical 
Series 98. Montreal: Secretariat of the Convention on Biological 
Diversity; Singapore: National Parks Board. https://www.cbd.int/doc/
publications/cbd-ts-98-en.pdf.
Cochran, F., J. Daniel, L. Jackson, and A. Neale. 2020. “Earth Observa -
tion-Based Ecosystem Services Indicators for National and Sub -
national Reporting of the Sustainable Development Goals.” Remote 
Sensing of Environment 244 (July): 111796. https://doi.org/10.1016/j.
rse.2020.111796.
Croke, J., C. Thompson, and K. Fryirs. 2017. “Prioritising the Placement 
of Riparian Vegetation to Reduce Flood Risk and End-of-Catchment 
Sediment Yields: Important Considerations in Hydrologically-Variable 
Regions.” Journal of Environmental Management  190 (April): 9–19. 
https://doi.org/10.1016/j.jenvman.2016.12.046.
Deslauriers, M.R., A. Asgary, N. Nazarnia, and J.A.G. Jaeger. 2018. “Im -
plementing the Connectivity of Natural Areas in Cities as an Indicator 
in the City Biodiversity Index (CBI),” in “Landscape Indicators—Moni -
toring of Biodiversity and Ecosystem Services at Landscape Level,” 
edited by U. Walz and R.-U. Syrbe, special issue, Ecological Indicators  
94 (November): 99–113. https://doi.org/10.1016/j.ecolind.2017.02.028.
Donchyts, G., H. Winsemius, J. Schellekens, T. Erickson, H. Gao, 
H. Savenije, and N. van de Giesen. 2016. “Global 30m Height 
above the Nearest Drainage (HAND).” Geophysical Research Ab -
stracts 18: EGU2016-17445-3. https://gee-community-catalog.org/
projects/hand/.
Energy Star. n.d “ENERGY STAR Program Requirements for Roof 
Products: Partner Commitments.” https://www.energystar.gov/sites/
default/files/specs//Roof%20Products%20V3%20Program%20Re -
quirements_0.pdf. Accessed March 7, 2023.
Engel-Cox, J.A., R.M. Hoff, and A.D.J. Haymet. 2004. “Recommenda -
tions on the Use of Satellite Remote-Sensing Data for Urban Air 
Quality.” Journal of the Air & Waste Management Association 54 (11): 
1360–71. https://doi.org/10.1080/10473289.2004.10471005.
EOS Data Analytics. 2019. “NDVI FAQ: All You Need to Know about 
Index.” Agriculture (blog), August 30. https://eos.com/blog/ndvi-faq-
all-you-need-to-know-about-ndvi/.
EPA (U.S. Environmental Protection Agency). n.d. “Understanding 
Global Warming Potentials.” https://www.epa.gov/ghgemissions/
understanding-global-warming-potentials. Accessed January 12, 2016.

30  |  
  
Ermida, S.L., P. Soares, V. Mantas, F.-M. Göttsche, and I.F. Trigo. 2020. 
“Google Earth Engine Open-Source Code for Land Surface Tempera -
ture Estimation from the Landsat Series.” Remote Sensing  12 (9): 1471. 
https://doi.org/10.3390/rs12091471.
ESA (European Space Agency). 2015a. “Sentinel-2: Cloud Probability.” 
Earth Engine Data Catalog. https://developers.google.com/earth-
engine/datasets/catalog/COPERNICUS_S2_CLOUD_PROBABILITY.
ESA. 2015b. “Sentinel-2 MSI: MultiSpectral Instrument, Level-1C.”Earth 
Engine Data Catalog. https://developers.google.com/earth-engine/
datasets/catalog/COPERNICUS_S2.
ESA. 2020a. “ESA WorldCover 10m V100.” Earth Engine Data Cata -
log. https://developers.google.com/earth-engine/datasets/catalog/
ESA_WorldCover_v100.
ESA. 2020b. WorldCover Product User Manual, Version 1.0 . Paris: ESA. 
https://worldcover2020.esa.int/data/docs/WorldCover_PUM_V1.1.pdf.
Fahrig, L. 2003. “Effects of Habitat Fragmentation on Biodiversity.” 
Annual Review of Ecology, Evolution, and Systematics 34: 487–515. 
https://doi.org/10.1146/annurev.ecolsys.34.011802.132419.
Feng, S., D. Gao, F. Liao, F. Zhou, and X. Wang. 2016. “The Health 
Effects of Ambient PM 2.5 and Potential Mechanisms.” Ecotoxicology 
and Environmental Safety  128 (June): 67–74. https://doi.org/10.1016/j.
ecoenv.2016.01.030.
Forkel, M., N. Carvalhais, J. Verbesselt, M.D. Mahecha, C.S.R. Neigh, 
and M. Reichstein. 2013. “Trend Change Detection in NDVI Time 
Series: Effects of Inter-annual Variability and Methodology.” Remote 
Sensing 5 (5): 2113–44. https://doi.org/10.3390/rs5052113.
Forman, R.T.T., and M. Godron. 1991. Landscape Ecology . Hoboken, 
NJ: Wiley. https://www.wiley.com/en-us/Landscape+Ecology-
p-9780471870371.
Fritz, S., L. See, T. Carlson, M. Haklay, J.L. Oliver, D. Fraisl, R. Mond -
ardini, et al. 2019. “Citizen Science and the United Nations Sustain -
able Development Goals.” Nature Sustainability  2 (October): 922–30. 
https://doi.org/10.1038/s41893-019-0390-3.
GBIF (Global Biodiversity Information Facility). 2022a. “Occurrence 
Download—Arthropods.” https://doi.org/10.15468/DL.DWV9AP.
GBIF. 2022b. “Occurrence Download—Birds.” https://doi.
org/10.15468/DL.H4AZRE.
GBIF. 2022c. “Occurrence Download—Vascular Plants.” https://doi.
org/10.15468/DL.6WANKS.
Geemap. n.d. “OSM Module.” https://geemap.org/osm/. Accessed 
November 8, 2022.
Gibbs, D., N. Harris, and J.-R. Pool. 2022. Global Protocol for Commu -
nity-Scale Greenhouse Gas Inventories: Supplemental Guidance for 
Forests and Trees. Washington, DC: Greenhouse Gas Protocol, World 
Resources Institute. https://ghgprotocol.org/gpc-supplemental-guid -
ance-forests-and-trees.
Giuliani, G., E. Petri, E. Interwies, V. Vysna, Y. Guigoz, N. Ray, and I. 
Dickie. 2021. “Modelling Accessibility to Urban Green Areas Using 
Open Earth Observations Data: A Novel Approach to Support the Ur -
ban SDG in Four European Cities.” Remote Sensing  13 (3): 422. https://
doi.org/10.3390/rs13030422.
Gong, P., X. Li, J. Wang, Y. Bai, B. Chen, T. Hu, X. Liu, et al. 2020. “Annual 
Maps of Global Artificial Impervious Area (GAIA) between 1985 and 
2018.” Remote Sensing of Environment  236 (January): 111510. https://
doi.org/10.1016/j.rse.2019.111510.
GEE (Google Earth Engine). 2021. “Weighted Reductions.” May 27. 
https://developers.google.com/earth-engine/guides/reducers_
weighting. Accessed November 8, 2022.
GEE. 2022. “Ee.Terrain.slope.” August 1. https://developers.google.
com/earth-engine/apidocs/ee-terrain-slope.
Granier, C., S. Darras, H. Denier van der Gon, J. Doubalova, N. El -
guindi, B. Galle, M. Gauss, et al. 2019. “The Copernicus Atmosphere 
Monitoring Service Global and Regional Emissions (April 2019 
Version).” Copernicus Atmosphere Monitoring Service. https://doi.
org/10.24380/D0BN-KX16.
Harris, N.L., D.A. Gibbs, A. Baccini, R.A. Birdsey, S. de Bruin, M. Farina, 
L. Fatoyinbo, et al. 2021. “Global Maps of Twenty-First Century Forest 
Carbon Fluxes.” Nature Climate Change 11 (3): 234–40. https://doi.
org/10.1038/s41558-020-00976-6.

TECHNICAL NOTE   |  March 2023  |  31
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
Helmrich, A.M., B.L. Ruddell, K. Bessem, M.V. Chester, N. Chohan, E. 
Doerry, J. Eppinger, et al. 2021. “Opportunities for Crowdsourcing in 
Urban Flood Monitoring.” Environmental Modelling & Software  143 
(September): 105124. https://doi.org/10.1016/j.envsoft.2021.105124.
Hersbach, H., B. Bell, P. Berrisford, S. Hirahara, A. Horányi, J. Muñoz‐
Sabater, J. Nicolas, et al. 2020. “The ERA5 Global Reanalysis.” Quar -
terly Journal of the Royal Meteorological Society 146 (730): 1999–2049. 
https://doi.org/10.1002/qj.3803.
Inness, A., M. Ades, A. Agustí-Panaredaz, J. Barré, A. Benedictow, A. 
Blechschmidt, J. Dominguez, et al. 2019. “CAMS Global Reanalysis 
(EAC4).” Copernicus Atmosphere Monitoring Service. https://ads.at -
mosphere.copernicus.eu/cdsapp#!/dataset/cams-global-reanalysis-
eac4?tab=overview.
Jing, C., M. Du, S. Li, and S. Liu. 2019. “Geospatial Dashboards for 
Monitoring Smart City Performance.” Sustainability  11 (20): 5648. 
https://doi.org/10.3390/su11205648.
Kalluri, S., P. Gilruth, and R. Bergman. 2003. “The Potential of Remote 
Sensing Data for Decision Makers at the State, Local and Tribal Level: 
Experiences from NASA’s Synergy Program.” Environmental Science & 
Policy 6 (6): 487–500. https://doi.org/10.1016/j.envsci.2003.08.002.
Kampa, M., and E. Castanas. 2008. “Human Health Effects of Air Pollu -
tion.” Environmental Pollution 151 (2): 362–67. https://doi.org/10.1016/j.
envpol.2007.06.012.
Kavvada, A., G. Metternicht, F. Kerblat, N. Mudau, M. Haldorson, S. 
Laldaparsad, L. Friedl, A. Held, and E. Chuvieco. 2020. “Towards 
Delivering on the Sustainable Development Goals Using Earth Ob -
servations.” Remote Sensing of Environment  247 (September): 111930. 
https://doi.org/10.1016/j.rse.2020.111930.
KBA (Key Biodiversity Areas) Partnership. 2017. The Relationship be -
tween Key Biodiversity Areas (KBAs) and Protected Areas . Cambridge, 
UK: KBA Secretariat, Birdlife International. https://www.keybiodiver -
sityareas.org/assets/8f1535aed3316ae2b720364019f8cb1c.
Kondo, M.C., S. Han, G.H. Donovan, and J.M. MacDonald. 2017. “The 
Association between Urban Trees and Crime: Evidence from the 
Spread of the Emerald Ash Borer in Cincinnati.” Landscape and Urban 
Planning 157 (January): 193–99. https://doi.org/10.1016/j.landurb -
plan.2016.07.003.
Kuffer, M., J. Wang, M. Nagenborg, K. Pfeffer, D. Kohli, R. Sliuzas, and 
C. Persello. 2018. “The Scope of Earth-Observation to Improve the 
Consistency of the SDG Slum Indicator.” ISPRS International Journal of 
Geo-Information  7 (11): 428. https://doi.org/10.3390/ijgi7110428.
Kuffer, M., D.R. Thomson, G. Boo, R. Mahabir, T. Grippa, S. Van -
huysse, R. Engstrom, et al. 2020. “The Role of Earth Observation 
in an Integrated Deprived Area Mapping ‘System’ for Low-to-
Middle Income Countries.” Remote Sensing  12 (6): 982. https://doi.
org/10.3390/rs12060982.
Lee, K.K., M.R. Miller, and A.S.V. Shah. 2018. “Air Pollution and Stroke.” 
Journal of Stroke 20 (1): 2–11. https://doi.org/10.5853/jos.2017.02894.
Lind, L., E.M. Hasselquist, and H. Laudon. 2019. “Towards Ecologically 
Functional Riparian Zones: A Meta-analysis to Develop Guidelines 
for Protecting Ecosystem Functions and Biodiversity in Agricultural 
Landscapes.” Journal of Environmental Management  249 (November): 
109391. https://doi.org/10.1016/j.jenvman.2019.109391.
Litwiller, F., C. White, K. Gallant, S. Hutchinson, and B. Hamilton-Hinch. 
2016. “Recreation for Mental Health Recovery.” Leisure/Loisir  40 (3): 
345–65. https://doi.org/10.1080/14927713.2016.1252940.
Ludwig, C., R. Hecht, S. Lautenbach, M. Schorcht, and A. Zipf. 2021. 
“Mapping Public Urban Green Spaces Based on OpenStreetMap and 
Sentinel-2 Imagery Using Belief Functions.” ISPRS International Jour -
nal of Geo-Information  10 (4): 251. https://doi.org/10.3390/ijgi10040251.
Martinuzzi, S., O.M. Ramos-González, T.A. Muñoz-Erickson, D.H. 
Locke, A.E. Lugo, and V.C. Radeloff. 2018. “Vegetation Cover in Rela -
tion to Socioeconomic Factors in a Tropical City Assessed from Sub-
meter Resolution Imagery.” Ecological Applications  28 (3): 681–93. 
https://doi.org/10.1002/eap.1673.
Martinuzzi, S., D.H. Locke, O. Ramos-González, M. Sanchez, J.M. 
Grove, T.A. Muñoz-Erickson, W.J. Arendt, and G. Bauer. 2021. “Explor -
ing the Relationships between Tree Canopy Cover and Socioeco -
nomic Characteristics in Tropical Urban Systems: The Case of Santo 
Domingo, Dominican Republic.” Urban Forestry & Urban Greening 62 
(July): 127125. https://doi.org/10.1016/j.ufug.2021.127125.

32  |  
  
McDonald, R.I., M. Colbert, M. Hamann, R. Simkin, and B. Walsh. 2018. 
Nature in the Urban Century: A Global Assessment of Where and How 
to Conserve Nature for Biodiversity and Human Wellbeing . Arlington 
County, VA: The Nature Conservancy. https://www.nature.org/en-us/
what-we-do/our-insights/perspectives/nature-in-the-urban-century/.
McFeeters, S.K. 2013. “Using the Normalized Difference Water Index 
(NDWI) within a Geographic Information System to Detect Swimming 
Pools for Mosquito Abatement: A Practical Approach.” Remote Sens -
ing 5 (7): 3544–61. https://doi.org/10.3390/rs5073544.
Myhre, G., D. Shindell, F.-M. Bréon, W. Collins, J. Fuglestvedt, J. Huang, 
D. Koch, et al. 2013. “Anthropogenic and Natural Radiative Forcing.” 
In Climate Change 2013: The Physical Science Basis. Contribution of 
Working Group I to the Fifth Assessment Report of the Intergovern -
mental Panel on Climate Change, edited by T.F. Stocker, D. Qin, G.-K. 
Plattner, M. Tignor, S.K. Allen, J. Boschung, A. Nauels, Y. Xia, V. Bex, 
and P.M. Midgley, 659–740. Cambridge and New York: Cambridge 
University Press. https://www.ipcc.ch/site/assets/uploads/2018/02/
WG1AR5_Chapter08_FINAL.pdf. 
NASA JPL (National Aeronautics and Space Administration Jet 
Propulsion Laboratory). 2020. “NASADEM Merged DEM Global 1 Arc 
Second V001.” Earth Engine Data Catalog. https://developers.google.
com/earth-engine/datasets/catalog/NASA_NASADEM_HGT_001.
Nicoletti, L., M. Sirenko, and T. Verma. 2022. “Disadvantaged Com -
munities Have Lower Access to Urban Infrastructure.” Environment 
and Planning B: Urban Analytics and City Science , October. https://doi.
org/10.1177/23998083221131044.
Niu, H., and E.A. Silva. 2020. “Crowdsourced Data Mining for Urban 
Activity: Review of Data Sources, Applications, and Methods.” Journal 
of Urban Planning and Development  146 (2): 04020007. https://doi.
org/10.1061/(ASCE)UP.1943-5444.0000566.
Pekel, J.-F., A. Cottam, N. Gorelick, and A.S. Belward. 2016. “High-
Resolution Mapping of Global Surface Water and Its Long-
Term Changes.” Nature 540 (December): 418–22. https://doi.
org/10.1038/nature20584.
Pietilä, M., M. Neuvonen, K. Borodulin, K. Korpela, T. Sievänen, and L. 
Tyrväinen. 2015. “Relationships between Exposure to Urban Green 
Spaces, Physical Activity and Self-Rated Health.” Journal of Outdoor 
Recreation and Tourism 10 (July): 44–54. https://doi.org/10.1016/j.
jort.2015.06.006.
Pool, J.-R., D. Gibbs, S. Alexander, and N. Harris. 2022. “5 Reasons 
Cities Should Include Trees in Climate Action.” Insights (blog), July 28. 
https://www.wri.org/insights/urban-trees-city-climate-action.
Potapov, P., M.C. Hansen, A. Pickens, A. Hernandez-Serna, A. Tyu -
kavina, S. Turubanova, V. Zalles, et al. 2022. “The Global 2000–2020 
Land Cover and Land Use Change Dataset Derived from the Landsat 
Archive: First Results.” Frontiers in Remote Sensing 3 (April). https://
doi.org/10.3389/frsen.2022.856903.
Prakash, M., S. Ramage, A. Kavvada, and S. Goodman. 2020. “Open 
Earth Observations for Sustainable Urban Development.” Remote 
Sensing 12 (10): 1646. https://doi.org/10.3390/rs12101646.
Runfola, D., A. Anderson, H. Baier, M. Crittenden, E. Dowker, S. Fuhrig, 
S. Goodman, et al. 2020. “GeoBoundaries: A Global Database of Politi -
cal Administrative Boundaries.” PLOS ONE  15 (4): e0231866. https://
doi.org/10.1371/journal.pone.0231866.
Salcedo-Sanz, S., P. Ghamisi, M. Piles, M. Werner, L. Cuadra, A. 
Moreno-Martínez, E. Izquierdo-Verdiguier, J. Muñoz-Marí, A. Mosavi, 
and G. Camps-Valls. 2020. “Machine Learning Information Fusion in 
Earth Observation: A Comprehensive Review of Methods, Applica -
tions and Data Sources.” Information Fusion  63 (November): 256–72. 
https://doi.org/10.1016/j.inffus.2020.07.004.
Sathyakumar, V., R. Ramsankaran, and R. Bardhan. 2020. “Geospatial 
Approach for Assessing Spatiotemporal Dynamics of Urban Green 
Space Distribution among Neighbourhoods: A Demonstration in 
Mumbai.” Urban Forestry & Urban Greening 48 (February): 126585. 
https://doi.org/10.1016/j.ufug.2020.126585.
Shindell, D.T. 2015. “The Social Cost of Atmospheric Release.” Climatic 
Change 130 (2): 313–26. https://doi.org/10.1007/s10584-015-1343-0.

TECHNICAL NOTE   |  March 2023  |  33
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
Song, Y., and P. Wu. 2021. “Earth Observation for Sustainable In -
frastructure: A Review.” Remote Sensing  13 (8): 1528. https://doi.
org/10.3390/rs13081528.
Stanley, T., and D.B. Kirschbaum. 2017. “A Heuristic Approach to Global 
Landslide Susceptibility Mapping.” Natural Hazards  87 (May): 145–64. 
https://doi.org/10.1007/s11069-017-2757-y.
Sugiarto, W. 2022. “Impact of Wildlife Crossing Structures on Wildlife-
Vehicle Collisions.” Transportation Research Record , August. https://
doi.org/10.1177/03611981221108158.
Thomson, D.R., D.R. Leasure, T. Bird, N. Tzavidis, and A.J. Tatem. 
2022. “How Accurate Are WorldPop-Global-Unconstrained Gridded 
Population Data at the Cell-Level? A Simulation Analysis in Urban 
Namibia.” PLOS ONE 17 (7): e0271504. https://doi.org/10.1371/jour -
nal.pone.0271504.
Thrasher, B., E.P. Maurer, C. McKellar, and P.B. Duffy. 2012. “Technical 
Note: Bias Correcting Climate Model Simulated Daily Temperature 
Extremes with Quantile Mapping.” Hydrology and Earth System Sci -
ences 16 (9): 3309–14. https://doi.org/10.5194/hess-16-3309-2012.
Tsendbazar, N., L. Li, M. Koopman, S. Carter, M. Herold, I. Georgieva, 
and M. Lesiv. 2021. WorldCover Product Validation Report, Version 1.1 . 
Paris: European Space Agency. https://esa-worldcover.s3.eu-cen -
tral-1.amazonaws.com/v100/2020/docs/WorldCover_PVR_V1.1.pdf.
Tuholske, C., K. Caylor, C. Funk, A. Verdin, S. Sweeney, K. Grace, P. Pe -
terson, and T. Evans. 2021. “Global Urban Population Exposure to Ex -
treme Heat.” Proceedings of the National Academy of Sciences of the 
United States of America 118 (41): e2024792118. https://doi.org/10.1073/
pnas.2024792118.
UNEP-WCMC (United Nations Environment Programme World 
Conservation Monitoring Centre) and IUCN (International Union for 
Conservation of Nature). n.d. (Database.) Protected Planet: The World 
Database on Protected Areas (WDPA). https://www.protectedplanet.
net/. Accessed October 4, 2022.
UN-Habitat (United Nations Human Settlements Programme). 
2020. Metadata on SDGs Indicator 11.7.1. Nairobi: UN-Habitat. https://
unhabitat.org/sites/default/files/2020/11/metadata_on_sdg_indica -
tor_11.7.1_02-2020_1.pdf.
UN-Habitat. 2022. Metadata on SDGs Indicator 15.1.1 . Nairobi: 
UN-Habitat. https://unstats.un.org/sdgs/metadata/files/Meta -
data-15-01-01.pdf.
United Nations. n.d. “Goal 11.” https://sdgs.un.org/goals/goal11. Ac -
cessed December 13, 2022.
van der Kamp, J. 2017. Social Cost-Benefit Analysis of Air Pollution 
Control Measures: Advancing Environmental-Economic Assessment 
Methods to Evaluate Industrial Point Emission Sources . Karlsruhe, 
Germany: Karlsruher Institut für Technologie. https://doi.org/10.5445/
KSP/1000072046.
van Donkelaar, A., M.S. Hammer, L. Bindle, M. Brauer, J.R. Brook, M.J. 
Garay, N.C. Hsu, et al. 2021. “Monthly Global Estimates of Fine Particu -
late Matter and Their Uncertainty.” Environmental Science & Technol -
ogy 55 (22): 15287–300. https://doi.org/10.1021/acs.est.1c05309.
Volin, E., A. Ellis, S. Hirabayashi, S. Maco, D.J. Nowak, J. Parent, and R.T. 
Fahey. 2020. “Assessing Macro-scale Patterns in Urban Tree Canopy 
and Inequality.” Urban Forestry & Urban Greening 55 (November): 
126818. https://doi.org/10.1016/j.ufug.2020.126818.
Wang, C., Z.-H. Wang, and J. Yang. 2018. “Cooling Effect of Urban Trees 
on the Built Environment of Contiguous United States.” Earth’s Future 
6 (8): 1066–81. https://doi.org/10.1029/2018EF000891.
Wang, Y., C. Huang, Y. Feng, M. Zhao, and J. Gu. 2020. “Using Earth 
Observation for Monitoring SDG 11.3.1-Ratio of Land Consumption 
Rate to Population Growth Rate in Mainland China.” Remote Sensing  
12 (3): 357. https://doi.org/10.3390/rs12030357.
Ward, P.J., H.C. Winsemius, S. Kuzma, M.F.P. Bierkens, A. Bouwman, 
H.D. Moel, A.D. Loaiza, et al. 2020. “Aqueduct Floods Methodology.” 
Technical Note. Washington, DC: World Resources Institute. https://
www.wri.org/research/aqueduct-floods-methodology.

34  |  
  
Wellmann, T., A. Lausch, E. Andersson, S. Knapp, C. Cortinovis, J. 
Jache, S. Scheuer, et al. 2020. “Remote Sensing in Urban Planning: 
Contributions towards Ecologically Sound Policies?” Landscape and 
Urban Planning 204 (December): 103921. https://doi.org/10.1016/j.
landurbplan.2020.103921.
WHO (World Health Organization). 2021. WHO Global Air Quality 
Guidelines: Particulate Matter (PM 2.5 and PM10
 ), Ozone, Nitrogen Diox -
ide, Sulfur Dioxide and Carbon Monoxide . Geneva: WHO. https://www.
who.int/publications-detail-redirect/9789240034228.
Wilson, S.J., E. Juno, J.-R. Pool, S. Ray, M. Phillips, S. Francisco, and S. 
McCallum. 2022. Better Forests, Better Cities . November. https://www.
wri.org/research/better-forests-better-cities.
WorldPop. n.d. “WorldPop Global Population Data.” Earth Engine Data 
Catalog. https://developers.google.com/earth-engine/datasets/cata -
log/WorldPop_GP_100m_pop. Accessed November 8, 2022.
Zanaga, D., R. Van De Kerchove, W. De Keersmaecker, N. Souverijns, 
C. Brockmann, R. Quast, J. Wevers, et al. 2021. “ESA WorldCover 10 m 
2020 V100.” Zenodo. https://doi.org/10.5281/zenodo.5571936.
Zerger, A., and D.I. Smith. 2003. “Impediments to Using GIS for Real-
Time Disaster Decision Support.” Computers, Environment and Urban 
Systems 27 (2): 123–41. https://doi.org/10.1016/S0198-9715(01)00021-7.

TECHNICAL NOTE   |  March 2023  |  35
Calculating indicators from global geospatial data sets for benchmarking and tracking change in the urban environment
ACKNOWLEDGMENTS
This research was made possible by the UrbanShift and 
Cities4Forests initiatives. We are thankful for the financial support 
to those initiatives from the Global Environment Facility and the UK 
Department for Environment, Food and Rural Affairs, respectively, 
which supported this research. 
The authors would like to thank the reviewers and advisers 
who provided input on this research (unless otherwise noted, 
organizational affiliations are WRI): Becky Atkins, Ignacio Bernabe, 
Alejandra Bosch, Beatriz Cárdenas, Ingrid Coetzee (ICLEI), Gennadii 
Donchyts (Google), Jessica Ertel, Catyana Falsetti, Gloria Ferreyra, 
David Gibbs, Argyro Kavvada (NASA), Robin King, Samantha Kuzma, 
Jiaying Lin, Marc Manyifika, John-Rob Pool, Jaap Schellekens (Planet), 
Bongiwe Simka (ICLEI), Gregory Taff, Wubanchi Tesso, and Mthobisi 
Wanda (ICLEI). Additionally, we would like to thank representatives 
of participant cities and liaisons who provided input on this research 
and presentations of the findings through surveys, focus groups, and 
interviews: Suryani Amin (ICLEI), Jessy Appavoo (C40 Cities), Ignacio 
Bernabe, Lara Caccia, Constant Cap (Code for Africa), Héctor Miguel 
Donado, Roger Mambeta Ndona, Bhaskar Padigala (ICLEI), Wubanchi 
Tesso, and Ji Xu (ICLEI).
Thanks also to the advisory group for the geospatial and data 
governance work of UrbanShift: Christoph Aubrecht (ESA), Zoltan 
Bartalis (ESA), Merlin Chatwin (Open North), Thomas Esch (German 
Aerospace Center), Dennis Mwaniki (UN-Habitat), Laura Parry 
(CDP), Steven Ramage (Group on Earth Observations), Stefaan 
Verhulst (New York University GovLab), and Dylan Weakley (City of 
Johannesburg). 
Thanks also to the WRI program, technical, and operational staff who 
made this work and publication possible: Sadof Alexander, Timothy 
Anderegg, James Anderson, Logan Byers, Marc Daniels, Todd 
Gartner, Christopher Gillespie, Bruno Hernandez Incau, Manal Khan, 
Pablo Lazo, Beth Olberding, Mariana Orloff, John-Rob Pool, Emilia 
Suarez, and Deborah Valencia.
ABOUT THE AUTHORS
Eric Mackres  is Senior Manager for Data and Tools at WRI Ross 
Center for Sustainable Cities.
Saif Shabou  is an Urban Data and Analytics Associate on the Data 
and Tools team at WRI Ross Center for Sustainable Cities.
Ted Wong is a Research and Project Associate on the Data and 
Tools team at WRI Ross Center for Sustainable Cities.

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
