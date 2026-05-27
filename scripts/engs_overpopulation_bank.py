# -*- coding: utf-8 -*-
"""Lec 5.1 Overpopulation — 23 MCQ/T-F items (matches LO5W / LO5A deck size)."""
from __future__ import annotations

QUESTIONS_PER_TOPIC = 23

L51 = "CvSU ENGS 32 — Lec 5.1 Overpopulation (PDF)"
L51_SHORT = "CvSU Lec 5.1 — Overpopulation"
PSA = ["Philippine Statistics Authority (cited in lecture)"]


def _mcq(
    n: int,
    text: str,
    opts: tuple[str, str, str, str],
    ans: str,
    expl: str,
    refs: list[str],
) -> dict:
    letters = ["a", "b", "c", "d"]
    return {
        "id": f"lo5o-{n:02d}",
        "lo": "LO5O",
        "level": "Analysis",
        "type": "mcq",
        "text": text,
        "choices": [{"ltr": letters[i], "text": opts[i]} for i in range(4)],
        "ans": ans,
        "expl": expl,
        "refs": refs,
    }


def _tf(n: int, text: str, ans: bool, expl: str, refs: list[str]) -> dict:
    return {
        "id": f"lo5o-{n:02d}",
        "lo": "LO5O",
        "level": "Analysis",
        "type": "tf",
        "text": text,
        "ans": ans,
        "expl": expl,
        "refs": refs,
    }


def overpopulation_bank() -> list[dict]:
    return [
        _mcq(
            1,
            "Per Lec 5.1, unchecked population growth most directly intensifies which environmental pressure bundle?",
            (
                "Higher demand for food and fiber plus more pollution, waste, and ecosystem degradation",
                "Exclusive reduction of urban air pollutants without resource demand",
                "Elimination of survival-driven human behavior toward the environment",
                "Guaranteed stabilization of pest and disease rates in dense cities",
            ),
            "a",
            "Correct (a): slides link more people to resource demand and pollution/waste/degradation. (b)–(d) contradict the lecture chain.",
            [L51, L51_SHORT],
        ),
        _mcq(
            2,
            "In population ecology (Lec 5.1), a population is defined as:",
            (
                "Any mixed-species assemblage in a biome regardless of place or time",
                "A group of interacting individuals of the same kind in the same place at the same time",
                "Only humans enumerated in a national census year",
                "The total biomass of producers minus consumers in a food web",
            ),
            "b",
            "Correct (b): matches the lecture definition (same kind, place, time). (a) drops species identity. (c) narrows to humans only. (d) is ecosystem metabolism, not population ecology.",
            [L51, L51_SHORT],
        ),
        _mcq(
            3,
            "A population with a large proportion of young individuals relative to adults is characterized in the slides as:",
            (
                "A declining population",
                "A stable population",
                "A growing population",
                "A population with zero natality",
            ),
            "c",
            "Correct (c): age-structure slide labels many young → growing population. (a) is the opposite pattern. (b) requires young ≈ adults. (d) denies births.",
            [L51, L51_SHORT],
        ),
        _mcq(
            4,
            "Absolute population density in Lec 5.1 refers to:",
            (
                "The number of individuals in relation to all other species in the community",
                "The actual count of individuals per unit area (per unit time in the definition)",
                "Only the crude birth rate per 1,000 persons",
                "The logistic carrying capacity K exclusively",
            ),
            "b",
            "Correct (b): absolute density = actual count. (a) defines relative density. (c) is a vital rate. (d) is a model parameter, not the density definition.",
            [L51, L51_SHORT],
        ),
        _tf(
            5,
            "Per Lec 5.1, high population density can increase crowding, competition, mortality, and pest or disease pressure.",
            True,
            "TRUE: lecture lists crowding, inconvenience, competition, retarded growth, increased mortality, and rapid pest/disease increase under high density. FALSE would deny documented density effects.",
            [L51, L51_SHORT],
        ),
        _mcq(
            6,
            "Low population density in the lecture is associated with which outcome pairing?",
            (
                "Larger individuals and increased reproduction with more available resources",
                "Mandatory exponential growth with unlimited resources forever",
                "Zero survivorship at all age classes",
                "Uniform spatial distribution only in urban NCR",
            ),
            "a",
            "Correct (a): low-density slide bullets. (b) misstates growth models. (c) contradicts survivorship concept. (d) confuses spatial pattern with density effects.",
            [L51, L51_SHORT],
        ),
        _mcq(
            7,
            "Which method for estimating density of mobile animals is named in Lec 5.1?",
            (
                "Capture-recapture",
                "Nephelometric turbidity standardization",
                "Biochemical oxygen demand proxy",
                "Ice–albedo positive feedback",
            ),
            "a",
            "Correct (a): capture-recapture listed with census and sampling. (b)–(d) belong to water quality or climate topics.",
            [L51, L51_SHORT],
        ),
        _mcq(
            8,
            "According to Lec 5.1 (2020 PSA figure cited), Manila’s population density is approximately:",
            (
                "363 persons per square kilometer (national average)",
                "73,920 persons per square kilometer",
                "2,847 persons per square kilometer (provincial Cavite figure)",
                "109 persons per square kilometer (MIMAROPA regional figure)",
            ),
            "b",
            "Correct (b): slide cites Manila as most densely populated city at 73,920 persons/km² (2020, PSA). (a) is national density. (c) is Cavite province. (d) is MIMAROPA.",
            [L51, L51_SHORT, *PSA],
        ),
        _mcq(
            9,
            "Spatial distribution patterns enumerated in Lec 5.1 include:",
            (
                "Random, uniform (regular), and clumped (aggregated)",
                "Only circadian and tidal rhythms",
                "Exponential, logistic, and carrying-capacity only",
                "Point source, non-point source, and leachate",
            ),
            "a",
            "Correct (a): spatial distribution trio from population ecology slides. (b) is temporal distribution. (c) names growth curves. (d) is pollution-source taxonomy.",
            [L51, L51_SHORT],
        ),
        _mcq(
            10,
            "Natality as taught in Lec 5.1 is best described as:",
            (
                "Production of new individuals by birth, hatching, germination, or cloning",
                "The percentage of individuals surviving to each age class",
                "Number of deaths per 1,000 population per year only",
                "Physical inability to reproduce under any circumstances",
            ),
            "a",
            "Correct (a): natality definition on slides. (b) is survivorship. (c) is mortality framing. (d) confuses fecundity limits with natality.",
            [L51, L51_SHORT],
        ),
        _mcq(
            11,
            "Fecundity versus fertility in Lec 5.1 is distinguished as:",
            (
                "Fecundity = physical ability to reproduce; fertility = actual offspring produced",
                "Fecundity = deaths per unit time; fertility = immigration rate",
                "Both terms mean identical census counts",
                "Fecundity = life span; fertility = life expectancy",
            ),
            "a",
            "Correct (a): slide pairing. (b) mislabels vital rates. (c) collapses distinct concepts. (d) mixes longevity metrics.",
            [L51, L51_SHORT],
        ),
        _mcq(
            12,
            "Crude birth rate in the lecture is defined as:",
            (
                "Number of born individuals per 1,000 individuals at a given time",
                "Number of individuals per square kilometer only",
                "Intrinsic rate r in the logistic equation exclusively",
                "Years an individual is expected to continue living at a given age",
            ),
            "a",
            "Correct (a): crude birth rate per 1,000. (b) is density. (c) is growth-rate parameter. (d) is life expectancy.",
            [L51, L51_SHORT],
        ),
        _tf(
            13,
            "Per Lec 5.1, exponential (geometric) population growth is density-independent and can produce a J-shaped curve when resources are effectively unlimited for a short period.",
            True,
            "TRUE: slides state dN/dt = rN under stable/unlimited conditions with J-shaped pattern; logistic growth is density-dependent. FALSE would swap model properties.",
            [L51, L51_SHORT],
        ),
        _mcq(
            14,
            "Logistic population growth in Lec 5.1 is characterized by:",
            (
                "dN/dt = rN with no upper limit ever",
                "dN/dt = rN(K − N)/K, slowing as density approaches carrying capacity K",
                "Zero mortality at all ages",
                "Only temporal distribution (circadian) patterns",
            ),
            "b",
            "Correct (b): logistic equation and density-dependent slowdown in slides. (a) is exponential form. (c) is unrealistic. (d) is unrelated.",
            [L51, L51_SHORT],
        ),
        _mcq(
            15,
            "In the squirrel example (Lec 5.1), N₀ = 500 in 2023 with r = 2.5% per year, N₂₀ in 2043 is approximately:",
            (
                "350 units",
                "500 units",
                "824 units",
                "1,411 million units",
            ),
            "c",
            "Correct (c): slide calculation N₂₀ = 500·e^(0.025×20) ≈ 824. (a) is the backward-projection starting population in the second example. (b) ignores growth. (d) confuses with national population ranks.",
            [L51, L51_SHORT],
        ),
        _mcq(
            16,
            "When population drops from 500 to 350 over five years in the lecture’s reverse example, the implied annual growth rate r is about:",
            (
                "2.5%",
                "0.94%",
                "7.1%",
                "50%",
            ),
            "c",
            "Correct (c): slide solves ln(350/500) = −5r → r ≈ 0.071 (7.1%). (a) is the forward squirrel rate. (b) is world growth cited elsewhere. (d) is a doubling-time misread.",
            [L51, L51_SHORT],
        ),
        _mcq(
            17,
            "World population figures in Lec 5.1 (April 2023) include approximately:",
            (
                "7.9 billion people with an estimated growth rate near 0.94%",
                "3.0 billion people with 7.1% annual growth",
                "114.1 million people ranking first globally",
                "76.5 million people as the 2026 UN median",
            ),
            "a",
            "Correct (a): ~7.9B and 0.94% growth from slides. (b) misstates scale/rate. (c) is Philippines-scale. (d) is an older PH baseline year.",
            [L51, L51_SHORT],
        ),
        _mcq(
            18,
            "In the 2018 country ranking slide, the Philippines is listed at rank 12 with a population of about:",
            (
                "110,560,241",
                "1,411,750,000",
                "334,674,000",
                "73,920",
            ),
            "a",
            "Correct (a): PH row in lecture table. (b) is China. (c) is United States. (d) is Manila density, not national population.",
            [L51, L51_SHORT],
        ),
        _mcq(
            19,
            "Top three regions by population size in the 2020 census (Lec 5.1) are:",
            (
                "CALABARZON, National Capital Region, and Central Luzon",
                "BARMM, MIMAROPA, and CAR only",
                "Western Visayas, Ilocos, and Batanes exclusively",
                "China, India, and Indonesia within the Philippines",
            ),
            "a",
            "Correct (a): CALABARZON (16.2M), NCR, Central Luzon named as top three. (b) lists sparse regions. (c) is incomplete. (d) confuses countries with regions.",
            [L51, L51_SHORT, *PSA],
        ),
        _tf(
            20,
            "If the Philippine annual population growth rate remains near 1.47% (2023 figure in lecture), the slides estimate doubling in roughly 47 years.",
            True,
            "TRUE: lecture states ~47 years to double at 1.47%. FALSE would contradict the stated doubling-time pedagogy.",
            [L51, L51_SHORT, *PSA],
        ),
        _mcq(
            21,
            "National population density in Lec 5.1 is given as about 363 persons/km², while NCR’s density is about:",
            (
                "21,765 persons/km²",
                "977 persons/km²",
                "93 persons/km²",
                "73,920 persons/km²",
            ),
            "a",
            "Correct (a): NCR = 21,765 vs national 363 in slides. (b) is CALABARZON. (c) is Batanes sparsity. (d) is Manila city metric.",
            [L51, L51_SHORT, *PSA],
        ),
        _mcq(
            22,
            "Average Filipino household size in Lec 5.1 declined to about _____ in 2020 from 5.07 persons in 1995.",
            (
                "4.1 persons",
                "5.9 persons",
                "7.9 persons",
                "1.63 persons",
            ),
            "a",
            "Correct (a): 4.1 persons average household (2020). (b) is BARMM largest regional average. (c) confuses with world population billions. (d) is a growth-rate figure.",
            [L51, L51_SHORT, *PSA],
        ),
        _mcq(
            23,
            "Integrated lesson from Lec 5.1: the Philippines holding many of the world’s densest cities implies that local environmental crises (pollution, waste, habitat pressure) are amplified because:",
            (
                "High human density concentrates resource demand and waste generation on limited land",
                "Population density automatically eliminates disease and pest outbreaks",
                "Logistic growth never applies to urban populations",
                "Natality and mortality cease to affect age structure in cities",
            ),
            "a",
            "Correct (a): ties density effects to the syllabus arc toward pollution and waste topics. (b)–(d) contradict lecture ecology and demography.",
            [L51, L51_SHORT],
        ),
    ]


def all_overpopulation_questions() -> list[dict]:
    bank = overpopulation_bank()
    assert len(bank) == QUESTIONS_PER_TOPIC, len(bank)
    texts = [q["text"].strip().lower() for q in bank]
    assert len(texts) == len(set(texts)), "duplicate stems in overpopulation bank"
    return bank
