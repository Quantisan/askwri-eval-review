Goal: 

Build eval query sets for a cross-lingual RAG system
* 207-doc corpus
* 169 en, rest zh/es/pt). 
* Queries always written in English regardless of source doc language. 


Method: 
Working one document (or twin-pair) at a time: 
* read doc. 
* manually generate high-level English queries whose expected answer is this
document 
* This document's `document_id` is useful for `Cite` mode.
* Write draft answers to the questions as well. 
    * This will be useful in the future for evaluation of `Answer` mode. 
* Do not attempt to capture chunks or excerpts at this stage. 

--

### doc review 1

```
document_id: 00be4a1d-33cc-4b56-a4d5-d15af0a5cc27
external_id: 2025_zero-emission-heavy-duty-trucks_00015
title: 驶向2035: 中国新能源重卡在区域与长途运输场景中的推广潜力研究
language: zh
```

Possible English twin: 
7c2e200e-9c01-4acd-b5ef-a18041a7f258
"Charging toward 2035: Policies to accelerate zero-emission heavy-duty trucks in China's regional and long-haul freight" (en)

Query: "What is the projected market penetration rate of new energy heavy-duty trucks in China through 2035?"
* There are three scenarios -- no policy, current policy, and enhanced policy. 
* No-policy scenario: regional transport reaches 2%–17% penetration by MY2030; long-haul stays at a nascent, low level all the way through MY2035.
* Current-policy scenario: the trade-in subsidy lifts long-range BEV semi-tractor penetration in regional transport to ~10% by MY2027.
* Enhanced-policy scenario (current + enhanced combined): regional transport penetration exceeds 50% during MY2027–2030; long-haul growth stays slow until a sharp acceleration in MY2032–2035, implying sustained policy support is needed through 2035 for long-haul to reach meaningful levels.

Query: "How does total cost of ownership compare between battery electric and diesel heavy-duty trucks in China?"
* BEVs are more cost-competitive than diesel in regional transport and are projected to dominate there.
* The TCO/capex gap is larger for heavy cargo trucks (载货汽车) than for semi-tractors, because cargo trucks suffer bigger payload losses and diesel cargo trucks already have lower baseline purchase/energy costs.
* Concrete capex gap (short-range BEV vs. diesel heavy truck): CNY 150k–260k (MY2027) narrows to CNY 35k–120k with the trade-in subsidy, then widens back above CNY 130k once that subsidy ends in 2028, not dropping below CNY 100k again until MY2030.

Query: "What is the difference in zero-emission truck adoption potential between regional transport and long-haul transport scenarios?"
* Regional transport moves much faster toward competitiveness: BEV semis hit a 5-year payback by MY2027 with subsidies, and penetration crosses 50% by MY2027–2030 under enhanced policy.
* Long-haul lags substantially: nascent under no-policy through MY2035; even with enhanced policy, real growth only emerges MY2032–2035.
* Technology split also differs: BEVs dominate regional transport; in long-haul, BEVs work best for shorter-daily-mileage, low-time-sensitivity, light-cargo routes, while fuel-cell trucks (FCEVs) are more competitive for long-daily-mileage, time-sensitive, heavy-cargo routes.

Query: "What are the payback periods for battery electric semi-trucks compared to diesel trucks in China?"
* The study defines competitiveness thresholds as ≤5-year payback for regional transport and ≤4-year payback for long-haul. 
* With the trade-in subsidy, long-range BEV semi-tractors reach the 5-year payback threshold by MY2027 — three years earlier than the no-policy case.
* The vehicle purchase-tax exemption alone is not enough to make BEV semis competitive during MY2025–2027.
* In long-haul, by MY2035 both BEV and FCEV heavy cargo trucks on shorter-daily-mileage routes approach roughly a 5-year payback. 


### doc review 2

98cc253e — "How Dockless Bike Sharing Affects Cities"

```
document_id: 98cc253e-8d96-4499-b67a-38baffe2f3f2
external_id: 2020_dockless-bike-sharing_00124
title: 共享单车如何影响城市
language: zh
```

possible english twin: 
416a01af-1c79-4db1-a356-182f0577f844 
"How Dockless Bike Sharing Changes Lives: An Analysis of Chinese Cities" (en)

Queries
* "What share of bike-share trips replace private car, taxi, or ride-hailing trips in China?"
* "How much CO2 emissions reduction is attributed to bike-sharing in China?"
* "How does dockless bike-sharing affect travel behavior in Chinese cities?"

expected_documents: {98cc253e-8d96-4499-b67a-38baffe2f3f2, 416a01af-1c79-4db1-a356-182f0577f844}

Query: "What share of bike-share trips replace private car, taxi, or ride-hailing trips in China?"
* Based on survey data from 8,218 bike-share users across 12 Chinese cities.
* 54% of bike-share users use bike-sharing to connect with other transport modes; of those, 91% of that connecting use is to link with public transit.
* Across the 12 cities, 17%–45% of bike-share trips replaced private motorized trips — including private cars, taxis, ride-hailing, and motorcycles.

Query: "How much CO2 emissions reduction is attributed to bike-sharing in China?"
* Most bike-share trips substitute for walking or public transit trips (not emissions-reducing), but the portion that substitutes for private motorized trips does reduce emissions.
* That substitution effect reduces CO2 emissions by approximately 4.8 million tonnes per year.
* The report frames this as equivalent to the annual CO2 absorption of about 6.8 million acres of forest.

Query: "How does dockless bike-sharing affect travel behavior in Chinese cities?"
* The study found high consistency in travel-behavior effects across all 12 cities, despite differing economic/social development levels.
* 54% of users ride to connect with other transport modes, primarily public transit (91% of connecting trips).
* 17%–45% of bike-share trips (varying by city) displace private motorized trips (cars, taxis, ride-hailing, motorcycles).
* Overall, the report frames bike-sharing as a "last-mile" solution that both strengthens public transit connectivity and substitutes for short private-vehicle trips — changing the broader urban mobility ecosystem, not just individual trip choices.


