package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type passport struct {
	byr bool
	iyr bool
	eyr bool
	hgt bool
	hcl bool
	ecl bool
	pid bool
	cid bool
}

func (p passport) isValid() bool {
	r := p.byr && p.iyr && p.eyr && p.hgt && p.hcl && p.ecl && p.pid
	return r
}

func build(s string) passport {
	byr := strings.Contains(s, "byr:")
	iyr := strings.Contains(s, "iyr:")
	eyr := strings.Contains(s, "eyr:")
	hgt := strings.Contains(s, "hgt:")
	hcl := strings.Contains(s, "hcl:")
	ecl := strings.Contains(s, "ecl:")
	pid := strings.Contains(s, "pid:")
	cid := strings.Contains(s, "cid:")

	return passport{
		byr: byr,
		iyr: iyr,
		eyr: eyr,
		hgt: hgt,
		hcl: hcl,
		ecl: ecl,
		pid: pid,
		cid: cid,
	}
}

func getInput(sample bool) []passport {
	input := make([]string, 0)
	if sample {
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
	passports := getInput(false)
	sum := 0
	for _, p := range passports {
		if p.isValid() {
			sum++
		}
	}
	fmt.Println(sum)
}
