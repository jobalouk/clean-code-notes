*J'ai volontairement converti les exemples en python*

# Noms

## Choisir des noms révélateurs des intentions

Le nom d’une variable, d’une fonction ou d’une classe doit répondre à certaines grandes questions :

**La raison de son existence, son rôle et son utilisation.**

```python
d # Temps écoulé en jours.
```

Le nom `d` ne révèle rien

```python
  elapsed_time_in_days: int
  days_since_creation: int
  days_since_modification: int
  file_age_in_days: int
```


Mauvais exemple
```python
def get_item() -> List[int]:
  list1: List[int] = []
  for x in the_list:
    if x[0] == 4:
      list1.add(x)
      return list1
```


Le code devrait répondre à ces questions :

1. Quelles sortes de choses trouve-t-on dans `the_list` ?
2. Quelle est la signification de l’indice zéro sur un élément de `the_list` ?
3. Quelle est la signification de la valeur 4 ?
4. Comment dois-je utiliser la liste retournée


En supposant que l’on travail sur un jeu de démineur

Exemple plus sympas
```python
def get_flagged_cells() -> List[int]:
  flagged_cells: List[int] = []
  for x in game_board:
    if cell[STATUS_VALUE] == FLAGGED:
      flagged_cells.append(cell)
  return flagged_cells
```


Exemple tip top
```python
def get_flagged_cells() -> List[int]:
  flagged_cells: List[int] = []
  cell: Cell
  for cell in game_board:
    if cell.is_flagged():
      flagged_cells.append(cell)
  return flagged_cells
```
Avec une classe pour les cellules on peut cacher les constantes magiques et ajouter une fonction révélatrice des intentions.


## Éviter la désinformation
Pour faire réf à un groupe de compte nommer la variable `account_list` uniquement si il s'agit bien d'une liste.

Ne pas choisir de nom trop proche :\
`XYZ_controlle_for_efficient_handling_of_strings` et `XYZ_controller_for_efficient_storage_of_strings`


## Faire des distinction significative
Il ne suffit pas d'ajouter des numéros ou des mots parasites. Si des noms doivent être différents alors doivent\
représenter également des choses différentes.


```python
  def cop_chars(a1, a2):
    for in in range(len(a1)):
      a2[i] = a1[i]
  }
}
```
Cette fonction serait beaucoup lisible si les args se nommaient `source` et `destination`.

Autres exemples :

`ProductInfo` et `ProductData`
Vous avez choisi des noms différents sans qu’ils représentent quelque chose de différent.\
Info et Data sont des mots parasites vagues.


## Choisir des noms prononcable

Du mal à avoir besoin d'exemple pour ça tellement cela parait évident.


## Choisir des noms compatibles avec une recherche

Les noms d’une seule lettre et les constantes numériques présentent un problème parti-\
culier en cela qu’ils sont des éléments difficiles à localiser dans le corps d’un texte.

Les noms d'une seule lettre ne doivent être utilisé dans un scope local\
*La longueur d’un nom doit correspondre à la taille de sa portée*


On comprend rien, c'est chiant
```python
for i in range(34):
  s += t[i] * 4 / 5
```

On prend du plaisir là
```python
real_days_per_ideal_day = 4
WORK_DAYS_PER_WEEK = 5
sum = 0
for i in range(NUMBER_OF_TASKS):
  real_task_days = task_estimate[i] * real_days_per_ideal_day
  real_task_weeks = real_days / WORK_DAYS_PER_WEEK
  sum += real_task_weeks
```


## Interface et implémentations
Codifier l'implémentation pas la factory :\
on ne veut pas que l'utilisateur sache qu'il passe par une interface, juste que la factory existe.


## Éviter les associations mentales
Le lecteur ne doit pas avoir à convertir mentalement vos noms en noms qu’il connaît déjà.

Le programmeur intelligent comprends que la clarté prime. Les professionnels emploient leurs facultés\
à bon escient et écrivent du code que les autres sont en mesure de comprendre.


## Noms des classes
Pour les classes et les objets, nous devons choisir des noms ou des groupes nominaux comme\
`Customer`, `WikiPage`, `AddressParser`\
Un nom de classe ne doit pas être un verbe.


## Noms de méthodes
Pour les méthodes ont doit choisir des verbes ou des groupes verbaux comme `post_payment`, `delete_page` ou `save`.\
Les accesseurs, les mutateurs et les prédicats doivent être nommés d’après leur valeur et préfixés par `get`, `set` ou `is`.

Lorsque des constructeurs sont surchargés, nous devons utiliser des méthodes de fabri-\
que statiques avec des noms qui décrivent les arguments. Par exemple,

`complex: Complex = Complex.from_real_number(23.0)`
Pour imposer l’emploi de ces méthodes de fabrique, les constructeurs correspondants\
doivent être rendus privés.


## Choisir un mot par concept
Déroutant d'avoir `fetch`, `retrieve` et `get` ou `controller`, `manager` et `driver` par exemple


## Éviter les jeux de mots
Vous devez éviter d’employer le même mot dans deux sens différents. Si vous utilisez\
le même terme pour deux idées différentes, il s’agit d’un jeu de mots.

Dans une classe utiliser `add` pour créer une nouvelle valeur ou en concaténant deux valeurs\
existantes et dans une autre classe utilisé `add` pour mettre un paramètre dans une collection,\
doit-on appeler cette méthode `add` ?\
C'est mieux d'utiliser un mot comme `insert` ou `append`.


## Choisir des noms dans le domaine de la solution
Ne pas hésiter à utiliser des termes techniques.\
Utiliser des termes liés au domaine du problème pourrait obliger à se tourner vers le client.


## Choisir des noms dan le domaine du problème
Lorsqu’il n’existe aucun terme informatique pour ce que vous faites, utilisez le nom\
issu du domaine du problème.

Separation of concern
SOLUTION / PROBLÈME

Le code qui est fortement lié aux concepts du domaine du problème doit employer des noms tirés de ce domaine.


## Ajouter un contexte significatif
Pour `first_name`, `last_name`, `street`, `house_number`, `city`, `state`, `zip_code`

Ajouter
`addr_first_name`, `add_last_name`, ...

On comprendra que ça fait parti d'une structure plus vaste.

Une meilleur solution reste de créer une classe `Address`

### Variable dans un contexte flou
Il faut lire la fonction pour comprendre que les trois variables font parties\
de `guess_message`. Le contexte doit être déduit :

```python
def print_guess_statitics(candidate: str, count: int):
  number: str
  verb: str
  plural_modifier str

  if count == 0:
    number = 'no'
    verb = 'are'
    pluralModifier = 's'
  elif count == 1:
    number = '1'
    verb = 'is'
    pluralModifier = '
  else:
    number = str(count)
    verb = 'are'
    pluralModifier = 's'

  guess_message = f'There {verb} {number} {candidate} {plural_modifier}'

  print(guess_message)
```

Améliorer le contexte avec une classe :
```python
class GuessStatisticsMessage:
  number: str
  verb: str
  plural_modifier: str

  def make(self, candidate: str, count: int):
    self.create_plural_dependent_message_parts(count)
    return f'There {self.verb} {self.number} {candidate} {self.plural_modifier}'

  def create_plural_dependent_message_parts(self, count):
    if count == 0:
      self.there_are_no_letters()
    elif count == 1:
      self.there_is_one_letter()
    else:
      self.there_are_many_letters(count)

  def there_are_many_letters(self, count):
    self.number = str(count)
    self.verb = 'are'
    self.plural_modifier = 's'

  def there_is_one_letter(self):
    self.number = 1
    self.verb = 'is'
    self.plural_modifier = ''

  def there_are_no_letters(self):
    self.number = 'no'
    self.verb = 'are'
    self.plural_modifier = 's'
```

## Ne pas ajouter de contexte inutile
Dans une application fictive appelée "Gas Station Deluxe" (station-service de luxe), il\
est déconseillé de préfixer chaque classe par GSD.

Les noms `accountAddress` et `customerAddress` sont parfaits pour des instances de la\
classe `Address`, mais ils font de piètres noms de classes.

Ajouter un contexte à `Address` si on en a besoin : `PostalAddress`.


# Fonctions

## Faire court
La première règle est d’écrire des fonctions courtes. La deuxième règle est qu’elles\
doivent être encore plus courtes que cela.


## Blocs et indentation
Les blocs des instructions if, des instructions else, des instructions while, etc. ne doivent occuper qu’une seule ligne.\
Le niveau d’indentation d’une fonction ne doit donc pas être supérieur à un ou deux.


## Faire une seule chose
"Une fonction doit faire une seule  chose. Elle doit le faire bien et ne faire qu'elle"

```python
def render_page_with_setups_and_teardowns(page_data, is_suite):
  if is_test_page(page_data):
    include_setup_and_tear_down_pages(page_data, is_suite)
  return page_data.get_html()
```

Description de la fonction :\
POUR générer une page qui comprend un montage et un démontage (
render_page_with_setups_and_teardowns), nous vérifions que la page est une
page de test et, dans l’affirmative, nous incluons les pages de montage et de
démontage. Dans tous les cas, nous présentons la page en HTML.

Lorsqu'une fonction met en oeuvre des étapes qui se trouvent à un seul niveau sous son nom, la fonction\
réalise une seule chose.

Déterminer s’il est possible d’en extraire une autre fonction dont le nom n’est\
pas simplement une reformulation de son implémentation.


### Section à l'intérieur des fonctions
Une fonction qui ne fait qu'une seule chose ne peut pas être découpé en section


## Un niveau d'abstraction par fonction
Mélanger les niveaux d'abstraction au sein d'une même fonction est déroutant.


### Lire le code de haut en bas : la régle de décroissance
Nous voulons que chaque fonction soit suivie des fonctions de niveau d’abstraction\
inférieure.

**Pour inclure les pages de montage et de démontage, nous incluons le
montage, puis le contenu de la page de test et enfin le démontage.

Pour inclure le montage, nous incluons le montage d’une suite s’il s’agit
d’une suite, puis nous incluons le montage normal.

Pour inclure le montage d’une suite, nous recherchons la page "SuiteSetUp"
dans la hiérarchie parente et nous incluons une instruction avec le chemin de
cette page.

Pour rechercher le parent...**


## Instruction switch (java)

## Arguments d’une fonction
