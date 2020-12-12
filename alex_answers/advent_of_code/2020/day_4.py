from day_4_input import puzzle_input
from pydantic import BaseModel, ValidationError, validator
from typing import Optional, Literal
import re

puzzle_input = [{j.split(":")[0]: j.split(":")[1] for j in i.split()} for i in puzzle_input.strip().split("\n\n")]

class Passport(BaseModel):

    iyr: str
    byr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: Literal["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pid: str
    cid: Optional[str]

    @validator('hcl')
    def validate_hcl(cls, v):
        if not re.match("#([0-9]|[a-f]){6}", v):
            raise ValueError
        return v

    @validator('pid')
    def validate_pid(cls, v):
        if not len(v) == 9:
            raise ValueError
        return v

    @validator('iyr')
    def validate_iyr(cls, v):
        if len(v) != 4 or not (2010 <= int(v) <= 2020):
            raise ValueError
        return v


    @validator('byr')
    def validate_byr(cls, v):
        if len(v) != 4 or not (1920 <= int(v) <= 2002):
            raise ValueError
        return v

    @validator('eyr')
    def validate_eyr(cls, v):
        if len(v) != 4 or not (2020 <= int(v) <= 2030):
            raise ValueError
        return v

    @validator('hgt')
    def validate_hgt(cls, v):
        if 'in' in v:
            if not (59 <= int(v.replace('in', '')) <= 76):
                raise ValueError
            return v

        if not (150 <= int(v.replace('cm', '')) <= 193):
            raise ValueError
        return v


valid_count = 0

for passport_dict in puzzle_input:

    try:
        Passport(**passport_dict)
    except ValidationError as e:
        pass
    else:
        valid_count += 1

print(valid_count)