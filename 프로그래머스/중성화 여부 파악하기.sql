SELECT ANIMAL_ID, NAME, if (SEX_UPON_INTAKE like '%Spayed%' or SEX_UPON_INTAKE like '%Neutered%', 'O', 'X' ) as '중성화'
from ANIMAL_INS
order by ANIMAL_ID
