---
doc_id: 2024_city-scale-city-relevant-climate-hazard_3175
source_pdf: kp-docs/askwri-kps/2024_city-scale-city-relevant-climate-hazard_3175.pdf
extraction_method: cache-plaintext
char_count: 107001
title: City-Scale, City-Relevant Climate Hazard Indicators Under 1.5°C, 2.0°C, and 3.0°C of Global Warming
authors: Wong, Ted; Mackres, Eric
date_published: 9/19/2024
article_type: Technical Note
sub_tag: Transport decarbonization
wri_primary_office: WRI Global
wri_programs: Cities
language: English
url: "https://www.wri.org/research/technical-note-city-climate-hazards-warming-scenarios"
doi: "https://doi.org/10.46830/writn.23.00154"
summary: This paper describes a data set of 14 temperature- and precipitation-related climate hazard indicators, calculated for 996 cities at the 1.5°C, 2.0°C, and 3.0°C global warming scenarios.
---

# City-Scale, City-Relevant Climate Hazard Indicators Under 1.5°C, 2.0°C, and 3.0°C of Global Warming

TECHNICAL NOTE   |  Version 1.0  |  August 2024  |  1
WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
WO RL DWO RL D
RE SO UR CE SRE SO UR CE S
IN STIT UT EIN STIT UT E
CONTENTS
Abstract. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
Overview. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
Methods .................................. 2
Results ................................... 10
Discussion ............................... 17
Data Availability. . . . . . . . . . . . . . . . . . . . . . . . . .19
Appendix. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
Endnotes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
References .............................. 22
Acknowledgments ...................... 28
About the authors. . . . . . . . . . . . . . . . . . . . . . . 28
About WRI  .............................. 28
Technical notes document the research or analytical 
methodology underpinning a publication, interactive 
application, or tool.
Suggested Citation: Wong, T . and E. Mackres. 2024. 
“City-scale, city-relevant climate hazard indicators 
under 1.5°C, 2.0°C, and 3.0°C of global warming.” 
Technical Note. Washington, DC: World Resources 
Institute. Available online at: doi.org/10.46830/
writn.23.00154.
TECHNICAL NOTE
City-scale, city-relevant climate hazard 
indicators under 1.5°C, 2.0°C, and 3.0°C  
of global warming
Theodore Wong and Eric Mackres
ABSTRACT
We present a data set reporting estimates of average values of 14 temperature-, 
humidity- and precipitation-based climate hazards for the world’s most popu-
lous 996 cities under three global warming scenarios: 1.5°C, 2.0°C, and 3.0°C 
above a preindustrial (1880–1900) baseline. We also report probabilities that the 
hazard magnitudes exceed certain extreme values. The hazards focus on themes 
of operational and planning relevance to city government decision-makers in 
public health, infrastructure, and economic productivity. Hazard magnitude 
probabilities were estimated from probability models parameterized from three 
downscaled global climate models (from NEX-GDDP-CMIP6) determined 
to be most appropriate for each location based on comparison with historical 
reanalysis data. Across all 996 cities studied, heat waves become, on average, 
longer and more frequent as the world warms. Number of days with optimal 
temperature for the malaria vector Anopheles gambiae decreases modestly, but 
days with optimal temperature for the arbovirus vectors Aedes aegypti and Aedes 
albopictus become more frequent. Precipitation-based hazards change little when 
averaged across all 996 cities, but differences arise when cities are disaggregated 
by region or income level. We provide the data publicly to aid decision-makers 
in climate action planning and to illustrate the dire consequences for cities if 
global warming is allowed to exceed the 1.5°C Paris Agreement target.
OVERVIEW
In the global climate policy discourse, outcome targets are frequently expressed 
in terms of global mean surface temperature (GMST). The 2015 Paris Agree-
ment, for example, establishes a target to limit global warming to 1.5°C above 
the preindustrial average (UNFCCC 2016), and a great deal of research has 
focused on identifying the policies and actions that are compatible with that 
target (e.g., Millar et al. 2017; Tilmes et al. 2020; Meinshausen et al. 2022; 
Riahi et al. 2022). As an indicator, GMST is convenient and useful—it encap-
sulates in a single number the degree to which the climate has changed from 
a preindustrial baseline. It does not, however, directly provide decision-makers

2  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
or the public with specific information about the climate futures 
they or their constituents will face or the local consequences to 
ecosystems, people, or economies. Moreover, analyses of the con-
sequences of increasing GMST for ecosystems and societies have 
tended to be global or regional in scale (Arnell et al. 2018; IPCC 
2018) and have focused on regional systems such as agriculture or 
water (Schleussner et al. 2016; Ren et al. 2018).
We are publishing a data set1 that estimates climate hazard 
magnitudes that cities will face as GMST increases. For three 
warming levels—+1.5°C, +2.0°C, and +3.0°C—we estimated 
the average values of 14 city-relevant climate hazards for the 
world’s most populous 996 cities. For each city, we also estimated 
the probabilities that hazard magnitude values exceed particular 
extreme thresholds. The hazards were chosen to address climate 
adaptation decision-making in public health, infrastructure 
maintenance, and economic productivity. Local decision-makers 
in the included cities can use the estimates to guide planning and 
policy for climate adaptation and mitigation. The estimates also 
predict clear differences between the +1.5°C and +3.0°C sce-
narios. Differences in direction and degree of change exist when 
cities are disaggregated by region and income level; yet in general, 
urban dwellers in a +3.0°C world will see greater extremes of 
high temperature, as well as a modest increase in drought, com-
pared to the +1.5°C scenario.
METHODS
City selection
Our analysis encompasses the 996 cities globally (Figure 1) 
whose 2015 populations were greater than 500,000 according 
to the Global Human Settlement Layer (GHSL) Urban Centre 
Database, version 1.2 (Florczyk et al. 2019). The cities include 
roughly 2 billion people, or 56 percent of the roughly 3.5 billion 
urban dwellers represented in the cities of the database. We 
chose this data set because it is currently the only global data set 
that spatially delineates urban areas and associates them with 
place names. Cities are defined in the Urban Centre Database 
based on resident population and built-up land share, and they 
are metropolitan areas rather than cities as defined by admin-
istrative boundaries. Our indicator calculation method uses 
point locations, so we used the centroid of each GHSL urban-
center polygon to estimate the climate hazard probabilities. We 
acknowledge that our approach does not support within-city 
analyses, but researchers focusing on one city or region might be 
able to obtain high-resolution climate simulations—for example, 
from regional models—and apply our methods to obtain high-
resolution results.
Figure 1  |   Cities included in this study 
Note: For the study, 996 cities were chosen for having populations larger than 500,000 in 2015, according to the Global Human Settlement Layer Urban Centre Database.
Source: Florczyk et al. 2019.

TECHNICAL NOTE   |  August 2024  |  3
City-scale, city-relevant climate hazard indicators under 1.5°C, 2.0°C, and 3.0°C of global warming
Models
All estimates of future hazards are calculated from nine global 
climate models included in the NEX-GDDP-CMIP6 col-
lection of downscaled model outputs (Thrasher et al. 2022). 
NEX-GDDP-CMIP6 is frequently used in local-scale climate 
impact studies (e.g., Zhang et al. 2023, Paul and Maity 2023, 
Rao et al. 2024). All NEX-GDDP-CMIP6 models have a 
horizontal spatial resolution of 0.25 degrees. The corresponding 
ground distance varies by latitude but is approximately 25 kilo-
meters for many of our cities. These model outputs include daily 
minimum, maximum, and mean air temperature at two meters 
above Earth’s surface; daily cumulative precipitation; average 
daily relative humidity; and average daily wind speed. 
As processed for storage in Google Earth Engine (Gorelick 
et al. 2017), the model outputs are available as daily values for 
the period 1950–2100 for the historical scenario and for two 
greenhouse gas emissions scenarios. For the years 2015–2100, 
the greenhouse gas emissions scenario can be specified as 
either of two Shared Socioeconomic Pathway (SSP) scenarios: 
SSP2-4.5 or SSP5-8.5 (see Riahi et al. [2017] for discussion of 
SSP scenarios).
Kuma et al. (2023) found that models derived from the same 
original code—that is, members of the same model families—
can produce results that are more similar to each other than 
models of different families. Failure to account for similarities 
within model families can lead to underestimating uncertainty 
in predictions. NEX-GDDP-CMIP6 includes 35 models, 
which represent nine model families. To avoid oversampling any 
particular model family, and because the scope of this project 
required us to limit the models to a manageable number, we 
used only one randomly chosen model from each of the nine 
model families. Table 1 lists the selected models, their families, 
and the research institutions that created and maintain them.
Table 1  |   Climate models included in NEX-GDDP-CMIP6, with model families
MODEL MODEL FAMILY INSTITUTION
CanESM5 CanAM Canadian Centre for Climate Modelling and Analysis
EC-Earth3-
Veg-LR
ECMWF EC-Earth Consortium (Agencia Estatal de Meteorología, Spain; Barcelona Supercomputing Center, Spain; Consiglio Nazionale 
delle Ricerche–Instituto di Scienze dell’Atmosfera e del Clima, Italy; Danish Meteorological Institute, Denmark; Ente per le Nuove 
Technologie l’Energia e l’Ambiente, Italy; Finnish Meteorological Institute, Finland; Geomar, Germany; Irish Centre for High-
End Computing, Ireland; International Centre for Theoretical Physics, Italy; Instituto Dom Luiz, Portugal; Institute for Marine 
and Atmospheric research Utrecht, Netherlands; Instituto Português do Mar e da Atmosfera, Portugal; Karlsruhe Institute of 
Technology, Germany; Royal Netherlands Meteorological Institute, Netherlands; Lund University, Sweden; Met Eireann, Ireland; 
Netherlands eScience Center, Netherlands; Norwegian University of Science and Technology, Norway; Oxford University, United 
Kingdom; SURFsara, Netherlands; Swedish Meteorological and Hydrological Institute, Sweden; Stockholm University, Sweden; 
Unite ASTR, Belgium; University College Dublin, Ireland; University of Bergen, Norway; University of Copenhagen, Denmark; 
University of Helsinki, Finland; University of Santiago de Compostela, Spain; Uppsala University, Sweden; Utrecht University, 
Netherlands; Vrije Universiteit Amsterdam, Netherlands; Wageningen University, Netherlands)
FGOALS-g3 CCM Chinese Academy of Sciences
GFDL-ESM4 GFDL National Oceanic and Atmospheric Administration (United States), Geophysical Fluid Dynamics Laboratory
INM-CM5-0 INM Institute for Numerical Mathematics, Russian Academy of Science
IPSL- CM6A-LR IPSL Institut Pierre Simon Laplace
MIROC-ES2L MIROC Japan Agency for Marine-Earth Science and Technology
MRI-ESM2-0 UCLA GCM Meteorological Research Institute (Japan)
UKESM1-0-LL HadAM Met Office Hadley Centre; Natural Environment Research Council (United Kingdom); National Institute of Meteorological 
Sciences/Korea Meteorological Administration
Notes: We acknowledge the World Climate Research Programme, which, through its Working Group on Coupled Modelling, coordinated and promoted the Coupled Model 
Intercomparison Project Phase 6 (CMIP6). We thank the climate modeling groups for producing and making available their model output, the Earth System Grid Federation (ESGF) for 
archiving the data and providing access, and the multiple funding agencies that support CMIP6 and ESGF. Model families are from Kuma et al. (2023).

4  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
Warming scenario years
Assessing climate futures at various GMST values requires pro-
jections for future meteorological conditions that are associated 
with those GMSTs. One could identify two general approaches 
to obtaining or identifying the relevant meteorological projec-
tions: generating climate model data specifically for target 
GMSTs or examining climate models that at some point exceed 
target GMSTs and then identifying time intervals whose time-
averaged GMSTs correspond to the GMSTs of interest.
The first approach, which we did not take, finds or derives 
climate model runs that stabilize at the target GMST by a spec-
ified future year. The difficulty in this approach is that the major 
model intercomparison projects do not include model runs that 
correspond closely to all GMSTs of interest. Some studies (e.g., 
Mitchell et al. 2017; Sieck et al. 2021) address this issue by using 
weighted averages of the models that stabilize closest to the 
target GMSTs. Others (e.g., Sanderson 2017; Nangombe 2018) 
create simplified emulations of published global climate models 
and run the emulations with greenhouse gas emissions pathways 
that produce the desired equilibrium GMSTs. Both methods 
generate model outputs at the coarse spatial resolutions of global 
climate models, so using them for our city-focused study would 
require computationally expensive downscaling.
We took the second approach. Following Schleussner et al. 
(2016), Dosio et al. (2018), Jacob et al. (2018), and Li et al. 
(2022), we examined model runs that span our GMSTs of inter-
est and identified within each of them multiyear periods with 
the average GMST values of interest. This approach allowed 
us to use the NEX-GDDP-CMIP6 models, which come with 
two advantages: they are downscaled to a city-relevant spatial 
scale, and we were able to access several independent models for 
each variable-location combination and select the models for 
each location that seem to minimize the unavoidable regional 
biases that all global climate models have. Note that it will often 
be the case that a single city’s heat-based hazard indicators are 
estimated using different models from those used to estimate 
precipitation-based hazard indicators. This should create no 
difficulties as long as different hazard indicators are examined 
separately from each other. Specifically, indicators for different 
hazards should not be combined into compound indicators. 
For example, the probabilities of exceeding extreme-magnitude 
thresholds for two hazards should not be combined into a 
joint probability.
Specifically, for each of the NEX-GDDP-CMIP6 models we 
used, we calculated the model’s recent historical reference period 
level as the average GMST over every day of the 20-year period 
1995–2014. Dosio et al. (2018) estimate that the GMST in 
these 20 years, centered on 2005, is 0.81°C above a preindustrial 
baseline, so GMST values of +1.5°C, +2.0°C, and +3.0°C above 
the same preindustrial baseline correspond to these values minus 
the 2005 value, or +0.69°C, +1.19°C, and +2.19°C above the 
recent historical reference period level.
GMST was calculated in Google Earth Engine using the 
function ee.Reducer.mean() and applied to the average two-
meter-height air temperature over the entire globe. For each 
year during the 2015–2091 period, we identified the first year 
at which the average exceeded +0.69°C, +1.19°C, and +2.19°C 
relative to the 20-year average GMST for 1995–2014. The time 
interval for which we estimate annual average climate hazard 
indicators was the 10-year interval centered on this year. (In 
the rest of this paper we refer to the warming scenarios by the 
GMSTs relative to the preindustrial baseline—that is, +1.5°C, 
+2.0°C, and +3.0°C—rather than by the GMSTs relative to 
1995–2014.) For every model, the SSP2-4.5 emissions scenario 
allowed us to find 10-year intervals with little or no overlap 
between the +1.5°C and +2.0°C scenarios and between the 
+2.0°C and +3.0°C scenarios. For our purposes, only the degree 
to which Earth has warmed—and not the emissions pathway 
that caused the warming—is relevant.
Figure 3 represents the GMST trajectories for each of the 
model scenarios used, and Table 3 lists the center-point years of 
the time intervals corresponding to their GMST warming levels. 
For four of the models (MRI-ESM2-0, FGOALS-g3, IPSL-
CM6A-LR, and CanESM5), there is some overlap between the 
+1.5°C and +2.0°C scenario intervals. In these cases it is difficult 
to distinguish between these warming levels.

TECHNICAL NOTE   |  August 2024  |  5
City-scale, city-relevant climate hazard indicators under 1.5°C, 2.0°C, and 3.0°C of global warming
Figure 2  |   GMST trajectories as modeled by the nine NEX-GDDP-CMIP6 models used in this study
Notes: Temperatures from each model are given as changes relative to the 1880–1900 preindustrial baseline. Each model’s +1.5°C, +2.0°C, and +3.0°C scenario years are the 10-year 
windows roughly centered on the year when the model first exceeds the warming level of interest. Target global mean surface temperatures are indicated by the horizontal red lines.
Source: WRI authors.
Global mean surface temperature (°C)
2010 2020 2030 2040 2050 2060 2070 2080 2090
Year
UKESM1-0-LL
CanESM5
IPSL-CM6A-LR
EC-Earth3-Veg-LR
MIROC-ES2L
MRI-ESM2-0
GFDL-ESM4
FGOALS-g3
INM-CM5-0
7
6
5
4
3
2
1
1.5
0
Table 2  |   Center-point years for each global warming 
scenario
MODEL +1.5°C +2.0°C +3.0°C
MIROC-ES2L 2019 2035 2055
UKESM1-0-LL 2015 2024 2034
EC-Earth3-Veg-LR 2015 2024 2060
GFDL-ESM4 2018 2031 2053
INM-CM5-0 2032 2044 2086
MRI-ESM2-0 2018 2024 2048
FGOALS-g3 2020 2025 2068
IPSL- CM6A-LR 2021 2029 2042
CanESM5 2017 2022 2028
Note: Center-point years are the years on which, roughly, the model’s global mean 
surface temperature first exceeds 1.5°C , 2.0°C , or 3.0°C  above the 1880–1900 baseline. 
All indicator values in this study were calculated using model outputs from the 10-year 
windows approximately centered on the center-point years.
Source: WRI Authors.
Hazards
In this paper, we use climate hazard to mean a defined meteoro-
logical condition that without mitigation causes or exacerbates 
a negative societal impact. We chose 10 climate hazards based 
primarily on temperature and 4 based on precipitation. (One 
temperature hazard also uses relative humidity.) We selected 
hazard definitions based on relevance to public health, infra-
structure, and economic productivity; interviews and other 
engagements with local governments; and the authors’ general 
knowledge of the data needs of local governments for climate 
adaptation planning. The city engagements include interviews 
with the governments of Hobart, Australia; Makati, Philippines; 
Tópaga, Colombia; and Vitacura, Chile, conducted in 2021 in 
collaboration with the Global Covenant of Mayors for Climate 
and Energy for a pilot adaptation-data project. The interviews 
focused on which climate hazards were of concern and what 
role hazard projections might play in planning. We also engaged 
with the government of Campinas, Brazil, as part of a World 
Resources Institute partnership with Campinas focused on 
climate action planning. In this project we worked with the

6  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
Campinas government to identify and define climate hazard 
indicators. In general in the present project, we chose hazards 
whose indicator calculations were simple but demonstrative 
of our methods’ capabilities and which addressed a variety of 
hazards relevant to public health, infrastructure maintenance, 
and economic productivity.
It is useful to note that this project addresses climate hazards 
only. It does not address how cities differ in their vulnerability 
(due to demographic, socioeconomic, or geographic factors 
unrelated to climate) or their ability to tolerate or adapt to 
climate extremes. (See Begum et al. 2022, particularly Figure 
1.5 and discussion thereof, for a more complete treatment of the 
interplay of hazard, vulnerability, and exposure.) Furthermore, 
the climate hazards we deal with are limited to those whose def-
initions include air temperature, precipitation, and, in the case 
of one hazard, humidity. Because of limitations in the climate 
simulations that we used, wind, shade, and the direct effects of 
solar radiation are not included in these hazards. Nothing in our 
methods would preclude inclusion of these variables in future 
work if appropriate models and historical data become available.
Maximum annual temperature (Tmax_highest)
Extremely high temperatures can cause illness in humans (Lin 
et al. 2009) and damage transportation and energy infrastruc-
ture (Underwood et al. 2017; Burillo et al. 2019). It is therefore 
useful for health and engineering departments to know both 
average values of this hazard and probabilities of temperature 
extremes reaching particular asset-specific thresholds. The  
hazard Tmax_highest is the highest temperature in a single year.
We calculate this hazard as the maximum value of Tmax in a cal-
endar year, where Tmax is the maximum daily air temperature at a 
height of two meters. We report magnitudes in degrees Celsius.
Days-hotter-than-threshold hazards
Extreme heat is associated with increased morbidity and mortal-
ity (Mathes et al. 2017; Green et al. 2019; Khatana et al. 2022), 
decreased economic activity (Morrissey et al. 2021; Zhao et 
al. 2021), and increased energy expenditure (Auffhammer and 
Mansur 2014; Zhang et al. 2022). The hazards Tmax95pctl_days, 
Tmax35_days, and Tmax40_days all describe the number of 
days in a year on which the high temperature equals or exceeds 
a threshold. The definitions we use do not consider humid-
ity, which would exacerbate the health and economic harms 
of these hazards.
Annual days with maximum temperature 
equal to or exceeding the 95th percentile 
(Tmax95pctl_days)
The threshold for Tmax95pctl_days is the local 95th percentile of 
daily high temperature for that city, calculated from the 40-year 
period 1980–2019. We used this interval because it includes the 
earliest years available in our observed-climate data set, ERA5, 
as stored as daily aggregates in Google Earth Engine. A hazard 
pegged to a locally defined extreme is useful because many 
negative impacts of temperature are associated with devia-
tions from local norms (Medina-Ramón and Schwartz 2007; 
Lee et al. 2014). 
We calculated this hazard as the number of days in a calendar 
year on which Tmax equals or exceeds the local 95th percentile  
of Tmax.
Annual days with maximum temperature equal 
to or exceeding 35°C (Tmax35 _days)
Similar to Tmax95pctl_days, the hazard Tmax35_days is the 
number of days in a year on which the high temperature equals 
or exceeds 35°C. This temperature is commonly accepted as 
a human-tolerance threshold because extended exposure to 
a humid environment at 35°C is likely lethal (Sherwood and 
Huber 2010). The number of days with dangerously high 
temperatures is relevant not only for public health but also for 
economic productivity because outdoor labor and occupancy of 
uncooled buildings become dangerous. 
We calculated this hazard as the number of days in a calendar 
year on which Tmax equals or exceeds 35°C.
Annual days with maximum temperature equal 
to or exceeding 40°C (Tmax40_days)
Similar to Tmax35_days, the hazard Tmax40_days is the number 
of days in a year on which the high temperature equals or 
exceeds 40°C. This temperature was chosen as a critical tem-
perature for infrastructure operation because it is a standard 
maximum-rated outdoor ambient temperature for electrical 
transformers (IEEE 2012; IEC 2018). 
We calculated this hazard as the number of days in a calendar 
year on which Tmax equals or exceeds 40°C.
Annual cooling degree-days (CDD21)
The demand for the cooling of buildings is directly related 
to cooling degree-days (CDDs; De Rosa 2015), a commonly 
used hazard based on deviations above a reference temperature.

TECHNICAL NOTE   |  August 2024  |  7
City-scale, city-relevant climate hazard indicators under 1.5°C, 2.0°C, and 3.0°C of global warming
Numerous studies have used CDDs to model the relationship 
between temperature regime and demand for cooling (e.g., Jiang 
et al. 2009; Petri and Caldeira 2015; Andrade et al. 2021; Ukey 
and Rai 2021). For this hazard, we used 21°C as the reference 
temperature because recent country-level work by Scoccimarro 
et al. (2023) predicts widespread increases in CDD21.
We calculated this hazard as
where the sum is over the days in the calendar year, and Tavg is 
the respective day’s mean air temperature at two-meter height. 
Our data set presents CDD21 as this absolute quantity, but local 
differences in the prevalence and energy efficiency of cooling 
technology make it difficult to reach energy-consumption con-
clusions based on comparisons of raw CDD values among cities. 
There is no universal conversion coefficient that maps CDDs 
to, say, joules. 
Annual days with wet-bulb temperature equal to 
or exceeding 31°C (Twb31_days)
Wet-bulb temperature, Twb, is a thermal-comfort measure that 
takes into account both air temperature and the evaporative 
cooling effects of humidity. It differs from wet-bulb globe 
temperature in that Twb does not consider the effects of wind 
or shade. Extended exposure to Twb greater than 30°C–31°C 
can lead to heat-related illness and possibly death (Vecel-
lio et al. 2022).
The advantage of Twb over wet-bulb globe temperature is that it 
can easily be estimated from commonly measured and modeled 
meteorological variables. We calculate Twb using the formula 
of Stull (2011):
where RH is relative humidity expressed as a percent (e.g., 
“65” for “65 percent humidity”) and is reported in the NEX-
GDDP-CMIP6 models. T is air temperature. For T we used 
Tmax. The hazard is the number of days on which Twb equals 
or exceeds 31°C.
Heat waves
Heat waves are periods of abnormally hot weather (Möller et al. 
2022). Precise definitions differ with context, with different stud-
ies specifying different thresholds for “hot,” different minimum 
durations of the “period,” and different temperature variables (i.e., 
maximum, minimum, or average daily temperature or else a ther-
mal-comfort hazard such as wet-bulb temperature). Heat waves, 
in general, are associated with increases in mortality (Anderson 
and Bell 2011; Ragettli et al. 2017; Faurie et al. 2022), though 
the magnitude of the increase depends on the definition of heat 
wave used (Xu et al. 2016). For this study, we define heat waves 
as three or more consecutive days on which the high temperature 
equals or exceeds the local 90th percentile for daily maximum 
temperature. This definition allowed us to apply a consistent 
global definition while accommodating variation in adaptation 
and acclimation to high temperatures. Xu et al. (2016) suggest 
the 90th percentile as a compromise between setting too high a 
threshold and missing some dangerous events and setting too low 
a threshold and flagging events that might not warrant alarm. We 
calculated percentiles from the 40-year period 1980–2019.
Because our method calculates hazard magnitudes by the year, 
for this hazard and other summertime hazards that are defined 
by runs of consecutive days meeting a particular condition, it is 
possible we inadvertently divided a single run into two runs at 
the boundary between two years. To reduce the chance that this 
occurs, for southern hemisphere cities, where summer spans the 
calendar-year boundary, we followed common practice and used 
the year July 1–June 30 to place the summer season within the 
modeled year (Wehrli et al. 2019; Graw et al. 2020). For northern 
hemisphere cities, we simply used the calendar year. However, 
this practice would not be effective in aseasonal environments.
ANNUAL LONGEST HEAT WAVE DURATION  
(heatwave_duration)
We calculated this hazard as the length in days of the longest 
heat wave in a year. We defined a heat wave as three or more 
consecutive days on which the high temperature equals or 
exceeds the local 90th percentile for daily maximum tempera-
ture. For northern hemisphere cities, we used the calendar year. 
For southern hemisphere cities, we used the year July 1–June 30.
ANNUAL HEAT WAVE COUNT (heatwave_count)
We calculated this hazard as the number of distinct heat waves 
in a year. We defined a heat wave as three or more consecutive 
days on which the high temperature equals or exceeds the local 
90th percentile for daily maximum temperature. For northern 
hemisphere cities, we used the calendar year. For southern 
hemisphere cities, we used the year July 1–June 30.

8  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
Annual number of days with average 
temperature optimal for malaria transmission 
(malaria_days) 
Prevalence of malaria depends importantly on the environ-
mental conditions for its transmission vector, mosquitoes of the 
genus Anopheles (Paaijmans et al. 2009; Blanford et al. 2013). 
Several studies (e.g., Mordecai et al. 2013; Lunde et al. 2016; 
Mordecai et al. 2016) have estimated either thermal tolerance 
ranges or optimal temperature ranges for Anopheles. For this 
hazard, we adopted the optimal transmission range used by 
Ryan et al. (2020): 22.9°C–27.8°C. We chose to use this study’s 
range because Ryan et al. used a conservative approach that 
yielded empirically plausible geographic ranges for Anopheles 
gambiae. Their approach was similar to ours in attempting to 
project malaria risk ranges based on climate models. Mosquito 
life cycles, however, depend on more than temperature. This haz-
ard definition is best interpreted as reflecting mosquito activity 
when there is no mitigation and other conditions exist in which 
mosquitoes thrive.
We calculated this hazard as the number of days in a calen-
dar year, possibly nonconsecutive, on which 22.9°C ≤ Tavg 
≤ 27.8°C, where Tavg is the daily mean air temperature at 
two-meter height.
Annual number of days with average 
temperature optimal for arbovirus transmission 
(arbovirus_days)
As with malaria transmission, transmission of arboviral diseases 
such as dengue, chikungunya, and Zika is strongly influenced 
by air temperature (Mordecai et al. 2017; Ciota and Keyel 2019; 
Wimberly et al. 2020). For this hazard, we use the optimal tem-
perature range for the vector mosquito Aedes aegypti and Aedes 
albopictus as reported in Mordecai et al. (2017): 26°C–29°C. 
Mordecai et al. base this range on theoretical and laboratory 
research grounds, and they find that predictions from the range 
align with epidemiological data.
We calculated this hazard as the number of days in a calendar 
year on which 26°C ≤ Tavg ≤ 29°C, where Tavg is the daily mean 
air temperature at two-meter height.
Heavy one-day precipitation
The risk that an extreme precipitation event overwhelms a city’s 
stormwater management system depends on the climate and on 
the stormwater system’s design parameters (Malik and James 
2007; Rosenberg et al. 2010). Precipitation events that exceed 
design capacity can cause flooding and sewage overflows. Design 
capacity varies from location to location and is generally based 
on locally determined extreme precipitation volumes.
Hazards defined by return periods of multiday heavy rain 
events are probably more directly relevant to the infrastructure 
impacts of extreme precipitation, but a hazard based on one-day 
precipitation is computationally less costly and therefore more 
practical for this global study. Also note that we only calculate 
precipitation within the pixel whose centroid is the closest to 
the city centroid, even though precipitation in nearby pixels can 
also impact flooding. We believe pr_highest and pr90octl_days 
to be useful for among-city comparisons, but single-location 
studies for engineering should consider hazards informed by 
detailed local hydrological models. We do not currently account 
for whether the precipitation is frozen or liquid, and cities that 
receive large volumes of snow might find this hazard to be less 
useful. Estimation of snow and ice volumes is a topic for future 
iterations of this research.
HIGHEST ANNUAL ONE-DAY PRECIPITATION (pr_highest)
We calculated this hazard as the highest one-day precipitation 
in a calendar year. We report these hazard magnitudes in mil-
limeters per day.
ANNUAL DAYS WITH ONE-DAY PRECIPITATION  
EQUAL TO OR EXCEEDING THE 90TH PERCENTILE 
(pr90pctl_days)
We calculated this hazard as the number of days in a calendar 
year during which one-day precipitation equals or exceeds the 
local 90th percentile of one-day precipitation. Percentiles were 
calculated from the 40-year period 1980–2019. The precipitation 
is frozen or liquid.
ANNUAL DAYS IN DROUGHT (drought_days)
Droughts have enormous impacts on a city’s public health 
(Stanke et al. 2013; Zhang et al 2019; Sugg et al. 2020) and 
economy (Desbureaux and Rodella 2019; Cremades et al. 2021). 
There is no universal definition of drought, and drought con-
cepts can incorporate climate, surface and subsurface hydrology, 
and the economics and politics of water management. For this 
hazard, we used the Standardized Precipitation Index (SPI; 
Svoboda et al. 2012), a widely accepted index adopted by the 
World Meteorological Organization for the monitoring of 
meteorological drought.
The SPI fits local, historical precipitation data to a gamma 
distribution probability model, which is then transformed into a 
Normal distribution. For the year of interest, precipitation data 
are mapped onto the Normal distribution, and the SPI reports 
deviations for each day from the historical mean in standard

TECHNICAL NOTE   |  August 2024  |  9
City-scale, city-relevant climate hazard indicators under 1.5°C, 2.0°C, and 3.0°C of global warming
deviations. Common SPI values range from −2.5 to 2.5, with 
negative values representing below-median precipitation. For 
this hazard, we counted drought days as those with SPI less than 
−1.5 (McKee et al. 1993, Lloyd-Hughes and Saunders 2002).
We calculated this hazard using the SPI function in the SPEI 
Python library (Vonk 2023). The hazard is the number of days 
in a year with SPI less than −1.5. For locations in the southern 
hemisphere, we used the year July 1–June 30.
For some cities, the SPI function was unable to converge on a 
usable reference probability distribution. The data set reports no 
data in these cases.
Annual days with high landslide risk 
(landsliderisk_days)
Landslides have enormous impacts on cities, both economically 
and in loss of life (Schuster and Highland 2007; Petley 2009; 
Mia et al. 2015; Klose et al. 2016). Landslide risk occurs in 
susceptible areas when there is risk of either earthquake or 
extended periods of heavy rain. Stanley and Kirschbaum (2017) 
mapped global landslide susceptibility based on the presence of 
roads, the absence of trees, proximity to a major tectonic fault, 
and steep slopes. Kirschbaum and Stanley (2018) combine this 
susceptibility map with an antecedent rainfall index (ARI), 
which is an indicator of prolonged, heavy rain. ARI for  
a particular day, d0, is calculated as
where t is the number of days before the day of interest, pt is 
precipitation on day d0 - t, and wt = (t + 1)-2.
The landslide susceptibility map is available from the Landslide 
Hazard Assessment for Situational Awareness project, ver-
sion 1.1.2 We used this map and intersected it with GHSL’s 
city boundaries to find which of our 996 cities include land 
with high susceptibility. For the 427 susceptible cities, we then 
calculated the landsliderisk_days hazard as the number of days 
in a calendar year on which ARI exceeds the local 95th per-
centile for ARI.
Calculation of average indicator values
For each hazard, we calculated two types of indicators for each 
location. The first indicator is the expected hazard value associ-
ated with the GMST of interest. For example, for the indicator 
drought_days, an average value of 8.5 indicates that our estimate 
of the average number of annual drought days at the GMST of 
interest is 8.5 days for a particular city. We report this estimate 
of the expected value as well as a standard deviation of that esti-
mate. (The accuracy of the estimate depends on the accuracy of 
the underlying model, and the uncertainty reflected in the stan-
dard deviation does not include uncertainty in model accuracy.)
The second indicator is the probability that the hazard value 
exceeds a particular threshold magnitude in any year during 
the 10-year window associated with the GMST of interest. For 
each hazard, we selected three hazard magnitudes to be used for 
all three GMSTs, for all locations. The thresholds were selected 
to serve as a basis for comparisons among GMSTs and among 
locations rather than for any operational significance. However, 
these methods could be applied to calculate the probability 
of exceedance for any locally important thresholds for these 
indicators, which may be valuable for engineering and risk 
management applications (Figueiredo et al. 2018). Table 3 lists 
the magnitude thresholds used for our threshold exceedance 
probability calculations.
Table 3  |   Hazard-value magnitudes used to calculate 
threshold exceedance probabilities
  THRESHOLD MAGNITUDES
Tmax_highest (°C) 35 40 45
Tmax95pctl_days (days) 60 70 80
Tmax40_days (days) 10 20 30
Tmax35_days (days) 10 20 30
CDD21 (degree-days) 2,000 3,000 4,000
Twb31_days (days) 10 25 30
heatwave_duration (days) 20 30 40
heatwave_count  
(heat waves) 1 3 5
malaria_days (days) 30 60 90
arbovirus_days (days) 30 60 90
pr_highest (mm) 500 1,000 2,000
pr90pctl_days (days) 20 30 40
drought_days (days) 100 140 180
landsliderisk_days (days) 5 10 20
Source: WRI Authors.

10  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
All indicator calculations involved several steps, applied sepa-
rately for each indicator, for each city location, for each of the 
three GMSTs of interest. The model grid cell used in the calcu-
lations was the cell that contains the city’s centroid. The methods 
for model selection and calibration and to calculate projected 
averages of hazard magnitudes and of threshold exceedance 
probabilities are detailed in Wong and Switzer (2023).
1. For each hazard, we selected the three models whose 
simulated historical values most closely match observed 
historical values based on RMSD between modeled and 
observed seasonal means. The meteorological variables 
used for these comparisons were those used to calculate 
hazard magnitudes. For example, our heat wave definition 
uses daily maximum temperature, so model selection was 
based on daily maximum temperature. For multivariable 
hazards, we based comparisons on the hazard magnitudes 
themselves. For historical observations, we used 1980–2014 
data from ERA5.
2. All models have their particular biases. We used historical 
data to reduce these biases. We used ERA5 data to generate 
a calibration function for each of the three selected models. 
Each calibration function was based on a percentile-
percentile plot (P-P plot) so that the marginal frequency 
distribution of the calibrated model data approximately 
matches the marginal frequency distribution of the 
corresponding ERA5 data. Each model had its own 
calibration function for each meteorological variable for each 
location. See Holmgren (1995) for a detailed treatment of 
P-P plots and their application to model calibration.
3. For each model, using the appropriate calibration function 
to shift the simulated data, we found for each GMST 
of interest the 10-year window centered on the GMST 
exceedance year in Table 2. From the model outputs in the 
window, we then constructed a histogram of annual hazard 
indicator values for the relevant 10-year future window 
(hereafter referred to as a frequency vector) of hazard values. 
The model outputs are from the model’s SSP2-4.5 run as 
stored in Google Earth Engine. For years before the SSP run 
begins, we used the model’s simulated historical data.
4. We used these frequency vectors to parameterize Bayesian 
probability models for the frequency of various hazard 
magnitudes that a city could expect under a particular 
warming scenario. We used these probability models to 
generate predictions of the average values of the hazard 
magnitudes for each scenario.3 The accompanying 
data set provides these estimated averages and the 
standard deviations.
5. To calculate threshold exceedance probabilities, we similarly 
generated probability models from the frequencies of 
threshold exceedance found in the simulations.4 These 
probability models generate predictive distributions of the 
exceedance probabilities. We report as estimated probability 
of threshold-exceedance the means of these distributions, 
along with the standard deviations of the distributions.
Unlike the standard deviations reported in Tables 6 and 7, the 
standard deviations reported in the data set and in Tables 4 and 
5 describe the uncertainty in the estimate of each indicator. They 
do not reflect among-city or interannual variability.
RESULTS
In this note we do not summarize the threshold exceedance 
probability indicators in the data set, but to illustrate how these 
data are structured we have extracted the exceedance probabili-
ties for the heatwave_count hazard for Kigali, Rwanda. Table 4 
shows the estimated probabilities that Kigali experiences at least 
one, three, or five heat waves in one year, for the recent historical 
reference period 1995–2014 and the three GMSTs. Estimates 
are provided for all three models selected for temperature 
hazards in Kigali: FGOALS-g3, INM-CM5-0, and CanESM5. 
As in the data set, the reported standard deviations describe 
uncertainty in our estimate, not interannual variability.
The data set reports indicator estimates from each of the 
three best (i.e., smallest historical RMSD with ERA5) mod-
els for each location-hazard combination. Table 5 shows an 
example from the data set: means and standard deviations of 
the estimates of the estimated number of heat waves in Kigali, 
calculated from all three models.

TECHNICAL NOTE   |  August 2024  |  11
City-scale, city-relevant climate hazard indicators under 1.5°C, 2.0°C, and 3.0°C of global warming
Table 4  |   Probabilities that annual heat waves number exceeds 1, 3, or 5 in Kigali, Rwanda
MODEL RANK RECENT HISTORICAL +1.5°C +2.0°C +3.0°C
1 heat wave 1 36.4 (5.1) 37.1 (5.1) 37.5 (5.2) 38.1 (5.2)
2 39.4 (23.0) 54.8 (29.3) 62.8 (30.6) 78.7 (40.1)
3 8.2 (21.4) 10.5 (24.4) 11.9 (26.0) 14.3 (29.8)
3 heat waves 1 31.9 (48.7) 37.3 (51.5) 37.3 (51.5) 47.8 (60.2)
2 1,101.9 (848.4) 1,242.9 (905.5) 1,305.9 (932.1) 1,436.6 (987.7)
3 0.2 (2.7) 0.3 (3.7) 0.3 (4.3) 0.5 (5.5)
5 heat waves 1 14.2 (21.1) 20.7 (29.7) 23.5 (29.4) 30.5 (35.7)
2 4.5 (1.4) 5.7 (1.8) 6.3 (2.0) 7.1 (2.9)
3 115.1 (98.6) 108.9 (90.0) 106.6 (86.5) 98.8 (77.9)
Note: Probabilities are mean estimates that the annual heat wave number equals or exceeds the threshold. Numbers in parentheses are standard deviations of the predictive 
distributions generated by the probability models. They therefore describe uncertainty of the estimates, rather than predicted interannual variation. Recent historical values are averages 
from the 1995–2014 reference period. Models are ranked 1, 2, and 3 based on lowest RMSD of quarterly mean maximum temperatures against ERA5 are FGOALS-g3, INM-CM5-0, and 
CanESM5, respectively..
Source: WRI Authors.
Table 5  |   Expected number of heat waves for each model for Kigali, Rwanda
MODEL RANK RECENT HISTORICAL +1.5°C +2.0°C +3.0°C
1 3.3 (1.0) 4.8 (1.4) 4.9 (1.5) 8.9 (2.3)
2 3.9 (1.1) 4.3 (0.8) 5.8 (1.0) 8.5 (1.2)
3 4.3 (1.4) 5.1 (1.2) 5.5 (1.1) 7.5 (1.4)
Note: Expected values are mean estimates of the expected value of  annual heat wave number. Numbers in parentheses are standard deviations of the predictive distributions generated 
by the probability models. They therefore describe uncertainty of the estimates, rather than predicted interannual variation. Recent historical values are averages from the 1995–2014 
reference period. Models ranked 1, 2, and 3 are FGOALS-g3, INM-CM5-0, and CanESM5, respectively.
Source: WRI Authors.

12  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
The standard deviation of the three estimates can describe the 
variation among the estimates from the three models, or the 
among-model variation. Table 6 shows the all-city average of 
this standard deviation. In general the average among-model 
variation increases with increasing GMST . The variation is nota-
bly large for the wetbulb-temperature hazard Twb31_days and 
the drought hazard droughtrisk_days. For these and all hazards, 
these standard deviations are useful in that they show substantial 
differences for some of the indicators among the three best 
models. The standard deviations are the greatest for most indica-
tors at +3 degrees C above the preindustrial baseline.
The analyses that follow are based only on the projections 
from the single best of the three selected for each hazard for 
each location. We remind and urge readers who are interested 
in understanding the uncertainty of our estimates to compare 
projections among all three models.
Table 7 shows the means of the city-specific estimates under 
each warming scenario, taken over all 996 cities. In general, 
the temperature-based indicators show consistent increases 
across all cities, but increases and decreases are mixed for the 
precipitation-based indicators. To calculate population-weighted 
values, we used the 2020 gridded population estimates from 
the GHSL GHS-POP data set (Schiavina et al. 2023), which 
we summed over the metropolitan area polygons in the GHSL 
Urban Centre Database (Florczyk et al. 2019). Table 8 lists 
the population-weighted values. Tables 7 and 8 also report 
standard deviations, which describe the among-city variation 
in the indicator values.5 The standard deviations reflect only the 
uncertainty in our indicator calculations, not the uncertainty in 
the population data.
Table 6  |   Population-weighted mean values of city-average climate hazard indicator values
RECENT HISTORICAL +1.5°C +2.0°C +3.0°C
Tmax_highest 0.50 0.54 0.53 0.60
Tmax95pctl_days 7.62 9.18 11.78 12.70
Tmax40_days 2.55 2.64 3.27 3.59
Tmax35_days 3.71 4.86 5.33 6.50
CDD21 40.09 51.78 52.36 56.19
Twb31_days 9.30 71.62 71.85 72.28
heatwave_duration 6.14 8.41 11.08 11.84
heatwave_count 0.77 0.88 1.00 1.12
malaria_days 7.63 8.86 9.20 10.04
arbovirus_days 7.82 9.06 10.12 10.83
pr_highest 6.57 7.03 7.12 7.07
pr90pctl_days 5.29 5.92 5.96 6.54
drought_days 15.98 17.33 17.34 18.87
landsliderisk_days 4.05 4.08 4.42 4.24
Notes: For each city, we calculated indicators using the three best NEX-GDDP-CMIP6 models based on minimizing RMSD with ERA5. Variation among the results from the three models 
can be characterized by a standard deviation. This table reports the average across all 996 cities of these standard deviations. The three best models differ from city to city. Larger 
values reflect greater among-model variation. Recent historical values are averages from the 1995–2014 reference period.
Source: WRI Authors.

TECHNICAL NOTE   |  August 2024  |  13
City-scale, city-relevant climate hazard indicators under 1.5°C, 2.0°C, and 3.0°C of global warming
Table 7  |   Unweighted all-city average climate hazard indicator values
RECENT HISTORICAL +1.5°C +2.0°C +3.0°C
Tmax_highest 36.4 (5.1) 36.6 (5.1) 36.9 (5.1) 37.6 (5.1)
Tmax95pctl_days 39.4 (23.0) 44.2 (25.8) 49.8 (26.9) 65.2 (32.4)
Tmax40_days 8.2 (21.4) 8.8 (22.4) 9.6 (23.3) 12.3 (26.4)
Tmax35_days 31.9 (48.7) 33.0 (49.3) 35.4 (51.1) 42.2 (55.2)
CDD21 1,101.9 (848.4) 1,045.1 (866.0) 1,116.0 (942.1) 1,340.0 (931.0)
Twb31_days 0. (2.7) 0.3 (3.5) 0.3 (4.0) 0.4 (5.1)
heatwave_duration 14.2 (21.1) 16.3 (23.6) 18.4 (26.9) 24.5 (31.9)
heatwave_count 4.5 (1.4) 4.9 (1.6) 5.4 (1.7) 6.4 (2.1)
malaria_days 115.1 (98.6) 114.0 (95.8) 110.4 (91.8) 104.4 (85.1)
arbovirus_days 71.2 (76.0) 74.7 (79.4) 76.9 (81.4) 80.7 (84.9)
pr_highest 40.7 (20.1) 41.7 (20.3) 42.7 (20.5) 43.7 (21.2)
pr90pctl_days 38.7 (12.9) 39.1 (13.4) 40.0 (13.1) 40.6 (13.9)
drought_days 112.4 (50.2) 113.9 (51.6) 114.9 (52.9) 113.6 (51.8)
landsliderisk_days 8.3 (12.0) 20.0 (10.4) 20.8 (10.4) 21.3 (10.9)
Notes: Reported averages are from each city’s best model, as assessed by RMSD against ERA5. Parameters for landsliderisk_days  calculated only for nonzero hazard magnitudes. 
Calculation of parameters for droughtrisk_days  excluded no-data instances. Numbers in parentheses are standard deviations, describing among-city variation. The standard deviations 
are calculated from the predictive distribution from which the mean estimate was calculated. Recent historical values are averages from the 1995–2014 reference period.
Source: WRI Authors.

14  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
Table 8  |   Population-weighted all-city average climate hazard indicator values
RECENT HISTORICAL +1.5°C +2.0°C +3.0°C
Tmax_highest 36.0 (4.7) 36.2 (4.7) 36.5 (4.7) 37.1 (4.7)
Tmax95pctl_days 38.2 (17.1) 42.6 (19.2) 48.5 (20.0) 63.8 (26.3)
Tmax40_days 6.4 (19.2) 6.8 (20.1) 7.4 (20.6) 9.2 (23.3)
Tmax35_days 25.9 (44.0) 27.2 (44.9) 29.8 (47.2) 35.7 (51.1)
CDD21 1,102.4 (833.5) 1,153.2 (854.1) 1,205.1 (879.5) 1,327.7 (927.7)
Twb31_days 0.1 (2.2) 0.2 (3.2) 0.3 (3.7) 0.4 (4.7)
heatwave_duration 13.3 (15.6) 14.8 (17.2) 16.8 (19.3) 22.6 (23.6)
heatwave_count 4.5 (1.4) 5.0 (1.6) 5.5 (1.6) 6.5 (2.1)
malaria_days 119.7 (99.9) 118.1 (96.1) 113.6 (91.1) 105.4 (82.3)
arbovirus_days 77.9 (81.2) 80.6 (82.7) 83.7 (87.4) 86.9 (91.1)
pr_highest 43.7 (23.3) 45.0 (23.8) 45.4 (22.5) 45.7 (22.8)
pr90pctl_days 39.3 (15.5) 40.0 (15.8) 41.2 (16.90 41.9 (17.0)
drought_days 107.7 (48.8) 108.9 (51.0) 108.1 (52.2) 109.0 (50.9)
landsliderisk_days 11.4 (15.5) 21.3 (14.5) 21.9 (14.7) 22.7 (14.9)
Notes: Reported averages are from each city’s best model, as assessed by RMSD against ERA5. Parameters for landsliderisk_days calculated only for nonzero hazard magnitudes. 
Calculation of parameters for droughtrisk_days  excluded no-data instances. Standard deviations (in parentheses) are calculated with population as frequency weights. Standard 
deviations reflect only uncertainty in the climate-hazard predictions, not uncertainty in population estimates. The standard deviations are calculated from the predictive distribution 
from which the mean estimate was calculated. Metropolitan area populations are 2020 estimates from GHS-POP. Recent historical values are averaged over 1995–2014.
Source: WRI Authors.
Some global trends stand out:
 ▪ Heat wave duration increases dramatically from +1.5°C to 
+3.0°C. The unweighted all-city average is 14.2 days for 
1995–2014; it increases to 16.3 days at +1.5°C  and 24.5 days 
at +3.0°C. Weighted by 2015 metropolitan area population, 
the all-city means for heatwave_duration at the recent 
historical reference period, +1.5°C, and +3.0°C are 13.3, 14.8, 
and 22.6 days, respectively. This means that for the average 
dweller of our 996 cities, the difference from +1.5°C to 
+3.0°C brings a 53 percent increase in heat wave duration.
 ▪ Heat wave frequency (as captured by heatwave_count) also 
increases, growing from a population-weighted average 
of 4.5 heat waves per year recently to 5.0 and 6.5 per 
year, respectively, under +1.5°C and +3.0°C (see Figure 4). 
Notably, the contrast is starker for cities in low-income 
countries. The shift from +1.5°C to +3.0°C brings a 29 
percent increase in unweighted heat wave frequency for 
all 996 cities, but it lowers to a 14 percent increase when 
considering only cities in high-income countries. Cities 
in low-income countries, in contrast, will see a 45 percent 
increase in heat wave frequency. Income categories are 2023 
categories from the World Bank (n.d.) and are based on 
gross national income.

TECHNICAL NOTE   |  August 2024  |  15
City-scale, city-relevant climate hazard indicators under 1.5°C, 2.0°C, and 3.0°C of global warming
There are some regional differences in the direction of change 
from +1.5°C to +3.0°C:
 ▪ Using the World Bank’s (n.d.) 2023 country-level regional 
classifications, we find that North America and the Europe–
Central Asia region see a modest increase in malaria_days, 
but other locations see a decrease (Figure 4, panel a). Average 
arbovirus_days, in contrast, increase in all regions except the 
Middle East, East Asia and the Pacific, and South Asia. 
Across all 996 cities, the average malaria_days decrease by 
9.6 days whereas average arbovirus_days increase by 6.0 days 
(Figure 4, panel b). By the optimal temperature ranges used 
in our hazard calculations, arbovirus-carrying mosquitoes 
thrive at higher temperatures than malaria-carrying 
mosquitoes. A shift to higher temperatures thus favors 
arboviral over malarial transmission.
 ▪ A shift from +1.5°C to +3.0°C brings little change in 
drought days globally (Figure 5). Cities in all regions see 
increases or small decreases, except North America, whose 
average value of drought_days decreases by 8.7 days. The 
Middle East–North Africa region sees a striking increase of 
12.1 drought days.
Figure 3  |   Change in heat wave frequency between the +1.5°C and +3.0°C warming scenarios
Note: Heat waves become more frequent overall, but the predicted increase is less dramatic for high-income cities and more dramatic for the lowest-income cities.
Source: WRI authors.
1.5
0.7
1.8
2.1
0.0
0.5
1.0
1.5
2.0
2.5
All income classesH igh income Upper-middle income Lower-middle income Low income
Change in days
1.4

16  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
Figure 4  |   Estimated number of days on which average temperature is optimal for disease transmission 
Notes: Panel a shows the malaria-carrying mosquito Anopheles gambia , and panel b shows the arbovirus-carrying mosquito Aedes aegypti. Days are given for 1.5°C and 3.0°C above the 
historical baseline.
Source: WRI authors.
B: High-Risk Arbovirus Days
+1.5C+ 3.0C
75
81 All regions
29
35 North America
78
91 Latin America and Caribbean
104
129 Sub-Saharan Africa
46 46 Middle East and North Africa
12 15 Europe and Central Asia
100 98 South Asia
89
96 East Asia and Pacific
A: High-Risk Malaria Days
+1.5C+ 3.0C
114
104 All regions
65 65 North America
149 144 Latin America and Caribbean
196
184 Sub-Saharan Africa
79
70 Middle East and North Africa
31 34 Europe and Central Asia
122
108 South Asia
121
105 East Asia and Pacific
Figure 5  |   Change in number of drought days from +1.5°C to +3.0°C of warming
Note: Average drought days changes modestly when averaged across all regions, with a large increase in the Middle East–North Africa region and a large decrease in North America.
Source: WRI authors.
Change in drought days
East Asia 
and Pacific
South AsiaEurope and 
Central Asia
Middle East 
and North Africa
Sub-Saharan 
Africa
Latin America 
and Caribbean
North AmericaAll regions
–8.7
3.9 4.6
1.2 –1.2 –3.2
12.1
–0.3
15
10
5
0
-5
-10

TECHNICAL NOTE   |  August 2024  |  17
City-scale, city-relevant climate hazard indicators under 1.5°C, 2.0°C, and 3.0°C of global warming
Using the 2020 population estimates (Schiavina et al. 2023), 
we estimated the number of people exposed to various hazards. 
Some prominent findings follow:
 ▪ Across all 996 cities, at +1.5°C, 547 million people are 
exposed to 30 or more days with temperatures at or 
exceeding 35°C. As warming reaches +3.0°C, the number 
exposed to these temperatures is expected to grow 
to 701 million.
 ▪ Demand for cooling (as captured by CDD21) doubles from 
the recent historical period 1995–2014 to +1.5°C for 8.7 
million people. From the same reference period to +3.0°C, 
194 million people have a doubled demand for cooling.
DISCUSSION
The literature associating climate impacts to particular GMST 
values is vast (e.g., IPCC 2018), but to date there has been little 
climate-projection work specifically targeting decision-makers 
in cities. This study fills this gap in two ways: it projects cli-
mate hazard magnitudes at a spatial scale appropriate to much 
city-level decision-making, and it focuses on hazard indicators 
chosen for relevance to cities.
Our findings are largely unsurprising. Increasing frequency and 
duration of heatwaves have been observed and predicted by oth-
ers (Perkins-Kirkpatrick and Gibson 2017, Perkins-Kirkpatrick 
and Lewis 2020, Qiu and Yan 2020), and Scoccimarro et al. 
(2023) predicts increasing cooling demand as captured by cool-
ing degree-days. Ryan et al. (2015) predict a contraction of the 
geographic range of malaria-carrying mosquitos in Africa as the 
climate warms beyond their physiological tolerance. Mordecai et 
al. (2020) predict a similar decline in malaria-carrying mosqui-
tos and a surge in arbovirus-carrying mosquitos. Global and 
regional drought projections vary widely, as drought definitions 
and models vary widely (Xu et al. 2019, Wang et al. 2021). Stud-
ies that, like ours, focused on meteorological drought, and not 
drought driven by other hydrological processes, have found little 
evidence for strong directional trends on a global scale, though 
they acknowledge that drought models that consider evapo-
transpiration suggest increasing dryness (Asadi Zarch 2022, 
Vicente-Serrano et al. 2022).
The data we present are suitable to be used for adaptation plan-
ning, disaster mitigation, and risk management in cities. We 
also hope that our work illuminates the particular challenges 
global warming poses to cities and the need for investment 
in high-resolution climate models. We also expect that these 
data can support local activists and subnational political lead-
ers in their work to limit global warming. Additionally, the 
underlying methods are appropriate for developing many 
more city- and sector-relevant indicators. We hope that these 
indicators generate ideas and requests from urban decision-
makers for additional indicators to more precisely meet local 
planning needs.
Limitations
As with all modeling, this study has important limitations. 
Many of our methodological choices result in simplifications, 
but, where possible, we made these choices with the intention 
of keeping our methods conservative—overestimating rather 
than underestimating uncertainty and underestimating rather 
than overestimating hazard severity. We note here some impor-
tant limitations: 
 ▪ Our projections include uncertainty. No attempt to project 
future trends can eliminate uncertainty. Sources of 
uncertainty include limitations in the current understanding 
of earth system processes, uncertainty in future land use 
and greenhouse gas emissions, uncertainty in our ability to 
simulate climate computationally, and the stochastic nature 
of the weather (Kemp et al. 2022). Some uncertainty can 
be addressed (but not reduced) by the use of more than one 
climate model. In this project we used nine models, and 
we present results from three models for each indicator, 
for each city, in the data set. We urge readers to consult the 
data from all three models to have a sense of the magnitude 
of the uncertainty (see below, “Interpreting the data”), but 
note that even if the models agree perfectly some underlying 
uncertainty remains.
 ▪ Our models do not consider urban heat islands or other urban 
climate effects. The effects of pavement, buildings, and 
vehicular traffic are not accounted for in global climate 
models like those included in NEX-GDDP-CMIP6. 
Particularly in the case of the urban heat island effect, we 
expect our methods to underestimate the magnitudes of 
heat-related hazards. (See Phelan et al. [2015] and Deilami 
et al. [2018] for reviews on urban heat islands.)
 ▪ We do not consider urbanization or other demographic processes. 
Cities grow in population and spatial extent over time, 
but we do not account for these changes in this project. 
Population changes would likely affect the population-
weighted indicators we report in this paper. Spatial-extent 
changes might occasionally affect which model grid cell 
is used for indicator calculation, but we do not think the 
differences are likely to be large. Increasing urbanization 
and population growth would also likely increase urban heat 
island effects.

18  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
 ▪ Spatial resolution of 0.25 degrees is not sufficiently fine for 
intra-city work. Neighborhoods within a city can vary 
enormously in climate. Numerous factors—building height, 
vegetation, local topography, proximity to large bodies of 
water—can influence temperature and precipitation in ways 
that contribute to within-city differences in hazard exposure 
and quality of life. In the case of our malaria and arbovirus 
transmission hazards, the spatial resolution of our data can 
obscure vector hotspots. Our data does not capture variation 
at the neighborhood scale and is therefore not useful in 
understanding neighborhood-level differences in climate 
adaptation priorities.
 ▪ We probably underestimate variation, especially in precipitation. 
Spatially coarse data has the effect of averaging away any 
variation that exists at finer scales (O’Neill et al. 1986). 
One consequence of this is that our calculations probably 
underestimate variation and fail to capture peaks and troughs 
at fine geographic scales both in the hazard magnitudes and 
in the hazard indicators.
 ▪ Our exposure estimates are based on recent populations, not 
population projections. We use GHSL’s 2020 population 
estimates and GHSL’s 2015 estimates of the spatial extents 
of urban areas. A more robust approach would base exposure 
estimates on projections both of population and of urban 
extents, even as it introduces additional uncertainty through 
inclusion of another projected variable. The result is that 
future population exposure is underestimated. 
Some of these limitations would be mitigated with climate 
model outputs at finer spatial resolution. For this global study, 
we used global models and were limited by the resolution of 
available models. Nothing would preclude a researcher from 
applying the indicator calculation methods in Wong and 
Switzer (2023) to outputs from a local climate model with 
finer resolution.
However, even with limited data availability, we see that a world 
3.0°C warmer than the preindustrial baseline is likely to be far 
worse for far more city dwellers than a world that is only 1.5°C 
warmer. This is particularly true for heat-related hazards—heat 
waves become longer and more common, more energy is 
required to maintain safe and comfortable conditions indoors, 
and there is greater risk of infrastructure-endangering tempera-
tures. Also, these hazards are not uniformly distributed. Cities 
in the Global South face disproportionately greater increases in 
arbovirus risk, and cities in low-income countries are predicted 
to experience more frequent heat waves. In this paper, we 
have limited our effort on analysis of socioeconomic dispari-
ties in climate hazard exposure and vulnerability. However, the 
accompanying data set should serve as a sound basis for further 
work in this area.
Interpreting the data
We expect the indicators in our data set to be useful in a variety 
of applications, and we acknowledge that some users might be 
unfamiliar with this sort of data. We offer the following advice 
on interpreting our, and all, model results.
 ▪ Acknowledge uncertainty. The data set includes two ways to 
assess some (but not all: see above, “Limitations”) of the 
uncertainty inherent in our estimates of the indicator values. 
Each estimate is the mean of the predicted indicator values 
from a single model. The accompanying standard deviation 
describes the variation in that model’s predictions. Large 
standard deviations indicate greater within-model uncertainty. 
This is true for both types of indicator—expected value and 
threshold-exceedance probability. We also provide estimates 
(and accompanying standard deviations) from three 
independent climate models. Comparing the three indicator 
values provides a sense of the uncertainty that arises from 
differences in modeling methods—among-model uncertainty. 
Greater disagreement among the three models’ projections 
indicates greater uncertainty.
 ▪ Remain mindful of the spatial scale of the indicators. Our input 
data, and therefore our indicator estimates, are spatially 
averaged over grid cells that are 0.25 degrees by 0.25 degrees 
in size. Near the equator, 0.25 degrees is equivalent to 
approximately 28 kilometers, so a single grid cell is larger 
than many cities. This means that for many locations, 
the averages include both urban climates and climates in 
outlying areas. One consequence of the averaging is that 
temperatures experienced in the centers of cities are likely to 
be higher than the average over its grid cell if that cell also 
includes rural areas.
 ▪ Avoid combining indicators numerically. We calculate every 
indicator independently of the others, and we are aware of 
no mathematical justification for combining two indicators 
that have been calculated for different hazards or from 
different models. For this reason we discourage combining 
indicators for different hazards. For example, it would not be 
appropriate to multiply heat wave duration and heat wave 
frequency to  estimate the annual number of days spent in 
heat waves. Number of days spent in heat waves would define 
a new hazard, and the methods in Wong and Switzer (2023) 
could be applied to estimate its future average magnitudes 
and probabilities of threshold exceedance. We also discourage

TECHNICAL NOTE   |  August 2024  |  19
City-scale, city-relevant climate hazard indicators under 1.5°C, 2.0°C, and 3.0°C of global warming
reporting across-model indicator means. If a single indicator 
value is desired, we recommend reporting either the median 
of the three values or the value from the top-ranked model. 
The latter has the advantage that any one city’s indicators for 
different GMSTs will be from the same model.
 ▪ Avoid sorting or ranking the data by indicator value. Users of 
multi-city data occasionally want to sort the data in order 
to find the cities with the most extreme indicator values—
for example, the cities with the highest projected annual 
temperatures. We discourage this. Every indicator estimate 
can be thought of as the sum of a true value (whose value 
we do not know) and some modeling error. If two cities had 
the same true number of peak malaria-transmission days 
at a particular GMST , their malaria_days indicator values 
would almost certainly be different in our data set because 
of chance error. When data are sorted or ranked by indicator 
values, values that are high or low because of chance error 
can be overrepresented in the high or low ranks. The result 
is that lists of the hottest or driest cities are likely to include 
cities that, but for chance, would not make the list.
 ▪ Focus on aggregates. We discourage grouping cities by 
indicator-value rank, but we encourage other ways of 
grouping cities. It might be fruitful to compare average 
indicator values among cities grouped by size, wealth level, 
geographic region, progress toward climate goals, or any 
other attribute that is not derived from our data.
 ▪ Avoid overstating impact. Our intention is to address issues 
that are salient to the lives and livelihoods of cities, but in 
this project we have been limited to climatic variables that 
are straightforward to model. This approach necessarily 
leaves unaddressed relevant, important factors. For example, 
our treatment of infectious-disease transmission focuses only 
on optimal temperatures for the adult mosquitos that carry 
disease. It does not address climatic factors that affect other 
parts of the pathogen, vector, or host life cycles. It does not 
account for whether the pathogens or mosquitos are present 
to begin with. And it does not address mitigation actions 
like vaccination and vector control. Similarly, our treatment 
of drought addresses only rainfall and does not account 
for important drought factors like groundwater dynamics, 
evapotranspiration, and water use.
 ▪ Question counterintuitive values. Some indicators for some 
cities will inevitably be surprising. For example, some 
historically cool cities will be characterized as surprisingly 
hot, or an indicator calculated for +2.0°C is lower in value 
than both the +1.5°C and 3.0°C values. Without an in-depth 
study using local data or high-resolution local modeling, it 
is impossible to know how much of the gap between data 
and intuition to attribute to a surprising but correct future 
and how much to attribute to systematic or chance error. It 
is useful to remember that these data are not the totality of 
the information we bring to bear; we have knowledge about 
local context and conditions, as well as prior knowledge of 
the city’s historical climate trends. Our data do not replace 
existing knowledge, but should rather be evaluated in light of 
it and—with appropriate caveats—be added to it.
DATA AVAILABILITY
All indicator values, along with summary tables, are available in 
the provided data set.6 The spreadsheet containing the indicator 
values includes mean estimates for each indicator for each of 
the GMSTs of interest: +1.5°C, +2.0°C, and +3.0°C. They also 
report recent historical reference period averages, calculated 
from modeled data for the 20-year period 1995–2014. We also 
report for each mean estimate the standard deviation of the 
predictive distribution from which the mean estimate was taken. 
These are the mean and standard deviation of the predictive 
distribution of the indicator as generated by a Bayesian prob-
ability model. The standard deviation should not be interpreted 
as reflecting variability of the hazard magnitude but rather 
an indicator of some of the uncertainty in our estimate of the 
mean hazard magnitude. Mean estimates of the indicators, and 
standard deviations, are provided for the three best models for 
each city as assessed by RMSD against ERA5.
The spreadsheet columns and their values are as follows:
loc_id An integer unique to each city
city City name
country Country name
latitude Latitude in decimal degrees north
longitude Longitude in decimal degrees east
hazard  Hazard short-names. Listed in the section 
“Hazards” and in Table 3.
scenario  Warming scenarios. Can be recent_historical 
(i.e., 1995–2014), 1.5C, 2.0C, or 3.0C.
model  The NEX-GDDP-CMIP6 model used 
for calculating the indicator. Models are 
listed in Table 1.
model_rank  The rank of the model. Can be 1, 2, or 
3, where the model with rank 1 has the 
strongest association between its historical 
predictions and ERA5 data.

20  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
indicator  Can be exceedanceprob (for probability 
of exceeding the threshold) or expect-
edvalue (for the expected value of the 
indicator magnitude).
threshold  Hazard magnitudes chosen as extreme values, 
listed in Table 3
mean_estimate  The mean of the predictive distribution of 
indicator values as generated by a Bayesian 
probability model. This value can be inter-
preted as an estimate of the indicator value.
stdev_estimate  The standard deviation of the predictive 
distribution of indicator values as generated 
by a Bayesian probability model. This value 
reflects the uncertainty in the estimate of the 
indicator value.
APPENDIX. SUITABILITY OF 
NEX-GDDP-CMIP6 FOR URBAN 
APPLICATIONS.
The CMIP6 models generally do not model urban climate processes. 
In the absence either of urban-specific climate modeling (e.g., 
Zhao et al. 2021) or bias correction using empirical city-level data, 
a CMIP6 model will fail to account for the climate impacts of cities 
(e.g., heat island effect). The NEX-GDDP-CMIP6 downscaled dataset 
was calculated using a bias-correction process using the Global 
Meteorological Forcing Dataset (GMFD) for Land Surface Modeling 
(Sheffield et al. 2006). We apply a second bias correction to NEX-
GDDP-CMIP6 model outputs (see Wong and Switzer [2023] for 
methodological details) using the European Centre for Medium-
Range Weather Forecasts Reanalysis version 5 (ERA5; ECMWF 2022). 
GMFD and ERA5 are reanalysis datasets: they begin with empirical 
data and use modeling for bias correction and to fill data gaps. 
We note that because GMFD and ERA5 include empirical climate 
observations, urban climates are reflected in the bias-corrected NEX-
GDDP-CMIP6 model outputs for urban locations used in this study, 
even if the underlying CMIP6 models do not explicitly model cities.
The scatterplots in Figure A1 illustrate the relationships among 
the monthly means of daily maximum temperature data from four 
datasets for the years 2006–2024. The four datasets are the NEX-
GDDP-CMIP6 downscaled data from the CanESM climate model, 
the same CanESM data modified with an urban climate model by 
Zhao and colleagues (2021), ERA5, and weather-station data from 
the Global Historical Climatology Network (GHCN; Lawrimore et al. 
2011). The Zhao et al. dataset is the only publicly available dataset 
that applies urban climate modeling to global climate models. Each 
scatterplot includes 227,088 points: 12 monthly means × 19 years × 
996 cities. The data are the values in the respective datasets at the 
grid cell or weather station geographically nearest  
to the city centroid.
Table A1 reports the root mean squared difference (RMSD) between 
the two model datasets (NEX-GDDP-CMIP6 and the Zhao et al. data) 
and the two empirical datasets (ERA5 and GHCN). The association 
between the NEX-GDDP-CMIP6 outputs and the ERA5 data is 
remarkably strong, as can be seen in the small RMSD value (2.27) and 
the narrow point cloud in the nex-ERA5 scatterplot in Figure 2. The 
Zhao et al. data outperform NEX-GDDP-CMIP6 in their association 
with the GHCN weather-station data, but the difference as quantified 
by RMSD is small.
The strong association between the NEX-GDDP-CMIP6 CESM 
temperature data and ERA5 temperature data suggests that NEX-
GDDP-CMIP6 is suitable for predicting climate at a spatial resolution 
similar to the ERA5 resolution (31 km). The weaker association with 
the GHCN weather-station data suggests that NEX-GDDP-CMIP6 is 
less suitable for predicting climate at point locations. This contrast 
underscores an important caveat about our research: the indicator 
values we report are spatial averages over grid cells that are 0.25 
degrees by 0.25 degrees in extent. They should not be interpreted  
as estimates for cities as point locations.

TECHNICAL NOTE   |  August 2024  |  21
City-scale, city-relevant climate hazard indicators under 1.5°C, 2.0°C, and 3.0°C of global warming
Figure A1  |   Dataset comparisons for monthly means of daily maximum temperature, 2006–2024 
Notes: The datasets compared are the CanESM model outputs in NEX-GDDP-CMIP6 (“nex”), the CanESM model outputs as modified with urban climate modeling by Zhao et al. (“zhao”), 
the ERA5 reanalysis dataset, and weather station data from the Global Historical Climatology Network (“ghcn”). The points represent monthly mean of daily maximum temperature, 
2006–2024, in the 996 study cities. The unit for all axes is degrees Celsius.
Source: WRI authors.
-20         0    10         30
-30      -10       10       30
-30      -10       10       30
-60         -20     0     20   40
-60         -20     0     20   40
-60         -20     0     20   40 -20        0         20        40
-20         0    10         30
-20         0    10         30 -20        0         20        40
nex
zhao
era5
ghcn
Table A1  |   Root-mean-squared differences between 
modeled and empirical temperature data
ERAS GHCN
NEX-GDDP-CMIP6 2.27 15.73
Zhao et al. 13.68 14.94
Notes: The datasets compared are the CESM model outputs in NEX-GDDP-CMIP6, the 
CESM model outputs as modified with urban climate modeling by Zhao et al., the ERA5 
reanalysis dataset, and weather station data from the Global Historical Climatology 
Network. Compared data are monthly means of daily maximum temperature, 2006–
2024, in the 996 study cities.
Source: WRI Authors.

22  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
REFERENCES
Anderson, G.B., and M.L. Bell. 2011. “Heat Waves in the United States: 
Mortality Risk during Heat Waves and Effect Modification by Heat 
Wave Characteristics in 43 US Communities.” Environmental Health 
Perspectives 119 (2): 210–18. https://doi.org/10.1289/ehp.1002313.
Andrade, C., S. Mourato, and J. Ramos. 2021. “Heating and Cooling 
Degree-Days Climate Change Projections for Portugal.” Atmosphere  
12 (6): 715. https://doi.org/10.3390/atmos12060715.
Arnell, N.W., J.A. Lowe, B. Lloyd-Hughes, and T.J. Osborn. 2018.  
“The Impacts Avoided with a 1.5°C Climate Target: A Global and Re -
gional Assessment.” Climatic Change 147 (March): 61–76. https://doi.
org/10.1007/s10584-017-2115-9.
Asadi Zarch, M.A. 2022. “Past and Future Global Drought Assess -
ment.” Water Resources Management  36 (13): 5259–76.
Auffhammer, M., and E.T. Mansur. 2014. “Measuring Climatic Impacts 
on Energy Consumption: A Review of the Empirical Literature.” 
Energy Economics 46 (November): 522–30. https://doi.org/10.1016/j.
eneco.2014.04.017.
Begum, A., R. Lempert, E. Ali, T.A. Benjaminsen, T. Bernauer, W. 
Cramer, X.   Cui, K. Mach, G. Nagy, N.C. Stenseth, R. Sukumar, and 
P. Wester. 2022. “Point of Departure and Key Concepts.” In Climate 
Change 2022: Impacts, Adaptation, and Vulnerability . Contribu-
tion of Working Group II to the Sixth Assessment Report of the 
Intergovernmental Panel on Climate Change H.-O. Pörtner, D.C. 
Roberts, M. Tignor, E.S. Poloczanska, K. Mintenbeck, A. Alegría, M. 
Craig, S. Langsdorf, S. Löschke, V. Möller, A. Okem, B. Rama (eds.). 
New York and Cambridge: Cambridge University Press, 121–96, 
doi:10.1017/9781009325844.003.
Blanford, J.I., S. Blanford, R.G. Crane, M.E. Mann, K.P. Paaijmans, K.V. 
Schreiber, and M.B. Thomas. 2013. “Implications of Temperature 
Variation for Malaria Parasite Development across Africa.” Scientific 
Reports 3 (1300). https://doi.org/10.1038/srep01300.
Burillo, D., M.V. Chester, S. Pincetl, and E. Fournier. 2019. “Electricity 
Infrastructure Vulnerabilities due to Long-Term Growth and Extreme 
Heat from Climate Change in Los Angeles County.” Energy Policy  128 
(May): 943–53. https://doi.org/10.1016/j.enpol.2018.12.053.
Ciota, A.T., and A.C. Keyel. 2019. “The Role of Temperature in Trans -
mission of Zoonotic Arboviruses.” Viruses  11 (11): 1013. https://doi.
org/10.3390/v11111013.
ENDNOTES
1. The data set can be downloaded at https://datasets.wri.org/data -
set/city-scale-climate-hazard-indicators-warming-scenarios.
2. The landslide susceptibility map can be downloaded at https://
gpm.nasa.gov/landslides/projects.html.
3. Specifically, we used a noninformative Bayes Dirichlet prior 
distribution for the histogram of annual climate hazard indicators 
and conditioned them on the specific frequency vectors. For each 
model, hazard, and GMST, this yielded a posterior multinomial dis -
tribution that characterizes the uncertainty in the histogram of the 
future indicator values for this period. Samples from this posterior 
multinomial distribution were used to generate the predictive dis -
tribution for the average annual hazard indicator. The means and 
standard deviations of these predictive distributions are shown as 
rows in the accompanying data set.
4. For predicted probabilities of threshold exceedance, a Bayes 
framework was applied to frequencies of threshold exceedance 
counts in the hazard-value frequency distribution. In the case of 
the heat wave hazards, samples from a gamma prior were used 
to parameterize posterior Poisson distributions. For the other 
hazards, samples from a beta prior were used to parameter -
ize posterior binomial distributions. Samples from the posterior 
distributions are predictive distributions of the future counts of 
exceedance events.
5. The means in Tables 8 and 9 are population parameters, rather 
than sample statistics. The standard deviations should therefore 
be interpreted only as a measure of among-city variability, and 
not as an indicator of significant differences from null values.
6. See endnote 1.

TECHNICAL NOTE   |  August 2024  |  23
City-scale, city-relevant climate hazard indicators under 1.5°C, 2.0°C, and 3.0°C of global warming
Cremades, R., A. Sanchez-Plaza, R.J. Hewitt, H. Mitter, J.A. Baggio, 
M. Olazabal, A. Broekman, B. Kropf, and N.C. Tudose. 2021. “Guiding 
Cities under Increased Droughts: The Limits to Sustainable Urban 
Futures.” Ecological Economics  189: 107140. https://doi.org/10.1016/j.
ecolecon.2021.107140.
Deilami, K., M. Kamruzzaman, and Y. Liu. 2018. “Urban Heat Island 
Effect: A Systematic Review of Spatio-temporal Factors, Data, 
Methods, and Mitigation Measures.” International Journal of Applied 
Earth Observation and Geoinformation  67 (May): 30–42. https://doi.
org/10.1016/j.jag.2017.12.009.
De Rosa, M., V. Bianco, F. Scarpa, and L.A. Tagliafico. 2015. “Historical  
Trends and Current State of Heating and Cooling Degree-Days in 
Italy.” Energy Conversion and Management  90 (January): 323–35. 
https://doi.org/10.1016/j.enconman.2014.11.022.
Desbureaux, S., and A.-S. Rodella. 2019. “Drought in the City: The 
Economic Impact of Water Scarcity in Latin American Metropoli -
tan Areas.” World Development 114 (February): 13–27. https://doi.
org/10.1016/j.worlddev.2018.09.026.
Dosio, A., L. Mentaschi, E.M. Fischer, and K. Wyser. 2018.  
“Extreme Heat Waves under 1.5°C and 2°C Global Warming.” 
Environmental Research Letters  13 (April): 054006. https://doi.
org/10.1088/1748-9326/aab827.
ECMWF (European Centre for Medium-Range Weather Forecasts). 
2022. “ERA5: Data Documentation.” July 14. https://confluence.ecmwf.
int/display/CKB/ERA5%3A+data+documentation.
Faurie, C., B.M. Varghese, J. Liu, and P. Bi. 2022. “Association between 
High Temperature and Heatwaves with Heat-Related Illnesses:  
A Systematic Review and Meta-analysis.” Science of the Total Environ-  
ment 852 (December): 158332. https://doi.org/10.1016/j.scito -
tenv.2022.158332.
Figueiredo, R., M.L. Martina, D.B. Stephenson, and B.D. Young -
man. 2018. “A Probabilistic Paradigm for the Parametric Insurance 
of Natural Hazards.” Risk Analysis 38 (11): 2400–14. https://doi.
org/10.1111/risa.13122.
Florczyk, A., C. Corbane, M. Schiavina, M. Pesaresi, L. Maffenini,  
M. Melchiorri, P. Politis, et al. 2019. “GHS-UCDB R2019A: GHS Urban 
Centre Database 2015, Multitemporal and Multidimensional Attri -
butes.” European Commission, Joint Research Centre. https://data.jrc.
ec.europa.eu/dataset/53473144-b88c-44bc-b4a3-4583ed1f547e.
Gorelick, N., M. Hancher, M. Dixon, S. Ilyushchenko, D. Thau, and  
R. Moore. 2017. “Google Earth Engine: Planetary-Scale Geospatial 
Analysis for Everyone.” Remote Sensing of Environment  202 (Decem -
ber): 18–27. https://doi.org/10.1016/j.rse.2017.06.031.
Graw, V., G. Ghazaryan, J. Schreier, J. Gonzalez, A. Abdel-Hamid,  
Y. Walz, K. Dall, J. Post, A. Jordaan, and O. Dubovyk. 2020. “Timing Is 
Everything—Drought Classification for Risk Assessment.” IEEE Journal 
of Selected Topics in Applied Earth Observations and Remote Sensing  
13: 428–33. https://doi.org/10.1109/JSTARS.2019.2963576.
Green, H., J. Bailey, L. Schwarz, J. Vanos, K. Ebi, and T. Benmarhnia. 
2019. “Impact of Heat on Mortality and Morbidity in Low and Middle 
Income Countries: A Review of the Epidemiological Evidence and 
Considerations for Future Research.” Environmental Research  171 
(April): 80–91. https://doi.org/10.1016/j.envres.2019.01.010.
Holmgren, E.B. 1995. “The P-P Plot as a Method for Comparing Treat -
ment Effects.” Journal of the American Statistical Association 90 (429) 
360–65. https://doi.org/10.1080/01621459.1995.10476520.
IEC (International Electrotechnical Commission). 2018. “IEC 60076-
7:2018: Power Transformers—Part 7: Loading Guide for Mineral-
Oil-Immersed Power Transformers.” https://webstore.iec.ch/
publication/34351.
IEEE (Institute of Electrical and Electronics Engineers). 2012. “IEEE 
C57.91-2011: IEEE Guide for Loading Mineral-Oil-Immersed Trans -
formers and Step-Voltage Regulators.” https://standards.ieee.org/
ieee/C57.91/5297/.
IPCC (Intergovernmental Panel on Climate Change). 2018. Global 
Warming of 1.5°C. An IPCC Special Report on the Impacts of Global 
Warming of 1.5°C above Pre-industrial Levels and Related Global 
Greenhouse Gas Emission Pathways, in the Context of Strengthening  
the Global Response to the Threat of Climate Change, Sustainable 
Development, and Efforts to Eradicate Poverty . Edited by V. Masson-
Delmotte, P. Zhai, H.-O. Pörtner, D. Roberts, J. Skea, P.R. Shukla, A. 
Pirani, et al. Cambridge and New York: Cambridge University Press. 
https://www.ipcc.ch/sr15/.
Jacob, D., L. Kotova, C. Teichmann, S.P. Sobolowski, R. Vautard,  
C. Donnelly, A.G. Koutroulis, et al. 2018. “Climate Impacts in Europe  
Under +1.5°C Global Warming.” Earth’s Future 6 (2): 264–85.  
https://doi.org/10.1002/2017EF000710.
Jiang, F., X. Li, B. Wei, R. Hu, and Z. Li. 2009. “Observed Trends of  
Heating and Cooling Degree-Days in Xinjiang Province, China.”  
Theoretical and Applied Climatology 97: 349–60. https://doi.
org/10.1007/s00704-008-0078-5.
Khatana, S.A.M., R.M. Werner, and P.W. Groeneveld. 2022.  
“Association of Extreme Heat with All-Cause Mortality in the  
Contiguous US 2008–2017.” JAMA Network Open 5 (5): e2212957. 
https://doi.org/10.1001/jamanetworkopen.2022.12957.

24  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
Kemp, L., C. Xu, J. Depledge, K.L. Ebi, G. Gibbins, T.A. Kohler, J. Rock -
ström, M. Scheffer, H.J. Schellnhuber, W. Steffen, and T.M. Lenton. 
2022. “Climate Endgame: Exploring Catastrophic Climate Change 
Scenarios.” Proceedings of the National Academy of Sciences 119 
(34): e2108146119.
Kirschbaum, D., and T. Stanley. 2018. “Satellite‐Based Assessment 
of Rainfall‐Triggered Landslide Hazard for Situational Awareness.” 
Earth’s Future 6 (3): 505–23. https://doi.org/10.1002/2017EF000715.
Klose, M., P. Maurischat, and B. Damm. 2016. “Landslide Impacts in 
Germany: A Historical and Socioeconomic Perspective.” Landslides  13 
(February): 183–99. https://doi.org/10.1007/s10346-015-0643-9.
Kuma, P., F.A.-M. Bender, and A.R. Jönsson. 2023. “Climate Model 
Code Genealogy and Its Relation to Climate Feedbacks and  
Sensitivity.” Journal of Advances in Modeling Earth Systems 15 (7): 
e2022MS003588. https://doi.org/10.1029/2022MS003588.
Lawrimore, J.H., M.J. Menne, B.E. Gleason, C.N. Williams, D.B. Wuertz, 
R.S. Vose, and J. Rennie. 2011. Global Historical Climatology Network— 
Monthly (GHCN-M) , Version 3. NOAA National Centers for Environ -
mental Information. doi:10.7289/V5X34VDR. Accessed 10 July 2024.
Lee, M., F. Nordio, A. Zanobetti, P. Kinney, R. Vautard, and J. Schwartz. 
2014. “Acclimatization across Space and Time in the Effects of Tem -
perature on Mortality: A Time-Series Analysis.” Environmental Health  
13 (October): 89. https://doi.org/10.1186/1476-069X-13-89.
Li, K., J. Pan, W. Xiong, W. Xie, and T. Ali. 2022. “The Impact of 1.5°C 
and 2.0°C Global Warming on Global Maize Production and Trade.” 
Scientific Reports  12 (October): 17268. https://doi.org/10.1038/
s41598-022-22228-7.
Lin, S., M. Luo, M., R.J. Walker, X. Liu, S.-A. Hwang, and R. Chinery. 
2009. “Extreme High Temperatures and Hospital Admissions for  
Respiratory and Cardiovascular Diseases.” Epidemiology  20(5): 
738–46. https://doi.org/10.1097/EDE.0b013e3181ad5522.
Lloyd‐Hughes, B., and M.A. Saunders. 2002. “A Drought Climatology 
for Europe.” International Journal of Climatology 22 (13): 1571–92.
Lunde, T.M., M.N. Bayoh, and B. Lindtjørn. 2013. “How Malaria Models 
Relate Temperature to Malaria Transmission.” Parasites and Vectors 6 
(20). https://doi.org/10.1186/1756-3305-6-20.
Malik, U., and W. James. 2007. “Reliability of Design Storms 
Used to Size Urban Stormwater System Elements.” Journal of 
Water Management Modeling R227-16 (15): 309–26. https://doi.
org/10.14796/JWMM.R227-16.
Meinshausen, M., J. Lewis, C. McGlade, J. Gütschow, Z. Nicholls, R. 
Burdon, L. Cozzi, and B. Hackmann. 2022. “Realization of Paris Agree -
ment Pledges May Limit Warming Just below 2°C.” Nature  604 (April): 
304–9. https://doi.org/10.1038/s41586-022-04553-z.
Mathes, R.W., K. Ito, K. Lane, and T.D. Matte. 2017. “Real-Time Surveil -
lance of Heat-Related Morbidity: Relation to Excess Mortality  
Associated with Extreme Heat.” PLoS ONE  12 (9): e0184364.  
https://doi.org/10.1371/journal.pone.0184364.
McKee, T.B., N.J. Doesken, and J. Kleist. 1993. “The Relationship of 
Drought Frequency and Duration to Time Scales.” Proceedings of the 
8th Conference on Applied Climatology 17 (22): 179–83.
Mia, M.T., N. Sultana, and A. Paul. 2015. “Studies on the Causes, 
Impacts and Mitigation Strategies of Landslide in Chittagong City, 
Bangladesh.” Journal of Environmental Science and Natural Resources  
8 (2): 1–5. https://doi.org/10.3329/jesnr.v8i2.26854.
Millar, R.J., J.S. Fuglestvedt, P. Friedlingstein, J. Rogelj, M.J. Grubb, H.D. 
Matthews, R.B. Skeie, P.M. Forster, D.J. Frame, and M.R. Allen. 2017. 
“Emission Budgets and Pathways Consistent with Limiting Warming  
to 1.5°C.” Nature Geoscience 10 (October): 741–47. https://doi.
org/10.1038/ngeo3031.
Mitchell, D., K. AchutaRao, M. Allen, I. Bethke, U. Beyerle, A. Ciavarella, 
P.M. Forster, et al. 2017. “Half a Degree Additional Warming, Progno -
sis and Projected Impacts (HAPPI): Background and Experimental 
Design.” Geoscientific Model Development  10 (2): 571–83. https://doi.
org/10.5194/gmd-10-571-2017.
Medina-Ramón, M., and J. Schwartz. 2007. “Temperature, Temperature 
Extremes, and Mortality: A Study of Acclimatization and Effect Modi -
fication in 50 United States Cities.” Occupational and Environmental 
Medicine 64 (12): 827–33. https://doi.org/10.1136/oem.2007.033175.
Möller, V., R. van Diemen, J.B.R. Matthews, C. Méndez, S. Semenov,  
J.S. Fuglestvedt, and A. Reisinger, eds. 2022: “Annex II: Glossary.”  
In Climate Change 2022: Impacts, Adaptation and Vulnerability . Con-
tribution of Working Group II to the Sixth Assessment Report of the 
Intergovernmental Panel on Climate Change, edited by H.-O. Pörtner, 
D.C. Roberts, M. Tignor, E.S. Poloczanska, K. Mintenbeck, A. Alegría, 
M. Craig, et al. Cambridge and New York: Cambridge University 
Press. https://doi.org/10.1017/9781009325844.029.
Mordecai, E.A., K.P. Paaijmans, L.R. Johnson, C. Balzer, T. Ben-Horin, 
E. de Moor, A. McNally, et al. 2012. “Optimal Temperature for Malaria 
Transmission Is Dramatically Lower than Previously Predicted.”  
Ecology Letters  16 (1): 22–30. https://doi.org/10.1111/ele.12015.

TECHNICAL NOTE   |  August 2024  |  25
City-scale, city-relevant climate hazard indicators under 1.5°C, 2.0°C, and 3.0°C of global warming
Mordecai, E.A., J.M. Cohen, M.V. Evans, P. Gudapati, L.R. Johnson, C.A. 
Lippi, K. Miazgowicz, et al. 2017. “Detecting the Impact of Temperature 
on Transmission of Zika, Dengue, and Chikungunya Using Mecha -
nistic Models.” PLoS Neglected Tropical Diseases 11 (4): e0005568. 
https://doi.org/10.1371/journal.pntd.0005568.
Mordecai, E.A., S.J. Ryan, J.M. Caldwell, M.M. Shah, and A.D. LaBeaud. 
2020. “Climate Change Could Shift Disease Burden from Malaria  
to Arboviruses in Africa.” Lancet Planetary Health  4 (9): e416–23. 
https://doi.org/10.1016/S2542-5196(20)30178-9.
Morrissey, M.C., G.J. Brewer, W.J. Williams, T. Quinn, and D.J. Casa. 
2021. “Impact of Occupational Heat Stress on Worker Productivity 
and Economic Cost.” American Journal of Industrial Medicine 64 (12): 
981–88. https://doi.org/10.1002/ajim.23297.
Nangombe, S., T. Zhou, W. Zhang, B. Wu, S. Hu, L. Zou, and D. Li. 2018. 
“Record-Breaking Climate Extremes in Africa under Stabilized 1.5°C 
and 2°C Global Warming Scenarios.” Nature Climate Change  8 (May): 
375–80. https://doi.org/10.1038/s41558-018-0145-6.
O’Neill, R.V., D.L. DeAngelis, J.B. Waide, and T.F.H. Allen. 1986. A Hier -
archical Concept of Ecosystems . Volume 23. Princeton, NJ: Princeton 
University Press.
Paaijmans, K.P., A.F. Read, and M.B. Thomas. 2009. “Understand -
ing the Link between Malaria Risk and Climate.” Proceedings of the 
National Academy of Sciences of the United States of America 106 (33): 
13844–9. https://doi.org/10.1073/pnas.0903423106.
Paul, A.R. and R. Maity. 2023. “Future Projection of Climate Extremes 
across Contiguous Northeast India and Bangladesh.” Scientific  
Reports 13(1): 15616.
Perkins-Kirkpatrick, S.E., and P.B. Gibson. 2017. “Changes in Regional 
Heatwave Characteristics as a Function of Increasing Global  
Temperature.” Scientific Reports  7 (1): 12256.
Perkins-Kirkpatrick, S.E., and S.C. Lewis. 2020. “Increasing Trends  
in Regional Heatwaves.” Nature Communications  11 (1): 3357.
Petley, D.N., 2009. “On the Impact of Urban Landslides.” Geological 
Society of London, Engineering Geology Special Publications 22 (1): 
83–99. https://doi.org/10.1144/EGSP22.6.
Petri, Y., and K. Caldeira. 2015. “Impacts of Global Warming on 
Residential Heating and Cooling Degree-Days in the United States.” 
Scientific Reports  5 (August): 12427. https://doi.org/10.1038/srep12427.
Phelan, P.E., K. Kaloush, M. Miner, J. Golden, B. Phelan, H. Silva, and 
R.A. Taylor. 2015. “Urban Heat Island: Mechanisms, Implications, and 
Possible Remedies.” Annual Review of Environment and Resources  
40 (November): 285–307. https://doi.org/10.1146/annurev-envi -
ron-102014-021155.
Qiu, W., and X. Yan. 2020. “The Trend of Heatwave Events in the 
Northern Hemisphere.” Physics and Chemistry of the Earth, Parts 
A/B/C 116: 102855.
Ragettli, M.S., A.M. Vicedo-Cabrera, C. Schindler, and M. Röösli. 2017. 
“Exploring the Association between Heat and Mortality in Switzer -
land between 1995 and 2013.” Environmental Research  158 (October): 
703–9. https://doi.org/10.1016/j.envres.2017.07.021.
Rao, K.K., A. Al Mandous, M. Al Ebri, N. Al Hameli, M. Rakib, and S. Al 
Kaabi. 2024. “Future Changes in the Precipitation Regime over the 
Arabian Peninsula with Special Emphasis on UAE: Insights from NEX-
GDDP CMIP6 Model Simulations.” Scientific Reports  14(1): 151.
Ren, X., Y. Lu, B.C. O’Neill, and M. Weitzel. 2018. “Economic and  
Biophysical Impacts on Agriculture under 1.5°C and 2°C Warming.”  
Environmental Research Letters  13 (11): 115006. https://doi.
org/10.1088/1748-9326/aae6a9.
Riahi, K., D.P. Van Vuuren, E. Kriegler, J. Edmonds, B.C. O’Neill, S. Fuji -
mori, N. Bauer, et al. 2017. “The Shared Socioeconomic Pathways and 
Their Energy, Land Use, and Greenhouse Gas Emissions Implications: 
An Overview.” Global Environmental Change 42 (January): 153–68. 
https://doi.org/10.1016/j.gloenvcha.2016.05.009.
Riahi, K., R. Schaeffer, J. Arango, K. Calvin, C. Guivarch, T. Hasegawa, 
K. Jiang, et al. 2022. “Mitigation Pathways Compatible with Long-Term 
Goals.” In Climate Change 2022: Mitigation of Climate Change . Con-
tribution of Working Group III to the Sixth Assessment Report of the 
Intergovernmental Panel on Climate Change, edited by P. R. Shukla, 
J. Skea, R. Slade, A. Al Khourdajie, R. van Diemen, D. McCollum, M. 
Pathak, et al. Cambridge and New York: Cambridge University Press. 
https://doi.org/10.1017/9781009157926.005.
Rosenberg, E.A., P.W. Keys, D.B. Booth, D. Hartley, J. Burkey, A.C. 
Steinemann, and D.P. Lettenmaier. 2010. “Precipitation Extremes and 
the Impacts of Climate Change on Stormwater Infrastructure in Wash -
ington State.” Climatic Change 102 (September): 319–49. https://doi.
org/10.1007/s10584-010-9847-0.
Ryan, S.J., C.A. Lippi, and F. Zermoglio. 2020. “Shifting Transmission 
Risk for Malaria in Africa with Climate Change: A Framework for 
Planning and Intervention.” Malaria Journal 19 (May): 170. https://doi.
org/10.1186/s12936-020-03224-6.

26  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
Ryan, S.J., A. McNally, L.R. Johnson, E.A. Mordecai, T. Ben-Horin, K. 
Paaijmans, and K.D. Lafferty. 2015. “Mapping Physiological Suitability 
Limits for Malaria in Africa under Climate Change.” Vector-Borne and 
Zoonotic Diseases , 15 (12): 718–25.
Sanderson, B.M., Y. Xu, C. Tebaldi, M. Wehner, B. O’Neill, A. Jahn, A.G. 
Pendergrass, et al. 2017. “Community Climate Simulations to Assess 
Avoided Impacts in 1.5 and 2°C Futures.” Earth System Dynamics 8 (3): 
827–47. https://doi.org/10.5194/esd-8-827-2017.
Schiavina, M., S. Freire, A. Carioli, and K. MacManus. 2023. “GHS-
POP R2023A: GHS Population Grid Multitemporal (1975–2030).” 
European Commission, Joint Research Centre. https://doi.
org/10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE.
Schleussner, C.-F., T. K. Lissner, E. M. Fischer, J. Wohland, M. Perrette, 
A. Golly, J. Rogelj, et al. 2016. “Differential Climate Impacts for Policy-
Relevant Limits to Global Warming: The Case of 1.5°C and 2°C.” Earth 
System Dynamics 7: 327–51. https://doi.org/10.5194/esd-7-327-2016.
Schuster, R.L., and L.M. Highland. 2007. “The Third Hans Cloos 
Lecture. Urban Landslides: Socioeconomic Impacts and Overview of 
Mitigative Strategies.” Bulletin of Engineering Geology and the Environ -
ment 66: 1–27. https://doi.org/10.1007/s10064-006-0080-z.
Scoccimarro, E., O. Cattaneo, S. Gualdi, F. Mattion, A. Bizeul, A.M. 
Risquez, and R. Quadrelli. 2023. “Country-Level Energy Demand 
for Cooling Has Increased over the Past Two Decades.” Commu -
nications Earth & Environment  4 (1): 208. https://doi.org/10.1038/
s43247-023-00878-3.
Sheffield, J., G. Goteti, and E.F. Wood. 2006. Development of a 50-Year 
High-Resolution Global Dataset of Meteorological Forcings for Land 
Surface Modeling. Journal of Climate  19 (13): 3088–3111.
Sherwood, S.C., and M. Huber. 2010. “An Adaptability Limit to Climate 
Change Due to Heat Stress.” Proceedings of the National Academy of 
Sciences of the United States of America 107 (21): 9552–55. https://doi.
org/10.1073/pnas.0913352107.
Sieck, K., C. Nam, L.M. Bouwer, D. Rechid, and D. Jacob. 2021. 
“Weather Extremes over Europe under 1.5 and 2.0°C Global Warming 
from HAPPI Regional Climate Ensemble Simulations.” Earth System 
Dynamics 12 (2): 457–68. https://doi.org/10.5194/esd-12-457-2021.
Stanke, C., M. Kerac, C. Prudhomme, J. Medlock, and V. Murray. 2013. 
“Health Effects of Drought: A Systematic Review of the Evidence.” 
PLoS Currents 5 (June). https://doi.org/10.1371/currents.dis.7a2cee9e9
80f91ad7697b570bcc4b004.
Stanley, T., and D.B. Kirschbaum. 2017. “A Heuristic Approach to Global 
Landslide Susceptibility Mapping.” Natural Hazards  87 (May): 145–64. 
https://doi.org/10.1007/s11069-017-2757-y.
Stull, R. 2011. “Wet Bulb Temperature from Relative Humidity and Air 
Temperature.” Journal of Applied Meteorology and Climatology  50 (11): 
2267–69. https://doi.org/10.1175/JAMC-D-11-0143.1.
Sugg, M., J. Runkle, R. Leeper, H. Bagli, A. Golden, L.H. Handwerger, 
T. Magee, et al. 2020. “A Scoping Review of Drought Impacts on 
Health and Society in North America.” Climatic Change  162 (October): 
1177–95. https://doi.org/10.1007/s10584-020-02848-6.
Svoboda, M., M. Hayes, and D.A. Wood. 2012. Standardized Precipita -
tion Index User Guide . Geneva: World Meteorological Organization. 
https://library.wmo.int/idurl/4/39629.
Thrasher, B., W. Wang, A. Michaelis, F. Melton, T. Lee, and R. Nemani. 
2022. “NASA Global Daily Downscaled Projections, CMIP6.” Scientific 
Data 9 (June): 262. https://doi.org/10.1038/s41597-022-01393-4.
Tilmes, S., D.G. MacMartin, J.T.M. Lenaerts, L. van Kampenhout,  
L. Muntjewerf, L. Xia, C.S. Harrison, et al. 2020. “Reaching 1.5 and 
2.0°C Global Surface Temperature Targets Using Stratospheric  
Aerosol Geoengineering.” Earth System Dynamics 11 (3): 579–601. 
https://doi.org/10.5194/esd-11-579-2020.
Underwood, B.S., Z. Guido, P. Gudipudi, and Y. Feinberg. 2017.  
“Increased Costs to US Pavement Infrastructure from Future  
Temperature Rise.” Nature Climate Change 7 (October): 704–7.  
https://doi.org/10.1038/nclimate3390.
UNFCCC (United Nations Framework Convention on Climate 
Change). 2016. The Paris Agreement. Bonn, Germany: UNFCCC 
Secretariat. https://unfccc.int/sites/default/files/resource/paris -
agreement_publication.pdf.Ukey, R., and A.C. Rai. 2021. “Impact of 
Global Warming on Heating and Cooling Degree Days in Major 
Indian Cities.” Energy and Buildings 244 (August): 111050. https://doi.
org/10.1016/j.enbuild.2021.111050.
Vecellio, D.J., S.T. Wolf, R.M. Cottle, and W.L. Kenney. 2022. “Evaluating 
the 35°C Wet-Bulb Temperature Adaptability Threshold for Young, 
Healthy Subjects (PSU HEAT Project).” Journal of Applied Physiology  
132 (2): 340–45. https://doi.org/10.1152/japplphysiol.00738.2021.
Vicente-Serrano, S.M., D. Peña-Angulo, S. Beguería, F. Domínguez-
Castro, M. Tomás-Burguera, I. Noguera, L Gimeno-Sotelo, and A. El 
Kenawy. 2022. “Global Drought Trends and Future Projections.” Philo -
sophical Transactions of the Royal Society A 380 (2238): 20210285.
Vonk, M.A. 2023. “SPEI: A Simple Python Package to Calculate and 
Visualize Drought Indices (v0.3.5).” Zenodo. https://doi.org/10.5281/
zenodo.10816741.Wehrli, K., B.P. Guillod, M. Hauser, M. Leclair, and S.I. 
Seneviratne. 2019. “Identifying Key Driving Processes of Major Recent 
Heat Waves.” Journal of Geophysical Research: Atmospheres 124 (22): 
11746–65. https://doi.org/10.1029/2019JD030635.

TECHNICAL NOTE   |  August 2024  |  27
City-scale, city-relevant climate hazard indicators under 1.5°C, 2.0°C, and 3.0°C of global warming
Wang, T., X. Tu, V.P. Singh, X. Chen, and K. Lin. 2021. “Global Data As -
sessment and Analysis of Drought Characteristics Based on CMIP6.” 
Journal of Hydrology 596: 126091.
Wimberly, M.C., J.K. Davis, M.V. Evans, A. Hess, P.M. Newberry, N. 
Solano-Asamoah, et al. 2020. “Land Cover Affects Microclimate and 
Temperature Suitability for Arbovirus Transmission in an Urban Land -
scape.” PLoS Neglected Tropical Diseases 14 (9): e0008614. https://doi.
org/10.1371/journal.pntd.0008614.
Wong, T., and P. Switzer. 2023. “Estimating Future Local Climate Haz -
ard Probabilities.” Technical Note. Washington, DC: World Resources 
Institute. https://doi.org/10.46830/writn.22.00074.
World Bank. n.d. “World Bank Country and Lending Groups.” https://
datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-
bank-country-and-lending-groups. Accessed November 1, 2023.
Xu, L., N. Chen, and X. Zhang. 2019. “Global Drought Trends  
under 1.5° and 2°C Warming.” International Journal of Climatology 
39 (4): 2375–85.
Xu, Z., G. FitzGerald, Y. Guo, B. Jalaludin, and S. Tong. 2016. “Impact  
of Heatwave on Mortality under Different Heatwave Definitions:  
A Systematic Review and Meta-analysis.” Environment International   
89–90 (April–May): 193–203. https://doi.org/10.1016/j.en -
vint.2016.02.007.
Zhang, F., L.X. Wei, and Y.H. Li. 2023. “Evaluation and Projection of 
Extreme High Temperature Indices in Southwestern China using 
NEX-GDDP-CMIP6.” Journal of Meteorological Research  37(0): 1-20.
Zhang, S., Q. Guo, R. Smyth, and Y. Yao. 2022. “Extreme Temperatures 
and Residential Electricity Consumption: Evidence from Chinese 
households.” Energy Economics 107 (March): 105890. https://doi.
org/10.1016/j.eneco.2022.105890.
Zhang, X., N. Chen, H. Sheng, C. Ip, L. Yang, Y. Chen, Z. Sang, et al. 
2019. “Urban Drought Challenge to 2030 Sustainable Development 
Goals.” Science of the Total Environment 693 (November): 133536. 
https://doi.org/10.1016/j.scitotenv.2019.07.342.
Zhao, L., K. Oleson, E. Bou-Zeid, E.S. Krayenhoff, A. Bray, Q. Zhu, Z. 
Zheng, C. Chen, and M. Oppenheimer. 2021. Global Multi-model 
Projections of Local Urban Climates. Nature Climate Change , 
11 (2): 152–57.
Zhao, M., J.K.W. Lee, T. Kjellstrom, and W. Cai. 2021. “Assessment 
of the Economic Impact of Heat-Related Labor Productivity Loss: 
A Systematic Review.” Climatic Change 167 (July): 22. https://doi.
org/10.1007/s10584-021-03160-7.

Copyright 2024 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License.  
To view a copy of the license, visit http://creativecommons.org/licenses/by/4.0/
  
10 G Street, NE  |  Washington, DC 20002  |  WRI.ORGWOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
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
This research was supported by Bloomberg Philanthropies.
The authors would like to thank the reviewers and advisers 
who provided input on this research (unless otherwise noted, 
organizational affiliations are WRI): Jessy Appavoo (C40 Cities), 
Alejandro Blei (NYU), Rebecca Carter, Taryn Fransen, Benjamin 
Jance (Global Covenant of Mayors), Robin King, Marc Manyifika, Paul 
Switzer (Stanford University), Gregory Taff, Harriet Tregoning, and 
Elizabeth Wesley.
ABOUT THE AUTHORS
Theodore Wong  is a Research and Project Associate on the Data 
and Tools team at WRI Ross Center for Sustainable Cities.
Contact: ted.wong@wri.org
Eric Mackres  is Senior Manager for Data and Tools at WRI Ross 
Center for Sustainable Cities.
Contact: eric.mackres@wri.org
