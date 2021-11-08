package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

type passport struct {
	byr string
	iyr string
	eyr string
	hgt string
	hcl string
	ecl string
	pid string
	cid string
}

func (p passport) isValid_1() bool {
	r := len(p.byr) > 0 && len(p.iyr) > 0 && len(p.eyr) > 0 && len(p.hgt) > 0 && len(p.hcl) > 0 && len(p.ecl) > 0 && len(p.pid) > 0
	return r
}

var hgtCmRegex = regexp.MustCompile(`(?P<hgt>\d+)cm`)
var hgtInRegex = regexp.MustCompile(`(?P<hgt>\d+)in`)
var hclValidRegex = regexp.MustCompile(`(?P<hcl>#[0-9a-f]{6})`)
var pidValidRegex = regexp.MustCompile(`^(?P<pid>\d{9})$`)

var validEcl = map[string]bool{
	"amb": true,
	"blu": true,
	"brn": true,
	"gry": true,
	"grn": true,
	"hzl": true,
	"oth": true,
}

func (p passport) isValid_2() bool {

	// byr (Birth Year) - four digits; at least 1920 and at most 2002.
	byr, _ := strconv.Atoi(p.byr)
	if 1920 > byr || byr > 2002 {
		return false
	}

	// iyr (Issue Year) - four digits; at least 2010 and at most 2020.
	iyr, _ := strconv.Atoi(p.iyr)
	if 2010 > iyr || iyr > 2020 {
		return false
	}

	// eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
	eyr, _ := strconv.Atoi(p.eyr)
	if 2020 > eyr || eyr > 2030 {
		return false
	}

	// hgt (Height) - a number followed by either cm or in:
	// If cm, the number must be at least 150 and at most 193.
	// If in, the number must be at least 59 and at most 76.
	match := hgtCmRegex.FindStringSubmatch(p.hgt)
	if len(match) > 0 {
		cm, _ := strconv.Atoi(match[1])
		if cm < 150 || cm > 193 {
			return false
		}
	} else {
		match = hgtInRegex.FindStringSubmatch(p.hgt)
		if len(match) > 0 {
			in, _ := strconv.Atoi(match[1])
			if in < 59 || in > 76 {
				return false
			}
		} else {
			return false
		}
	}

	//hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
	match = hclValidRegex.FindStringSubmatch(p.hcl)
	if len(match) == 0 {
		return false
	}

	// ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
	_, ok := validEcl[p.ecl]
	if !ok {
		return false
	}

	// pid (Passport ID) - a nine-digit number, including leading zeroes.
	match = pidValidRegex.FindStringSubmatch(p.pid)
	if len(match) == 0 {
		return false
	}

	// cid (Country ID) - ignored, missing or not.

	return true
}

var byrRegex = regexp.MustCompile(`byr:(?P<byr>\S+)`)
var iyrRegex = regexp.MustCompile(`iyr:(?P<iyr>\S+)`)
var eyrRegex = regexp.MustCompile(`eyr:(?P<eyr>\S+)`)
var hgtRegex = regexp.MustCompile(`hgt:(?P<hgt>\S+)`)
var hclRegex = regexp.MustCompile(`hcl:(?P<hcl>\S+)`)
var eclRegex = regexp.MustCompile(`ecl:(?P<ecl>\S+)`)
var pidRegex = regexp.MustCompile(`pid:(?P<pid>\S+)`)
var cidRegex = regexp.MustCompile(`cid:(?P<cid>\S+)`)

func build(s string) passport {

	match := byrRegex.FindStringSubmatch(s)
	byr := ""
	if len(match) > 0 {
		byr = match[1]
	}

	match = iyrRegex.FindStringSubmatch(s)
	iyr := ""
	if len(match) > 0 {
		iyr = match[1]
	}

	match = eyrRegex.FindStringSubmatch(s)
	eyr := ""
	if len(match) > 0 {
		eyr = match[1]
	}

	match = hgtRegex.FindStringSubmatch(s)
	hgt := ""
	if len(match) > 0 {
		hgt = match[1]
	}

	match = hclRegex.FindStringSubmatch(s)
	hcl := ""
	if len(match) > 0 {
		hcl = match[1]
	}

	match = eclRegex.FindStringSubmatch(s)
	ecl := ""
	if len(match) > 0 {
		ecl = match[1]
	}

	match = pidRegex.FindStringSubmatch(s)
	pid := ""
	if len(match) > 0 {
		pid = match[1]
	}

	match = cidRegex.FindStringSubmatch(s)
	cid := ""
	if len(match) > 0 {
		cid = match[1]
	}

	p := passport{
		byr: byr,
		iyr: iyr,
		eyr: eyr,
		hgt: hgt,
		hcl: hcl,
		ecl: ecl,
		pid: pid,
		cid: cid,
	}
	return p
}

func getInput(sample int) []passport {
	input := make([]string, 0)
	if sample == 1 {
		input = append(input, "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd")
		input = append(input, "byr:1937 iyr:2017 cid:147 hgt:183cm")
		input = append(input, "")
		input = append(input, "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884")
		input = append(input, "hcl:#cfa07d byr:1929")
		input = append(input, "")
		input = append(input, "hcl:#ae17e1 iyr:2013")
		input = append(input, "eyr:2024")
		input = append(input, "ecl:brn pid:760753108 byr:1931")
		input = append(input, "hgt:179cm")
		input = append(input, "")
		input = append(input, "hcl:#cfa07d eyr:2025 pid:166559648")
		input = append(input, "iyr:2011 ecl:brn hgt:59in")
	} else if sample == 2 {
		input = append(input, "eyr:1972 cid:100")
		input = append(input, "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926")
		input = append(input, "")
		input = append(input, "iyr:2019")
		input = append(input, "hcl:#602927 eyr:1967 hgt:170cm")
		input = append(input, "ecl:grn pid:012533040 byr:1946")
		input = append(input, "")
		input = append(input, "hcl:dab227 iyr:2012")
		input = append(input, "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277")
		input = append(input, "")
		input = append(input, "hgt:59cm ecl:zzz")
		input = append(input, "eyr:2038 hcl:74454a iyr:2023")
		input = append(input, "pid:3556412378 byr:2007")
	} else if sample == 3 {
		input = append(input, "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980")
		input = append(input, "hcl:#623a2f")
		input = append(input, "")
		input = append(input, "eyr:2029 ecl:blu cid:129 byr:1989")
		input = append(input, "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm")
		input = append(input, "")
		input = append(input, "hcl:#888785")
		input = append(input, "hgt:164cm byr:2001 iyr:2015 cid:88")
		input = append(input, "pid:545766238 ecl:hzl")
		input = append(input, "eyr:2022")
		input = append(input, "")
		input = append(input, "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719")
	} else {
		file, err := os.Open("input.txt")
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()

		scanner := bufio.NewScanner(file)

		for scanner.Scan() {
			input = append(input, scanner.Text())
		}
	}

	passports := make([]passport, 0)
	current := ""
	for _, s := range input {
		if s == "" {
			passports = append(passports, build(current))
			current = ""
		} else {
			current += " " + s
		}
	}
	passports = append(passports, build(current))
	return passports

}

func main() {
	passports := getInput(0)
	sum1 := 0
	for _, p := range passports {
		if p.isValid_1() {
			sum1++
		}
	}
	fmt.Printf("Valid 1: %d\n", sum1)

	sum2 := 0
	for _, p := range passports {
		if p.isValid_2() {
			sum2++
		}
	}
	fmt.Printf("Valid 2: %d\n", sum2)
}
