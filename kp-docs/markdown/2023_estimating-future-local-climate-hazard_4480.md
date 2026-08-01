---
doc_id: 2023_estimating-future-local-climate-hazard_4480
source_pdf: kp-docs/askwri-kps/2023_estimating-future-local-climate-hazard_4480.pdf
extraction_method: cache-plaintext
char_count: 76123
title: Estimating Future Local Climate Hazard Probabilities
authors: Wong, Ted; Switzer, Paul
date_published: 11/28/2023
article_type: Technical Note
sub_tag: Transport decarbonization
wri_primary_office: WRI Global
wri_programs: Cities
language: English
url: "https://www.wri.org/research/estimating-future-local-climate-hazard-probabilities"
doi: "https://doi.org/10.46830/writn.22.00074"
summary: This note describes methods for selecting and calibrating downscaled global climate models and using the modeled projections to generate probability models of complex climate hazard indicators.
---

# Estimating Future Local Climate Hazard Probabilities

WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
WO RL DWO RL D
RE SO UR CE SRE SO UR CE S
IN STIT UT EIN STIT UT E
TECHNICAL NOTE   |  Version 2.1  |  April 2024  |  1
CONTENTS
Abstract. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
Background. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .3
Climate model selection and calibration 5
Estimates of climate hazard frequencies 
and their uncertainty. . . . . . . . . . . . . . . . . . . . . .6
Examples ................................. 9
Applications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
Limitations ............................... 21
Endnotes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
Abbreviations ........................... 22
References .............................. 22
Acknowledgments ...................... 24
About the authors. . . . . . . . . . . . . . . . . . . . . . . 24
About WRI  .............................. 24
Technical notes document the research or analytical 
methodology underpinning a publication, interactive 
application, or tool.
Suggested Citation: Wong, T ., and P Switzer. 2023. 
“Estimating future local climate hazard probabilities.” 
Technical Note. Washington, DC: World Resources 
Institute. Available online at: doi.org/10.46830/
writn.22.00074.v2.
TECHNICAL NOTE
Estimating future local climate hazard 
probabilities
Theodore Wong and Paul Switzer
ABSTRACT
Decision-makers in government, the private sector, and civil society can better 
plan for climate change if their decisions are informed by predictions of future 
climate conditions and meteorological events as well as information about 
prediction uncertainty. This Technical Note describes a probabilistic method 
for predicting geographically localized future climate hazard events using 
output from downscaled climate models. The method provides probabilistic 
estimates of how often a given location will experience a prescribed climate 
hazard event or indicator during a prescribed future planning period, as 
defined by a user. Insights from this process can support climate adaptation 
and disaster risk reduction planning in agriculture, infrastructure, public health, 
and other domains.
BACKGROUND
Decision-making that involves land, built assets, or human populations must 
confront how the local climate will change. Long-standing societal systems 
such as cities and agriculture have adapted to long-existing climate regimes. 
Climate change has already begun disrupting these systems, and the increas-
ing frequency of disruptive meteorological conditions and events has already 
attracted the concern of researchers and practitioners in food security (Thorn-
ton et al. 2014), transportation infrastructure (Nasr et al. 2019; Wang et al. 
2019), energy infrastructure (Burillo et al. 2017), emergency management 
(Arnell 2022), worker safety (Moda et al. 2019), public health (Ngonghala et al. 
2021; Rocklöv and Tozan 2019), and other domains of human activity.
Global climate models provide readily available information on climate futures, 
but this information can be difficult for decision-makers to apply to their 
particular needs. For example, consider a roadway engineer who wants to know 
whether current local pavement design standards will be adequate under the 
future precipitation regime. Specifically, it might be useful to know how often

2  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
that most closely agree with matching observational data during 
the historical calibration period 1980–2014 (see “Estimates 
of climate hazard frequencies and their uncertainty”). Model 
selection will depend on both the geographic location and the 
specific weather variable(s) involved in the hazard specification. 
Further, the weather time series of the selected downscaled 
climate models are calibrated so that the calibrated model data 
match the statistics of the observational data (see “Climate 
model selection and calibration”).
However, all climate models carry inherent uncertainty in their 
future predictions, which is characterized probabilistically. 
Basically, a climate model’s future hazard event count is treated 
as a realization of a random variable, and Bayes methodol-
ogy is then used as a framework for generating a distribution 
of possible future hazard event counts as an expression of the 
prediction uncertainty. (This probabilistic framework is more 
fully described in “Estimates of climate hazard frequencies and 
their uncertainty.”)
Project background
The method was developed to produce hazard information 
for climate adaptation as part of the Data Portal for Cities 
project (GCoM 2023), which is a partnership between World 
Resources Institute (WRI) and the Global Covenant of Mayors 
for Climate and Energy (GCoM). GCoM member cities are 
expected to report future climate hazard probabilities under 
GCoM’s Common Reporting Framework (GCoM 2018). This 
method allows us to estimate those probabilities as well as future 
average values of those hazards.
Existing data resources provide climate hazard forecasts, but 
without some useful detail that our method can provide. Some, 
such as the Climate Change Knowledge Portal (World Bank 
n.d.) and the Intergovernmental Panel on Climate Change 
Working Group I Atlas (Iturbide et al. 2021), provide simple 
meteorological variable predictions. The ThinkHazard! Tool 
provides ordinal (i.e., high, medium, low, and very low) risk 
assessments based on probabilities of predefined indicators 
and thresholds.1 It does not allow users to choose indicators or 
critical thresholds. Our method differs from these approaches in 
its ability to allow data tools to report exceedance probabilities 
based on indicators and thresholds provided by, and presumably 
directly relevant to, users.
This method has been piloted using hazard definitions identi-
fied in collaboration with GCoM, four GCoM cities (Hobart, 
Australia; Makati, Philippines; Tópaga, Colombia; and Vitacura, 
Chile), and stakeholders in an integrated climate assessment 
process in Campinas, Brazil. It is also being piloted in data 
to expect “extreme” precipitation events for the planning period 
2050–90, where an extreme precipitation event is defined as an 
accumulation greater than a specified threshold, perhaps over a 
four-day period. Climate models do not output annual frequen-
cies of events such as four-day threshold exceedances but rather 
as hourly, daily, or monthly instances of raw meteorological 
variables in a number of simulations. Converting these simula-
tion outputs into estimates of frequencies of complicated climate 
hazard events is a nontrivial task.
The hypothetical roadway engineer will also need information 
regarding the uncertainty of the prediction. Some decisions—for 
example, whether to invest in redundant systems or whether to 
purchase insurance—depend not only on hazard predictions but 
also on prediction uncertainty.
The goal of this paper is to provide estimates of the frequen-
cies of localized climate hazard events for a specified future 
period, together with a representation of the uncertainty of such 
estimates, based on information provided by available climate 
models. Climate models are built on numerous assumptions, and 
their outputs include an enormous amount of uncertainty. Our 
method does not remove this uncertainty; rather, it expresses it 
in terms of probabilities of climate events.
The climate hazard events that are considered here are those 
whose occurrences can be seen or derived from the four parallel 
daily time series of minimum temperature, maximum tempera-
ture, daily precipitation, and daily average relative humidity. In 
addition, hazard events may also be defined in terms of a daily 
time series calculated from two or more of these four afore-
mentioned time series, such as a thermal comfort index that 
combines daily temperature and humidity.
These are some examples of hazard definitions:
 ▪ Yearlong precipitation exceeding 1,800 millimeters 
 ▪ Runs of five or more consecutive days with maximum wet-
bulb globe temperature exceeding 35°C
 ▪ Sixty or more consecutive days with zero precipitation
 ▪ Accumulation of 3,000 growing degree-days between a crop’s 
planting date and the first autumn frost
Estimates of the frequency of future hazard events can be 
obtained from the daily time series output of any of the numer-
ous climate models. There will be inevitable disagreement 
among these climate models, and there are potential biases 
introduced when coarse-scale global models are downscaled to 
estimate higher-resolution climate phenomena. We deal with 
model disagreement by focusing on those downscaled models

TECHNICAL NOTE   |  December 2023   |  3
Estimating future local climate hazard probabilities
dashboards for the UrbanShift and Cities4Forests platforms, 
for the prototype AgriAdapt agricultural climate risk assess-
ment tool funded by the Walmart Foundation, and a project 
supported by Bloomberg Philanthropies to describe city climate 
hazards under 1.5°C and 2.0°C global warming scenarios.
DATA  
Data sources
This method requires two types of data: a historical time series 
of daily meteorological variables and a modeled daily time series 
whose temporal coverage includes both the historical series 
and the future years of interest. (The method requires only 
one modeled series, but we provide a method for choosing a 
few best-performing models from a larger set of models.) This 
method does not depend on specific choices of source data, such 
as spatial or temporal extent, spatial resolution, or greenhouse 
gas emissions scenario. The data sources we name below are the 
ones we used when developing the method.
One set of time series, used for climate model calibration, are 
historical observations for the years 1980–2014. For this, we 
use the ERA5 reanalysis data set (ECMWF 2022), a satel-
lite data product of the European Centre for Medium-Range 
Weather Forecasts with a spatial resolution of 31 kilometers 
(km). The other data set is an ensemble of downscaled daily time 
series outputs from global climate models (GCMs). These time 
series include the historical years covered by the observation 
time series as well as the specified future years of interest. We 
have used the National Aeronautics and Space Administration 
(NASA) NEX-GDDP-CMIP6 product (NASA 2022), which 
includes outputs from 34 Coupled Model Intercomparison 
Project Phase 6 (CMIP6) models at approximately 25 km 
spatial resolution. CMIP6 is a project that coordinates among 
research institutions to standardize model outputs to allow for 
intercomparison (Eyring 2016). Of the 34 models included in 
NEX-GDDP-CMIP6, 30 include all variables of interest for all 
years of interest. These models are listed in Table 1.
MODEL MODEL 
FAMILYa
INSTITUTION b
ACCESS-CM2 HadAM Commonwealth Scientific and Industrial Research Organisation (CSIRO); Australian Research Council Centre of Excellence for 
Climate System Science
ACCESS-ESM1-5 HadAM CSIRO 
BCC-CSM2-MR CCM Beijing Climate Center
CanESM5 CanAM Canadian Centre for Climate Modelling and Analysis
CMCC-CM2-SR5 CCM
Fondazione Centro Euro-Mediterraneo sui Cambiamenti Climatici
CMCC-ESM2 CCM
CNRM-CM6-1 ECMWF Centre National de Recherches Meteorologiques; Centre Européen de Recherche et de Formation Avancée en Calcul 
ScientifiqueCNRM-ESM2-1 ECMWF
EC-Earth3 ECMWF EC-Earth Consortium (Agencia Estatal de Meteorología, Spain; Barcelona Supercomputing Center, Spain; Consiglio Nazionale 
delle Ricerche–Istituto di Scienze dell’Atmosfera e del Clima, Italy; Danish Meteorological Institute, Denmark; Ente per le 
Nuove Technologie l’Energia e l’Ambiente, Italy; Finnish Meteorological Institute, Finland; Geomar, Germany; Irish Centre for 
High-End Computing, Ireland; International Centre for Theoretical Physics, Italy; Instituto Dom Luiz, Portugal; Institute for 
Marine and Atmospheric research Utrecht, Netherlands; Instituto Português do Mar e da Atmosfera, Portugal; Karlsruhe 
Institute of Technology, Germany; Royal Netherlands Meteorological Institute, Netherlands; Lund University, Sweden; Met 
Eireann, Ireland; Netherlands eScience Center, Netherlands; Norwegian University of Science and Technology, Norway; 
Oxford University, UK; SURFsara, Netherlands; Swedish Meteorological and Hydrological Institute, Sweden; Stockholm 
University, Sweden; Unite ASTR, Belgium; University College Dublin, Ireland; University of Bergen, Norway; University of 
Copenhagen, Denmark; University of Helsinki, Finland; University of Santiago de Compostela, Spain; Uppsala University, 
Sweden; Utrecht University, Netherlands; Vrije Universiteit Amsterdam, Netherlands; Wageningen University, Netherlands)
EC-Earth3-Veg-LR ECMWF
FGOALS-g3 CCM Chinese Academy of Sciences
Table 1  |  Climate models included in NEX-GDDP-CMIP6

4  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
MODEL MODEL 
FAMILYa
INSTITUTION b
GFDL-CM4 GFDL
National Oceanic and Atmospheric Administration (United States), Geophysical Fluid Dynamics LaboratoryGFDL-CM4_gr2 GFDL
GFDL-ESM4 GFDL
HadGEM3-GC31-LL HadAM Met Office Hadley Centre; Natural Environment Research Council (United Kingdom)
HadGEM3-GC31-MM HadAM Met Office Hadley Centre; Natural Environment Research Council (United Kingdom); National Institute of Meteorological 
Sciences/Korea Meteorological Administration
INM-CM4-8 INM Institute for Numerical Mathematics, Russian Academy of Science
INM-CM5-0 INM
IPSL- CM6A-LR IPSL Institut Pierre Simon Laplace
KACE-1-0-G HadAM National Institute of Meteorological Sciences/Korea Meteorological Administration; National Institute of Water and 
Atmospheric Research (New Zealand)
KIOST-ESM GFDL Korea Institute of Ocean Science and Technology
MIROC6 MIROC Japan Agency for Marine-Earth Science and Technology
MIROC-ES2L MIROC
MPI-ESM1-2-HR ECMWF HAMMOZ Consortium (ETH Zurich, Switzerland; Max Planck Institut für Meteorologie, Germany; Forschungszentrum Jülich, 
Germany; University of Oxford, United Kingdom; Finnish Meteorological Institute, Finland; Leibniz Institute for Tropospheric 
Research, Germany; Center for Climate Systems Modeling, ETH Zurich, Switzerland)MPI-ESM1-2-LR ECMWF
MRI-ESM2-0 UCLA GCM Meteorological Research Institute (Japan)
NorESM2-LM CCM NorESM Climate Modeling Consortium (Center for International Climate and Environmental Research; Norwegian 
Meteorological Institute; Nansen Environmental and Remote Sensing Center; Norwegian Institute for Air Research; University 
of Bergen; University of Oslo; and Uni Research)NorESM2-MM CCM
TaiESM1 CCM Research Center for Environmental Changes, Academia Sinica
UKESM1-0-LL HadAM Met Office Hadley Centre; Natural Environment Research Council (United Kingdom); National Institute of Meteorological 
Sciences/Korea Meteorological Administration
Note: We acknowledge the World Climate Research Programme, which, through its Working Group on Coupled Modelling, coordinated and promoted CMIP6. We thank the climate 
modeling groups for producing and making available their model output, the Earth System Grid Federation (ESGF) for archiving the data and providing access, and the multiple funding 
agencies who support CMIP6 and ESGF.
Sources:  a. Kuma et al. 2023; b. NASA 2023.
Table 1 also lists a model family for each included model. Kuma 
et al. (2023) find that many of the climate models included in 
model intercomparison projects share algorithms and code. This 
is because research institutions commonly share modular code 
components among each other, and researchers commonly reuse 
code as they develop newer generations of models. Combining 
or comparing results from different models will likely under-
estimate variation if one fails to account for the underlying 
similarity among models that share a family. As we describe 
below, our strategy here is to ensure that we always report results 
from models from different families. (See Sanderson et al. 
[2017] for an alternative approach to making use of information 
from model ensembles.)
NEX-GDDP-CMIP6 provides several greenhouse gas emission 
scenarios based on the Shared Socioeconomic Pathways (SSPs; 
Riahi et al. 2017) We used SSP5-8.5, which incorporates the 
high emissions scenario that most closely reflects both historical 
emissions and plausible scenarios of future emissions (Schwalm 
Table 1  |  Climate models included in NEX-GDDP-CMIP6 (continued)

TECHNICAL NOTE   |  December 2023   |  5
Estimating future local climate hazard probabilities
2020). In the CMIP6 models, the emission pathways are used 
only for years beginning with 2015. For years 2014 and prior, 
atmospheric composition is driven by historical natural and 
human-driven processes. Our selected historical year range ends 
with 2014 to allow us to separate our consideration of historical 
and emission-driven climates.
Occurrences of specified hazard events are determined from the 
daily time series of the relevant weather variables, such as the 
maximum daily near-surface air temperature, minimum daily 
temperature, and daily precipitation.
CLIMATE MODEL SELECTION 
AND CALIBRATION
Climate model selection
We select those climate models that perform best for a particu-
lar weather variable in a particular geographic location. Model 
output time series are compared with the corresponding observed 
time series over the historical period 1980–2014. We divide the 
35-year historical period into 140 quarterly seasons and find 
each season’s mean value for the weather variable of interest. 
We compute the root-mean-square error (RMSE) difference 
between the 140 quarterly mean values for the model output and 
the corresponding 140 historical average values. We do this for 
each of 30 NEX-GDDP-CMIP6 models and rank the models 
according to their RMSE when compared with observations for 
the historical period. The goal is to select downscaled models 
that best match the relevant weather variable seasonal climatol-
ogy of the observations at the specified location, not to match 
day-by-day observations. We note that models that perform 
well for average values of weather values might not perform well 
for extreme values. Model selection methods that address this 
potential shortcoming are a topic of future research.
To present concise model-based estimates of the frequency 
of future hazard events and reduce the computational burden 
of subsequent calculation, we select the three climate models 
with the smallest RMSE when compared with corresponding 
observations for the historical period 1980–2014. We further 
constrain the selection of climate models to ensure that they 
are from three different model families. Selection is imple-
mented as follows:
1. For each model family, rank the member models by RMSE.
2. Rank the families by the smallest RMSE of their members.
3. Select as the best models the best members of the 
three best families.
When selecting the best models, the decision will depend both 
on the specified geographic location and the particular weather 
variable relevant to the specified hazard event definition. For 
hazards that combine more than one weather variable, we sug-
gest choosing the single models that perform best for the hazard 
itself, based on RMSE calculated for the hazard, rather than for 
any one of its component variables.
Climate model calibration
We then calibrate the best models to better align with the 
historical data; that is, we shift the climate model output data 
to more closely align with the distribution of the histori-
cal data. To do so, for each of the selected climate models, 
the relevant weather variable data are recalibrated so that the 
marginal frequency distribution of the pooled daily values of 
calibrated model data approximately matches the marginal 
frequency distribution of the corresponding pooled observed 
data for the historical period 1980–2014. The marginal distri-
bution of time series data is the frequency distribution of the 
daily weather variable measurements considered as a pooled 
sample of numbers.
We align the model frequency distribution with the historical 
data by shifting the percentiles of the model distribution. For 
example, if the 20th model percentile corresponds to the 30th 
percentile of the observations, then the 30th percentile of the 
calibrated model data will correspond to the 20th percentile of 
the uncalibrated model data. The calibration is achieved using 
percentile-percentile (P-P) plots. (See Holmgren [1995] for a 
discussion of P-P plots.) Specifically, a P-P plot shows the frac-
tion of the observed daily values (horizontal axis) that are less 
than or equal to the p percentile of the model data (vertical axis), 
for values of p between zero and 100 percent. P-P calibration is 
described algorithmically below.
The flexibility of percentile calibration allows for model data to 
shift both higher and lower in different parts of the distribu-
tion. Although common methods of calibrating model data to 
observations typically use parametric linear regressions, we chose 
to adapt nonparametric P-P plots for calibration because of 
their flexibility over the whole range of weather data. Percentile 
calibration also avoids having to make arbitrary adjustments to 
parametric methods when they result in impossible values (e.g., 
negative counts).
The following is an algorithmic description of the P-P calibra-
tion plot construction. The horizontal and vertical axes of a P-P 
plot run from 0 to 1, respectively, representing the cumulative

6  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
fractions of the observed and modeled historical weather vari-
able data. Ignoring leap years, there are some 13,140 daily values 
of the weather variable during the 36-year calibration period.
 ▪ Pool all the 2N daily data, combining the observed and 
model data, and sort the pooled data from small to large.
 ▪ Let O(j) be the position in the combined sorted data of the 
j-th smallest value in the sorted unpooled observed data. 
 ▪ The P-P calibration plot is a nondecreasing plot with  plotted 
points whose coordinates are 
Effective P-P model calibration requires substantial overlap 
of the historical frequency distributions of the selected model 
weather data and corresponding observations at the specified 
location. Models were selected based on how well they matched 
the historical period weather data; nevertheless, a selected model 
may be a bad match to marginal distribution of the observations. 
Therefore, model predictions for future time periods should not 
be attempted with output from that model. P-P calibration will 
not correct gross model inadequacy. As a suggested arbitrary 
rule of thumb, the smallest of the modeled daily weather values 
for the historical calibration period should not exceed the 10th 
percentile of the observed values, and the largest of the modeled 
values should not fall below the 90th percentile of the observed 
values, with at least 80 percent overlap between observations and 
selected-model data. In our examples, insufficient distributional 
overlap was not encountered.
We derive four separate P-P calibration plots that are specific 
to data from each season, defined as March–May, June–August, 
September–November, and December–February, and each 
quarter includes 3,285 daily values of observed or model data, 
for each weather variable, in the historical period. P-P plots 
are further specific to the selected climate model, geographic 
location, and the relevant weather variable. The P-P calibration 
plots derived from the historical data are then used to recalibrate 
the future-period daily weather variable time series generated by 
the selected climate models. The four seasonal P-P calibration 
plots are then used to shift the marginal distribution of future 
model-generated daily weather data, separately for each season, 
for the specified future hazard prediction period. The method of 
using the P-P plots to calibrate future model data is described 
algorithmically below.
Application of the P-P plot to calibrate 
future model weather data
Future daily weather time series, derived from a selected climate 
model for a specified future period, are recalibrated using the 
previously described P-P calibration plots that were estimated 
from past historical data. Recalibration is done separately for 
the pooled model data from each of the four seasons, using the 
season-specific P-P plot. The number of season-specific daily 
values is denoted by Nfut; for example, a 20-year future period 
has approximately Nfut = 1825 = 20 × 365 ÷ 4 daily values from 
each of the four seasons.
First, the daily data are put in size order from small to large. 
Calibration consists of replacing the j-th smallest value by the 
j’-th smallest value, where j’ is calculated using the associated 
P-P calibration specific to the season and the selected climate 
model as follows: 
 ▪ Set                   on the horizontal axis of the P-P plot and 
determine the corresponding vertical coordinate 
from the P-P plot.                   
 ▪ Set                             (i.e., replace the j-th smallest future 
model value by the j’-th smallest future value). 
 ▪ Repeat this model data shifting for each                 .   
(Note: Some of the very smallest or very largest of the 
calibrated data values may repeat.)
Finally, put combined shifted model values back into their 
original time order to obtain the calibrated model daily time 
series for the specified future period. The calibrated model future 
time series is then scanned to obtain a count of the number of 
predicted events. This future data calibration exercise is repeated 
for each of the three selected climate models.
ESTIMATES OF CLIMATE 
HAZARD FREQUENCIES AND 
THEIR UNCERTAINTY
The goal is to predict the number of occurrences of a specified 
climate hazard event during a specified future period at a speci-
fied geographic location. In general, to obtain the future hazard 
frequency estimate for a selected climate model, we calibrate the 
relevant future model weather data and then scan the result-
ing calibrated daily time series to obtain the model-estimated 
count of the number of hazard events during the specified future 
period. This event count derived from the future calibrated

TECHNICAL NOTE   |  December 2023   |  7
Estimating future local climate hazard probabilities
model time series is denoted by C. The statistical uncertainty 
associated with this predicted future event count derives from 
the probabilistic framework described below.
Total count of future-period hazard 
events
The uncertainty assessment of future model-based event counts 
is based on probabilistic assumptions. Here we assume that 
hazard events occur over time according to a nonhomogeneous 
Poisson stochastic process that is governed by an unknown rate 
parameter. This rate parameter could vary year to year over the 
duration of the specified future prediction period (thus making 
it nonhomogeneous) to reflect ongoing climate evolution. The 
Poisson rate parameter could also vary seasonally. The time-inte-
grated value of this uncertain rate parameter is denoted by r. The 
number of event occurrences over the specified future period is 
then a Poisson-distributed random variable with mean r. (The 
Poisson process framework does restrict the type of hazard 
events that can be considered. Specifically, it excludes events that 
are expected to occur clustered in time. For such cases, counts of 
individual events could be replaced by counts of event clusters, 
suitably defined.)
Cast in a Bayes framework, we use the Jeffreys invariant prior 
distribution for the unknown Poisson distribution parameter, r. 
Then, conditioning on the future event count, C, obtained from 
the calibrated model data, will yield a gamma posterior distribu-
tion for the Poisson distribution parameter, r. This posterior 
gamma distribution for r has mean             .
To represent the uncertainty in the future event count, based on 
the selected climate model, we use the resulting Bayes predic-
tive frequency distribution. This distribution is a form of the 
gamma-Poisson distribution where the probability of seeing  
events during the future period is
where  denotes the gamma function. This distribution is left 
skewed with mean             ,  and standard deviation is              . 
This frequency distribution of predicted event counts can be 
graphically represented by its histogram (see “Illustration: Nai-
robi drought”). This distribution of future hazard event counts 
can also be used to obtain probabilities of specified outcomes of 
interest, such as the probability of experiencing at least K hazard 
events during the specified future period. 
Hazard event counts for the specified future prediction period 
can also be expressed as average annual counts by dividing by N, 
the length in years of the specified future period.
The event count prediction exercise described above is repeated 
for each of the three selected climate models chosen for the 
specified hazard definition at the specified location. Hazard 
event count prediction distributions that are derived from dif-
ferent climate models will differ more or less from one another; 
we report results for the three selected models to illustrate the 
degree to which the climate models might differ in their predic-
tions. There is no simple statistical basis for combining results 
from different climate models. (See “Limitations,” where we 
further discuss the issue of combining or not combining predic-
tions from different climate models). 
These future hazard event count uncertainties are conditional 
on the model calibration P-P plots derived from the histori-
cal calibration period. These calibration plots shift daily model 
weather data so that they match the 40-year marginal frequency 
distribution of the historical daily data. If we had access in 
our downscaled data set to multiple, independent runs of each 
model, then the hazard event prediction exercise, including 
calibration, could be repeated separately for each ensemble 
member, and the predicted future hazard event counts would be 
pooled across all ensemble members. The pooled event counts 
would then also include variation induced by variability among 
the calibration plots. However, given the 40-year length of the 
historical calibration period, we would not expect large differ-
ences among calibration plots for different ensemble members 
from the same model.
Zero-one annual count data
If hazard events are defined as occurring or not occurring during 
a calendar year, then a more appropriate probabilistic formula-
tion of event count uncertainty treats each year as a Bernoulli 
trial with event occurrence probabilities p and (1 - p), respec-
tively. For example, a hazard event year might be one having at 
least 10 days with a maximum temperature of 40°C or higher, as 
in the Kolkata illustration described in the “Examples” section. 
The goal is to provide a prediction for the number of future-
period years that experience the hazard event, together with a 
range of uncertainty based on probability modeling of event 
occurrences. For the Kolkata example, hazard event occurrences 
are derived from the maximum temperature daily time series; 
climate model selection and calibration to historical maximum 
temperature data are the same as previously described.

8  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
For the specified future period, such as the 21-year period 
2050–70, we obtain the model daily time series of the relevant 
weather variable, which is then recalibrated separately for each 
of the selected downscaled climate models. We use the recali-
brated daily time series to obtain a count, C, of the number of 
years that meet the specified hazard event definition.
If the annual event occurrence probability p is assumed not 
to change during the N-year future prediction period, then 
the total number of years with event occurrences would be 
a binomial random variable with parameters N and p. The 
assumption is also that the occurrence of the event in one year 
does not affect the event occurrence probability in another 
year. These independence assumptions are less restrictive than 
the requirements described earlier for Poisson modeling of 
event occurrences.
With this probabilistic structure for future event occurrences, 
our Bayes formulation treats the binomial event-rate parameter, , 
as itself random with a Jeffreys invariant prior distribution. Then 
the posterior distribution of the future period p, conditional on 
the model event count, C, is a beta distribution with  
parameters                                  . 
The resulting uncertainty distribution of the future-period 
hazard event count, derived from the selected climate model, is 
represented by the Bayes predictive frequency distribution. This 
distribution is the beta-binomial distribution where the prob-
ability of seeing x hazard years out of N years is
The mean of this distribution of hazard event counts is  
  ; the standard deviation is
These probabilities for the predicted event counts are repre-
sented by a histogram and are repeated for each of the three 
selected climate models (see “Illustration: Probability of thresh-
old exceedance for Kolkata extreme heat”).
Event counts could alternatively be expressed as annual aver-
age counts by dividing the counts by N, the length in years of 
the specified future period. Longer future prediction periods 
have a smaller coefficient of variation, defined as the prediction 
standard deviation as a proportion of its mean value.
The Bernoulli annual hazard event occurrence parameter may 
evolve over the course of the specified future period. If so, 
the binomial distribution will no longer be strictly correct for 
describing the total event count over the N-year period. To 
mitigate the problem, one could divide the future prediction 
period into a small number of shorter periods, say decades, and 
separately record the calibrated model event counts in each 
decade. The prediction exercise could then be done separately 
for each decade, yielding separate decadal posterior distributions 
for the annual rate parameter. The uncertainty associated with 
the sum of the decadal hazard event counts is represented by the 
sum of independent beta-binomial distributions.
Prediction of average annual counts of 
hazard events  
We describe a general nonparametric Bayes approach to 
estimate location-specific future annual weather statistics based 
on a calibrated climate model’s daily weather time series for a 
specified N-year future period. The predictive Bayes method we 
describe generates multiple N-year realizations of future-period 
yearly counts of hazard events, conditioned on the climate 
model data for that future period. This predictive Bayes ensem-
ble of yearly counts for this N-year period is used to derive a 
corresponding predictive distribution for the average annual 
number of hazard event occurrences for the specified period. The 
probabilistic structure in this section generalizes the discussion 
of the preceding section, “Zero-one annual count data,” which 
deals with binary annual hazard events (i.e., yearly event counts 
of either zero or greater than zero).
Our nonparametric approach is based on a histogram of the N 
years of annual hazard counts. For the histogram, we use a speci-
fied number, K, of equal-width bins and a specified range  
(Hmin, Hmax) of possible future values of the annual hazard count. 
There is no single prescribed method for setting the range, but 
it may be guided by the minimum and maximum annual hazard 
counts seen in the future-period output of the selected calibrated 
climate models. We use K = 10 bins, although average annual 
counts are not expected to be sensitive to the number of bins. 
The bin boundaries are defined using the following notation:
Bin width is 
Bin centers are 
Bins are

TECHNICAL NOTE   |  December 2023   |  9
Estimating future local climate hazard probabilities
Allocate the annual hazard event counts for the future N-year 
period to the K bins. The resulting bin frequencies are denoted 
C(i)  i = 1..K, with sum { C(i) } = N. Bins may have counts of 
zero. We define the average annual hazard count as a frequency-
weighted average of the bin centers, which will typically differ 
somewhat from the simple annual average of the individual 
yearly hazard counts.
We use Bayes histogram probability modeling. The climate 
model bin frequencies C(1)..C(K) are considered to be a realiza-
tion from a multinomial distribution whose a priori probability 
vector is sampled from the uniform Dirichlet distribution 
with constant parameter 1/K  for each bin (Berger et al. 2015). 
Then the posterior distribution for the multinomial probability 
vector, conditional on the observed histogram of future-period 
annual counts, is a nonuniform Dirichlet distribution with 
vector parameter
To obtain a predictive histogram for future annual counts, we 
repeatedly simulate probability vectors from the above posterior 
Dirichlet distribution. (We use 10,000 simulated vectors.) For 
each of these simulated probability vectors, we then generate a 
multinomial vector of histogram bin frequencies that sum to N. 
These simulated predictive bin frequencies are denoted  
Cpred(i),i = 1..K. 
Each simulation of a predictive histogram of bin frequencies 
yields a corresponding weighted average annual count for the 
N-year future period,  
Repetitions of the simulation yield a predictive distribution of 
the average annual hazard count, Hpred, for the specified N-year 
period. This predictive distribution for Hpred illustrates the proba-
bilistic uncertainty associated with climate model estimates for 
the yearly number of occurrences of the specific climate hazard 
indicator. The Hpred predictive distribution could then be sum-
marized by its mean and standard deviation or by a quartile box 
plot, for example. The standard deviation or other expression of 
uncertainty describes uncertainty in the estimate of the average, 
not the variability of the underlying hazard count.
EXAMPLES
Summary of steps to estimate future 
climate hazard event occurrence 
frequencies
1. Specify a geographic location. This method can be applied 
to only one model pixel at a time. If information for several 
adjacent pixels is desired, the method would have to be run 
separately for each pixel.
2. Specify a future period of interest, typically 
spanning 10–50 years.
3. Specify a hazard event of interest, whose occurrences can be 
determined from daily time series of minimum temperature, 
maximum temperature, total precipitation, and average 
relative humidity.
4. Collect relevant observed daily weather-variable time 
series for the specified geographic location for the 35-year 
historical model calibration period 1980–2014.
5. Collect the corresponding daily weather-variable time series 
for the candidate downscaled climate models.
6. Select the three best candidate models by comparing all 
candidate models with the observed data for the 35-year 
historical model calibration period, as described in “Climate 
model selection and calibration.” The following steps are 
repeated for each of the selected climate models.
7. Compute season-specific P-P calibration plots based on the 
observations and model data for the historical period.
i. For the specified future period of interest, obtain the 
relevant climate model daily time series for the relevant 
weather variable. Recalibrate this future-period time 
series using the seasonal P-P calibrations derived from 
the historical period data. 
ii. For the specified hazard event, count the number of 
future occurrences in the calibrated daily time series.
iii. Use the Bayes procedure outlined in “Estimates of 
climate hazard frequencies and their uncertainty,” in 
conjunction with the calibrated-model future event 
count, to obtain a posterior frequency distribution for 
future event counts. 
iv. Report the histogram of the future hazard event count, 
together with appropriate summary statistics. Show 
these side by side for the three selected models to 
exhibit model similarities or differences for predicted 
hazard event counts.

10  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
Figure 1  |  Average maximum daily temperature, by seasonal quarter, for a location in Kolkata, India (1980–2014) 
Notes: Observed values from ERA5 are in yellow. Seasonal averages from the three best models are shown in red. Models were selected based on root-mean-square error (RMSE) 
calculated between modeled and observed quarterly averaged data, across all seasons. These selected models are NorESM2-LM, ACCESS-ESM1-5, and MIROC-ES2L.
Source: WRI authors.
Illustration: Probability of threshold 
exceedance for Kolkata extreme heat
The first example looks at the frequency of hot weather years 
in Kolkata, India, during the 21-year period 2050–70. A hot 
weather year is specified as having 10 or more days with a 
maximum temperature of 40°C or higher. We chose this event 
definition for ease of illustration. For example, other heat-related 
hazard events might be based on a different temperature thresh-
old or a minimum temperature or thermal comfort index. In 
practice, event definition would be informed by relevant research 
and consultation with local experts and decision-makers.
Figure 1 presents four annual time series of season-specific 
daily maximum temperature averages for a location (latitude 
22.53° north, longitude 88.36° east) in Kolkata for the years 
1980–2014. Seasonal averages are calculated over the three 
indicated months, and the time series track how the seasonal 
averages change from year to year. The observed temperature 
series taken from ERA5 are plotted in yellow. Overall, there are 
140 quarters in the historical period for comparing model aver-
ages with observed averages to calculate a model’s RMSD The 
three GCMs with the lowest overall RMSE are plotted in red. 
The three selected GCM’s with the lowest overall RMSE are 
NorESM2-LM, ACCESS-ESM1-5, and MIROC-ES2L.
Figure 2 shows the four seasonal P-P calibration plots of mod-
eled versus observed daily maximum temperatures at Kolkata for 
the historical period 1980–2014. The three color-coded plots are 
for the best-fitting climate models. Future modeled time series 
of daily maximum temperatures are recalibrated based on these 
plots (see “Climate model selection and calibration” and “Esti-
mates of climate hazard frequencies and their uncertainty”).
Figure 2. P-P plots for each of the selected climate models, 
based on the marginal distributions of daily maximum tempera-
ture at Kolkata (1980–2014)

TECHNICAL NOTE   |  December 2023   |  11
Estimating future local climate hazard probabilities
Figure 2  |  P-P plots for each of the selected climate models, based on the marginal distributions of daily maximum 
temperature in Kolkata (1980–2014)
Notes: A percentile-percentile (P-P) plot shows the fraction of the observed daily values (horizontal axis) that are less than or equal to the p  percentile of the model data (vertical axis). 
Future period maximum daily temperatures derived from a selected climate model are adjusted based on these plots.
Source: WRI authors.

12  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
Figure 3  |  Daily maximum temperatures for Kolkata (2050–2070), derived from the selected model NorESM2-LM  
Notes: Temperatures of 40°C and higher are shaded pink. Panel A shows uncalibrated values; Panel B shows values adjusted according to the percentile-percentile calibration plots 
shown in Figure 2.
Source: WRI authors.
A
B

TECHNICAL NOTE   |  December 2023   |  13
Estimating future local climate hazard probabilities
Figure 3 plots the daily maximum temperature time series 
for 2050–70, as modeled by one of the three selected GCMs: 
NorESM2-LM. Panel a shows the raw output time series, and 
Panel b shows the corresponding calibrated time series, using 
the corresponding P-P plots of Figure 2 for calibration. Daily 
maximum temperatures of 40°C and higher are shaded pink. 
For each calendar year in 2050–70 and for each of the selected 
climate models, we determine whether that year experienced 
an excessive number of hot days as defined above. The number 
of such hot years, C, is modeled as the outcome of a binomial 
distribution with N = 21 years and unknown average annual rate 
parameter p. For the three selected climate models—NorESM2-
LM, ACCESS-ESM1-5, and MIROC-ES2L—the Kolkata 
hot year counts derived from the calibrated climate models for 
2050–70 are, respectively, C = 12, 18, and 15 years.
Using the probability structure described in “Estimates of 
climate hazard frequencies and their uncertainty,” the posterior 
probability distribution of the binomial rate parameter is a beta 
distribution with parameters 
Rather than being uncertainty distributions, these describe the 
binomial rate parameter for future event counts.
The future event count uncertainty is the beta-binomial distri-
bution described in “Estimates of climate hazard frequencies 
and their uncertainty,” with N = 21 and parameters 
         . Figure 4 shows the histogram 
of the beta-binomial distribution of predicted counts of future 
hot year occurrences, together with the corresponding mean 
predicted counts for the 21-year period 2050–70. We do 
this separately for each of three selected climate models. The 
histograms display the uncertainty of these predicted counts, 
reflecting our probability modeling assumptions. The three 
recalibrated climate models each produced different future-
period mean event counts: approximately 11.9 years, 17.7 years, 
and 14.8 years, respectively. Expressed as percentages of the 
21-year period, they are approximately 60 percent, 88 percent, 
and 74 percent.
Illustration: Estimation of predicted 
average number of extreme heat 
events in Kolkata
Using the same hazard definition, modeled temperature data, 
and calibration functions as above, we estimate a predictive dis-
tribution for the number of days per year where the maximum 
temperature exceeds 35°C in Kolkata each year for the 21-year 
period 2050–70.
For the selected calibrated climate model NorESM2-LM, the 
21 annual future-period hazard counts for the years 2050–70 
are [39, 1, 21, 5, 0, 0, 15, 0, 9, 13, 12, 10, 11, 5, 10, 2, 23, 5, 44, 
22, 18]. We take Hmin = 0 and Hmax as a specified plausible range 
for the annual hazard counts. With K = 10 histogram bins, 
Figure 4  |  Posterior distribution estimates of the frequency of hot years in Kolkata (2050–2070) for each of the three 
selected climate models
Notes: A hot year event is 10 or more days in a year with maximum temperatures equaling or exceeding 40°C. The frequency-weighted mean number of hot years, calculated from these 
histograms, are approximately 11.9 years, 17.7 years, and 14.8 years, for the three selected models, respectively. Expressed as percentages of the 21-year period, they are approximately 60 
percent, 88 percent, and 74 percent.
Source: WRI authors.

14  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
the corresponding histogram bin boundaries are [-2.44–2.44, 
2.44–7.33, 7.33–12.22, 12.22–17.11, 17.11–22.00, 22.00–26.89, 
26.89–31.78, 31.78–36.67, 36.67–41.56, 41.56–46.44]. Sorting 
the 21 annual counts into the 10 bins described above, we obtain 
the vector of bin frequencies [5, 3, 5, 2, 2, 2, 0, 0, 1, 1], summing 
to N = 21. The weighted average annual count, based on these 
histogram bin frequencies, is 12.57 hazard days per year, which 
is close to the raw average count of 12.61 events per year.
Following the Bayes probabilistic methodology described in 
“Prediction of average annual counts of hazard events,” we 
obtain the posterior Dirichlet-multinomial predictive distribu-
tion for the vector of 10 bin frequencies, conditional on the bin 
frequencies above, derived from the calibrated NorESM2-LM 
climate model. This represents the Bayes predictive distribution 
of the future-period histogram of annual hazard event counts. 
We simulate 10,000 sample vectors of bin frequencies from the 
predictive distribution. For each such sample of bin frequencies, 
we calculate the weighted-average annual hazard count, Hpred, 
as described in “Prediction of average annual counts of hazard 
events.” The variability exhibited by these 10,000 predicted aver-
age annual hazard counts represents the probabilistic uncertainty 
associated with this climate model’s estimate of the average 
annual hazard count.
Figure 5 exhibits the variability of the 10,000 simulated values, 
Hpred, of the weighted-average annual count of heat events at 
Kolkata for the period 2050–70, shown separately for each of 
the three selected temperature models for Kolkata.
Statistical summaries of these Hpred histograms are 
given in Table 2.
Figure 5  |  Histograms of predicted mean values of number of days per year with maximum temperature equaling or 
exceeding 40°C in Kolkata (2050–2070)
Source: WRI authors.
Source: WRI authors.
NORESM2-LM ACCESS-ESM1-5 MIROC-ES2L
Mean (days per year) 9.9 11.7 11.0
Standard deviation (days per year) 3.5 3.7 4.5
25th percentile (days per year) 7.4 9.1 7.7
Median (days per year) 9.8 11.5 10.6
75th percentile (days per year) 12.3 14.1 14.0
Table 2  |  Statistical summaries of predicted mean values

TECHNICAL NOTE   |  December 2023   |  15
Estimating future local climate hazard probabilities
Figure 6  |  Mean daily precipitation, by seasonal quarter, for a location in Nairobi, Kenya (1980–2014)
Notes: Observed values from ERA5 are shown in yellow. The values from the three best models, based on root-mean-square error calculated between modeled and observed data, are 
shown in red. 
Source: WRI authors.
Illustration: Nairobi drought
The second example looks at prolonged dry spell events in 
Nairobi, Kenya. The objective in this example is to estimate the 
number of dry spells consisting of 15 or more consecutive days 
with zero precipitation during the period 2050–70. The zero-
precipitation and 15-day thresholds were chosen for illustration 
purposes only; other minimum precipitation thresholds and 
minimum durations could be specified. 
Figure 6 shows the time series of seasonal mean daily precipita-
tion values for a location (latitude -1.28°, longitude 36.82°) in 
Nairobi, for the historical period 1980–2014. The observed series 
is plotted in yellow, and the series from the three best models, 
selected for low RMSE with the observed series, are plotted in 
red. These three best models are MRI-ESM2-0, IPSL-CM6A-
LR, and HadGEM3-GC31-MM.
Figure 7 shows the seasonal P-P calibration plots of modeled 
versus observed daily precipitation at Nairobi for the historical 
period 1980–2014. The three color-coded plots are for the three 
best-fitting climate models. Future modeled precipitation time 
series are recalibrated based on these plots (see “Climate model 
selection and calibration” and “Estimates of climate hazard 
frequencies and their uncertainty”).
Figure 8 shows the raw daily precipitation time series (Panel 
a) as well as the corresponding calibrated time series (Panel b) 
for 2050–70, output by the downscaled climate model MRI-
ESM2-0. This model’s historical daily precipitation differs 
the least from the observed data, using the matching criteria 
described in “Climate model selection and calibration.” The 
calibrated daily precipitation time series are scanned to obtain 
counts of the number of hazard event occurrences, which are 
runs of at least 15 days with zero precipitation. The dry spells 
are shaded pink in these time series plots. Panels c and d pres-
ent close-up views for a single year of daily precipitation data, 
providing clearer views of the dry spells. The dry spell counts 
from the calibrated time series are lower than those for the 
uncalibrated series because the climate models underpredicted 
daily rainfall amounts for the dry seasons during the historical 
calibration period.
The total counts, C, of dry spell events during 2050–70 
in Nairobi, as derived from the three best models, 
calibrated—MRI-ESM2-0, IPSL-CM6A-LR, and Had-
GEM3-GC31-MM—were, respectively, C = 4, 5, and 1. The 
count, C, is modeled probabilistically as the outcome of a Pois-
son random variable, with mean parameter r (see “Estimates of 
climate hazard frequencies and their uncertainty”). The resulting 
posterior distribution of the unknown Poisson parameter, r, is a 
unit-scaled gamma distribution with mean            .

16  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
Figure 7  |  Quarterly P-P plots for each of the selected climate models based on the marginal distributions of daily total 
precipitation in Nairobi (1980–2014)
Notes: A percentile-percentile (P-P) plot shows the fraction of the observed daily values (horizontal axis) that are less than or equal to the p  percentile of the model data (vertical axis). 
Future period daily precipitation values derived from the selected climate models are adjusted based on these plots.
Source: WRI authors.

TECHNICAL NOTE   |  December 2023   |  17
Estimating future local climate hazard probabilities
Figure 8  |  Daily precipitation for Nairobi, as modeled by one of the models selected for low historical deviation from 
observed values (2050–2070)
A
B

18  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
Notes: Dry spells (consecutive runs of days with zero precipitation) of at least 15 days are shaded pink. Panel A presents the uncalibrated time series. Panel B shows the calibrated time 
series and uses the seasonal calibration plots shown in Figure 6. Panel C (uncalibrated precipitation time series) and Panel D (calibrated precipitation time series) provide close-ups 
showing dry spells in 2052.
Source: WRI authors.
Figure 8  |  Daily precipitation for Nairobi, as modeled by one of the models selected for low historical deviation from 
observed values (2050–2070) (continued)
C
D

TECHNICAL NOTE   |  December 2023   |  19
Estimating future local climate hazard probabilities
The resulting predictive uncertainty distribution for the 
21-year dry spell count is the gamma-Poisson distribution with 
parameter a (see the method in “Estimates of climate hazard 
frequencies and their uncertainty”). This future-period count 
uncertainty is represented by the histograms for the selected 
climate models: MRI-ESM2-0, IPSL-CM6A-LR, and 
HadGEM3-GC31-MM (Figure 9). They describe the esti-
Notes: The mean predicted counts are 4.5, 5.5, and 1.5, respectively. HadGEM3-C31-MM has notably different dry spell count predictions than the other two selected climate models.
Source: WRI authors.
Figure 9  |  Predicted distributions for future Nairobi dry spell counts from the three downscaled climate models (2050–
2070)
mated probabilities of various dry spell counts over the specified 
21-year future period. The respective mean event counts are 4.5, 
5.5, and 1.5. Although HadGEM3-GC31-MM has a notably 
different dry spell count prediction than the other models, it was 
selected based on its fit to observed data during the historical 
period 1980–2015.2

20  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
APPLICATIONS
These methods are versatile and can be applied to a wide variety 
of decision domains. Below, we outline some domains in which 
we have either applied or contemplated applying them.
Agriculture. Crops and their pests have physiological tolerance 
ranges that lend themselves well to hazard definition in our 
method. For example, Pezzopane et al. (2008) estimate that 
an economically important cultivar of Coffea arabica requires 
2,887 degree-days above a 10.2°C base temperature between 
planting and harvest. We can define successful accumulation of 
these degree-days as a Bernoulli-modeled event and estimate 
the probability that this event occurs once per year. We intend 
to use this and related event definitions to support decision-
making in the agricultural supply chain as part of WRI’s 
AgriAdapt platform.
Energy planning. Degree-day calculations are frequently used 
in estimating capacity requirements and energy use in building 
heating and cooling systems. For example, the American Society 
of Heating, Refrigerating and Air-Conditioning Engineers pub-
lishes a set of standardized climate zones to be used in designing 
heating and cooling systems (ASHRAE 2021). The zones are 
defined in terms of degree-days and other climate indicators, all 
of which can be accommodated by our method.
Public health (heat waves). Researchers take numerous 
approaches to modeling heat and heat waves, many of which 
lend themselves well to our method. For example, Kim et al. 
(2023) find that deaths in Japan increase substantially when 
minimum nighttime temperatures stay at or above 25°C or the 
prefecture’s 95th percentile of minimum temperature. We can 
estimate probabilities of future hot night occurrences using 
threshold temperatures like these and the calculations detailed 
above in “Summary of steps to estimate future climate hazard 
event occurrence frequencies.”
Public health (infectious diseases). Some modes of disease trans-
mission are at least partially mediated by climate-sensitive 
factors. For example, Mordecai et al. (2017) find that mosquito-
borne arboviruses such as Zika, dengue, and chikungunya are 
most readily transmitted when the temperature is between 
26°C and 29°C. We can use temperature ranges like this to 
estimate the number of future high-risk days for transmitting 
these diseases.
Disaster risk reduction (landslides). The landslide hazard indicator, 
as defined in Emberson et al. (2020), includes two conceptual 
elements: landslide susceptibility—which arises from natural 
topography and substrate material (it does not include effects of 
human-made impervious surfaces)—and the amount of heavy 
rainfall in the past six days. Practically, it requires calculating the 
antecedent rainfall index (ARI), comparing ARI to the histori-
cal 95th percentile of ARI, and overlaying the ARI comparison 
on the susceptibility map.
For the Data Portal for Cities adaptation pilot, we obtained 
an ARI 95th percentile map and landslide susceptibility map 
from NASA’s Landslide Hazard Assessment for Situational 
Awareness (LHASA) project.3 We then calculated future ARI-
modeled precipitation time series and calculated a risk indicator 
as the number of days each year that a location with high sus-
ceptibility experiences ARI greater than its local 95th percentile.
Worker safety. More than 1 billion agricultural workers, road and 
construction crews, and other outdoor workers face health risks 
and even death from high-heat conditions (Ebi et al. 2021). 
Vecellio et al. (2022) find extended exposure to a wet-bulb 
globe temperature (Tw) of 30°C–31°C to be potentially lethal. 
Our method allows for estimation of future risk of worker 
illness and death or of constraints on agricultural and eco-
nomic productivity.
We use the Stull (2011) formula for Tw:
where RH is relative humidity expressed as a percent (e.g., “65” 
for “65 percent humidity”). For T, air temperature in degrees 
Celsius, we use maximum daily temperature. The ERA5 data set 
does not report RH, but it does report dewpoint temperature, 
Dp; thus, to calculate Tw for the observed data, first we calculate 
RH using this formula from Alduchov and Eskridge (1996):

TECHNICAL NOTE   |  December 2023   |  21
Estimating future local climate hazard probabilities
LIMITATIONS
These are some limitations of the hazard estimation methods:
Hazard indicator constraints. Our method for estimating counts 
of geographically localized future hazard events can only accom-
modate events whose occurrences are determined from the daily 
time series of four weather variables: minimum temperature, 
maximum temperature, daily precipitation, and daily average 
relative humidity.
Downscaled data limitations. Our downscaled climate models 
typically do not model land use and cannot distinguish urban 
land from rural land or wilderness. Our data may not, therefore, 
reflect factors not accounted for in the downscaling process, 
such as urban heat islands. 
Climate model selection. Different climate models will typically 
provide different estimated future occurrence counts for a 
prescribed hazard event at a chosen location. For conciseness, we 
show hazard estimates derived from a best model from each of 
three model families. Thus, after recalibration, remaining uncor-
rected model biases are not incorporated into the uncertainties 
reflected in model-specific prediction histograms. Model biases 
are not random errors.
There is no clear basis for combining estimates from differ-
ent selected models or to expect cancellation of model errors 
when model outputs are averaged. Therefore, predictions for the 
selected climate models are shown separately and compared.4 
When future hazard occurrence rate estimates from different 
models are similar, there is no real benefit in their combination; 
when they differ, it is best to exhibit the disagreement among 
climate model estimates.
Future greenhouse gas scenarios. We use climate model outputs 
derived from a particular future greenhouse gas emissions 
scenario. Different scenarios would yield different estimates for 
future hazard event occurrences.
Spatial resolution. We currently use models and historical 
observation data with spatial resolution of approximately 25–30 
km. This resolution is not sufficiently fine for many urban and 
agricultural decision-making applications. Our method does 
not depend on the resolution of the input data, so it should be 
applicable to higher-resolution data if they become available.
Model calibration. Future hazard estimates are derived from 
recalibrated time series and are conditional on our histori-
cally derived calibration plots of observed versus model data 
for the historical period 1980–2014. Calibration is only an 
approximation of how future model data will differ from future 
observational data. Calibration uncertainly is not evaluated, 
absent ensemble data from individual models. The calibra-
tions are based on matching marginal distributions rather than 
matching day-to-day values. 
Probabilistic modeling of prediction uncertainties. Inevitably, 
quantification of estimation uncertainty requires choosing 
a probability model as the data-generating mechanism (see 
“Estimates of climate hazard frequencies and their uncertainty”). 
Although the probability model used to characterize future 
hazard event uncertainty is adjusted to data, the appropriateness 
of the probability structure cannot be assured. 
Climate model biases. The uncertainties reflected in the distribu-
tion of future event counts that we exhibit do not reflect climate 
model biases introduced by incorrect assumptions of future 
greenhouse gas emissions or modeling errors resulting from 
incomplete specification of model dynamics. Even when climate 
models have shown small biases on larger geographic scales, they 
may still exhibit appreciable local biases. Our climate model 
selection and calibration are meant to reduce model bias for a 
historical period with available corresponding observations, but 
future biases may not be adequately corrected by methods based 
on past-data recalibration. 
Timescale. Model timescales seldom match the timescale of 
modeled phenomena. As a result, climate models and our 
analyses can fail to capture some climate dynamics and changes 
to the parameters of our probability models. Sensitivity analysis 
might be useful for determining whether different time-step 
lengths are important in understanding specific climate hazards 
in particular locations.

22  |  WOR LD RE SO UR CE S IN STIT UT EWOR LD RE SO UR CE S IN STIT UT E
  
ABBREVIATIONS
ARI  antecedent rainfall index 
CMIP6  Coupled Model Intercomparison Project   
  Phase 6 (CMIP6)
CSIRO  Commonwealth Scientific and Industrial   
  Research Organisation 
ESGF  Earth System Grid Federation
GCM  global climate model
GCoM  Global Covenant of Mayors for Climate and Energy
LHASA  Landslide Hazard Assessment for    
  Situational Awareness
NASA  National Aeronautics and Space Administration 
P-P  percentile-percentile
RMSE  root-mean-square error
SSP  Shared Socioeconomic Pathway
ENDNOTES
1. For more information about the ThinkHazard! tool, see https://
thinkhazard.org/en/.
2. The Python code used for these examples is available in Jupyter 
notebooks at the GitHub repository, https://github.com/wri/cities-
probabilistic-indicators/.
3. These data sets are available from the LHASA GitHub repository: 
https://github.com/nasa/LHASA.
4. See the discussion related to difficulties in combining predictions 
from climate models in Knutti et al. (2010) and the discussion on 
the question of model weighting in Wootten et al. (2023).
REFERENCES
Alduchov, O.A., and R.E. Eskridge. 1996. “Improved Magnus Form 
Approximation of Saturation Vapor Pressure.” Journal of Applied Me -
teorology and Climatology  35 (4): 601–9. https://doi.org/10.1175/1520-
0450(1996)035<0601:IMFAOS>2.0.CO;2.
Arnell, N.W. 2022. “The Implications of Climate Change for Emergency 
Planning.” International Journal of Disaster Risk Reduction  83 (Decem-
ber): 103425. https://doi.org/10.1016/j.ijdrr.2022.103425.
ASHRAE (American Society of Heating, Refrigerating and Air-Condi -
tioning Engineers). 2021. Climatic Data for Building Design Standards . 
Peachtree Corners, GA: ASHRAE. https://www.ashrae.org/file%20
library/technical%20resources/standards%20and%20guidelines/
standards%20addenda/169_2020_a_20211029.pdf.
Burillo, D., M.V. Chester, B. Ruddell, and N. Johnson. 2017. “Electricity 
Demand Planning Forecasts Should Consider Climate Non-stationar -
ity to Maintain Reserve Margins during Heat Waves.” Applied Energy  
206 (November): 267–77. https://doi.org/10.1016/j.apenergy.2017.08.141.
Ebi, K.L., A. Capon, P. Berry, C. Broderick, R. de Dear, G. Havenith, 
Y. Honda, et al. 2021. “Hot Weather and Heat Extremes: Health 
Risks.” Lancet 398 (10301): 698–708. https://doi.org/10.1016/S0140-
6736(21)01208-3.
ECMWF (European Centre for Medium-Range Weather Forecasts). 
2022. “ERA5: Data Documentation.” July 14. https://confluence.ecmwf.
int/display/CKB/ERA5%3A+data+documentation.
Emberson, R., D. Kirschbaum, and T. Stanley. 2020. “New Global Char -
acterisation of Landslide Exposure.” Natural Hazards and Earth System 
Science 20 (12): 3413–24. https://doi.org/10.5194/nhess-20-3413-2020.
Eyring, V., S. Bony, G.A. Meehl, C.A. Senior, B. Stevens, R.J. Stouffer, 
and K.E. Taylor. 2016. “Overview of the Coupled Model Intercompari -
son Project Phase 6 (CMIP6) Experimental Design and Organiza -
tion.” Geoscientific Model Development  9 (5): 1937–58. https://doi.
org/10.5194/gmd-9-1937-2016.
GCoM (Global Covenant of Mayors for Climate and Energy). 2018. 
Global Covenant of Mayors Common Reporting Framework . Version 6.1. 
Brussels: GCoM Secretariat. https://www.globalcovenantofmayors.
org/wp-content/uploads/2019/04/FINAL_Data-TWG_Reporting-
Framework_website_FINAL-13-Sept-2018_for-translation.pdf.
GCoM. 2023. (Database.) Data Portal for Cities . https://dataportal -
forcities.org/. Accessed on 21 November 2023.
Holmgren, E.B. 1995. “The P-P Plot as a Method for Comparing Treat -
ment Effects.” Journal of the American Statistical Association 90 (429) 
360–5. https://doi.org/10.1080/01621459.1995.10476520.

TECHNICAL NOTE   |  December 2023   |  23
Estimating future local climate hazard probabilities
Iturbide, M., J. Fernández, J.M. Gutiérrez, J. Bedia, E. Cimadevilla, J. 
Díez-Sierra, R. Manzanas, et al. 2022. “Implementation of FAIR Prin -
ciples in the IPCC: The WG1 AR6 Atlas Repository.” Scientific Data  9 
(629). https://doi.org/10.1038/s41597-022-01739-y.
Kim, S.E., M. Hashizume, B. Armstrong, A. Gasparrini, K. Oka, Y. 
Hijioka, A.M. Vicedo-Cabrera, and Y. Honda. 2023. “Mortality Risk of 
Hot Nights: A Nationwide Population-Based Retrospective Study in 
Japan.” Environmental Health Perspectives  131 (5): 057005. https://doi.
org/10.1289/EHP11444.
Knutti, R., R. Furrer, C. Tebaldi, J. Cermak, and G.A. Meehl. 2010. “Chal -
lenges in Combining Projections from Multiple Climate Models.” Jour -
nal of Climate 23 (10): 2739–58. https://doi.org/10.1175/2009JCLI3361.1.
Kuma, P., F.A.-M. Bender, and A.R. Jönsson. 2023. “Climate Model 
Code Genealogy and Its Relation to Climate Feedbacks and Sen -
sitivity.” Journal of Advances in Modeling Earth Systems 15 (7): 
e2022MS003588. https://doi.org/10.1029/2022MS003588.
Moda, H.M., W.L. Filho, and A. Minhas. 2019. “Impacts of Climate 
Change on Outdoor Workers and Their Safety: Some Research Priori -
ties.” International Journal of Environmental Research and Public Health  
16 (18): 3458. https://doi.org/10.3390/ijerph16183458.
Mordecai, E.A., J.M. Cohen, M.V. Evans, P. Gudapati, L.R. Johnson, C.A. 
Lippi, K. Miazgowicz, et al. 2017. “Detecting the Impact of Temperature 
on Transmission of Zika, Dengue, and Chikungunya Using Mecha -
nistic Models.” PLoS Neglected Tropical Diseases 11 (4): e0005568. 
https://doi.org/10.1371/journal.pntd.0005568.
NASA (National Aeronautics and Space Administration). 2023. “NASA 
Earth Exchange Global Daily Downscaled Projections (NEX-GDDP-
CMIP6).” August 27. https://www.nccs.nasa.gov/sites/default/files/
NEX-GDDP-CMIP6-Tech_Note.pdf.
Nasr, A., I. Björnsson, D. Honfi, O.L. Ivanov, J. Johansson, and E. Kjell -
ström. 2021. “A Review of the Potential Impacts of Climate Change 
on the Safety and Performance of Bridges.” Sustainable and Resil -
ient Infrastructure  6 (3–4): 192–212. https://doi.org/10.1080/23789
689.2019.1593003.
Ngonghala, C.N., S.J. Ryan, B. Tesla, L.R. Demakovsky, E.A. Mordecai, 
C.C. Murdock, and M.H. Bonds. 2021. “Effects of Changes in Tem -
perature on Zika Dynamics and Control.” Journal of the Royal Society 
Interface 18 (178): 20210165. https://doi.org/10.1098/rsif.2021.0165.
Pezzopane, J.R.M., M.J.P. Júnior, M.B.P. de Camargo, and L.C. Fa -
zuoli. 2008. “Exigência térmica do café arábica cv. Mundo Novo no 
subperíodo florescimento-colheita.” Ciência e Agrotecnologia  32 (6): 
1781–86. https://doi.org/10.1590/S1413-70542008000600016.
Riahi, K., D.P. van Vuuren, E. Kriegler, J. Edmonds, B.C. O’Neill, S. Fuji -
mori, N. Bauer, et al. 2017. “The Shared Socioeconomic Pathways and 
Their Energy, Land Use, and Greenhouse Gas Emissions Implications: 
An Overview.” Global Environmental Change 42: 153–68. https://doi.
org/10.1016/j.gloenvcha.2016.05.009.
Rocklöv, J., and Y. Tozan. 2019. “Climate Change and the Rising Infec -
tiousness of Dengue.” Emerging Topics in Life Sciences 3 (2): 133–42. 
https://doi.org/10.1042/ETLS20180123.
Sanderson, B.M., M. Wehner, and R. Knutti. 2017. “Skill and Inde -
pendence Weighting for Multi-model Assessment.” Geoscien -
tific Model Development 10 (6): 2379–95. https://doi.org/10.5194/
gmd-10-2379-2017.
Schwalm, C.R., S. Glendon, and P.B. Duffy. 2020. “RCP8.5 Tracks 
Cumulative CO2 Emissions.” Proceedings of the National Academy of 
Sciences of the United States of America 117 (33): 19656–57. https://doi.
org/10.1073/pnas.2007117117.
Stull, R. 2011. “Wet Bulb Temperature from Relative Humidity and Air 
Temperature.” Journal of Applied Meteorology and Climatology  50 (11): 
2267–69. https://doi.org/10.1175/JAMC-D-11-0143.1.
Thornton, P.K., P.J. Ericksen, M. Herrero, and A.J. Challinor. 2014. 
“Climate Variability and Vulnerability to Climate Change: A 
Review.” Global Change Biology  20 (11): 3313–28. https://doi.
org/10.1111/gcb.12581.
Vecellio, D.J., S.T. Wolf, R.M. Cottle, and W.L Kenney. 2022. “Evaluating 
the 35°C Wet-Bulb Temperature Adaptability Threshold for Young, 
Healthy Subjects (PSU HEAT Project).” Journal of Applied Physiology  
132 (2): 340–45. https://doi.org/10.1152/japplphysiol.00738.2021.
Wang, W., S. Yang, H.E. Stanley, and J. Gao . 2019. “Local Floods Induce 
Large-Scale Abrupt Failures of Road Networks.” Nature Communica -
tions 10 (May): 2114. https://doi.org/10.1038/s41467-019-10063-w.
Wootten, A.M., E.C. Massoud, D.E. Waliser, and H. Lee. 2023. “As -
sessing Sensitivities of Climate Model Weighting to Multiple Meth -
ods, Variables, and Domains in the South-Central United States.” 
Earth System Dynamics 14 (1): 121–45. https://doi.org/10.5194/
esd-14-121-2023.
World Bank. n.d. (Database.) Climate Change Knowledge Portal . 
https://climateknowledgeportal.worldbank.org/. Accessed No -
vember 20, 2022.

Copyright 2023 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License.  
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
We are pleased to acknowledge our institutional strategic partners 
that provide core funding to WRI: the Netherlands Ministry of 
Foreign Affairs, Royal Danish Ministry of Foreign Affairs, and Swedish 
International Development Cooperation Agency. 
We also acknowledge the Global Covenant of Mayors for Climate and 
Energy, the Walmart Foundation, and Bloomberg Philanthropies. 
ABOUT THE AUTHORS
Theodore Wong  is a Research and Project Associate at WRI Ross 
Center for Sustainable Cities. 
Contact: ted.wong@wri.org
Paul Switzer  is Stanford University Professor Emeritus of Statistics 
and Earth System Science. 
Contact: switzer@stanford.edu
