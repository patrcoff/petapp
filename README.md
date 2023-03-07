# petapp
An app for managing purchasing and administering of pet medications (backend)

I am currently deciding on a license to use for this project, it is currently not officially open source. Feel free to read the code but technically you shouldn't use it until I have uploaded a specific license.

This branch is for pursuing a fresh approach using fast api.

We'll use the readme for planning purposes at this point in the project, it will later be moved out and a proper readme written in its place.

Whitepaper:

The main purpose of this project is to provide a backend for an app (web app / mobile) which allows the user to manage the purchasing and administering of pet medications. It will provide the functionality to add/edit pets under the users account, add medications along with metadata such as dosages, strength, frequency of dosage. As well as this, the user will be able to track their purchases (and thus stock) of the medications, as well as log when they administer it to their pets, leave notes about general wellfair, plan/schedule future purchasing and administering of medications and set up reminders for both. This would be the MVP, future versions may expand upon this adding additional functionality and broader areas such as food, toys and other pet consumables.

Main functionality required:

- Sign up (user)
- Register pets
- edit pet details
- Add pets to shared group (for sharing pets with another user i.e. your partner)
- Add medications
- Add medication application data (i.e. dosage, frequency, method etc) of a specific medication to a specific pet
- Add reminders to purchase / apply medications
- log when medication is actually applied
- View stock and predict when they will run out
- View calendar of when next applications should be
- Take general health notes about a pet (can be used when going to vets to produce a summary) (can we add in the vaccinations by barcode from the vetenary system - is this open data?)
- 

Potential future versions functionalities:

- log walking, trips to park, specific acitivites and excercises (related to species and breed)
- add equivilent tracking functionality for food stock and portioning
    - within this, provide predictions as to when food  will run out and needs purchased by
    - suggest if pets are being over/under fed
    - log treats
    - suggest nutritional advice
- add a general budgeting portion of the app which logs all pet based spending 
- pet birthdays
- tasteful handling of pet deaths
- pet relationships (i.e. parents, siblings etc)
- 

Version 1.0
===========

Data:

Users
    username
    email
    fullnames
    (do we really need any further PII? I would prefer to minimise this at this time as I'm not in the business of selling data)

Pets
    Species
        Breeds
    Name
    Age
    Colour
    Description
    sizes
    weight
    Conditions
    Other medical notes
    pictures

    all of the above about specific pets

    general metadata of some of the above about the species and breeds, obtained from some external data source(s)

Medications
    brand
    name
    type
    description
    active ingredient(s)
    dosage qty
    dosage unit
    active ingredient units per dosage

Actions
    schedules
    dosage to pet links
    log events
    share history (report for vets)
    calendar sync with google calendar etc (this may be handled at frontend)
    set reminders




Example pets to prompt thoughts on the data structures needed to encompase a wide variety of animals

Oliver, dog, setter/retriever cross, 17.6kg, 1 year old, ginger, 
    flea and tic treatment, 15ml drops, apply on back of neck, monthly, 3 in stock, next applied 30th March
    wormer, pill, note:give burried in food, unit: each, 1, 5 in stock, next applied 30th March

Jeffry, fish, clownfish, 15cm, 3 years old, orange, 
    anti-fish-mite treatment, drops, 1ml, monthly, apply to tank, 2 in stock, next applied 30th March

Bird

Cat

Reptile



External functions examples:
    stock of superpetdrug x: 10 units, next application 30th march, doses to be applied on next application, 7, remaining stock after next application: 3, to purchase: before 30th April, auto-reminder: true





tables:

USERS: ID, USERNAME, NAME, PREMIUM(CURRENTLY_UNUSED), AGE(?), DISABLED, 


SPECIES: ID, SPECIES_NAME, DESCRIPTION, AVERAGE_LIFE_SPAN, AVERAGE_SIZE, AVERAGE_WEIGHT

BREED: ID, SPECIES_ID, BREED_NAME, AVERAGE_LIFE_SPAN, AVERAGE_SIZE, AVERAGE_WEIGHT, HAIR TYPE

BREED_SIZE: ID, BREED_ID, BREED_SIZE_NAME, MIN_HEIGHT, MAX_HEIGHT, MIN_LENGTH, MAX_LENGTH (EXAMPLES: LARGE_DOG, SMALL_CAT)

PET: ID, NAME, AGE, SPECIES, MAIN_BREED (RELATION:BREED), SECONDARY_BREED (RELATION:BREED), COLOUR, AGE_NEUTERED, HAS_BRED,

SIBLINGS: ID, PET1, PET2, RELATIONSHIP (OF 2 IS TO 1, I.E. NIECE)


OWNERSHIP_GROUP: ID, NAME, CREATOR, PICTURE, DESCRIPTION

OWNERSHIP_GROUP_MEMBERSHIP: ID, OWNERSHIP_GROUP_ID, MEMBER_ID, CAN_EDIT_PETS

PET_OWNERSHIP: ID, PET_ID, OWNERSHIP_GROUP_ID





ACCESS RULES - USER IS MEMBER OF OWNERSHIP_GROUP X, PET Y IS IN OWNERSHIP_GROUP X, USER CAN VIEW PET Y


CONSIDERATIONS - SOME DATA IS USER GENERATED AND SOME IS PRE-POPULATED. SHOULD SOME USER DATA BE JSON INSTEAD OF TABULAR, FOR EXAMPLE, MEDICATION INFO
RE THAT PODCAST EPISODE I LISTENED TO RECENTLY (I THINK TALK PYTHON TO ME) ABOUT STORING JSON INSIDE A RELATIONAL DB 