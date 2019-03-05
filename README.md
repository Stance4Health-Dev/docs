

## Abstract

[Stance4Health](http://www.stance4health.com/) is an [European Union’s Horizon 2020 project](https://cordis.europa.eu/project/rcn/218510/factsheet/es) which fosters a global ecosystem while enabling collection, management, and analysis of healthcare and feeding data, with the aim of developing a **Smart Personalized Nutrition** service, based on food production that will optimize the gut microbiota activity.
It will be tailored to different target groups, from healthy children and adults to children with coeliac disease or food allergy,
as well as overweight children and adults, which will have an impact on the development of NCDs such as obesity or type 2 diabetes.
The specific personalised nutrition tools developed along Stance4Health will be based on robust scientific evidence and knowledge
from different fields like nutrition, medicine, food sciences, microbiology, computer sciences, and social sciences and humanities
like economics, marketing, psychology and social anthropology.

In this document you can see how the project is being implemented, what technologies will be used, what programming technique is most appropriate, and
how the data will be treated in terms of management and migration.
This repository was created with the purpose of collecting information for the development of Stance4Health.  

## How will be the development experience: Continuous Integration

How are developers going to be organized to implement the system? using continuous integration.
In a development based on continuous integration, the workers/developers who are implementing the system share their work together, pooling it in common with the rest of the members, in an **automatic** and **systematized** way.
The development is continuous because each worker pools his work in common constantly, every time he fixes a bug, implements a new feature or some characteristic.
You can implement CI without using third-party tools, but it becomes very tedious. Because we need to take control of source code, manage the versions, perform unit tests, etc. For this there are services that can help us, such as the **git version control system**, which is what we use for the project. Then, thanks to its use, the development becomes systematized.
The development of the project advances through changes, these changes are the modifications we make to the files within the version control system and  published later, **commit**, so the repository is updated. We can also bring the changes, that some of the members made, of the repository to have our workspace always updated.
Git keeps information about what has been modified, who modified it, when it was modified and in some cases why it was modified. In this way, we have a history of all the changes that are presented in the project, allowing us to interact with the versions and go back if something went wrong.
What can we keep in a version control system? mainly the source code is saved, however it is not the only thing, we can store anything digital, for example images, icons, sound, videos, binary files, libraries, and even the same project documentation, from which you are reading.
The git version control allows us to work on a copy of the main project, without connection, in local. This makes it much faster than other alternatives such as SVS, Perfoce or Mercurial, among others. For example, Mercurial uses commands that need the server to be completed, however, git can do a  **fetch** to get the repository information and then work offline, allowing comparisons **merge** and see the **logs** from your branch or from the rest of the branches of the repository, even if they do not belong to your local branches.

## Test-driven development: all code emerged is tested

Test-driven development is the programming technique used to develop the system. This technique includes:

- First implement the tests.
- Refactoring: eliminate duplicate code, unnecessary dependencies.

This technique gives us certain advantages, such as minimizing errors, implementing software functionalities, producing modular software, among others.
To improve efficiency and test times, automatic tests are often used. Advantages:

- Execute a mayor number of tests.
- Greater frequency of tests.
- Greater depth of the tests.

### Using Travis CI

> Developing..

### Battery of tests

It is important to have a sample list that is very complete, concrete and unambiguous.
List of actions focused on passing the tests:
- ...
- ...

### Some classic vulnerabilities to consider

- Fuzzing: massive entry of random data to the entry points of the system. Ex: negative numbers, very large numbers, urls, html text, etc.
- SQL injection: unauthorized requests to databases.
- XSS: injection of malicious javascritp code. Ex: web based applications.

## Python as data management

The system needs to handle a lot of information constantly, therefore, we have chosen the Python programming language as the main development language. Python is an interpreted language, slower than others, like C ++, but you only need one interpreter to run it, which makes it cross-platform. In addition, it comes pre-installed in many systems like Linux or Mac.
It is multi-paradigm, unlike other languages ​​such as [R](https://www.r-project.org/), can be oriented to different needs, such as object-oriented programming, modular development, functional programming and scripts. These scripts can be used for system administration tasks, tests, correction of errors and direct interaction with the database, among other usefull uses.

It is opensource and is supported by a large community that continues to develop libraries and modules that facilitate our work. Many of these
libraries are oriented to massive data computing ([Awesome Python](https://github.com/vinta/awesome-python)).

Python has a very broad and easy to read syntax, similar to pseudocode. It allows to easily manipulate data in a table way.
It is not necessary to declare the type of variable, depending on the content that a variable takes, it is of one type or another, this gives more flexibility when it comes to processing different types of data.

### Python 2.x vs 3.x

Both versions are incompatible, so we have chosen version 3.x for the development because it is the most recent version (3.6 2016) compared to
the latest version 2.x (2.7 2010), which will also no longer have support next year.
Most of the 2.x libraries are already available in 3.x, in the following [link](https://python3wos.appspot.com/) we can see some of those that are not available in red color.

## Use Cases: Using Personas
Personas bring us a tool that allows to create models that represent a user or group of users focused on a specific activity. With the publication in 1998 of the book 'The Inmates Are Running the Asylum', [Alan Cooper](https://twitter.com/MrAlanCooper) begins his approach towards what we know as Personas today.
Personas [4,5,6] is a practical way to design the interaction and user experience with the system. It is a good option when we have a complex design, since it allows to differentiate without ambiguities between the functionalities and requirements that are necessary and those that are not.
Users tend to be divided according to three criteria:
- Goals.
- Chores.
- Skill level.

There are different criteria and ways to represent a future user, let's see an example:

|        ![Alt text](http://icons.iconarchive.com/icons/icons8/windows-8/48/Users-Name-icon.png)    |                         	
         Sofía Morales 	                         |
|----------------|-------------------------------|
|Vital statistics|24 years, Female, Puertollano, Spain           |
|Diseases        |Celiac           				 |
|Job          	 |Nurse. Actually working with cancer patients.	 |
|Queries         | <ul><li>Usually she buys the same products that she already knows are gluten free.</li><li>Quick access to a database that allows to verify components of products.</li><li>Discover new recipes suitable for her</li><li>Notification of new free gluten restaurants</li></ul>  |
|Links          	 |<ul><li>[Ranked the 10 best Spanish cities to eat gluten-free](http://www.infoceliaco.com/index.php/restaurantes/3338-clasifican-las-10-mejores-ciudades-espanolas-para-comer-sin-gluten)</li><li>[Ciudad Real [ESP] - Bars per inhabitant](https://www.lanzadigital.com/provincia/ciudad-real/ciudad-real-bares-habitante/)</i></ul>|


You can find here more [user stories](https://github.com/Stance4Health-Dev/docs/tree/master/user-stories) of the system, intented to get the prerequisites and needs of the future application.

[4] Cooper, A. 1999. The Inmates Are Running the Asylum,
Indianapolis, Sams.
[5] Cooper A., Reimann R., Cronin, D. 2007. About Face 3: The
Essentials of Interaction Design. Indianapolis, Wiley.
[6] Cooper A. 2003. The Origin of Personas. Retrieved June 12,
2008, from http://www.cooper.com/journal/2003/08/the_origin_of_personas.html


## Database

> Developing..

- Sources: idioma y licencia.
- Migracion: como obtenemos los datos, que medios usamos, como los almacenamos.
- Standard: SPN, Nutricion inteligente Personalizada

At the moment, you can find information about:

- [Representation of Food Composition databases](https://github.com/Stance4Health-Dev/docs/tree/master/data-representation) like [FDA](https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/nutrient-data-laboratory/docs/sr28-download-files/), [Open Food Facts](https://world.openfoodfacts.org/), [Intake24](https://intake24.co.uk/) and so on.


### Migration

> Developing..

## Convenio Europeo

> Translating..

Reglamento (UE) 1169/2011 [.pdf](https://www.boe.es/doue/2011/304/L00018-00063.pdf)

- Valores de referencia de nutrientes.
- Tablas Expresión y representación de los nutrientes.
- Tablas factor de conversión para cálculo energético por nutriente.
- Dieta ideal 2000kcal dividido en nutrientes.
