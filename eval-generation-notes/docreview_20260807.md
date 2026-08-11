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

