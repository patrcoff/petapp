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
- 