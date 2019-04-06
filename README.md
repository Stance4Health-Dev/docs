## Index
- [Abstract](#Abstract)
- [How will be the development experience](#Continuous-Integration)
- [Test-driven development](#Test-driven-development)
  * [Using Travis CI](#Using-Travis-CI)
  * [Battery of tests](#Battery-of-tests)
  * [Classic vulnerabilities](#Some-classic-vulnerabilities-to-consider)
- [Python as data management](#Python-as-data-management)
  * [Python 2.x vs 3.x](#Python-2.x-vs-3.x)
- [Use Cases: Using Personas](#Using-Personas)
- [Database](#Database)
  * [Graph Database](#Graph-Database)
  * [Migration](#Migration)
- [References](#References)

<a name="Abstract"/>

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

➤ [Index](#Index)

<a name="Continuous-Integration"/>

## How will be the development experience: Continuous Integration (CI)

How are developers going to be organized to implement the system? using continuous integration.
In a development based on continuous integration, the workers/developers who are implementing the system share their work together, pooling it in common with the rest of the members, in an **automatic** and **systematized** way. The development is continuous because each worker pools his work in common constantly, every time he fixes a bug, implements a new feature or some characteristic.

You can implement CI without using third-party tools, but it becomes very tedious. Because we need to take control of source code, manage the versions, perform unit tests, etc. For this there are services that can help us, such as the **git version control system**, which is what we use for the project. Then, thanks to its use, the development becomes systematized.
The development of the project advances through changes, these changes are the modifications we make to the files within the version control system and  published later, **commit**, so the repository is updated. We can also bring the changes, that some of the members made of the repository to have our workspace always updated. Git keeps information about what has been modified, who modified it, when it was modified and in some cases why it was modified. In this way, we have a history of all the changes that are presented in the project, allowing us to interact with the versions and go back if something went wrong.

What can we keep in a version control system? mainly the source code is saved, however it is not the only thing, we can store anything digital, for example images, icons, sound, videos, binary files, libraries, and even the same project documentation, from which you are reading.

The git version control allows us to work on a copy of the main project, without connection, in local. This makes it much faster than other alternatives such as Subversion (SVN), Perforce or Mercurial, among others. For example, Mercurial uses commands that need the server to be completed, however, git can do a  **fetch** to get the repository information and then work offline, allowing comparisons **merge** and see the **logs** from your branch or from the rest of the branches of the repository, even if they do not belong to your local branches.

➤ [Index](#Index)

<a name="Test-driven-development"/>

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

➤ [Index](#Index)

## Python as data management

The system needs to handle a lot of information constantly, therefore, we have chosen the Python programming language as the main development language. Python is an interpreted language, slower than others, like C ++, but you only need one interpreter to run it, which makes it cross-platform. In addition, it comes pre-installed in many systems like Linux or Mac.
It is multi-paradigm, unlike other languages ​​such as [R](https://www.r-project.org/), can be oriented to different needs, such as object-oriented programming, modular development, functional programming and scripts. These scripts can be used for system administration tasks, tests, correction of errors and direct interaction with the database, among other usefull uses.

It is opensource and is supported by a large community that continues to develop libraries and modules that facilitate our work. Many of these
libraries are oriented to massive data computing ([Awesome Python](https://github.com/vinta/awesome-python)).

Python has a very broad and easy to abstractread syntax, similar to pseudocode. It allows to easily manipulate data in a table way.
It is not necessary to declare the type of a variable, depending on the content that a variable takes, it is of one type or another, this gives more flexibility when it comes to processing differenabstractt types of data.

### Python 2.x vs 3.x

Both versions are incompatible, so we have chosen version 3.x for the development because it is the most recent version (3.6 2016) compared to
the latest version 2.x (2.7 2010), which will also no longer have support next year.
Most of the 2.x libraries are already available in 3.x, in the following [link](https://python3wos.appspot.com/) we can see some of those that are not available in red color.

➤ [Index](#Index)

<a name="Using-Personas"/>

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

➤ [Index](#Index)

## Database

The industry started to store data in relational databases like SQL (in 1970 by IBM) and in human readable tables like Excell (in 1985 by Microsoft).
Relational Databases use a ledger-style representation and come with a key feature. We can identify each piece of data using the primary key (sometimes auto-generated) and get relationships with other pieces using the foreign keys. 

In the current time, there has been a data explotion, petabytes and exabytes, known as Big Data. We can store it in disk, but, how we interact with all of this data? how we managment this big volume of primary and foreign keys? 
Although we continue to use them with the next versions, they are based on the initial scheme. So, these first tools are not suitable for these needs. But we still need to store all this information in a system where relationships play a crucial role. Innovation reappeared and databases based on graphs emerged.
 
## Graph Database

The base idea of graph database is that any data that we already know and store, already have a relational structure, and it is easy to be represented in graph way, like a social network.
The whiteboard model is the physical model, what you draw in the whiteboard to represent the data model, is represented on disk in the exact same way using graphs. What  perhaps  differentiates graphs from many other data modeling  techniques,  however,  is  the  close  affinity between the  logical  and  physical  models. The  interesting  thing  about  graph  diagrams  is  that  they  tend  to  contain specific instances  of nodes  and  relationships,  rather  than  classes  or  archetypes.

There are three dominant graph data models: the labeled  property  graph, hypergraphs (this model allows any number of nodes at either end of a relationship) and Resource Description Framework (RDF) triples by W3C.

For this project we will develop the labeled property graph. This model has the following characteristics:
+ It contains nodes, relationships, properties, and labels.
+ Nodes contain properties (key-value pairs).
+ Nodes can be labeled with one or more labels.
+ Relationships are named and directed, and always have a start and end node.
+ Relationships can also contain properties.

Let's make an example to understand the characteristics above:

In the next image we can see a graph with two nodes, one a "ingredient/food" type (label 0), and being more specific, the label 1 say us that is an "onion" object. The second object is a "nutrient" type (label 0), being more specific, it is a "vitamin" (label 1) with the name "C" (label 2). We have both nodes well defined with their labels and determinated properties. 

In terms of relationships, the object "onion" starts an edge that ends in "vitamin" "C" node with the relationship name "contains" with a value equeal to 19, that gives us the total amount of "vitamin" "C" in the onion object. Then, according to the assigned value we can know if the amount of vitamine C is important or significant, always according to the business logic.
The second relationship starts in zinq node and ends in apple node, it has the relationship name "make up", and gives us the certainty/relationship that zinq is part of the apple.

![Graph example](https://github.com/Stance4Health-Dev/docs/blob/master/img/graph-example.png)

### Use cases/goals when devs want evaluate databases:

- Flexibility: Mean a way to create and maintain your data in a logical wey.  No just translation from code into database calls, also translation between the business logic describing the applications requirements,
and the developers satisfyong those requeriments. The  flexibility  of  the  graph  model  allow  us  to  add  new nodes and new relationships without compromising the existing network or migrating data from the original data and its intent remain intact.
Because of the graph model’s flexibility, we don’t have to model our domain in exhaustive detail ahead of time a practice that is all but foolhardy in the face of changing business requirements. The additive nature of graphs also means we tend to perform fewer migrations, thereby
reducing maintenance overhead and risk.

- Perfomance: In contrast to relational databases, where join-intensive query performance deteriorates as the dataset gets bigger, with a graph database performance tends to remain relatively constant, even as the dataset grows. 
This is because queries are localized to a portion of the graph. As a result, the execution time for each query is proportional only to the size of the part of the graph traversed to satisfy that query,
rather than the size of the overall graph.

- Agility: they are schema free, graph databases lack the kind of schema-oriented data governance mechanisms we’re familiar with in the relational world. But this is not a risk, rather, 
it calls forth a far more visible and actionable kind of governance. Agility is another measure of speed. How easy and quickly can your code adapt to changing business? graph databases 
are in step with changing business environments.

## Native graph technology

### Native graph storage
Some graph databases use native graph storage that is optimized and designed for storing and managing graphs. The benefit of native graph storage is that its purpose-built stack 
is engineered for performance and scalability. Unlike non-native  graph  storage, it  typically  depends  on  a  mature  non-graph  backend  (such  as  MySQL) whose  production  
characteristics  are  well  understood  by  common operations teams. This non-native approach leads to latent results as their storage layer is not optimized for graphs. 

### Native graph processing
Others graph databases use index-free adjacency, meaning that connected nodes physically “point” to each other in the database. Native  graph  processing  (index-free  adjacency) 
benefits  traversal  performance,  but  at  the  expense  of  making  some queries that don’t use traversals difficult or memory intensive.
In common databases, traversing  the  graphs remains  expensive,  because  each  operation (Create, Read, Update, and Delete - CRUD) requires  an  index  lookup.  This  is  because  aggregates (like in SQL)  have  no notion of locality,  unlike  graph  databases,  which  naturally  provide the index-free adjacency. This  substantial  cost  is  amplified  when  it  comes  to  traversing  deeper than  just  one hop/search. Friends are easy enough, but imagine trying to compute in real time friends-of-friends(depth 2), or friends-of-friends-of-friends(depth 3). 
It will be slow because of the number of index lookups involved. Again, graphs use index-free adjacency to ensure that traversing connected data is extremely rapid.
Graph databases can carry out a series of operations, Create, Read, Update, and Delete (CRUD) methods that expose the graph data model.

#### How the performance of traversing changes with the size of the dataset
A graph database provides a constant order search for queries. In our case, we simply find the node in the graph that represents the object "apple" that is an "ingredient"/"food" type, and then we follow the incoming 
nutrient relationships, these relationships lead to nodes that represent "nutrient" that "make up" the object "apple".
This is far cheaper than brute-forcing the result because it considers far fewer members of the network, that is, it considers only those that are connected to "apple". Of course, if all nutrients make up the "apple" object, 
we’ll still end up considering the entire dataset.

Ex. Finding extended friends in a relational database versus efficient finding in Neo4j. Source: [Graph Databases, OReilly](https://www.oreilly.com/library/view/graph-databases/9781449356255/)

| Depth | DBMS exec time | Neo4j exec time | Dataset |
|-------|-----------------|-----------------|---------|
| 2     | 0.016           | 0.01            | ~2500   |   
| 3     | 30.267          | 0.168           | ~110000 |   
| 4     | 1543.505        | 1.359           | ~600000 |   
| 5     | Unfinished      | 2.132           | ~800000 |  

### Query language      
Diagrams are great for describing graphs outside of any technology context, but when it comes to using a database,  we  need  some  other  mechanism  for  creating,  manipulating,  and  querying data. We need a query language.
The two main paradigms of database query languages are imperative and declarative languages.

#### Imperative Query Languages
Imperative query languages are used to describe how you want something done specifically. Step-by step manner, the sequence and wording of each line of code plays a critical role.
imperative database query languages can also be limiting and not very user-friendly, requiring an extensive knowledge of the language and deep technical understanding of physical 
implementation details prior to usage. Writing one part incorrectly creates faulty outcomes.
Example: Gremlin, GraphQL (Neo4J-GraphQL integration Simplifying Data-Intensive Development 2019)    

#### Declarative Query Languages
Declarative query languages let users express what data to retrieve, letting the engine underneath take care of seamlessly retrieving it, rather than the specifics on how to complete it.
Using a declarative database query language may also result in better code than what can be created manually, and it is usually easier to understand the purpose of the code written in a declarative language.
Example: Cypher(Neo4j), Gremlin

### Database objects
The objects/nodes of the graph represent the real world objects that we want to digitize and store. 
For our feed database we distinguish the following basic objects:

Menu Object: set of recipes that together form a menu. 

| Labels | Properties                                     |
|--------|------------------------------------------------|
| Menu   | Name: menu_name                                |
|        | Type: [breakfast, lunch, snack, dinner, other] |
|        | Price aprox: _ €                               |


Recipe object: is a tutorial with a set of ingredients and properties that make up a recipe.

| Labels      | Properties        |
|-------------|-------------------|
| Recipe      | Name: recipe_name |
| Recipe_name | Tutorial: string  |
|             | Cooking time: min |
|             | Country: _        |


Ingredient object: it is the food itself. Any product of the supermarket, anything that is attributed to nutritional values is considered an ingredient/food.

| Labels                          | Properties                |
|---------------------------------|---------------------------|
| Ingredient/food_product         | Energy: _ kcal            |
| Ingredient_name/commercial_name | cholesterol: _ mg         |
|                                 | Unit: _                   |
|                                 | Quantity: _                 |
|                                 | State: [solid,liquid,gas] |
|                                 | Alcohol: _ mg             |

Nutrient object: There are many types and variants of nutrients, but we are not going to break down nutrients into more atomic components. 

| Labels                         | Properties |
|--------------------------------|------------|
| Nutrient                       | Unit:_     |
| Nutrient_type (nutrients_type.txt) | Source:_   |
| Nutrient_name                  |            |

Aditive object: Non-nutritive contribution. There are many types and variants of aditives.

| Labels                           | Properties |
|----------------------------------|------------|
| Aditive                          | Unit:_     |
| Aditive_type(aditives-types.txt) | Source:_   |
| Aditive_name                     |            |

The properties of each object above are not definitive, you can eliminate and add new properties without interfering with the operation of the graph. This 
leaves us open a wide range of possibilities and variants within the same database.

Lists of different types of data:
+ aditives.txt
+ nutrients.txt
+ vitamins.txt
+ minerals.txt
+ aminoacids.txt
+ fatty-acids-saturated.txt
+ fatty-acids-unsatured.txt
+ countries.txt

### Database relationships
The relational edges represent the relationship between the objects/nodes.
For our feed database we distinguish the following basic relationship labels:

| Labels  | Meaning                          |
|---------|----------------------------------|
| Contain | Carry or have [something] inside |
| Compose | Be part of something             |
| . . .   | . . .                            |

These labels are what allow us to traverse the graph respecting the coherence and logic of the business. More labels are 
added to the list as new relationships appear, the inclusion of new objects fosters new relationships.


#### Improving relationships
[Probabilistic Label Relation Graphs with Ising Models](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Ding_Probabilistic_Label_Relation_ICCV_2015_paper.pdf)
> Developing

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


➤ [Index](#Index)


## References
- https://www.fda.gov/Food/IngredientsPackagingLabeling/FoodAdditivesIngredients/ucm094211.htm
- https://neo4j.com/news/graphql-neo4j-grand-stack/
- https://neo4j.com/blog/imperative-vs-declarative-query-languages/
- https://neo4j.com/blog/native-vs-non-native-graph-technology/
- [Graph Databases Book, OReilly](https://www.oreilly.com/library/view/graph-databases/9781449356255/)