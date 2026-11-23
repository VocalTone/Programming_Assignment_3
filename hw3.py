import data
import build_data
from data import CountyDemographics



# purpose: return the total 2014 population of all supplied counties
# input: a list of CountyDemographics objects
# output: the total population as an integer
def population_total(counties: list[CountyDemographics]) -> int:
    total = 0
    for county in counties:
        total += county.population['2014 Population']
    return total



# purpose: return all counties belonging to the specified state
# input: a list of counties and a state abbreviation
# output: a list of matching CountyDemographics objects
def filter_by_state(counties: list[CountyDemographics],
                    state: str) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.state == state:
            result.append(county)
    return result




# purpose: calculate the estimated population with the specified education level
# input: a list of counties and an education dictionary key
# output: the estimated population as a float
def population_by_education(counties: list[CountyDemographics],
                            key: str) -> float:
    total = 0
    for county in counties:
        if key in county.education:
            total += county.population['2014 Population'] * \
                     county.education[key] / 100
    return total


# purpose: calculate the estimated population belonging to the specified ethnicity
# input: a list of counties and an ethnicity dictionary key
# output: the estimated population as a float
def population_by_ethnicity(counties: list[CountyDemographics],
                            key: str) -> float:
    total = 0
    for county in counties:
        if key in county.ethnicities:
            total += county.population['2014 Population'] * \
                     county.ethnicities[key] / 100
    return total


# purpose: calculate the estimated population below the poverty level
# input: a list of counties
# output: the estimated population below poverty level as a float
def population_below_poverty_level(
        counties: list[CountyDemographics]) -> float:
    total = 0
    for county in counties:
        if 'Persons Below Poverty Level' in county.income:
            total += county.population['2014 Population'] * \
                     county.income['Persons Below Poverty Level'] / 100
    return total



# purpose: calculate the overall percentage with the specified education level
# input: a list of counties and an education dictionary key
# output: the population-weighted percentage as a float
def percent_by_education(counties: list[CountyDemographics],
                         key: str) -> float:
    total = population_total(counties)
    if total == 0:
        return 0
    return population_by_education(counties, key) / total * 100


# purpose: calculate the overall percentage belonging to the specified ethnicity
# input: a list of counties and an ethnicity dictionary key
# output: the population-weighted percentage as a float
def percent_by_ethnicity(counties: list[CountyDemographics],
                         key: str) -> float:
    total = population_total(counties)
    if total == 0:
        return 0
    return population_by_ethnicity(counties, key) / total * 100


# purpose: calculate the overall percentage below the poverty level
# input: a list of counties
# output: the population-weighted poverty percentage as a float
def percent_below_poverty_level(
        counties: list[CountyDemographics]) -> float:
    total = population_total(counties)
    if total == 0:
        return 0
    return population_below_poverty_level(counties) / total * 100



# purpose: return counties whose education percentage is greater than a threshold
# input: a list of counties, an education key, and a numeric threshold
# output: a list of matching CountyDemographics objects
def education_greater_than(counties: list[CountyDemographics],
                           key: str,
                           threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if key in county.education and county.education[key] > threshold:
            result.append(county)
    return result


# purpose: return counties whose education percentage is less than a threshold
# input: a list of counties, an education key, and a numeric threshold
# output: a list of matching CountyDemographics objects
def education_less_than(counties: list[CountyDemographics],
                        key: str,
                        threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if key in county.education and county.education[key] < threshold:
            result.append(county)
    return result


# purpose: return counties whose ethnicity percentage is greater than a threshold
# input: a list of counties, an ethnicity key, and a numeric threshold
# output: a list of matching CountyDemographics objects
def ethnicity_greater_than(counties: list[CountyDemographics],
                           key: str,
                           threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if key in county.ethnicities and county.ethnicities[key] > threshold:
            result.append(county)
    return result


# purpose: return counties whose ethnicity percentage is less than a threshold
# input: a list of counties, an ethnicity key, and a numeric threshold
# output: a list of matching CountyDemographics objects
def ethnicity_less_than(counties: list[CountyDemographics],
                        key: str,
                        threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if key in county.ethnicities and county.ethnicities[key] < threshold:
            result.append(county)
    return result


# purpose: return counties whose poverty percentage is greater than a threshold
# input: a list of counties and a numeric threshold
# output: a list of matching CountyDemographics objects
def below_poverty_level_greater_than(
        counties: list[CountyDemographics],
        threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] > threshold:
            result.append(county)
    return result


# purpose: return counties whose poverty percentage is less than a threshold
# input: a list of counties and a numeric threshold
# output: a list of matching CountyDemographics objects
def below_poverty_level_less_than(
        counties: list[CountyDemographics],
        threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] < threshold:
            result.append(county)
    return result 
