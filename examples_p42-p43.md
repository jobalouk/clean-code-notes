### Implementation de 3.4 p.42


```python
def calculate_pay(e: Employee) -> Optional[Money]:
    try:
        if e.type == COMMISSIONED:
            return calculate_commissioned_pay(e)
        elif e.type == HOURLY:
            return calculate_hourly_pay(e)
        elif e.type == SALARIED:
            return calculate_salaried_pay(e)
        else:
            return None
    raise InvalidEmployeeType('Invalid employee')
  ```



- Fonction longue et ne fera que grandir en ajoutant des nouveau types d'employés
- Elle prend en charge plusieurs choses
- Elle ne respecte pas le principe de responsabilité unique (SRP, Single Responsibility Principle)\
car il existe plusieurs raisons de la modifier
- Elle ne respecte pas le principe ouvert/fermé (OCP, Open closed format) ???

Mais son principal problème est sans doute qu’un nombre illimité d’autres fonctions auront la même structure :

```python
is_payday(e: Employee, date: Date)
```
```python
deliver_pay(e: Employee, Money: pay)
```


Solution : enfouir la logique dans une méthode de classe

### Implementation de 3.5 p.43

```python
class Pay:

  def __init__(self, record):
    self.record = record

  def is_payday(self):
    NotImplementedError

  def calculate_pay(self):
    NotImplementedError

  def delivery_pay(self):
    NotImplementedError
```


```python  
class Employee:

  def make(self, record: EmployeeRecord):
    if e.type == COMMISSIONED:
        return CommissionedEmployee(record=record)
    elif e.type == HOURLY:
        return HourlyEmployee(record=record)
    elif e.type == SALARIED:
        return SalariedEmploye(record=record)
    else:
        return None
```


```python
class CommissionedEmployee(Pay):
  def is_payday(self):
    self.record = record??
    # Instructions...

  def calculate_pay(self):
    # Instructions...

  def delivery_pay(self):
    # Instructions...
```

La même chose pour les autres classes
