---
doc_id: 2025_calculating-indicators-from-global-geospatial_3765
source_pdf: kp-docs/askwri-kps/2025_calculating-indicators-from-global-geospatial_3765.pdf
extraction_method: cache-plaintext
char_count: 202320
title: Calculating Indicators From Global Geospatial Data Sets for Benchmarking and Tracking Change in the Urban Environment
authors: Mackres, Eric; Shabou, Saif; Wong, Ted
date_published: 10/29/2025
article_type: Technical Note
wri_primary_office: WRI Global
wri_programs: Cities
language: English
url: "https://www.wri.org/research/calculating-indicators-global-geospatial-datasets-urban-environment"
doi: "http://doi.org/10.46830/writn.22.00123v2"
summary: "Global geospatial datasets—from remote sensing, crowdsourcing, and urban sensors—can generate standardized, comparable urban indicators across seven themes: access to amenities, air quality, biodiversity, flooding, greenhouse gas emissions, heat, and land protection. Using zonal statistics applied to open-source datasets within locally defined administrative boundaries, indicators are calculated for entire cities and subareas, enabling within-city equity analysis disaggregated by age, sex, and informality. Methods align with SDGs, the 15-minute city concept, and 3-30-300 urban greening guidelines. The open-source framework supports low-cost replication globally, particularly benefiting data-scarce regions."
---

# Calculating Indicators From Global Geospatial Data Sets for Benchmarking and Tracking Change in the Urban Environment

TECHNICAL NOTE  |  Version 2.0  |  November 2025  |  1
TECHNICAL NOTE
Calculating indicators from global geospatial 
datasets to benchmark and track changes in the 
urban environment
Eric Mackres, Ted Wong, Saif Shabou, Elizabeth Wesley, and Thet Hein Tun
CONTENTS
Abstract. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
Methods .................................... 3
Indicators ................................... 6
General limitations ......................... 34
Further work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .36
Appendix A. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .37
Endnotes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .40
References ................................. 41
Acknowledgments ......................... 46
About the Authors ......................... 46
About WRI ................................. 46
Technical notes document the research or analytical 
methodology underpinning a publication, interactive 
application, or tool.
Suggested Citation: Mackres, E., T . Wong,  
S. Shabou, E. Wesley, and T .H.Tun. 2025. 
“Calculating indicators from global geospatial 
datasets to benchmark and track changes in the 
urban environment.” Technical Note. Washington, 
DC: World Resources Institute. Available online at 
doi.org/10.46830/writn.22.00123v2.
Abstract
Global datasets derived from remote sensing, urban sensors, crowdsourcing, 
or surveys can provide valuable insights on the current state of cities, how 
cities are changing, and opportunities to improve the urban environment. 
This technical note discusses methods for using these data in combination 
with locally meaningful jurisdictional boundaries to calculate local measure-
ments of indicators on several themes—including access to urban amenities, 
air quality, biodiversity, flooding, climate change mitigation, heat, and land 
protection and restoration—relevant to urban decision-makers, research -
ers, and other stakeholders. The authors identified and prioritized these 
indicators in consultation with program staff and stakeholders from several 
global sustainable urban development initiatives: Cities4Forests; UrbanShift; 
Transformative Urban Coalitions; and Deep Dive Cities from World Resources 
Institute’s Ross Center for Sustainable Cities. We also generated indicator 
calculations for cities of interest for these initiatives. These indicators can help 
urban policymakers and civil society assess differences within their cities; 
make comparisons with other cities; and measure themselves against national 
or global benchmarks, such as the Sustainable Development Goals, or against 
self-defined metrics. We applied geospatial analysis and zonal statistics 
methods to existing published geospatial datasets and relevant administrative, 
statistical, or physical city boundaries to calculate comparable indicators for 
any city or urban area. This methodology can be applied to any area of inter-
est on Earth. Most indicators are based on open-source data, increasing the 
feasibility of repeating, replicating, and scaling the analyses at low marginal 
cost. Although the transferability and comparability of these methods are 
notable strengths of this approach, this note also discusses the limitations of 
this approach for decision-making.

2  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
Introduction
Global datasets derived from sources such as remote sensing, 
urban sensors, crowdsourcing, or surveys can provide valuable 
insights on the current state of cities, how cities are changing, 
differences among cities and among neighborhoods within 
cities, and opportunities to improve the urban environment 
(Prakash et al. 2020; Helmrich et al. 2021). However, these 
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
machine learning—technologies that are quickly generat-
ing new insights about Earth and its urban areas (Fritz et al. 
2019; Kavvada et al. 2020; Niu and Silva 2020; Salcedo-Sanz 
et al. 2020; Ludwig et al. 2021). For the first time, research-
ers and citizen scientists have access to globally standardized, 
open-source, continually updated datasets and methods to help 
answer important questions about how we live and the impacts 
of our present and future activities, from the neighborhood to 
the continent scale. This also means that some information that 
had not been previously collected or made public through local 
methods (e.g., ground-based tree inventories) can be generated 
through alternative means (e.g., remote sensing–based tree cover 
mapping), which are often cheaper and easier to implement 
over large areas. Moreover, using open-source data increases the 
feasibility of repeating, replicating, and scaling the analyses for 
additional cities or time frames at low marginal cost, which can 
be particularly helpful in data-scarce regions or on topics with 
limited local data available.
To help understand the status of development and sustain-
ability in cities and identify existing and potential challenges, 
this paper presents a consistent, replicable approach to calculate 
indicators on seven key themes: access to urban services and 
amenities (ACC), air quality (AQ), biodiversity (BIO), flood-
ing (FLD), climate change mitigation (GHG), heat (HEA), 
and land protection and restoration (LND). Data to measure 
these indicators, as described in this document, were taken 
almost exclusively from global, open-source datasets. However, 
these methods can be customized by including equivalent 
local datasets.  
We calculated indicators to assess the baselines and trends of 
change within each city on identified themes, providing infor-
mation to distinguish patterns within and between cities and 
helping to detect problems and define solutions (e.g., prioritiz-
ing neighborhoods with limited tree cover for a tree-planting 
campaign). The methods are open source, so other researchers 
are also welcome to use the methods and scripts developed 
to process data and make calculations for other cities or with 
different input data. The results will be disseminated to local and 
national governments as well as to civil society stakeholders in 
the context of initiatives supported by World Resources Insti-
tute’s (WRI’s) Ross Center for Sustainable Cities.  
So far, the indicators developed using this framework align with 
themes of interest of four city cohorts with which WRI Ross 
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
communities. The initiative’s focus includes biodiversity, 
climate change, and land degradation, and we have developed 
indicators on these themes. We anticipate that city planning 
and other strategic sustainable urban investment–focused 
staff in municipal governments will use the indicators to 
inform policies, programs, and projects in UrbanShift cities. 
The indicators will also support these initiatives of the 
WRI Ross Center:
 ▪ Transformative Urban Coalitions, which facilitates the 
establishment of coalitions in five Latin American cities to 
develop new strategies for addressing inequality and other 
development challenges, while reducing carbon emissions.

TECHNICAL NOTE  |  November 2025  |  3
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
 ▪ The Deep Dive Cities Initiative, which focuses on locally 
driven strategic projects as entry points to foster long-term, 
cross-sectoral, and transformative change. Through the 
initiative, WRI provides strategic funding and additional 
technical capacity to support a wide range of projects, from 
decarbonizing transportation and enhancing climate action 
to strengthening disaster preparedness and urban resilience.
The themes prioritized and indicators calculated for the city 
cohorts convened by these initiatives were developed in con-
sultation with their staff and stakeholders. An iterative process 
involving meetings with and surveys of staff working directly 
with city stakeholders in 2022 (Cities4Forests account managers 
and UrbanShift regional coordinators) and 2024 (Deep Dive 
Cities engagement leads) provided the main information used 
to identify the most important and relevant themes, define the 
indicators, and organize the presentation of the calculations for 
the cities. Indicator calculations and visualizations for these cit-
ies are publicly accessible through an online dashboard. 
We anticipate that these indicators, and others like them 
calculated using a similar framework, will be relevant to many 
other city cohorts and for other urban themes. Many indicators 
also align with global objectives, such as the urban targets of 
the Sustainable Development Goals (UN n.d.), the “3-30-300” 
guidelines for urban greening (Konijnendijk 2021), and the 
“15-minute city” concept (Moreno et al. 2021). (We briefly 
describe 3-30-300 and other frameworks in the indicator 
descriptions below.) We foresee additional uses of the indica-
tors included in this technical note in other geographies and 
time frames and the development of supplemental indicators on 
existing and new themes and using new data sources. Addition-
ally, we expect to update the indicator calculation methodologies 
for these current city cohorts as new data covering additional 
years become available. 
Some cities may have more granular and detailed relevant data 
for measuring the themes of our indicators. However, even 
those cities can benefit from measurements that are standard-
ized globally, between cities, and over time; provide enhanced 
temporal resolution; and are available worldwide. Additionally, 
these indicators can provide a screening and prioritization 
tool. Global data will rarely, if ever, be more useful than local 
data for monitoring local dynamics, but such datasets can help 
users understand the main challenges faced locally and start 
conversations about addressing them. Even when the lower local 
accuracy levels of global datasets impede local usability, they can 
help generate the conversations needed to identify local con-
cerns and then identify better data. 
Other projects on various urban and nonurban topics have 
developed indicators using zonal statistics derived from global 
geospatial datasets (Bocher et al. 2018; Jing et al. 2019; Cochran 
et al. 2020; Kuffer et al. 2020; Sathyakumar et al. 2020; Boe-
ing et al. 2022; Nicoletti et al. 2022). However, this publication 
presents the first method of this kind developed by WRI to 
include multiple urban themes and focus on the needs of specific 
city cohorts and their questions around urban change, opportu-
nities, and risks. 
Methods
Selection of relevant input datasets 
For several indicators, multiple potential source datasets could 
be used. To select the datasets for use in our indicators, we 
followed a few general principles. We typically chose the dataset 
that met the greatest number of our criteria. In cases where 
there were trade-offs among multiple criteria, we prioritized 
the criteria that were most important to enable consistent and 
meaningful calculations of the specific indicator. We used the 
following criteria to evaluate datasets:
 ▪ Published in a peer-reviewed source
 ▪ Open-source license
 ▪ Globally consistent coverage
 ▪ Recency of data
 ▪ High spatial resolution
 ▪ High accuracy compared with peer data
 ▪ Broad temporal coverage (multiple years of data to enable 
time series comparisons)
 ▪ Likelihood of ongoing support for the source data initiative 
and future updates to the dataset, enabling updates to the 
indicators and tracking over time
 ▪ Compatible spatial and temporal resolution with other 
datasets used for the indicator
To calculate the indicators, we used a general data management 
workflow that we consistently applied across all indicators. We 
also used methods to process specific data relevant to individual 
indicators. We assigned all indicators short name designations 
and organized them into themes, as shown in Figure 1. The defi-
nitions and methodologies we used to calculate the indicators in 
the seven themes below are described in detail in the following 
sections, which are organized and named by theme. 
 ▪ Access to urban services and amenities

4  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
 ▪ Air quality 
 ▪ Biodiversity 
 ▪ Flooding 
 ▪ Climate change mitigation 
 ▪ Heat 
 ▪ Land protection and restoration 
These themes and indicators are not intended to be exhaustive; 
rather, they are tailored to the needs of the specific initiatives 
for which they were originally developed. We anticipate adding 
indicators under these themes and potentially adding themes 
as they are identified as important by cities or other stakehold-
ers. All indicators are subject to limitations and uncertainty 
associated with their methods, as described specifically in 
each indicator section and generally in the “General limi-
tations” section.
General data management workflow
Our general data workflow consisted of five steps to process 
data, as illustrated in Figure 2.
 ▪ 1: Input source data and boundaries. We calculated the 
indicators from a variety of sources of global data, and for 
particular zones, or areas of interest. We defined zones 
based on locally relevant administrative boundaries. For 
each city, we defined boundaries for two administrative 
levels: the overall area of interest (typically a municipality 
or a metropolitan area) and several subareas (typically 
multiple wards or districts within a municipality or multiple 
municipalities within a metropolitan area). The former 
represents the union into a single polygon of the multiple 
geographies of the latter. In most cases, we obtained the 
sources of these boundaries from a polygon file or map 
received from the local government or from a national 
statistical agency. If such a local data source was not 
easily accessed, we retrieved the boundaries from a global 
database such as geoBoundaries (Runfola et al. 2020) or 
INDICATORS
THEMES Air quality
Air pollutant emissions 
and costs
High pollution days
Fine particulate matter 
exposure (area-
weighted)
Fine particulate matter 
exposure (population-
weighted)
Biodiversity
Natural 
areas
Habitat connectivity 
(eﬀective mesh size)
Habitat connectivity 
(landscape 
coherence)
Biodiversity in built-
up areas (birds)
Change in number of 
vascular plant species
Change in number of 
bird species
Change in number of 
arthropod species
Flooding
Exposure to coastal 
and river flooding
Future extreme-
precipitation days
Land near natural 
drainage
Impervious  
surfaces
Vegetation cover in 
built areas
Vegetation cover in 
riparian zones
Vulnerability of steep 
slopes
Climate change 
mitigation
Greenhouse gas 
emissions
Greenhouse gas 
impact of trees
Heat
Future heatwave 
frequency
Future extreme 
temperature
Land surface 
temperature
Surface reflectivity
Built land without tree 
cover
Vegetated area
Land protection 
and restoration
Permeable 
areas
Tree cover
Vegetation-covered 
land
Vegetation-covered 
land
Water-covered land
Habitat areas  
restored
Habitat types 
 restored
Protection of Key 
Biodiversity Areas
Protected areas
Built-up Key 
Biodiversity Areas
Access to urban 
services & 
amenities
Recreational space 
per capita
Residential prevalence 
of tree cover
Urban open space for 
public use
Proximity to potential 
employment
Proximity to goods 
and services
Area of tree-covered 
land per resident
Proximity to schools
Proximity to  
public open space
Proximity to  
public green open 
space
Potential employers 
within convenient 
proximity
Proximity to public 
transportation
Proximity to 
healthcare
Hospitals per 1000 
residents
Figure 1 | Themes and indicators described in this document 
Source: WRI authors.

TECHNICAL NOTE  |  November 2025  |  5
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
OpenStreetMap (OSM).3 Where multiple options were 
available, we consulted stakeholders, generally through WRI 
country offices and the managers of program partners, on 
the most appropriate boundaries to use. We also considered 
maps of the extent of regional urban agglomerations as an 
alternative definition of the city boundary, using urban-
extent areas as classified from built-up density by Angel et 
al. (2024). For indicators that use a time series of data and 
for regions where boundaries may have changed over time, 
we used only the most recent available boundaries for our 
calculations to hold the region of study constant. We then 
saved the boundaries for each area of interest as GeoJSON 
files with a standard naming schema.
The sources of the global data required to calculate each indi-
cator are described with the indicators, below. We obtained 
some data through application programming interfaces 
(APIs) maintained by the organizations providing the data. 
API-derived data include species-observation data from the 
Global Biodiversity Information Facility, locations of urban 
amenities and street networks from OpenStreetMap, and 
air-pollutant concentrations from the Copernicus Atmo-
sphere Monitoring Service. We retrieved some data from 
Google Earth Engine (GEE) (Gorelick et al. 2017), which 
collects, stores, and provides researchers with a rich collection 
of environmental data. GEE-served data include popula-
tion estimates from WorldPop, the NEX-GDDP-CMIP64 
downscaled climate simulation outputs, and reflectance and 
greenness data from the Sentinel-2 satellite mission (ESA 
2015b). We obtained some data directly from data-providing 
organizations. We stored these data for our use in calculat-
ing indicators. These data include the Key Biodiversity 
Areas from BirdLife International and concentrations of 
fine particulate matter from the Atmospheric Composition 
Analysis Group at Washington University in St. Louis. The 
specific datasets named here are only a subset of the datasets 
in each category, and we provide more detailed descriptions 
and citations in the indicator descriptions. We also obtained 
metadata to accompany the data, and we make information 
from the metadata available with the indicators. 
 ▪ 2–3: Compute and store layers and indicators. From the 
source data, we calculated layers and indicators. Layers 
are spatially explicit data, calculated for the entire area of 
interest, which can be useful for understanding the spatial 
pattern of environmental or social factors relevant to city 
decision-making. Layers take the form of raster data (stored 
in GeoTIFF format) or vector data (stored as GeoJSON 
files). Indicators are data that summarize or synthesize 
layer data, calculated as a single numerical value either for 
the entire area of interest or each administrative district. 
Indicators are stored as tables. We used the defined boundary 
extents to extract the data for each city area of interest from 
global datasets relevant to calculating one or more indicator.
We processed the source data into layers and calculated 
the indicators from layers using Python scripts that call 
on a collection of open-source libraries written in Python, 
R, and Java. All Python scripts and their dependencies are 
made available through the Cities Indicators Framework 
(CIF).5 We stored layer datasets and indicator tables for each 
city, using a common data schema to facilitate provision 
of data through the CIF API. Storage is currently in a set 
of S3 (Simple Storage Service) buckets provided by Ama-
zon Web Services.
 ▪ 4–5: Publish and visualize. Layer and indicator data for 
any of our project cities, along with metadata, are available 
through the Cities Indicators API.6 Data can also be 
visualized in the CitiesMetrics Dashboard,7 which provides 
a user-friendly interactive interface for viewing data as maps 
and tables; comparing data among cities; and downloading 
layer data, indicator data, and map images.
Disaggregation and time series
We calculated and report some indicators for a variety of sub-
populations or years of interest.
For indicators that describe the exposure of city residents or 
built-up areas to environmental hazards or proximity of city 
amenities to residents, we calculated indicator values for both 
the general population and separately for some subpopulations 
that might vary in their vulnerability to hazards or their need to 
make use of amenities. The subpopulations for which we made 
these calculations are children, elderly persons, female persons, 
and residents of areas with informal development.
Some indicators are based not on population, but on area of 
land. For several heat-related indicators (HEA-3–HEA-5, 
which address land surface temperature, surface reflectivity, and 
vegetation), we report indicators calculated for total city area and 
for the subset of the city area that is simultaneously classified 
as built-up and having informal development. These indicators 
address heat hazards that are of particular concern in built-up 
areas, and informality in built-up areas is a vulnerability class for 
which we wish to provide separate information.
For indicators for which we have more than one year of data, we 
allow users to choose years of interest. We report some indica-
tors as time series and provide values as tables and multiyear 
plots. Indicators that are reported as time series include those

6  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
describing concentrations of greenhouse gases and other pol-
lutants, estimates of species richness, and indicators built on 
estimates of vegetative cover.
Indicators
Access to urban services and amenities 
(ACC)
Cities exist because the physical proximity of many kinds of 
activities enables residents to more easily access opportunities 
and collaborate economically. But access to opportunities varies 
considerably within cities. These indicators measure the variation 
in physical access to services and amenities within cities. Ameni-
ties in this paper include parks, schools, health care facilities, 
public transportation stops, places for the purchase and sale of 
goods and services, and places that are likely to provide jobs to 
city residents.
While indicators ACC-1 through ACC-5 assess the availability 
of amenities without regard to travel time within the city, indi-
cators ACC-6 through ACC-13 assess the proximity of urban 
amenities to city residents’ homes. The general method for our 
proximity indicators was to do the following:
1. Find the locations of the amenities
2. Find information on the city’s transportation networks
3. Estimate zones describing locations from which a person can 
access at least one amenity location within a given period—
in which case we call the zones isochrone areas—or within 
a given travel distance via a given transportation mode—in 
which case we call the zones isodistance areas
4. Estimate the fraction of the population residing within the 
isochrone or isodistance areas
Travel times, distances, and travel modes used for isochrone and 
isodistance estimates can be customized for particular applica-
tions. To date, we have implemented these indicators only for 
Figure 2 | General data management workflow  
Notes: Abbreviations: AWS = Amazon Web Services; S3 = Simple Storage Service; API = application programming interface. The figure describes the steps we applied to generate 
calculations for each city, data source, and indicator. We used boundaries to extract a spatial subset layer from the source dataset that is relevant to the city. We then stored this subset 
and added its metadata to a data catalog. We applied the indicator methods to the spatial subset, and appended the calculation result for each boundary to a table that stores the 
unique indicator results for each boundary.
Source: WRI authors.
Cities Indicators
Framework
Compute layers
Compute indicators
Global
data
Metadata
CityMetrics 
Dashboard
Cities 
Indicators API
Cities
boundaries
INPUT COMPUTE STORE PUBLISH VISUALIZE
Airtable GitHub AWS S3 FastAPI React

TECHNICAL NOTE  |  November 2025  |  7
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
walking and bicycling. Our implementation can distinguish 
between pedestrian-accessible and pedestrian-inaccessible road-
ways, as coded by citizen mappers in OpenStreetMap. Future 
iterations of this work will calculate isochrone areas and isodis-
tance areas for vehicles in nearly the same way as for walking, 
but with different travel speeds and consideration of one-way 
streets. Future iterations of this work will also incorporate rout-
ing and service-frequency data from public transit agencies, and 
will allow us to address the accessibility of urban amenities via 
bus, metro, and train. Higher values are associated with greater 
or more inclusive access to essential urban amenities.
For most of the amenity classes we address, we calculated 
accessibility for at least the 15-minute walking and bicycling 
isochrone areas and the 400 meter (m) walking isodistance area. 
The 15-minute isochrone areas support cities in assessing align-
ment with the concept of the 15-minute city, which is that all 
city residents should live within a 15-minute walk or bicycle ride 
of all essential urban amenities (Moreno et al. 2021). The 400 
m isodistance areas support assessment under Indicator 1.2.1 
of the Global Urban Monitoring Framework, which addresses 
“the proportion of population living in households with access 
to basic service” (UN-Habitat 2022). Some accessibility indica-
tors include additional distances and/or travel times to support 
assessment against other well-known frameworks such as the 
Sustainable Development Goals and the 3-30-300 guidance 
for urban greening. These alignments are described with the 
relevant indicators.
These accessibility indicators are not meant to assess the overall 
use of the amenities of interest. Rather, we intend to assess the 
ease with which a city resident could access an amenity by walk-
ing, bicycling, or (in future versions of this work) taking public 
transportation. City residents who have private vehicles might 
have easy access to larger areas of cities and greater varieties of 
schools, businesses, and other amenities. However, as poorer 
people often lack access to private vehicles, an assessment of 
equitable access to urban amenities focuses on access by foot, 
bicycle, and public transportation.
ACC-1: recreational space per capita
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
We calculated the recreational services indicator using the fol-
lowing equation:
We took data on recreational areas from the crowdsourced data 
initiative OSM using the OSMnx library (Boeing 2024). The 
OSM tags used to retrieve polygons of these areas were park, 
nature_reserve, common, playground, pitch, and track in the leisure 
category and protected_area and national_park in the boundary 
category. Population data are 2020 unconstrained estimates 
from WorldPop accessed through Google Earth Engine 
(WorldPop n.d.). 
LIMITATIONS
WorldPop’s global gridded unconstrained dataset is built from 
the disaggregation of governments’ census data. The uncon-
strained data, which consider all land area rather than only 
areas with satellite-detectable settlements, can underestimate 
populations in some urban areas. For example, analysis of these 
WorldPop data for Namibia has found large cell-level errors, 
particularly in areas of informal settlements (Thomson et al. 
2022). We used the unconstrained dataset rather than the 
settlement-constrained dataset because it is more likely to be 
updated regularly. If a regularly updated, constrained population 
dataset becomes available, we may choose to use it.
OSM is a crowdsourced dataset with a diverse user community, 
and its completeness, accuracy, and standards of use vary consid-
erably. Accuracy within individual studied cities is not precisely 
known. Some regions lack data on some of their open spaces 
in OSM, but all cities we have analyzed so far have data on the 
sites of at least some open spaces. Additionally, local contribut-
ing communities use the OSM taxonomic system of tags to 
categorize features differently. In selecting the tags used in our 
methods, we considered the most commonly used tags to des-
ignate open spaces available for public use (e.g., parks, athletic 
fields) but attempted to exclude tags used primarily for private, 
limited access or indeterminate open spaces. However, as the 
OSM tagging system is not designed to make this distinction, 
this may result in the exclusion of data on some open spaces

8  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
that are available for public use as well as the inclusion of some 
nonpublic open spaces for some cities. OSM is being constantly 
edited, potentially improving the relevant data for these cities, 
so our download of data from one point in time may become 
outdated. Finally, metadata for OSM features (e.g., parks, roads) 
include when the feature was added or edited in the map but 
typically do not provide information on when it was installed on 
the ground. This makes it difficult to measure changes to cities 
over time using OSM data.
We considered only recreational open space (generally parks) for 
this indicator, so smaller recreational facilities like gymnasiums, 
recreation centers, and smaller swimming pools were excluded. 
City residents typically have access to more recreational oppor-
tunities than are found in recreational open space.
ACC-2: area of tree-covered land per resident
DEFINITION
The area of land with tree canopy of at least 3 m in height 
per city resident.
IMPORTANCE
Trees provide city residents with numerous benefits, like cooling 
through shade and evaporative cooling, mitigation of air pollu-
tion and noise pollution, and support for local biodiversity with 
its attendant benefits. Without attempting to quantify these 
benefits, this indicator reflects the benefit conferred on residents 
by the areal prevalence of tree canopy in the city or district.
METHODS
For population data, we used the unconstrained gridded 
population for 2020 at a 100 m resolution from the WorldPop 
project as retrieved from Google Earth Engine. For tree cover, 
we used tree cover data from the Meta-WRI Global Canopy 
Height dataset (Tolan et al. 2024). We reduced the spatial 
resolution of the 1 m tree-height dataset to align with the 100 m 
population dataset. In so doing, we considered a 100 m pixel to 
represent 30 percent canopy coverage when at least 30 percent 
of the 1 m pixels represented 3 m or more of canopy height. 
The 30 percent threshold aligns with the Nature Based Solu-
tions Institute’s 3-30-300 rule (Konijnendijk 2021), which is 
that every city resident should live within line of sight of at least 
three trees, that neighborhoods should have at least 30 percent 
tree cover, and that every resident should live within 300 m of 
green open space.
There is no standard tree height for defining urban canopy. We 
used a 3 m minimum because in urban settings a tree that is at 
least 3 m in height can cast a downward shadow on pedestrians. 
We divided the area of the city with tree canopy at least 3 m in 
height by the number of residents.
LIMITATIONS
Tolan et al.’s (2024) method for estimating tree canopy height 
was developed and tested for the assessment of forests and 
agroforests for carbon management, not specifically for monitor-
ing sparsely vegetated areas like cities. The Meta-WRI Global 
Canopy Height dataset is based on analysis of recent historical 
satellite data, and its usefulness for long-term change detec-
tion depends on future updates. As with all data derived from 
automated analysis of satellite data, these data are subject to 
error. The estimated mean absolute error in tree canopy height in 
this dataset is 2.8 m.
ACC-3: residential prevalence of tree cover
DEFINITION
The percentage of the populated areas with tree cover of at least 
3 m in height for greater than 30 percent of the area.
IMPORTANCE
Residential prevalence of tree cover is an important indicator 
of quality green space, whether the trees are in public or private 
space. Privately maintained trees also provide a variety of public 
benefits, including improved air quality, heat mitigation, and 
shade. In addition to providing a range of ecosystem services, 
urban forests are increasingly recognized for their socioeconomic 
benefits (Kondo et al. 2017; Martinuzzi et al. 2018, 2021; Volin 
et al. 2020). To align with the 3-30-300 concept (Konijnendijk 
2021), this indicator considers the 30 percent canopy cover-
age rule. Note that we calculated this indicator based on area, 
not population.
METHODS
For population data, we used the unconstrained gridded 
population for 2020 at a 100 m resolution from the WorldPop 
project as retrieved from Google Earth Engine. For canopy 
coverage, we used tree cover data from the Meta-WRI Global 
Canopy Height dataset, which estimates tree canopy height 
from satellite data from the years 2009–20 and estimates tree 
heights within each 1 m pixel (Tolan et al. 2024). For every pixel 
in the population dataset, we examined the canopy-height pixels 
within a distance of 300 m (in a study of the 3-30-300 rule, 
Owen et al. [2024] used a 300 m distance to define neighbor-
hoods). If at least 30 percent of the canopy-height pixels within 
this distance indicated a tree canopy height of at least 3 m, we

TECHNICAL NOTE  |  November 2025  |  9
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
counted the focal population pixel as meeting the “30” rule. The 
indicator value is the sum of the values of the population pixels 
that met the rule, divided by the sum of all the population pixels 
within the city boundary.
We report this indicator using the total population, as well 
as the population disaggregated by sex and age class, and by 
informality of residential settlement. For assessing proximity for 
particular sexes or age groups, we used WorldPop’s age- and sex-
disaggregated unconstrained 100 m population estimates. We 
defined children as persons aged 0–14, which is the age group-
ing for children used by the United Nations (UN) Department 
of Economic and Social Affairs (UN DESA 2022). We defined 
elderly persons as those aged 60 or more years, again in align-
ment with UN practice (UN DESA 2022). To assess proximity 
for residents of informal settlements, we used the WorldPop 
estimates for regions identified as informal development in the 
Intraurban Land Use dataset (Guzder-Williams et al. 2023).
LIMITATIONS
For this indicator, we used a global neighborhood definition that 
does not conform to how many people perceive or experience 
their neighborhoods. An indicator using local data might be 
based on formal or resident-provided neighborhood boundaries.
Informality in the Intraurban Land Use dataset is based on the 
morphological characteristics of buildings as seen in satellite 
imagery. It therefore does not directly assess the provision of 
formal services to residents.
ACC-4: urban open space for public use
DEFINITION
The percentage of the urban extent that is open space 
for public use.
IMPORTANCE
The availability and area of public open space, such as parks, 
are key factors for assessing the quality of life for city residents. 
Open spaces provide ecosystem services, recreation opportu-
nities, and habitat for wildlife. Indicators of open space are 
included in the SDGs (Indicator 11.7.1) (UN-Habitat 2020), 
the Singapore Index on Cities’ Biodiversity (Chan et al. 2021), 
and the IUCN Urban Nature Indexes (IUCN 2023).
This indicator differs from ACC-1 in that it considers the per-
centage of land area devoted to public use, rather than the area 
per resident (or per 1,000 residents).
METHODS
For this indicator, we used polygon data on categories of open 
space as retrieved from OSM using the OSMnx library (Boe-
ing 2024). The OSM tags used to retrieve these areas were 
park, nature_reserve, common, playground, pitch, and track in 
the leisure category and protected_area and national_park in 
the boundary category. For this indicator, we focused on open 
space that is within urbanized areas of the city and therefore 
more easily accessible by a greater population. This is distinct 
from ACC-1, which considers all public open space within the 
jurisdictional boundary, including in nonurbanized areas. To 
constrain our analysis to urbanized areas of the city (areas where 
land is predominantly covered by urban infrastructure, such as 
buildings and streets, and where most people live and work), 
we used data on these areas as derived from the urban extents 
dataset from Angel et al. (2024) to estimate total metropolitan 
area. This dataset estimates boundaries of the metropolitan 
area based on automated classification of satellite imagery. One 
advantage of using this dataset instead of built-up areas within 
the jurisdictional boundary is that it includes land that would be 
excluded by the built-up classification in the ESA WorldCover 
10 m 2021 V200 land-classification map (ESA 2020a, 2020b; 
Zanaga et al. 2021).
LIMITATIONS
Because of the relatively high (10 m) resolution of the World-
Cover dataset and its definition of built-up areas, large- and 
medium-sized urban open spaces that are predominantly green 
areas were excluded. As a result, this indicator best captures 
smaller open spaces, such as pocket parks; open spaces that are 
not predominantly green, such as plazas; and designated parks 
that are a mix of built-up and nonbuilt land, such as historic dis-
tricts. This indicator is a candidate for future revision to use an 
alternative urbanized area mask based on a dataset that provides 
a common, global definition of urbanized areas of cities that is 
less restrictive of green open spaces. See the above discussion of 
the urban extents dataset.
The limitations of OSM described in ACC-1 apply here as well.
ACC-5: hospitals per 1,000 residents
DEFINITION
The number of hospitals per 1,000 residents.
IMPORTANCE
The availability of hospital beds is essential for planning for 
disasters and other major health crises. This indicator supports 
long-term planning for the availability of health care.

10  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
METHODS
For hospital locations, we queried OSM for hospital in the 
amenity category. Points that were within 0.001 degrees of each 
other (approximately 100 m) were considered duplicates; all but 
one duplicate were removed. We estimated the city’s popula-
tion as the sum within city boundaries of the pixel values from 
WorldPop’s unconstrained population estimates, and calculated 
the indicator using the following equation:
LIMITATIONS
The limitations previously described for OSM data and World-
Pop’s unconstrained population estimates apply to this indicator.
This analysis does not consider the capacity, quality, or geo-
graphical accessibility of hospitals.
ACC-6: proximity to public open space
DEFINITION
The percentage of the population within a 300 m walk, 400 m 
walk, 15-minute walk (1,125 m), or 15-minute (3 kilometer 
[km]) bicycle ride of public open space. 
IMPORTANCE
Beyond simply being present, open space must also be easy to 
access. Although accessibility has many elements, physical prox-
imity to open spaces is an important factor affecting who does 
or does not have access. The spatial distribution of open spaces 
across a city, their alignment with population locations, and their 
accessibility within walking distance are all critical factors for 
understanding how many city residents are well served by open 
space. In addition to addressing the 15-minute walking and 
bicycling isochrone areas, we calculated this indicator using a 
300 m isodistance area in alignment with the 3-30-300 rule (see 
ACC-2) and a 400 m isodistance area in alignment with SDG 
11.7.1 (UN n.d.). Fifteen minutes by foot or bicycle corresponds 
in our estimates to 1,125 m and 3 km, respectively. This indica-
tor can also be calculated using distance or travel time via modes 
of transportation other than walking and bicycling.
We report this indicator using the total population, as well 
as the population disaggregated by sex and age class, and by 
informality of residential settlement. To assess proximity by sex 
and age group, we used WorldPop’s age- and sex-disaggregated 
unconstrained 100 m population estimates. To assess proximity 
for residents of informal settlements, we used the WorldPop 
estimates for regions identified as informal development in the 
Intraurban Land Use dataset.
METHODS
This indicator makes use of global unconstrained gridded 
population at a 100 m resolution from the WorldPop proj-
ect as accessed on Google Earth Engine (WorldPop n.d.).  We 
retrieved the sampled points on the perimeters of the open space 
polygons from OSM as in ACC-1. We then used these points 
as focal points to generate isochrone-area and isodistance-
area polygons by the R package r5r (Pereira et al. 2021) or 
the Python package r5py (Fink et al. 2022). We estimated 
travel times for a given network of streets and roads, which we 
obtained from OSM. The population within an isochrone or 
isodistance area was calculated and then converted to a percent-
age by dividing that value by the total population of the area of 
interest. The r5r and r5py packages can calculate isochrones for 
different travel times and different travel modes. For public-
transit travel times, transit-network information for the city 
in question must be provided to r5r and r5py in the form of a 
General Transit Feed Specification (GTFS) file.
We determined walking time using a walking speed of 4.5 km/
hour, the median walking speed in data collected by Schimpl et 
al. (2011). For bicycle speed, we used 12 km/hour, which is the 
default bicycle speed in r5r (Saraiva et al. 2025).
LIMITATIONS
The previously described limitations of OSM data, WorldPop’s 
unconstrained population estimates, and assessments of infor-
mality in the Intraurban Land Use dataset are also relevant to 
this indicator. WorldPop’s age- and sex-disaggregated popula-
tion estimates are based in part on census data and in part on a 
statistical model based on a variety of spatial covariates (Alegana 
et al. 2015). This modeling was developed with rural applications 
in mind and might include unknown biases.
The r5r and r5py packages’ travel-time estimates are based only 
on roadway geometry and type (and, in the case of public transit, 
any available GTFS data on service frequency). They do not 
consider roadway conditions, climate, topography, or other envi-
ronmental factors that affect the ability of persons or vehicles to 
move through transportation networks. These estimates should 
therefore be considered best-case estimates.

TECHNICAL NOTE  |  November 2025  |  11
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
ACC-7: proximity to green public open space
DEFINITION
The percentage of the population within a 300 m walk, 400 m 
walk, 15-minute walk (1,125 m), or 15-minute (3 km) bicycle 
ride of vegetated public open space. 
IMPORTANCE
Trees and other vegetation confer benefits on urban residents, 
including cooling, mitigation of air pollution and noise pollu-
tion, beauty, and habitat for local biodiversity. This indicator is 
identical to ACC-6, but considers only the subset of open space 
that is largely vegetated.
METHODS
Calculation of this indicator is identical to that for ACC-6, 
except that it considers only the open spaces that meet at least 
one of these two criteria:
 ▪ At least 30 percent of the area within the open space 
includes tree cover 3 m or greater in height
 ▪ At least 30 percent of the area within the open space has 
fractional vegetation of at least 0.5.
Fractional vegetation (Fr) is a measure of the areal fraction of 
a patch of land that is covered by living plants calculated using 
data from the Normalized Difference Vegetation Index (NDVI). 
It is a well-respected measure that outperforms many other 
vegetation indicators in being robust both to soil noise and to 
scale effects (Gao et al. 2020). Using the method of Carlson and 
Ripley (1997), we calculated Fr for each pixel using the fol-
lowing equation:
where the so-called endmembers, NDVIveg and NDVInonveg, are 
the NDVI in pixels representing fully vegetated and completely 
unvegetated patches, respectively. Most researchers establish 
endmembers by manually selecting vegetated and unvegetated 
locations within their areas of interest (e.g., Song et al. 2022; 
Wesley and Brunsell 2019; Amiri et al. 2009). Zeng et al. (2000) 
suggest an approach to finding locally appropriate endmember 
values from remote-sensing data, using percentile values of 
NDVI measurements. To avoid NDVI variability associated 
with artifacts and from seasonal changes in vegetation, we 
created and used a composite image of the 90th-percentile 
NDVI value, NDVI90, of the area of interest. We calculated the 
percentiles for each pixel over all the days in the calendar year, 
using only cloud-free pixels. Using percentile values from Gao et 
al. (2020), we took as endmembers the 75th-percentile NDVI90 
value of all pixels classified in the Dynamic World vegetation-
classification dataset (Brown et al. 2022) as either tree, grass, or 
scrub and shrub for NDVIveg, and for NDVInonveg, the 5th-percen-
tile NDVI90 for pixels classified as built-up in Dynamic World. 
We also used NDVI90 in the calculation of Fr.
As with ACC-3, we calculated this indicator using popula-
tion disaggregated by sex and age class, and by informality of 
residential settlement.
LIMITATIONS
The limitations of ACC-3 apply to this indicator.
Our method of defining open green space is based on global data 
and can fail to account for important factors affecting accessibil-
ity by the public and provision of the benefits of urban nature. 
For example, it does not distinguish between woodlands and 
patches dominated by turf and therefore would treat sport fields 
the same as forested parks.
Our method of identifying open space relies on crowdsourced 
OpenStreetMap data. We could not verify each asset’s quality 
or availability to the public, so this indicator might overestimate 
access to open space.
ACC-8: proximity to schools
DEFINITION
The percentage of the population living within a 400 m walk, 
15-minute walk (1,125 m), or 15-minute bicycle ride (3 
km) of a school.
IMPORTANCE
Proximity to schools is an important indicator of the acces-
sibility of education and other social services for children, and 
equitable access to schools drives equitable social and economic 
opportunity more generally ( Joshi 2017). SDGs 4.1 and 4.2 call 
for equitable access to high-quality pre-primary, primary, and 
secondary education. This indicator considers all kindergartens 
and primary and secondary schools within walking distance of 
a city’s resident children. Rodríguez-López et al. (2017) found 
that, on average, urban children tend to use modes of transpor-
tation other than walking when schools are more than 1,250 m 
from their homes.

12  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
METHODS
For school locations, we queried OSM for school in the building 
category and school and kindergarten in the amenity category. 
We used the point locations of the schools as the focal points 
of an isodistance analysis as in ACC-6. We estimated travel 
distances for a given network of streets and roads, which we 
obtained from OSM. The population within the isochrone and 
isodistance areas was calculated and then converted to a percent-
age by dividing that value by the total population of the area of 
interest. The main population of interest is children, or persons 
aged 0–14 years. However, accessibility of school to the entire 
population, to residents of informal settlements, or to children 
residing in informal settlements might also be of interest. 
Isochrone calculations using modes of transportation other than 
walking are contemplated as a future update. We calculated this 
indicator using the citywide population of children, as well as 
the subset of children estimated to be living in informal devel-
opments, as in ACC-3.
We determined walking time using a walking speed of 4.5 km/
hour, the median walking speed in data collected by Schimpl et 
al. (2011). For bicycle speed, we used 12 km/hour, which is the 
default bicycle speed in r5r (Saraiva et al. 2025).
LIMITATIONS
The limitations previously described for OSM and WorldPop 
data, the Intraurban Land Use dataset, and the r5r isodistance 
calculations apply to this indicator.
There is currently no consistent descriptor within OSM data 
to differentiate among levels of school. Countries use differ-
ent terminology to describe categories of schools that differ by 
the grades they offer and ages they serve. The only consistent 
differentiation of educational facilities is between primary or 
secondary education (i.e., elementary through high schools) and 
higher education (i.e., colleges and universities).
ACC-9: proximity to goods and services
DEFINITION
The percentage of the population living within a 400 m walk, 
15-minute walk (1,125 m), or 15-minute (3 km) bicycle ride of 
buildings used for commercial activity, including stores, shop-
ping centers, supermarkets, and restaurants.
IMPORTANCE
Urban residents must have safe, sustainable, and equitable access 
to sites where goods and services are bought and sold. This 
indicator is in alignment with the concept of the 15-minute city 
(Moreno et al. 2021) and considers all sites of commercial activ-
ity within a 15-minute walk or bicycle trip of a city’s residences.
METHODS
For places where goods and services are sold, we queried OSM 
for key-value pairs8 specified as commerce in Table A-1, Appen-
dix A. These included buildings, land parcels, and point locations 
mapped as banks, shops, cafés, fast food, and veterinary offices.
We used the point locations of these sites as the focal points of 
an isochrone analysis as in ACC-6. We estimated travel times 
for a given network of streets and roads, which we obtained 
from OSM. We calculated the population within 400 m iso-
distance areas and 15-minute walking and bicycling isochrone 
areas in r5r or r5py and then converted the value to a percent-
age by dividing that value by the total population of the area of 
interest. We conducted these analyses with the total population, 
women and girls, children, elderly persons, and residents of 
informal settlements.
We determined walking time using a walking speed of 4.5 km/
hour, the median walking speed in data collected by Schimpl et 
al. (2011). For bicycle speed, we used 12 km/hour, which is the 
default bicycle speed in r5r (Saraiva et al. 2025). 
LIMITATIONS
The limitations previously described for OSM and WorldPop 
data, the Intraurban Land Use dataset, and the r5r isochrone 
calculations apply to this indicator.
Regarding the use of walking and bicycling speeds to calculate 
isochrones, our use of a single representative speed for all cal-
culations does not allow our analyses to reflect the variation in 
travel times and of isochrone extent that arise from differences 
in topography, traffic patterns, road and sidewalk conditions, 
traveler age and health, weather, and numerous other factors that 
affect travelers’ experiences on particular routes.
Because of practical limitations, we treated all goods and services 
as a single type. That is, we did not differentiate among banks, 
shops, or cafés, among others. Commercial entities of different 
types often cluster together in commercial neighborhoods, but 
not always. This indicator addresses proximity to any commercial 
entity, not proximity to the full range of commercial activities 
available in a city.

TECHNICAL NOTE  |  November 2025  |  13
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
ACC-10: proximity to potential employment
DEFINITION
The percentage of the population living within a 400 m walk, 
15-minute walk (1,125 m), or 15-minute (3 km) bicycle ride of 
sites of commercial or industrial activity, including stores, shop-
ping centers, supermarkets, offices, schools, and factories.
IMPORTANCE
Urban residents must have safe, sustainable, and equitable access 
to jobs and sites where they can find employment. Employ-
ment is an essential urban amenity in the ideal 15-minute city, 
in which opportunities for work, among other essential social 
functions, exist within easy access by foot or bicycle (Moreno 
et al. 2021). This indicator considers all sites of commercial and 
industrial activity within a 15-minute walk or bicycle trip of a 
city’s residences.
METHODS
We queried OSM for all key-value pairs specified in Appendix 
A, including all categories of potential employer: commerce, 
education, health care and social services, agriculture, government, 
industry, and transportation and logistics. These included point 
locations mapped as banks, shops, cafés, fast food, and vet-
erinary offices.
Isochrones were calculated, and the percentage of the popula-
tion within 400 m or a 15-minute walk or bicycle ride of at least 
one potential employer is reported separately for each employer 
category. We determined walking time using a walking speed 
of 4.5 km/hour, the median walking speed in data collected by 
Schimpl et al. (2011). For bicycle speed, we used 12 km/hour, 
which is the default bicycle speed in r5r (Saraiva et al. 2025).
The point locations of these sites were used as the focal points 
of an isochrone analysis as in ACC-6. We estimated travel times 
for a given network of streets and roads, which we obtained 
from OSM. The population within 15-minute walking and bicy-
cling isochrone areas was calculated in r5r and then converted to 
a percentage by dividing that value by the total population of the 
area of interest.
As with ACC-3, we also calculated this indicator using popula-
tion disaggregated by sex and age class, and by informality of 
residential settlement.
LIMITATIONS
The limitations previously described for OSM, WorldPop data, 
the Intraurban Land Use dataset, and the r5r isochrone calcula-
tions apply to this indicator.
We considered only potential employers. We were unable to 
consider whether employers have vacancies, whether available 
vacancies are well suited to residents within the isochrones, or 
the quality of the jobs. This analysis also considered employment 
only at physical, formal business establishments and as a result 
didn’t consider informal employment or remote employment 
opportunities. 
ACC-11: number of potential employers in 
proximity
DEFINITION
The population-weighted average number of sites of public, 
commercial, or industrial activity, including stores, shopping 
centers, supermarkets, offices, schools, and factories that are 
within a 400 m walk, 15-minute walk (1,125 m), or 15-minute 
(3 km) bicycle ride of each location in the city.
IMPORTANCE
Indicator ACC-10 reflects the proximity to each resident of 
at least one potential employer. It does not reflect how many 
potential employers are nearby and therefore addresses the 
spatial distribution, rather than the volume, of economic activity. 
Indicator ACC-11 reflects the volume of economic activity, and 
hence potential employment, conveniently accessible to city 
residents by walking or bicycling. It is weighted by population, 
so it reflects the experience of an average city resident.
METHODS
As in ACC-10, we retrieved locations of economic activity, using 
all categories in Appendix A, from OSM. We considered points 
that were within 0.0001 degrees of each other (approximately 
11 m) duplicates; all but one duplicate were removed. (Note that 
duplicate points are not a problem for ACC-10.) We calculated 
15-minute walking and bicycling isochrones using r5r. Some of 
these isochrones overlapped. We calculated a raster, each pixel 
of which stores the number of isochrones that intersect with the 
pixel center, generating a count of potential employers acces-
sible from that location. To calculate the population-weighted 
average, we multiplied each pixel value by the fraction of the 
total population that resides in the area represented by that pixel. 
Pixels are equal in area, so the indicator is the mean pixel value 
within the city or district.
We determined walking time using a walking speed of 4.5 km/
hour, the median walking speed in data collected by Schimpl et 
al. (2011). For bicycle speed, we used 12 km/hour, which is the 
default bicycle speed in r5r (Saraiva et al. 2025).

14  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
As with ACC-3, we also calculated this indicator using popula-
tion disaggregated by sex and age class, and by informality of 
residential settlement.
LIMITATIONS
The limitations previously described for OSM and World-
Pop data, the Intraurban Land Use dataset, the r5r isochrone 
calculations, and the challenges of using OSM data to represent 
potential jobs apply to this indicator. 
Our method of removing duplicates might have removed 
records of genuinely separate businesses that appeared to occupy 
the same location. This error could occur due to human error 
on behalf of the OSM mapper, because the locations are closer 
together than 0.0001 degrees, or because one of the businesses 
is directly above the other in a multilevel building. This indica-
tor might underestimate the density of potential employers, 
especially in dense cities. Removing duplicates is a conceptual 
and technical challenge, and improving our method of doing so 
is a priority for future work.
This indicator does not consider the quality, availability, or 
number of jobs at sites identified as potential employers.
ACC-12: proximity to public transportation
DEFINITION
The percentage of the population living within a 500 m walk, 
15-minute walk (1,125 m), or 15-minute (3 km) bicycle ride of 
a public bus, tram, trolley, subway, train, ferry, or aerialway stop.
IMPORTANCE
Equitable access to public transportation allows a city’s residents 
more sustainable and equitable access to a greater quantity and 
variety of economic, social, and recreational amenities. This indi-
cator directly supports Global Urban Monitoring Framework 
Indicator 1.2.2 and SDG Indicator 11.2.1, which measure a 
population’s convenient access to public transportation. UN-
Habitat considers a transit stop to be conveniently accessible if it 
is within a 500 m walk (UN-Habitat 2018, 2022). Because a 500 
m isodistance area is similar to a 400 m isodistance area, we did 
not calculate this indicator using a 400 m isodistance area.
METHODS
For transit stop locations, we queried OSM for the following:
 ▪ Ferry terminal in the amenity category
 ▪ Stop, platform, halt, tram stop, subway entrance, and station in 
the railway category
 ▪ Bus stop and platform in the highway category
 ▪ Platform, stop position, and stop area in the public 
transport category
 ▪ Subway in the station category
 ▪ Station in the aerialway category
We used the point locations of these sites as the focal points of 
an isochrone analysis as in ACC-6. We estimated travel times 
for a given network of streets and roads, which we obtained 
from OSM. Population estimates are from WorldPop uncon-
strained 100 m gridded population estimates. The population 
within the isochrone or isodistance area was calculated and then 
converted to a percentage by dividing that value by the total 
population of the area of interest. We conducted these analyses 
with the total population, women and girls, children, elderly 
persons, and residents of informal settlements.
Walking time was determined using a walking speed of 4.5 km/
hour, the median walking speed in data collected by Schimpl et 
al. (2011). For bicycle speed, we used 12 km/hour, which is the 
default bicycle speed in r5r (Saraiva et al. 2025). 
LIMITATIONS
The limitations previously described for OSM data, WorldPop’s 
unconstrained population estimates, assessment of informal-
ity in the Intraurban Land Use dataset, and the r5r isodistance 
calculations apply to this indicator. In addition, we did not 
have global access to data on the frequency of transit vehicles 
or the importance of particular stops in terms of route popular-
ity or connectivity. Our method treated all stops as equivalent 
to one another.
ACC-13: proximity to health care
DEFINITION
The percentage of the population living within a 400 m walk, 
15-minute walk (1,125 m), or 15-minute (3 km) bicycle ride of 
a hospital, clinic, or doctor’s office.
IMPORTANCE
Reducing travel distance to hospitals is associated with 
improved health outcomes, including outcomes in cardiac crises 
and unintentional injuries (Buchmueller et al. 2006), maternal 
and perinatal outcomes from childbirth (Minion et al. 2022), 
and preventative care (Dai 2010). This indicator supports 
assessment of the spatial accessibility of hospitals, clinics, and 
doctors’ offices.

TECHNICAL NOTE  |  November 2025  |  15
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
METHODS
For health care facility locations, we queried OSM 
for the following:
 ▪ Doctors and hospital in the amenity category
 ▪ Clinic and hospital in the building category
We used the point locations of these sites as the focal points of 
an isochrone or isodistance analysis as in ACC-6. We estimated 
isochrone and isodistance polgygons for a given network of 
streets and roads, which we obtained from OSM. We retrieved 
population estimates from WorldPop unconstrained 100 m 
gridded population estimates. The 400 m distance threshold 
aligns with Global Urban Monitoring Framework Indicator 
1.2.1 (UN-Habitat 2022). We calculated the population within 
the isochrone or isodistance areas and then converted that value 
to a percentage by dividing it by the total population of the area 
of interest. We conducted these analyses with the total popula-
tion, women and girls, children, elderly persons, and residents of 
informal settlements.
We determined walking time using a walking speed of 4.5 km/
hour, the median walking speed in data collected by Schimpl et 
al. (2011). For bicycle speed, we used 12 km/hour, which is the 
default bicycle speed in r5r (Saraiva et al. 2025).
LIMITATIONS
The limitations previously described for OSM data, WorldPop’s 
unconstrained population estimates, the Intraurban Land Use 
dataset, and the r5r and r5py isodistance calculations apply to 
this indicator.
This analysis treats hospitals, clinics, and doctors’ offices as 
equivalent, despite the large differences in capacity among these 
types of health care facilities.
Air quality (AQ)
Air quality is a major factor in the physical health of urban 
residents. Cities both produce air pollution and are impacted 
by pollution. These indicators measure city contributions to air 
pollution and resident exposure to pollution. Higher values are 
associated with greater hazard, exposure, or vulnerability.
AQ-1: air pollutant emissions
DEFINITION
The annual air pollutant emissions from city areas (tonnes) 
and related social costs (in US dollars), disaggregated by pol-
lutant and sector.
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
dataset of the Copernicus Atmosphere Monitoring Service 
(CAMS) and the Emissions of atmospheric Compounds and 
Compilation of Ancillary Data (ECCAD) (Granier et al. 
2019).9 The dataset provides annual estimates of emissions from 
12 sectors of human activity, on a 0.1-degree (approximately 11 
km) spatial resolution. The estimates are based on simulations 
and historical data and are updated intermittently. The included 
sectors are agriculture (livestock); agriculture (soils); agriculture 
(waste burning); power generation; fugitive emissions; industry; 
combustion in residential, commercial, and other settings; ships; 
solvents; solid waste and wastewater; off-road transportation; 
and on-road transportation.
We used Google Earth Engine to calculate the emissions from 
within our areas of interest (city administrative boundaries). We 
extracted annual, sector-disaggregated emissions in tonnes per 
year for each of the health-related pollutant species available in 
the dataset: black carbon (BC), methane (CH4), carbon monox-
ide (CO), nitrogen oxides (NOx), sulfur dioxide (SO2), organic 
carbon (OC) compounds, ammonia (NH3), and non-methane 
volatile organic compounds (NMVOCs). Because of the coarse 
resolution of this dataset, we report values for the geographic 
area of only the full city and not for each subcity area. 
LIMITATIONS
The emissions data used for this indicator account for only 
direct emissions from activities within the boundaries of the 
city (Scope 1 emissions). They do not account for emissions 
associated with electricity that is used in the city but generated 
elsewhere (Scope 2); or emissions produced elsewhere associated 
with products or services consumed in the city (Scope 3), such 
as air pollution from fires in formerly forested areas cleared to 
produce agricultural commodities consumed in cities, including 
beef and palm oil. Additionally, this analysis does not provide 
information on where the social cost of these emissions accrues. 
Because pollution travels and most costs are associated with 
pollution exposure, not emissions, many of the costs associated 
with pollution from the city may be experienced outside the city.

16  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
The CAMS dataset is modeled data based on an ensemble of 
multiple emissions models and is subject to the limitations of 
those models. The methods used to develop the CAMS emis-
sions dataset are described in Granier et al. (2019).
Some audiences might be accustomed to seeing pollutant 
concentrations reported on a per-capita or per-area basis. After 
conducting additional research into our target users’ preferences, 
we might change our reporting of this indicator to a per-capita 
or per-area basis.
AQ-2: social cost of air pollution
DEFINITION
The estimated cost to society of air pollution, in US 
dollars per year.
IMPORTANCE
AQ-1 reports air pollution in terms of pollutant concentration, 
but concentrations can be difficult to interpret. This indica-
tor expresses the information in AQ-1 in terms of estimated 
monetary cost to society of the health damage caused by air 
pollution. The social cost can be used for cost-benefit analyses 
and to communicate the urgency of air quality interventions.
METHODS
We converted tonnes of pollutant from AQ-1 to US dollars 
based on health-related social costs per tonne (Table 1) as 
estimated by Shindell (2015) for all pollutant species except 
NMVOCs. For the social cost of NMVOCs, we used the 
median value for NMVOCs emitted below an elevation of 100 
m in van der Kamp (2017). Van der Kamp’s estimates are in 
2015 €, which we converted to 2015 US$ at €1 = $1.11. We 
report annual emissions and social costs as a time series for the 
years 2000–24. Provision of future years’ data will depend on the 
availability of updates to the CAMS data.
We summed the daily cost for each pollutant species over the 
year in question and report the annual sum.
LIMITATIONS
The limitations of our method of estimating pollutant con-
centrations in AQ-1 apply to this indicator. In addition, our 
simple method of converting concentrations to social cost ignore 
enormous complexities in atmospheric mixing, health impacts, 
the societal cost of health impacts, and the values of currencies 
relative to the US dollar. The estimates we provide based on 
global data should not be used in place of local studies using 
local data and assumptions.
AQ-3: high pollution days
DEFINITION
The annual number of days that air pollutants were above World 
Health Organization (WHO) air quality standards in the 
year of interest.
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
Reanalysis EAC4 dataset (Inness et al. 2019), which combines 
satellite monitoring of pollutant concentrations with atmo-
spheric modeling to estimate concentrations near the Earth’s 
surface.10 The EAC4 data are provided at an approximately 80 
Table 1 | Estimated social cost for each pollutant species
POLLUTANT SPECIES SOCIAL COST PER 
TONNE (US$)
Ammonia (NH3) 22,000 a 
Black carbon (BC) 62,000a
Carbon dioxide (CO 2) 0a
Carbon monoxide (CO) 250a
Methane (CH4) 740a
Nitrogen oxides (NO x) 67,000a 
Non-methane volatile organic compounds (NMVOCs) 1,172b
Organic carbon (OC) 51,000a
Sulfur dioxide (SO 2) 33,000a 
Notes: a Nonclimate health-related costs are estimated in Shindell (2015). b The median 
cost across four German regions for emissions below 100 meters, as estimated in van 
der Kamp (2017).
Source: WRI authors.

TECHNICAL NOTE  |  November 2025  |  17
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
km spatial resolution. Because of the coarse resolution of this 
dataset, we report values for the geographic area of only the full 
city and not for each subcity area.
We report the number of days each city was estimated in the 
year of interest to have had a near-surface concentration of 
air pollutants that exceeded WHO’s standards for outdoor air 
pollutants (WHO 2021). The indicator is reported as a time 
series of annual values. Table 2 outlines the pollutants and 
standards used. 
LIMITATIONS
The CAMS data have uncertainty related to the limitations 
of the atmospheric modeling methods used. Additionally, 
the low resolution of the dataset does not allow for analysis 
of subcity geographic units and may introduce uncertainty to 
the city-scale calculations due to aggregated data from an area 
larger than the city.
AQ-4: exposure to fine particulate matter
DEFINITION
The population-weighted annual mean fine particulate matter 
(PM2.5) concentration as a percentage of the WHO’s air quality 
guideline for annual exposure.
IMPORTANCE
PM2.5 consists of very small particles with diameters of 2.5 
micrometers (µm) or less. (For comparison, a typical human hair 
has a diameter of 50–70 µm.) PM2.5 is released from combus-
tion (including fuel combustion in vehicles and power plants, 
the use of wood and other biomass for cooking and heating, as 
well as wildfires), degradation of vehicle tires during use, and 
some chemical processes that occur in the atmosphere. PM2.5 is 
a serious health concern because the small size allows PM2.5 par-
ticles to travel deep into human lungs, enter the bloodstream, 
and cause direct damage to internal organs. Long-term exposure 
to PM2.5 leads to increased incidence of heart and lung diseases, 
cancers, and premature death (Feng et al. 2016; WHO 2021). 
This indicator can help decision-makers determine how many 
city residents face long-term exposure to dangerous levels of 
PM2.5 and in which neighborhoods these residents live.
METHODS
For this indicator, we used the global surface PM2.5 V5.
GL.02 dataset from the Atmospheric Composition Analysis 
Group at Washington University in St. Louis (van Donkelaar 
et al. 2021).11 This dataset combines models of atmospheric 
mixing and chemistry with analysis of imagery from the 
Moderate Resolution Imaging Spectroradiometer, Multi-
angle Imaging SpectroRadiometer, and Sea-viewing Wide 
Field-of-view Sensor satellite instruments from the National 
Aeronautics and Space Administration (NASA) to generate 
estimates of PM2.5 concentrations near the Earth’s surface. 
The data are provided at a spatial resolution of 0.01 degrees, or 
approximately 1.1 km.
For each year of interest, we found the average PM2.5 concentra-
tion for each 0.01-degree pixel within the city boundary, and 
weighed it by the fraction of the total population that was found 
within that pixel. Population data are the 2020 unconstrained 
estimates from WorldPop. We report the population-weighted 
concentration as a percentage of the WHO’s air quality guide-
line (recommended maximum level) for annual exposure: 5 µg 
Table 2 | WHO standards for outdoor air pollutants 
POLLUTANT SPECIES AVERAGING TIME (HOURS) A WHO-RECOMMENDED AIR QUALITY GUIDELINE MAXIMUM LEVEL
Carbon monoxide (CO) 24 4,000 µg/m 3 
Coarse particulate matter (PM 10) 24 45 µg/m3 
Fine particulate matter (PM 2.5) 24 15 µg/m3 
Nitrogen dioxide (NO 2) 24 25 µg/m3 
Ozone (O3) 8b 100 µg/m3 
Sulfur dioxide (SO 2) 24 40 µg/m3 
Notes: Abbreviations: WHO = World Health Organization; µg/m 3 = micrograms per cubic meter; PM 2.5 = particulate matter of 2.5 micrometers or less in diameter; PM 10 = particulate 
matter of 10 micrometers or less in diameter. a The WHO provides additional guidelines for the same pollutants for other averaging times. b Due to limitations with the Copernicus 
Atmosphere Monitoring Service dataset, for the ozone calculations, we used data for the nine-hour window of 6 a.m. to 3 p.m. In some parts of the world, the highest level of ozone is 
reached after 5 p.m.
Source: WHO 2021.

18  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
per cubic meter (m3) (WHO 2021). We calculated the annual 
average spatially over the area of the district. For example, an 
average concentration of 15 µg/m3 would be reported as 300 
percent of the WHO standard. This indicator is based on the 
WHO annual average concentration recommendation for PM2.5, 
as distinct from the WHO 24-hour average recommendation 
used in indicator AQ-3. We report this indicator as a time series 
for the years 2000–22. Provision of future years will depend on 
the availability of updates to the source dataset. We report time 
series for the general population as well as for children, elderly 
residents, female residents, and residents of areas with infor-
mal development.
LIMITATIONS
The PM2.5 dataset has uncertainty related to the limitations of 
the atmospheric modeling methods that it uses. The concentra-
tion levels we report cannot be directly translated into health 
impacts. The health impacts of air pollution are not linearly 
related to pollutant concentrations, so although higher con-
centrations are worse for health, concentrations at, for example, 
300 percent of the WHO standard should not be interpreted as 
being three times worse than concentrations at 100 percent.
If this indicator is reported only at an all-city level, basing 
this indicator on an all-city average might obscure pollution 
hotspots. For all-city reporting, it might be useful to consider 
reporting the maximum exposure rather than the average. We 
report this indicator at the all-city level as well as for subcity 
administrative districts. 
Biodiversity (BIO)
Cities are often thought of as detrimental to biodiversity—and 
they can have significant negative impacts related to habitat loss 
and resource extraction—but cities can also make choices that 
mitigate biodiversity loss and enhance habitat. 
Most of the indicator methods in this category are based on 
the indicator definitions used in the Singapore Index on Cities’ 
Biodiversity (Chan et al. 2021) and the IUCN Urban Nature 
Indexes (IUCN 2023). Both are widely recognized assessment 
frameworks designed to help assess and track biodiversity and 
its protection within cities. They encompass assessment of 
biodiversity, access to the societal benefits of biodiversity, and 
government structures and processes supporting biodiversity. 
They can be used to assess the status of local biodiversity and the 
conditions that support it as well as identify priority areas for 
future urban biodiversity efforts.
The indexes define indicators and scoring methods, and cit-
ies are invited to adapt the indicators and definitions for their 
own purposes. The indexes do not provide data for calculating 
indicator values, and data acquisition and processing can pose 
challenges for some cities. We provide data supporting a subset 
of the Singapore Index’s and UNI’s indicators that address 
biodiversity and access to benefits. Some of the biodiversity 
indicators do not measure biodiversity directly but rather condi-
tions that support or harm biodiversity. We have defined and 
implemented our indicators to adhere as closely as possible to 
the definitions in the Singapore Index. Our approach prioritizes 
global, publicly available, and peer-reviewed datasets to develop 
indicators; however, cities often have access to local data that are 
of higher quality or are more specifically suited to local con-
texts and needs.
For these indicators, higher values are associated with greater 
biodiversity or greater support for biodiversity.
BIO-1: natural areas
DEFINITION
The percentage of land that is within natural area land classes.
IMPORTANCE
Natural areas support biodiversity by providing habitat. They 
also provide human beings with ecosystem services. The portion 
of the total city area that is close to a natural state thus gives 
information about a city’s biodiversity and about the benefits 
provided by biodiversity.
METHODS
Natural ecosystems, as defined by the Singapore Index, are all 
areas that are not highly disturbed or completely human altered. 
Examples of natural ecosystems include forests, mangroves, 
freshwater swamps, natural grasslands, streams, and lakes. We 
calculated this indicator as the percentage of natural area within 
the city boundary:
We calculated this indicator using the ESA WorldCover 10 
m 2021 V200 land-classification map (Zanaga et al. 2021). 
We included as natural area all land classified in this dataset as 
trees, shrubland, grassland, herbaceous wetland, mangrove, or 
moss and lichen.

TECHNICAL NOTE  |  November 2025  |  19
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
LIMITATIONS
 ▪ The ESA WorldCover 10 m 2020 V100 layer was assessed 
to have overall accuracy of 74.4 percent (Tsendbazar et 
al. 2021). The dataset we used, being similar to the V100 
dataset, is therefore very likely to include errors in land cover 
classification. These errors would be carried through to our 
characterization of natural and nonnatural lands. 
 ▪ The WorldCover dataset has a spatial resolution of 10 m. 
For some wildlife species, patches smaller than 10 m might 
provide useful habitat. WorldCover and our implementation 
of this indicator could fail to account for these tiny patches.
 ▪ Some species have requirements with respect to habitat 
patch size, plant-community composition, level of vegetation 
homogeneity, and composition of nearby land. Our 
method accounts for none of these (or other) potentially 
important ecological details. Biodiversity planning that 
prioritizes particular species or that is informed by a locally 
implemented ecological assessment should contemplate 
augmenting our indicators with local ground truthing and 
habitat classifications defined by local species’ requirements.
 ▪ For many biodiversity-planning purposes, highly managed 
grassy areas such as lawns and golf courses might not be 
considered natural. However, as WorldCover classifies these 
areas as grass, our method classifies them as natural area.
BIO-2 and BIO-3: connectivity of natural lands
DEFINITION
Landscape coherence (BIO-2) and effective habitat mesh size 
(BIO-3) are measures of the connectivity of patches of land that 
can serve as habitat for wild animals. Values for both range from 
0 to 1, with larger values indicating greater ease of animal move-
ment between habitat patches.
IMPORTANCE
In general, contiguous habitat benefits biodiversity better than 
habitat that is subdivided by roads, buildings, and other built 
infrastructure (Forman and Godron 1991; Fahrig 2003). The 
connectivity of habitat patches mitigates the effects of habitat 
fragmentation by allowing wildlife to access more habitat 
without having to cross inhospitable terrain. The fragmentation 
of natural areas affects species differently. For example, a road 
might not be a barrier for birds, but it can seriously fragment 
a population of arboreal primates. Although consideration of 
dispersal ability and habitat requirements are important in the 
management of particular species, the Singapore Index adopts a 
generalist approach to quantifying connectivity based purely on 
patch geometry.
Indicator 3.5 of the IUCN Urban Nature Indexes uses effective 
mesh size as a measure of habitat connectivity (IUCN 2023). 
Indicator 2 of the Singapore Index uses landscape coherence 
(Chan et al. 2021). We calculated both.
PLAIN-LANGUAGE CONCEPTUAL DEFINITIONS
A natural area is land that is hospitable to wild animals. 
Because animal species differ in their habitat requirements, 
the concept of a natural area is necessarily nonspecific and is 
taken by the Singapore Index and by us to encompass natural, 
near-natural, and other lands that are relatively undisturbed by 
human activity.
Connected natural area patches are patches that are separated 
from each other at their nearest points by 100 m at most. Most 
animals can move from one habitat patch to another, crossing 
some distance of inhospitable land. Animal species differ in their 
movement behaviors and their tolerance of nonhabitat environ-
ments, so the Singapore Index uses a generally useful distance 
to define patch isolation. The 100 m threshold was chosen by a 
consensus of expert advisers to the Singapore Index.
Effective mesh size and coherence are landscape measures of 
natural area connectivity. Effective mesh size (EMS) is the 
probability that any two randomly selected points in a city’s 
natural areas will be located in the same contiguous natural 
area patch, or network of connected patches. If the two ran-
dom points represent the locations of two animals of the same 
species, the EMS models the probability that they encounter 
one another. EMS is the sum of the squared areas of each 
natural area patch, divided by the total natural area. (The areas 
of patches that are connected to each other are summed and 
treated as a single patch.) Maximum EMS would indicate a 
landscape in which all natural area exists as a single contiguous 
(or connected) patch: Coherence would be unity. A landscape 
in which natural area is subdivided into many isolated patches 
would have coherence between 0 and unity. Coherence is the 
EMS divided by the total natural area. This normalizes the EMS 
to be between 0 and 1, so that coherence is the sum of squared 
areas of each natural patch, divided by the squared total natural 
area. Because it accounts for the variation in area among cities, it 
is useful for among-city comparisons.
METHODS
We calculated this indicator using the ESA WorldCover 10 m 
2020 V100 land-classification map (Zanaga et al. 2021). We 
included as natural area all land classified as trees, shrubland, 
grassland, herbaceous wetland, mangrove, or moss and lichen.

20  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
We calculated the EMS (BIO-3) using the following equation:
where Atotal is the total area of all natural areas; AG1 to AGn are the 
sizes of each group of connected patches of natural area that are 
distinct from each other; and n is the total number of groups 
of connected patches of natural area. AG1 to AGn may consist of 
areas that are the sum of two or more smaller patches that are 
connected. In general, patches were considered to be connected 
if they were less than 100 m apart. We derived this equation 
from Deslauriers et al. (2018).
We calculated coherence (BIO-2) as coherence = EMS / Atotal.
LIMITATIONS
 ▪ This indicator shares the limitations of BIO-1, which stem 
from unavoidable errors in land classification.
 ▪ This indicator does not currently address roadways as 
particular dangers to animals, despite the well-documented 
role that vehicle collisions play in harming wildlife (Sugiarto 
2022). We would like to integrate roadway information into 
our implementation of future versions of this indicator.
 ▪ We considered two habitat patches to be connected if 
they were no more than 100 m apart. We took the 100 
m threshold from the definition of the corresponding 
indicator in the Singapore Index, but its appearance there 
does not suggest any universal applicability to all types 
of animal movement. Some flying animals are likely to 
tolerate greater distances, and some small animals (especially 
amphibians) cannot traverse 100 m of, say, pavement. 
Biodiversity planning that prioritizes certain animals for 
protection should contemplate implementing this indicator 
using a distance threshold that accounts for the specific 
movement behaviors and physiological tolerances of the 
species of interest.
BIO-4: biodiversity in built-up areas (birds)
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
We calculated the indicator using the following equation:
To delineate built-up areas, we used the ESA WorldCover 2021 
classification of built-up land (Zanaga et al. 2021). For the 
number of bird species, we estimated the saturation levels of 
species-area curves as described for indicators BIO-4, BIO-5, 
and BIO-6, using research-grade observations of birds over 
a five-year period in the crowdsourced iNaturalist database, 
accessed through the Global Biodiversity Information Facility 
(GBIF 2025). Calculations were made using only the observa-
tions that occurred on built-up land and using all observations 
within city boundaries. We report the built-up estimate divided 
by the all-city estimate. 
LIMITATIONS 
This method shares the limitations of BIO-4, BIO-5, and BIO-
6, as well as the following:
 ▪ The WorldCover dataset’s built-up classification is subject 
to error due to both automated data processing and 
resolution issues.
 ▪ All estimates include unavoidable errors. This indicator is 
calculated from two estimates, and so the potential error is 
greater. When nearly the entire city or district is built up, 
the estimated species count on built-up land will be very 
similar to the citywide estimate, and the indicator value will 
be close to 1. Occasionally, the calculated value is greater 
than 1 because of errors introduced by the methods used to 
produce the numerator, the denominator, or both. In these 
cases, because values greater than 1 are impossible, we report 
the value as 1.

TECHNICAL NOTE  |  November 2025  |  21
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
Figure 3 | An example of a species accumulation curve
Note: In a field species census, as more individuals are caught, the more unique 
species are identified. Because the addition of unique species grows more slowly at 
high capture numbers, it is possible to extrapolate the curve and estimate a saturation 
species number.
Source: Terrestrial Ecosystems n.d.
Because this indicator requires several years of data to calculate, 
and because high-quality iNaturalist data have only recently 
become available, it is not yet possible to provide this indicator 
as a time series. As iNaturalist data continue to be updated, we 
expect to be able to report estimates for more than one time 
point for comparison.
BIO-5–BIO-7: number of vascular plant, bird, and 
arthropod species 
DEFINITION
The estimated number of vascular plant (BIO-5), bird (BIO-6), 
and arthropod (BIO-7) species over a five-year period.
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
throughout the plant. In contrast to nonvascular plants (e.g., 
mosses), vascular plants can grow tall and in locations with 
little moisture on the surface of the soil. Vascular plants 
include more than 90 percent of the Earth’s vegetation.
 ▪ Birds are one of the most visible species groups in urban 
areas, and they are often considered a key indicator of 
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
A local data collection process would typically involve part-
nering with a local research institution to carry out a species 
survey. This survey would be repeated every few years; the 
indicator is the change in time from a baseline level to the 
current year. Here, we provide species counts estimated from 
crowdsourced species-occurrence datasets. Our method cannot 
substitute for on-the-ground species surveys. We intend it to 
provide rough estimates that can be used in the absence of more 
intensive efforts.
These indicators support Singapore Index Indicators 4–6 and 
IUCN Urban Nature Indexes Indicators 4.1 and 4.2.
METHOD FOR ESTIMATING SPECIES NUMBER
Biologists often interpret species survey data by examining the 
number of species found as a function of effort, plotted as a 
species accumulation curve (SAC). The SAC plots the cumula-
tive number of species recorded as a function of sampling effort 
(i.e., number of individuals collected or cumulative number of 
samples). At the start of a species survey, the total number of 
species found typically grows quickly with every unit of effort. 
After some time, however, effort expended yields more and more 
species that were found earlier in the survey—and the total 
number of species grows more slowly per unit of effort. A plot 
of species number versus effort will come to a plateau, and this 
saturation level is a common estimator for the number of species 
in an area, as shown in Figure 3.
50
45
40
35
30
25
20
15
10
5
0
0 100 200 300 400 500 600 700 800 900 1,000
Number of individuals caught

22  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
We estimated species richness by estimating the saturation level 
of SACs using individual crowdsourced observations as our 
effort unit. The estimated counts are the mean saturation levels 
of 100 SACs, each generated by randomizing the order of all 
research-grade iNaturalist observations of the Aves  (birds), Tra -
cheophyta (vascular plants), and Arthropoda (arthropods) taxa 
(GBIF 2025) in 2019–24. Only species observations with 
enough data to generate SACs were considered for estimating 
species richness. Although using just one year of observations 
might have allowed us to associate species count estimates with 
particular years, observation data in most cities were insufficient 
when we limited our method to single-year data. We thus 
combined data over six years to increase the number of cities for 
which we could report estimates.
LIMITATIONS 
We used the SAC curve-fitting approach because it was impos-
sible to conduct an exhaustive survey of all species present even 
in the indicator taxa. However, our reliance on crowdsourced 
species observations introduces serious limitations:
 ▪ Citizen-scientist observations do not benefit from deliberate 
spatial sampling techniques. One consequence is that the 
observations that informed our calculations tended to be 
clustered in heavily populated areas and popular recreational 
sites. We are therefore likely to have missed species that tend 
to avoid human activity. This probably biases our estimates 
toward undercounts. See DiCecco et al. (2021) and Grande 
et al. (2022) for detailed treatments of the issues with 
crowdsourced biodiversity data.
 ▪ Our curve-fitting method included a step that randomized 
the sequence in which observations were incorporated 
into the SAC. Because of the randomization, calculating 
any of these indicators twice with the same data generally 
yields slightly different values. We tried to minimize the 
randomization effects by averaging over 100 instances of 
the curve-fitting step, but we were unable to eliminate the 
effect entirely.
 ▪ In many cities and subcity areas, there were not enough 
citizen-scientist observations to estimate a plausible SAC. 
This can be true for any number of the indicator taxa. When 
there were insufficient data, we were unable to report a 
species count estimate.
 ▪ We were unable to distinguish between native and 
introduced species. Our estimates almost certainly include 
introduced species, and in this way our indicators differ 
from their counterparts in the Singapore Index. Introduced 
species can (but do not always) harm native populations 
and ecosystems, and so a large species count—if it does 
not exclude introduced species—should not be taken as an 
unambiguous signal of good ecological health.
Because these indicators require several years of data to calcu-
late, and because high-quality iNaturalist data have only recently 
become available, it is not yet possible to provide these indica-
tors as a time series. As iNaturalist data continue to be updated, 
we expect to be able to report estimates for more than one time 
point for comparison.
Flooding (FLD)
Most cities are sited based on access to water for use in agri-
culture, power, transportation, or other purposes. But proximity 
to water also exposes cities to the risk of flooding, which is 
expected to increase in most of the world with a changing 
climate. These indicators measure city exposure to a variety of 
flood-related risks. For these indicators, higher values are associ-
ated with greater hazard, exposure, or vulnerability.
FLD-1: exposure to coastal and riverine flooding
DEFINITION
The percentage of built land exposed to coastal or 
riverine flooding.
IMPORTANCE
Most cities are built near coasts or along rivers. These natural 
assets for economic development can also present a hazard 
when they cause flooding in built-up areas. The prevalence of 
these floods is increasing globally due to sea-level rise, extreme 
precipitation, and snowmelt caused by climate change.
METHODS
We used projections from Aqueduct Floods (Ward et al. 
2020), with a resolution of 30 arc seconds (approximately 1 
km), retrieved through Google Earth Engine to characterize 
the coastal and riverine flood hazards for each city in terms of 
meters of expected inundation depth for a given scenario.12 The 
scenario variables we used include a 100-year return period 
(providing the expected depth of inundation from a once-in-
100-years flood event), the business-as-usual (Representative 
Concentration Pathway 8.5) climate scenario, high sea-level rise, 
no subsidence, and the mean inundation depth from the results 
of all five riverine projection models that are available in Aque-
duct Floods. We then compared locations of either projected 
coastal or riverine flooding to built-up areas in the city in 2020 
as defined by the built-up class from ESA WorldCover. For 
each city and city district, we calculated the number of built-up

TECHNICAL NOTE  |  November 2025  |  23
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
pixels and the number of built-up pixels projected to experience 
a flood inundation depth greater than zero under the described 
flooding scenario. Then we calculated the percentage of built-up 
pixels with flood exposure.
Aqueduct Floods projections are available for the years 2010, 
2030, 2050, and 2080. We report this indicator as a time series 
of values for these years.
LIMITATIONS
The Aqueduct Floods dataset with a 1 km resolution may be 
too coarse for some applications, including those related to 
assessing flood risk for individual blocks and buildings. Addi-
tionally, because this indicator considers built-up areas in 2020 
compared with projected 2030, 2050, and 2080 inundation, it 
may underestimate built area exposed to the hazard as a result of 
future land development. Note, however, that this is an indica-
tor of flood hazard, and it does not consider how mitigation 
measures such as flood protection infrastructure (e.g., levees) 
may impact the risk of inundation from flooding under the 
scenario described. This indicator is limited in scope to riverine 
and coastal flooding hazards, which are modeled indepen-
dently—combined effects from riverine and coastal floods are 
not included. It also does not describe hazards from flash pluvial 
flooding resulting from heavy precipitation events. 
FLD-2: expected annual days with extreme 
precipitation
DEFINITION
The expected annual number of days with one-day precipitation 
exceeding the local 90th percentile calculated for three 10-year 
periods: 2020–29, 2040–49, and 2060–69.
IMPORTANCE
Extremely high volumes of one-day precipitation can over-
whelm stormwater management systems, particularly as climate 
change causes some cities to become wetter (Malik and James 
2007; Rosenberg et al. 2010). This indicator supports long-term 
planning for heavy precipitation and can help engineering 
departments design both gray and green stormwater infrastruc-
ture (Bell et al. 2019; van Oorschot et al. 2024).
METHODS
Extreme precipitation for this indicator is defined as the local 
90th percentile of cumulative one-day precipitation, calculated 
for the years 1980–2014 for the pixel that includes the city 
centroid. The historical data are from the ERA daily reanalysis 
dataset (Hersbach et al. 2020).
This indicator is the expected value of the number of days dur-
ing which total precipitation exceeds the 90th percentile. The 
estimate of the expected value is based on a probability model 
parameterized using model outputs from the NEX-GDDP-
CMIP6 ensemble of downscaled global climate simulations 
(NASA 2023). We were able to estimate expected values over 
10-year future periods, for any decade ending in or before 2100, 
with simulations using either the SSP2-4.5 or the SSP5-8.5 
emissions scenarios13 (Riahi et al. 2017). Details on the prob-
ability modeling are in Wong and Switzer (2023).
The spatial resolution of the NEX-GDDP-CMIP6 climate 
simulations is 0.25 degrees, or approximately 25 km. This 
resolution is too coarse to inform most subcity decision-making, 
so we report this indicator as three numbers for the decade of 
interest—the estimates from the three NEX-GDDP-CMIP6 
models whose historical temperature predictions are closest 
to the ERA514 historical data—estimated at the centroid of 
the city or district. We currently report this indicator for three 
decades—2020–29, 2040–49, and 2060–69—using SSP2-4.5.
LIMITATIONS
This indicator is based on estimates of precipitation magnitude 
probabilities as modeled by climate simulations. There are 
unavoidable errors—including climate stochasticity, scientific 
uncertainty regarding Earth system processes, and uncertainty 
in future greenhouse gas emissions trends—from numerous 
sources. Notably, we used the expected value of a random vari-
able to capture information about a probability distribution in a 
single number. It should not be interpreted as a prediction. 
Maximum daily precipitation is also not a direct predictor 
of flooding. It does not account for aggravating or moderat-
ing factors such as antecedent rainfall, the local geography 
of impervious surfaces or stormwater management sys-
tems, or topography.
Our method does not distinguish between rain and fro-
zen precipitation.
FLD-3: land near natural drainage
DEFINITION
The percentage of built land cover within 1 m above the 
nearest drainage.
IMPORTANCE
Land near natural drainage (e.g., streams, rivers) is at risk for 
pluvial or flash flooding hazards. Development closer in eleva-
tion to natural drainage, especially near drainage for large 
land areas, is at greater risk. The risk for these types of floods

24  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
can be difficult to predict, and beyond height above drainage, 
other factors—such as the amount of precipitation, soil type, 
extent of impervious surfaces, distance from natural drainage, 
and presence and efficacy of built drainage systems—are also 
important influences.
METHODS
For this indicator, we used 30 m resolution data on height above 
drainage channels from the Global 30m Height Above the 
Nearest Drainage dataset (Donchyts et al. 2016)15 to estimate 
the land area 1 m or less above the nearest drainage for drains 
with a flow accumulation area of at least 1 square km. We then 
compared these areas to built-up areas in the city as defined 
by the built-up class from the ESA WorldCover for 2020. 16 
For each city and city district, we calculated at a 10 m scale the 
number of built-up pixels and the number of built-up pixels 
within 1 m of the nearest drainage. Then we calculated the 
percentage of built-up pixels that were 1 m or less above the 
nearest drainage.
LIMITATIONS
Although this indicator is an important factor related to flash 
flooding hazards, it does not include other important informa-
tion (e.g., soil type, artificial drainage systems) essential to 
comprehensively assessing them. The resulting spatial analysis 
should not be interpreted as a hazard map. Because it does 
not incorporate data on artificial drainage networks or the 
city’s conveyance and routing of water (e.g., sewers, drains, 
canals), this analysis does not provide a comprehensive pic-
ture of where water is going and where it is likely to stagnate 
during pluvial flooding; rather, it provides only an extremely 
rough approximation.
FLD-4: impervious surface on urbanized land
DEFINITION
The percentage of urbanized land that has impervious surfaces.
IMPORTANCE
Impervious surfaces (in urban areas, these are typically build-
ings and roads and other pavement) prevent water from soaking 
into the ground on-site, contribute to decreased overall water 
infiltration and increased runoff, and can raise the prevalence of 
localized flooding. This type of flooding also lowers the qual-
ity of receiving waters fed by surface water runoff, impacting 
the biodiversity of aquatic and marine systems downstream. 
Building cities in ways that minimize impervious surfaces (with 
alternative construction materials or intentional greening) 
allows for greater natural water infiltration and can enable cities 
to “sponge” up excess water, decrease the risk of flooding, and 
recharge groundwater resources.
METHODS
We obtained the estimated extent of impervious areas from 
Tsinghua University’s annual maps of global artificial impervi-
ous area (Gong et al. 2020).17 This 30 m resolution dataset 
defines a pixel with at least 50 percent estimated impervious 
surface as being impervious. We compared the impervious area 
within the urban extent to the total urban-extent area, using 
the urban extents dataset from Angel et al. (2024). For each 
city and city district, we calculated the urbanized area and the 
area of impervious built-up pixels at a 10 m scale. Then we 
calculated the percentage of urbanized area that is impervious. 
This indicator is similar to LND-1, with two distinctions. This 
indicator considers only urbanized area in the area of interest 
(not all land), and the numerator in the calculation is imperme-
able area. We report this indicator as a time series for the years 
1990, 1995, 2000, 2005, 2010, and 2015. These are the years for 
which we have both the Tsinghua impervious-area data and the 
urban-extent data.
LIMITATIONS
These calculations are based entirely on remotely sensed data, 
which we did not assess against local ground truth data. The two 
datasets compared are in different resolutions and assess differ-
ent years, which presents difficulties for precise comparison.
FLD-5: vegetation cover in built areas
DEFINITION
The percentage of built land cover without vegetation.
IMPORTANCE
Vegetation cover provides many benefits in urban areas. For 
flood mitigation, greater vegetation cover can increase water 
infiltration into the ground, reducing water stagnation and 
runoff on the surface. In turn, an absence of vegetation cover can 
increase the prevalence of localized flooding.
METHODS
As with ACC-7, we identified areas as vegetation covered if 
their fractional vegetation (Fr) was equal to or greater than 
0.6. Zhang et al. (2023) report that urban heat islands are best 
mitigated where fractional vegetation exceeds 0.6. We then 
compared these areas to built-up areas in the city as defined by 
the built-up class from ESA WorldCover for the same year of 
interest. For each city and city district, we calculated at a 10 m

TECHNICAL NOTE  |  November 2025  |  25
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
scale the number of built-up pixels and the number of vegetated 
built-up pixels. Then we calculated the percentage of built-up 
pixels that were vegetated.
We have implemented this indicator for 2020 and 2021. As 
future years of WorldCover data become available, it will be 
practical to report this indicator in the form of a percentage 
change from earlier years. 
LIMITATIONS
These calculations are based fully on remotely sensed data, which 
we did not assess against local ground truth data. We used an 
annual mosaic to assess the greenest point in the year for each 
individual pixel; as a result, this assessment does not measure 
the state of vegetation at any one point in time but rather the 
maximum state of vegetation during the year. This estimates 
for each pixel a combination of the amount of vegetation and 
state of greenness at peak greenness. In most pixels, the amount 
of vegetation does not change (except for leaves), but using 
the peak greenness allows us to estimate how much vegetation 
exists. Temporal and seasonal changes in vegetation (e.g., vegeta-
tion that sheds foliage or goes dormant seasonally) are known to 
affect the ability of green space to deliver expected benefits such 
as stormwater mitigation. The benefits in areas with seasonal 
change will not be as high as those in evergreen ecosystems or 
where there is no seasonal change (Wilson et al. 2022).
FLD-6: vegetation cover in riparian zones
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
For this indicator, we used data on elevation and drainage 
channels from the Global 30m Height Above the Nearest 
Drainage dataset and on the location of water bodies from the 
Joint Research Centre ( JRC) Global Surface Water dataset 
(Pekel et al. 2016)18 to estimate the location of lakes, rivers, and 
streams. To identify riparian zones, we buffered these waterways 
by 144 m—the estimated size of riparian areas often needed 
to preserve significant bird diversity (Lind et al. 2019)—and 
excluded the area of the water channel itself. To assess vegeta-
tion and water cover, we used the NDVI-derived fractional 
vegetation (Fr) as calculated in ACC-7, and the Normalized 
Difference Water Index using the McFeeters (1996) Minimum 
Threshold method as described in LND-4, with minimum 
thresholds of 0.6 and 0.5, respectively (Zhang et al. 2023; 
McFeeters 1996). For the buffered riparian areas in each city 
or subcity unit, we calculated at a 30 m scale the count of all 
riparian-area pixels and the count of riparian-area pixels with 
vegetation or water cover. Then we calculated the percentage of 
riparian-area pixels without vegetation or water cover.
This indicator is reported as a time series of annual values begin-
ning with the year 2017.
LIMITATIONS
These calculations are based entirely on remotely sensed data, 
which we did not assess against local ground truth data. In 
particular, the general definition of riparian zone used may 
not match the situation on the ground as characterized with 
additional local data, such as in the case of extreme topography 
adjacent to drainage channels. 
FLD-7: steep slopes without vegetation
DEFINITION
The percentage of steep hillside slopes without vegetation cover.
IMPORTANCE
Steep slopes are vulnerable to landslides, especially during 
incidents of extreme precipitation or flooding, where soil can 
become saturated with or washed away by water. Vegetation is 
critical for stabilizing slopes; roots hold soil in place, and plants 
absorb water from the soil. Steep slopes without vegetation 
cover are particularly vulnerable to erosion, which can under-
mine the entire slope’s stability and lead to landslides.
METHODS
To estimate slopes on land, we applied the Google Earth Engine 
slope algorithm (GEE 2022) to the global NASA NASADEM 
30 m digital elevation model (NASA JPL 2020). The slope layer 
was then masked to include high slope areas of only 10 degrees 
or greater—the threshold at which landslide susceptibility starts 
to grow quickly (Stanley and Kirschbaum 2017). We estimated 
vegetation cover using fractional vegetation (Fr) as calculated 
for ACC-7. For the high slope areas in each city or subcity unit, 
we calculated at a 30 m scale the count of all high-slope pixels

26  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
and the count of high-slope pixels with any 10 m Sentinel-2 
subpixels not meeting a Fr threshold of 0.6. Then we used these 
values to calculate the percentage of high-slope pixels without 
vegetation cover.
This indicator is reported as a time series of annual values begin-
ning with the year 2017.
LIMITATIONS
These calculations are based entirely on remotely sensed data, 
which we did not assess against local ground truth data. The 
digital elevation model is based on data collected in 2000, which 
may be outdated if significant changes have occurred in local 
slopes. Additionally, its relatively low resolution (30 horizontal 
m) may not capture important smaller-slope details.
This indicator combines data from the NASADEM eleva-
tion dataset and data from the Sentinel-2 satellite mission for 
fractional vegetation. Geometric misalignment among remote-
sensing products can cause small spatial inaccuracies in the 
resulting derived data.
Climate change mitigation (GHG)
Cities are responsible for most human-produced greenhouse 
gas emissions, but cities are also efficient at using resources and 
can reduce emissions through innovations to mitigate climate 
change. These indicators consider how cities contribute to 
climate change, including by measuring the contribution of eco-
nomic sectors, gases, and activities. For these indicators, higher 
values are associated with higher greenhouse gas emissions.
GHG-1: greenhouse gas emissions
DEFINITION
Annual cumulative greenhouse gas emissions (measured in car-
bon dioxide equivalent, or CO2e) from a city area, disaggregated 
by pollutant and sector.
IMPORTANCE
Human activity contributes to air pollution and climate change 
through greenhouse gas emissions from fuel combustion, 
industrial processes, and agriculture. This indicator can help 
decision-makers and stakeholders identify the most important 
pollutants emitted locally, the activities responsible for the emis-
sions, and, with multiple years of data, emissions trends.
METHODS
This indicator is based on the CAMS Global Anthropogenic 
Emissions dataset (Granier et al. 2019). The dataset provides 
estimates of emissions from 12 sectors of human activity, on a 
0.1-degree (approximately 11 km) spatial resolution. The esti-
mates are based on simulations and historical data. The included 
sectors are agriculture (livestock); agriculture (soils); agriculture 
(waste burning); power generation; fugitive emissions; industry; 
Table 3 | Global warming potential of each pollutant species
POLLUTANT SPECIES INCLUDED AS GHG GWP (20-YEAR CO 2  EQUIVALENT) GWP SOURCE
Ammonia (NH3) No N/A N/A
Black carbon (BC) Yes 460 Global values reported in IPCC AR5, Table 8.A.6
Carbon dioxide (CO 2) Yes 1 Definition of GWP
Carbon monoxide (CO) Yes 7.65 Midpoints of global values reported in IPCC AR5, Table 
8.A.4
Methane (CH4) Yes 84 Global values reported in IPCC AR5, Table 8.A.1
Nitrogen oxides (NO x) Yes 19 Global values reported in IPCC AR5, Table 8.A.3
Non-methane volatile organic compounds (NMVOCs) Yes 14 Global values reported in IPCC AR5, Table 8.A.5
Organic carbon (OC) Yes −240 Global values reported in IPCC AR5, Table 8.A.6
Sulfur dioxide (SO 2) No N/A N/A
Note: Abbreviations: GHG = greenhouse gas; GWP = global warming potential; CO 2 = carbon dioxide; IPCC = United Nations Intergovernmental Panel on Climate Change; AR5 = Fifth 
Assessment Report of the IPCC; N/A =not applicable.
Source: Myhre et al. 2013.

TECHNICAL NOTE  |  November 2025  |  27
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
combustion in residential, commercial, and other settings; ships; 
solvents; solid waste and wastewater; off-road transportation; 
and on-road transportation.
We used Google Earth Engine to calculate the emissions from 
within our areas of interest (city administrative boundaries). We 
extracted annual, sector-disaggregated emissions in tonnes/year 
for each year, for each pollutant species. In our implementation, 
we also provide annual summaries of total emissions. Because 
of the coarse resolution of this dataset, we report values for the 
geographic area of only the full city and not for each subcity 
area. To have a shared unit of measurement for all species of 
emissions, we converted tonnes to CO2 e based on the 20-year 
global warming potentials (EPA n.d.) as listed in Table 3. To 
produce a summary number for the final indicator, we shared 
the cumulative CO2 e for each year beginning in 2000 as a 
time series. Future updates will depend on continued updates 
to the CAMS data.
LIMITATIONS
The emissions data used for this indicator account for only 
direct emissions from activities within the boundaries of the city 
(Scope 1 emissions). These data do not account for emissions 
associated with electricity that is used in the city but generated 
elsewhere (Scope 2) or emissions produced elsewhere associ-
ated with products or services consumed in the city (Scope 3). 
The CAMS dataset is modeled data based on an ensemble of 
multiple emissions models and is subject to the limitation of 
those models. The methods used to develop the CAMS emis-
sions dataset are described in Granier et al. (2019).
GHG-2: impact of trees on greenhouse gases
DEFINITION
Annual greenhouse gas net flux from trees per hectare (ha) of 
city area, measured in megagrams (Mg) of CO2e/ha.
IMPORTANCE
Trees are critical contributors to a balanced climate system. 
Whereas healthy, growing trees remove carbon from the 
atmosphere and sequester it, trees that are cut or die emit carbon 
(Gibbs et al. 2022). Cities can work to keep forests and trees 
healthy and invest in expanding tree cover to increase carbon 
removal and reduce trees’ contribution to climate change (Pool 
et al. 2022; Wilson et al. 2022).
METHODS
We calculated this indicator using the Net Carbon Flux 
from Forests dataset (Version 1.2.2) per Harris et al. (2021), 
as accessed on Google Earth Engine. 19 This 30 m resolution 
data layer provides an estimate of net carbon flux from trees 
(gross emissions minus gross removals) from 2001 through 
2021 inclusive in units of Mg CO2e/ha. To calculate the mean 
annual carbon flux for each area of interest, we first unmasked 
the dataset; then pixels where the dataset showed no carbon 
flux were given a value of 0 and were included in subsequent 
calculations. Next, we calculated the mean for the area to 
estimate the average carbon net flux per hectare from the area 
of interest during each year. As we were interested in measur-
ing city and area characteristics based on their full geographies, 
not just forest areas, we normalized net flux using total area as 
the denominator.
We report this indicator as a time series of annual values. 
Negative numbers represent net greenhouse gas removals, and 
positive values indicate net emissions.
LIMITATIONS
The carbon flux model used for the calculations was designed 
for forests and is based on tree cover as detected by Landsat, 
which means it does not pick up or measure carbon flux from 
sparse tree cover. At a 30 m resolution, Landsat and products 
developed from it do not pick up isolated trees. Additionally, the 
model is limited to pixels with tree canopy density greater than 
30 percent and trees of at least 5 m in height, so low-density and 
short-tree cover are not included. Other limitations of the net 
flux data are described in Harris et al. (2021).
This indicator does not measure the impacts of indirect land-use 
change or the greenhouse gas implications of land-use decisions 
outside its borders. For instance, if a city chooses to avoid devel-
oping a green area within its borders, this may lead to exporting 
the development to nearby suburban areas, possibly resulting in 
the loss of a greater number of trees and increased transporta-
tion demand, both of which could increase net carbon emissions. 
When making decisions related to land use, cities should 
consider both the direct and indirect impacts of those decisions.
Heat (HEA)
Due to the urban heat island effect, cities and their residents are 
exposed to greater heat hazard than equivalent rural areas. Cli-
mate change is expected to further exacerbate this risk to cities. 
These indicators measure local heat hazard and the presence of 
heat-mitigating infrastructure. For these indicators, higher val-
ues are associated with greater hazard, exposure, or vulnerability.

28  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
HEA-1: expected annual number of heat waves
DEFINITION
The expected number of heat waves annually over a 
10-year period.
IMPORTANCE
Heat waves, or extended, nonoverlapping periods of abnormally 
high temperatures, are among the deadliest climate phenomena 
(Nunes 2024; Matthews et al. 2025). Beyond direct health 
impacts, they can strain economies and energy infrastructure 
(Burillo et al. 2019; García-León et al. 2021). Understanding the 
future dynamics of heat waves can inform planning for extreme 
heat events and assessment of investment needs and opportuni-
ties for heat mitigation.
There is no globally accepted definition of heat wave. Definitions 
vary in what durations are considered “extended periods,” what 
temperatures are considered “abnormally high,” and even which 
temperature to consider (e.g., daytime high temperature, night-
time low temperature, 24-hour mean temperature). We adopted 
a definition that is meant to be generally useful: three or more 
consecutive days on which the daily maximum temperature 
exceeds the local 97.5th percentile. The 97.5th percentile is 
similar to using the 90th percentile, as recommended by Xu et 
al. (2016), but considers only the warmest one-quarter of the 
days. As our definition is based on locally calculated extremes, 
rather than on a single extreme applied globally, this indicator 
is suited to address changes in cities’ climates and the potential 
for mismatches between future heat hazard and past or existing 
measures for coping with heat.
METHODS
We defined a heat wave as three or more consecutive days on 
which the daily maximum temperature exceeded the local 
90th percentile of daily maximum temperature, calculated for 
summertime months ( June, July, and August in the northern 
hemisphere, and December, January, and February in the 
southern hemisphere) in the years 1980–2014 for the pixel that 
includes the city centroid. The historical data are from the ERA 
daily reanalysis dataset (Hersbach et al. 2020).
Similar to FLD-2, this indicator is the expected value of the 
number of heat waves, based on a probability model parameter-
ized using model outputs from the NEX-GDDP-CMIP6 
ensemble of downscaled global climate simulations (NASA 
2023). We were able to estimate expected values over 10-year 
future periods, for any decade ending in or before 2100, 
with simulations using either the SSP2-4.5 middle-of-the-
road or the SSP5-8.5 high-emissions scenarios (Riahi et al. 
2017). Details on the probability modeling are in Wong and 
Switzer (2023).
The spatial resolution of the NEX-GDDP-CMIP6 climate 
simulations is 0.25 degrees, or approximately 25 km. This 
resolution is too coarse to inform most subcity decision-making, 
so we report this indicator as three numbers for the decade of 
interest—the estimates from the three NEX-GDDP-CMIP6 
models whose historical temperature predictions are closest 
to the ERA5 historical data—estimated at the centroid of the 
city or district. We currently report this indicator for three 
decades—2020–29, 2040–49, and 2060–69—using SSP2-4.5.
LIMITATIONS
The limitations of climate models and our method of estimating 
expected values described for FLD-2 apply here.
Many of the climate models do not consider the presence of 
buildings or pavement, and any such treatment in a global 
climate model is necessarily highly simplified. Our method does 
include a calibration step, whereby the NEX-GDDP-CMIP6 
outputs are corrected using the historical ERA5 reanalysis data, 
but even so they are likely to underestimate temperatures that 
are elevated by the urban heat island effect. The indicator there-
fore probably underestimates heat wave frequencies, especially in 
the most built-up parts of cities.
Our heat wave definition might not be the most relevant for 
some planning applications. For example, heat waves defined 
by nighttime temperature might be more important for under-
standing health impacts for particular age and sex groups 
(Majeed and Floras 2022).
A more detailed discussion of our heat wave indicators is in 
Wong and Mackres (2024).
HEA-2: expected highest annual temperature
DEFINITION
The expected highest temperature in one year over a 
10-year period. 
IMPORTANCE
Whereas the heat wave indicator HEA-1 is intended to address 
threats to public health, this indicator is designed to address 
potential risk to infrastructure. Outdoor infrastructure like 
bridges, rails, and power transformers can all be damaged by 
extreme temperatures (Underwood et al. 2017; Burillo et al. 
2019). Understanding future temperature extremes can help 
infrastructure engineers with long-term capital planning and 
risk management.

TECHNICAL NOTE  |  November 2025  |  29
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
METHODS
As with HEA-1, we calculated this indicator from a probability 
model parameterized with outputs from NEX-GDDP-CMIP6 
climate models (Wong and Switzer 2023).
We currently report this indicator for three decades—2020–29, 
2040–49, and 2060–69—using SSP2-4.5.
LIMITATIONS
This indicator is based on estimates of probabilities as modeled 
by climate simulations. There are unavoidable errors—includ-
ing climate stochasticity, scientific uncertainty regarding Earth 
system processes, and uncertainty in future greenhouse gas 
emissions trends—from numerous sources. Notably, we used 
the expected value of a random variable to capture information 
about a probability distribution in a single number. It should not 
be interpreted as a prediction.
HEA-3: land surface temperature
DEFINITION
The percentage of built land with a high land surface tempera-
ture (LST), defined as greater than or equal to 3 degrees Celsius 
(°C) above the mean for built land, during the hot season.
IMPORTANCE
LST is correlated with near-surface air temperature, which is 
one important dimension of how people experience heat. This 
metric can identify areas of the city exposed to above-average 
heat. Such areas may be good candidates for heat mitigation 
measures such as increased tree or vegetation cover or solar 
reflective surfaces.
METHODS
For this indicator, we used LST for each pixel in the area of 
interest calculated using the methods from Ermida et al. (2020) 
and Landsat imagery, at a 30 m resolution, as retrieved from 
Google Earth Engine. We defined the local hot season as the 
90-day calendar interval centered on the date of the hottest day 
in the years 2013–22 as determined from the ERA5 daily aggre-
gates (Hersbach et al. 2020). We calculated LST from a mosaic 
of cloud-masked Landsat images from this hot season, over the 
same years. This collection of LST images was then masked 
for the built-up class in the ESA WorldCover data. We then 
retrieved the mean LST value for each unmasked pixel. Finally, 
areas that were 3°C or more above the area average were masked 
to calculate the percentage of built area with high LST .
LIMITATIONS
LST is not a direct measure of how people in cities experience 
heat, which is more closely related to near-surface air tempera-
ture and heat indices. Additionally, for this indicator, we used 
measurements from the times of day at which Landsat retrieves 
images, usually within a few hours of midday locally. As a result, 
this indicator does not measure heat in the evening or at night, 
which is important for understanding local heat impacts. Finally, 
because we used an image mosaic to remove cloud cover and 
provide an average for the hot season in the location, the indica-
tor does not reflect any one year, day, or heat event.
HEA-4: surface reflectivity
DEFINITION
The percentage of built land with low surface reflectivity, defined 
as below 0.2 albedo.
IMPORTANCE
This indicator can identify areas of the city with a high share 
of surfaces that retain excess heat. Surfaces with low solar 
reflectivity (albedo) absorb heat and transfer it to the immediate 
surroundings. Areas with a high share of low albedo surfaces 
may be candidates for installing measures—such as trees or 
solar reflective roofs and pavements—that will reduce the heat 
retained on surfaces or otherwise cool the immediate area.
METHODS
For this indicator, we used pixel-wise albedo values derived 
from Sentinel-2, at a 10 m resolution, as retrieved from Google 
Earth Engine using the algorithms defined by Bonafoni and 
Sekertekin (2020). We calculated annual mean albedo from 
cloud-free pixels from 2021. We derived values for built land 
cover areas only using the built-up class from the 10 m resolu-
tion ESA WorldCover dataset as a mask. Finally, pixels with 
albedo values below 0.2—a common threshold used for defin-
ing moderately reflective surfaces (Energy Star n.d.)—were 
masked to calculate the percentage of built area with low 
surface reflectivity.
LIMITATIONS
These calculations are based fully on remotely sensed data, 
which are subject to atmospheric interference and other chal-
lenges in data collection and which we did not assess against 
local ground truth data. For this indicator, we used an image 
mosaic to remove cloud cover and provide an annual aver-
age; thus, the indicator does not reflect the situation at any 
one point in time.

30  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
HEA-5: built land without tree cover
DEFINITION
The percentage of built land without tree cover.
IMPORTANCE
This indicator can identify city areas without significant tree 
cover and therefore those lacking in shade and evapotranspira-
tion that can reduce local heat. Tree cover in built areas varies 
significantly across cities. Tree cover can provide a cooling effect, 
documented to be in the range of 3°C (Wang et al. 2018), in 
urban areas. Areas without tree cover are often exposed to a 
higher extreme heat hazard. Areas with low tree cover may be 
candidates for implementing heat mitigation measures—such as 
trees, other vegetation, or solar reflective roofs and pavements—
that will reduce the heat retained locally or otherwise cool the 
immediate area.
METHODS
As in ACC-2, we used the Meta-WRI Global Canopy Height 
dataset (Tolan et al. 2024) and defined tree cover as locations with 
tree height of at least 3 m. We used the built-up class for 2020 
from ESA WorldCover to mask the tree cover layer. Because the 
canopy-height dataset has a spatial resolution of 1 m, we reduced 
the spatial resolution of the classified dataset to 100 m to match 
WorldCover. Each pixel of the reduced-resolution data represents 
the fraction of its component 1 m pixels that were classified as 
having canopy cover. The percentage of built land with tree cover 
is the average of the unmasked pixel values, times 100. We then 
inverted this value for percent tree cover to derive a value for the 
percentage of built-up land without tree cover.
LIMITATIONS
The limitations associated with the Meta-WRI Global 
Canopy Height dataset as described in ACC-2 also apply to 
this indicator. 
Land protection and restoration (LND)
Cities play an important role in protecting and restoring natural 
lands. These lands provide ecosystem services to cities, habitat 
to wildlife, and other benefits. These indicators classify and 
measure the characteristics of land within the city and changes 
over time. For these indicators, higher values are associated with 
greater protection of natural, nature-like, or otherwise undevel-
oped land uses within city boundaries.
LND-1: permeable areas
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
impacting water quality for the biodiversity of aquatic and 
marine systems downstream.
METHODS
We calculated this indicator by measuring the proportion of all 
permeable areas to the total terrestrial area of the city using the 
following equation:
Permeable areas were taken from the Global Artificial Impervi-
ous Area impervious surface dataset (Gong et al. 2020), which 
classifies land at a 30 m spatial resolution as permeable or 
impermeable to water based on vegetation dynamics, water con-
tent, and reflectance. Water bodies and undeveloped land were 
assumed to be permeable. This indicator is similar to FLD-4, 
with two distinctions: It considers all land in the area of interest 
(not just land within the urban extent), and the numerator in the 
calculation is permeable area (not impermeable area). We report 
these data for years of interest 1985–2018. Values for a series of 
years can be reported as a time series.
LIMITATIONS
These calculations are based entirely on remotely sensed data, 
which we did not assess against local ground truth data. Other 
variables that factor into permeability that are not detectable 
with remote sensing, such as soil type and use of permeable pav-
ing surfaces, are not considered in this analysis. 
This dataset has not been updated since 2018.

TECHNICAL NOTE  |  November 2025  |  31
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
LND-2: tree cover
DEFINITION
The percentage of land area that has tree cover.
IMPORTANCE
Trees provide numerous services to cities. They provide cooling, 
improve air quality, store carbon, reduce noise pollution, and 
regulate the water cycle. Trees also provide habitat for birds, 
insects, and mammals, and generally improve local ecosystem 
health (Wilson et al. 2022).
METHODS
For this indicator, we used the 1 m Meta-WRI Global Canopy 
Height dataset (Tolan et al. 2024). For a land pixel to count 
as being tree-covered, canopy height must have equaled or 
exceeded 3 m. We used the following formula: 
This indicator differs from indicator HEA-5 in two ways: It is 
calculated over the entire area of interest (not just built-up areas 
within it), and it counts the areas with tree cover (rather than 
those without).
LIMITATIONS
The limitations associated with data from the Meta-WRI 
Global Canopy Height dataset, as described in ACC-2, also 
apply to this indicator. 
LND-3: percent of area covered with high 
vegetation cover
DEFINITION
Percentage of area with fractional vegetation exceeding 0.6.
IMPORTANCE
Vegetation provides many ecosystem services to cities, including 
stormwater management, temperature moderation, and habitat 
for urban wildlife. This indicator supports planning and moni-
toring in vegetation management. It also supports the IUCN 
Urban Nature Indexes Indicator 3.4 (IUCN 2023).
METHODS
We calculated fractional vegetation (Fr) for every 10 m pixel 
within the city boundary, following the method described in 
ACC-7. We considered a pixel area to be covered by vegetation 
if its Fr ≥ 0.6. Zhang et al. (2023) report that urban heat islands 
are best mitigated where fractional vegetation exceeds 0.6.
We calculated the percent covered using the following equation:
The indicator is reported as a time series of annual values 
beginning with 2017.
LIMITATIONS
The limitations of fractional vegetation described in ACC-7 
apply to this indicator. Note that this indicator does not address 
vegetation type. Local knowledge is necessary to consider differ-
ences in species, growth habit, and seasonality that are relevant 
to particular vegetation-management applications.
This indicator reports the percentage of pixels whose fractional 
vegetation values exceeded a threshold. Some users might con-
fuse this with the fractional vegetation value of the entire area of 
interest, and in fact might prefer such an indicator. In the future 
we might change this indicator to the fractional vegetation of an 
entire area of interest, or add it as a new indicator, if it is useful 
for our target audience.
LND-4: percentage of area covered by water
DEFINITION
Percentage of area covered by water.
IMPORTANCE
Water cover provides many ecosystem services to cities, includ-
ing groundwater recharge, flood management, temperature 
moderation, and support for wildlife.
METHODS
We used 10 m Sentinel-2 data, as accessed on Google Earth 
Engine, and cloud masked (ESA 2015a) to calculate the 
Normalized Difference Water Index (NDWI) as described by 
McFeeters (1996). We created annual bluest-pixel mosaics for 
each year following the Minimum Threshold method, which 
Sekertekin (2021) found to have the greatest accuracy among 15 
tested thresholding methods. Based on this method, we repeat-
edly smoothed the histogram of the NDWI values to produce a 
histogram with two local maxima, and we took as the threshold

32  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
(NDWIthresh) that separates non-water from water pixels the 
NDWI value between the two maxima with the lowest histo-
gram density. We calculated the percent covered by water using 
the following equation: 
We report this indicator as a time series for the 
years 2017–present.
LIMITATIONS
This indicator is based on interpretation of satellite data, and 
it is likely to be less accurate than methods based on locally 
acquired data from land surveys and water-monitoring pro-
grams. For example, it does not distinguish between water 
bodies of different depth, water quality, or other hydrological 
characteristics.
LND-5: habitat area restored
DEFINITION
The area of habitat land restored between two years of interest as 
a percentage of habitat land in the base year.
IMPORTANCE
Cities can directly improve biodiversity by converting poor 
habitat or nonhabitat land to good habitat. Good habitat 
generally includes multispecies vegetation and enough structural 
complexity to provide shade and cover from predators. The 
IUCN Urban Nature Indexes Indicator 3.2 and Singapore Index 
Indicator 7 call on cities to either estimate the area of land 
restored to “good ecological functioning” or enumerate the types 
of habitat restored. This indicator supports the area-of-land-
restored method.
METHODS
We were unable to discern habitat quality using global data, 
but we could provide data on changes in land classification 
from nonhabitat classes to habitat classes. We used the Landsat 
Analysis Ready Data (Potapov et al. 2022) from the Global 
Land Analysis and Discovery research group at the University 
of Maryland.20 In our implementation, we defined habitat as 
aquatic or noncropland vegetated classes, and we compared clas-
sifications from 2000 as the base year, or year 1, and 2020 as year 
2. We defined new habitat as pixels that were classified as non-
habitat (urban, cropland, or bare) in year 1 but as habitat in year 
2. We calculated this indicator using the following equation:
LIMITATIONS
This method differs somewhat from what is described in the 
Singapore Index Indicator 7. Our denominator is nonhabitat 
rather than degraded habitat. Degraded habitat was habitat in 
the recent past, but nonhabitat includes degraded habitat and 
land that has long been converted to other uses. Our estimate 
therefore probably underestimates restoration as measured by 
this indicator.
The Landsat Analysis Ready Data dataset is currently available 
only for 2000 and 2020. We will add comparisons for additional 
pairs of years if more data become available.
LND-6: habitat types restored
DEFINITION
The number of habitat types restored between two years of 
interest as a percentage of all habitat types in the area.
IMPORTANCE
Cities can directly improve biodiversity by converting poor 
habitat or nonhabitat land to good habitat. Good habitat 
generally includes multispecies vegetation and enough struc-
tural complexity to provide shade and cover. Indicator 7 in the 
Singapore Index calls on cities to either estimate the area of land 
restored to “good ecological functioning” or enumerate the types 
of habitat restored. This indicator supports the habitat-type 
enumeration method.
METHODS
We calculated this indicator using the following formula:
The Landsat Analysis Ready Data discern six land cover classes 
that we included as types of habitat: short vegetation, forest, 
tall forest (taller than 20 m), wetland with short vegetation, 
wetland forest, and open water. (We treated the classes for bare 
ground, snow or ice, cropland, and built-up area as nonhabitat.) 
We calculated our indicator by identifying areas of new habitat, 
where habitat existed in year 2 but not in year 1 or the base year; 
counting the number of habitat types (i.e., aquatic and vegetated 
land cover classes) in these areas of new habitat; and compar-
ing this number to the total number of habitat types in the 
city in year 2. For example, consider a city that had four types

TECHNICAL NOTE  |  November 2025  |  33
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
of habitat in 2020. We took 2020 as year 2 and looked for all 
habitat areas in 2020 that were nonhabitat in the baseline year 
2000 and considered these to be new habitat areas. If there were 
two habitat types in the new habitat areas, we calculated the 
indicator as follows:
LIMITATIONS
This indicator describes restoration as a fraction of the existing 
diversity of habitat types, not as the absolute diversity of restored 
habitat. It does not distinguish between a city that restores many 
types of habitat and a city that simply has few habitat types. For 
example, in a city with six habitat types, restoration of six types 
of habitat will result in an indicator value of 100 percent. The 
indicator is also 100 percent if a city with just one habitat type 
restores just one habitat type. By scaling restored diversity by 
overall diversity, this indicator focuses narrowly on cities’ efforts 
to restore native diversity and not on the diversity itself.
Our method also differs from that of the Singapore Index: We 
used new habitat instead of habitat that had been improved 
from degraded to good ecological function. Cities that have 
access to local data specifically detailing the extent and status of 
habitat restoration projects would probably benefit from calcu-
lating the Singapore Index Indicator 7 using those data.
LND-7: protected areas
DEFINITION
The percentage of land area that is designated as protected area.
IMPORTANCE
Protected or secured natural areas indicate a government’s 
legally formalized commitment to conserve biodiversity. 
Protected areas are lands (or waters) with legal restrictions on 
development or use and sometimes physical barriers to entry. 
Protected areas inside and near cities, including outside their 
jurisdictional boundaries, can provide multiple benefits to people 
living in cities in the form of human health and well-being 
and water security (Wilson et al. 2022). Importantly, they serve 
as havens for biodiversity and can be used to create ecologi-
cal connectivity and restore previously lost biodiversity in the 
cityscape. This indicator supports the IUCN Urban Nature 
Indexes Indicator 3.1.
METHODS
We calculated this indicator using the following formula:
Our data on protected areas come from the World Database 
on Protected Areas (WDPA), which is a collection of data on 
protected areas contributed by national governments (UNEP-
WCMC and IUCN n.d.).
LIMITATIONS
 ▪ This indicator measures only protected areas within city 
boundaries, excluding nearby protected areas. 
 ▪ The WDPA is based on information contributed by national 
governments. It might exclude areas whose protections do 
not fit criteria set by these governments.
 ▪ Intensive, biodiversity-harming activities can occur within 
formally protected areas. We did not assess specific legal 
protections; nor did we assess enforcement of protections.
 ▪ Because of the nature of the source WDPA data, we 
were unable to report this indicator as a time series 
of annual values.
LND-8: protection of Key Biodiversity Areas
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

34  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
METHODS
KBAs can often benefit from formal protection (KBA Partner-
ship 2017). In this indicator, we provide information on how 
much of a city’s KBA is currently under formal protection. This 
is the formula:
KBA data are provided by BirdLife International (2022) for the 
KBA Partnership, and data on protected areas come from the 
WDPA (UNEP-WCMC and IUCN n.d.). 
LIMITATIONS
This indicator shares the limitations of LND-7 arising from 
limitations in the WDPA. Both the WDPA and the KBA data 
are periodically updated. Those who use values of this indicator 
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
LND-9: undeveloped Key Biodiversity Areas
DEFINITION
The percentage of KBA land that is not built up. 
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
The KBA data are periodically updated. Those who use values of 
this indicator calculated by WRI or others should note whether 
they were based on the most recent versions of the input data.
The terms of use provided by the KBA Partnership do not allow 
us to share the source data, but all data can be requested on its 
website (https://www.keybiodiversityareas.org).
General limitations
The indicators developed through these methods can provide 
numerous insights on variations within and between cities and 
changes over time. However, there are limitations to the value 
provided by these indicators, uncertainty regarding the result-
ing indicator values, and caveats to their meaning and potential 
applications that should be understood. In addition to the 
limitations specific to each indicator mentioned, there are also 
a few general methodological constraints. We have addressed 
these concerns to the extent practical in how specific indicators 
are defined and presented, but these issues remain important for 
users of the indicators.
 ▪ Boundaries and aggregations. These methods primarily 
focus on providing a summary value of each area of 
interest for each indicator. Doing so helps simplify a 
large number of data, but it can also obscure nuance and 
important information. First, the areas of interest need to 
be meaningful. We used administrative areas because they 
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
profoundly affect the results of data aggregations for the 
area of interest. As an example, if a park is equally split 
between two city wards that have similar vegetation coverage, 
the boundaries could obscure the significant vegetation 
differences within their respective residential areas due 
to averaging. If the park is classified as a separate area of 
interest, a vegetation cover indicator would more accurately

TECHNICAL NOTE  |  November 2025  |  35
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
characterize the differences between the two remaining 
residential areas. Third, the size of the areas of interest in 
comparison to the scale of the datasets used to calculate 
indicators can produce results that range from insightful 
to nearly meaningless. For example, assume a city has 
equally sized square districts of 1 km in each direction. A 
raster dataset that is at a smaller scale would give useful 
information about the area within the district (but if it is 
much smaller in scale, such as 10 m, it may give too much 
information for an aggregate indicator to fully summarize, 
as we discuss further below). However, if the dataset is of a 
larger scale, say 10 km, aggregations at the smaller district 
scale result in the same value for many districts, which 
likely does not reflect the reality on the ground and does 
not give any meaningful information for comparison among 
the districts. 
 ▪ Data uncertainty and incompleteness. The data sources 
used to calculate the indicators themselves have significant 
limitations. The global-scale datasets from remote sensing 
or crowdsourcing used for our indicators are limited by 
what sensors can detect, their minimum mapping unit, 
and user contributions. They can give the impression of 
completeness while not being relevant at the scale of the 
desired analysis or can be missing important contextual 
details. We document limitations of specific datasets within 
the methods’ description for each indicator. In contrast, local 
data pose their own problems, including being limited in 
scope, using local definitions that are often incompatible 
with data used elsewhere, introducing bias to an analysis, and 
often being difficult to access. The time required to collect 
and process local data makes it impossible to use local data 
for this project, which aims to calculate shared indicators for 
eventually hundreds of cities around the world. Ultimately, 
decisions about the most appropriate data for a local 
challenge need to be made by or with local stakeholders. 
For this reason, methods with flexible data input sources are 
critical. Our indicator methods can be adapted by our team 
or other researchers for use with similar alternative datasets, 
including from local sources, if a more appropriate one is 
developed or identified. 
 ▪ Comparability between indicators and datasets. The 
differences between datasets—such as their scale or date of 
acquisition—can make it complex to use multiple datasets 
together. We intend for multiple indicators to be shared 
with stakeholders; however, indicators within the same 
thematic areas, and even indicators themselves, may draw 
on information from various datasets. Within individual 
indicators, we often use multiple datasets together (e.g., a 
primary dataset and another dataset to mask the data to 
focus on land cover types of interest) to develop an indicator 
statistic. The best datasets for required variables may be 
available for different years, meaning some changes during 
that time period are ignored or misrepresented. Or they may 
be of different scales, meaning that issues of aggregation 
(as discussed previously) or precision (e.g., more trees being 
detectable at a 10 m scale than a 30 m scale) can mean that 
the datasets show different information in the same place. 
 ▪ Spatial observational data are not enough. Our indicators 
almost exclusively identify the current physical states or 
changes to them in cities. This information can establish 
trends; benchmark areas against each other; and help 
identify opportunities, diagnose problems, and spatially 
target interventions. However, the indicators alone are 
likely not sufficient to identify actions and set targets. 
Domain expertise and local knowledge to identify options 
and planning processes to determine objectives are 
required. Importantly, these indicators do not measure or 
attribute influences on physical changes, such as policies 
or infrastructure investment, or their effectiveness. To 
track progress toward physical goals, observational data are 
essential. To understand which actions are working well and 
which are falling short, other data and methods are required.
 ▪ Indicators address single dimensions, while urban 
sustainability is multidimensional. Most of our indicators 
were chosen to address issues in a single theme, but cities 
must contend with many themes at once. Consider an 
extended example: Some cities might seek to reduce flood 
risk, improve support for biodiversity, reduce greenhouse gas 
emissions, and improve residents’ access to urban amenities. 
Indicator FLD-5 addresses flood risk, and preservation 
of green space in a matrix of built-up land would be one 
(but not the only!) strategy to improve flood mitigation 
as reflected in FLD-5. Green space preservation would 
probably also preserve or promote habitat for some types 
of wildlife. However, such a strategy might also work 
against efforts to increase the density of developed land, 
complicating land-use strategies to improve accessibility of 
urban amenities and reduce vehicle use. Our indicators are 
intended to inform city decision-making, but in themselves 
they do not provide guidance on the difficult, city-specific 
work of choosing which themes to prioritize and crafting 
solutions that are best suited to the local environmental, 
social, and political context.

36  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
Further work
These indicator methods and their uses can be further refined 
and enhanced. Options identified so far include the following:
 ▪ Offer guidance on developing new or revised indicators 
emphasizing designs that are fit for purpose for dataset 
comparison and selection. 
 ▪ Develop additional indicators or adapt existing indicator 
methods into our calculation framework to allow for similar 
standard measurements on other urban themes relevant to 
city decision-makers or stakeholders. 
 ▪ Calculate indicators for additional cities and for other 
initiatives supporting cities on sustainable development.  
 ▪ Compare our indicator findings with socioeconomic data to 
explore relationships among indicators of urban equity and 
the presence of urban amenities and risk in multiple cities.
 ▪ Create a process for vetting and validating new global or 
local data layers as they become available to potentially 
integrate with and improve existing indicator methods.
 ▪ Compare computed indicators using global data with 
computations from available local data for validation 
and provide support to stakeholders for collecting local 
data as needed. 
 ▪ Improve integration of user feedback and needs into 
indicator prioritization, design, and development.
 ▪ Connect more with potential users and stakeholders and 
define their profiles, statuses, data capacities, and needs. 
 ▪ Conduct user needs assessments to better understand 
how the proposed indicators may help our stakeholders 
in their decision-making processes and what additional 
indicators—or modifications to existing indicators—may 
be useful for users. 
 ▪ Map our indicators with potential city-level actions and 
how the proposed metrics may drive them. 
 ▪ Create focus groups or case studies of cities sharing 
feedback on the value and uses of the data and indicators.

TECHNICAL NOTE  |  November 2025  |  37
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
Appendix A. OpenStreetMap key-value pairs
Table A-1 | Search parameters used in OpenStreetMap queries
  COMMERCE EDUCATION HEALTH CARE 
AND SOCIAL 
SERVICES
AGRICULTURE GOVERNMENT INDUSTRY TRANSPORTATION 
AND LOGISTICS
aeroway: terminal X
amenity: animal_boarding X
amenity: animal_breeding X
amenity: animal_shelter X
amenity: bank X
amenity: biergarten X
amenity: bus_station X
amenity: cafe X
amenity: casino X
amenity: childcare X
amenity: college X
amenity: courthouse X
amenity: dentist X
amenity: doctors X
amenity: fast_food X
amenity: ferry_terminal X
amenity: fire_station X
amenity: food_court X
amenity: hospital X
amenity: kindergarten X
amenity: library X
amenity: mortuary X
amenity: music_school X
amenity: nightclub X
amenity: nursing_home X
amenity: pharmacy X
amenity: police X
amenity: post_office X
amenity: prep_school X
amenity: research_institute X
amenity: restaurant X

38  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
  COMMERCE EDUCATION HEALTH CARE 
AND SOCIAL 
SERVICES
AGRICULTURE GOVERNMENT INDUSTRY TRANSPORTATION 
AND LOGISTICS
amenity: school X
amenity: social_facility X
amenity: studio X
amenity: theatre X
amenity: townhall X
amenity: university X
amenity: veterinary X
building: bank X
building: clinic X
building: college X
building: commercial X
building: factory X
building: government X
building: government_office X
building: hospital X
building: industrial X
building: manufacture X
building: office
building: poultry_house X
building: pub X
building: restaurant X
building: retail X
building: school X
building: shop X
building: store X
building: supermarket X
building: university X
building: warehouse X
cargo: * X
industrial: * X
landuse: animal_keeping X
landuse: aquaculture X
landuse: commercial X

TECHNICAL NOTE  |  November 2025  |  39
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
  COMMERCE EDUCATION HEALTH CARE 
AND SOCIAL 
SERVICES
AGRICULTURE GOVERNMENT INDUSTRY TRANSPORTATION 
AND LOGISTICS
landuse: education X
landuse: farm X
landuse: farmyard X
landuse: greenhouse_horticulture X
landuse: harbour X
landuse: industrial X
landuse: orchard X
landuse: paddy X
landuse: plant_nursery X
landuse: quarry X
landuse: retail X
landuse: vinyard X
railway: station X
school: * X
Note: Key-value pairs relate information (values) to category labels (keys). This table lists the key-value pairs we used to extract data on the locations of urban amenities from 
OpenStreetMap for indicators ACC-4 through ACC-13. An X indicates that a key-value pair (row) was included in the OpenStreetMap query for a particular amenity class (column). Key-
value pairs were combined into a query by OR-relations: We searched for all amenity locations tagged with at least one of the listed key-value pairs. An asterisk (*) indicates that all data 
tagged with a key, regardless of the associated value, were part of the query.
Source: WRI authors.

40  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
Endnotes
1. To learn about the Cities4Forests initiative, visit https://cities4for -
ests.com/. 
2. For information about the UrbanShift initiative, see https://www.
shiftcities.org/.
3. For more information about the OSM database, see https://www.
openstreetmap.org/.
4. NEX-GDDP refers to the National Aeronautics and Space Admin -
istration Earth Exchange Global Daily Downscaled Projections. 
CMIP6 refers to the sixth phase of the Coupled Model Intercom -
parison Project.
5. The Cities Indicators Framework is an open-source Python pack -
age available at https://github.com/wri/cities-cif .
6. To access the WRI Cities Indicators API, visit https://cities-data-
api.wri.org/.
7. To access the CityMetrics data dashboard, visit https://www.
citymetrics.wri.org/.
8. Key-value pairs describe how data are structured, often in sys -
tems that store large volumes of varied data. The key is an identi -
fier, and the value is the information associated with that identifier.
9. To learn more about the Global Anthropogenic Emissions dataset, 
see https://eccad3.sedoo.fr/metadata/479 ; for CAMS, see https://
atmosphere.copernicus.eu/; and for ECCAD, see https://eccad.
aeris-data.fr/. 
10. For more information about the CAMS Global Reanalysis EAC4 
dataset, visit https://www.ecmwf.int/en/forecasts/dataset/cams-
global-reanalysis.
11. To learn more about the V5.GL.02 dataset, see https://sites.wustl.
edu/acag/datasets/surface-pm2-5/#V5.GL.02 , and for the Atmo -
spheric Composition Analysis Group, see https://sites.w ustl.edu/
acag/.
12. For more information about the Aqueduct Floods database, visit 
https://www.wri.org/applications/aqueduct/floods .
13. SSP stands for shared socioeconomic pathway. SSP2-4.5 refers to 
a middle-of-the-road emissions scenario and SSP5-8.5 to a high-
emissions scenario.
14. ERA5 refers to the fifth-generation atmospheric reanalysis dataset 
produced by the Copernicus Climate Change Service at the Euro -
pean Centre for Medium-Range Weather Forecasts. 
15. For additional information about the Global 30m Height Above the 
Nearest Drainage dataset, see https://gee-community-catalog.
org/projects/hand/.
16. For more information about the 2020 ESA WorldCover, visit 
https://developers.google.com/earth-engine/datasets/catalog/
ESA_WorldCover_v100.
17. For more information about the Tsinghua annual maps, see 
https://developers.google.com/earth-engine/datasets/catalog/
Tsinghua_FROM-GLC_GAIA_v10.
18. More information about the JRC Global Surface Water dataset is 
available at https://developers.google.com/earth-engine/datasets/
catalog/JRC_GSW1_3_GlobalSurfaceWater .
19. To access the Net Carbon Flux from Forests dataset, visit https://
code.earthengine.google.com/?asset=projects/wri-datalab/gfw-
data-lake/net-flux-forest-extent-per-ha-v1-2-2-2001-2021/net-flux-
global-forest-extent-per -ha-2001-2021. 
20. To learn more about the Global Land Analysis and Discovery 
research group, visit https://glad.umd.edu/.

TECHNICAL NOTE  |  November 2025  |  41
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
References
Alegana, V.A., P.M. Atkinson, C. Pezzulo, A. Sorichetta, D. Weiss, T. 
Bird, E. Erbach-Schoenberg, et al. 2015. “Fine Resolution Mapping of 
Population Age-Structures for Health and Development Applications.” 
Journal of the Royal Society Interface 12 (105): 20150073.
Amiri, R., Q. Weng, A. Alimohammadi, and S.K. Alavipanah. 2009. 
“Spatial-Temporal Dynamics of Land Surface Temperature in Relation 
to Fractional Vegetation Cover and Land Use/Cover in the Tabriz 
Urban Area, Iran.” Remote Sensing of Environment  113 (12): 2606–17.
Angel, S., E. Mackres, and B. Guzder-Williams. 2024. “Measur -
ing Change in Urban Land Consumption: A Global Analysis.” 
Land 13 (9): 1491. 
Avtar, R., R. Aggarwal, A. Kharrazi, P. Kumar, and T.A. Kurniawan. 2019. 
“Utilizing Geospatial Information to Implement SDGs and Monitor 
Their Progress.” Environmental Monitoring and Assessment  192 (De-
cember): 35. https://doi.org/10.1007/s10661-019-7996-9 .
Bell, C.D., K. Spahr, E. Grubert, J. Stokes-Draut, E. Gallo, J.E. McCray, 
and T.S. Hogue. 2019. “Decision Making on the Gray-Green Stormwa -
ter Infrastructure Continuum.” Journal of Sustainable Water in the Built 
Environment 5 (1): 04018016.
BirdLife International. 2022. (Database.) World Database of Key 
Biodiversity Areas . Key Biodiversity Areas Partnership. https://www.
keybiodiversityareas.org/.
Bocher, E., G. Petit, J. Bernard, and S. Palominos. 2018. “A Geoprocess -
ing Framework to Compute Urban Indicators: The MApUCE Tools 
Chain.” Urban Climate 24 (June): 153–74. https://doi.org/10.1016/j.
uclim.2018.01.008.
Boeing, G., C. Higgs, S. Liu, B. Giles-Corti, J.F. Sallis, E. Cerin, M. Lowe, 
et al. 2022. “Using Open Data and Open-Source Software to De -
velop Spatial Indicators of Urban Design and Transport Features for 
Achieving Healthy and Sustainable Cities.” Lancet Global Health  10 (6): 
e907–18. https://doi.org/10.1016/S2214-1 09X(22)00072-9.
Boeing, G. 2024. “Modeling and Analyzing Urban Networks and Ame -
nities with OSMnx.” Working Paper. Geographical Analysis . https://
geoffboeing.com/publication s/osmnx-paper/.
Bonafoni, S., and A. Sekertekin. 2020. “Albedo Retrieval from Senti -
nel-2 by New Narrow-to-Broadband Conversion Coefficients.” IEEE 
Geoscience and Remote Sensing Letters  17 (9): 1618–22. https://doi.
org/10.1109/LGRS.2020.2967085.
Brown, C.F., S.P. Brumby, B. Guzder-Williams, T. Birch, S.B. Hyde, 
J. Mazzariello, W. Czerwinski, et al. 2022. “Dynamic World, Near 
Real-Time Global 10 M Land Use Land Cover Mapping.” Scientific 
Data 9 (1): 251.
Buchmueller, T.C., M. Jacobson, and C. Wold. 2006. “How Far to the 
Hospital? The Effect of Hospital Closures on Access to Care.” Journal 
of Health Economics 25 (4): 740–61.
Burillo, D., M.V. Chester, S. Pincetl, and E. Fournier. 2019. “Electric -
ity Infrastructure Vulnerabilities Due to Long-Term Growth and 
Extreme Heat from Climate Change in Los Angeles County.” Energy 
Policy 128: 943–53.
Carlson, T.N., and D.A. Ripley. 1997. “On the Relation between NDVI, 
Fractional Vegetation Cover, and Leaf Area Index.” Remote Sens -
ing of Environment 62 (3): 241–52. https://doi.org/10.1016/S0034-
4257(97)00104-1.
Chan, L., O. Hillel, P. Werner, N. Holman, I. Coetzee, R. Galt, and T. 
Elmqvist. 2021. Handbook on the Singapore Index on Cities’ Biodiversity 
(also Known as the City Biodiversity Index). CBD Technical Series 98. 
Montreal: Secretariat of the Convention on Biological Diversity; Sin -
gapore: National Parks Board. https://www.cbd.int/doc/publications/
cbd-ts-98-en.pdf.
Cochran, F., J. Daniel, L. Jackson, and A. Neale. 2020. “Earth Observa -
tion-Based Ecosystem Services Indicators for National and Sub -
national Reporting of the Sustainable Development Goals.” Remote 
Sensing of Environment 244 (July): 111796. https://doi.org/10.1016/j.
rse.2020.111796 .
Croke, J., C. Thompson, and K. Fryirs. 2017. “Prioritising the Placement 
of Riparian Vegetation to Reduce Flood Risk and End-of-Catchment 
Sediment Yields: Important Considerations in Hydrologically-Variable 
Regions.” Journal of Environmental Management  190 (April): 9–19. 
https://doi.org/10.1016/j.jenvman.2016.12.046 .
Dai, D. 2010. “Black Residential Segregation, Disparities in Spatial 
Access to Health Care Facilities, and Late-Stage Breast Cancer Diag -
nosis in Metropolitan Detroit.” Health & Place 16 (5): 1038–52.
Deslauriers, M.R., A. Asgary, N. Nazarnia, and J.A.G. Jaeger. 2018. 
“Implementing the Connectivity of Natural Areas in Cities as an Indi -
cator in the City Biodiversity Index (CBI).” In Landscape Indicators—
Monitoring of Biodiversity and Ecosystem Services at Landscape Level , 
edited by U. Walz and R.-U. Syrbe, Special Issue, Ecological Indicators  
94 (November): 99–113. https://doi.org/10.1016/j.ecolind.2017.02.028.
DiCecco, G.J., V. Barve, M.W. Belitz, B.J. Stucky, R.P Guralnick, and A.H. 
Hurlburt. 2021. “Observing the Observers: How Participants Con -
tribute Data to iNaturalist and Implications for Biodiversity Science.” 
BioScience 71 (11): 1179–88.
Donchyts, G., H. Winsemius, J. Schellekens, T. Erickson, H. Gao, H. 
Savenije, and N. van de Giesen. 2016. “Global 30m Height above 
the Nearest Drainage (HAND).” Geophysical Research Abstracts  18: 
EGU2016-17445-3. https://gee-community-catalog.org/projects/
hand/.
Energy Star. n.d. “ENERGY STAR Program Requirements for Roof 
Products: Partner Commitments.” Energy Star. https://www.energy -
star.gov/sites/default/files/specs//Roof%20Products%20V3%20Pro -
gram%20Requirements_0.pdf. Accessed March 7, 2023.
Engel-Cox, J.A., R.M. Hoff, and A.D.J. Haymet. 2004. “Recommenda -
tions on the Use of Satellite Remote-Sensing Data for Urban Air 
Quality.” Journal of the Air & Waste Management Association 54 (11): 
1360–71. https://doi.org/10.1080/10473289 .2004.10471005 .
EPA (US Environmental Protection Agency). n.d. “Understanding 
Global Warming Potentials.” https://www.epa.gov/ghgemissions/
understanding-global-warming-potentials . Accessed January 12, 2016.

42  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
Ermida, S.L., P. Soares, V. Mantas, F.-M. Göttsche, and I.F. Trigo. 2020. 
“Google Earth Engine Open-Source Code for Land Surface Tempera -
ture Estimation from the Landsat Series.” Remote Sensing  12 (9): 1471. 
https://doi.org/10.3 390/rs12091471 .
ESA (European Space Agency). 2015a. “Sentinel-2: Cloud Probability.” 
Earth Engine Data Catalog. https://developers.google.com/earth-
engine/datasets/catalog/COPERNICUS_S2_CLO UD_PROBABILITY.
ESA. 2015b. “Sentinel-2 MSI: MultiSpectral Instrument, Level-1C.” 
Earth Engine Data Catalog. https://developers.google.com/earth-
engine/datasets/catalog/COPERNICUS_S2 .
ESA. 2020a. “ESA WorldCover 10m V100.” Earth Engine Data Cata -
log. https://developers.google.com/earth-engine/datasets/catalog/
ESA_WorldCover_v100.
ESA. 2020b. WorldCover Product User Manual, Version 1.0 . Paris: ESA. 
https://worldcover2020.esa.int/data/docs/WorldCover_PUM_V1.1.pdf .
Fahrig, L. 2003. “Effects of Habitat Fragmentation on Biodiversity.” 
Annual Review of Ecology, Evolution, and Systematics 34: 487–515. 
https://doi.org/10.1146/annurev.ecolsys.34.011802.132419 .
Feng, S., D. Gao, F. Liao, F. Zhou, and X. Wang. 2016. “The Health 
Effects of Ambient PM 2.5 and Potential Mechanisms.” Ecotoxicology 
and Environmental Safety  128 (June): 67–74. https://doi.org/10.1016/j.
ecoenv.2016.01.030.
Fink, C., W. Klumpenhouwer, M. Saraiva, R. Pereira, and H. Tenkanen. 
2022. “R5py: Rapid Realistic Routing with R5 in Python.” Zenodo . 
doi:10.5281/ZENODO.7060437. 
Forman, R.T.T., and M. Godron. 1991. Landscape Ecology . Hoboken, 
NJ: Wiley. https://www.wiley.com/en-us/Landscape+Ecology-
p-9780471870371 .
Fritz, S., L. See, T. Carlson, M. Haklay, J.L. Oliver, D. Fraisl, R. Mond -
ardini, et al. 2019. “Citizen Science and the United Nations Sustain -
able Development Goals.” Nature Sustainability  2 (October): 922–30. 
https://doi.org/10.1038/s41893-019-0390-3.
García-León, D., A. Casanueva, G. Standardi, A. Burgstall, A.D. Flouris, 
and L. Nybo. 2021. “Current and Projected Regional Economic Im -
pacts of Heatwaves in Europe.” Nature Communications  12 (1): 5807.
GBIF (Global Biodiversity Information Facility). 2025. “GBIF Occur -
rence Download.”  https://doi.org/10.15468/dl.ef5u6r.
GEE. 2022. “Ee.Terrain.slope.” August 1. https://developers.google.
com/earth-engine/apidocs/ee -terrain-slope.
Gibbs, D., N. Harris, and J.-R. Pool. 2022. Global Protocol for Commu -
nity-Scale Greenhouse Gas Inventories: Supplemental Guidance for 
Forests and Trees. Washington, DC: Greenhouse Gas Protocol, World 
Resources Institute. https://ghgprotocol.org/gpc-supplemental-guid-
ance-forests-and-trees.
Giuliani, G., E. Petri, E. Interwies, V. Vysna, Y. Guigoz, N. Ray, and I. 
Dickie. 2021. “Modelling Accessibility to Urban Green Areas Using 
Open Earth Observations Data: A Novel Approach to Support the 
Urban SDG in Four European Cities.” Remote Sensing  13 (3): 422. 
https://doi.org/10.3 390/rs13030422 .
Gong, P., X. Li, J. Wang, Y. Bai, B. Chen, T. Hu, X. Liu, et al. 2020. “Annual 
Maps of Global Artificial Impervious Area (GAIA) between 1985 and 
2018.” Remote Sensing of Environment  236 (January): 111510. https://
doi.org/10.1016/j.rse.2019.111510.
Gorelick, N., M. Hancher, M. Dixon, S. Ilyushchenko, D. Thau, and R. 
Moore. 2017. “Google Earth Engine: Planetary-Scale Geospatial Analy -
sis for Everyone.” Remote Sensing of Environment  202: 18–27.
Grande, A.M., N.W. Chan, P. Gajbhiye, D.J. Perkins, and P.S. Warren. 
2022. “Evaluating the Use of Semi-structured Crowdsourced Data to 
Quantify Inequitable Access to Urban Biodiversity: A Case Study with 
eBird.” PLOS One 17 (11): e0277223.
Granier, C., S. Darras, H. Denier van der Gon, J. Doubalova, N. Elguindi, 
B. Galle, M. Gauss, et al. 2019. “The Copernicus Atmosphere Moni -
toring Service Global and Regional Emissions (April 2019 Version).” 
Copernicus Atmosphere Monitoring Service. https://doi.org/10.2 4380/
D0BN-KX16.
Guzder-Williams, B., E. Mackres, S. Angel, A.M. Blei, and P. Lamson-
Hall. 2023. “Intra-urban Land Use Maps for a Global Sample of Cities 
from Sentinel-2 Satellite Imagery and Computer Vision.” Computers, 
Environment and Urban Systems  100: 101917.
Harris, N.L., D.A. Gibbs, A. Baccini, R.A. Birdsey, S. de Bruin, M. Farina, 
L. Fatoyinbo, et al. 2021. “Global Maps of Twenty-First Century Forest 
Carbon Fluxes.” Nature Climate Change 11 (3): 234–40. https://doi.
org/10.1038/s41558-020-00976-6.
Helmrich, A.M., B.L. Ruddell, K. Bessem, M.V. Chester, N. Chohan, E. 
Doerry, J. Eppinger, et al. 2021. “Opportunities for Crowdsourcing in 
Urban Flood Monitoring.” Environmental Modelling & Software  143 
(September): 105124. https://doi.org/10.1016/j.envso ft.2021.105124.
Hersbach, H., B. Bell, P. Berrisford, S. Hirahara, A. Horányi, J. Muñoz‐
Sabater, J. Nicolas, et al. 2020. “The ERA5 Global Reanalysis.” Quar -
terly Journal of the Royal Meteorological Society 146 (730): 1999–2049. 
https://doi.org/10.1002/qj.3803.
Inness, A., M. Ades, A. Agustí-Panaredaz, J. Barré, A. Benedictow, A. 
Blechschmidt, J. Dominguez, et al. 2019. “CAMS Global Reanalysis 
(EAC4).” Copernicus Atmosphere Monitoring Service. https://ads.
atmosphere.copernicus.eu/cdsapp#!/dataset/cams-global-reanalysis-
eac4?tab=overview.
IUCN (International Union for the Conservation of Nature). 2023. The 
IUCN Urban Nature Indexes . Gland, Switzerland: IUCN. https://doi.
org/10.2305/RWDY8899 .
Jing, C., M. Du, S. Li, and S. Liu. 2019. “Geospatial Dashboards for 
Monitoring Smart City Performance.” Sustainability  11 (20): 5648. 
https://doi.org/10.3 390/su11205648.
Joshi, P. 2017. “A Perspective on Education’s Importance for Urban 
Development.” European Journal of Education  52 (4): 421–26.
Kalluri, S., P. Gilruth, and R. Bergman. 2003. “The Potential of Remote 
Sensing Data for Decision Makers at the State, Local and Tribal Level: 
Experiences from NASA’s Synergy Program.” Environmental Science & 
Policy 6 (6): 487–500. https://doi.org/10.1016/j.envs ci.2003.08.002 .
Kampa, M., and E. Castanas. 2008. “Human Health Effects of Air Pollu -
tion.” Environmental Pollution 151 (2): 362–67. https://doi.org/10.1016/j.
envpol.2007.06.012.

TECHNICAL NOTE  |  November 2025  |  43
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
Kavvada, A., G. Metternicht, F. Kerblat, N. Mudau, M. Haldorson, S. 
Laldaparsad, L. Friedl, et al. 2020. “Towards Delivering on the Sustain -
able Development Goals Using Earth Observations.” Remote Sens -
ing of Environment 247 (September): 111930. https://doi.org/10.1016/j.
rse.2020.111930.
KBA Partnership (Key Biodiversity Areas Partnership). 2017. The Rela -
tionship between Key Biodiversity Areas (KBAs) and Protected Areas . 
Cambridge, UK: KBA Secretariat, Birdlife International. https://www.
keybiodiversityareas.org/assets/8f1535aed3316ae2b7 20364019f8cb1c.
Kondo, M.C., S. Han, G.H. Donovan, and J.M. MacDonald. 2017. “The 
Association between Urban Trees and Crime: Evidence from the 
Spread of the Emerald Ash Borer in Cincinnati.” Landscape and Urban 
Planning 157 (January): 193–99. https://doi.org/10.1016/j.landurb -
plan.2016.07.003.
Konijnendijk, C. 2021. “The 3-30-300 Rule for Urban Forestry and 
Greener Cities.” Biophilic Cities Journal 4 (2): 2.
Kuffer, M., J. Wang, M. Nagenborg, K. Pfeffer, D. Kohli, R. Sliuzas, and 
C. Persello. 2018. “The Scope of Earth-Observation to Improve the 
Consistency of the SDG Slum Indicator.” ISPRS International Journal of 
Geo-Information  7 (11): 428. https://doi.org/10.3390/ijgi7110428.
Kuffer, M., D.R. Thomson, G. Boo, R. Mahabir, T. Grippa, S. Vanhuysse, 
R. Engstrom, et al. 2020. “The Role of Earth Observation in an Inte -
grated Deprived Area Mapping ‘System’ for Low-to-Middle Income 
Countries.” Remote Sensing 12 (6): 982. https://doi.org/10.3 390/
rs12060982.
Lee, K.K., M.R. Miller, and A.S.V. Shah. 2018. “Air Pollution and Stroke.” 
Journal of Stroke 20 (1): 2–11. https://doi.org/10.5853/jos.2017.02894.
Lind, L., E.M. Hasselquist, and H. Laudon. 2019. “Towards Ecologically 
Functional Riparian Zones: A Meta-analysis to Develop Guidelines 
for Protecting Ecosystem Functions and Biodiversity in Agricultural 
Landscapes.” Journal of Environmental Management  249 (November): 
109391. https://doi.org/10.1016/j.jenvman.2019.109391.
Litwiller, F., C. White, K. Gallant, S. Hutchinson, and B. Hamilton-Hinch. 
2016. “Recreation for Mental Health Recovery.” Leisure/Loisir  40 (3): 
345–65. https://doi.org/10.1080/1492771 3.2016.1252940.
Ludwig, C., R. Hecht, S. Lautenbach, M. Schorcht, and A. Zipf. 2021. 
“Mapping Public Urban Green Spaces Based on OpenStreetMap and 
Sentinel-2 Imagery Using Belief Functions.” ISPRS International Jour -
nal of Geo-Information  10 (4): 251. https://doi.org/10.3390/ijgi10040251 .
Majeed, H., and J.S. Floras. 2022. “Warmer Summer Nocturnal Surface 
Air Temperatures and Cardiovascular Disease Death Risk: A Popula -
tion-Based Study.” BMJ Open 12 (3): e056806.
Malik, U., and W. James. 2007. “Reliability of Design Storms 
Used to Size Urban Stormwater System Elements.” Journal of 
Water Management Modeling R227-16 (15): 309–26. https://doi.
org/10.14796/JWMM.R227-16.
Martinuzzi, S., O.M. Ramos-González, T.A. Muñoz-Erickson, D.H. 
Locke, A.E. Lugo, and V.C. Radeloff. 2018. “Vegetation Cover in Rela -
tion to Socioeconomic Factors in a Tropical City Assessed from Sub-
meter Resolution Imagery.” Ecological Applications  28 (3): 681–93. 
https://doi.org/10.1002/eap.1673.
Martinuzzi, S., D.H. Locke, O. Ramos-González, M. Sanchez, J.M. 
Grove, T.A. Muñoz-Erickson, W.J. Arendt, et al. 2021. “Exploring the 
Relationships between Tree Canopy Cover and Socioeconomic Char -
acteristics in Tropical Urban Systems: The Case of Santo Domingo, 
Dominican Republic.” Urban Forestry & Urban Greening 62 (July): 
127125. https://doi.org/10.1016/j.ufug.2021.127125.
Matthews, T., C. Raymond, J. Foster, J.W. Baldwin, C. Ivanovich, Q. 
Kong, P. Kinney, et al. 2025. “Mortality Impacts of the Most Extreme 
Heat Events.” Nature Reviews Earth & Environment 6 (3): 1–18.
McDonald, R.I., M. Colbert, M. Hamann, R. Simkin, and B. Walsh. 2018. 
Nature in the Urban Century: A Global Assessment of Where and How 
to Conserve Nature for Biodiversity and Human Wellbeing . Arlington 
County, VA: The Nature Conservancy. https://www.nature.org/en-us/
what-we-do/our-insights/perspectives/nature-in-the-urban-century/.
McFeeters, S.K. 1996. “The Rise of the Normalized Difference 
Water Index (NDWI) in the Delineation of Open Water Features.”  
International Journal of Remote Sensing  17: 1425–32. https://doi.
org/10.1080/01431169608948714.
Minion, S.C., E.E. Krans, M.M. Brooks, D.D. Mendez, and C.L. Hag -
gerty. 2022. “Association of Driving Distance to Maternity Hospitals 
and Maternal and Perinatal Outcomes.” Obstetrics and Gynecology  
140 (5): 812–19.
Moreno, C., Z. Allam, D. Chabaud, C. Gall, and F. Pratlong. 2021. 
“Introducing the ‘15-Minute City’: Sustainability, Resilience and Place 
Identity in Future Post-pandemic Cities.” Smart Cities  4 (1): 93–111.
Myhre, G., D. Shindell, F.-M. Bréon, W. Collins, J. Fuglestvedt, J. Huang, 
D. Koch, et al. 2013. “Anthropogenic and Natural Radiative Forcing.” 
In Climate Change 2013: The Physical Science Basis. Contribution of 
Working Group I to the Fifth Assessment Report of the Intergovern -
mental Panel on Climate Change, edited by T.F. Stocker, D. Qin, G.-K. 
Plattner, M. Tignor, S.K. Allen, J. Boschung, A. Nauels, et al., 659–740. 
Cambridge and New York: Cambridge University Press. https://www.
ipcc.ch/site/assets/uploads/2018/02/WG1AR5_Chapter08_FINAL.pdf .
NASA (National Aeronautics and Space Administration). 2023. “NASA 
Earth Exchange Global Daily Downscaled Projections (NEX-GDDP-
CMIP6).” August 27. https://www.nccs.nasa.gov/sites/default/files/
NEX-GDDP-CMIP6-Tech_Note.pdf.
NASA JPL (NASA Jet Propulsion Laboratory). 2020. “NASADEM 
Merged DEM Global 1 Arc Second V001.” Earth Engine Data Cata -
log. https://developers.google.com/earth-engine/datasets/catalog/
NASA_NASADEM_HGT_001.
Nicoletti, L., M. Sirenko, and T. Verma. 2022. “Disadvantaged Com -
munities Have Lower Access to Urban Infrastructure.” Environment 
and Planning B: Urban Analytics and City Science , October. https://doi.
org/10.1177/23998083221131044.
Niu, H., and E.A. Silva. 2020. “Crowdsourced Data Mining for Urban 
Activity: Review of Data Sources, Applications, and Methods.” Journal 
of Urban Planning and Development  146 (2): 04020007. https://doi.
org/10.1061/(ASCE)UP.1943-5444.0000566.
Nunes, A.R. 2024. “Heatwaves: The Silent Killers of Public Health.” 
Disaster Medicine and Public Health Preparedness 18: e227.

44  |  
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment  
Owen, D., A. Fitch, D. Fletcher, J. Knopp, G. Levin, K. Farley, E. 
Banzhaf, et al. 2024. “Opportunities and Constraints of Implement -
ing the 3-30-300 Rule for Urban Greening.” Urban Forestry & Urban 
Greening 98: 128393.
Pekel, J.-F., A. Cottam, N. Gorelick, and A.S. Belward. 2016. “High-
Resolution Mapping of Global Surface Water and Its Long-Term 
Changes.” Nature 540 (December): 418–22. https://doi.org/10.1038/
nature20584.
Pereira, R.H.M., M. Saraiva, D. Herszenhut, C.K.V. Braga, and 
M.W. Conway. 2021. “R5r: Rapid Realistic Routing on Multimodal 
Transport Networks with R5 in R.” Findings , March. https://doi.
org/10.32866/001c.21262.
Pietilä, M., M. Neuvonen, K. Borodulin, K. Korpela, T. Sievänen, and L. 
Tyrväinen. 2015. “Relationships between Exposure to Urban Green 
Spaces, Physical Activity and Self-Rated Health.” Journal of Outdoor 
Recreation and Tourism 10 (July): 44–54. https://doi.org/10.1016/j.
jort.2015.06.006 .
Pool, J.-R., D. Gibbs, S. Alexander, and N. Harris. 2022. “5 Reasons 
Cities Should Include Trees in Climate Action.” Insights (blog), July 28. 
World Resources Institute. https://www.wri.org/insights/urban-trees-
city-climate-action.
Potapov, P., M.C. Hansen, A. Pickens, A. Hernandez-Serna, A. Tyu -
kavina, S. Turubanova, V. Zalles, et al. 2022. “The Global 2000–2020 
Land Cover and Land Use Change Dataset Derived from the Landsat 
Archive: First Results.” Frontiers in Remote Sensing 3 (April). https://
doi.org/10.3389/frs en.2022.856903.
Prakash, M., S. Ramage, A. Kavvada, and S. Goodman. 2020. “Open 
Earth Observations for Sustainable Urban Development.” Remote 
Sensing 12 (10): 1646. https://doi.org/10.3 390/rs12101646.
Riahi, K., D.P. Van Vuuren, E. Kriegler, J. Edmonds, B.C. O’Neill, S. Fuji -
mori, N. Bauer, et al. 2017. “The Shared Socioeconomic Pathways and 
Their Energy, Land Use, and Greenhouse Gas Emissions Implications: 
An Overview.” Global Environmental Change 42 (January): 153–68. 
https://doi.org/10.1016/j.gloenvcha.2016.05.009.
Rodríguez-López, C., Z.M. Salas-Fariña, E. Villa-González, M. Borges-
Cosic, M. Herrador-Colmenero, J. Medina-Casaubón, F.B. Ortega, et al. 
2017. “The Threshold Distance Associated with Walking from Home to 
School.” Health, Education and Behavior  44 (6): 857–66.
Rosenberg, E.A., P.W. Keys, D.B. Booth, D. Hartley, J. Burkey, A.C. 
Steinemann, and D.P. Lettenmaier. 2010. “Precipitation Extremes and 
the Impacts of Climate Change on Stormwater Infrastructure in Wash -
ington State.” Climatic Change 102 (September): 319–49. https://doi.
org/10.1007/s10584-010-9847-0.
Runfola, D., A. Anderson, H. Baier, M. Crittenden, E. Dowker, S. Fuhrig, 
S. Goodman, et al. 2020. “GeoBoundaries: A Global Database of Politi -
cal Administrative Boundaries.” PLOS One  15 (4): e0231866. https://
doi.org/10.1371/journal.pone.0231866 .
Salcedo-Sanz, S., P. Ghamisi, M. Piles, M. Werner, L. Cuadra, A. 
Moreno-Martínez, E. Izquierdo-Verdiguier, et al. 2020. “Machine 
Learning Information Fusion in Earth Observation: A Comprehen -
sive Review of Methods, Applications and Data Sources.” Infor -
mation Fusion 63 (November): 256–72. https://doi.org/10.1016/j.
inffus.2020.07.004.
Saraiva, M., R.H.M. Pereira, D. Herszenhut, C.K.V. Braga, M.W. Bhagat-
Conway, and L. Liu. 2025. “Package r5r.” Version 2.1.0. https://cran.r-
project.org/web/packages/r5r/r5r.pdf.
Sathyakumar, V., R. Ramsankaran, and R. Bardhan. 2020. “Geospatial 
Approach for Assessing Spatiotemporal Dynamics of Urban Green 
Space Distribution among Neighbourhoods: A Demonstration in 
Mumbai.” Urban Forestry & Urban Greening 48 (February): 126585. 
https://doi.org/10.1016/j.ufug.2020.126585.
Schimpl, M., C. Moore, C. Lederer, A. Neuhaus, J. Sambrook, J. Danesh, 
W. Ouwehand, et al. 2011. “Association between Walking Speed and 
Age in Healthy, Free-Living Individuals Using Mobile Accelerometry: 
A Cross-Sectional Study.” PLOS One 6 (8): e23299. 
Sekertekin, A. 2021. “A Survey on Global Thresholding Methods for 
Mapping Open Water Body Using Sentinel-2 Satellite Imagery and 
Normalized Difference Water Index.” Archives of Computational Meth -
ods in Engineering 28 (3): 1335–47.
Shindell, D.T. 2015. “The Social Cost of Atmospheric Release.” Climatic 
Change 130 (2): 313–26. https://doi.org/10.1007/s10584-015-1343-0.
Song, Y., and P. Wu. 2021. “Earth Observation for Sustainable In -
frastructure: A Review.” Remote Sensing  13 (8): 1528. https://doi.
org/10.3390/rs13081528.
Song, D.X., Z. Wang, T. He, H. Wang, and S. Liang. 2022. “Estima -
tion and Validation of 30 M Fractional Vegetation Cover over China 
through Integrated Use of Landsat 8 and Gaofen 2 Data.” Science of 
Remote Sensing 6: 100058.
Stanley, T., and D.B. Kirschbaum. 2017. “A Heuristic Approach to Global 
Landslide Susceptibility Mapping.” Natural Hazards  87 (May): 145–64. 
https://doi.org/10.1007/s11069-017-2757-y.
Sugiarto, W. 2022. “Impact of Wildlife Crossing Structures on Wildlife-
Vehicle Collisions.” Transportation Research Record , August. https://
doi.org/10.1177/036 11981221108158.
Terrestrial Ecosystems. n.d. “Species Accumulation Curves.” https://
terrestrialecosystems.com/species-accumulation-curves/. Accessed 
November 9, 2022.
Thomson, D.R., D.R. Leasure, T. Bird, N. Tzavidis, and A.J. Tatem. 
2022. “How Accurate Are WorldPop-Global-Unconstrained Gridded 
Population Data at the Cell-Level? A Simulation Analysis in Urban 
Namibia.” PLOS One 17 (7): e0271504. https://doi.org/10.1371/journal.
pone.0271504. 
Tolan, J., H.I. Yang, B. Nosarzewski, G. Couairon, H.V. Vo, J. Brandt, J. 
Spore, et al. 2024. “Very High Resolution Canopy Height Maps from 
RGB Imagery Using Self-Supervised Vision Transformer and Convo -
lutional Decoder Trained on Aerial Lidar.” Remote Sensing of Environ -
ment 300: 113888.

TECHNICAL NOTE  |  November 2025  |  45
Calculating indicators from global geospatial datasets to benchmark and track changes in the urban environment
Tsendbazar, N., L. Li, M. Koopman, S. Carter, M. Herold, I. Georgieva, 
and M. Lesiv. 2021. WorldCover Product Validation Report, Version 1.1 . 
Paris: European Space Agency. https://esa-worldcover.s3.eu-central-1.
amazonaws.com/v100/2020/docs/WorldCover_PVR_V1.1.pdf . 
UN (United Nations). n.d. “Goal 11.” https://sdgs.un.org/goals/goal11. 
Accessed December 13, 2022.
Underwood, B.S., Z. Guido, P. Gudipudi, and Y. Feinberg. 2017. 
“Increased Costs to US Pavement Infrastructure from Future Tem -
perature Rise.” Nature Climate Change 7 (October): 704–7. https://doi.
org/10.1038/nclimate3390.
UN DESA (UN Department of Economic and Social Affairs). 2022. 
Methodology, United Nations Database on Household Size and 
Composition 2022 . UN DESA/POP/2022/DC/NO. 8. New York: 
United Nations.
UNEP-WCMC and IUCN (UN Environment Programme World Con -
servation Monitoring Centre and International Union for Conserva -
tion of Nature). n.d. (Database.) Protected Planet: The World Database 
on Protected Areas (WDPA). UNEP-WCMC and IUCN. https://www.
protectedplanet.net/.
UN-Habitat (UN Human Settlements Programme). 2018. SDG Indicator 
11.2.1 Training Module: Public Transport System . Nairobi: UN-Habitat.
UN-Habitat. 2020. Metadata on SDGs Indicator 11.7.1. Nairobi: UN-
Habitat. https://unhabitat.org/sites/default/files/2020/11/metadata_
on_sdg_indicator_11.7.1_02-2020_1.pdf .
UN-Habitat. 2022. The Global Urban Monitoring Framework. Nairobi: 
UN-Habitat. https://unhabitat.org/sites/default/files/2022/08/the_
global_urban_monitoring_framework_metadata.pdf.
van der Kamp, J. 2017. Social Cost-Benefit Analysis of Air Pollution 
Control Measures: Advancing Environmental-Economic Assessment 
Methods to Evaluate Industrial Point Emission Sources . Karlsruhe, 
Germany: Karlsruher Institut für Technologie. https://doi.org/10.5445/
KSP/1000072046.
van Donkelaar, A., M.S. Hammer, L. Bindle, M. Brauer, J.R. Brook, M.J. 
Garay, N.C. Hsu, et al. 2021. “Monthly Global Estimates of Fine Particu -
late Matter and Their Uncertainty.” Environmental Science & Technol -
ogy 55 (22): 15287–300. https://doi.org/10.1021/acs.est.1c05309 .
van Oorschot, J., M. Slootweg, R.P. Remme, B. Sprecher, and E. van der 
Voet. 2024. “Optimizing Green and Gray Infrastructure Planning for 
Sustainable Urban Development.” npj Urban Sustainability  4 (1): 41.
Volin, E., A. Ellis, S. Hirabayashi, S. Maco, D.J. Nowak, J. Parent, and R.T. 
Fahey. 2020. “Assessing Macro-scale Patterns in Urban Tree Canopy 
and Inequality.” Urban Forestry & Urban Greening 55 (November): 
126818. https://doi.org/10.1016/j.ufug.2020.126818.
Wang, C., Z.-H. Wang, and J. Yang. 2018. “Cooling Effect of Urban Trees 
on the Built Environment of Contiguous United States.” Earth’s Future 
6 (8): 1066–81. https://doi.org/10.102 9/2018EF000891.
Wang, Y., C. Huang, Y. Feng, M. Zhao, and J. Gu. 2020. “Using Earth 
Observation for Monitoring SDG 11.3.1-Ratio of Land Consumption 
Rate to Population Growth Rate in Mainland China.” Remote Sensing  
12 (3): 357. https://doi.org/10.3 390/rs12030357.
Ward, P.J., H.C. Winsemius, S. Kuzma, M.F.P. Bierkens, A. Bouwman, 
H.D. Moel, A.D. Loaiza, et al. 2020. “Aqueduct Floods Methodology.” 
Technical Note. Washington, DC: World Resources Institute. https://
www.wri.org/research/aqueduct-floods-methodology .
Wellmann, T., A. Lausch, E. Andersson, S. Knapp, C. Cortinovis, J. 
Jache, S. Scheuer, et al. 2020. “Remote Sensing in Urban Planning: 
Contributions towards Ecologically Sound Policies?” Landscape and 
Urban Planning 204 (December): 103921. https://doi.org/10.1016/j.
landurbplan.2020.103921.
Wesley, E.J., and N.A. Brunsell. 2019. “Greenspace Pattern and the 
Surface Urban Heat Island: A Biophysically-Based Approach to 
Investigating the Effects of Urban Landscape Configuration.” Remote 
Sensing 11 (19): 2322.
WHO (World Health Organization). 2021. WHO Global Air Quality 
Guidelines: Particulate Matter (PM 2.5 and PM10), Ozone, Nitrogen Diox -
ide, Sulfur Dioxide and Carbon Monoxide . Geneva: WHO. https://www.
who.int/publications-detail-redirect/9789240034228 .
Wilson, S.J., E. Juno, J.-R. Pool, S. Ray, M. Phillips, S. Francisco, and S. 
McCallum. 2022. Better Forests, Better Cities . Washington, DC: World 
Resources Institute. https://www.wri.org/research/better-forests-
better-cities .
Wong, T., and P. Switzer. 2023. “Estimating Future Local Climate Haz -
ard Probabilities.” Technical Note. Washington, DC: World Resources 
Institute. https://doi.org/10.46830/writn.22.00074.
Wong, T., and E. Mackres. 2024. “City-Scale, City-Relevant Climate 
Hazard Indicators under 1.5°C, 2.0°C, and 3.0°C of Global Warming.” 
Technical Note. Washington, DC: World Resources Institute. https://
doi.org/10.46830/writn.23.00154.
WorldPop. n.d. “WorldPop Global Population Data.” Earth Engine Data 
Catalog. https://developers.google.com/earth-engine/datasets/cata -
log/WorldPop_GP_100m_pop. Accessed November 8, 2022.
Xu, Z., G. FitzGerald, Y. Guo, B. Jalaludin, and S. Tong. 2016. “Impact of 
Heatwave on Mortality under Different Heatwave Definitions: A Sys -
tematic Review and Meta-analysis.” Environment International  89–90 
(April–May): 193–203. https://doi.org/10.1016/j.envint.2016.02.007.
Zanaga, D., R. Van De Kerchove, W. De Keersmaecker, N. Souverijns, 
C. Brockmann, R. Quast, J. Wevers, et al. 2021. “ESA WorldCover 10 M 
2020 V100.” Zenodo. https://doi.org/10.5281/zenodo.5571936 .
Zeng, X., R.E. Dickinson, A. Walker, M. Shaikh, R.S. DeFries, and J. Qi. 
2000. “Derivation and Evaluation of Global 1-km Fractional Vegetation 
Cover Data for Land Modeling.” Journal of Applied Meteorology  39 (6): 
826–839. https://doi.org/10.1175/1520-0450(2000)039<0826:D AEOGK
>2.0.CO;2.
Zerger, A., and D.I. Smith. 2003. “Impediments to Using GIS for Real-
Time Disaster Decision Support.” Computers, Environment and Urban 
Systems 27 (2): 123–41. https://doi.org/10.1016/S0198-9 715(01)00021-7.
Zhang, M., S. Tan, C. Zhang, S. Han, S. Zou, and E. Chen. 2023. “As -
sessing the Impact of Fractional Vegetation Cover on Urban Thermal 
Environment: A Case Study of Hangzhou, China.” Sustainable Cities 
and Society 96: 104663.

Copyright 2025 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License.  
To view a copy of the license, visit http://creativecommons.org/licenses/by/4.0/
  
10 G Street, NE  |  Washington, DC 20002  |  WRI.ORG
Acknowledgments
This research was made possible by the UrbanShift and 
Cities4Forests initiatives. We are thankful for the financial support 
of those initiatives from the Global Environment Facility and the 
United Kingdom Department for Environment, Food & Rural Affairs, 
respectively, which supported this research. 
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
About the Authors
Eric Mackres  is senior manager for urban analytics and data 
innovation at WRI Ross Center for Sustainable Cities.
Ted Wong is a research and project associate on the Urban Analytics 
and Data Innovation team at WRI Ross Center for Sustainable Cities.
Saif Shabou  is an urban data and analytics associate on the 
Urban Analytics and Data Innovation team at WRI Ross Center for 
Sustainable Cities.
Elizabeth Jane  Wesley is a data scientist, urban surfaces and 
extreme heat, at WRI Ross Center for Sustainable Cities.
Thet Hein Tun is a senior transportation research associate at WRI 
Ross Center for Sustainable Cities.
About WRI
World Resources Institute works to improve people’s lives, protect 
and restore nature, and stabilize the climate. As an independent 
research organization, we leverage our data, expertise, and global 
reach to influence policy and catalyze change across systems like 
food, land and water; energy; and cities. Our 2,000+ staff work on the 
ground in more than a dozen focus countries and with partners in 
over 50 nations.
